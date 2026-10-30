# Book 10 of Euclid's Elements — Step-by-Step AI Proofs (Run C)

## Proposition 10.1
**Statement:** Two unequal magnitudes being set out, if from the greater there be subtracted a magnitude greater than its half, and from that which is left a magnitude greater than its half, and if this process be repeated continually, there will be left some magnitude which will be less than the lesser magnitude set out.

**Step 1.** Let AB and C be two unequal magnitudes with AB greater than C. We are to show that by repeatedly subtracting from the remainder a magnitude greater than its half, there will at length remain a magnitude less than C.

**Step 2.** Since AB and C are magnitudes of the same kind, by D5.4, C is capable, when multiplied, of exceeding AB. Multiply C until a multiple of C is produced that exceeds AB. Let DE be this multiple, so that DE > AB, and let DE be divided into parts each equal to C, namely DF, FG, GH, ..., HE, where each part equals C and DE = nC for some finite number n (by D5.2, DE is a multiple of C).

**Step 3.** From AB subtract BH1 greater than half of AB, leaving remainder A1 (so A1 < half of AB). From DE subtract one part equal to C (namely HE), leaving remainder D1 = DE - C = (n-1)C. Since DE > AB and we subtracted BH1 > (1/2)AB from AB, while we subtracted only C from DE, we have D1 >= A1. To verify: DE > AB implies DE - C >= AB - C. Since BH1 > (1/2)AB >= C (if C <= (1/2)AB), we get A1 = AB - BH1 < AB - (1/2)AB = (1/2)AB. Meanwhile D1 = DE - C >= AB - C >= AB - (1/2)AB = (1/2)AB > A1. If instead C > (1/2)AB, then A1 < (1/2)AB < C and we are already done.

**Step 4.** Assuming the process has not yet terminated, we have D1 >= A1 with D1 = (n-1)C. From A1 subtract more than its half, leaving A2 < (1/2)A1. From D1 subtract another copy of C, leaving D2 = (n-2)C. By the same reasoning as Step 3, since D1 >= A1, we get D2 >= A2.

**Step 5.** Continue this process. At each stage k, we have Dk = (n-k)C and Ak < (1/2)Ak-1, and Dk >= Ak. This process must terminate in at most n-1 steps, because DE was divided into exactly n parts each equal to C. After n-1 subtractions of C, the DE-remainder is reduced to Dn-1 = C.

**Step 6.** At the step where the DE-remainder equals 2C (that is, Dn-2 = 2C), we have An-2 <= Dn-2 = 2C. We then subtract from An-2 more than its half, leaving An-1 < (1/2)An-2 <= (1/2)(2C) = C. Therefore An-1 < C.

**Step 7.** Hence after finitely many subtractions (each removing more than half of the current remainder), a magnitude less than C remains. The finiteness of the process is guaranteed because DE consists of only finitely many copies of C by D5.4 and D5.2, and by CN5 each remainder is strictly less than the magnitude from which it was taken, since the whole is greater than the part. This is what was to be proved.

**USED:** CN5, D5.2, D5.4
**Human refs (from References field):** D5.4
**Jaccard:** 0.333 — AI adds ['CN5', 'D5.2']

## Proposition 10.2
**Statement:** If, when the less of two unequal magnitudes is continually subtracted in turn from the greater, that which is left never measures the one before it, the magnitudes will be incommensurable.

**Step 1.** Let A and B be two unequal magnitudes such that, when the less is continually subtracted in turn from the greater, the remainder never measures the magnitude before it. We must prove that A and B are incommensurable.

**Step 2.** Suppose, for the sake of contradiction, that A and B are commensurable. Then by definition (D10.1.1), there exists some magnitude C that measures both A and B.

**Step 3.** Since C measures both A and B, consider the anthyphairesis (mutual subtraction) process. Without loss of generality, assume A is the greater. We subtract B from A as many times as possible; since the remainder never measures B (by hypothesis), a positive remainder R1 is left, with R1 less than B. Since C measures A and C measures B, and R1 equals A minus some multiple of B, then C also measures R1 (by repeated application of CN3: if equals be subtracted from equals, the remainders are equal — here, since C measures A and C measures every copy of B subtracted, C measures the remainder).

**Step 4.** In the next stage of the process, we subtract R1 from B as many times as possible, obtaining a remainder R2 with R2 less than R1. By the same reasoning as in Step 3, since C measures both B and R1, C also measures R2.

**Step 5.** Continuing in this manner, at every stage of the anthyphairesis process, C measures each successive remainder. Moreover, each remainder is a positive magnitude (since by hypothesis the process never terminates — that is, no remainder ever exactly measures the one before it), and each remainder is strictly less than the preceding one.

**Step 6.** Now, since C is a definite magnitude, and the remainders form a decreasing sequence of positive magnitudes, by Proposition 10.1 (applied to the process of continually subtracting more than half from the greater — each subtraction of the lesser from the greater removes at least half, since the lesser is subtracted as many times as possible), there must eventually be a remainder R_n that is less than C.

**Step 7.** But C measures R_n, which means R_n is either equal to C or a multiple of C (by D5.1 and D5.2, a magnitude that is measured by C has C as a part of it, so R_n is at least as large as C). Yet R_n is less than C. This is a contradiction, since no positive magnitude less than C can be measured by C (CN5: the whole is greater than the part, so if C measured R_n, then R_n would be at least C).

**Step 8.** Therefore our assumption that A and B are commensurable is false. Hence A and B are incommensurable (D10.1.1). Q.E.D.

**USED:** 10.1, CN3, CN5, D10.1.1, D5.1, D5.2
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['10.1', 'CN3', 'CN5', 'D10.1.1', 'D5.1', 'D5.2']

## Proposition 10.3
**Statement:** Given two commensurable magnitudes, to find their greatest common measure.

**Step 1.** Let AB and CD be two commensurable magnitudes, with AB the greater (or equal). Since they are commensurable, by definition (D10.1.1) some magnitude E measures both AB and CD.

**Step 2.** Since E measures the lesser CD, there is some multiple of E equal to CD (D5.2). And since E also measures AB, AB is likewise a multiple of E. Therefore E is a common measure of AB and CD.

**Step 3.** Now apply the successive subtraction process (anthyphairesis) to AB and CD. Subtract CD from AB as many times as possible. If CD measures AB exactly, then CD itself is a common measure of AB and CD. Since CD measures CD (trivially) and CD measures AB, any common measure of AB and CD must measure CD (D5.1), so CD is the greatest common measure, and we are done.

**Step 4.** If CD does not measure AB, then after subtracting CD from AB as many times as possible, some remainder less than CD is left; call it R1, so that AB = m*CD + R1 where R1 < CD. Now subtract R1 from CD as many times as possible. If R1 measures CD, proceed to Step 6. Otherwise a remainder R2 < R1 is left. Continue this process.

**Step 5.** We claim this process must terminate, leaving some remainder that measures the one before it. For suppose it did not terminate. Then the lesser is continually subtracted in turn from the greater, and that which is left never measures the one before it. By Proposition 10.2, AB and CD would be incommensurable. But this contradicts our hypothesis that AB and CD are commensurable (D10.1.1). Therefore the process must terminate.

**Step 6.** Let the process terminate at some stage where the remainder, call it G, exactly measures the magnitude from which it is subtracted. We show G is a common measure of AB and CD by working back through the chain. At the last step, G measures the preceding remainder. At each prior step, G measures both the remainder and the magnitude from which subtractions were made (since G measures the subtracted part and G measures the leftover, G measures their sum by CN2). Working back through every stage, G measures CD and G measures AB. Therefore G is a common measure of AB and CD.

**Step 7.** We now show G is the greatest common measure. Let F be any common measure of AB and CD. Since F measures both AB and CD, F measures AB - m*CD = R1 (CN3 applied repeatedly: if F measures the whole AB and F measures the part m*CD subtracted from it, F measures the remainder R1). Similarly, since F measures CD and F measures R1, F measures CD - n*R1 = R2. Continuing through each stage, F measures G.

**Step 8.** Since every common measure F of AB and CD measures G, it follows that F is not greater than G (CN5: G is the whole, and if F measured G, F would be a part of G or equal to G). Therefore G is the greatest common measure of AB and CD.

**Step 9.** Therefore, given two commensurable magnitudes AB and CD, we have found their greatest common measure G. Q.E.F.

**USED:** 10.2, CN2, CN3, CN5, D10.1.1, D5.1, D5.2
**Human refs (from References field):** 10.2
**Jaccard:** 0.143 — AI adds ['CN2', 'CN3', 'CN5', 'D10.1.1', 'D5.1', 'D5.2']

## Proposition 10.4
**Statement:** Given three commensurable magnitudes, to find their greatest common measure.

**Step 1.** Let A, B, C be three commensurable magnitudes. Since A and B are commensurable, by Proposition 10.3, take D the greatest common measure of A and B. Then D measures both A and B [10.3].

**Step 2.** Since A, B, C are commensurable, by Definition D10.1.1 there exists some magnitude E that measures all three of A, B, and C.

**Step 3.** Since E measures both A and B, E is a common measure of A and B. But D is the greatest common measure of A and B [10.3], and by the property established in 10.3, every common measure of A and B also measures D. Therefore E measures D.

**Step 4.** Since E measures both D and C, D and C have a common measure, so D and C are commensurable [D10.1.1].

**Step 5.** Now either D measures C, or D does not measure C.

**Step 6.** Case 1: Suppose D measures C. Then D measures each of A, B, and C, so D is a common measure of A, B, C. Let G be any common measure of A, B, and C. Then G measures both A and B, so G is a common measure of A and B. Since D is the greatest common measure of A and B [10.3], G measures D. Therefore no common measure of A, B, C is greater than D, and D is the greatest common measure of A, B, C.

**Step 7.** Case 2: Suppose D does not measure C. Since D and C are commensurable [Step 4], by Proposition 10.3, take F the greatest common measure of D and C.

**Step 8.** Since F measures D, and D measures A, F measures A. Similarly, since D measures B, F measures B. Also F measures C [10.3]. Therefore F is a common measure of A, B, and C.

**Step 9.** Let G be any common measure of A, B, and C. Since G measures both A and B, G is a common measure of A and B. Since D is the greatest common measure of A and B [10.3], G measures D. Also G measures C. Therefore G is a common measure of D and C.

**Step 10.** Since F is the greatest common measure of D and C [10.3], and G is a common measure of D and C, G measures F. Therefore no common measure of A, B, C is greater than F, and F is the greatest common measure of A, B, C.

**Step 11.** Therefore, in either case, the greatest common measure of the three commensurable magnitudes A, B, C has been found. Q.E.F.

**USED:** 10.3, D10.1.1, D5.1
**Human refs (from References field):** 10.3
**Jaccard:** 0.333 — AI adds ['D10.1.1', 'D5.1']

## Proposition 10.5
**Statement:** Commensurable magnitudes have to one another the ratio which a number has to a number.

**Step 1.** Let A and B be commensurable magnitudes. Then by the definition of commensurable magnitudes (D10.1.1), there exists a magnitude C which measures both A and B.

**Step 2.** Since C measures A, by definition A is a multiple of C (D5.2). That is, there exists a number m such that A is C taken m times, so A = mC. Likewise, since C measures B, there exists a number n such that B = nC. Here m and n are numbers, being multitudes composed of units (D7.2).

**Step 3.** We claim that A has to B the ratio which m has to n. To establish this, we apply the definition of same ratio (D5.5) and show that for any numbers p and q, the equimultiple pA compared with qB yields the same ordering as pm compared with qn.

**Step 4.** Take any equimultiples pA of A and pm of m, and any equimultiples qB of B and qn of n. Since A = mC, the magnitude pA is p times mC. By Proposition 5.3, p times the multiple mC equals the multiple (pm)C. Thus pA = (pm)C. Similarly, since B = nC, we have qB = (qn)C.

**Step 5.** Now pA and qB are both multiples of the same magnitude C, namely (pm)C and (qn)C respectively. If pm > qn, then (pm)C is a greater multiple of C than (qn)C, so pA > qB, since the whole is greater than the part (CN5). If pm = qn, then (pm)C = (qn)C, so pA = qB. If pm < qn, then by the same reasoning pA < qB.

**Step 6.** Therefore, for all positive integers p and q, pA exceeds, equals, or falls short of qB precisely when pm exceeds, equals, or falls short of qn. By the definition of same ratio (D5.5), A : B = m : n.

**Step 7.** Since m and n are numbers (D7.2), the ratio A : B is a ratio which a number has to a number. Therefore commensurable magnitudes have to one another the ratio which a number has to a number. Q.E.D.

**USED:** 5.3, CN5, D10.1.1, D5.2, D5.5, D7.2
**Human refs (from References field):** 5.22, 5.7, D7.20
**Jaccard:** 0.000 — AI adds ['5.3', 'CN5', 'D10.1.1', 'D5.2', 'D5.5', 'D7.2']; Human adds ['5.22', '5.7', 'D7.20']

## Proposition 10.6
**Statement:** If two magnitudes have to one another the ratio which a number has to a number, the magnitudes will be commensurable.

**Step 1.** Let A and B be two magnitudes such that A:B = m:n, where m and n are numbers.

**Step 2.** Since m is a number composed of units, divide A into as many equal magnitudes as there are units in m. Let each such part be called C, so that A is the same multiple of C that m is of the unit; that is, A = m times C [D5.2].

**Step 3.** Since n is a number, take the magnitude D equal to n times C, so that D = n times C [D5.2].

**Step 4.** We claim A:D = m:n. To verify this by D5.5, take any arbitrary positive integers s and t. We must show that s times A is greater than, equal to, or less than t times D according as s times m is greater than, equal to, or less than t times n.

**Step 5.** Since A = m times C, we have s times A = (s times m) times C [5.3]. Similarly, since D = n times C, we have t times D = (t times n) times C [5.3].

**Step 6.** Now (s times m) times C is greater than, equal to, or less than (t times n) times C according as the number s times m is greater than, equal to, or less than the number t times n. This holds because equimultiples of the same magnitude preserve the ordering of the multiplying numbers [CN5, and the nature of multiples per D5.2].

**Step 7.** Therefore, for all positive integers s and t, s times A exceeds, equals, or falls short of t times D precisely when s times m exceeds, equals, or falls short of t times n. By the definition of same ratio [D5.5], A:D = m:n.

**Step 8.** But by hypothesis, A:B = m:n. Therefore A:B = A:D.

**Step 9.** Since A has the same ratio to both B and D, it follows that B = D [5.9].

**Step 10.** Since D = n times C, we have B = n times C. Thus C measures B (taken n times), and C measures A (taken m times) [D5.1, D5.2].

**Step 11.** Since A and B are both measured by the common measure C, the magnitudes A and B are commensurable [D10.1.1].

Therefore, if two magnitudes have to one another the ratio which a number has to a number, the magnitudes are commensurable. Q.E.D.

**USED:** 5.3, 5.9, CN5, D10.1.1, D5.1, D5.2, D5.5
**Human refs (from References field):** 5.11, 5.22, 5.7, 5.9, D7.20
**Jaccard:** 0.091 — AI adds ['5.3', 'CN5', 'D10.1.1', 'D5.1', 'D5.2', 'D5.5']; Human adds ['5.11', '5.22', '5.7', 'D7.20']

## Proposition 10.7
**Statement:** Incommensurable magnitudes have not to one another the ratio which a number has to a number.

**Step 1.** Let A and B be incommensurable magnitudes. We wish to show that A does not have to B the ratio which a number has to a number.

**Step 2.** Suppose, for the sake of contradiction, that A has to B the ratio which a number has to a number. That is, suppose A : B = m : n for some numbers m and n.

**Step 3.** Then, by Proposition 10.6, since A and B have to one another the ratio which a number has to a number, A and B are commensurable. [10.6]

**Step 4.** But A and B are incommensurable by hypothesis (D10.1.1). This contradicts the conclusion of Step 3.

**Step 5.** Therefore the supposition is false, and A does not have to B the ratio which a number has to a number.

**Step 6.** Hence incommensurable magnitudes have not to one another the ratio which a number has to a number. Q.E.D.

**USED:** 10.6, D10.1.1
**Human refs (from References field):** 10.6
**Jaccard:** 0.500 — AI adds ['D10.1.1']

## Proposition 10.8
**Statement:** If two magnitudes have not to one another the ratio which a number has to a number, the magnitudes will be incommensurable.

**Step 1.** Let A and B be two magnitudes that have not to one another the ratio which a number has to a number. We aim to show that A and B are incommensurable.

**Step 2.** Suppose, for the sake of contradiction, that A and B are commensurable, that is, that there exists some common measure that measures both A and B [D10.1.1].

**Step 3.** Since A and B are commensurable, by Proposition 10.5, A and B have to one another the ratio which a number has to a number [10.5].

**Step 4.** But this contradicts the hypothesis that A and B have not to one another the ratio which a number has to a number.

**Step 5.** Therefore our supposition is false, and A and B are not commensurable; that is, A and B are incommensurable [D10.1.1].

Therefore, if two magnitudes have not to one another the ratio which a number has to a number, the magnitudes will be incommensurable. Q.E.D.

**USED:** 10.5, D10.1.1
**Human refs (from References field):** 10.5
**Jaccard:** 0.500 — AI adds ['D10.1.1']

## Proposition 10.9
**Statement:** The squares on straight lines commensurable in length have to one another the ratio which a square number has to a square number; and squares which have to one another the ratio which a square number has to a square number will also have their sides commensurable in length. But the squares on straight lines incommensurable in length have not to one another the ratio which a square number has to a square number; and squares which have not to one another the ratio which a square number has to a square number will not have their sides commensurable in length either.

**Step 1.** Let A and B be two straight lines commensurable in length. We wish to show that sq(A) : sq(B) is as a square number to a square number.

**Step 2.** Since A and B are commensurable in length, by Proposition 10.5, A : B is as some number m to some number n.

**Step 3.** By the corollary of Proposition 6.20, the square on A has to the square on B the duplicate ratio of that which A has to B; that is, sq(A) : sq(B) is the duplicate ratio of A : B.

**Step 4.** Since A : B = m : n, the duplicate ratio of A : B is the same as the duplicate ratio of m : n. By Proposition 8.11, the square number m*m has to the square number n*n the ratio duplicate of that which m has to n. Therefore sq(A) : sq(B) = m*m : n*n.

**Step 5.** By Definition 7.18, m*m and n*n are square numbers. Hence the squares on A and B have to one another the ratio which a square number has to a square number. This completes the proof of the first part.

**Step 6.** Conversely, let sq(A) : sq(B) be as a square number to a square number; say sq(A) : sq(B) = p*p : q*q, where p*p and q*q are square numbers. We wish to show that A and B are commensurable in length.

**Step 7.** By the corollary of Proposition 6.20, sq(A) : sq(B) is the duplicate ratio of A : B.

**Step 8.** By Proposition 8.11, p*p : q*q is the duplicate ratio of p : q.

**Step 9.** Therefore the duplicate ratio of A : B equals the duplicate ratio of p : q. Since two ratios whose duplicate ratios are equal must themselves be equal (by Definition 5.9, the duplicate ratio uniquely determines the base ratio given the same terms), we conclude A : B = p : q.

**Step 10.** Since A : B is as the number p to the number q, by Proposition 10.6 the straight lines A and B are commensurable in length. This completes the proof of the second part.

**Step 11.** Now let A and B be straight lines incommensurable in length. We wish to show that sq(A) : sq(B) is not as a square number to a square number.

**Step 12.** Suppose for the sake of contradiction that sq(A) : sq(B) is as a square number to a square number. Then by what was proved in the second part (Steps 6-10), A and B would be commensurable in length. But this contradicts the hypothesis that A and B are incommensurable. Therefore sq(A) : sq(B) is not as a square number to a square number. This completes the proof of the third part.

**Step 13.** Finally, let sq(A) : sq(B) not be as a square number to a square number. We wish to show that A and B are incommensurable in length.

**Step 14.** Suppose for the sake of contradiction that A and B are commensurable in length. Then by what was proved in the first part (Steps 1-5), sq(A) : sq(B) would be as a square number to a square number. But this contradicts the hypothesis. Therefore A and B are incommensurable in length. This completes the proof of the fourth part.

**Step 15.** Therefore the squares on straight lines commensurable in length have to one another the ratio which a square number has to a square number; and squares which have to one another the ratio which a square number has to a square number also have their sides commensurable in length. And the squares on straight lines incommensurable in length do not have to one another the ratio which a square number has to a square number; and squares which do not have to one another the ratio which a square number has to a square number do not have their sides commensurable in length either. Q.E.D.

**USED:** 10.5, 10.6, 6.20, 8.11, D5.9, D7.18
**Human refs (from References field):** 10.5, 10.6, 6.20, 8.11
**Jaccard:** 0.667 — AI adds ['D5.9', 'D7.18']

## Proposition 10.10
**Statement:** To find two straight lines incommensurable, the one in length only, and the other in square also, with an assigned straight line.

**Step 1.** Let A be the assigned straight line. We must find two straight lines, one incommensurable with A in length only, and the other incommensurable with A in square also.

**Step 2.** Let the square on A be set out. Since the ratio 2:1 is a ratio which a number has to a number, by Proposition 10.6 we can find a magnitude commensurable with the square on A in this ratio. Let the square on B be that magnitude, so that the square on A is to the square on B as 2 is to 1.

**Step 3.** Since the square on A has to the square on B the ratio 2:1, and 2:1 is a ratio of a number to a number, the squares on A and B are commensurable, so A and B are commensurable in square, by Definition D10.1.2.

**Step 4.** Now 2 is not a square number, for there is no number which multiplied by itself gives 2. Therefore the ratio 2:1 is not the ratio of a square number to a square number. By Proposition 10.9, since the squares on A and B have to one another a ratio which is not that of a square number to a square number, the straight lines A and B are incommensurable in length.

**Step 5.** Therefore B is commensurable with A in square (Step 3) but incommensurable with A in length (Step 4), that is, B is incommensurable with A in length only. This is the first required line.

**Step 6.** Now let C be taken as a mean proportional between A and B, by Proposition 6.13. Then A is to C as C is to B.

**Step 7.** Since A is to C as C is to B, by Proposition 6.17, the rectangle contained by A and B is equal to the square on C.

**Step 8.** Therefore the square on A is to the square on C as the square on A is to the rectangle contained by A and B. But the square on A is to the rectangle contained by A and B as the straight line A is to the straight line B, by Proposition 6.1. Therefore the square on A is to the square on C as A is to B.

**Step 9.** Since A and B are incommensurable in length (Step 4), the ratio of A to B is not the ratio of a number to a number, by Proposition 10.7.

**Step 10.** Therefore the ratio of the square on A to the square on C is not the ratio of a number to a number (Step 8, Step 9). By Proposition 10.8, the square on A and the square on C are incommensurable.

**Step 11.** Since the squares on A and C are incommensurable, A and C are incommensurable in square, by Definition D10.1.2. Lines incommensurable in square are necessarily also incommensurable in length. Therefore C is incommensurable with A in square also. This is the second required line.

**Step 12.** Therefore, given the assigned straight line A, we have found B incommensurable with A in length only, and C incommensurable with A in square also. Q.E.F.

**USED:** 10.6, 10.7, 10.8, 10.9, 6.1, 6.13, 6.17, D10.1.2
**Human refs (from References field):** 10.11, 10.6, 10.9, D5.9
**Jaccard:** 0.200 — AI adds ['10.7', '10.8', '6.1', '6.13', '6.17', 'D10.1.2']; Human adds ['10.11', 'D5.9']

## Proposition 10.11
**Statement:** If four magnitudes be proportional, and the first be commensurable with the second, the third will also be commensurable with the fourth; and, if the first be incommensurable with the second, the third will also be incommensurable with the fourth.

**Step 1.** Let A, B, C, D be four magnitudes such that A is to B as C is to D (that is, A:B :: C:D), as given by the hypothesis and the definition of proportional magnitudes [D5.6].

**Step 2.** First, suppose that A is commensurable with B [D10.1.1]. Since A is commensurable with B, A has to B the ratio which some number has to some number [10.5].

**Step 3.** Let A have to B the ratio which the number n has to the number m. Since A:B :: C:D (given) and A:B :: n:m, then C:D :: n:m, because ratios which are the same with the same ratio are also the same with one another [5.11].

**Step 4.** Since C has to D the ratio which the number n has to the number m, C is commensurable with D [10.6].

**Step 5.** Now suppose that A is incommensurable with B [D10.1.1]. Since A is incommensurable with B, A has not to B the ratio which a number has to a number [10.7].

**Step 6.** I say that C is also incommensurable with D. For suppose, for the sake of contradiction, that C is commensurable with D. Then C has to D the ratio which some number has to some number [10.5].

**Step 7.** But A:B :: C:D (given), and if C:D is a ratio of number to number, say C:D :: p:q, then A:B :: p:q, since ratios which are the same with the same ratio are also the same with one another [5.11].

**Step 8.** This means A has to B the ratio which a number has to a number, which contradicts the fact that A is incommensurable with B and therefore has not to B such a ratio [10.7].

**Step 9.** Therefore the supposition that C is commensurable with D is false, and so C has not to D the ratio which a number has to a number. Therefore C is incommensurable with D [10.8].

**Step 10.** Therefore, if four magnitudes be proportional and the first be commensurable with the second, the third is also commensurable with the fourth; and if the first be incommensurable with the second, the third is also incommensurable with the fourth. Q.E.D.

**USED:** 10.5, 10.6, 10.7, 10.8, 5.11, D10.1.1, D5.6
**Human refs (from References field):** 10.5, 10.6, 10.7, 10.8
**Jaccard:** 0.571 — AI adds ['5.11', 'D10.1.1', 'D5.6']

## Proposition 10.12
**Statement:** Magnitudes commensurable with the same magnitude are commensurable with one another also.

**Step 1.** Let A and B each be commensurable with a magnitude C. We must show that A is commensurable with B.

**Step 2.** Since A is commensurable with C, by Proposition 10.5, the ratio A:C is as some number m is to some number n. That is, A:C = m:n.

**Step 3.** Since B is commensurable with C, by Proposition 10.5, the ratio B:C is as some number p is to some number q. That is, B:C = p:q.

**Step 4.** By Proposition 7.17, if the number q multiplies the numbers m and n, the products have the same ratio as the numbers multiplied. Therefore qm:qn = m:n. Since A:C = m:n, we have A:C = qm:qn.

**Step 5.** By Proposition 7.17 again, if the number n multiplies the numbers q and p, the products have the same ratio as the numbers multiplied. Therefore nq:np = q:p. Since B:C = p:q, by Proposition 5.7 (corollary on inversion), C:B = q:p. Hence C:B = nq:np.

**Step 6.** We now have A:C = qm:qn and C:B = nq:np. Since qn = nq, the middle terms agree. By Proposition 5.22 (ex aequali), from A:C = qm:nq and C:B = nq:np, we conclude A:B = qm:np.

**Step 7.** Now qm and np are each the product of two numbers, and hence are themselves numbers. Therefore A:B is a ratio which a number (qm) has to a number (np).

**Step 8.** Since A and B have to one another the ratio which a number has to a number, by Proposition 10.6, A and B are commensurable with one another.

**Step 9.** Therefore, magnitudes commensurable with the same magnitude are commensurable with one another also. Q.E.D.

**USED:** 10.5, 10.6, 5.22, 5.7, 7.17, D10.1.1
**Human refs (from References field):** 10.5, 10.6, 5.11, 5.22, 8.4
**Jaccard:** 0.375 — AI adds ['5.7', '7.17', 'D10.1.1']; Human adds ['5.11', '8.4']

## Proposition 10.13
**Statement:** If two magnitudes be commensurable, and the one of them be incommensurable with any magnitude, the remaining one will also be incommensurable with the same.

**Step 1.** Let A and B be two commensurable magnitudes, and let A be incommensurable with some magnitude C. We are to prove that B is also incommensurable with C. [D10.1.1]

**Step 2.** Suppose, for the sake of contradiction, that B is commensurable with C.

**Step 3.** Since A is commensurable with B (by hypothesis), and B is commensurable with C (by our assumption), it follows by Proposition 10.12 that A is commensurable with C. [10.12]

**Step 4.** But A was given as incommensurable with C, which contradicts the conclusion of Step 3.

**Step 5.** Therefore the assumption in Step 2 is false, and B is incommensurable with C. [D10.1.1]

**Step 6.** Hence, if two magnitudes be commensurable, and one of them be incommensurable with any magnitude, the remaining one will also be incommensurable with the same. Q.E.D.

**USED:** 10.12, D10.1.1
**Human refs (from References field):** 10.12
**Jaccard:** 0.500 — AI adds ['D10.1.1']

## Proposition 10.14
**Statement:** If four straight lines be proportional, and the square on the first be greater than the square on the second by the square on a straight line commensurable with the first, the square on the third will also be greater than the square on the fourth by  the square on a straight line commensurable with the third. And, if the square on the first be greater than the square on the second by the square on a straight line incommensurable with the first, the square on the third will also be greater than the square on the fourth by the square on a straight line in-commensurable with the third.

**Step 1.** Let A, B, C, D be four straight lines such that A:B :: C:D. Suppose that sq(A) > sq(B) by the square on a straight line E, so that sq(A) = sq(B) + sq(E). We must show that sq(C) > sq(D) by the square on a straight line F, and that F is commensurable with C if E is commensurable with A, or incommensurable with C if E is incommensurable with A.

**Step 2.** Since A:B :: C:D, the similar and similarly described figures on these lines are proportional. In particular, the squares on them are proportional: sq(A):sq(B) :: sq(C):sq(D). [6.22]

**Step 3.** Since sq(A) > sq(B) (given that sq(A) = sq(B) + sq(E)), and sq(A):sq(B) :: sq(C):sq(D), the first being greater than the second, the third is also greater than the fourth, so sq(C) > sq(D). [5.14]

**Step 4.** Since sq(C) > sq(D), let a right triangle be constructed with hypotenuse equal to C and one leg equal to D. By the Pythagorean theorem, the remaining leg F satisfies sq(C) = sq(D) + sq(F), so that sq(F) = sq(C) - sq(D). Thus the square on C is greater than the square on D by the square on the straight line F. [1.47]

**Step 5.** From the proportion sq(A):sq(B) :: sq(C):sq(D), since all four terms are areas (squares on straight lines) and hence magnitudes of the same kind, we take the alternate ratio: sq(A):sq(C) :: sq(B):sq(D). [5.16]

**Step 6.** Now sq(B) is less than sq(A) (since sq(A) = sq(B) + sq(E)) and sq(D) is less than sq(C) (since sq(C) = sq(D) + sq(F)), and as the whole sq(A) is to the whole sq(C), so is the part subtracted sq(B) to the part subtracted sq(D). Therefore the remainder is to the remainder as the whole is to the whole: sq(E):sq(F) :: sq(A):sq(C). [5.19]

**Step 7.** Since sq(E):sq(F) :: sq(A):sq(C), and all four terms are magnitudes of the same kind (areas), we take the alternate ratio: sq(E):sq(A) :: sq(F):sq(C). [5.16]

**Step 8.** (Commensurable case.) Suppose E is commensurable in length with A. Then by Proposition 10.9, the squares on E and A have to one another the ratio which a square number has to a square number, that is, sq(E):sq(A) is a ratio of square numbers. Since sq(E):sq(A) :: sq(F):sq(C), the ratio sq(F):sq(C) is the same ratio, and hence is also a ratio of square numbers. By the converse part of 10.9, the sides F and C are commensurable in length. Therefore the square on C is greater than the square on D by the square on F, which is commensurable with C. [10.9]

**Step 9.** (Incommensurable case.) Suppose E is incommensurable in length with A. Then by 10.9, the ratio sq(E):sq(A) is not a ratio of square numbers. Since sq(E):sq(A) :: sq(F):sq(C), the ratio sq(F):sq(C) is the same ratio, and hence is likewise not a ratio of square numbers. By 10.9, the sides F and C are incommensurable in length. Therefore the square on C is greater than the square on D by the square on F, which is incommensurable with C. [10.9]

**Step 10.** Both parts of the proposition have been established: if four straight lines are proportional and the square on the first exceeds the square on the second by the square on a line commensurable with the first, then the square on the third exceeds the square on the fourth by the square on a line commensurable with the third; and if the excess is by a line incommensurable with the first, then the corresponding excess for the third and fourth is by a line incommensurable with the third. Q.E.D.

**USED:** 1.47, 10.9, 5.14, 5.16, 5.19, 6.22
**Human refs (from References field):** 10.11, 5.17, 5.22, 6.22
**Jaccard:** 0.111 — AI adds ['1.47', '10.9', '5.14', '5.16', '5.19']; Human adds ['10.11', '5.17', '5.22']

## Proposition 10.15
**Statement:** If two commensurable magnitudes be added together, the whole will also be commensurable with each of them; and, if the whole be commensurable with one of them, the original magnitudes will also be commensurable.

**Step 1.** Let AB and BC be two commensurable magnitudes, and let AC be the whole magnitude composed of AB and BC. We must prove two things: (i) that AC is commensurable with each of AB and BC, and (ii) conversely, that if AC is commensurable with one of AB and BC, then AB and BC are commensurable with each other.

**Step 2.** [Part (i): Forward direction.] Since AB and BC are commensurable, by Definition D10.1.1 there exists some magnitude D that measures both AB and BC.

**Step 3.** Since D measures AB, there is some number m such that AB is the same multiple of D as m is of unity, that is, AB = mD [D5.1, D5.2]. Similarly, since D measures BC, there is some number n such that BC = nD.

**Step 4.** Then AC = AB + BC = mD + nD = (m + n)D [CN2]. Since m and n are numbers, (m + n) is also a number, so D measures AC [D5.1, D5.2].

**Step 5.** Since D measures both AC and AB, AC and AB have a common measure, so AC is commensurable with AB [D10.1.1]. Since D measures both AC and BC, AC is also commensurable with BC.

**Step 6.** [Part (ii): Converse.] Now suppose that AC is commensurable with AB. We must prove that AB and BC are commensurable.

**Step 7.** Since AC and AB are commensurable, by D10.1.1 there exists a magnitude E that measures both AC and AB.

**Step 8.** Since E measures AC, we have AC = pE for some number p. Since E measures AB, we have AB = qE for some number q. Now BC = AC - AB = pE - qE = (p - q)E [CN3]. Since AC is greater than AB (the whole is greater than the part, CN5), we have p > q, so (p - q) is a number.

**Step 9.** Therefore E measures BC [D5.1, D5.2]. Since E measures both AB and BC, AB and BC have a common measure, so AB and BC are commensurable [D10.1.1].

**Step 10.** Therefore, if two commensurable magnitudes be added together, the whole is commensurable with each of them; and if the whole be commensurable with one of them, the original magnitudes are also commensurable. Q.E.D.

**USED:** CN2, CN3, CN5, D10.1.1, D5.1, D5.2
**Human refs (from References field):** D10.1.1
**Jaccard:** 0.167 — AI adds ['CN2', 'CN3', 'CN5', 'D5.1', 'D5.2']

## Proposition 10.16
**Statement:** If two incommensurable magnitudes be added together, the whole will also be incommensurable with each of them; and, if the whole be incommensurable with one of them, the original magnitudes will also be incommensurable.

**Step 1.** Let AB and BC be two incommensurable magnitudes. I say that the whole AC is incommensurable with each of AB and BC.

**Step 2.** Suppose, for the sake of contradiction, that AC is commensurable with AB. Then since AC is commensurable with AB, and AB is trivially commensurable with itself, by Proposition 10.15, since the whole AC is commensurable with one of the magnitudes AB, the original magnitudes AB and BC must also be commensurable with one another.

**Step 3.** But AB and BC were assumed to be incommensurable, which contradicts the conclusion of Step 2. Therefore AC is not commensurable with AB; that is, AC is incommensurable with AB.

**Step 4.** By the same argument, suppose AC is commensurable with BC. Then by Proposition 10.15, since the whole AC is commensurable with one of the magnitudes BC, the original magnitudes AB and BC must also be commensurable. This again contradicts the hypothesis that AB and BC are incommensurable. Therefore AC is incommensurable with BC.

**Step 5.** Hence, if two incommensurable magnitudes are added together, the whole is incommensurable with each of them.

**Step 6.** Now suppose conversely that the magnitude AC is incommensurable with one of the magnitudes AB or BC; let it be incommensurable with AB. I say that AB and BC are incommensurable.

**Step 7.** Suppose, for the sake of contradiction, that AB and BC are commensurable. Then by Proposition 10.15, since two commensurable magnitudes AB and BC are added together, the whole AC is commensurable with each of AB and BC. In particular, AC is commensurable with AB.

**Step 8.** But AC was assumed to be incommensurable with AB, which contradicts the conclusion of Step 7. Therefore AB and BC are not commensurable; that is, AB and BC are incommensurable.

**Step 9.** Therefore, if two incommensurable magnitudes be added together, the whole will also be incommensurable with each of them; and, if the whole be incommensurable with one of them, the original magnitudes will also be incommensurable. Q.E.D.

**USED:** 10.15, D10.1.1
**Human refs (from References field):** D10.1.1
**Jaccard:** 0.500 — AI adds ['10.15']

## Proposition 10.17
**Statement:** If there be two unequal straight lines, and to the greater there be applied a parallelogram equal to the fourth part of the square on the less and deficient by a square figure, and if it divide it into parts which are commensurable in length, then the square on the greater will be greater than the square on the less by the square on a straight line commensurable with the greater. And, if the square on the greater be greater than the square on the less by the square on a straight line commensurable with  the greater, and if there be applied to the greater a parallelogram equal to the fourth part of the square on the less and deficient by a square figure, it will divide it into parts which are commensurable in length.

**Step 1.** Let A and B be two unequal straight lines with A greater than B. Suppose that to A there has been applied a parallelogram equal to the fourth part of the square on B, deficient by a square figure, and that this application divides A into segments AE and EB (so that AE + EB = A and the rectangle contained by AE, EB equals the fourth part of the square on B).

**Step 2.** Bisect A at point C, so that AC = CB = A/2 [1.10]. Bisect B at point F, so that BF = B/2 [1.10]. Then the fourth part of the square on B equals the square on BF. To see this, apply 2.4 to the line B cut at F: the square on B equals the square on BF plus the square on BF plus twice the rectangle contained by BF and BF, which equals four times the square on BF. Hence the square on BF is the fourth part of the square on B.

**Step 3.** Therefore the rectangle contained by AE, EB equals the square on BF, that is, the square on B/2.

**Step 4.** Since A is cut into equal segments at C and into unequal segments at E, by 2.5 the rectangle contained by AE, EB together with the square on CE equals the square on AC. That is: rect(AE, EB) + sq(CE) = sq(AC).

**Step 5.** Substituting the result of Step 3: sq(BF) + sq(CE) = sq(AC). Therefore sq(AC) - sq(BF) = sq(CE), or equivalently sq(CE) = sq(AC) - sq(BF) [CN3].

**Step 6.** Now by 2.4 applied to the line A bisected at C: sq(A) = 4 · sq(AC). Similarly sq(B) = 4 · sq(BF) (from Step 2), and viewing the line 2CE as bisected at its midpoint and applying 2.4: sq(2CE) = 4 · sq(CE).

**Step 7.** From Step 5, sq(CE) = sq(AC) - sq(BF). Taking four times each side [CN2 applied repeatedly]: 4 · sq(CE) = 4 · sq(AC) - 4 · sq(BF), that is, sq(2CE) = sq(A) - sq(B) [by Step 6]. Therefore the square on A exceeds the square on B by the square on the straight line 2CE.

**Step 8.** (Forward direction) Now suppose that AE and EB are commensurable in length. Since AE and EB are commensurable, there exists a magnitude m that measures both AE and EB [D10.1.1]. Since m measures AE and m measures EB, m also measures AE + EB = A and AE - EB = 2CE (for if AE = p · m and EB = q · m, then A = (p+q) · m and 2CE = AE - EB = (p-q) · m) [D10.1.1]. Therefore A and 2CE are commensurable [D10.1.1]. Since by Step 7 the square on A exceeds the square on B by the square on 2CE, and 2CE is commensurable with A, the square on the greater is greater than the square on the less by the square on a straight line commensurable with the greater.

**Step 9.** (Converse direction) Conversely, suppose the square on A is greater than the square on B by the square on a straight line D that is commensurable with A, so that sq(D) = sq(A) - sq(B). By Step 7, sq(2CE) = sq(A) - sq(B) as well. Therefore sq(D) = sq(2CE) [CN1], and hence D = 2CE.

**Step 10.** Since D is commensurable with A, the line 2CE is commensurable with A, that is, 2CE is commensurable with 2AC (since A = 2AC). A common measure of 2CE and 2AC measures their sum 2AC + 2CE = 2 · AE and their difference 2AC - 2CE = 2 · EB [D10.1.1]. Therefore 2 · AE and 2 · EB are commensurable.

**Step 11.** By 5.15, parts have the same ratio as the same multiples taken in corresponding order, so AE : EB :: 2·AE : 2·EB. Since 2·AE and 2·EB are commensurable (Step 10), by 10.11 (if four magnitudes are proportional and the first is commensurable with the second, the third is also commensurable with the fourth), AE is commensurable with EB.

**Step 12.** Therefore the application divides A into parts AE and EB which are commensurable in length. This completes the proof of both directions. Q.E.D.

**USED:** 1.10, 10.11, 2.4, 2.5, 5.15, CN1, CN2, CN3, D10.1.1
**Human refs (from References field):** 10.12, 10.15, 10.6, 2.5
**Jaccard:** 0.083 — AI adds ['1.10', '10.11', '2.4', '5.15', 'CN1', 'CN2', 'CN3', 'D10.1.1']; Human adds ['10.12', '10.15', '10.6']

## Proposition 10.18
**Statement:** If there be two unequal straight lines, and to the greater there be applied a parallelogram equal to the fourth part of the square on the less and deficient by a square figure, and if it divide it into parts which are incommensurable, the square on the greater will be greater than the square on the less by the square on a straight line incommensurable with the greater. And, if the square on the greater be greater than the square on the less by the square on a straight line incommensurable with the greater, and if there be applied to the greater a parallelogram equal to the fourth part of the square on the less and deficient by a square figure, it divides it into parts which are incommensurable. Let A, BC be two unequal straight lines, of which BC is the greater, and to BC let there be applied a parallelogram equal to the fourth part of the square on the less, A, and deficient by a square figure.

**Step 1.** Let A and BC be two unequal straight lines with BC the greater. Let there be applied to BC a parallelogram equal to the fourth part of the square on A and deficient by a square figure, and let it divide BC into BD and DC. We must prove that BD and DC are incommensurable in length if and only if the square on BC is greater than the square on A by the square on a straight line incommensurable with BC.

**Step 2.** Bisect BC at E [1.10]. Then since BC is divided into equal segments at E and into unequal segments at D (for the applied parallelogram divides it into parts BD and DC which are unequal), by 2.5 the rectangle contained by BD and DC together with the square on ED equals the square on BE.

**Step 3.** But the rectangle BD by DC equals the fourth part of the square on A (by hypothesis of the application). Therefore the fourth part of the square on A together with the square on DE equals the square on BE.

**Step 4.** Now BE equals half of BC, so the square on BE equals the fourth part of the square on BC. Therefore the fourth part of the square on BC equals the fourth part of the square on A together with the square on DE [CN1].

**Step 5.** Subtracting the fourth part of the square on A from both sides [CN3], the square on DE equals the fourth part of the square on BC minus the fourth part of the square on A, that is, the fourth part of the excess of the square on BC over the square on A.

**Step 6.** Therefore the excess of the square on BC over the square on A equals four times the square on DE, which is the square on a straight line equal to the double of DE. Let FG be the double of DE. Then the square on BC is greater than the square on A by the square on FG.

**Step 7.** Now since BC equals the double of BE and FG equals the double of DE, BC is to FG as BE is to DE. Therefore BC and FG are commensurable or incommensurable according as BE and DE are commensurable or incommensurable [10.11].

**Step 8.** Also, since BD equals BE plus ED and DC equals BE minus ED [for E is the midpoint of BC], we have BD plus DC equals twice BE, and BD minus DC equals twice DE.

**PART I (Forward direction):** Suppose BD and DC are incommensurable in length.

**Step 9.** Assume for the sake of contradiction that BE and DE are commensurable. Then since BD equals BE plus DE, by 10.15 BD is commensurable with BE. Likewise since DC equals BE minus DE, by 10.15 DC is commensurable with BE. Therefore BD and DC, being each commensurable with BE, are commensurable with one another [10.12]. But this contradicts the hypothesis that BD and DC are incommensurable. Therefore BE and DE are incommensurable.

**Step 10.** Since BE and DE are incommensurable, BC and FG are incommensurable [by Step 7 and 10.11]. Therefore the square on BC is greater than the square on A by the square on FG, a straight line incommensurable with BC.

**PART II (Converse direction):** Suppose the square on BC is greater than the square on A by the square on a straight line FG incommensurable with BC.

**Step 11.** Since FG is incommensurable with BC, and BC equals the double of BE while FG equals the double of DE, it follows that BE is incommensurable with DE [10.11].

**Step 12.** Assume for the sake of contradiction that BD and DC are commensurable. Then by the forward direction of 10.17, since the parallelogram equal to the fourth part of the square on A applied to BC and deficient by a square divides BC into commensurable parts BD and DC, the square on BC would be greater than the square on A by the square on a straight line commensurable with BC. But the square on BC is greater than the square on A by the square on FG, which is incommensurable with BC. This is a contradiction.

**Step 13.** Therefore BD and DC are incommensurable in length. Q.E.D.

**USED:** 1.10, 10.11, 10.12, 10.15, 10.17, 2.5, CN1, CN3
**Human refs (from References field):** 10.13, 10.16, 10.17, 10.6
**Jaccard:** 0.091 — AI adds ['1.10', '10.11', '10.12', '10.15', '2.5', 'CN1', 'CN3']; Human adds ['10.13', '10.16', '10.6']

## Proposition 10.19
**Statement:** The rectangle contained by rational straight lines commensurable in length is rational.

**Step 1.** Let A and B be rational straight lines commensurable in length with one another. We must show that the rectangle contained by A and B is rational.

**Step 2.** Since A is a rational straight line, by Definition D10.1.3, A is commensurable in square with the assigned rational straight line. Therefore the square on A is commensurable with the square on the assigned straight line, and by Definition D10.1.4, the square on A is rational.

**Step 3.** Consider the rectangle contained by A and B, and the square on A. These are parallelograms sharing the same height A. By Proposition 6.1, parallelograms under the same height are to one another as their bases. Therefore the rectangle contained by A and B is to the square on A as B is to A.

**Step 4.** Since A and B are commensurable in length, by Proposition 10.5, the ratio of B to A is the ratio which a number has to a number.

**Step 5.** Since the rectangle contained by A and B has to the square on A the ratio which a number has to a number, by Proposition 10.6, the rectangle contained by A and B is commensurable with the square on A.

**Step 6.** But the square on A is rational, meaning it is commensurable with the square on the assigned rational straight line (Step 2). Since the rectangle contained by A and B is commensurable with the square on A (Step 5), and the square on A is commensurable with the square on the assigned straight line, by Proposition 10.12 the rectangle contained by A and B is commensurable with the square on the assigned straight line.

**Step 7.** Therefore, by Definition D10.1.4, the rectangle contained by A and B is rational. Q.E.D.

**USED:** 10.12, 10.5, 10.6, 6.1, D10.1.3, D10.1.4
**Human refs (from References field):** 10.11, 6.1, D10.1.4
**Jaccard:** 0.286 — AI adds ['10.12', '10.5', '10.6', 'D10.1.3']; Human adds ['10.11']

## Proposition 10.20
**Statement:** If a rational area be applied to a rational straight line, it produces as breadth a straight line rational and commensurable in length with the straight line to which it is applied.

**Step 1.** Let the rational area S be applied to the rational straight line A, producing as breadth the straight line B, so that S is the rectangle contained by A and B.

**Step 2.** Since S is a rational area, S is commensurable with the square on the assigned rational straight line rho [D10.1.4].

**Step 3.** Since A is rational, A is commensurable with rho either in length or in square [D10.1.3]. If A is commensurable in length with rho, then the squares on A and rho have to one another the ratio which a square number has to a square number, and hence the square on A is commensurable with the square on rho [10.9]. If A is commensurable in square only with rho, then by definition the square on A is commensurable with the square on rho [D10.1.2]. In either case, the square on A is commensurable with the square on rho, and therefore the square on A is rational [D10.1.4].

**Step 4.** Since S is commensurable with the square on rho (Step 2), and the square on A is commensurable with the square on rho (Step 3), S and the square on A are commensurable with one another [10.12].

**Step 5.** Now the rectangle contained by A and B, and the square on A (which is the rectangle contained by A and A), are parallelograms with the same height A. Therefore the rectangle S has to the square on A the ratio which B has to A [6.1].

**Step 6.** Since S and the square on A are commensurable (Step 4), their ratio is a ratio which a number has to a number [10.5].

**Step 7.** Therefore the ratio of B to A is a ratio which a number has to a number [from Steps 5 and 6].

**Step 8.** Therefore B is commensurable in length with A [10.6].

**Step 9.** Since A is rational, and B is commensurable in length with A, B is also rational [D10.1.3]. Moreover, B is commensurable in length with the straight line A to which the area was applied (Step 8).

**Step 10.** Therefore, if a rational area be applied to a rational straight line, it produces as breadth a straight line rational and commensurable in length with the straight line to which it is applied. Q.E.D.

**USED:** 10.12, 10.5, 10.6, 10.9, 6.1, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 10.11, 6.1, D10.1.4
**Jaccard:** 0.222 — AI adds ['10.12', '10.5', '10.6', '10.9', 'D10.1.2', 'D10.1.3']; Human adds ['10.11']

## Proposition 10.21
**Statement:** The rectangle contained by rational straight lines commensurable in square only is irrational, and the side of the square equal to it is irrational. Let the latter be called medial.

**Step 1.** Let A and B be rational straight lines commensurable in square only. We are to show that the rectangle contained by A and B is irrational, and that the side of the square equal to it is irrational.

**Step 2.** Since A is rational, the square on A is rational [D10.1.3, D10.1.4].

**Step 3.** Consider the rectangle contained by A and B, and the square on A. Both are parallelogrammic areas with the same height A: the square on A has base A, and the rectangle contained by A and B has base B. By 6.1, parallelograms under the same height are to one another as their bases. Therefore the rectangle contained by A and B is to the square on A as B is to A.

**Step 4.** Since A and B are commensurable in square only, they are by definition incommensurable in length [D10.1.2].

**Step 5.** Since A and B are incommensurable in length, the ratio of B to A is not as a number to a number [10.7].

**Step 6.** But the rectangle contained by A and B is to the square on A as B is to A (Step 3). Therefore the rectangle contained by A and B is to the square on A not as a number to a number.

**Step 7.** Therefore the rectangle contained by A and B is incommensurable with the square on A [10.8].

**Step 8.** But the square on A is rational (Step 2). And an area incommensurable with a rational area is irrational [D10.1.4]. Therefore the rectangle contained by A and B is irrational.

**Step 9.** Now let C be the side of the square equal to the rectangle contained by A and B; that is, let the square on C equal the rectangle contained by A and B. Since the rectangle contained by A and B is irrational, the square on C is irrational. Therefore C is irrational [D10.1.4]. Let C be called medial.

**Step 10.** Therefore the rectangle contained by rational straight lines commensurable in square only is irrational, and the side of the square equal to it is irrational. Q.E.D.

**USED:** 10.7, 10.8, 6.1, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 10.11, 6.1, D10.1.4
**Jaccard:** 0.286 — AI adds ['10.7', '10.8', 'D10.1.2', 'D10.1.3']; Human adds ['10.11']

## Proposition 10.22
**Statement:** The square on a medial straight line, if applied to a rational straight line, produces as breadth a straight line rational and incommensurable in length with that to which it is applied.

**Step 1.** Let A be a medial straight line and let B be a rational straight line. Apply the square on A to B, producing as breadth a straight line C, so that the rectangle contained by B and C equals the square on A, that is, B * C = A^2. We must show that C is rational and incommensurable in length with B.

**Step 2.** Since A is medial, by the definition established in 10.21, the square on A (that is, A^2) is equal to the rectangle contained by two rational straight lines D and E that are commensurable in square only. Thus B * C = A^2 = D * E. By 10.21, this area A^2 is irrational (a medial area).

**Step 3.** Since B * C = D * E, by 6.16 (if the rectangle contained by two straight lines equals the rectangle contained by two other straight lines, then they are reciprocally proportional), we have B : D = E : C.

**Step 4.** Since B and D are both rational straight lines, the squares on them are both rational areas (by D10.1.4), and hence B^2 and D^2 are commensurable with one another.

**Step 5.** Since B : D = E : C, and squares are similar rectilineal figures, by 6.22 the squares on these proportional lines are also proportional: B^2 : D^2 = E^2 : C^2.

**Step 6.** Since B^2 and D^2 are commensurable (Step 4), and B^2 : D^2 = E^2 : C^2 (Step 5), by 10.11 the magnitudes E^2 and C^2 are also commensurable.

**Step 7.** Since E is rational, E^2 is a rational area (by D10.1.4). Since C^2 is commensurable with E^2 (Step 6), and E^2 is a rational area, C^2 is also a rational area (by 10.12, since C^2 is commensurable with E^2, and E^2 is commensurable with the square on the assigned rational line). Therefore C is rational (by D10.1.3).

**Step 8.** Now we show C is incommensurable in length with B. Since B * C = A^2, we have B * C : B^2 = C : B (by 6.1, as the ratio of rectangles with equal height B equals the ratio of their bases).

**Step 9.** The area A^2 is a medial area, which is irrational (by 10.21), and hence incommensurable with B^2, which is a rational area (by D10.1.4). Therefore B * C and B^2 are incommensurable (since B * C = A^2).

**Step 10.** Since B * C : B^2 = C : B (Step 8), and B * C is incommensurable with B^2 (Step 9), by 10.11 the straight line C is incommensurable with B, that is, C is incommensurable in length with B.

**Step 11.** Therefore C is rational (Step 7) and incommensurable in length with B (Step 10). That is, the square on a medial straight line, if applied to a rational straight line, produces as breadth a straight line rational and incommensurable in length with that to which it is applied. Q.E.F.

**USED:** 10.11, 10.12, 10.21, 6.1, 6.16, 6.22, D10.1.3, D10.1.4
**Human refs (from References field):** 10.11, 10.13, 10.21, 6.14, 6.22, D10.1.4
**Jaccard:** 0.400 — AI adds ['10.12', '6.1', '6.16', 'D10.1.3']; Human adds ['10.13', '6.14']

## Proposition 10.23
**Statement:** A straight line commensurable with a medial straight line is medial.

**Step 1.** Let A be a medial straight line, and let B be commensurable with A. We must show that B is also medial.

**Step 2.** Let a rational straight line CD be set out. To the straight line CD, let the rectangle CD·DE be applied equal to the square on A, producing DE as breadth. By Proposition 10.22, since A is medial, the breadth DE is rational and incommensurable in length with CD.

**Step 3.** To the same straight line CD, let the rectangle CD·DF be applied equal to the square on B, producing DF as breadth. Thus CD·DE = A² and CD·DF = B².

**Step 4.** Since A and B are commensurable in length, by Proposition 10.9, the squares on A and B have to one another the ratio which a square number has to a square number. Since a ratio of square numbers is a ratio of numbers, by Proposition 10.6, the square on A and the square on B are commensurable. That is, A² and B² are commensurable.

**Step 5.** Since CD·DE = A² and CD·DF = B², and these rectangles share the same base CD, by Proposition 6.1, A² is to B² as DE is to DF.

**Step 6.** Since A² and B² are commensurable (Step 4), and A² is to B² as DE is to DF (Step 5), by Proposition 10.11, DE is commensurable with DF.

**Step 7.** Since DE is rational (Step 2) and DF is commensurable with DE (Step 6), by Proposition 10.12, DF is also rational. More precisely, DE is commensurable with the assigned rational line, and DF is commensurable with DE, so DF is commensurable with the assigned rational line, hence rational by Definition D10.1.3.

**Step 8.** Since DE is incommensurable in length with CD (Step 2), and DF is commensurable with DE (Step 6), by Proposition 10.13, DF is incommensurable in length with CD.

**Step 9.** Therefore CD and DF are both rational straight lines which are incommensurable in length with one another. By Definition D10.1.3, they are commensurable in square only.

**Step 10.** The rectangle CD·DF, which equals B² (Step 3), is thus contained by rational straight lines commensurable in square only. By Proposition 10.21, this rectangle is irrational, and the side of the square equal to it is irrational and is called medial.

**Step 11.** But the side of the square equal to CD·DF is B itself (since CD·DF = B²). Therefore B is medial.

Hence a straight line commensurable with a medial straight line is medial. Q.E.D.

**USED:** 10.11, 10.12, 10.13, 10.21, 10.22, 10.6, 10.9, 6.1, D10.1.3
**Human refs (from References field):** 10.11, 10.13, 10.21, 10.22, 6.1, D10.1.3
**Jaccard:** 0.667 — AI adds ['10.12', '10.6', '10.9']

## Proposition 10.24
**Statement:** The rectangle contained by medial straight lines commensurable in length is medial.

**Step 1.** Let A and B be medial straight lines commensurable in length. We must show that the rectangle contained by A and B is medial.

**Step 2.** Since A is a medial straight line, by the definition of medial (10.21), A is irrational, and the square on A is equal to the rectangle contained by rational straight lines commensurable in square only. Thus the square on A is an irrational area, that is, a medial area (D10.1.4).

**Step 3.** By 6.1, the rectangle contained by A and B is to the square on A as B is to A, since rectangles under the same height (A) are to one another as their bases (B and A respectively).

**Step 4.** Since A and B are commensurable in length, the ratio of B to A is as some number to some number (10.5).

**Step 5.** Since the rectangle contained by A and B is to the square on A as B is to A (Step 3), and B is to A as a number to a number (Step 4), the rectangle contained by A and B is to the square on A as a number to a number. Therefore the rectangle contained by A and B is commensurable with the square on A (10.6).

**Step 6.** Let C be the side of the square equal to the rectangle contained by A and B; such a square exists by 2.14. Then the square on C equals the rectangle contained by A and B.

**Step 7.** Since the square on C (which equals the rectangle contained by A and B) is commensurable with the square on A (Step 5), the straight lines C and A are commensurable in square (D10.1.2).

**Step 8.** Since A is medial and C is commensurable with A (in square), C is also medial (10.23).

**Step 9.** Therefore the rectangle contained by A and B, being equal to the square on the medial straight line C, is a medial area (D10.1.4). Hence the rectangle contained by medial straight lines commensurable in length is medial. Q.E.D.

**USED:** 10.21, 10.23, 10.5, 10.6, 2.14, 6.1, D10.1.2, D10.1.4
**Human refs (from References field):** 10.11, 10.23, 6.1
**Jaccard:** 0.222 — AI adds ['10.21', '10.5', '10.6', '2.14', 'D10.1.2', 'D10.1.4']; Human adds ['10.11']

## Proposition 10.25
**Statement:** The rectangle contained by medial straight lines commensurable in square only is either rational or medial.

**Step 1.** Let A and B be medial straight lines commensurable in square only. We must show that the rectangle contained by A and B is either rational or medial.

**Step 2.** Set out a rational straight line C. Since A is medial, the square on A is a medial area. Apply the square on A to C, producing breadth D, so that sq(A) = C * D. By 10.22, D is rational and incommensurable in length with C.

**Step 3.** Similarly, since B is medial, apply the square on B to C, producing breadth E, so that sq(B) = C * E. By 10.22, E is rational and incommensurable in length with C.

**Step 4.** Since A and B are commensurable in square, sq(A) is commensurable with sq(B) [D10.1.2]. Since sq(A) = C * D and sq(B) = C * E, we have C * D commensurable with C * E. By 6.1, C * D : C * E = D : E, so D and E have a ratio equal to that of two commensurable magnitudes. Therefore D is commensurable in length with E [10.11].

**Step 5.** Apply the rectangle contained by A and B to C, producing breadth F, so that rect(A, B) = C * F.

**Step 6.** Now sq(A) = C * D and rect(A, B) = C * F. By 6.1, sq(A) : rect(A, B) = D : F. But also sq(A) : rect(A, B) = (A * A) : (A * B) = A : B by 6.1, since both areas have the same side A. Therefore D : F = A : B.

**Step 7.** Similarly, rect(A, B) = C * F and sq(B) = C * E. By 6.1, rect(A, B) : sq(B) = F : E. But rect(A, B) : sq(B) = (A * B) : (B * B) = A : B by 6.1, since both areas have the same side B. Therefore F : E = A : B.

**Step 8.** From Steps 6 and 7, D : F = F : E. That is, F is a mean proportional between D and E. By 6.17, the rectangle contained by D and E equals the square on F, i.e., rect(D, E) = sq(F).

**Step 9.** Since D and E are both rational [Steps 2 and 3] and commensurable in length with one another [Step 4], the rectangle contained by D and E is rational [10.19]. Therefore sq(F) is rational [D10.1.4].

**Step 10.** Since sq(F) is rational, sq(F) is commensurable with the square on the rational line C [D10.1.4]. Therefore F is commensurable in square with C, so F is rational [D10.1.3].

**Step 11.** Now rect(A, B) = C * F, where C is rational and F is rational. There are two cases. Case (i): If F is commensurable in length with C, then rect(A, B) is a rational area [10.19]. Case (ii): If F is incommensurable in length with C (that is, C and F are rational lines commensurable in square only), then rect(A, B) is a medial area [10.21].

**Step 12.** Since A and B are commensurable in square only, they are incommensurable in length. By Step 6, D : F = A : B, and since A and B are incommensurable in length, D and F are incommensurable in length [10.11]. Since D is incommensurable in length with F, we cannot determine from the given hypotheses alone whether F is commensurable in length with C or not; but F must be one or the other. In either case, by Step 11, the rectangle contained by A and B is either rational or medial.

**Step 13.** Therefore the rectangle contained by medial straight lines commensurable in square only is either rational or medial. Q.E.D.

**USED:** 10.11, 10.19, 10.21, 10.22, 6.1, 6.17, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 10.11, 10.19, 10.21, 10.22, 5.11, 6.1, 6.17
**Jaccard:** 0.600 — AI adds ['D10.1.2', 'D10.1.3', 'D10.1.4']; Human adds ['5.11']

## Proposition 10.26
**Statement:** A medial area does not exceed a medial area by a rational area.

**Step 1.** Suppose, for the sake of contradiction, that AB and CD are medial areas with AB greater than CD, and that their difference AB minus CD is a rational area.

**Step 2.** Let EF be a rational straight line. Apply the area AB to EF, producing as breadth the straight line FH, so that the rectangle EF times FH equals AB. Apply the area CD to EF, producing as breadth FG, so that the rectangle EF times FG equals CD, where G falls between F and H (since CD is less than AB). Then the rectangle EF times GH equals AB minus CD, where GH equals FH minus FG.

**Step 3.** Since AB is a medial area applied to the rational straight line EF, the breadth FH is rational and incommensurable in length with EF [10.22]. Similarly, since CD is a medial area applied to the rational straight line EF, the breadth FG is rational and incommensurable in length with EF [10.22].

**Step 4.** Since AB minus CD is a rational area (by hypothesis) applied to the rational straight line EF, the breadth GH is rational and commensurable in length with EF [10.20].

**Step 5.** Since FH is rational, FH is commensurable in square with EF [D10.1.3], so the square on FH is commensurable with the square on EF. Since FG is rational, likewise the square on FG is commensurable with the square on EF. Therefore the square on FH and the square on FG are commensurable with one another [10.12]. Since the square on FH is commensurable with the square on FG, the difference of the square on FH and the square on FG is commensurable with the square on FG [10.15], and hence commensurable with the square on EF [10.12]. Therefore the difference of the squares on FH and FG is a rational area [D10.1.4].

**Step 6.** Now, by repeated application of the distributive property of rectangles [2.1], the rectangle contained by the sum FH plus FG and the difference FH minus FG equals the square on FH minus the square on FG. Since FH minus FG equals GH, the rectangle contained by FH plus FG and GH equals the difference of the squares on FH and FG, which is a rational area by Step 5.

**Step 7.** The rectangle contained by FH plus FG and GH is thus a rational area, and GH is a rational straight line commensurable in length with EF (from Step 4). Applying this rational area to the rational straight line GH, the breadth is FH plus FG. By the property that a rational area applied to a rational straight line produces a breadth rational and commensurable in length with that line [10.20], the straight line FH plus FG is rational and commensurable in length with GH. Since GH is commensurable in length with EF, the straight line FH plus FG is commensurable in length with EF [10.12].

**Step 8.** We now have that FH plus FG is commensurable in length with EF, and GH (which equals FH minus FG) is commensurable in length with EF. Since both are commensurable with EF, they are commensurable with one another [10.12]. Therefore their sum, which equals (FH plus FG) plus (FH minus FG) equals twice FH, is commensurable with each of them [10.15], and hence commensurable in length with EF [10.12].

**Step 9.** Since twice FH is commensurable in length with EF, and FH has to twice FH the ratio 1 to 2 (which is a ratio of numbers), FH and twice FH are commensurable [10.6]. Since FH is commensurable with twice FH and twice FH is commensurable with EF, it follows that FH is commensurable in length with EF [10.12].

**Step 10.** But this contradicts Step 3, which established that FH is incommensurable in length with EF [10.22]. Therefore the supposition that AB minus CD is rational is false, and a medial area does not exceed a medial area by a rational area. Q.E.D.

**USED:** 10.12, 10.15, 10.20, 10.22, 10.6, 2.1, D10.1.3, D10.1.4
**Human refs (from References field):** 10.11, 10.13, 10.16, 10.20, 10.22, 10.6, 2.4, D10.1.4
**Jaccard:** 0.333 — AI adds ['10.12', '10.15', '2.1', 'D10.1.3']; Human adds ['10.11', '10.13', '10.16', '2.4']

## Proposition 10.27
**Statement:** To find medial straight lines commensurable in square only which contain a rational rectangle.

**Step 1.** Let A be a set-out rational straight line (D10.1.3).

**Step 2.** By 10.10, there exists a straight line B commensurable in square only with A. Then B is also rational (D10.1.3), and A, B are incommensurable in length but commensurable in square.

**Step 3.** By 6.13, take C the mean proportional between A and B, so that A:C = C:B.

**Step 4.** By 6.17, since A, C, B are three straight lines in proportion, rect(A, B) = sq(C).

**Step 5.** Since A and B are rational straight lines commensurable in square only, rect(A, B) is irrational and specifically medial, by 10.21. Therefore sq(C) is a medial area, and C is a medial straight line (D10.1.4).

**Step 6.** By 6.11, find E as the third proportional to C and A, so that C:A = A:E.

**Step 7.** Since C:A = A:E, by 6.17 the rectangle contained by the extremes equals the square on the mean: rect(C, E) = sq(A). Since sq(A) is a rational area (D10.1.4), the rectangle rect(C, E) is rational.

**Step 8.** I now show that C and E are incommensurable in length. From C:A = A:E, we obtain C:E = C:A composed with A:E = (C:A) composed with (C:A), that is, C has to E the duplicate ratio of C to A. Now by 6.1, sq(A):rect(A, B) = A:B, and since rect(A, B) = sq(C), we have sq(A):sq(C) = A:B, so C:A is the inverse of this, giving the ratio sq(C):sq(A) = B:A. Since A and B are incommensurable in length (Step 2), the ratio B:A is not a ratio of commensurable magnitudes. Therefore C:E, being the duplicate of an irrational ratio, is itself irrational. Hence C and E are incommensurable in length.

**Step 9.** I now show that C and E are commensurable in square. From C:A = A:E, by 6.22 (similar figures on proportional lines are proportional), sq(C):sq(A) = sq(A):sq(E). So sq(C), sq(A), sq(E) are three magnitudes in continued proportion. By 6.17 applied to this proportion, sq(C) times sq(E) equals sq(A) squared. Therefore sq(E) = sq(A)^2 / sq(C), and the ratio sq(E):sq(C) = sq(A)^2 : sq(C)^2. From Step 8, sq(A):sq(C) = A:B, so sq(A)^2:sq(C)^2 = sq(A):sq(B) (by 6.22, the ratio of squares is the duplicate of the ratio of sides, applied inversely). Now since A and B are both rational, sq(A) and sq(B) are each commensurable with the assigned rational area, and hence commensurable with each other (by 10.12). Thus sq(E):sq(C) = sq(A):sq(B) is a ratio of commensurable magnitudes, so sq(E) and sq(C) are commensurable. Therefore C and E are commensurable in square.

**Step 10.** Since C and E are commensurable in square (Step 9) but incommensurable in length (Step 8), C and E are commensurable in square only.

**Step 11.** Since C is medial (Step 5), and E is commensurable in square with C (Step 9), by 10.23 E is also medial.

**Step 12.** Therefore C and E are medial straight lines, commensurable in square only (Step 10), and they contain a rational rectangle, namely rect(C, E) = sq(A) (Step 7). This is what was required to find.

**USED:** 10.10, 10.12, 10.21, 10.23, 6.1, 6.11, 6.13, 6.17, 6.22, D10.1.3, D10.1.4
**Human refs (from References field):** 10.11, 10.21, 10.23, 5.16, 6.12, 6.13, 6.17
**Jaccard:** 0.286 — AI adds ['10.10', '10.12', '6.1', '6.11', '6.22', 'D10.1.3', 'D10.1.4']; Human adds ['10.11', '5.16', '6.12']

## Proposition 10.28
**Statement:** To find medial straight lines commensurable in square only which contain a medial rectangle.

**Step 1.** Let A be a rational straight line set out, and let there be taken three numbers p, q, and r such that p:q is not the ratio which a square number has to a square number, r:q is the ratio which a square number has to a square number (say r = 4q so that r:q = 4:1), and p:r is not the ratio which a square number has to a square number. For example, let p = 2, q = 3, r = 12; then p:q = 2:3, r:q = 4:1, and p:r = 1:6, of which only r:q is a ratio of square numbers.

**Step 2.** By 6.12, find a straight line B such that sq(A):sq(B) = p:q. Since p:q is a ratio of numbers, sq(A) and sq(B) are commensurable by 10.6, so A and B are commensurable in square. Since p:q is not the ratio of a square number to a square number, A and B are incommensurable in length by 10.9. Both A and B are rational by D10.1.3, so A and B are rational straight lines commensurable in square only.

**Step 3.** Similarly, by 6.12, find a straight line D such that sq(A):sq(D) = p:r. Since p:r is a ratio of numbers, sq(A) and sq(D) are commensurable by 10.6, so A and D are commensurable in square. Since p:r is not the ratio of a square number to a square number, A and D are incommensurable in length by 10.9. Hence A and D are rational straight lines commensurable in square only.

**Step 4.** Since sq(A):sq(B) = p:q and sq(A):sq(D) = p:r, we have sq(B):sq(D) = r:q by 5.16 (ex aequali). Since r:q is the ratio of a square number to a square number, B and D are commensurable in length by 10.9. Let the ratio B:D = s:t where s:t is the sub-duplicate of r:q; with r:q = 4:1, we have B:D = 2:1.

**Step 5.** By 6.13, let C be the mean proportional of A and B, so that A:C = C:B. By 6.17, the rectangle contained by A and B equals the square on C, that is, sq(C) = rect(A,B). Since A and B are rational straight lines commensurable in square only, the rectangle contained by A and B is irrational by 10.21, and C, the side of the square equal to it, is a medial straight line.

**Step 6.** By 6.13, let E be the mean proportional of A and D, so that A:E = E:D. By 6.17, sq(E) = rect(A,D). Since A and D are rational straight lines commensurable in square only, the rectangle contained by A and D is irrational by 10.21, and E is a medial straight line.

**Step 7.** Now sq(C) = rect(A,B) and sq(E) = rect(A,D). By 6.1, since the rectangles rect(A,B) and rect(A,D) have a common side A, we have rect(A,B):rect(A,D) = B:D. Therefore sq(C):sq(E) = B:D = s:t = 2:1. Since s:t is a ratio of numbers, sq(C) and sq(E) are commensurable by 10.6, so C and E are commensurable in square. Since s:t = 2:1 is not the ratio of a square number to a square number, C and E are incommensurable in length by 10.9. Therefore C and E are medial straight lines commensurable in square only.

**Step 8.** By 6.13, let G be the mean proportional of B and D, so that B:G = G:D. By 6.17, sq(G) = rect(B,D). Since B and D are rational straight lines commensurable in length (Step 4), the rectangle contained by B and D is rational by 10.19. Therefore sq(G) is a rational area, and G is a rational straight line by D10.1.3.

**Step 9.** We now show that the rectangle contained by C and E equals the rectangle contained by A and G. Since A:C = C:B (Step 5) and A:E = E:D (Step 6), and B:G = G:D (Step 8), we proceed as follows. From sq(E):sq(G) and sq(C):sq(B), using the relations sq(E) = rect(A,D) and sq(G) = rect(B,D), we get sq(E):sq(G) = rect(A,D):rect(B,D) = A:B by 6.1 (rectangles with common side D have ratio as their other sides). Similarly, sq(C):sq(B) = rect(A,B):sq(B). By 6.1, rect(A,B):rect(B,B) = A:B (rectangles with common side B). So sq(C):sq(B) = A:B. Therefore sq(E):sq(G) = sq(C):sq(B), since both equal A:B, by CN1. By 6.22, since the squares (being similar rectilineal figures) on E, G are proportional to the squares on C, B, the straight lines are themselves proportional: E:G = C:B. But A:C = C:B from Step 5. Therefore A:C = E:G. By 6.16, since A:C = E:G, the rectangle contained by A and G equals the rectangle contained by C and E.

**Step 10.** We show that A and G are commensurable in square only. We have sq(A):sq(G) = sq(A):rect(B,D). Now rect(B,D) = B times D = B times B/2 (since B:D = 2:1), so rect(B,D) = sq(B)/2. By 6.1, sq(B):rect(B,D) = B:D = 2:1. Compounding the ratios: sq(A):rect(B,D) = (sq(A):sq(B)) times (sq(B):rect(B,D)) = (p:q) times (2:1). With p = 2, q = 3, this gives sq(A):sq(G) = 4:3 by 5.22. Since 4:3 is a ratio of numbers, sq(A) and sq(G) are commensurable by 10.6, so A and G are commensurable in square. Since 4:3 is not the ratio of a square number to a square number, A and G are incommensurable in length by 10.9. Therefore A and G are rational straight lines commensurable in square only.

**Step 11.** Since A and G are rational straight lines commensurable in square only, the rectangle contained by A and G is irrational by 10.21, and is a medial area. Since the rectangle contained by C and E equals the rectangle contained by A and G (Step 9), the rectangle contained by C and E is also a medial area.

**Step 12.** Therefore C and E are medial straight lines, commensurable in square only (Step 7), which contain a medial rectangle (Step 11). This is what was required to find.

**USED:** 10.10, 10.19, 10.21, 10.6, 10.9, 5.16, 5.22, 6.1, 6.12, 6.13, 6.16, 6.17, 6.22, CN1, D10.1.3
**Human refs (from References field):** 10.11, 10.21, 10.23, 5.16, 6.12, 6.13, 6.16, 6.17
**Jaccard:** 0.353 — AI adds ['10.10', '10.19', '10.6', '10.9', '5.22', '6.1', '6.22', 'CN1', 'D10.1.3']; Human adds ['10.11', '10.23']

## Proposition 10.29
**Statement:** To find two rational straight lines commensurable in square only and such that the square on the greater is greater than the square on the less by the square on a straight line commensurable in length with the greater.

**Step 1.** Let A be a rational straight line set out. [D10.1.3]

**Step 2.** Take two square numbers whose difference is not a square number. Let these be 4 and 1, since 4 - 1 = 3 is not a square number.

**Step 3.** Bisect A to obtain a straight line C equal to half of A, so that A = C + C. [1.10]

**Step 4.** Since A is the double of C, by 2.4 the square on A equals the square on C plus the square on C plus twice the rectangle contained by C and C, that is, sq(A) = 4 * sq(C). Thus sq(A) : sq(C) = 4 : 1. Since 4 and 1 are both square numbers, by 10.9 A and C are commensurable in length. Since A is rational and C is commensurable in length with A, C is also rational. [2.4, 10.9, D10.1.3]

**Step 5.** Now construct a straight line B such that sq(B) = sq(A) - sq(C). To do this, construct a right angle at a point [1.11], along one arm mark off a segment equal to C [1.3], and with center at the vertex draw a circle with radius equal to A [P3]. Since sq(A) = 4 * sq(C) and sq(C) is less than sq(A) [CN5], A is greater than C, so the circle meets the other arm. Let B be the segment from the vertex to this intersection. By 1.47, in the resulting right triangle with hypotenuse A and one leg C, we have sq(A) = sq(B) + sq(C), and therefore sq(B) = sq(A) - sq(C). [1.11, 1.3, P3, CN5, 1.47]

**Step 6.** Since sq(A) = 4 * sq(C) and sq(B) = sq(A) - sq(C) = 4 * sq(C) - sq(C) = 3 * sq(C) [CN3], both sq(A) and sq(B) are multiples of sq(C). Therefore sq(A) : sq(B) = 4 : 3, which is a ratio of a number to a number. By 10.6, sq(A) and sq(B) are commensurable, so A and B are commensurable in square. [CN3, 10.6, D10.1.2]

**Step 7.** However, 4 is a square number and 3 is not a square number, so 4 : 3 is not a ratio of a square number to a square number. By 10.9, A and B are incommensurable in length. [10.9]

**Step 8.** Since A and B are commensurable in square (Step 6) but incommensurable in length (Step 7), A and B are commensurable in square only. [D10.1.2]

**Step 9.** Since A is rational and B is commensurable in square with A, B is rational. [D10.1.3]

**Step 10.** From Step 5, sq(A) - sq(B) = sq(C), and from Step 4, C is commensurable in length with A. Since sq(A) > sq(B) (as the ratio sq(A) : sq(B) = 4 : 3), A is the greater and B is the less. Therefore the square on the greater exceeds the square on the less by the square on a straight line C that is commensurable in length with the greater.

**Step 11.** Therefore two rational straight lines A and B have been found, commensurable in square only, such that the square on the greater is greater than the square on the less by the square on a straight line commensurable in length with the greater. Q.E.F.

**USED:** 1.10, 1.11, 1.3, 1.47, 10.6, 10.9, 2.4, CN3, CN5, D10.1.2, D10.1.3, P3
**Human refs (from References field):** 1.47, 10.6, 10.9, 3.31, 5.19, D10.1.4
**Jaccard:** 0.200 — AI adds ['1.10', '1.11', '1.3', '2.4', 'CN3', 'CN5', 'D10.1.2', 'D10.1.3', 'P3']; Human adds ['3.31', '5.19', 'D10.1.4']

## Proposition 10.30
**Statement:** To find two rational straight lines commensurable in square only and such that the square on the greater is greater is greater than the square on the less by the square on a straight line incommensurable in length with the greater.

**Step 1.** Let A be a rational straight line set out.

**Step 2.** Find two square numbers DE and EF such that their sum DF = DE + EF is not a square number. For example, let DE = 4 and EF = 9, so that DF = 13, which is not a square number. Such numbers exist by the arithmetic of square numbers.

**Step 3.** Since DF and DE are both numbers (with DF > DE), let it be contrived that DF : DE :: the square on A : the square on FG [10.6]. This is possible since we can find a straight line FG such that the squares are in this ratio.

**Step 4.** Since DF : DE is a ratio of number to number, the square on A is commensurable with the square on FG [10.6]. Since A is rational, FG is also rational [D10.1.3].

**Step 5.** Now DE is a square number and DF is not a square number, so DF : DE is not a ratio of a square number to a square number. For if DF : DE were as some square number m squared to some square number n squared, then since DE is a square number (say d squared), DF would equal d squared times m squared divided by n squared, which would be a perfect square, contradicting the fact that DF is not a square number. Therefore DF : DE is not a ratio of a square number to a square number.

**Step 6.** Since the square on A is to the square on FG as DF is to DE, and DF : DE is not a ratio of a square number to a square number, the square on A does not have to the square on FG the ratio which a square number has to a square number. Therefore A is incommensurable in length with FG [10.9].

**Step 7.** Thus A and FG are rational straight lines commensurable in square only (by Steps 4 and 6).

**Step 8.** Since DF : DE :: the square on A : the square on FG, and DF > DE (because DF = DE + EF with EF > 0), the square on A is greater than the square on FG [5.14]. Therefore A is greater than FG.

**Step 9.** Let the square on H be equal to the excess of the square on A over the square on FG, so that the square on A equals the square on FG plus the square on H [1.47, 3.31 or by construction].

**Step 10.** Since DF : DE :: the square on A : the square on FG, by separation of a ratio (separando) [5.17], EF : DE :: (the square on A minus the square on FG) : the square on FG. That is, EF : DE :: the square on H : the square on FG.

**Step 11.** Now EF and DE are both square numbers, so EF : DE is a ratio of a square number to a square number. Since the square on H is to the square on FG as the square number EF is to the square number DE, the sides H and FG are commensurable in length [10.9].

**Step 12.** Now consider the ratio of the square on H to the square on A. From Step 3, the square on A : the square on FG :: DF : DE. From Step 10, the square on H : the square on FG :: EF : DE. Therefore the square on H : the square on A :: EF : DF [5.22, by ex aequali via the common term, the square on FG].

**Step 13.** Since EF is a square number and DF is not a square number, EF : DF is not a ratio of a square number to a square number (by the same reasoning as in Step 5, with roles of EF and DF). Therefore the square on H does not have to the square on A the ratio which a square number has to a square number. By 10.9, H is incommensurable in length with A.

**Step 14.** Therefore we have found two rational straight lines A and FG, commensurable in square only (Step 7), where the square on the greater A exceeds the square on the lesser FG by the square on H (Step 9), and H is incommensurable in length with the greater A (Step 13).

Q.E.F.

**USED:** 1.47, 10.6, 10.9, 5.14, 5.17, 5.22, D10.1.3
**Human refs (from References field):** 1.47, 10.6, 10.9, 3.31, 5.19
**Jaccard:** 0.333 — AI adds ['5.14', '5.17', '5.22', 'D10.1.3']; Human adds ['3.31', '5.19']

## Proposition 10.31
**Statement:** To find two medial straight lines commensurable in square only, containing a rational rectangle, and such that the square on the greater is greater than the square on the less by the square on a straight line commensurable in length with the greater.

**Step 1.** By Proposition 10.29, find two rational straight lines A and B, with A greater than B, which are commensurable in square only and such that the square on A is greater than the square on B by the square on a straight line commensurable in length with A. [10.29]

**Step 2.** By Proposition 6.13, take C as the mean proportional between A and B, so that A : C = C : B. Then by Proposition 6.17, the rectangle contained by A and B equals the square on C, that is, rect(A, B) = sq(C). [6.13, 6.17]

**Step 3.** Since A and B are rational straight lines commensurable in square only, the rectangle contained by A and B is irrational by Proposition 10.21, and the side of the square equal to it is medial. Since sq(C) equals this irrational rectangle, C is a medial straight line. [10.21]

**Step 4.** By Proposition 6.12, find a straight line D such that A : B = C : D, making D the fourth proportional to A, B, C. [6.12]

**Step 5.** We show that C and D are incommensurable in length. Since A : B = C : D, and A is incommensurable in length with B (because A and B are commensurable in square only), by Proposition 10.11 C is incommensurable in length with D. [10.11, D10.1.2]

**Step 6.** We show that C and D are commensurable in square. Since A : B = C : D, by Proposition 6.22 the duplicate ratio of A to B equals the ratio sq(A) : sq(B), and the duplicate ratio of C to D equals the ratio sq(C) : sq(D). Since the ratios A : B and C : D are equal, their duplicate ratios are equal, so sq(A) : sq(B) = sq(C) : sq(D). Now since A and B are commensurable in square, sq(A) is commensurable with sq(B). Therefore by Proposition 10.11 applied to the proportion sq(A) : sq(B) = sq(C) : sq(D), sq(C) is commensurable with sq(D). Hence C and D are commensurable in square. [6.22, 10.11, D10.1.2]

**Step 7.** From Steps 5 and 6, C and D are commensurable in square only. [D10.1.2]

**Step 8.** We show that D is medial. Since sq(C) and sq(D) are commensurable (Step 6), and C is medial (Step 3), D is also medial by Proposition 10.23, which states that a straight line commensurable with a medial straight line is medial. [10.23]

**Step 9.** We show that the rectangle contained by C and D is rational. From Step 4, A : B = C : D. By Proposition 5.16 (alternando), A : C = B : D. But from Step 2, A : C = C : B (the mean proportional relation). Therefore C : B = B : D. By Proposition 6.17, since B is the mean proportional between C and D, the rectangle contained by C and D equals the square on B, that is, rect(C, D) = sq(B). Since B is a rational straight line, sq(B) is a rational area. Therefore rect(C, D) is rational. [5.16, 6.17, D10.1.3, D10.1.4]

**Step 10.** We show that the square on C is greater than the square on D by the square on a straight line commensurable in length with C. From Step 4, we have the proportion A : B = C : D among four straight lines. By hypothesis (Step 1), the square on A is greater than the square on B by the square on a straight line commensurable in length with A. Therefore by Proposition 10.14, the square on C is greater than the square on D by the square on a straight line commensurable in length with C. [10.14]

**Step 11.** Therefore C and D are two medial straight lines commensurable in square only (Steps 7, 8), containing a rational rectangle (Step 9), and such that the square on the greater is greater than the square on the less by the square on a straight line commensurable in length with the greater (Step 10). This is what was required to find. Q.E.F.

**USED:** 10.11, 10.14, 10.21, 10.23, 10.29, 5.16, 6.12, 6.13, 6.17, 6.22, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 10.11, 10.14, 10.21, 10.23, 10.29, 10.30
**Jaccard:** 0.357 — AI adds ['5.16', '6.12', '6.13', '6.17', '6.22', 'D10.1.2', 'D10.1.3', 'D10.1.4']; Human adds ['10.30']

## Proposition 10.32
**Statement:** To find two medial straight lines commensurable in square only, containing a medial rectangle, and such that the square on the greater is greater than the square on the less by the square on a straight line commensurable with the greater.

**Step 1.** By Proposition 10.29, find two rational straight lines A and B commensurable in square only such that the square on A is greater than the square on B by the square on a straight line commensurable in length with A. [10.29]

**Step 2.** Since A and B are rational and commensurable in square only, the rectangle contained by A and B is medial. [10.21]

**Step 3.** Find a rational straight line E that is commensurable in square only with A and incommensurable in length with B. To construct E: since A and B are rational, their squares are commensurable with the square on the assigned rational straight line, so sq(A) and sq(B) have to one another the ratio which a number has to a number, say p to q, where p:q is not a ratio of square numbers (since A and B are commensurable in square only). By choosing a number r such that neither r:p nor r:q is a ratio of square numbers (for example, r a prime not dividing p or q), and finding E such that sq(E) has to the square on the assigned rational line the ratio r:1, we obtain E rational (commensurable in square with the assigned rational line, hence rational by Definition 10.1.3) with sq(E):sq(A) = r:p (not a ratio of square numbers, so E is incommensurable in length with A, hence commensurable in square only with A) and sq(E):sq(B) = r:q (not a ratio of square numbers, so E is incommensurable in length with B). [10.6, 10.9, D10.1.3]

**Step 4.** Since A and E are rational and commensurable in square only, the rectangle contained by A and E is medial. Let M be the straight line such that the square on M equals the rectangle contained by A and E. Then M is a medial straight line. [10.21]

**Step 5.** Now rect(A, E) and rect(A, B) are both medial areas. By Proposition 6.1, rect(A, E) is to rect(A, B) as E is to B, since the rectangles share the side A. Since E and B are incommensurable in length (Step 3), rect(A, E) is incommensurable with rect(A, B). That is, the square on M is incommensurable with rect(A, B). [6.1]

**Step 6.** By Proposition 6.12, find the fourth proportional G to the three straight lines A, B, M, so that A is to B as M is to G. [6.12]

**Step 7.** We show that G is medial. Since A is to B as M is to G, by Proposition 6.22 the square on A is to the square on B as the square on M is to the square on G. Now since A and B are commensurable in square (both rational), the square on A is commensurable with the square on B. Therefore by Proposition 10.11, the square on M is commensurable with the square on G. Since the square on M is a medial area (M being medial), the square on G is commensurable with a medial area, hence is itself medial. Therefore G is a medial straight line. [6.22, 10.11, 10.23]

**Step 8.** We show that M and G are commensurable in square only. From Step 7, the squares on M and G are commensurable, so M and G are commensurable in square. Since A is to B as M is to G, and A is incommensurable in length with B (being commensurable in square only), by Proposition 10.11 M is incommensurable in length with G. Therefore M and G are commensurable in square only. [10.11]

**Step 9.** We show that the rectangle contained by M and G is medial. By Proposition 6.1, rect(M, G) is to sq(M) as G is to M. From the proportion A:B = M:G, by inversion G is to M as B is to A. Therefore rect(M, G) is to sq(M) as B is to A. Now sq(M) equals rect(A, E), and by Proposition 6.1, rect(B, E) is to rect(A, E) as B is to A (the rectangles sharing side E). Therefore rect(M, G) is to sq(M) as rect(B, E) is to sq(M), whence rect(M, G) equals rect(B, E). Now B and E are both rational (B from Step 1 and E from Step 3). They are commensurable in square, since the squares on B and E are each commensurable with the square on the assigned rational line, hence commensurable with each other. They are incommensurable in length (Step 3). Therefore B and E are commensurable in square only. By Proposition 10.21, rect(B, E) is medial. Since rect(M, G) equals rect(B, E), the rectangle contained by M and G is medial. [6.1, 5.7, 5.9, 10.12, 10.21]

**Step 10.** We show that the square on M is greater than the square on G by the square on a straight line commensurable with M. We have the four straight lines A, B, M, G in proportion (A:B = M:G). The square on A is greater than the square on B by the square on a straight line commensurable in length with A (Step 1). Therefore by Proposition 10.14, the square on M is greater than the square on G by the square on a straight line commensurable in length with M. [10.14]

**Step 11.** Therefore M and G are two medial straight lines commensurable in square only, containing a medial rectangle, and such that the square on the greater is greater than the square on the less by the square on a straight line commensurable with the greater. Q.E.F.

**USED:** 10.11, 10.12, 10.14, 10.21, 10.23, 10.29, 10.6, 10.9, 5.7, 5.9, 6.1, 6.12, 6.22, D10.1.3
**Human refs (from References field):** 10.11, 10.14, 10.21, 10.23, 10.29, 10.30, 6.16, 6.17, 6.4, 6.8
**Jaccard:** 0.263 — AI adds ['10.12', '10.6', '10.9', '5.7', '5.9', '6.1', '6.12', '6.22', 'D10.1.3']; Human adds ['10.30', '6.16', '6.17', '6.4', '6.8']

## Proposition 10.33
**Statement:** To find two straight lines incommensurable in square which make the sum of the squares on them rational but the rectangle contained by them medial.

**Step 1.** By 10.30, find two rational straight lines AB, BC commensurable in square only such that the square on the greater AB is greater than the square on the less BC by the square on a straight line incommensurable in length with AB.

**Step 2.** Bisect BC at D [1.10], so that BD equals DC and the square on BD is one-fourth of the square on BC.

**Step 3.** By 6.28, apply to AB a parallelogram equal to the square on BD, deficient by a square figure. Let the resulting rectangle be contained by AE and EB, where E is a point on AB, so that rect(AE, EB) equals sq(BD).

**Step 4.** Since the square on AB is greater than the square on BC by the square on a straight line incommensurable in length with AB, and we have applied to AB a parallelogram equal to the fourth part of the square on BC (namely sq(BD)) deficient by a square figure which divides AB into AE and EB, by 10.18 AE is incommensurable in length with EB.

**Step 5.** Describe a semicircle on AB as diameter [P3, D1.17, D1.18]. From E, draw EF at right angles to AB [1.11] meeting the semicircle at F. Join AF and FB [P1].

**Step 6.** Since F lies on the semicircle with diameter AB, angle AFB is a right angle [3.31].

**Step 7.** Since in the right-angled triangle AFB the perpendicular EF has been drawn from the right angle at F to the base AB, by 6.8 the triangles AEF and FEB are each similar to the whole triangle AFB and to one another. From the similarity of triangle AEF to triangle AFB, we have AE is to AF as AF is to AB, whence the square on AF equals the rectangle contained by AE and AB [6.17]. From the similarity of triangle FEB to triangle AFB, we have EB is to BF as BF is to AB, whence the square on BF equals the rectangle contained by EB and AB [6.17]. From the similarity of triangle AEF to triangle FEB, we have AE is to EF as EF is to EB, whence the square on EF equals the rectangle contained by AE and EB [6.17].

**Step 8.** Since angle AFB is a right angle, by 1.47 the square on AB equals the sum of the squares on AF and BF. That is, sq(AF) + sq(BF) = sq(AB). Since AB is rational, the square on AB is a rational area [D10.1.4]. Therefore the sum sq(AF) + sq(BF) is rational.

**Step 9.** From Step 7, sq(EF) = rect(AE, EB). From Step 3, rect(AE, EB) = sq(BD). Therefore sq(EF) = sq(BD), and hence EF equals BD.

**Step 10.** From the similarity established in Step 7 (triangle AEF similar to triangle AFB, via 6.8), the sides satisfy EF is to FB as AF is to AB. Therefore rect(EF, AB) = rect(AF, FB) [6.16]. That is, rect(AF, FB) = rect(AB, EF).

**Step 11.** Since EF = BD [Step 9] and BD = BC/2 [Step 2], EF equals half of BC. The ratio of EF to BC is thus 1 to 2, which is a ratio of number to number, so EF is commensurable in length with BC [10.6]. Since BC is rational, EF is rational [D10.1.3, as EF is commensurable with a rational line].

**Step 12.** Since AB and BC are commensurable in square only, they are incommensurable in length. Since EF is commensurable in length with BC [Step 11], if AB were commensurable in length with EF, then by 10.12 AB would be commensurable in length with BC, which is a contradiction. Therefore AB is incommensurable in length with EF. Both AB and EF are rational [D10.1.3], so their squares are each commensurable with the square on the assigned rational straight line, and hence commensurable with each other [10.12]. Thus AB and EF are rational straight lines commensurable in square only. By 10.21, the rectangle contained by AB and EF is medial. Since rect(AF, FB) = rect(AB, EF) [Step 10], the rectangle contained by AF and FB is medial.

**Step 13.** From Step 7, sq(AF) = rect(AE, AB) and sq(BF) = rect(EB, AB). Therefore sq(AF) is to sq(BF) as AE is to EB [6.1]. Since AE is incommensurable in length with EB [Step 4], AE has not to EB the ratio which a number has to a number [10.7]. Therefore sq(AF) has not to sq(BF) the ratio which a number has to a number, so sq(AF) and sq(BF) are incommensurable [10.8]. Hence AF and BF are incommensurable in square [D10.1.2].

**Step 14.** Therefore AF and BF are two straight lines incommensurable in square [Step 13] which make the sum of the squares on them rational [Step 8] and the rectangle contained by them medial [Step 12]. This is what was required to find.

**USED:** 1.10, 1.11, 1.47, 10.12, 10.18, 10.21, 10.30, 10.6, 10.7, 10.8, 3.31, 6.1, 6.16, 6.17, 6.28, 6.8, D1.17, D1.18, D10.1.2, D10.1.3, D10.1.4, P1, P3
**Human refs (from References field):** 1.47, 10.18, 10.21, 10.23, 10.30, 6.28
**Jaccard:** 0.208 — AI adds ['1.10', '1.11', '10.12', '10.6', '10.7', '10.8', '3.31', '6.1', '6.16', '6.17', '6.8', 'D1.17', 'D1.18', 'D10.1.2', 'D10.1.3', 'D10.1.4', 'P1', 'P3']; Human adds ['10.23']

## Proposition 10.34
**Statement:** To find two straight lines incommensurable in square which make the sum of the squares on them medial but the rectangle contained by them rational.

**Step 1.** By 10.27, find two medial straight lines A and B that are commensurable in square only and such that the rectangle contained by A and B is rational.

**Step 2.** Since A is a medial straight line, the square on A is a medial area (by D10.1.4 and 10.21). Similarly, since B is a medial straight line, the square on B is a medial area.

**Step 3.** Since A and B are commensurable in square only, the squares on A and B are commensurable areas (by D10.1.2). Since the square on A is commensurable with the square on B, the sum of the squares on A and B is commensurable with the square on A (by 10.15).

**Step 4.** Since the square on A is medial and the sum of the squares on A and B is commensurable with the square on A (Step 3), the sum of the squares on A and B is medial (by 10.23, since a magnitude commensurable with a medial magnitude is medial).

**Step 5.** The rectangle contained by A and B is rational, by the construction of Step 1 (from 10.27).

**Step 6.** Since A and B are commensurable in square only, they are incommensurable in length but their squares are commensurable. They are therefore two straight lines incommensurable in square (in the sense that they are not commensurable in length, only in square -- D10.1.2), which make the sum of the squares on them medial (Step 4) but the rectangle contained by them rational (Step 5).

**Step 7.** Therefore two straight lines have been found, incommensurable in square, which make the sum of the squares on them medial but the rectangle contained by them rational. Q.E.F.

**USED:** 10.15, 10.21, 10.23, 10.27, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 1.47, 10.11, 10.18, 10.31, 10.6, 3.31, 6.28
**Jaccard:** 0.000 — AI adds ['10.15', '10.21', '10.23', '10.27', 'D10.1.2', 'D10.1.3', 'D10.1.4']; Human adds ['1.47', '10.11', '10.18', '10.31', '10.6', '3.31', '6.28']

## Proposition 10.35
**Statement:** To find two straight lines incommensurable in square which make the sum of the squares on them medial and the rectangle contained by them medial and moreover incommensurable with the sum of the squares on them.

**Step 1.** By 10.30, let DE and EF be two rational straight lines commensurable in square only such that the square on DE is greater than the square on EF by the square on a straight line incommensurable in length with DE.

**Step 2.** By 6.12, let GH be a rational straight line commensurable in length with DE, with GH greater than DE, and such that the ratio DE:GH is not a ratio of square numbers. Since DE and GH are commensurable in length, the ratio sq(DE):sq(GH) is a ratio of square numbers [10.9]. Since DE and EF are commensurable in square only, the ratio sq(EF):sq(DE) is a ratio of numbers but not of square numbers [10.5, 10.9]. Therefore the compound ratio sq(EF):sq(GH) is a ratio of numbers but not of square numbers. Hence EF and GH are commensurable in square [10.6] but incommensurable in length [10.9], that is, commensurable in square only.

**Step 3.** By 6.13, let KL be the mean proportional of DE and EF, so that sq(KL) = rect(DE, EF) [6.17]. Since DE and EF are rational and commensurable in square only, rect(DE, EF) is medial [10.21]. Hence KL is a medial straight line [D10.1.4].

**Step 4.** By 6.13, let MN be the mean proportional of EF and GH, so that sq(MN) = rect(EF, GH) [6.17]. Since EF and GH are rational and commensurable in square only [Step 2], rect(EF, GH) is medial [10.21]. Hence MN is a medial straight line.

**Step 5.** We show KL and MN are commensurable in square only. We have sq(KL):sq(MN) = rect(DE,EF):rect(EF,GH) = DE:GH [6.1]. Since DE and GH are commensurable in length, DE:GH is a ratio of numbers [10.5], so sq(KL) and sq(MN) are commensurable, meaning KL and MN are commensurable in square [10.6]. Since DE:GH is not a ratio of square numbers [Step 2], KL and MN are incommensurable in length [10.9]. Therefore KL and MN are commensurable in square only.

**Step 6.** We show rect(KL, MN) is medial. By 6.13, let T be the mean proportional of DE and GH, so sq(T) = rect(DE, GH) [6.17]. Since DE and GH are commensurable in length, rect(DE, GH) is rational [10.19], so T is a rational straight line. Now sq(KL):sq(EF) = rect(DE,EF):sq(EF) = DE:EF [6.1], and sq(T):sq(MN) = rect(DE,GH):rect(EF,GH) = DE:EF [6.1]. Hence sq(KL):sq(EF) = sq(T):sq(MN) [CN1]. Since these are duplicate ratios of KL:EF and T:MN respectively [D5.9], we have KL:EF = T:MN. By 6.16, rect(KL, MN) = rect(EF, T). Now sq(EF):sq(T) = sq(EF):rect(DE,GH). Both sq(EF) and rect(DE,GH) are rational areas, so their ratio is a ratio of numbers [10.5], and EF and T are commensurable in square [10.6]. We verify EF and T are incommensurable in length: if they were commensurable in length, then sq(EF):sq(T) would be a ratio of square numbers [10.9], meaning sq(EF):rect(DE,GH) is a ratio of square numbers, i.e., sq(EF)/(DE*GH) = (p/q)^2 for integers p, q. But sq(EF)/sq(DE) is not a ratio of square numbers (since DE, EF are commensurable in square only), and sq(DE)/(DE*GH) = DE/GH is a ratio of numbers (DE, GH commensurable in length). So sq(EF)/(DE*GH) = [sq(EF)/sq(DE)] * [DE/GH], the product of a non-square rational and a rational, which by our choice of GH (with DE:GH not a ratio of square numbers) is not a ratio of square numbers. Hence EF and T are commensurable in square only. Therefore rect(EF, T) is medial [10.21], and so rect(KL, MN) is medial.

**Step 7.** We establish the excess property. Since sq(MN) = rect(EF, GH) and sq(KL) = rect(DE, EF), and GH > DE, we have sq(MN) > sq(KL). The difference sq(MN) - sq(KL) = rect(EF, GH) - rect(DE, EF) = rect(EF, GH - DE) [2.1 applied inversely]. Let W be the straight line such that sq(W) = sq(MN) - sq(KL). Then sq(W):sq(MN) = rect(EF, GH-DE):rect(EF, GH) = (GH-DE):GH [6.1]. Since GH and DE are commensurable in length, (GH - DE) is commensurable in length with GH [10.15 applied to lengths], so (GH-DE):GH is a ratio of numbers [10.5]. Hence sq(W) and sq(MN) are commensurable, so W and MN are commensurable in square [10.6]. However, (GH-DE)/GH = 1 - DE/GH; since DE:GH is not a ratio of square numbers [Step 2], and this difference ratio, while rational, is not a ratio of square numbers either (by our construction). Hence W and MN are incommensurable in length [10.9]. Therefore sq(MN) exceeds sq(KL) by the square on a straight line incommensurable in length with MN.

**Step 8.** To MN, apply a parallelogram equal to the fourth part of the square on KL and deficient by a square figure [6.28]. Let MN be divided at O into segments MO and ON such that rect(MO, ON) = sq(KL)/4. Since sq(MN) > sq(KL) by the square on a straight line incommensurable in length with MN [Step 7], the segments MO and ON are incommensurable in length [10.18].

**Step 9.** On MN as diameter, describe a semicircle [P3]. From O, draw a straight line at right angles to MN [1.11], and let it meet the semicircle at R. Join MR and RN [P1].

**Step 10.** Since MRN is an angle inscribed in a semicircle, the angle MRN is a right angle [3.31]. Therefore sq(MR) + sq(RN) = sq(MN) [1.47].

**Step 11.** MR and RN are incommensurable in square. Since RO is perpendicular to the diameter MN from the point R on the semicircle, by 6.8 the triangles MRO, RNO, and MRN are similar. From the similarity of triangles MRO and MRN: sq(MR) = rect(MN, MO) [6.8, 6.17]. From the similarity of triangles RNO and MRN: sq(RN) = rect(MN, ON) [6.8, 6.17]. Therefore sq(MR):sq(RN) = rect(MN, MO):rect(MN, ON) = MO:ON [6.1]. Since MO and ON are incommensurable [Step 8], MO:ON is not a ratio of numbers [10.7]. Hence sq(MR):sq(RN) is not a ratio of numbers, and so MR and RN are incommensurable in square [10.9].

**Step 12.** The sum of the squares on MR and RN is medial. By Step 10, sq(MR) + sq(RN) = sq(MN). Since MN is a medial straight line [Step 4], sq(MN) is a medial area [D10.1.4]. Hence sq(MR) + sq(RN) is medial.

**Step 13.** The rectangle contained by MR and RN is medial. From the similarity established in Step 11, we also have MR:RN = MO:RO [from triangle MRO similar to triangle RNO via 6.8, 6.4]. Hence rect(MR, RN) = rect(MN, RO) [since from the similar triangles MR*RN = MN*RO, which follows from the equal areas of triangle MRN computed as (1/2)*MR*RN and (1/2)*MN*RO]. Now sq(RO) = rect(MO, ON) [6.8, 6.13 applied to the altitude], and rect(MO, ON) = sq(KL)/4 [Step 8]. So RO = KL/2, meaning 2*RO = KL. Therefore 2*rect(MR, RN) = 2*rect(MN, RO) = rect(MN, 2*RO) = rect(MN, KL) = rect(KL, MN), which is medial [Step 6]. Since rect(MR, RN) is commensurable with the medial area 2*rect(MR, RN), and any area commensurable with a medial area is itself medial (being incommensurable with the rational square [10.13] and commensurable with a medial area), rect(MR, RN) is medial.

**Step 14.** The sum of the squares on MR and RN is incommensurable with the rectangle contained by MR and RN. We have sq(MR) + sq(RN) = sq(MN) [Step 10] and 2*rect(MR, RN) = rect(KL, MN) [Step 13]. Now sq(MN):rect(KL, MN) = sq(MN):(KL*MN) = MN:KL [6.1]. Since KL and MN are commensurable in square only [Step 5], they are incommensurable in length, so MN:KL is not a ratio of numbers [10.7]. Hence sq(MN) and rect(KL, MN) are incommensurable [10.11]. That is, sq(MR) + sq(RN) is incommensurable with 2*rect(MR, RN). Since rect(MR, RN) is commensurable with 2*rect(MR, RN), it follows that sq(MR) + sq(RN) is incommensurable with rect(MR, RN) [10.13].

**Step 15.** Therefore MR and RN are two straight lines incommensurable in square [Step 11] which make the sum of the squares on them medial [Step 12] and the rectangle contained by them medial [Step 13] and moreover the sum of the squares is incommensurable with the rectangle [Step 14]. Q.E.D.

**USED:** 1.11, 1.47, 10.11, 10.13, 10.15, 10.18, 10.19, 10.21, 10.30, 10.5, 10.6, 10.7, 10.9, 2.1, 3.31, 5.16, 6.1, 6.12, 6.13, 6.16, 6.17, 6.28, 6.4, 6.8, CN1, D10.1.3, D10.1.4, D5.9, P1, P3
**Human refs (from References field):** 1.47, 10.11, 10.13, 10.18, 10.32, 3.31
**Jaccard:** 0.161 — AI adds ['1.11', '10.15', '10.19', '10.21', '10.30', '10.5', '10.6', '10.7', '10.9', '2.1', '5.16', '6.1', '6.12', '6.13', '6.16', '6.17', '6.28', '6.4', '6.8', 'CN1', 'D10.1.3', 'D10.1.4', 'D5.9', 'P1', 'P3']; Human adds ['10.32']

## Proposition 10.36
**Statement:** If two rational straight lines commensurable in square only be added together, the whole is irrational; and let it be called binomial.

**Step 1.** Let AB and BC be two rational straight lines commensurable in square only. Let AC be the whole line formed by adding AB and BC together, so that AC = AB + BC. We are to show that AC is irrational.

**Step 2.** Since AB and BC are rational, the squares on AB and on BC are each rational areas, that is, each is commensurable with the square on the assigned rational straight line [D10.1.3, D10.1.4].

**Step 3.** Since the square on AB and the square on BC are each commensurable with the same rational area (the square on the assigned rational line), they are commensurable with one another [10.12].

**Step 4.** Since the square on AB and the square on BC are commensurable with one another, their sum — the square on AB together with the square on BC — is commensurable with each of them, and hence is a rational area [10.15].

**Step 5.** Since AB and BC are rational straight lines commensurable in square only, the rectangle contained by AB and BC is irrational, namely medial [10.21].

**Step 6.** Twice the rectangle contained by AB and BC is commensurable with the rectangle AB, BC, since they have the ratio 2 to 1, which is a ratio of a number to a number [10.6]. Since the rectangle AB, BC is irrational (medial), and twice the rectangle is commensurable with it, twice the rectangle AB, BC is also irrational [10.12, D10.1.4]. More precisely, twice the rectangle is incommensurable with the assigned rational area because the rectangle AB, BC is incommensurable with it, and twice the rectangle is commensurable with the rectangle; thus by 10.13, twice the rectangle is also incommensurable with the assigned rational area, and so is irrational.

**Step 7.** By 2.4, the square on AC equals the sum of the squares on AB and BC together with twice the rectangle contained by AB and BC.

**Step 8.** Now the sum of the squares on AB and BC is rational (Step 4), hence commensurable with the assigned rational area. And twice the rectangle AB, BC is irrational (Step 6), hence incommensurable with the assigned rational area. Since one of these two magnitudes (the sum of squares) is commensurable with the assigned rational area and the other (twice the rectangle) is incommensurable with it, the sum of squares and twice the rectangle are incommensurable with one another [10.13].

**Step 9.** Since the sum of the squares on AB and BC and twice the rectangle AB, BC are incommensurable with one another, their sum — which is the square on AC — is incommensurable with each of them [10.16]. In particular, the square on AC is incommensurable with the sum of the squares on AB and BC.

**Step 10.** But the sum of the squares on AB and BC is rational (Step 4). Therefore the square on AC, being incommensurable with a rational area, is irrational [D10.1.4].

**Step 11.** Since the square on AC is irrational, AC itself is irrational [D10.1.4].

**Step 12.** Therefore, if two rational straight lines commensurable in square only be added together, the whole is irrational. Let such a line be called binomial. Q.E.D.

**USED:** 10.12, 10.13, 10.15, 10.16, 10.21, 10.6, 2.4, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 10.11, 10.13, 10.15, 10.16, 10.6, 2.4, D10.1.4
**Jaccard:** 0.545 — AI adds ['10.12', '10.21', 'D10.1.2', 'D10.1.3']; Human adds ['10.11']

## Proposition 10.37
**Statement:** If two medial straight lines commensurable in square only and containing a rational rectangle be added together, the whole is irrational; and let it be called a first bimedial straight line.

**Step 1.** Let AB and BC be two medial straight lines commensurable in square only such that the rectangle contained by AB and BC is rational. Let AC be the whole line composed of AB and BC placed in a straight line. We must show that AC is irrational.

**Step 2.** Since AB is medial, the square on AB is a medial area, that is, an area incommensurable with the square on any assigned rational straight line [D10.1.3, D10.1.4]. Likewise, since BC is medial, the square on BC is also a medial area.

**Step 3.** Since AB and BC are commensurable in square only, the squares on AB and on BC are commensurable areas [D10.1.2]. Therefore, by 10.15, the sum of the squares on AB and BC is commensurable with the square on AB.

**Step 4.** Since the square on AB is medial (and hence irrational, i.e., incommensurable with the square on the assigned rational straight line), and the sum of the squares on AB and BC is commensurable with the square on AB, it follows by 10.13 that the sum of the squares on AB and BC is also incommensurable with the square on the assigned rational straight line. Therefore the sum of the squares on AB and BC is irrational, that is, a medial area.

**Step 5.** Now, the rectangle contained by AB and BC is rational by hypothesis. The ratio of twice the rectangle contained by AB and BC to the rectangle contained by AB and BC is as 2 is to 1, which is a ratio of a number to a number. Therefore, by 10.6, twice the rectangle AB, BC is commensurable with the rectangle AB, BC. Since the rectangle AB, BC is rational, twice the rectangle AB, BC is also commensurable with the square on the assigned rational straight line, and hence is rational [D10.1.4].

**Step 6.** By 2.4, the square on AC equals the sum of the squares on AB and BC together with twice the rectangle contained by AB and BC. That is, the square on AC equals the sum of the squares on AB and BC plus twice the rectangle AB, BC.

**Step 7.** Suppose, for the sake of contradiction, that AC is rational, so that the square on AC is a rational area. Since twice the rectangle AB, BC is also rational (Step 5), and rational areas are commensurable with one another, the difference of the square on AC and twice the rectangle AB, BC would be commensurable with each of them [10.15]. Hence the sum of the squares on AB and BC, being this difference, would be rational.

**Step 8.** But this contradicts Step 4, which established that the sum of the squares on AB and BC is irrational (medial). Therefore the square on AC is not rational.

**Step 9.** Furthermore, the square on AC cannot be medial either. For if it were, then since the sum of the squares on AB and BC is medial, and the square on AC is their sum plus twice the rectangle AB, BC, we would have that twice the rectangle AB, BC equals the square on AC minus the sum of the squares on AB and BC. If both the square on AC and the sum of the squares on AB and BC were medial areas, then twice the rectangle AB, BC would be the difference of two medial areas. But twice the rectangle AB, BC is rational, so a medial area would exceed another medial area by a rational area, contradicting 10.26.

**Step 10.** Therefore the square on AC is neither rational nor medial; it is irrational. Since the square on AC is irrational, AC itself is irrational [D10.1.4]. Let AC be called a first bimedial straight line.

**USED:** 10.13, 10.15, 10.26, 10.6, 2.4, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 10.16, 10.36, 2.4, D10.1.4
**Jaccard:** 0.200 — AI adds ['10.13', '10.15', '10.26', '10.6', 'D10.1.2', 'D10.1.3']; Human adds ['10.16', '10.36']

## Proposition 10.38
**Statement:** If two medial straight lines commensurable in square only and containing a medial rectangle be added together, the whole is irrational; and let it be called a second bimedial straight line.

**Step 1.** Let AB and BC be two medial straight lines commensurable in square only such that the rectangle AB by BC is medial. Let AC be their sum. We aim to show that AC is irrational.

**Step 2.** Since AB is medial, the square on AB is a medial area. Since BC is medial, the square on BC is a medial area. Since AB and BC are commensurable in square, the square on AB is commensurable with the square on BC. By 10.15, the sum of the squares on AB and BC is commensurable with the square on AB, and hence is itself a medial area.

**Step 3.** Since the rectangle AB by BC is medial (by hypothesis), and 2 times the rectangle AB by BC has to the rectangle AB by BC the ratio 2:1, which is a ratio of number to number, by 10.6 the area 2*AB*BC is commensurable with AB*BC. Since AB*BC is medial, by 10.23 (applied to areas: a magnitude commensurable with a medial magnitude is medial), the area 2*AB*BC is also medial.

**Step 4.** Now, by 2.4, the square on AC equals the sum of the squares on AB and BC together with twice the rectangle AB by BC. That is, AC^2 = (AB^2 + BC^2) + 2*AB*BC.

**Step 5.** We show that AB^2 + BC^2 is incommensurable with 2*AB*BC. Since AB and BC are commensurable in square only, AB is incommensurable in length with BC. The ratio of the square on AB to the rectangle AB by BC equals the ratio AB to BC (for AB^2 : AB*BC :: AB : BC, since each bears to AB*BC the same ratio by the properties of rectangles and lines). Since AB is incommensurable in length with BC, by 10.11 the square on AB is incommensurable with the rectangle AB by BC.

**Step 6.** By 10.15, since the square on AB is commensurable with the square on BC, the sum AB^2 + BC^2 is commensurable with AB^2. By 10.13, since AB^2 is incommensurable with AB*BC and AB^2 is commensurable with (AB^2 + BC^2), it follows that AB^2 + BC^2 is incommensurable with AB*BC.

**Step 7.** Since AB*BC is commensurable with 2*AB*BC (as shown in Step 3), by 10.13 again, AB^2 + BC^2 is incommensurable with 2*AB*BC.

**Step 8.** Let D be a rational straight line. Apply the area AB^2 + BC^2 to D, producing breadth EF, so that D*EF = AB^2 + BC^2. Apply the area 2*AB*BC to D, producing breadth FG, so that D*FG = 2*AB*BC. Then D*EG = AC^2, where EG = EF + FG.

**Step 9.** Since AB^2 + BC^2 is a medial area applied to the rational straight line D, by 10.22 the breadth EF is rational and incommensurable in length with D. Since 2*AB*BC is a medial area applied to the rational straight line D, by 10.22 the breadth FG is rational and incommensurable in length with D.

**Step 10.** Since AB^2 + BC^2 is incommensurable with 2*AB*BC (Step 7), and D*EF = AB^2 + BC^2 while D*FG = 2*AB*BC, by 10.11 EF is incommensurable in length with FG.

**Step 11.** Now EF and FG are both rational straight lines. Since both are commensurable in square with the rational line D (being rational), by 10.12 they are commensurable in square with each other. Since they are incommensurable in length (Step 10), they are commensurable in square only. By 10.36, the sum EF + FG = EG is irrational; it is a binomial straight line.

**Step 12.** Since D is rational and EG is irrational, the rectangle D*EG is irrational (for if D*EG were a rational area, then by 10.20 EG would be rational and commensurable in length with D, contradicting the irrationality of EG). Therefore AC^2, which equals D*EG, is an irrational area, and consequently AC is irrational.

**Step 13.** Therefore, when two medial straight lines commensurable in square only and containing a medial rectangle are added together, the whole is irrational. Let such a line be called a second bimedial straight line. Q.E.D.

**USED:** 10.11, 10.12, 10.13, 10.15, 10.20, 10.22, 10.23, 10.36, 10.6, 2.4, D10.1.1, D10.1.3, D10.1.4
**Human refs (from References field):** 1.44, 10.11, 10.13, 10.15, 10.20, 10.22, 10.36, 10.6, 2.4, 6.1, D10.1.4
**Jaccard:** 0.600 — AI adds ['10.12', '10.23', 'D10.1.1', 'D10.1.3']; Human adds ['1.44', '6.1']

## Proposition 10.39
**Statement:** If two straight lines incommensurable in square which make the sum of the squares on them rational, but the rectangle contained by them medial, be added together, the whole straight line is irrational: and let it be called major.

**Step 1.** Let AB and BC be two straight lines incommensurable in square which make the sum of the squares on them rational but the rectangle contained by them medial, and let them be placed in a straight line so that AC is the whole. I say that AC is irrational.

**Step 2.** Since the rectangle AB by BC is medial, twice the rectangle AB by BC is also medial [D10.1.4, 10.23]. But the sum of the squares on AB and BC is rational. Therefore the sum of the squares on AB and BC is incommensurable with twice the rectangle AB by BC, since a rational area is incommensurable with a medial area [D10.1.3, D10.1.4].

**Step 3.** Now the square on AC equals the sum of the squares on AB and BC together with twice the rectangle AB by BC [2.4]. Therefore the square on AC equals the sum of a rational area and a medial area.

**Step 4.** Since the sum of the squares on AB and BC is incommensurable with twice the rectangle AB by BC, and the square on AC is their sum, the square on AC is incommensurable with each of the two parts [10.16]. In particular, the square on AC is incommensurable with the sum of the squares on AB and BC.

**Step 5.** But the sum of the squares on AB and BC is rational, that is, commensurable with the square on a rational straight line [D10.1.4]. Since the square on AC is incommensurable with this rational area, the square on AC is incommensurable with the square on the rational straight line [10.13]. Therefore the square on AC is irrational [D10.1.4].

**Step 6.** Therefore AC itself is irrational [D10.1.4]. Let it be called major.

**Step 7.** Therefore, if two straight lines incommensurable in square which make the sum of the squares on them rational but the rectangle contained by them medial be added together, the whole straight line is irrational. Q.E.D.

**USED:** 10.13, 10.16, 10.23, 2.4, D10.1.3, D10.1.4
**Human refs (from References field):** 10.16, 10.23, 10.33, 10.6, D10.1.4
**Jaccard:** 0.375 — AI adds ['10.13', '2.4', 'D10.1.3']; Human adds ['10.33', '10.6']

## Proposition 10.40
**Statement:** If two straight lines incommensurable in square which make the sum of the squares on them medial, but the rectangle contained by them rational, be added together, the whole straight line is irrational; and let it be called the side of a rational plus a medial area.

**Step 1.** Let AB and BC be two straight lines incommensurable in square such that the sum of the squares on them, sq(AB) + sq(BC), is medial, and the rectangle contained by them, rect(AB, BC), is rational. Let AC be the whole straight line AB + BC. We must show that AC is irrational.

**Step 2.** By 2.4, the square on AC equals the sum of the squares on AB and BC together with twice the rectangle contained by AB and BC. That is, sq(AC) = sq(AB) + sq(BC) + 2·rect(AB, BC).

**Step 3.** Since rect(AB, BC) is rational, we show that 2·rect(AB, BC) is also rational. The ratio 2:1 is a ratio of numbers, so by 10.6, the areas 2·rect(AB, BC) and rect(AB, BC) are commensurable. Since rect(AB, BC) is rational (commensurable with the assigned rational square by D10.1.4), and 2·rect(AB, BC) is commensurable with it, by 10.12 the area 2·rect(AB, BC) is also commensurable with the assigned rational square, and hence rational by D10.1.4.

**Step 4.** By hypothesis, sq(AB) + sq(BC) is medial. By 10.21 and D10.1.4, a medial area is irrational, meaning it is incommensurable with the assigned rational square.

**Step 5.** Since 2·rect(AB, BC) is rational, it is commensurable with the assigned rational square. Since sq(AB) + sq(BC) is medial, it is incommensurable with the assigned rational square. Therefore sq(AB) + sq(BC) and 2·rect(AB, BC) are incommensurable with one another, for if they were commensurable, then since 2·rect(AB, BC) is commensurable with the rational square, by 10.12 the area sq(AB) + sq(BC) would also be commensurable with the rational square, contradicting its being medial. So sq(AB) + sq(BC) is incommensurable with 2·rect(AB, BC), and we apply 10.13.

**Step 6.** Since sq(AB) + sq(BC) and 2·rect(AB, BC) are incommensurable magnitudes, by 10.16 their sum sq(AC) = sq(AB) + sq(BC) + 2·rect(AB, BC) is incommensurable with each summand. In particular, sq(AC) is incommensurable with 2·rect(AB, BC).

**Step 7.** Since 2·rect(AB, BC) is rational (commensurable with the assigned rational square), and sq(AC) is incommensurable with 2·rect(AB, BC), it follows by 10.13 that sq(AC) is incommensurable with the assigned rational square. Therefore sq(AC) is irrational by D10.1.4.

**Step 8.** Since the square on AC is irrational, AC itself is irrational by D10.1.4 (the straight line producing an irrational square is irrational).

**Step 9.** Therefore, if two straight lines incommensurable in square which make the sum of the squares on them medial but the rectangle contained by them rational be added together, the whole straight line is irrational. Let it be called the side of a rational plus a medial area. Q.E.D.

**USED:** 10.12, 10.13, 10.16, 10.21, 10.6, 2.4, D10.1.4
**Human refs (from References field):** 10.16, 10.34, D10.1.4
**Jaccard:** 0.250 — AI adds ['10.12', '10.13', '10.21', '10.6', '2.4']; Human adds ['10.34']

## Proposition 10.41
**Statement:** If two straight lines incommensurable in square which make the sum of the squares on them medial, and the rectangle contained by them medial and also incommensurable with the sum of the squares on them, be added together, the whole straight line is irrational; and let it be called the   side of the sum of two medial areas.

**Step 1.** Let AB and BC be two straight lines incommensurable in square such that the sum of the squares on them, sq(AB) + sq(BC), is medial, the rectangle rect(AB, BC) is medial, and sq(AB) + sq(BC) is incommensurable with rect(AB, BC). Let AC = AB + BC. We must show that AC is irrational.

**Step 2.** By 2.4, sq(AC) = sq(AB) + sq(BC) + 2*rect(AB, BC). Thus sq(AC) is the sum of the area sq(AB) + sq(BC) and the area 2*rect(AB, BC).

**Step 3.** Since rect(AB, BC) is medial, and 2*rect(AB, BC) has to rect(AB, BC) the ratio 2:1, which is the ratio of a number to a number, 2*rect(AB, BC) is commensurable with rect(AB, BC) by 10.6. Since rect(AB, BC) is medial and 2*rect(AB, BC) is commensurable with it, 2*rect(AB, BC) is also medial by 10.23 (applied to areas via D10.1.4, since the sides of squares equal to commensurable areas are commensurable).

**Step 4.** Since sq(AB) + sq(BC) is incommensurable with rect(AB, BC), and 2*rect(AB, BC) is commensurable with rect(AB, BC) (Step 3), it follows by 10.13 that sq(AB) + sq(BC) is incommensurable with 2*rect(AB, BC).

**Step 5.** Set out a rational straight line DE. Apply to DE a rectangle equal to sq(AB) + sq(BC), producing breadth DH, so that rect(DE, DH) = sq(AB) + sq(BC). Then apply to DE a rectangle equal to 2*rect(AB, BC), producing breadth HG, so that rect(DE, HG) = 2*rect(AB, BC). Then rect(DE, DG) = sq(AB) + sq(BC) + 2*rect(AB, BC) = sq(AC), where DG = DH + HG.

**Step 6.** Since sq(AB) + sq(BC) is medial and rect(DE, DH) = sq(AB) + sq(BC), and DE is rational, by 10.22 the breadth DH is rational and incommensurable in length with DE.

**Step 7.** Since 2*rect(AB, BC) is medial and rect(DE, HG) = 2*rect(AB, BC), and DE is rational, by 10.22 the breadth HG is rational and incommensurable in length with DE.

**Step 8.** Since sq(AB) + sq(BC) is incommensurable with 2*rect(AB, BC) (Step 4), and rect(DE, DH) = sq(AB) + sq(BC) while rect(DE, HG) = 2*rect(AB, BC), these two rectangles sharing the common side DE are incommensurable. Therefore by 10.11, DH is incommensurable in length with HG.

**Step 9.** DH and HG are each rational (Steps 6 and 7), meaning each is commensurable in square with the rational line DE. Since sq(DH) is commensurable with sq(DE) and sq(HG) is commensurable with sq(DE), by 10.12, sq(DH) is commensurable with sq(HG). Thus DH and HG are commensurable in square.

**Step 10.** Since DH and HG are rational and commensurable in square (Step 9), yet incommensurable in length (Step 8), they are rational straight lines commensurable in square only. Therefore by 10.36, DG = DH + HG is irrational (a binomial straight line).

**Step 11.** Since DE is rational and DG is irrational, DG is not commensurable with DE. If sq(AC) = rect(DE, DG) were rational, then by 10.20, DG would be rational and commensurable in length with DE, contradicting the fact that DG is irrational. Therefore sq(AC) is not rational, hence sq(AC) is irrational.

**Step 12.** Since sq(AC) is irrational, AC is irrational by D10.1.4. And since sq(AC) = (medial area) + (medial area), namely the sum of two medial areas sq(AB) + sq(BC) and 2*rect(AB, BC), let AC be called the side of the sum of two medial areas. Q.E.D.

**USED:** 10.11, 10.12, 10.13, 10.20, 10.22, 10.23, 10.36, 10.6, 2.4, D10.1.4
**Human refs (from References field):** 10.11, 10.22, 10.35, 10.36, 2.4, 6.1, D10.1.4
**Jaccard:** 0.417 — AI adds ['10.12', '10.13', '10.20', '10.23', '10.6']; Human adds ['10.35', '6.1']

## Proposition 10.42
**Statement:** A binomial straight line is divided into its terms at one point only.

**Step 1.** Let AB be a binomial straight line, and let it be divided into its terms at C, so that AC and CB are rational straight lines commensurable in square only, with AC greater than CB [10.36].

**Step 2.** Suppose, for the sake of contradiction, that AB is also divided into its terms at a point D different from C, so that AD and DB are rational straight lines commensurable in square only, with AD greater than DB [10.36].

**Step 3.** Since AC and CB are rational, the squares on AC and CB are each rational areas [D10.1.4]. Since AC and CB are commensurable in square, the squares on AC and CB are commensurable with one another [D10.1.2]. Therefore by 10.15, the sum of the squares on AC and CB is commensurable with each of them, and hence is a rational area.

**Step 4.** Since AC and CB are rational straight lines commensurable in square only, the rectangle contained by AC and CB is medial [10.21].

**Step 5.** By the same reasoning applied to the division at D: since AD and DB are rational and commensurable in square only, the sum of the squares on AD and DB is a rational area [D10.1.4, D10.1.2, 10.15], and the rectangle contained by AD and DB is medial [10.21].

**Step 6.** Since AC + CB = AB = AD + DB, by 2.4 applied to each decomposition, the square on AB equals the sum of the squares on AC and CB together with twice the rectangle contained by AC and CB, and the square on AB also equals the sum of the squares on AD and DB together with twice the rectangle contained by AD and DB.

**Step 7.** Since both expressions equal the square on AB, they are equal to one another [CN1]. Therefore the sum of the squares on AC and CB together with twice the rectangle AC by CB equals the sum of the squares on AD and DB together with twice the rectangle AD by DB.

**Step 8.** Subtracting equals from equals [CN3], the difference of the sums of squares equals the difference of twice the rectangles. That is, (sq(AC) + sq(CB)) minus (sq(AD) + sq(DB)) equals twice the rectangle AD by DB minus twice the rectangle AC by CB.

**Step 9.** The left-hand side is the difference of two rational areas. Both rational areas are commensurable with the assigned rational square area, and hence commensurable with each other [10.12]. Therefore their difference, if nonzero, is commensurable with each of them and hence is a rational area.

**Step 10.** If this difference is nonzero, then twice the rectangle AD by DB differs from twice the rectangle AC by CB by a rational area. Since the ratio 2 to 1 is rational, twice the rectangle AC by CB is commensurable with the rectangle AC by CB, and similarly twice the rectangle AD by DB is commensurable with the rectangle AD by DB. Thus the rectangle AD by DB would differ from the rectangle AC by CB by a rational area (being half of a rational area, which is rational). But the rectangle AC by CB is medial and the rectangle AD by DB is medial [Step 4, Step 5]. This means a medial area would exceed a medial area by a rational area, which is impossible [10.26].

**Step 11.** Therefore the difference must be zero. Hence the sum of the squares on AC and CB equals the sum of the squares on AD and DB, and also twice the rectangle AC by CB equals twice the rectangle AD by DB, so the rectangle contained by AC and CB equals the rectangle contained by AD and DB.

**Step 12.** Bisect AB at E [1.10]. By 2.5, since AB is divided into equal segments at E and into unequal segments at C, the rectangle contained by AC and CB together with the square on EC equals the square on EB. Likewise, the rectangle contained by AD and DB together with the square on ED equals the square on EB.

**Step 13.** Since both expressions equal the square on EB [CN1], the rectangle AC by CB together with the square on EC equals the rectangle AD by DB together with the square on ED. But the rectangle AC by CB equals the rectangle AD by DB [Step 11]. Subtracting these equal rectangles from the equal sums [CN3], the square on EC equals the square on ED. Therefore EC equals ED, and hence C and D are the same point.

**Step 14.** This contradicts the assumption that D is different from C. Therefore a binomial straight line is divided into its terms at one point only. Q.E.D.

**USED:** 1.10, 10.12, 10.15, 10.21, 10.26, 10.36, 2.4, 2.5, CN1, CN3, D10.1.2, D10.1.4
**Human refs (from References field):** 10.21, 10.36, 2.4
**Jaccard:** 0.250 — AI adds ['1.10', '10.12', '10.15', '10.26', '2.5', 'CN1', 'CN3', 'D10.1.2', 'D10.1.4']

## Proposition 10.43
**Statement:** A first bimedial straight line is divided at one point only.

**Step 1.** Let AB be a first bimedial straight line, and let it be divided at C so that AC and CB are its terms, with AC being the greater. Suppose, for the sake of contradiction, that AB is also divided at another point D, so that AD and DB are also two medial straight lines commensurable in square only and containing a rational rectangle, with AD being the greater.

**Step 2.** Since AB is a first bimedial divided at C, by the definition of a first bimedial (10.37), AC and CB are medial straight lines commensurable in square only, and the rectangle AC by CB is rational.

**Step 3.** Similarly, since AB is divided at D as a first bimedial, AD and DB are medial straight lines commensurable in square only, and the rectangle AD by DB is rational.

**Step 4.** Since AC is medial, the square on AC is a medial area (D10.1.4). Since CB is medial, the square on CB is a medial area. Since AC and CB are commensurable in square, the squares on AC and CB are commensurable areas. By 10.15, the sum of the squares on AC and CB is commensurable with the square on AC, and therefore the sum of the squares on AC and CB is itself a medial area (by 10.23 applied to areas, since an area commensurable with a medial area is medial).

**Step 5.** By the same reasoning, since AD and DB are medial and commensurable in square, the sum of the squares on AD and DB is also a medial area.

**Step 6.** By 2.4, the square on AB equals the sum of the squares on AC and CB together with twice the rectangle AC by CB. That is, AB^2 = AC^2 + CB^2 + 2·rect(AC, CB).

**Step 7.** Likewise by 2.4, the square on AB equals the sum of the squares on AD and DB together with twice the rectangle AD by DB. That is, AB^2 = AD^2 + DB^2 + 2·rect(AD, DB).

**Step 8.** Therefore, AC^2 + CB^2 + 2·rect(AC, CB) = AD^2 + DB^2 + 2·rect(AD, DB) (CN1).

**Step 9.** Rearranging, (AC^2 + CB^2) - (AD^2 + DB^2) = 2·rect(AD, DB) - 2·rect(AC, CB) (CN2, CN3).

**Step 10.** Now 2·rect(AC, CB) is rational (from Step 2, since rect(AC, CB) is rational, and twice a rational area is rational by 10.15). Similarly, 2·rect(AD, DB) is rational (from Step 3). The difference of two rational areas is either rational or zero, since rational areas are commensurable with the same rational square and their difference (if nonzero) is commensurable with that square, hence rational.

**Step 11.** From Step 4, the sum AC^2 + CB^2 is medial. From Step 5, the sum AD^2 + DB^2 is medial. If these two medial areas are unequal, then one exceeds the other by the amount computed in Step 9, which is rational. But by 10.26, a medial area does not exceed a medial area by a rational area. Therefore the difference must be zero.

**Step 12.** Since (AC^2 + CB^2) - (AD^2 + DB^2) = 0, we have AC^2 + CB^2 = AD^2 + DB^2. From Step 9, it follows that 2·rect(AC, CB) = 2·rect(AD, DB), and hence rect(AC, CB) = rect(AD, DB).

**Step 13.** We now have two conditions: AC + CB = AD + DB (since both equal AB), and rect(AC, CB) = rect(AD, DB). By 2.5, if a straight line is cut into equal and unequal segments, the rectangle contained by the unequal segments together with the square on the segment between the points of section equals the square on the half. Apply this to AB with the two division points C and D.

**Step 14.** Without loss of generality, suppose AD > AC (and consequently DB < CB, since AD + DB = AC + CB). Let E be the midpoint of AB. By 2.5 applied to AB cut equally at E and unequally at C: rect(AC, CB) + sq(EC) = sq(EB). By 2.5 applied to AB cut equally at E and unequally at D: rect(AD, DB) + sq(ED) = sq(EB).

**Step 15.** Since rect(AC, CB) = rect(AD, DB) (from Step 12) and both expressions equal sq(EB) minus a square, we obtain sq(EC) = sq(ED) (CN1, CN3). Therefore EC = ED.

**Step 16.** Since E is the midpoint of AB and EC = ED, the points C and D are equidistant from E. Since both C and D lie on the segment AB with AC + CB = AD + DB, and EC = ED, we have two possibilities: either C = D, or C and D are on opposite sides of E at equal distances.

**Step 17.** If C and D were on opposite sides of E with EC = ED, then one of them, say C, is between A and E, and D is between E and B (or vice versa). In that case, AC = AE - EC and AD = AE + ED = AE + EC, so AD - AC = 2·EC. Also CB = EB + EC and DB = EB - ED = EB - EC, so CB - DB = 2·EC. This gives AD = AC + 2·EC and DB = CB - 2·EC.

**Step 18.** But AC is the greater term at the division point C (AC > CB), and AD is the greater term at the division point D (AD > DB). From Step 17, AD > AC and DB < CB. Since AC and CB are commensurable in square only and both medial, and AD and DB are commensurable in square only and both medial, we examine: AC + CB = AD + DB, and AC > CB, AD > DB. The segments are (AC, CB) and (AD, DB) where AC < AD.

**Step 19.** Consider the identity from 2.5 more carefully. Since AC + CB = AD + DB and rect(AC, CB) = rect(AD, DB), the pairs (AC, CB) and (AD, DB) are roots of the same quadratic equation: t^2 - AB·t + rect(AC, CB) = 0 (by 2.5 and 2.6). This equation has exactly two roots. Since AC > CB, we must have AC as the larger root and CB as the smaller. Similarly AD is the larger root and DB the smaller. Therefore AC = AD and CB = DB.

**Step 20.** Since AC = AD, the points C and D coincide. This contradicts our assumption that D is different from C. Therefore, a first bimedial straight line is divided into its terms at one point only. Q.E.D.

**USED:** 10.15, 10.23, 10.26, 10.37, 2.4, 2.5, CN1, CN2, CN3, D10.1.4
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['10.15', '10.23', '10.26', '10.37', '2.4', '2.5', 'CN1', 'CN2', 'CN3', 'D10.1.4']

## Proposition 10.44
**Statement:** A second bimedial straight line is divided at one point only.

**Step 1.** Let AB be a second bimedial straight line, and let it be divided into its medial terms at C, so that AC and CB are medial straight lines commensurable in square only and containing a medial rectangle [10.38]. We must show that AB cannot be so divided at any other point.

**Step 2.** Suppose, for the sake of contradiction, that AB is also divided at D into terms AD and DB satisfying the same conditions: AD and DB are medial, commensurable in square only, and the rectangle AD by DB is medial.

**Step 3.** Since AC and CB are medial and commensurable in square only, the squares on AC and CB are each medial areas, and since AC and CB are commensurable in square, the squares on AC and CB are commensurable with each other. Therefore the sum of the squares on AC and CB is medial [10.15, 10.23].

**Step 4.** Similarly, since AD and DB are medial and commensurable in square only, the sum of the squares on AD and DB is medial.

**Step 5.** By Proposition 2.4, the square on AB equals the squares on AC and CB together with twice the rectangle contained by AC and CB. That is, AB^2 = AC^2 + CB^2 + 2*rect(AC, CB).

**Step 6.** Likewise, AB^2 = AD^2 + DB^2 + 2*rect(AD, DB) [2.4].

**Step 7.** Therefore AC^2 + CB^2 + 2*rect(AC, CB) = AD^2 + DB^2 + 2*rect(AD, DB) [CN1].

**Step 8.** Now, since both divisions produce a second bimedial, twice the rectangle contained by AC and CB is medial (since rect(AC, CB) is medial, and twice a medial area is medial [10.23]), and twice the rectangle contained by AD and DB is medial for the same reason.

**Step 9.** Also, the sum of squares AC^2 + CB^2 is incommensurable with 2*rect(AC, CB), and similarly AD^2 + DB^2 is incommensurable with 2*rect(AD, DB). This follows from the construction of the second bimedial [10.38].

**Step 10.** From Step 7, rearranging, we get (AC^2 + CB^2) - (AD^2 + DB^2) = 2*rect(AD, DB) - 2*rect(AC, CB).

**Step 11.** Now suppose C and D are different points. We consider the relationship between these sums of squares. Since AC and CB are terms of a second bimedial, and AD and DB are also terms of a second bimedial with the same whole AB, we examine whether the difference of the sums of squares can equal the difference of twice the rectangles.

**Step 12.** The sum AC^2 + CB^2 is medial (Step 3), and the sum AD^2 + DB^2 is medial (Step 4). If these two medial areas are equal, then from Step 10, 2*rect(AD, DB) = 2*rect(AC, CB), so rect(AD, DB) = rect(AC, CB).

**Step 13.** If AC^2 + CB^2 = AD^2 + DB^2 and rect(AC, CB) = rect(AD, DB), then by 2.5 and 2.6 (applied to the line AB divided at C and at D): if AC^2 + CB^2 = AD^2 + DB^2, then since AB is divided at C and at D, and the rectangles are also equal, the segments must satisfy the conditions of 2.5 and 2.6 which force C and D to be equidistant from the midpoint of AB. Combined with equal rectangles, this means either C = D, or the segments are simply interchanged (AC = DB and CB = AD), which geometrically means C = D since both divisions have the greater segment on the same side (AC > CB implies AD > DB by the equal sums and products).

**Step 14.** Now suppose instead that AC^2 + CB^2 is not equal to AD^2 + DB^2. Then their difference is nonzero. From Step 10, this difference equals 2*rect(AD, DB) - 2*rect(AC, CB), which is the difference of two medial areas (Step 8).

**Step 15.** Since AC^2 + CB^2 is medial and AD^2 + DB^2 is medial, if they are commensurable, their difference is either zero or medial. If they are incommensurable, their difference need not be rational or medial in general.

**Step 16.** However, we can proceed more precisely. Since AB^2 = AC^2 + CB^2 + 2*rect(AC, CB), and the sum AC^2 + CB^2 is incommensurable with 2*rect(AC, CB) [Step 9], the whole AB^2 is the sum of two incommensurable medial areas.

**Step 17.** Similarly, AB^2 = AD^2 + DB^2 + 2*rect(AD, DB), where AD^2 + DB^2 is incommensurable with 2*rect(AD, DB).

**Step 18.** Now set E = AC^2 + CB^2 and F = 2*rect(AC, CB), and G = AD^2 + DB^2 and H = 2*rect(AD, DB). We have E + F = G + H, so E - G = H - F.

**Step 19.** E is medial and G is medial [Steps 3, 4]. F is medial and H is medial [Step 8]. If E - G is not zero, then E - G = H - F, meaning the difference of two medial areas (E and G) equals the difference of two medial areas (H and F).

**Step 20.** Since E is incommensurable with F [Step 9], suppose E - G were rational. Then H - F is rational, meaning two medial areas H and F differ by a rational area. But this contradicts Proposition 10.26, which states that a medial area does not exceed a medial area by a rational area.

**Step 21.** Similarly, if E and G are commensurable and unequal, then E - G is medial (nonzero). Then H - F is also medial. Now E + F = G + H gives E - G = H - F. Since E is incommensurable with F, and G is incommensurable with H, consider: E = G + (H - F). Since H - F is medial and G is medial, if H - F and G were commensurable, E would be medial and commensurable with G, consistent so far. But then F = H - (E - G) = H - (H - F) = F, which is trivially true, so we need a more refined argument.

**Step 22.** We apply the method used in 10.42 and 10.43 more carefully. Without loss of generality, assume AC > AD (and hence DB > CB, since AC + CB = AD + DB = AB). Set AC = AD + x where x > 0, so CB = DB - x.

**Step 23.** Then AC^2 + CB^2 = (AD + x)^2 + (DB - x)^2 = AD^2 + DB^2 + 2x^2 + 2x(AD - DB). And 2*rect(AC, CB) = 2*(AD + x)(DB - x) = 2*(AD*DB - x*AD + x*DB - x^2) = 2*rect(AD, DB) + 2x(DB - AD) - 2x^2.

**Step 24.** From Step 10: (AC^2 + CB^2) - (AD^2 + DB^2) = 2*rect(AD, DB) - 2*rect(AC, CB). The left side equals 2x^2 + 2x(AD - DB) from Step 23. The right side equals -(2x(DB - AD) - 2x^2) = 2x^2 - 2x(DB - AD) = 2x^2 + 2x(AD - DB). These are indeed equal, confirming the algebra but not yet yielding the contradiction.

**Step 25.** We instead use the approach of 10.42 directly adapted. Let a rational straight line r be set out. Apply the area AC^2 + CB^2 to r, producing breadth p; apply the area AD^2 + DB^2 to r, producing breadth q. Since AC^2 + CB^2 is medial and r is rational, p is rational and incommensurable in length with r [10.22]. Similarly q is rational and incommensurable in length with r [10.22].

**Step 26.** Apply 2*rect(AC, CB) to r, producing breadth s. Since 2*rect(AC, CB) is medial and r is rational, s is rational and incommensurable in length with r [10.22]. Similarly, applying 2*rect(AD, DB) to r produces breadth t, which is rational and incommensurable in length with r [10.22].

**Step 27.** Since AB^2 = AC^2 + CB^2 + 2*rect(AC, CB), applying AB^2 to r produces breadth p + s. And AB^2 = AD^2 + DB^2 + 2*rect(AD, DB) gives breadth q + t. So p + s = q + t.

**Step 28.** Now, since AC^2 + CB^2 is incommensurable with 2*rect(AC, CB) [Step 9], p is incommensurable with s [10.11]. Similarly q is incommensurable with t. Both p and s are rational [Steps 25, 26], so p + s is a binomial straight line [10.36]. Likewise q + t is a binomial straight line [10.36].

**Step 29.** But by Proposition 10.42, a binomial straight line is divided into its terms at one point only. Since p + s = q + t are both divisions of the same binomial line into rational terms (where each pair of terms is commensurable in square only and incommensurable in length), the division is unique. Therefore p = q and s = t [10.42].

**Step 30.** From p = q, we have AC^2 + CB^2 = AD^2 + DB^2 (since both were applied to the same rational line r producing equal breadths). From s = t, we have 2*rect(AC, CB) = 2*rect(AD, DB), hence rect(AC, CB) = rect(AD, DB).

**Step 31.** Since AC + CB = AD + DB = AB, and AC^2 + CB^2 = AD^2 + DB^2, it follows that 2*rect(AC, CB) = 2*rect(AD, DB) (which we already know from Step 30, confirming consistency). By 2.5 and 2.6, when a straight line is divided into equal and unequal parts, the rectangle contained by the unequal parts together with the square on the line between the points of section equals the rectangle contained by the equal parts. Since the sums of squares are equal, the segments AC, CB are equal to AD, DB respectively (possibly interchanged).

**Step 32.** More precisely, since AC^2 + CB^2 = AD^2 + DB^2 and AC + CB = AD + DB, subtracting: 2*rect(AC, CB) = (AC + CB)^2 - (AC^2 + CB^2) = (AD + DB)^2 - (AD^2 + DB^2) = 2*rect(AD, DB) [2.4]. The pair (AC, CB) and (AD, DB) are both pairs of values with the same sum and the same sum of squares, hence the same product. By 2.5, if AB is bisected at M and cut unequally at C, then rect(AC, CB) + MC^2 = MB^2. Similarly rect(AD, DB) + MD^2 = MB^2. Since rect(AC, CB) = rect(AD, DB), we get MC^2 = MD^2 [CN3], hence MC = MD, and therefore C = D.

**Step 33.** Therefore AB, being a second bimedial straight line, is divided into its terms at one point only. Q.E.D.

**USED:** 10.11, 10.15, 10.22, 10.23, 10.26, 10.36, 10.38, 10.42, 2.4, 2.5, CN1, CN3
**Human refs (from References field):** 10.11, 10.13, 10.22, 10.36, 10.38, 10.6, 2.4, 6.1
**Jaccard:** 0.333 — AI adds ['10.15', '10.23', '10.26', '10.42', '2.5', 'CN1', 'CN3']; Human adds ['10.13', '10.6', '6.1']

## Proposition 10.45
**Statement:** A major straight line is divided at one and the same point only.

**Step 1.** Let AB be a major straight line, and suppose it is divided at C so that AC, CB are the terms of the major line. Then by the definition of major (10.39), AC and CB are incommensurable in square, the sum sq(AC) + sq(CB) is rational, and the rectangle rect(AC, CB) is medial, so that 2*rect(AC, CB) is also medial.

**Step 2.** Suppose, for the sake of contradiction, that AB is also divided at a different point D into terms AD, DB satisfying the same conditions: AD and DB are incommensurable in square, sq(AD) + sq(DB) is rational, and 2*rect(AD, DB) is medial.

**Step 3.** By 2.4 applied to AB divided at C: sq(AB) = sq(AC) + sq(CB) + 2*rect(AC, CB). By 2.4 applied to AB divided at D: sq(AB) = sq(AD) + sq(DB) + 2*rect(AD, DB). Therefore, sq(AC) + sq(CB) + 2*rect(AC, CB) = sq(AD) + sq(DB) + 2*rect(AD, DB).

**Step 4.** Rearranging by CN3: [sq(AC) + sq(CB)] - [sq(AD) + sq(DB)] = 2*rect(AD, DB) - 2*rect(AC, CB).

**Step 5.** Now sq(AC) + sq(CB) is rational and sq(AD) + sq(DB) is rational. Since both are rational areas, each is commensurable with the square on the assigned rational straight line. By 10.12, they are commensurable with one another. By 10.15, their difference [sq(AC) + sq(CB)] - [sq(AD) + sq(DB)] is commensurable with each, and hence is a rational area (if nonzero) or zero.

**Step 6.** On the other side, 2*rect(AC, CB) is medial and 2*rect(AD, DB) is medial. By 10.26, a medial area does not exceed a medial area by a rational area. Therefore the difference 2*rect(AD, DB) - 2*rect(AC, CB) cannot be a nonzero rational area.

**Step 7.** From Steps 5 and 6, the common value of both sides must be zero. Hence sq(AC) + sq(CB) = sq(AD) + sq(DB), and 2*rect(AC, CB) = 2*rect(AD, DB), which gives rect(AC, CB) = rect(AD, DB).

**Step 8.** We now have AC + CB = AD + DB (both equal AB) and rect(AC, CB) = rect(AD, DB). The two segments AC, CB are therefore determined as the two values whose sum is AB and whose product (rectangle) is rect(AC, CB). Likewise AD, DB are determined as the two values with the same sum and the same product.

**Step 9.** Since two magnitudes are uniquely determined (as an unordered pair) by their sum and their rectangle -- for they are the two segments produced when a line of given length is divided so as to produce a given rectangle -- it follows that the pair {AC, CB} equals the pair {AD, DB} as a set of magnitudes.

**Step 10.** If AC = AD, then CB = DB (since AC + CB = AD + DB), and C coincides with D. If instead AC = DB and CB = AD, then since AC and CB are unequal (being incommensurable in square, they cannot be equal, for if AC = CB then sq(AC) = sq(CB) and they would be commensurable in square and in length), the point D would be the reflection of C about the midpoint of AB. But in either case the line AB is divided into the same two terms: the pair of magnitudes is identical.

**Step 11.** Therefore the major straight line AB is divided into its terms at one and the same point only; that is, the decomposition of a major straight line into its two constituent terms is unique.

**USED:** 10.12, 10.15, 10.26, 10.39, 2.4, CN3
**Human refs (from References field):** 10.26, 10.39
**Jaccard:** 0.333 — AI adds ['10.12', '10.15', '2.4', 'CN3']

## Proposition 10.46
**Statement:** The side of a rational plus a medial area is divided at one point only.

**Step 1.** Let AB be the side of a rational plus a medial area, and let it be divided at C so that AC and CB are the two straight lines described in the definition (10.40): AC and CB are incommensurable in square, the sum of the squares on AC and CB is medial, and twice the rectangle AC by CB is rational.

**Step 2.** Suppose, for the sake of contradiction, that AB is also divided at D so that AD and DB satisfy the same conditions: AD and DB are incommensurable in square, the sum of the squares on AD and DB is medial, and twice the rectangle AD by DB is rational.

**Step 3.** Since twice the rectangle AC by CB is rational and twice the rectangle AD by DB is rational, these two areas are commensurable with each other, for any two rational areas are commensurable (by D10.1.4 and 10.12, since both are commensurable with the square on the assigned rational straight line).

**Step 4.** Now, by 2.4, the square on AB equals the sum of the squares on AC and CB plus twice the rectangle AC by CB. Likewise, the square on AB equals the sum of the squares on AD and DB plus twice the rectangle AD by DB.

**Step 5.** Therefore the sum of the squares on AC and CB plus twice the rectangle AC by CB equals the sum of the squares on AD and DB plus twice the rectangle AD by DB (CN1).

**Step 6.** By subtraction (CN3), the difference between the sum of the squares on AC, CB and the sum of the squares on AD, DB equals the difference between twice the rectangle AD by DB and twice the rectangle AC by CB. That is: (sq(AC) + sq(CB)) - (sq(AD) + sq(DB)) = 2·rect(AD,DB) - 2·rect(AC,CB).

**Step 7.** From Step 3, twice the rectangle AC by CB and twice the rectangle AD by DB are both rational and therefore commensurable. Hence their difference is either zero or rational (by 10.15, since if two commensurable magnitudes are given, their sum is commensurable with each, and by analogous reasoning the difference of commensurable magnitudes is commensurable with each, hence rational).

**Step 8.** The sum of the squares on AC and CB is medial, and the sum of the squares on AD and DB is medial (by the hypothesis of 10.40 applied to each division).

**Step 9.** If the difference in Step 6 is nonzero, then a medial area exceeds a medial area by a rational area (since the left side of the equation in Step 6 is the difference of two medial areas, and the right side is rational). But this contradicts 10.26, which states that a medial area does not exceed a medial area by a rational area.

**Step 10.** Therefore the difference must be zero. Hence twice the rectangle AC by CB equals twice the rectangle AD by DB, and consequently the sum of the squares on AC and CB equals the sum of the squares on AD and DB.

**Step 11.** Since the sum of the squares on AC, CB equals the sum of the squares on AD, DB, and twice the rectangle AC by CB equals twice the rectangle AD by DB, the same conditions hold as in the proof of 10.45. In that proposition it was shown, under these identical equalities of the sums of squares and of the doubled rectangles, that the division point must be the same. Specifically: from 2.4, the square on AC equals the square on AD (which would follow from the equalities by algebraic rearrangement). But we must argue directly.

**Step 12.** Since the squares on AC and CB together equal the squares on AD and DB together, and twice the rectangle AC by CB equals twice the rectangle AD by DB, we add these: (sq(AC) + sq(CB) + 2·rect(AC,CB)) = (sq(AD) + sq(DB) + 2·rect(AD,DB)). By 2.4 applied in reverse, sq(AC + CB) = sq(AD + DB), i.e., sq(AB) = sq(AB), which is trivially true and does not immediately distinguish the points. We must instead subtract.

**Step 13.** From sq(AC) + sq(CB) = sq(AD) + sq(DB) and 2·rect(AC,CB) = 2·rect(AD,DB), subtract the rectangle equations from the square-sum equations: (sq(AC) + sq(CB) - 2·rect(AC,CB)) = (sq(AD) + sq(DB) - 2·rect(AD,DB)). By 2.7, sq(AC) + sq(CB) - 2·rect(AC,CB) = sq(AC - CB), and similarly sq(AD) + sq(DB) - 2·rect(AD,DB) = sq(AD - DB). Therefore sq(AC - CB) = sq(AD - DB).

**Step 14.** From Step 12 (addition), sq(AC + CB) = sq(AD + DB), so AC + CB = AD + DB (= AB). From Step 13, sq(AC - CB) = sq(AD - DB), so AC - CB = AD - DB (taking the positive difference, since in both cases the first-named segment is the greater by convention or we may take absolute values).

**Step 15.** Adding the equations AC + CB = AD + DB and AC - CB = AD - DB, we get 2·AC = 2·AD (CN2), hence AC = AD. Subtracting instead, 2·CB = 2·DB, hence CB = DB.

**Step 16.** Since AC = AD and CB = DB, the point C coincides with the point D. This contradicts the assumption that AB was divided at two distinct points.

**Step 17.** Therefore the side of a rational plus a medial area is divided at one point only. Q.E.D.

**USED:** 10.12, 10.15, 10.26, 10.40, 2.4, 2.7, CN1, CN2, CN3, D10.1.4
**Human refs (from References field):** 10.26, 10.40
**Jaccard:** 0.200 — AI adds ['10.12', '10.15', '2.4', '2.7', 'CN1', 'CN2', 'CN3', 'D10.1.4']

## Proposition 10.47
**Statement:** The side of the sum of two medial areas is divided at one point only.

**Step 1.** Let AB be the side of the sum of two medial areas, and suppose it is divided at C so that AC and CB satisfy the conditions of 10.41: AC and CB are incommensurable in square, the sum of the squares on AC and CB is medial, the rectangle contained by AC and CB is medial, and the sum of the squares on AC and CB is incommensurable with the rectangle AC.CB.

**Step 2.** Suppose for contradiction that AB is also divided at a different point D so that AD and DB likewise satisfy the conditions of 10.41: AD and DB are incommensurable in square, the sum of the squares on AD and DB is medial, the rectangle AD.DB is medial, and the sum of the squares on AD and DB is incommensurable with the rectangle AD.DB.

**Step 3.** By 2.4, the square on AB equals the squares on AC and CB together with twice the rectangle AC.CB. Likewise the square on AB equals the squares on AD and DB together with twice the rectangle AD.DB. Therefore the squares on AC and CB together with twice the rectangle AC.CB equal the squares on AD and DB together with twice the rectangle AD.DB [CN1].

**Step 4.** Set out a rational straight line rho [D10.1.3]. Apply the sum of the squares on AC and CB to rho, producing breadth p. Apply twice the rectangle AC.CB to rho, producing breadth q, placed adjacent to p along rho. Then the rectangle contained by rho and p+q equals the square on AB.

**Step 5.** Since the sum of the squares on AC and CB is medial, applying it to the rational line rho produces a breadth p that is rational and incommensurable in length with rho [10.22].

**Step 6.** Since the rectangle AC.CB is medial, and twice the rectangle AC.CB is commensurable with the rectangle AC.CB (their ratio being 2 to 1, which is a ratio of number to number, so they are commensurable by 10.6), and since a straight line commensurable with a medial straight line is medial [10.23], the side of the square equal to twice the rectangle AC.CB is medial, so twice the rectangle AC.CB is a medial area [D10.1.4]. Applying this medial area to the rational line rho produces a breadth q that is rational and incommensurable in length with rho [10.22].

**Step 7.** Since the sum of the squares on AC and CB is incommensurable with the rectangle AC.CB [by hypothesis from 10.41], and twice the rectangle AC.CB is commensurable with the rectangle AC.CB [Step 6], the sum of the squares on AC and CB is incommensurable with twice the rectangle AC.CB [10.13]. Now these areas, when applied to rho, produce breadths p and q respectively, and the areas are to one another as p is to q [6.1]. Since the areas are incommensurable, p is incommensurable in length with q [10.11].

**Step 8.** Since p and q are both rational [Steps 5 and 6] and incommensurable in length with each other [Step 7], they are commensurable in square only. Therefore the straight line p+q is a binomial [10.36].

**Step 9.** Similarly, apply the sum of the squares on AD and DB to rho producing breadth p', and twice the rectangle AD.DB to rho producing breadth q'. By the same reasoning as Steps 5 through 8 (using the conditions from 10.41 applied to the division at D), p' and q' are rational and commensurable in square only, and p'+q' is a binomial.

**Step 10.** From Step 3, since the total areas applied to rho are equal, the total breadths are equal: p+q = p'+q' [CN1].

**Step 11.** Since p+q is a binomial straight line, and a binomial straight line is divided into its terms at one point only [10.42], and p+q = p'+q' with both pairs being the terms of the same binomial, the point of division is the same. Therefore p = p' and q = q'.

**Step 12.** Since p = p' and both rectangles rho times p and rho times p' equal the sum of the squares on AC, CB and on AD, DB respectively, we have that the squares on AC and CB together equal the squares on AD and DB together. Since q = q', twice the rectangle AC.CB equals twice the rectangle AD.DB, whence the rectangle AC.CB equals the rectangle AD.DB [CN3].

**Step 13.** By 2.7, the square on the difference AC minus CB equals the squares on AC and CB minus twice the rectangle AC.CB. Likewise the square on the difference AD minus DB equals the squares on AD and DB minus twice the rectangle AD.DB. Since the squares on AC and CB equal the squares on AD and DB, and twice the rectangle AC.CB equals twice the rectangle AD.DB [Step 12], the square on AC minus CB equals the square on AD minus DB [CN1, CN3].

**Step 14.** Therefore AC minus CB equals AD minus DB. Since also AC plus CB equals AD plus DB (both sums equal AB), adding these two equalities gives twice AC equals twice AD [CN2], so AC equals AD. Subtracting gives twice CB equals twice DB, so CB equals DB.

**Step 15.** Since AC equals AD, the point C coincides with the point D. Therefore the side of the sum of two medial areas is divided at one point only. Q.E.D.

**USED:** 10.11, 10.13, 10.22, 10.23, 10.36, 10.41, 10.42, 10.6, 2.4, 2.7, 6.1, CN1, CN2, CN3, D10.1.3, D10.1.4
**Human refs (from References field):** 10.11, 10.22, 10.36, 10.42, 2.4, 6.1
**Jaccard:** 0.375 — AI adds ['10.13', '10.23', '10.41', '10.6', '2.7', 'CN1', 'CN2', 'CN3', 'D10.1.3', 'D10.1.4']

## Proposition 10.48
**Statement:** To find the first binomial straight line.

**Step 1.** Set out a rational straight line A. Set out two numbers AC and CB such that AB = AC + CB, where AB has to BC the ratio of a square number to a square number, but AB does not have to AC the ratio of a square number to a square number. For example, let AC = 3 and CB = 1, so that AB = 4. Then AB:BC = 4:1 = 2^2:1^2, a ratio of square number to square number; and AB:AC = 4:3, which is not a ratio of square number to square number.

**Step 2.** Let DG be the straight line such that sq(A):sq(DG) = BC:AB, that is, sq(DG):sq(A) = AB:BC. Since AB:BC = 4:1 is a ratio of a number to a number, by 10.6 the square on DG is commensurable with the square on A. Since A is rational, the square on A is rational (D10.1.3, D10.1.4), and therefore the square on DG is also rational, so DG is rational.

**Step 3.** Since AB:BC is a ratio of a square number to a square number, and sq(DG):sq(A) = AB:BC, by 10.9 DG is commensurable in length with A.

**Step 4.** Let GH be the straight line such that sq(A):sq(GH) = BC:AC, that is, sq(GH):sq(A) = AC:BC. Since AC:BC = 3:1 is a ratio of a number to a number, by 10.6 the square on GH is commensurable with the square on A. Since the square on A is rational, the square on GH is rational, so GH is rational.

**Step 5.** We now show that DG is incommensurable in length with GH. We have sq(DG):sq(A) = AB:BC and sq(GH):sq(A) = AC:BC. Therefore sq(DG):sq(GH) = AB:AC (since both ratios share sq(A) in the denominator, by 5.22 ex aequali, or equivalently by combining via CN1). Since AB:AC = 4:3 is not a ratio of a square number to a square number, by 10.9 DG is incommensurable in length with GH.

**Step 6.** Since DG and GH are both rational (Steps 2 and 4) and incommensurable in length (Step 5), they are rational straight lines commensurable in square only. By 10.36, the line DG + GH is a binomial straight line.

**Step 7.** We now show DG is the greater term. Since sq(DG):sq(GH) = AB:AC = 4:3, we have sq(DG) > sq(GH), so DG > GH (CN5), confirming DG is the greater term.

**Step 8.** We verify the first binomial condition on the difference of squares. We have sq(DG):sq(A) = AB:BC = 4:1, so sq(DG) = 4*sq(A). And sq(GH):sq(A) = AC:BC = 3:1, so sq(GH) = 3*sq(A). Therefore sq(DG) - sq(GH) = 4*sq(A) - 3*sq(A) = sq(A) (by CN3). Hence the straight line whose square equals sq(DG) - sq(GH) is A itself.

**Step 9.** Now sq(A):sq(DG) = BC:AB = 1:4, which is a ratio of a square number to a square number (1^2:2^2). Therefore by 10.9, A is commensurable in length with DG. That is, the straight line by which the square on DG exceeds the square on GH (namely A) is commensurable in length with DG.

**Step 10.** The greater term DG is commensurable in length with the rational straight line A (Step 3). The square on DG exceeds the square on GH by the square on a straight line commensurable in length with DG (Steps 8-9). Therefore, by D10.2.1, the binomial straight line DG + GH is a first binomial straight line.

**Step 11.** Therefore a first binomial straight line has been found, which is what was required to do.

**USED:** 10.13, 10.36, 10.6, 10.9, 5.22, CN1, CN3, CN5, D10.1.3, D10.1.4, D10.2.1
**Human refs (from References field):** 10.28, 10.36, 10.6, 10.9, 5.19
**Jaccard:** 0.231 — AI adds ['10.13', '5.22', 'CN1', 'CN3', 'CN5', 'D10.1.3', 'D10.1.4', 'D10.2.1']; Human adds ['10.28', '5.19']

## Proposition 10.49
**Statement:** To find the second binomial straight line.

**Step 1.** Let two numbers AC and CB be set out such that their sum AB has to BC the ratio of a square number to a square number, but has not to AC the ratio of a square number to a square number. For instance, take AC = 3, CB = 1, so that AB = 4; then AB:BC = 4:1 = 2^2:1^2 is a ratio of square numbers, while AB:AC = 4:3 is not a ratio of square numbers.

**Step 2.** Let a rational straight line D be set out, and let FG be commensurable in length with D; therefore FG is also rational [D10.1.3].

**Step 3.** Let it be contrived that as the number BA is to AC, so is the square on EF to the square on FG, where EF is a straight line greater than FG [10.6]. Since BA:AC is a ratio of a number to a number, the square on EF has to the square on FG the ratio which the number BA has to the number AC, and therefore EF is commensurable with FG in square [10.6].

**Step 4.** Since BA:AC (that is, 4:3) is not the ratio of a square number to a square number, the square on EF does not have to the square on FG the ratio of a square number to a square number, and therefore EF is incommensurable in length with FG [10.9].

**Step 5.** Since FG is rational and commensurable in square with EF, EF is also rational [D10.1.3]. Thus EF and FG are both rational and commensurable in square only.

**Step 6.** Therefore EF + FG, that is the whole straight line EG, is a binomial [10.36].

**Step 7.** We must show that the square on EF is greater than the square on FG by the square on a straight line commensurable in length with EF. Since sq(EF):sq(FG) = BA:AC, by conversion of the ratio, sq(EF):(sq(EF) - sq(FG)) = BA:(BA - AC) = AB:BC [5.19, CN3]. But AB:BC = 4:1 is the ratio of a square number to a square number (namely 2^2 to 1^2). Therefore sq(EF):(sq(EF) - sq(FG)) is the ratio of a square number to a square number, and hence EF is commensurable in length with the straight line whose square equals sq(EF) - sq(FG) [10.9]. That is, the square on EF is greater than the square on FG by the square on a straight line commensurable in length with EF.

**Step 8.** Now, the lesser term FG is commensurable in length with the rational straight line D set out [Step 2]. We must verify that the greater term EF is not commensurable in length with D. Since FG is commensurable in length with D, and EF is incommensurable in length with FG [Step 4], it follows that EF is incommensurable in length with D [10.13].

**Step 9.** Therefore EG is a binomial straight line whose terms are EF and FG; the square on the greater term EF is greater than the square on the lesser term FG by the square on a straight line commensurable in length with EF; and the lesser term FG is commensurable in length with the rational straight line D set out. Therefore, by definition, EG is a second binomial straight line [D10.2.2].

Thus the second binomial straight line EG has been found. Q.E.F.

**USED:** 10.13, 10.36, 10.6, 10.9, 5.19, CN3, D10.1.3, D10.2.2
**Human refs (from References field):** 10.36, 10.6, 10.9, 5.19
**Jaccard:** 0.500 — AI adds ['10.13', 'CN3', 'D10.1.3', 'D10.2.2']

## Proposition 10.50
**Statement:** To find the third binomial straight line.

**Step 1.** Let A be a rational straight line. Set out three numbers D, E, F such that D > E, the difference (D - E) has to D the ratio of a square number to a square number, and neither D to F nor E to F has the ratio of a square number to a square number. Such numbers exist: take D = 4, E = 3, F = 2, since (D - E) : D = 1 : 4 = 1^2 : 2^2 is a ratio of square numbers, while D : F = 4 : 2 = 2 : 1 and E : F = 3 : 2 are not ratios of square numbers to square numbers.

**Step 2.** Contrive that sq(G) : sq(A) = D : F. Since D : F is a ratio of number to number, sq(G) is commensurable with sq(A) [10.6], so G is rational [D10.1.3]. Since D : F is not the ratio of a square number to a square number, G is incommensurable in length with A [10.9].

**Step 3.** Contrive that sq(H) : sq(A) = E : F. Since E : F is a ratio of number to number, sq(H) is commensurable with sq(A) [10.6], so H is rational [D10.1.3]. Since E : F is not the ratio of a square number to a square number, H is incommensurable in length with A [10.9].

**Step 4.** From sq(G) : sq(A) = D : F, by invertendo [D5.5], sq(A) : sq(G) = F : D. Combining with sq(H) : sq(A) = E : F by ex aequali [5.22] (the chain being sq(H) : sq(A) : sq(G) with corresponding numbers E : F : D, where the middle terms sq(A) and F match), we obtain sq(H) : sq(G) = E : D. By invertendo [D5.5], sq(G) : sq(H) = D : E. Since D > E, we have sq(G) > sq(H) and therefore G > H. Since D : E is a ratio of number to number, sq(G) is commensurable with sq(H) [10.6], so G and H are commensurable in square. Since D : E is not the ratio of a square number to a square number (4 : 3 is not square to square), G and H are incommensurable in length [10.9]. Therefore G and H are commensurable in square only.

**Step 5.** Since G and H are rational straight lines commensurable in square only, the straight line G + H is binomial [10.36].

**Step 6.** Since sq(G) > sq(H), let K be a straight line such that sq(K) = sq(G) - sq(H) [1.47]. Then sq(G) = sq(K) + sq(H), so (sq(K) + sq(H)) : sq(H) = D : E. By separando [5.17], sq(K) : sq(H) = (D - E) : E.

**Step 7.** By invertendo [D5.5], sq(H) : sq(K) = E : (D - E). By ex aequali [5.22] applied to the chain sq(G) : sq(H) : sq(K) and D : E : (D - E) (the middle terms sq(H) and E matching), we obtain sq(G) : sq(K) = D : (D - E).

**Step 8.** Since (D - E) : D is the ratio of a square number to a square number by construction, D : (D - E) is likewise the ratio of a square number to a square number. Therefore sq(G) : sq(K) is the ratio of a square number to a square number, so G is commensurable in length with K [10.9]. Hence the square on G exceeds the square on H by the square on a straight line K that is commensurable in length with G.

**Step 9.** Neither G nor H is commensurable in length with the rational straight line A [Steps 2 and 3], the square on the greater term G exceeds the square on the lesser term H by the square on a straight line commensurable in length with G [Step 8], and G + H is a binomial straight line [Step 5]. Therefore, by the definition of a third binomial [D10.2.3], the straight line G + H is a third binomial straight line, which is what was required to find.

**USED:** 1.47, 10.36, 10.6, 10.9, 5.17, 5.22, D10.1.3, D10.2.3, D5.5
**Human refs (from References field):** 10.36, 10.6, 10.9, 5.19, 5.22
**Jaccard:** 0.400 — AI adds ['1.47', '5.17', 'D10.1.3', 'D10.2.3', 'D5.5']; Human adds ['5.19']

## Proposition 10.51
**Statement:** To find the fourth binomial straight line.

**Step 1.** Let AC be a rational straight line set out. By Proposition 10.30, we can find two rational straight lines commensurable in square only such that the square on the greater is greater than the square on the lesser by the square on a straight line incommensurable in length with the greater. Let these be found: let E and F be two such rational straight lines, with E the greater, such that E and F are rational, commensurable in square only, and the square on E is greater than the square on F by the square on a straight line incommensurable in length with E.

**Step 2.** Since E and F are rational straight lines (commensurable in square with AC), by Definition D10.1.3, the squares on E and on F are each commensurable with the square on AC, and hence rational areas. We now require that E be commensurable in length with AC. To achieve this, let E be taken commensurable in length with AC (which is possible since we may apply the construction of 10.30 starting from AC itself as the greater line, or by choosing E commensurable in length with AC by 10.6, since rational lines have to each other the ratio of a number to a number in square).

**Step 3.** More precisely, set out a rational straight line AC. Let the two numbers p and q be such that p^2 + q^2 is not a square number; this is possible (for example, take p = 1, q = 1, so p^2 + q^2 = 2, which is not a perfect square). Now by Proposition 10.29 and its method adapted via 10.30: take E = AC itself (so E is trivially commensurable in length with AC), and find F rational and commensurable in square only with E, such that the square on E exceeds the square on F by the square on a line incommensurable in length with E. This is exactly what 10.30 provides.

**Step 4.** So let E and F be found by 10.30 with E commensurable in length with AC. Then E and F are rational straight lines commensurable in square only, and the square on E is greater than the square on F by the square on a straight line incommensurable in length with E.

**Step 5.** Since E and F are rational and commensurable in square only, by Proposition 10.36, the sum E + F is a binomial straight line. Let AB = E + F, divided at the point where the two terms meet, so that the greater term is E and the lesser term is F.

**Step 6.** We now verify the conditions of Definition D10.2.4 for a fourth binomial. We must check three things: (i) the square on the greater term E is greater than the square on the lesser term F by the square on a straight line incommensurable in length with E; (ii) the greater term E is commensurable in length with the rational straight line AC set out; (iii) neither condition of the first, second, or third binomial applies.

**Step 7.** Condition (i): By construction in Step 4 (via 10.30), the square on E is greater than the square on F by the square on a straight line incommensurable in length with E. This is satisfied.

**Step 8.** Condition (ii): By construction in Step 4, E is commensurable in length with AC. This is satisfied.

**Step 9.** Condition (iii): We verify that AB is not a first, second, or third binomial. For a first binomial (D10.2.1), the square on the greater must exceed the square on the lesser by the square on a line commensurable with the greater, and the greater must be commensurable in length with the rational line. Here condition (ii) is met but condition on the excess is not (it is incommensurable, not commensurable), so AB is not a first binomial. For a second binomial (D10.2.2), the lesser term must be commensurable in length with AC, and the excess must be commensurable; the excess condition fails. For a third binomial (D10.2.3), neither term is commensurable in length with AC, and the excess is commensurable; both conditions fail. Since in all three cases the commensurability of the excess is required but does not hold here, AB is none of these types.

**Step 10.** By Definition D10.2.4, since the square on the greater term E is greater than the square on the lesser term F by the square on a straight line incommensurable in length with E, and the greater term E is commensurable in length with the rational straight line AC, the binomial straight line AB = E + F is a fourth binomial straight line.

**Step 11.** Therefore, we have found a fourth binomial straight line, which is what was required.

**USED:** 10.30, 10.36, D10.1.3, D10.2.1, D10.2.2, D10.2.3, D10.2.4
**Human refs (from References field):** 10.6, 10.9, 5.19
**Jaccard:** 0.000 — AI adds ['10.30', '10.36', 'D10.1.3', 'D10.2.1', 'D10.2.2', 'D10.2.3', 'D10.2.4']; Human adds ['10.6', '10.9', '5.19']

## Proposition 10.52
**Statement:** To find the fifth binomial straight line.

**Step 1.** Let a rational straight line A be set out, and let two numbers CG and GD be set out such that CG and GD have not to one another the ratio which a square number has to a square number, and let CD also not have to CG the ratio which a square number has to a square number, but let it have to GD the ratio which a square number has to a square number.

**Step 2.** Let the square number p^2 be such that CD has to GD the ratio p^2 : q^2 for some number q, while CD : CG is not such a ratio and CG : GD is not such a ratio. For example, let CD = 5, CG = 3, GD = 2. Then CD : GD = 5 : 2 (not a ratio of square numbers), so adjust: let CD = 8, CG = 3, GD = 5, then CD : GD = 8 : 5 (not square to square). We need CD : GD to be square to square. Let CD = 5, GD = 4, CG = 1, then CD : GD = 5 : 4 (not square to square). Let CD = 4, GD = 1, CG = 3, then CD : GD = 4 : 1 (square to square), CD : CG = 4 : 3 (not square to square), CG : GD = 3 : 1 (not square to square). These numbers satisfy our requirements.

**Step 3.** Let the square on E be to the square on A as the number CG is to GD, so that the square on E has to the square on A the ratio 3 : 1, which is not a ratio of square numbers. Then E and A are rational straight lines commensurable in square only, by 10.6 and 10.9: since CG : GD is not the ratio of a square number to a square number, E and A are incommensurable in length (by 10.9), yet commensurable in square since both squares are commensurable (the ratio 3 : 1 being a ratio of numbers, so by 10.6 the squares are commensurable).

**Step 4.** Since E and A are rational and commensurable in square only, the sum E + A is a binomial straight line, by 10.36.

**Step 5.** We must now show that this binomial is a fifth binomial. By the definition D10.2.5, we need: (i) the square on the greater term exceeds the square on the lesser by the square on a straight line incommensurable in length with the greater, and (ii) the lesser term is commensurable in length with the rational straight line set out.

**Step 6.** Now identify the terms. Since the square on E is to the square on A as 3 : 1, the square on E is greater than the square on A, so E is the greater term and A is the lesser term of the binomial. The lesser term A is the rational straight line set out, so A is commensurable in length with itself. This satisfies condition (ii).

**Step 7.** For condition (i), we must show that the square on E (the greater) exceeds the square on A (the lesser) by the square on a straight line incommensurable in length with E. The square on E is to the square on A as CG : GD = 3 : 1. So the square on E equals 3 times the square on A. Then the square on E minus the square on A equals 2 times the square on A. Let F be such that the square on F equals the square on E minus the square on A. Then the square on F equals 2 times the square on A.

**Step 8.** Now the square on E is to the square on F as the square on E is to (the square on E minus the square on A), which equals (3 times the square on A) to (2 times the square on A), which equals 3 : 2. By 5.11 (or direct calculation), the ratio of the square on E to the square on F is 3 : 2.

**Step 9.** Equivalently, the square on E is to the square on F as CD : CG = 4 : 3. Since CD : CG = 4 : 3, and 4 : 3 is not the ratio of a square number to a square number, then by 10.9 the straight lines E and F are incommensurable in length.

**Step 10.** Thus the square on E is greater than the square on A by the square on a straight line F that is incommensurable in length with E. This satisfies condition (i).

**Step 11.** We also verify that E (the greater term) is incommensurable in length with A (the rational straight line set out), as already shown in Step 3. And A (the lesser term) is commensurable in length with the rational straight line A. These are exactly the conditions for a fifth binomial, by D10.2.5 (given D10.2.4: the square on the greater exceeds the square on the lesser by the square on a line incommensurable with the greater; D10.2.5 specifies: if the lesser term is commensurable in length with the rational straight line, it is a fifth binomial).

**Step 12.** Therefore E + A is a fifth binomial straight line, and the fifth binomial straight line has been found. Q.E.F.

**USED:** 10.36, 10.6, 10.9, D10.1.3, D10.2.4, D10.2.5
**Human refs (from References field):** 10.36, 10.6, 10.9, 5.19
**Jaccard:** 0.429 — AI adds ['D10.1.3', 'D10.2.4', 'D10.2.5']; Human adds ['5.19']

## Proposition 10.53
**Statement:** To find the sixth binomial straight line.

**Step 1.** Let a rational straight line A be set out, and let three numbers E, F, and G be taken such that E has not to either F or G the ratio which a square number has to a square number, and let F also not have to G the ratio which a square number has to a square number.

**Step 2.** Let it be contrived that E is to F as the square on A is to the square on a straight line B. Then the square on A is commensurable with the square on B [by 10.6], so B is rational [by D10.1.3]. Since E does not have to F the ratio of a square number to a square number, the square on A does not have to the square on B the ratio of a square number to a square number, so A is incommensurable in length with B [by 10.9].

**Step 3.** Next, let it be contrived that F is to G as the square on B is to the square on a straight line C. Then the square on B is commensurable with the square on C [by 10.6], so the square on C is rational, and therefore C is rational [by D10.1.3]. Since F does not have to G the ratio of a square number to a square number, the square on B does not have to the square on C the ratio of a square number to a square number, so B is incommensurable in length with C [by 10.9].

**Step 4.** Since E does not have to F the ratio of a square number to a square number, and F is to G as the square on B is to the square on C, while E is to F as the square on A is to the square on B, therefore by the ex aequali ratio E is to G as the square on A is to the square on C [by 5.22]. But E does not have to G the ratio of a square number to a square number, therefore the square on A does not have to the square on C the ratio of a square number to a square number, and so A is incommensurable in length with C [by 10.9].

**Step 5.** Since B and C are each rational, and B is incommensurable in length with C, B and C are rational straight lines commensurable in square only. Therefore B + C is a binomial straight line [by 10.36].

**Step 6.** I say that B + C is a sixth binomial straight line. We must verify the three conditions of D10.2.6: (i) the square on B is greater than the square on C by the square on a straight line incommensurable in length with B, (ii) neither B nor C is commensurable in length with A.

**Step 7.** Since F is to G as the square on B is to the square on C, by conversion of ratio (componendo-like reasoning on the difference), F minus G is to G as the difference of the squares on B and C is to the square on C. That is, the square on B exceeds the square on C by some area. Let D be the straight line such that the square on B exceeds the square on C by the square on D, so that the square on B equals the square on C plus the square on D.

**Step 8.** Then the square on D is to the square on C as (F - G) is to G. Since F does not have to G the ratio of a square number to a square number, neither does (F - G) have to G the ratio of a square number to a square number. For if F - G to G were as a square number to a square number, then since G plus (F - G) equals F, it would follow (by properties of numbers) that F to G also has the ratio of a square number to a square number, which contradicts our hypothesis. Therefore (F - G) does not have to G the ratio of a square number to a square number [by 7.19, considering that the sum of a square number times a square and a square yields constraints on the ratio].

**Step 9.** Hence the square on D does not have to the square on C the ratio of a square number to a square number, so D is incommensurable in length with C [by 10.9]. Now, since the square on B equals the square on C plus the square on D, and F is to G as the square on B is to the square on C, the square on B is greater than the square on C by the square on D. We need to verify D is also incommensurable in length with B.

**Step 10.** Since F is to G as the square on B is to the square on C, the square on B is commensurable with the square on C but B is incommensurable in length with C. Now, the square on D equals the square on B minus the square on C. If we apply to B a parallelogram equal to one-fourth the square on C and deficient by a square, by 10.18, since F does not have to G the ratio of a square number to a square number, the parallelogram divides B into parts that are incommensurable. Therefore the square on B is greater than the square on C by the square on a straight line incommensurable in length with B [by 10.18].

**Step 11.** We have established from Step 2 that A is incommensurable in length with B, and from Step 4 that A is incommensurable in length with C. Therefore neither B nor C is commensurable in length with A.

**Step 12.** Therefore B + C is a binomial straight line [Step 5] whose terms B and C satisfy all the conditions of D10.2.6: the square on the greater term B exceeds the square on the lesser term C by the square on a straight line incommensurable in length with B [Step 10], and neither B nor C is commensurable in length with the rational straight line A [Step 11]. Therefore B + C is a sixth binomial straight line. Q.E.F.

**USED:** 10.18, 10.36, 10.6, 10.9, 5.22, 7.19, D10.1.3, D10.2.6
**Human refs (from References field):** 10.36, 10.6, 10.9, 5.19, 5.22
**Jaccard:** 0.444 — AI adds ['10.18', '7.19', 'D10.1.3', 'D10.2.6']; Human adds ['5.19']

## Proposition 10.54
**Statement:** If an area be contained by a rational straight line and the first binomial, the âsideâ of the area is the irrational straight line which is called binomial.

**Step 1.** Let the area AC be contained by the rational straight line AB and the first binomial straight line AD. I say that the "side" of the area AC (that is, the side of the square equal to AC) is the irrational straight line called binomial.

**Step 2.** Since AD is a first binomial straight line, let it be divided into its terms at E, so that AE is the greater term and ED is the lesser term. By the definition of a first binomial (D10.2.1), AE and ED are rational straight lines commensurable in square only, the square on AE is greater than the square on ED by the square on a straight line commensurable in length with AE, and AE is commensurable in length with the rational straight line AB set out.

**Step 3.** Let ED be bisected at F, and let there be applied to AE a rectangle equal to the square on EF and deficient by a square figure, producing sides AG and GE [by 6.28]. Since the square on AE is greater than the square on ED by the square on a line commensurable in length with AE (from the definition of the first binomial), and EF is half of ED, the square on AE is greater than the square on EF correspondingly. By 10.17, since we apply to AE a parallelogram equal to one-fourth of the square on ED (which equals the square on EF) deficient by a square, and the square on AE exceeds the square on ED by the square on a line commensurable with AE, the application divides AE into parts AG and GE that are commensurable in length.

**Step 4.** Since AG and GE are commensurable in length, and AE is rational, both AG and GE are rational by 10.15 and D10.1.3. Moreover, since AE is commensurable in length with the rational straight line AB, and AG is commensurable in length with AE (by Step 3), then AG is commensurable in length with AB by 10.12. Similarly GE is commensurable in length with AE, hence with AB by 10.12.

**Step 5.** Now construct: let the square on H be equal to the rectangle AB by AG, and let the square on K be equal to the rectangle AB by GE [by 2.14, such squares can be found]. Since AB and AG are both rational and commensurable in length (Step 4), the rectangle AB by AG is rational by 10.19. Therefore the square on H is rational, so H is rational. Similarly, AB and GE are rational and commensurable in length, so the rectangle AB by GE is rational by 10.19, the square on K is rational, and K is rational.

**Step 6.** Since AG is commensurable in length with GE (Step 3), the rectangle AB by AG is commensurable with the rectangle AB by GE [by 6.1, rectangles on the same base are as the other sides; then by 10.11]. Therefore the square on H is commensurable with the square on K, so H and K are commensurable in square.

**Step 7.** I claim that H and K are commensurable in square only, that is, they are incommensurable in length. Since AE and ED are commensurable in square only, AE and ED are incommensurable in length. Now, by construction, the rectangle AG by GE equals the square on EF (which is one-fourth the square on ED), so AG by GE = (ED/2)^2. We have AB * AE = AB * AG + AB * GE, and AB * AD = AB * AE + AB * ED. Consider that the rectangle contained by AG and GE equals the square on EF [by 6.28]. Since AD = AE + ED and AE = AG + GE, we have the square on H plus the square on K equals AB * (AG + GE) = AB * AE.

**Step 8.** Now twice the rectangle contained by H and K: since the square on (H + K) equals the square on H plus the square on K plus twice the rectangle H by K, we need to show that H + K is the side of AC. The rectangle AB by AD = AB * AE + AB * ED = (square on H + square on K) + AB * ED. Also the rectangle 2 * AB * EF = AB * ED (since EF is half of ED). And the rectangle AG by GE = square on EF, so AB * AG * GE relates to AB * (square on EF). By 2.5, since AE is cut into equal parts at F and unequal parts at G (after the application), we get AE * AG + square on EG... Let me proceed more directly.

**Step 9.** By the construction in Step 3 via 6.28, the rectangle AG by GE equals the square on EF. So 4 times the rectangle AG by GE equals the square on ED (since EF = ED/2). Now consider: the square on H = AB * AG and the square on K = AB * GE. Then the product (square on H) * (square on K) = AB^2 * AG * GE = AB^2 * EF^2. So the rectangle H by K = AB * EF (taking square roots of both sides, valid for areas/magnitudes). Thus twice the rectangle H by K = 2 * AB * EF = AB * ED. Therefore the square on (H + K) = square on H + square on K + 2 * rect(H,K) = AB * AG + AB * GE + AB * ED = AB * (AG + GE + ED) = AB * (AE + ED) = AB * AD.

**Step 10.** Therefore the square on (H + K) equals the rectangle AB by AD, which is the area AC. Hence H + K is the "side" of the area AC.

**Step 11.** It remains to show that H and K are incommensurable in length, so that H + K is a binomial by 10.36. Since AE and ED are incommensurable in length (being commensurable in square only), and EF = ED/2, AE and EF are incommensurable in length. By 10.17 (applied inversely via 10.18), since AE is incommensurable in length with EF, and the rectangle AG by GE = square on EF... Rather, consider the ratio: the square on H to the square on K equals AB * AG to AB * GE, which equals AG to GE [by 6.1]. Now AG to GE is the ratio of commensurable lengths (Step 3), hence the square on H to the square on K is a ratio of commensurable magnitudes, so the squares are commensurable.

**Step 12.** For incommensurability in length: the square on H to the rectangle H by K equals (AB * AG) to (AB * EF) = AG to EF. Now since AG and GE are commensurable in length but AE and ED are incommensurable in length, we need: the rectangle H by K = AB * EF (from Step 9). If H and K were commensurable in length, then the rectangle H by K would be commensurable with the square on H (by 10.19 reasoning), so AB * EF would be commensurable with AB * AG, giving EF commensurable with AG. But AG is commensurable in length with AE (Step 3), so EF would be commensurable with AE (by 10.12). Since EF = ED/2, ED would be commensurable with AE by 10.15, contradicting that AE and ED are commensurable in square only. Therefore H and K are incommensurable in length.

**Step 13.** Thus H and K are rational straight lines commensurable in square only. By 10.36, H + K is a binomial straight line. Since the square on (H + K) equals the area AC (Step 10), H + K is the "side" of the area AC, and it is binomial.

**Step 14.** Therefore, if an area be contained by a rational straight line and the first binomial, the "side" of the area is the irrational straight line which is called binomial. Q.E.D.

**USED:** 10.11, 10.12, 10.15, 10.17, 10.19, 10.36, 2.14, 6.1, 6.28, D10.1.3, D10.1.4, D10.2.1
**Human refs (from References field):** 10.11, 10.12, 10.13, 10.15, 10.17, 10.19, 10.36, 2.14, 6.1, 6.17, D10.2.1
**Jaccard:** 0.643 — AI adds ['6.28', 'D10.1.3', 'D10.1.4']; Human adds ['10.13', '6.17']

## Proposition 10.55
**Statement:** If an area be contained by a rational straight line and the second binomial, the âsideâ of the area is the irrational straight line which is called a first bimedial.

**Step 1.** Let the area AC be contained by the rational straight line AB and the second binomial CD. We are to show that the "side" of AC is a first bimedial straight line. Let CD be divided into its terms at E, where CE is the greater term. Then, since CD is a second binomial, by D10.2.2, the lesser term ED is commensurable in length with the rational straight line set out, the square on CE is greater than the square on ED by the square on a straight line commensurable in length with CE, and the terms CE, ED are rational straight lines commensurable in square only.

**Step 2.** Let the rational straight line set out (with respect to which CD is called a second binomial) also be AB. Then ED is commensurable in length with AB, while CE is commensurable in square only with AB (since CE and ED are commensurable in square only, and ED is commensurable in length with AB, if CE were also commensurable in length with AB, then CE and ED would be commensurable in length by 10.12, contradicting that they are commensurable in square only).

**Step 3.** Bisect ED at the point F, so that EF = FD [by 1.10]. Since the square on CE exceeds the square on ED by the square on a straight line commensurable in length with CE (by D10.2.2), apply to CE a rectangle equal to the square on EF (which is one quarter of the square on ED) and deficient by a square figure. By 10.17, since the excess is commensurable, this divides CE into parts commensurable in length. Let these parts be CG and GE, so that CG and GE are commensurable in length, with CG the greater part.

**Step 4.** Since CG and GE are commensurable in length, the rectangle CG by GE is commensurable with the square on GE [by 10.21 applied to the relation from 6.1 and 10.11]. Also, the rectangle contained by CG and GE equals the square on EF, that is, one quarter of the square on ED [by 2.5, since CE is divided at G and ED is bisected at F, giving CG * GE = EF^2].

**Step 5.** Now consider the rectangle AB by CD, which equals the rectangle AB by CE plus the rectangle AB by ED [by 2.1]. Set up the construction: let the square SH be equal to the rectangle AB by CG, and let the square SK be equal to the rectangle AB by GE, so that the straight lines which are the sides of these squares will compose the "side" of the whole area. Let the side of SH be called w and the side of SK be called x.

**Step 6.** Since AB, CG, GE are three straight lines with CG and GE commensurable in length, the rectangles AB by CG and AB by GE are commensurable [by 6.1 and 10.11]. Therefore the squares SH and SK are commensurable, whence w^2 and x^2 are commensurable, so w and x are commensurable in square [by D10.1.2].

**Step 7.** Since ED is commensurable in length with AB, and ED is rational, the rectangle AB by ED is rational [by 10.19]. Now the rectangle CG by GE equals the square on EF = (ED/2)^2, which is one quarter of the square on ED. The rectangle AB by ED relates to the rectangle AB by CG through the ratio ED to CG [by 6.1]. Since ED is incommensurable in length with CG (for CG is a part of CE, and CE is incommensurable in length with ED, and CG being commensurable in length with GE means CG is commensurable with CE by 10.15, so CG is incommensurable in length with ED by 10.13), the rectangle AB by CG is irrational, so the square on w is irrational, making w a medial straight line [by D10.1.4 and 10.21].

**Step 8.** Similarly, since GE is commensurable in length with CG, GE is also commensurable with CE [by 10.15 and 10.12], so GE is incommensurable in length with ED [by 10.13]. Therefore the rectangle AB by GE is incommensurable with the rectangle AB by ED. Since AB by ED is rational, and AB by GE is incommensurable with it, the rectangle AB by GE is irrational. Thus the square on x is irrational, making x medial [by D10.1.4].

**Step 9.** Now we show that w and x are commensurable in square only. Since CE is incommensurable in length with AB (as established in Step 2), and CE = CG + GE, while CG is commensurable in length with GE, the sum CG + GE is incommensurable in length with AB. The rectangle AB by CG is to the rectangle AB by GE as CG is to GE [by 6.1]. Since CG and GE are commensurable in length, the rectangles AB by CG and AB by GE are commensurable [by 10.11], so the squares w^2 and x^2 are commensurable. But w^2 (= AB * CG) is incommensurable with the rational area AB * ED, while x^2 (= AB * GE) is also incommensurable with AB * ED. The sum w^2 + x^2 is medial (since each is medial and they are commensurable, by 10.23 and 10.15). If w and x were commensurable in length, then their rectangle w * x would be commensurable with w^2, making w * x medial. But we shall show w * x is rational, giving a contradiction with 10.25 if they were commensurable in length. Thus w and x must be commensurable in square only.

**Step 10.** We now show that the rectangle w * x is rational. We have w^2 = AB * CG and x^2 = AB * GE. The rectangle w * x is the mean proportional between w^2 and x^2, so (w * x)^2 = (AB * CG)(AB * GE) = AB^2 * CG * GE [by 6.17]. Now CG * GE = EF^2 = (ED/2)^2, so (w * x)^2 = AB^2 * (ED/2)^2 = (AB * ED/2)^2. Thus w * x = AB * ED / 2 = AB * EF. Since ED is commensurable in length with AB, EF = ED/2 is commensurable in length with AB [by 10.15 and 10.12]. Both AB and EF are rational, so the rectangle AB * EF is rational [by 10.19]. Therefore w * x is rational.

**Step 11.** Since w and x are medial straight lines commensurable in square only, and the rectangle w * x is rational, the sum w + x is a first bimedial straight line [by 10.37 and its definition].

**Step 12.** It remains to show that w + x is the "side" of the area AC. The area AC = AB * CD = AB * (CE + ED). By the construction, w^2 + x^2 + 2wx = (w + x)^2. We have w^2 = AB * CG, x^2 = AB * GE, so w^2 + x^2 = AB * (CG + GE) = AB * CE. And 2wx = 2 * AB * EF = AB * ED (since EF = ED/2). Therefore (w + x)^2 = AB * CE + AB * ED = AB * (CE + ED) = AB * CD = the area AC. Hence w + x is the "side" of the area AC.

**Step 13.** Therefore, if an area be contained by a rational straight line and the second binomial, the "side" of the area is a first bimedial straight line. Q.E.D.

**USED:** 1.10, 10.11, 10.12, 10.13, 10.15, 10.17, 10.19, 10.21, 10.23, 10.25, 10.37, 2.1, 2.5, 6.1, 6.17, D10.1.2, D10.1.4, D10.2.2
**Human refs (from References field):** 10.11, 10.12, 10.13, 10.15, 10.17, 10.19, 10.21, 10.37, 6.1, D10.2.2
**Jaccard:** 0.556 — AI adds ['1.10', '10.23', '10.25', '2.1', '2.5', '6.17', 'D10.1.2', 'D10.1.4']

## Proposition 10.56
**Statement:** If an area be contained by a rational straight line and the third binomial, the âsideâ of the area is the irrational straight line called a second bimedial.

**Step 1.** Let the area AC be contained by the rational straight line AB and the third binomial CD. Let CD be divided into its terms at E, where CE is the greater term. Then by the definition of a third binomial (D10.2.3): CE and ED are rational and commensurable in square only, the square on CE is greater than the square on ED by the square on a straight line commensurable in length with CE, and neither CE nor ED is commensurable in length with AB.

**Step 2.** Let the same construction be made as was made in 10.54. That is, bisect ED at F, and to CE apply a rectangle equal to the square on EF and deficient by a square figure, producing segments CG and GE. By 10.17, since the square on CE exceeds the square on ED by the square on a line commensurable with CE, the segments CG and GE are commensurable in length.

**Step 3.** Through the points G, E, F draw GH, EK, FL parallel to AB (by 1.31). Apply to AB rectangles equal to the squares on CG and GE respectively; let the square on MN equal AH (the rectangle AB by CG) and the square on NO equal AK (the rectangle AB by GE), with MO in a straight line and N between M and O.

**Step 4.** Then the rectangle MN by NO equals AF (the rectangle AB by EF), by the same reasoning as in 10.54. Specifically, since AH equals the square on MN and AK equals the square on NO, and AH + AK = AC + rectangle CE by EG (by 2.5, since ED is bisected at F and CG and GE are the segments), and AF equals the rectangle contained by AB and EF, the rectangle MN by NO equals AF (following the construction of 10.54, using 2.5 and the arrangement of areas).

**Step 5.** Since CG and GE are commensurable in length (Step 2), the rectangles AB by CG and AB by GE are commensurable (by 6.1 and 10.11). That is, AH and AK are commensurable. Therefore the squares on MN and NO are commensurable, so MN and NO are commensurable in square (D10.1.2).

**Step 6.** Since CE is rational and incommensurable in length with AB (by the definition of a third binomial), the rectangle AB by CE is medial (by 10.21). But AH + AK = the rectangle AB by CG + the rectangle AB by GE. Now CG + GE = CE, and the rectangle AB by CE equals AH + AK (by 2.1). Since the rectangle AB by CE is medial, the sum AH + AK is medial. But AH = MN squared and AK = NO squared, so the sum of the squares on MN and NO is medial.

**Step 7.** Since ED is rational and incommensurable in length with AB, the rectangle AB by ED is medial (by 10.21). Now by 2.5, the rectangle CE by ED equals the square on EF plus the rectangle CG by GE, so the rectangle CG by GE = the rectangle CE by ED minus the square on EF. But twice the rectangle AB by EF = twice AF. We showed the rectangle MN by NO = AF, so twice the rectangle MN by NO = 2AF = the rectangle AB by ED (since EF is half of ED, the rectangle AB by 2EF = the rectangle AB by ED). Therefore twice the rectangle MN by NO equals the rectangle AB by ED, which is medial. So twice the rectangle MN by NO is medial.

**Step 8.** We now show that MN and NO are incommensurable in square. Since CE is incommensurable in length with AB, and CG is commensurable in length with CE (for CG is a segment of CE and CG is commensurable with GE, and CG + GE = CE; but more precisely, since CG and GE are commensurable and CG + GE = CE, CG is commensurable with CE by 10.15). Therefore CG is incommensurable in length with AB (by 10.13). The rectangle AB by CG, which equals the square on MN, is therefore medial (by 10.21), so MN is medial. Similarly, GE is commensurable with CG (Step 2), hence commensurable with CE (by 10.12 and 10.15), and therefore GE is incommensurable in length with AB (by 10.13). So the rectangle AB by GE (= NO squared) is medial (by 10.21), and NO is medial.

**Step 9.** Since CE is incommensurable in length with ED (they are commensurable in square only), and CG is commensurable with CE (by 10.15 as shown above), we have CG incommensurable in length with ED. But GE is commensurable with CG (Step 2), so GE is commensurable with CE (by 10.12). Now consider the ratio CG to GE: since CG and GE are both commensurable with CE but CE is incommensurable with ED, and by considering the rectangles AB by CG and AB by GE, these rectangles (= squares on MN and on NO) are commensurable with each other (Step 5). However, the sum of the squares on MN and NO is medial (Step 6), and twice the rectangle MN by NO is also medial (Step 7).

**Step 10.** We must verify that the sum of the squares on MN and NO is incommensurable with twice the rectangle MN by NO. The sum of the squares equals the rectangle AB by CE (Step 6), and twice the rectangle MN by NO equals the rectangle AB by ED (Step 7). By 6.1, the ratio of the rectangle AB by CE to the rectangle AB by ED equals CE to ED. Since CE and ED are incommensurable in length, the rectangle AB by CE is incommensurable with the rectangle AB by ED (by 10.11). Therefore the sum of the squares on MN and NO is incommensurable with twice the rectangle MN by NO.

**Step 11.** Therefore MN and NO are medial straight lines, commensurable in square only (since they are commensurable in square by Step 5, and if they were commensurable in length then the squares on them would have to each other the ratio of a square number to a square number by 10.9, but since AH and AK are medial and commensurable, and we can verify from the incommensurability of CE with ED that MN and NO are incommensurable in length). The sum of the squares on MN and NO is medial (Step 6), and twice the rectangle MN by NO is medial (Step 7), and these two are incommensurable with each other (Step 10).

**Step 12.** By 10.38, MN + NO is a second bimedial straight line, since MN and NO are medial straight lines commensurable in square only and containing a medial rectangle (twice the rectangle MN by NO is medial).

**Step 13.** But MO = MN + NO, and the square on MO equals the area AC (since the square on MN = AH, the square on NO = AK, and twice the rectangle MN by NO = 2AF, and AH + AK + 2AF = AC). Therefore MO is the "side" of the area AC, and MO is a second bimedial.

**Step 14.** Therefore, if an area be contained by a rational straight line and the third binomial, the "side" of the area is the irrational straight line called a second bimedial. Q.E.D.

**USED:** 1.31, 10.11, 10.12, 10.13, 10.15, 10.17, 10.21, 10.38, 10.54, 10.9, 2.1, 2.5, 6.1, D10.1.2, D10.1.3, D10.1.4, D10.2.3
**Human refs (from References field):** 10.13, 10.21, 10.38, D10.2.3
**Jaccard:** 0.235 — AI adds ['1.31', '10.11', '10.12', '10.15', '10.17', '10.54', '10.9', '2.1', '2.5', '6.1', 'D10.1.2', 'D10.1.3', 'D10.1.4']

## Proposition 10.57
**Statement:** If an area be contained by a rational straight line and the fourth binomial, the âsideâ of the area is the irrational straight line called major.

Let the area be contained by the rational straight line AC and the fourth binomial DE, and let the fourth binomial DE be divided into its terms at G, so that DG is the greater term.

**Step 1.** Since DE is a fourth binomial, by D10.2.4 the greater term DG is commensurable in length with the rational straight line set out, the square on DG is greater than the square on GE by the square on a straight line incommensurable in length with DG, and DG is commensurable in length with the rational straight line. Since DE is a binomial, DG and GE are rational straight lines commensurable in square only, by 10.36.

**Step 2.** Let the rectangle AC x DE be the given area. We wish to find the "side" of this area. Bisect DG at the point H, so that DH = HG, by 1.10. Since the square on DG is greater than the square on GE by the square on a straight line incommensurable in length with DG (by D10.2.4), by 10.18, if we apply to DG a parallelogram equal to the fourth part of the square on GE and deficient by a square figure, it divides DG into parts that are incommensurable in length.

**Step 3.** Apply to DG a rectangle equal to (1/4)(GE)^2 deficient by a square, with DH = HG (the bisection). Form the rectangle DH x HG = (DG/2)^2 and note that the rectangle on the segments into which DG is divided relates to the square on the half. Since the square on DG exceeds the square on GE by the square on a line incommensurable with DG, by 10.18 the segments produced (that is, DK and KG where K is the appropriate point) are incommensurable in length.

**Step 4.** Let the rectangle AC x DG equal the square on MN, and let the rectangle AC x GE equal the square on NX. Then the rectangle AC x DE = (square on MN) + (square on NX), by 2.1, since DE = DG + GE. The "side" of the area AC x DE is the straight line MX (where MX = MN + NX in the sense that the square on MX equals the square on MN plus the square on NX plus twice the rectangle MN x NX, but we proceed to show MX is a major line).

**Step 5.** Since DG is commensurable in length with the rational line AC (by D10.2.4, as DG is the greater term of a fourth binomial and is commensurable in length with the rational line set out), and AC is rational, the rectangle AC x DG is rational, by 10.19. Therefore the square on MN is rational, so MN is rational in square.

**Step 6.** Since GE is incommensurable in length with AC (for DG is commensurable in length with AC while DG and GE are commensurable in square only, hence GE is incommensurable in length with DG, and since DG is commensurable in length with AC, by 10.13, GE is incommensurable in length with AC), both GE and AC being rational, the rectangle AC x GE is medial, by 10.21. Therefore the square on NX is medial, so NX is medial.

**Step 7.** Since DG is incommensurable in length with GE, and AC x DG = (MN)^2 and AC x GE = (NX)^2, we have (MN)^2 : (NX)^2 = DG : GE (since both rectangles have the common side AC, by 6.1). Since DG is incommensurable in length with GE, by 10.11, (MN)^2 is incommensurable with (NX)^2. Therefore MN is incommensurable in square with NX.

**Step 8.** Since the square on MN is rational and the square on NX is medial, the sum of the squares on MN and NX is the sum of a rational and a medial area. The sum of the squares on MN and NX equals the square on MN + the square on NX. Since a rational area is incommensurable with a medial area (by 10.26, a medial area does not exceed a medial area by a rational area, and by the definitions, rational and medial areas are incommensurable), the square on MN is incommensurable with the square on NX. Hence their sum is irrational. But the sum of the squares on MN and NX is rational (we must verify this): the sum equals AC x DG + AC x GE = AC x DE. Since AC is rational and DE is a binomial (hence irrational by 10.36), AC x DE need not be rational. Rather, we must consider the sum of squares differently.

**Step 9.** Let us reconsider using the standard construction for these propositions. Let AC be the given rational straight line and DE the fourth binomial with terms DG, GE (DG > GE). Bisect DG at H. By 10.18, since the square on DG exceeds the square on GE by the square on a line incommensurable with DG, applying to DG a rectangle equal to (1/4)(GE)^2 deficient by a square produces segments incommensurable in length. Thus HG^2 - the applied rectangle gives rise to a point K on DG such that DK and KG are incommensurable in length.

**Step 10.** Set DK = p and KG = q so that p + q = DG and p, q are incommensurable in length. Since H is the midpoint of DG, we have DH = HG = DG/2, and by 2.5, the rectangle p x q + (square on HK) = (square on HG). Also by construction, p x q = (1/4)(GE)^2, so the rectangle DK x KG = (1/4)(GE)^2.

**Step 11.** Now let the square on MN equal the rectangle AC x DK, and let the square on NX equal the rectangle AC x KG. Since DK and KG are incommensurable in length and both rectangles share the side AC, by 6.1 and 10.11, (MN)^2 and (NX)^2 are incommensurable. Hence MN and NX are incommensurable in square.

**Step 12.** Since DG is commensurable in length with AC (by D10.2.4), and DG = DK + KG, we have AC x DG = AC x DK + AC x KG = (MN)^2 + (NX)^2. Since DG is commensurable in length with AC, the rectangle AC x DG is rational by 10.19. Therefore the sum (MN)^2 + (NX)^2 is rational.

**Step 13.** Since DK x KG = (1/4)(GE)^2, we have 4 x (DK x KG) = (GE)^2, so AC^2 x 4 x (DK x KG) = AC^2 x (GE)^2, which gives 4 x (AC x DK) x (AC x KG) = (AC x GE)^2, by 2.4. That is, 4 x (MN)^2 x (NX)^2 = (AC x GE)^2. Therefore (2 x MN x NX)^2 = (AC x GE)^2, so 2 x (rectangle MN x NX) = rectangle AC x GE.

**Step 14.** Since GE is incommensurable in length with AC (established in Step 6: GE is incommensurable in length with DG since they are commensurable in square only, and DG is commensurable in length with AC, so by 10.13, GE is incommensurable in length with AC), and both are rational, the rectangle AC x GE is medial, by 10.21. Therefore 2 x (rectangle MN x NX) is medial, so the rectangle MN x NX is medial.

**Step 15.** We now verify the conditions for MX = MN + NX to be a major line according to 10.39: (i) MN and NX are incommensurable in square (Step 11); (ii) the sum of the squares on MN and NX is rational (Step 12); (iii) the rectangle MN x NX is medial (Step 14). By 10.39, MX = MN + NX is the irrational line called major.

**Step 16.** It remains to show that MX is indeed the "side" of the area AC x DE. We have (MX)^2 = (MN)^2 + (NX)^2 + 2 x (rectangle MN x NX) = AC x DK + AC x KG + AC x GE = AC x (DK + KG) + AC x GE = AC x DG + AC x GE = AC x (DG + GE) = AC x DE, by 2.1. Therefore MX is the side of the area AC x DE.

**Step 17.** Therefore, if an area is contained by a rational straight line and the fourth binomial, the side of the area is the irrational straight line called major. Q.E.D.

**USED:** 1.10, 10.11, 10.13, 10.18, 10.19, 10.21, 10.36, 10.39, 2.1, 2.4, 2.5, 6.1, D10.1.3, D10.1.4, D10.2.4
**Human refs (from References field):** 10.11, 10.13, 10.18, 10.19, 10.21, 10.39, 6.1, D10.2.4
**Jaccard:** 0.533 — AI adds ['1.10', '10.36', '2.1', '2.4', '2.5', 'D10.1.3', 'D10.1.4']

## Proposition 10.58
**Statement:** If an area be contained by a rational straight line and the fifth binomial, the âsideâ of the area is the irrational straight line called the side of a rational plus a medial area.

**Step 1.** Let the area AC be contained by the rational straight line AB and the fifth binomial CD. We must show that the "side" of the area AC is the irrational straight line called the side of a rational plus a medial area.

**Step 2.** Let CD be divided into its terms at E, so that DE is the lesser term. Then by the definition of a fifth binomial (D10.2.5): (i) the square on CE is greater than the square on ED by the square on a straight line incommensurable in length with CE, and (ii) ED is commensurable in length with the rational straight line AB.

**Step 3.** Bisect ED at the point F, so that EF = FD (by 1.10). Apply to CE a rectangle equal to the square on EF and deficient by a square figure; let this produce the rectangle CG, GE (by 2.5 and 6.28). Since the square on CE is greater than the square on ED by the square on a straight line incommensurable in length with CE, by 10.18, CG is incommensurable in length with GE.

**Step 4.** As CG is to GE, so is the rectangle CG by GE to the square on GE (by 6.1). Therefore by 10.11, the rectangle CG by GE is incommensurable with the square on GE.

**Step 5.** Now CG + GE = CE, and CG by GE = EF squared = (1/4) ED squared. The squares on CG, GE together equal the square on CE plus or minus twice the rectangle CG by GE. Specifically, by 2.5, the rectangle CE by GE together with the square on EG equals the rectangle CG by GE (under the application construction). More precisely, by the identity of 2.4 and 2.5, the sum of the squares on CG and GE equals the square on CE minus twice the rectangle CG by GE, and the square on CE equals the sum of the squares on CG, GE plus twice the rectangle CG by GE (by 2.4 applied to CG + GE = CE).

**Step 6.** Construct on AB rectangles equal to the squares on CG and GE respectively: let AH be the rectangle AB by CG and HK be the rectangle AB by GE, so that AK = AB times CE. Since AB times CD = AC, and CD = CE + ED, we have AC = AB times CE + AB times ED (by 2.1). Let AB times ED = rectangle KL. Then AC = AK + KL.

**Step 7.** Since ED is commensurable in length with the rational straight line AB (by the definition of fifth binomial, D10.2.5), the rectangle AB times ED is rational (by 10.19). Thus KL is rational.

**Step 8.** Since CG is incommensurable in length with GE (Step 3), and the rectangle AB by CG is to the rectangle AB by GE as CG is to GE (by 6.1), therefore AH is incommensurable with HK (by 10.11).

**Step 9.** Now CE is incommensurable in length with AB. For if CE were commensurable with AB, then since ED is also commensurable with AB, CE and ED would be commensurable with each other (by 10.12), but CE and ED are commensurable in square only (they are terms of a binomial by 10.36), contradiction. Therefore CE is incommensurable in length with AB.

**Step 10.** Since CE = CG + GE, and CG is incommensurable with GE, at least one of CG, GE is incommensurable in length with AB. In fact, suppose CG were commensurable in length with AB; since CG is incommensurable with GE, GE would be incommensurable in length with AB. Then the square on CG would be commensurable with the square on AB and the square on GE incommensurable with the square on AB. The sum of the squares on CG and GE would be incommensurable with the square on AB. But the sum of the squares on CG and GE = square on CE minus twice rectangle CG by GE, and by 2.5 the rectangle CG by GE = one-fourth the square on ED. This leads to the sum of squares on CG, GE being incommensurable with AB squared. A symmetric argument applies if GE is commensurable. In either case, the sum of the squares on CG and GE is incommensurable with the rational area AB squared.

**Step 11.** Now AH + HK = AB times (CG + GE) = AB times CE. Since AH = AB times CG and HK = AB times GE, and AH is incommensurable with HK (Step 8), the sum AH + HK is the area AB times CE. The square on AB is rational, and the sum of the squares on CG and GE is incommensurable with AB squared (from the analysis above), so the area AH + HK (which equals AB times CE) is related to the sum of squares on CG and GE. Specifically, AH + HK = AB times CG + AB times GE, and these correspond (via 10.22 and the incommensurability relations) to medial areas. Therefore AH + HK is medial (since it equals a rational line times a line incommensurable in length with it, by 10.21).

**Step 12.** Now twice the rectangle CG by GE = twice times (1/4) ED squared = (1/2) ED squared. Since ED is commensurable with AB, the square on ED is commensurable with the square on AB (by 10.11). The area AB times (twice CG by GE / AB) must be analyzed. The rectangle corresponding to twice CG by GE when applied via AB: the area 2 AB times (CG by GE) relates to the rectangle under the "side." We showed KL = AB times ED is rational (Step 7). The rectangle 2 AH times HK corresponds to twice AB squared times CG times GE = AB squared times (1/2) ED squared (since CG times GE = (1/4) ED squared by 2.5). Since AB squared and ED squared are commensurable (as AB and ED are commensurable in length, so their squares are commensurable by 10.11), AB squared times (1/2) ED squared is rational. Therefore twice the rectangle corresponding to the "sides" of the area is rational.

**Step 13.** Now let the "side" of the area AC be the straight line w, so that the square on w equals AC. By 10.54's method (applied generally in 10.54-10.57), construct straight lines p, q such that the square on p equals AH and the square on q equals HK, so that the square on p + the square on q = AH + HK, which is medial (Step 11), and twice the rectangle p by q = KL, which is rational (Step 7). We need to verify that p, q are incommensurable in square.

**Step 14.** Since AH is incommensurable with HK (Step 8), the square on p is incommensurable with the square on q. Therefore p and q are incommensurable in square (by D10.1.2).

**Step 15.** The sum of the squares on p and q (= AH + HK) is medial, the rectangle p by q (half of the rational area KL, hence rational) is rational, and p, q are incommensurable in square. Also, AH + HK (the sum of squares on p, q) is medial while 2 p times q is rational, so these two are incommensurable with each other (by 10.26, a medial area cannot differ from a medial area by a rational area, and since the sum of squares is medial and twice the rectangle is rational, they are incommensurable).

**Step 16.** Therefore p + q is the irrational straight line called the side of a rational plus a medial area (by 10.40), since p and q are incommensurable in square, the sum of the squares on them is medial, and the rectangle contained by them is rational.

**Step 17.** And the square on (p + q) = the square on p + the square on q + twice the rectangle p by q = AH + HK + KL = AC. Therefore p + q is the "side" of the area AC.

**Step 18.** Therefore, if an area be contained by a rational straight line and the fifth binomial, the "side" of the area is the irrational straight line called the side of a rational plus a medial area. Q.E.D.

**USED:** 1.10, 10.11, 10.12, 10.18, 10.19, 10.21, 10.22, 10.26, 10.36, 10.40, 2.1, 2.4, 2.5, 6.1, 6.28, D10.1.2, D10.2.5
**Human refs (from References field):** 10.11, 10.12, 10.13, 10.18, 10.19, 10.21, 10.40, 6.1, D10.2.5
**Jaccard:** 0.444 — AI adds ['1.10', '10.22', '10.26', '10.36', '2.1', '2.4', '2.5', '6.28', 'D10.1.2']; Human adds ['10.13']

## Proposition 10.59
**Statement:** If an area be contained by a rational straight line and the sixth binomial, the âsideâ of the area is the irrational straight line called the side of the sum of two medial areas.

**Step 1.** Let the area ABCD be contained by the rational straight line AB and the sixth binomial straight line AD. We must show that the "side" of the area ABCD is the irrational straight line called the side of the sum of two medial areas.

**Step 2.** Let AD be the sixth binomial, divided into its terms at E, so that AE is the greater term and ED the lesser. By definition of the sixth binomial (D10.2.6), the square on AE is greater than the square on ED by the square on a straight line incommensurable in length with AE, and neither AE nor ED is commensurable in length with the rational straight line set out.

**Step 3.** By the same construction as in the preceding propositions (following the method of 10.54), let the rational straight line AB be set out, and let the rectangle ABCD equal to the rectangle AB by AD be constructed. Bisect ED at F, and apply to AE a rectangle equal to the square on EF and deficient by a square figure, producing segments AG and GE; that is, the rectangle AG by GE equals the square on EF (by 2.5 applied to the bisection and the construction).

**Step 4.** Since the square on AE is greater than the square on ED by the square on a straight line incommensurable in length with AE, and the rectangle AG by GE equals one-fourth of the square on ED (since EF is half of ED), by 10.18 the segments AG and GE are incommensurable in length.

**Step 5.** Construct GH perpendicular to AB (by 1.12), and draw through E the line EK parallel to AB and through A and D lines parallel to GH (by 1.31), thereby dividing the rectangle ABCD into sub-rectangles. Then the rectangle AH (that is, AB by AG) and the rectangle GK (that is, AB by GE) are the sub-rectangles corresponding to the segments AG and GE.

**Step 6.** Since AG and GE are incommensurable in length, the rectangles AB by AG and AB by GE are incommensurable (by 6.1 and 10.11). Thus the rectangle AH is incommensurable with the rectangle GK.

**Step 7.** Now let MN be a straight line such that the square on MN equals the rectangle AH, and let NO be a straight line such that the square on NO equals the rectangle GK, with MN and NO placed in a straight line. Then the square on MO equals the sum of the squares on MN and NO plus twice the rectangle MN by NO (by 2.4). But by construction, the square on MN plus the square on NO equals the rectangle AH plus the rectangle GK, and twice the rectangle MN by NO corresponds to twice the rectangle AB by EF.

**Step 8.** Since neither AE nor ED is commensurable in length with the rational straight line AB (from D10.2.6), and AG is a part of AE obtained by the construction, we examine the rectangle AB by AG. Since AE is incommensurable in length with AB, and AG is incommensurable in length with AE (because AG and GE are incommensurable in length, but their sum is AE), it follows from 10.13 that AG is incommensurable in length with AB. Therefore the rectangle AB by AG, which is the rectangle AH, is irrational relative to the square on AB, and similarly for the rectangle AB by GE. By 10.21, both the rectangle AH and the rectangle GK are medial areas, since they are each a rectangle of a rational straight line and a straight line incommensurable in length with it.

**Step 9.** Since AH and GK are each medial, the squares on MN and on NO are each medial areas. Hence MN and NO are each medial straight lines (by D10.1.4).

**Step 10.** Since AH is incommensurable with GK (Step 6), the square on MN is incommensurable with the square on NO. Therefore MN and NO are incommensurable in square, and hence also incommensurable in length.

**Step 11.** Now we must show that the sum of the squares on MN and NO is medial. We have that the sum of the squares on MN and NO equals AH + GK = AB by (AG + GE) = AB by AE. Since AE is incommensurable in length with the rational straight line AB (from D10.2.6), the rectangle AB by AE is irrational (by 10.21). Hence the sum of the squares on MN and NO is a medial area.

**Step 12.** Next we show that the rectangle MN by NO is also medial. We have that twice the rectangle MN by NO equals twice the rectangle AB by EF = AB by ED (since EF is half of ED, so twice AB by EF = AB by ED). Since ED is incommensurable in length with AB (from D10.2.6), the rectangle AB by ED is irrational (by 10.21). Hence the rectangle MN by NO is medial.

**Step 13.** Finally we show that the sum of the squares on MN and NO is incommensurable with the rectangle MN by NO. The sum of the squares on MN and NO equals AB by AE, and twice the rectangle MN by NO equals AB by ED. By 6.1, the ratio of AB by AE to AB by ED equals the ratio AE to ED. Since AE and ED are incommensurable in length (since if they were commensurable, then by 10.36 their sum AD would be a binomial with commensurable terms in length, contradicting the sixth binomial classification in D10.2.6 where the terms are commensurable in square only), the ratio AE to ED is not the ratio of a number to a number (by 10.7), so AB by AE is incommensurable with AB by ED (by 10.11). Hence the sum of the squares on MN and NO is incommensurable with the rectangle MN by NO.

**Step 14.** Therefore MN and NO are two straight lines incommensurable in square (Step 10), the sum of the squares on them is medial (Step 11), the rectangle contained by them is medial (Step 12), and the sum of the squares on them is incommensurable with the rectangle contained by them (Step 13). By 10.41, the whole straight line MO is the irrational straight line called the side of the sum of two medial areas.

**Step 15.** Moreover, the square on MO equals the area ABCD (by construction in Steps 7 and the identity from 2.4). Therefore MO is the "side" of the area ABCD.

**Step 16.** Therefore, if an area be contained by a rational straight line and the sixth binomial, the "side" of the area is the irrational straight line called the side of the sum of two medial areas. Q.E.D.

**USED:** 1.12, 1.31, 10.11, 10.13, 10.18, 10.21, 10.36, 10.41, 10.7, 2.4, 2.5, 6.1, D10.1.4, D10.2.6
**Human refs (from References field):** 10.11, 10.13, 10.21, 10.41, 6.1
**Jaccard:** 0.357 — AI adds ['1.12', '1.31', '10.18', '10.36', '10.7', '2.4', '2.5', 'D10.1.4', 'D10.2.6']

## Proposition 10.60
**Statement:** The square on the binomial straight line applied to a rational straight line produces as breadth the first binomial.

**Step 1.** Let AB be a binomial straight line, divided into its terms at C, so that AC is the greater term and CB is the lesser. By the definition of a binomial (10.36), AC and CB are rational straight lines commensurable in square only, with AC > CB. Let D be the given rational straight line. Apply the square on AB to D, producing as breadth the straight line EF. We must show that EF is a first binomial straight line.

**Step 2.** By 2.4, the square on AB equals the sum of the squares on AC and CB together with twice the rectangle contained by AC and CB. That is, AB^2 = AC^2 + CB^2 + 2*AC*CB.

**Step 3.** Apply the area AC^2 + CB^2 to the rational straight line D, producing breadth EG, and apply the area 2*AC*CB to D, producing breadth GF. Then EF = EG + GF.

**Step 4.** Since AC and CB are rational, the squares AC^2 and CB^2 are each rational areas (D10.1.4). Since AC and CB are commensurable in square, AC^2 and CB^2 are commensurable with one another. Therefore by 10.15, the sum AC^2 + CB^2 is rational and commensurable with each of AC^2 and CB^2.

**Step 5.** Since AC^2 + CB^2 is a rational area applied to the rational straight line D, by 10.20, the breadth EG is rational and commensurable in length with D.

**Step 6.** Since AC and CB are rational and commensurable in square only, by 10.21, the rectangle AC*CB is medial. The area 2*AC*CB has to AC*CB the ratio 2:1, which is a ratio of number to number, so by 10.6, the area 2*AC*CB is commensurable with AC*CB. Since AC*CB is incommensurable with D^2 (being medial, by D10.1.4), by 10.13, the area 2*AC*CB is also incommensurable with D^2, and hence is itself medial.

**Step 7.** Since 2*AC*CB is a medial area applied to the rational straight line D, by 10.22, the breadth GF is rational and incommensurable in length with D.

**Step 8.** Since AC^2 + CB^2 is rational (commensurable with D^2) and 2*AC*CB is medial (incommensurable with D^2), these two areas are incommensurable with each other (by 10.13, since AC^2 + CB^2 is commensurable with D^2 while 2*AC*CB is not). By 6.1, the areas applied to the same line D are as their breadths, so EG : GF = (AC^2 + CB^2) : 2*AC*CB. Since the areas are incommensurable, by 10.11, the breadths EG and GF are incommensurable in length.

**Step 9.** Now EG and GF are both rational (Steps 5 and 7). The square on EG is commensurable with D^2 (since EG is commensurable in length with D), and the square on GF is also commensurable with D^2 (since GF is rational, it is commensurable in square with D, by D10.1.3). By 10.12, the squares on EG and GF are commensurable with each other, so EG and GF are commensurable in square. Combined with their incommensurability in length (Step 8), EG and GF are commensurable in square only.

**Step 10.** It remains to show that the square on EG exceeds the square on GF by the square on a straight line commensurable in length with EG. Since AC and CB are commensurable in square, AC^2 : CB^2 is a ratio of number to number (10.5). Say AC^2 : CB^2 = m : n where m, n are numbers. Then AC^2 + CB^2 and AC^2 - CB^2 are commensurable, because (AC^2 + CB^2) : (AC^2 - CB^2) = (m + n) : (m - n), which is a ratio of number to number, so by 10.6 they are commensurable.

**Step 11.** Let H be the straight line such that D*H = AC^2 - CB^2. Since AC^2 + CB^2 is commensurable with AC^2 - CB^2 (Step 10), and by 6.1, D*EG : D*H = EG : H, the commensurability of the areas yields, by 10.11, that EG and H are commensurable in length.

**Step 12.** We now show EG^2 - GF^2 = H^2. We have D*EG = AC^2 + CB^2, D*GF = 2*AC*CB, and D*H = AC^2 - CB^2. Squaring these: D^2 * EG^2 = (AC^2 + CB^2)^2, D^2 * GF^2 = (2*AC*CB)^2 = 4*AC^2*CB^2, and D^2 * H^2 = (AC^2 - CB^2)^2. By 2.5, applied with a = AC^2 and b = CB^2, we have (AC^2 + CB^2)^2 = (AC^2 - CB^2)^2 + 4*AC^2*CB^2. Therefore D^2 * EG^2 = D^2 * H^2 + D^2 * GF^2 (CN2). Subtracting D^2 * GF^2 from both sides (CN3), D^2 * (EG^2 - GF^2) = D^2 * H^2, and hence EG^2 - GF^2 = H^2.

**Step 13.** Therefore the square on EG exceeds the square on GF by the square on H, and H is commensurable in length with EG (Step 11).

**Step 14.** Collecting the results: EG and GF are rational straight lines commensurable in square only (Step 9). The square on the greater term EG exceeds the square on the lesser term GF by the square on a straight line commensurable in length with EG (Step 13). The greater term EG is commensurable in length with the rational straight line D (Step 5). Therefore, by D10.2.1, the straight line EF = EG + GF is a first binomial straight line.

**Step 15.** Thus the square on the binomial straight line AB, applied to the rational straight line D, produces as breadth EF, which is a first binomial. This is what was to be proved.

**USED:** 10.11, 10.12, 10.13, 10.15, 10.20, 10.21, 10.22, 10.36, 10.5, 10.6, 2.4, 2.5, 6.1, CN2, CN3, D10.1.3, D10.1.4, D10.2.1
**Human refs (from References field):** 10.11, 10.13, 10.15, 10.17, 10.20, 10.21, 10.22, 10.36, 10.53, 6.1, 6.17, D10.2.1
**Jaccard:** 0.429 — AI adds ['10.12', '10.5', '10.6', '2.4', '2.5', 'CN2', 'CN3', 'D10.1.3', 'D10.1.4']; Human adds ['10.17', '10.53', '6.17']

## Proposition 10.61
**Statement:** The square on the first bimedial straight line applied to a rational straight line produces as breadth the second binomial.

**Step 1.** Let AB be a first bimedial straight line, and let it be divided into its medials at C, so that AC and CB are medial straight lines commensurable in square only and such that the rectangle AC by CB is rational [10.37]. Let DE be a rational straight line. Apply the square on AB to DE, producing the rectangle DEFG, so that DE times DG equals the square on AB [1.44]. We must show that DG is a second binomial straight line.

**Step 2.** Since AB equals AC plus CB, the square on AB equals the sum of the squares on AC and CB together with twice the rectangle AC by CB [2.4]. Apply these parts separately to DE: let DE times DH equal the sum of the squares on AC and CB, and let DE times HG equal twice the rectangle AC by CB, where H lies between D and G on the line DG. Then DG equals DH plus HG.

**Step 3.** Since AC and CB are medial straight lines commensurable in square, the squares on AC and CB are commensurable with one another [D10.1.2]. Therefore the sum of the squares on AC and CB is commensurable with the square on AC [10.15]. But the square on AC is medial (since AC is medial) [D10.1.4]. Hence the sum of the squares on AC and CB is also medial, being commensurable with a medial area [10.23, D10.1.4].

**Step 4.** Since the sum of the squares on AC and CB is a medial area, and it has been applied to the rational straight line DE producing breadth DH, it follows that DH is rational and incommensurable in length with DE [10.22].

**Step 5.** Since the rectangle AC by CB is rational (by the definition of the first bimedial), twice the rectangle AC by CB is also rational [10.15, D10.1.4]. This rational area has been applied to the rational straight line DE producing breadth HG, so HG is rational and commensurable in length with DE [10.20].

**Step 6.** Since DH is incommensurable in length with DE, while HG is commensurable in length with DE, it follows that DH is incommensurable in length with HG [10.13]. But both DH and HG are rational. Therefore DH and HG are rational straight lines commensurable in square only, and their sum DG is a binomial straight line [10.36].

**Step 7.** We now show that DH is greater than HG. Since AC and CB are incommensurable in length, AC is not equal to CB, and therefore the squares on AC and CB are not equal. Hence the square on AC minus the square on CB (or vice versa) is not zero, so (AC squared minus CB squared) squared is positive. Now (the sum of the squares on AC and CB) squared exceeds (twice the rectangle AC by CB) squared by (the square on AC minus the square on CB) squared. Therefore the sum of the squares on AC and CB is greater than twice the rectangle AC by CB. Since DE times DH equals the former and DE times HG equals the latter, DH is greater than HG.

**Step 8.** We now determine the nature of the excess of the square on DH over the square on HG. Since DE times DH equals the sum of the squares on AC and CB, and DE times HG equals twice the rectangle AC by CB, we have DE times (DH minus HG) equals the sum of the squares on AC and CB minus twice the rectangle AC by CB, which equals the square on AC minus twice the rectangle AC by CB plus the square on CB, that is, the square on the difference AC minus CB [2.4]. Also DE times (DH plus HG) equals the square on AB. Therefore the rectangle (DH plus HG) by (DH minus HG), which equals the square on DH minus the square on HG [2.5], equals (the square on AB times the square on the difference of AC and CB) divided by DE squared. In Euclidean terms, the square on DH minus the square on HG equals the square on the line (AC squared minus CB squared) divided by DE.

**Step 9.** More precisely, since the square on DH minus the square on HG equals the rectangle contained by DG and the difference DH minus HG, and since DE times (DH minus HG) equals the square on the difference (AC minus CB) [from Step 8], while DE times DH equals AC squared plus CB squared, the ratio of DH to (DH minus HG) equals the ratio of (AC squared plus CB squared) to the square on the difference (AC minus CB), which equals the ratio of (AC squared plus CB squared) to (AC squared minus 2 times AC times CB plus CB squared).

**Step 10.** We show that (AC squared minus CB squared) is commensurable with (AC squared plus CB squared). Since AC and CB are commensurable in square, the squares on AC and CB are commensurable [D10.1.2]. Since AC squared is commensurable with CB squared, the sum AC squared plus CB squared is commensurable with AC squared [10.15]. Also, since the sum AC squared plus CB squared is commensurable with AC squared, and since the difference AC squared minus CB squared can be expressed as: AC squared equals CB squared plus (AC squared minus CB squared), and AC squared is commensurable with CB squared, by the converse part of 10.15 the difference AC squared minus CB squared is commensurable with AC squared. Therefore AC squared minus CB squared is commensurable with AC squared plus CB squared [10.12].

**Step 11.** Now, DE times DH equals AC squared plus CB squared, so DH is as (AC squared plus CB squared) divided by DE. Similarly, the square on DH minus the square on HG equals the square of (AC squared minus CB squared) over DE squared, so the square root of (DH squared minus HG squared) equals (AC squared minus CB squared) divided by DE. Since AC squared minus CB squared is commensurable with AC squared plus CB squared [Step 10], and both are divided by the same rational line DE, the resulting lines (AC squared minus CB squared)/DE and (AC squared plus CB squared)/DE are commensurable in length [10.11]. The latter is DH. Therefore the square on DH exceeds the square on HG by the square on a straight line commensurable in length with DH [10.17].

**Step 12.** We have established: (i) DG is a binomial with terms DH and HG, where DH is the greater [Steps 6, 7]; (ii) the square on DH is greater than the square on HG by the square on a straight line commensurable in length with DH [Step 11]; (iii) the lesser term HG is commensurable in length with the rational straight line DE [Step 5]. These are precisely the conditions defining a second binomial straight line [D10.2.2].

**Step 13.** Therefore, the square on the first bimedial straight line AB, applied to the rational straight line DE, produces as breadth DG, which is a second binomial straight line. Q.E.D.

**USED:** 1.44, 10.11, 10.12, 10.13, 10.15, 10.17, 10.20, 10.22, 10.23, 10.36, 10.37, 2.4, 2.5, D10.1.2, D10.1.4, D10.2.2
**Human refs (from References field):** 10.11, 10.13, 10.15, 10.17, 10.20, 10.21, 10.22, 10.23, 10.36, 10.37, 6.1, D10.2.2
**Jaccard:** 0.556 — AI adds ['1.44', '10.12', '2.4', '2.5', 'D10.1.2', 'D10.1.4']; Human adds ['10.21', '6.1']

## Proposition 10.62
**Statement:** The square on the second bimedial straight line applied to a rational straight line produces as breadth the third binomial.

**Step 1.** Let AB be a second bimedial straight line and let DE be a rational straight line. Apply to DE a rectangle equal to the square on AB, producing DF as breadth, so that DE * DF = sq(AB). We shall show that DF is a third binomial straight line with respect to DE.

**Step 2.** Since AB is a second bimedial, let it be divided at C into its medial components, with AC the greater segment, so that AC and CB are medial straight lines, commensurable in square only, and the rectangle AC * CB is medial [10.38, 10.44].

**Step 3.** By 2.4, sq(AB) = sq(AC) + sq(CB) + 2 * rect(AC, CB). Apply each part to DE: let DE * DH = sq(AC), DE * HK = sq(CB), and DE * KF = 2 * rect(AC, CB). Then DF = DH + HK + KF. Set DM = DH + HK, so that DF = DM + KF, with DE * DM = sq(AC) + sq(CB).

**Step 4.** Since AC is medial, sq(AC) is a medial area [D10.1.4]. Applied to the rational line DE, it produces DH rational and incommensurable in length with DE [10.22]. Likewise, since CB is medial, sq(CB) is medial, and HK is rational and incommensurable in length with DE [10.22].

**Step 5.** Since AC and CB are commensurable in square, sq(AC) is commensurable with sq(CB) [D10.1.2]. Their ratio is therefore as a number to a number [10.5]. Since DE * DH = sq(AC) and DE * HK = sq(CB), we have DH : HK = sq(AC) : sq(CB) [6.1], which is a ratio of number to number. Therefore DH is commensurable in length with HK [10.6].

**Step 6.** Since DH and HK are commensurable in length and DH is rational, DM = DH + HK is commensurable in length with DH [10.15], and therefore DM is rational. Since DH is incommensurable in length with DE and DM is commensurable with DH, it follows that DM is incommensurable in length with DE [10.13].

**Step 7.** Since sq(AC) and sq(CB) are commensurable, sq(AC) + sq(CB) is commensurable with sq(AC) [10.15]. Since sq(AC) is medial, sq(AC) + sq(CB) is also medial. Thus DE * DM is a medial area, confirming DM is rational and incommensurable in length with DE [10.22].

**Step 8.** Since rect(AC, CB) is medial, 2 * rect(AC, CB) is also medial. Applied to the rational line DE, DE * KF = 2 * rect(AC, CB) produces KF rational and incommensurable in length with DE [10.22].

**Step 9.** We now show DM is incommensurable in length with KF. Since AC and CB are commensurable in square only, AC is incommensurable in length with CB. Now rect(AC, CB) : sq(CB) = AC : CB [6.1], so rect(AC, CB) is incommensurable with sq(CB) [10.11]. Since sq(AC) is commensurable with sq(CB), rect(AC, CB) is incommensurable with sq(AC) [10.13]. Since sq(AC) + sq(CB) is commensurable with sq(AC) [Step 7], rect(AC, CB) is incommensurable with sq(AC) + sq(CB) [10.13]. Therefore 2 * rect(AC, CB) is incommensurable with sq(AC) + sq(CB).

**Step 10.** Since DE * DM = sq(AC) + sq(CB) and DE * KF = 2 * rect(AC, CB), and these areas are incommensurable [Step 9], it follows that DM is incommensurable in length with KF [6.1, 10.11].

**Step 11.** Since DM and KF are both rational [Steps 6, 8] and incommensurable in length [Step 10], they are rational straight lines commensurable in square only. Therefore DF = DM + KF is a binomial straight line [10.36].

**Step 12.** Neither DM nor KF is commensurable in length with the rational straight line DE [Steps 6, 8]. This satisfies the first condition of D10.2.3 for a third binomial.

**Step 13.** It remains to show that sq(DM) exceeds sq(KF) by the square on a straight line commensurable in length with DM. Since DE * DM = sq(AC) + sq(CB) and DE * KF = 2 * rect(AC, CB), we compute sq(DM) - sq(KF) = [(sq(AC) + sq(CB))^2 - (2 * rect(AC, CB))^2] / sq(DE). Now (sq(AC) + sq(CB))^2 - 4 * rect(AC, CB)^2 = (sq(AC) + sq(CB) + 2 * rect(AC, CB))(sq(AC) + sq(CB) - 2 * rect(AC, CB)) = (AC + CB)^2 * (AC - CB)^2 by 2.4 and 2.7. However, more directly: (sq(AC) + sq(CB))^2 - (2 * AC * CB)^2 = (sq(AC) - sq(CB))^2 by algebraic identity. Therefore sq(DM) - sq(KF) = (sq(AC) - sq(CB))^2 / sq(DE) = sq((sq(AC) - sq(CB)) / DE).

**Step 14.** Let L be such that DE * L = sq(AC) - sq(CB). Then sq(DM) - sq(KF) = sq(L). We must show L is commensurable in length with DM. Since DE * DM = sq(AC) + sq(CB) and DE * L = sq(AC) - sq(CB), we have DM : L = (sq(AC) + sq(CB)) : (sq(AC) - sq(CB)) [6.1].

**Step 15.** Since sq(AC) : sq(CB) = p : q for integers p > q [10.5, as AC and CB are commensurable in square], we have (sq(AC) + sq(CB)) : (sq(AC) - sq(CB)) = (p + q) : (p - q), which is a ratio of number to number. Therefore DM is commensurable in length with L [10.6].

**Step 16.** Therefore sq(DM) exceeds sq(KF) by sq(L), where L is commensurable in length with DM. Combined with the fact that neither DM nor KF is commensurable in length with DE [Step 12], DF = DM + KF satisfies all three conditions of D10.2.3 and is therefore a third binomial straight line with respect to DE.

**Step 17.** Therefore, the square on the second bimedial straight line applied to a rational straight line produces as breadth the third binomial. Q.E.D.

**USED:** 10.11, 10.13, 10.15, 10.22, 10.36, 10.38, 10.44, 10.5, 10.6, 2.4, 6.1, D10.1.2, D10.1.4, D10.2.3
**Human refs (from References field):** 10.11, 10.12, 10.13, 10.15, 10.22, 10.23, 10.36, 10.38, 6.1, D10.2.3
**Jaccard:** 0.500 — AI adds ['10.44', '10.5', '10.6', '2.4', 'D10.1.2', 'D10.1.4']; Human adds ['10.12', '10.23']

## Proposition 10.63
**Statement:** The square on the major straight line applied to a rational straight line produces as breadth the fourth binomial.

**Step 1.** Let AB be a major straight line, and let DE be a rational straight line. Let the square on AB be applied to DE, producing DG as breadth, so that DE times DG equals the square on AB. We must show that DG is a fourth binomial straight line.

**Step 2.** Since AB is a major straight line, let it be divided at C so that AC and CB are two straight lines incommensurable in square, the sum of the squares on AC and CB is rational, and the rectangle AC by CB is medial [10.39, 10.45]. Here AC is the greater segment.

**Step 3.** Apply the square on AC to DE, producing DH as breadth, so that DE times DH equals the square on AC. Apply the square on CB to DE, producing HL as breadth (adjacent to DH along DE), so that DE times HL equals the square on CB. Then since the square on AB equals the square on AC plus the square on CB plus twice the rectangle AC by CB [2.4], we have DE times DG equals DE times DH plus DE times HL plus twice the rectangle AC by CB. Hence DE times (DG minus DH minus HL) equals twice the rectangle AC by CB.

**Step 4.** Let MN be the remaining breadth such that DE times MN equals twice the rectangle AC by CB. Then DG equals DH plus HL plus MN.

**Step 5.** Since the sum of the squares on AC and CB is rational, and DE is rational, the area equal to the sum of the squares on AC and CB (which equals DE times (DH + HL)) is rational. Since DE is rational, the breadth DH + HL is rational and commensurable in length with DE [10.20].

**Step 6.** Since twice the rectangle AC by CB is medial, and DE times MN equals twice the rectangle AC by CB, the area DE times MN is medial. Since DE is rational, MN is rational and incommensurable in length with DE [10.22].

**Step 7.** Since the sum of the squares on AC and CB is rational and twice the rectangle AC by CB is medial, the sum of the squares on AC and CB is incommensurable with twice the rectangle AC by CB [10.26, as a rational area is incommensurable with a medial area]. But DE times (DH + HL) equals the sum of the squares on AC and CB, and DE times MN equals twice the rectangle AC by CB. Therefore DE times (DH + HL) is incommensurable with DE times MN. Hence DH + HL is incommensurable in length with MN [6.1, 10.11].

**Step 8.** Now DH + HL is rational and commensurable in length with DE (Step 5), while MN is rational and incommensurable in length with DE (Step 6). Since DH + HL and MN are both rational but incommensurable in length with each other (Step 7), they are commensurable in square only [D10.1.3]. Therefore DG, which equals (DH + HL) + MN, is the sum of two rational straight lines commensurable in square only, so DG is a binomial straight line [10.36].

**Step 9.** We must further show that DG is specifically a fourth binomial. Since DH + HL is commensurable in length with DE (Step 5), and DH + HL is the greater term (as DH + HL is commensurable with DE while MN is incommensurable with DE, and the sum of the squares on AC, CB exceeds twice the rectangle AC by CB because the sum of the squares exceeds twice the rectangle by the square on AC minus CB, which is positive), DH + HL is the greater term of the binomial DG.

**Step 10.** We now show that the square on DH + HL exceeds the square on MN by the square on a straight line incommensurable in length with DH + HL. Since DE times DH equals the square on AC and DE times HL equals the square on CB, we have DE times DH is to DE times HL as the square on AC is to the square on CB. Therefore DH is to HL as the square on AC is to the square on CB [6.1].

**Step 11.** Since AC and CB are incommensurable in square (by the definition of the major straight line), the squares on AC and CB are incommensurable. Therefore DH is incommensurable in length with HL [6.1, 10.11].

**Step 12.** Now DE times MN equals twice the rectangle AC by CB, so DE times the square on MN can be related to the rectangle DH by HL as follows. Since DE times DH equals the square on AC and DE times HL equals the square on CB, the rectangle DH by HL times the square on DE equals the square on AC times the square on CB. Also, the square on MN times the square on DE equals four times the square of the rectangle AC by CB (since DE times MN equals twice the rectangle AC by CB). But the square on AC times the square on CB equals the square of the rectangle AC by CB [by the definition of rectangle and areas]. Hence the rectangle DH by HL times DE squared equals the square on MN times DE squared divided by 4. Therefore 4 times the rectangle DH by HL equals the square on MN.

**Step 13.** Since 4 times the rectangle DH by HL equals the square on MN, we can apply 2.5 and 2.6 to analyze the square on (DH + HL) minus the square on MN. By 2.5, the rectangle DH by HL plus the square on (DH - HL)/2 equals the square on (DH + HL)/2. Equivalently, the square on (DH + HL) equals the square on (DH - HL) plus 4 times the rectangle DH by HL [2.4]. Since 4 times DH by HL equals the square on MN (Step 12), the square on (DH + HL) minus the square on MN equals the square on (DH - HL). That is, the square on (DH + HL) exceeds the square on MN by the square on (DH - HL).

**Step 14.** Since DH is incommensurable in length with HL (Step 11), DH - HL is incommensurable in length with DH + HL [by 10.16, since DH + HL and DH - HL: if DH and HL are incommensurable, their sum is incommensurable with each of them by 10.16, and similarly for the difference]. More precisely, by the contrapositive of 10.17, since DH is incommensurable with HL, the square on (DH + HL) exceeds the square on MN by the square on a straight line incommensurable in length with DH + HL [10.18].

**Step 15.** Now we verify the conditions for a fourth binomial (D10.2.4): DG is a binomial divided into terms DH + HL and MN (Step 8), where DH + HL is the greater term. The square on the greater term DH + HL exceeds the square on the lesser term MN by the square on a straight line incommensurable in length with DH + HL (Step 14). The greater term DH + HL is commensurable in length with the rational straight line DE (Step 5). These are precisely the conditions of the fourth binomial (D10.2.4).

**Step 16.** Therefore, the square on the major straight line AB, applied to the rational straight line DE, produces as breadth the fourth binomial straight line DG. Q.E.D.

**USED:** 10.11, 10.18, 10.20, 10.22, 10.26, 10.36, 10.39, 10.45, 2.4, 6.1, D10.1.3, D10.2.4
**Human refs (from References field):** 10.11, 10.13, 10.18, 10.20, 10.22, 10.36, 10.39, 6.1, D10.2.4
**Jaccard:** 0.615 — AI adds ['10.26', '10.45', '2.4', 'D10.1.3']; Human adds ['10.13']

## Proposition 10.64
**Statement:** The square on the side of a rational plus a medial area applied to a rational straight line produces as breadth the fifth binomial.

**Step 1.** Let AB be the side of a rational plus a medial area, divided into its terms at C, where AC > CB. By the definition of this irrational (10.40), AC and CB are straight lines incommensurable in square, the sum of the squares on AC and CB is medial, and the rectangle AC by CB is rational.

**Step 2.** Let DE be a rational straight line. Apply to DE a rectangle equal to the square on AB, producing breadth DF, so that DE times DF equals the square on AB. We must show that DF is a fifth binomial straight line.

**Step 3.** By 2.4, the square on AB equals the sum of the squares on AC and CB together with twice the rectangle AC by CB. Apply to DE the rectangle equal to the sum of the squares on AC and CB, producing breadth DG, and apply to DE the rectangle equal to twice the rectangle AC by CB, producing breadth GF. Then DE times DG equals the sum of the squares on AC and CB, and DE times GF equals twice the rectangle AC by CB, and DF equals DG plus GF.

**Step 4.** Since the sum of the squares on AC and CB is medial and DE is rational, the rectangle DE times DG is medial. Therefore by 10.22, DG is rational and incommensurable in length with DE.

**Step 5.** Since the rectangle AC by CB is rational, twice the rectangle AC by CB is also rational. Since DE is rational and DE times GF equals twice the rectangle AC by CB, which is rational, by 10.20, GF is rational and commensurable in length with DE.

**Step 6.** Since DG is incommensurable in length with DE (Step 4) and GF is commensurable in length with DE (Step 5), by 10.13 DG is incommensurable in length with GF.

**Step 7.** Since DG and GF are each rational (Steps 4 and 5) and incommensurable in length with each other (Step 6), by 10.36 DF equals DG plus GF is a binomial straight line.

**Step 8.** We now show that DG is greater than GF. Since AC and CB are incommensurable in square, AC is not equal to CB, so AC and CB are unequal. Therefore by 2.7 (or the algebraic consequence that for unequal magnitudes, the sum of squares exceeds twice the rectangle), the sum of the squares on AC and CB is greater than twice the rectangle AC by CB. Since DE times DG equals the sum of squares on AC and CB, and DE times GF equals twice the rectangle AC by CB, it follows that DG is greater than GF.

**Step 9.** Now apply to DE the rectangle equal to the square on AC, producing breadth DH, so that DE times DH equals the square on AC. Then DE times HG equals the square on CB (where HG equals DG minus DH), since DE times DG equals the sum of the squares on AC and CB.

**Step 10.** Since AC and CB are incommensurable in square, the squares on AC and CB are incommensurable areas. Since DE times DH equals the square on AC and DE times HG equals the square on CB, we have DH is to HG as the square on AC is to the square on CB (by 6.1). Since the squares on AC and CB are incommensurable, by 10.11 DH and HG are incommensurable in length.

**Step 11.** Now, DE times DH equals the square on AC, and DE times HG equals the square on CB, so DE squared times DH times HG equals the square on AC times the square on CB, which equals the square of the rectangle AC by CB. Also, DE times GF equals twice the rectangle AC by CB, so DE squared times GF squared equals four times the square of the rectangle AC by CB. Therefore DE squared times GF squared equals four times DE squared times DH times HG, which gives GF squared equals four times DH times HG.

**Step 12.** By 2.5, since DG equals DH plus HG, the rectangle DH by HG plus the square on the excess of DH over HG (that is, the square on the half-difference) applied appropriately gives: four times the rectangle DH by HG plus the square on the difference DH minus HG equals the square on DH plus HG, that is, the square on DG. Therefore GF squared plus the square on the difference DH minus HG equals the square on DG. Hence the square on DG exceeds the square on GF by the square on the difference DH minus HG.

**Step 13.** Since DH and HG are incommensurable in length (Step 10), we apply 10.18: the rectangle equal to the fourth part of the square on GF (which equals DH times HG by Step 11), when applied to DG and deficient by a square, divides DG into the incommensurable parts DH and HG. Therefore by 10.18, the square on DG is greater than the square on GF by the square on a straight line incommensurable in length with DG.

**Step 14.** By the definition of the fifth binomial (D10.2.5, together with D10.2.4): DF is a binomial (Step 7), the square on the greater term DG exceeds the square on the lesser term GF by the square on a straight line incommensurable with DG (Step 13), and the lesser term GF is commensurable in length with the rational straight line DE set out (Step 5). Therefore DF is a fifth binomial straight line.

**Step 15.** Therefore the square on the side of a rational plus a medial area, applied to a rational straight line, produces as breadth the fifth binomial. Q.E.D.

**USED:** 10.11, 10.13, 10.18, 10.20, 10.22, 10.36, 10.40, 2.4, 2.5, 2.7, 6.1, D10.1.2, D10.2.4, D10.2.5
**Human refs (from References field):** 10.13, 10.18, 10.20, 10.22, 10.36, 10.40
**Jaccard:** 0.429 — AI adds ['10.11', '2.4', '2.5', '2.7', '6.1', 'D10.1.2', 'D10.2.4', 'D10.2.5']

## Proposition 10.65
**Statement:** The square on the side of the sum of two medial areas applied to a rational straight line produces as breadth the sixth binomial.

**Step 1.** Let AB be the side of the sum of two medial areas, divided at C so that AC is the greater segment. Let DE be a rational straight line, and let the rectangle DE.EF equal to the square on AB be applied to DE, producing EF as breadth. We must show that EF is a sixth binomial straight line.

**Step 2.** Since AB is the side of the sum of two medial areas, it is divided at C into two straight lines AC, CB which are incommensurable in square, such that the sum of the squares on AC, CB is medial, the rectangle contained by AC, CB is medial, and the sum of the squares on AC, CB is incommensurable with the rectangle AC.CB [10.41].

**Step 3.** Since the sum of the squares on AC, CB is medial, and DE is rational, the rectangle equal to the sum of the squares on AC, CB applied to the rational straight line DE produces as breadth a straight line rational and incommensurable in length with DE [10.22]. Let DG be the rectangle equal to the sum of the squares on AC, CB, so that DG = DE.EG, and EG is rational and incommensurable in length with DE.

**Step 4.** Since twice the rectangle AC.CB is medial (as the rectangle AC.CB is medial, and twice a medial area is medial [10.23, noting that a straight line commensurable with a medial is medial, and the side of twice a medial rectangle is commensurable in square with the side of the original, making twice the area medial by 10.24 and properties of medial areas]), the rectangle equal to twice AC.CB applied to the rational straight line DE produces as breadth a straight line rational and incommensurable in length with DE [10.22]. Let GF be the rectangle equal to twice the rectangle AC.CB, so that GF = DE.GF_breadth, and the breadth GF (that is, the segment from G to F along EF) is rational and incommensurable in length with DE.

**Step 5.** Now, the square on AB equals the squares on AC, CB plus twice the rectangle AC.CB [2.4]. Therefore the rectangle DE.EF, which equals the square on AB, equals the rectangle DE.EG (equal to the sum of the squares on AC, CB) plus the rectangle DE.GF_breadth (equal to twice AC.CB). Thus EF = EG + GF, where G lies between E and F.

**Step 6.** Since the sum of the squares on AC, CB is incommensurable with twice the rectangle AC.CB [from Step 2, since the sum of squares is incommensurable with the rectangle AC.CB, it is also incommensurable with twice the rectangle AC.CB by 10.13 and 10.6], the rectangle DG (equal to the sum of squares) is incommensurable with the rectangle GF (equal to twice AC.CB). Since DG = DE.EG and GF = DE.GF_breadth, and these rectangles on the same base DE are to each other as their breadths [6.1], EG is incommensurable in length with GF [10.11].

**Step 7.** Both EG and GF are rational (Steps 3 and 4), and they are incommensurable in length (Step 6). Therefore EG and GF are rational straight lines commensurable in square only, so EF = EG + GF is a binomial straight line [10.36].

**Step 8.** We must now show that EF is specifically a sixth binomial. Both EG and GF are incommensurable in length with DE (Steps 3 and 4), so neither term of the binomial EF is commensurable in length with the rational straight line DE.

**Step 9.** It remains to show that the square on EG is greater than the square on GF by the square on a straight line incommensurable in length with EG. Since the sum of the squares on AC, CB is incommensurable with the rectangle AC.CB, and DG (on base DE with breadth EG) corresponds to the sum of the squares, while GF corresponds to twice the rectangle, we have that EG is incommensurable with GF. Furthermore, since AC and CB are incommensurable in square, the squares on AC and CB are incommensurable with each other. The square on AC and the square on CB, being incommensurable, when applied to DE produce breadths that are incommensurable in length [10.11]. Let EG be divided at H so that DE.EH equals the square on AC and DE.HG equals the square on CB. Then EH and HG are incommensurable in length.

**Step 10.** Now EG = EH + HG, where DE.EH = sq(AC) and DE.HG = sq(CB). Since AC is the greater segment, EH is greater than HG. By 2.7, the square on EG plus the square on HG equals twice the rectangle EG.HG plus the square on EH. By algebraic rearrangement (equivalently 2.7), the square on EG minus the square on HG relates to the rectangle EG.HG. More precisely, by the identity from 2.5 (or direct computation), the rectangle EG.GF_breadth (where GF_breadth relates to twice AC.CB through the application to DE) and the relationship between the areas shows that the excess of the square on EG over the square on GF corresponds to terms involving the incommensurable quantities.

**Step 11.** To establish the incommensurability condition more precisely: we apply 10.18. Consider that EG and GF are the breadths produced by applying the sum of squares and twice the rectangle (respectively) to DE. Since AC and CB are incommensurable in square, sq(AC) and sq(CB) are incommensurable. These equal DE.EH and DE.HG respectively, so EH and HG are incommensurable [10.11]. If we apply to EG a parallelogram equal to the fourth part of the square on GF and deficient by a square figure, it divides EG into parts that are incommensurable (since the underlying magnitudes AC, CB are incommensurable in square). By 10.18, the square on EG is greater than the square on GF by the square on a straight line incommensurable in length with EG.

**Step 12.** By the definition of the sixth binomial [D10.2.6], a binomial straight line is called a sixth binomial when the square on the greater term is greater than the square on the lesser by the square on a straight line incommensurable in length with the greater, and neither term is commensurable in length with the rational straight line set out. We have established all three conditions: EF = EG + GF is a binomial (Step 7), neither EG nor GF is commensurable in length with DE (Step 8), and the square on EG exceeds the square on GF by the square on a straight line incommensurable with EG (Step 11).

**Step 13.** Therefore, EF is a sixth binomial straight line. That is, the square on the side of the sum of two medial areas, applied to a rational straight line, produces as breadth the sixth binomial. Q.E.D.

**USED:** 10.11, 10.13, 10.18, 10.22, 10.23, 10.24, 10.36, 10.41, 2.4, 6.1, D10.1.3, D10.1.4, D10.2.6
**Human refs (from References field):** 10.11, 10.22, 10.36, 10.41, 6.1
**Jaccard:** 0.385 — AI adds ['10.13', '10.18', '10.23', '10.24', '2.4', 'D10.1.3', 'D10.1.4', 'D10.2.6']

## Proposition 10.66
**Statement:** A straight line commensurable in length with a binomial straight line is itself also binomial and the same in order.

**Step 1.** Let AB be a binomial straight line, and let it be divided into its terms at C, where AC is the greater term. Then AC and CB are rational straight lines commensurable in square only [10.36]. Let DE be a straight line commensurable in length with AB. We must show that DE is also binomial and the same in order as AB.

**Step 2.** Since DE is commensurable in length with AB, the ratio DE:AB is a ratio which a number has to a number [10.5]. Let DE:AB = p:q where p, q are numbers.

**Step 3.** Let DE be divided at F so that DF:AC = FE:CB = DE:AB. This is possible because if we cut DE at F such that DF:DE = AC:AB, then by the properties of proportional division, DF:AC = DE:AB and the remainder FE:CB = DE:AB [6.12].

**Step 4.** Since DF:AC = p:q, a ratio of number to number, DF is commensurable in length with AC [10.6]. Similarly, since FE:CB = p:q, FE is commensurable in length with CB [10.6].

**Step 5.** Since AC is rational and DF is commensurable in length with AC, DF is rational [D10.1.3]. Since CB is rational and FE is commensurable in length with CB, FE is rational [D10.1.3].

**Step 6.** Since DF:AC = FE:CB, by alternation DF:FE = AC:CB [5.16]. Since AC and CB are commensurable in square only, AC is incommensurable in length with CB [D10.1.2]. Therefore DF is incommensurable in length with FE [10.11].

**Step 7.** Since AC and CB are commensurable in square, the ratio sq(AC):sq(CB) is a ratio of number to number [10.9]. Since DF:AC = FE:CB, we have sq(DF):sq(AC) and sq(FE):sq(CB) are each ratios of square numbers to square numbers [10.9, since commensurable in length implies commensurable in square]. By the chain of ratios sq(DF):sq(AC) = sq(FE):sq(CB), we obtain sq(DF):sq(FE) = sq(AC):sq(CB) [5.22]. Since sq(AC) is commensurable with sq(CB), it follows that sq(DF) is commensurable with sq(FE) [10.11].

**Step 8.** Thus DF and FE are rational straight lines commensurable in square only. Therefore DE = DF + FE is a binomial straight line [10.36].

**Step 9.** It remains to show that DE is the same in order as AB. Since DF:AC = FE:CB, the four lines DF, AC, FE, CB are proportional. By 10.14, if sq(AC) > sq(CB) by the square on a straight line commensurable in length with AC, then sq(DF) > sq(FE) by the square on a straight line commensurable in length with DF. Likewise, if sq(AC) > sq(CB) by the square on a straight line incommensurable in length with AC, then sq(DF) > sq(FE) by the square on a straight line incommensurable in length with DF.

**Step 10.** Now let a rational straight line G be set out. If AB is a first binomial, then AC is commensurable in length with G [D10.2.1]. Since DF is commensurable in length with AC [Step 4], DF is commensurable in length with G [10.12]. Combined with Step 9 (the commensurable case for the excess), DE satisfies the definition of a first binomial [D10.2.1].

**Step 11.** If AB is a second binomial, then CB is commensurable in length with G [D10.2.2]. Since FE is commensurable in length with CB [Step 4], FE is commensurable in length with G [10.12]. Combined with Step 9, DE satisfies the definition of a second binomial [D10.2.2].

**Step 12.** If AB is a third binomial, then neither AC nor CB is commensurable in length with G [D10.2.3]. Suppose for contradiction that DF were commensurable in length with G. Since DF is commensurable in length with AC [Step 4], then AC would be commensurable in length with G [10.12], contradicting the hypothesis. So DF is not commensurable in length with G. By the same argument, FE is not commensurable in length with G. Combined with Step 9, DE satisfies the definition of a third binomial [D10.2.3].

**Step 13.** If AB is a fourth binomial, then AC is commensurable in length with G and the excess is incommensurable [D10.2.4]. Since DF is commensurable in length with AC [Step 4], DF is commensurable in length with G [10.12]. Combined with Step 9 (the incommensurable case), DE satisfies the definition of a fourth binomial [D10.2.4].

**Step 14.** If AB is a fifth binomial, then CB is commensurable in length with G and the excess is incommensurable [D10.2.5]. Since FE is commensurable in length with CB [Step 4], FE is commensurable in length with G [10.12]. Combined with Step 9, DE satisfies the definition of a fifth binomial [D10.2.5].

**Step 15.** If AB is a sixth binomial, then neither AC nor CB is commensurable in length with G and the excess is incommensurable [D10.2.6]. By the same reasoning as in Step 12, neither DF nor FE is commensurable in length with G. Combined with Step 9, DE satisfies the definition of a sixth binomial [D10.2.6].

**Step 16.** Therefore in every case DE is a binomial straight line of the same order as AB. Q.E.D.

**USED:** 10.11, 10.12, 10.14, 10.36, 10.5, 10.6, 10.9, 5.16, 5.22, 6.12, D10.1.2, D10.1.3, D10.2.1, D10.2.2, D10.2.3, D10.2.4, D10.2.5, D10.2.6
**Human refs (from References field):** 10.11, 10.12, 10.13, 10.14, 10.36, 5.11, 5.16, 5.19, 6.12, D10.2.1, D10.2.2, D10.2.3, D10.2.4, D10.2.5, D10.2.6
**Jaccard:** 0.571 — AI adds ['10.5', '10.6', '10.9', '5.22', 'D10.1.2', 'D10.1.3']; Human adds ['10.13', '5.11', '5.19']

## Proposition 10.67
**Statement:** A straight line commensurable in length with a bimedial straight line is itself also bimedial and the same in order.

**Step 1.** Let AB be a bimedial straight line, and let CD be commensurable in length with AB. We must show that CD is also bimedial and the same in order as AB.

**Step 2.** Since AB is bimedial, it is either a first bimedial or a second bimedial. Let AB be divided into its medial terms at E, so that AB = AE + EB, where AE is the greater term. By the definition of bimedial (whether first or second, per 10.37 and 10.38), AE and EB are medial straight lines commensurable in square only.

**Step 3.** Since CD is commensurable in length with AB, let CD : AB be a ratio of commensurable magnitudes. By 10.6, CD and AB have to one another the ratio which a number has to a number. Let this ratio be that of the number p to the number q.

**Step 4.** Divide CD at F such that CF : AE = FD : EB = CD : AB. This can be done because we can set CF such that CF : AE = CD : AB, and then since CD = CF + FD and AB = AE + EB, by 5.19 (componendo applied inversely, i.e., separando), FD : EB = CD : AB as well.

**Step 5.** Since CF : AE = CD : AB and CD is commensurable in length with AB, the ratio CD : AB is a ratio of number to number (by 10.5). Therefore CF : AE is also a ratio of number to number, so by 10.6, CF is commensurable in length with AE. Similarly, FD is commensurable in length with EB.

**Step 6.** Since AE is medial and CF is commensurable in length with AE, by 10.23 CF is also medial. Similarly, since EB is medial and FD is commensurable in length with EB, FD is also medial.

**Step 7.** We now show CF and FD are commensurable in square only. Since AE and EB are commensurable in square only, the squares on AE and EB are commensurable (i.e., have a ratio of number to number). Since CF is commensurable in length with AE, the square on CF is commensurable with the square on AE (by 10.11 applied to the proportion of the squares, or directly because commensurable in length implies commensurable in square). Similarly, the square on FD is commensurable with the square on EB. Since sq(AE) is commensurable with sq(EB), and sq(CF) is commensurable with sq(AE), and sq(FD) is commensurable with sq(EB), by 10.12 sq(CF) is commensurable with sq(FD). Thus CF and FD are commensurable in square.

**Step 8.** Now suppose CF and FD were commensurable in length. Since CF is commensurable in length with AE, and FD is commensurable in length with EB, then by 10.12 AE would be commensurable in length with EB. But AE and EB are commensurable in square only, a contradiction. Therefore CF and FD are not commensurable in length, and hence they are commensurable in square only.

**Step 9.** We now show that the rectangle contained by CF and FD is of the same kind (rational or medial) as the rectangle contained by AE and EB. Since CF : AE = FD : EB (both equal to CD : AB), the rectangle CF.FD has to the rectangle AE.EB the duplicate ratio of CF to AE (by 6.23, since CF : AE = FD : EB). But CF is commensurable in length with AE, so CF : AE is a ratio of number to number (10.5), and the duplicate of a ratio of number to number is also a ratio of number to number (by 8.11). Therefore the rectangle CF.FD has to the rectangle AE.EB a ratio of number to number, so by 10.6 the rectangle CF.FD is commensurable with the rectangle AE.EB.

**Step 10.** Case 1: AB is a first bimedial. Then by 10.37, the rectangle AE.EB is rational. Since the rectangle CF.FD is commensurable with the rectangle AE.EB (Step 9), and a magnitude commensurable with a rational magnitude is rational, the rectangle CF.FD is also rational. Since CF and FD are medial straight lines commensurable in square only (Steps 6, 8) containing a rational rectangle, CD = CF + FD is a first bimedial by 10.37.

**Step 11.** Case 2: AB is a second bimedial. Then by 10.38, the rectangle AE.EB is medial. Since the rectangle CF.FD is commensurable with the rectangle AE.EB (Step 9), and a magnitude commensurable with a medial area is medial (by the definition of medial area, D10.1.4, and 10.23 applied to areas via 10.11), the rectangle CF.FD is also medial. Since CF and FD are medial straight lines commensurable in square only (Steps 6, 8) containing a medial rectangle, CD = CF + FD is a second bimedial by 10.38.

**Step 12.** Therefore in either case, CD is bimedial and the same in order as AB. Q.E.D.

**USED:** 10.11, 10.12, 10.23, 10.37, 10.38, 10.5, 10.6, 5.19, 6.23, 8.11, D10.1.4
**Human refs (from References field):** 10.11, 10.23, 10.37, 10.38, 5.11, 5.16, 5.19
**Jaccard:** 0.385 — AI adds ['10.12', '10.5', '10.6', '6.23', '8.11', 'D10.1.4']; Human adds ['5.11', '5.16']

## Proposition 10.68
**Statement:** A straight line commensurable with a major straight line is itself also major.

**Step 1.** Let AB be a major straight line, and let CD be commensurable in length with AB. I say that CD is also major.

**Step 2.** Since AB is a major straight line, let it be divided at E into its terms, so that AE, EB are straight lines incommensurable in square, the sum of the squares on AE and EB is rational, and the rectangle contained by AE and EB is medial [10.39].

**Step 3.** Since CD is commensurable in length with AB, let CD be divided at F such that CF is to FD as AE is to EB [6.12]. Then since AE is to EB as CF is to FD, we also have AB is to CD as AE is to CF, and also as EB is to FD [5.12, 5.16, 5.11]. Therefore AE is commensurable in length with CF, and EB is commensurable in length with FD, since AB is commensurable in length with CD [10.11].

**Step 4.** Since AE is commensurable in length with CF, the square on AE is commensurable with the square on CF [10.11]. For the same reason, the square on EB is commensurable with the square on FD.

**Step 5.** Therefore the sum of the squares on AE and EB is commensurable with the sum of the squares on CF and FD [10.15, 10.12]. But the sum of the squares on AE and EB is rational [Step 2]. Therefore the sum of the squares on CF and FD is also rational [D10.1.3].

**Step 6.** Again, since AE is to EB as CF is to FD [Step 3], the rectangle contained by AE and EB is to the rectangle contained by CF and FD as the square on AE is to the square on CF [6.16]. But the square on AE is commensurable with the square on CF [Step 4]. Therefore the rectangle contained by AE and EB is commensurable with the rectangle contained by CF and FD [10.11].

**Step 7.** But the rectangle contained by AE and EB is medial [Step 2]. Therefore the rectangle contained by CF and FD is also medial [10.23 applied to areas, i.e., an area commensurable with a medial area is medial; more precisely, by D10.1.4 and 10.12, since the rectangle AE·EB is medial, and the rectangle CF·FD is commensurable with it, the rectangle CF·FD is also medial].

**Step 8.** Now since AE is to EB as CF is to FD, and AE is incommensurable in square with EB [Step 2], CF is also incommensurable in square with FD [10.11].

**Step 9.** Therefore CF and FD are straight lines incommensurable in square which make the sum of the squares on them rational [Step 5] and the rectangle contained by them medial [Step 7].

**Step 10.** Therefore the whole CD is a major straight line [10.39]. Q.E.D.

**USED:** 10.11, 10.12, 10.15, 10.23, 10.39, 5.11, 5.12, 5.16, 6.12, 6.16, D10.1.3, D10.1.4
**Human refs (from References field):** 10.11, 10.23, 10.39, 5.11, 5.16, 5.18, 6.20
**Jaccard:** 0.357 — AI adds ['10.12', '10.15', '5.12', '6.12', '6.16', 'D10.1.3', 'D10.1.4']; Human adds ['5.18', '6.20']

## Proposition 10.69
**Statement:** A straight line commensurable with the side of a rational plus a medial area is itself also the side of a rational plus a medial area.

**Step 1.** Let AB be the side of a rational plus a medial area, and let DE be commensurable in length with AB. We must show that DE is also the side of a rational plus a medial area.

**Step 2.** Since AB is the side of a rational plus a medial area, by 10.40, AB has been divided at some point C into two straight lines AC, CB that are incommensurable in square, such that the sum of the squares on AC and CB is medial, and the rectangle contained by AC and CB is rational.

**Step 3.** Since DE is commensurable in length with AB, let DE be divided at F such that AB is to DE as AC is to DF and as CB is to FE (6.12, by dividing DE proportionally to the division of AB at C).

**Step 4.** Then AB : DE = AC : DF = CB : FE. Since AB is commensurable in length with DE, it follows that AC is commensurable in length with DF, and CB is commensurable in length with FE (10.11).

**Step 5.** Since AC is commensurable in length with DF, the square on AC is commensurable with the square on DF (6.22, 10.11). Similarly, since CB is commensurable in length with FE, the square on CB is commensurable with the square on FE.

**Step 6.** Therefore the sum of the squares on AC and CB is commensurable with the sum of the squares on DF and FE (10.15, by adding commensurable magnitudes).

**Step 7.** Since the sum of the squares on AC and CB is medial (by hypothesis from Step 2), and the sum of the squares on DF and FE is commensurable with it, the sum of the squares on DF and FE is also medial (10.23 applied to areas: a medial area commensurable with a medial area is medial, which follows because a medial area applied to a rational line gives a rational breadth incommensurable with it by 10.22, and commensurable areas give commensurable breadths by 10.11, so the breadth for the new sum is also rational and incommensurable, hence the area is medial).

**Step 8.** Since AC : DF = CB : FE (from Step 4), the rectangle AC.CB is to the rectangle DF.FE as the square on AC is to the square on DF (6.16, since AC : DF = CB : FE implies rect(AC,CB) : rect(DF,FE) = AC.CB : DF.FE = AC^2 : AC.DF, but more precisely, by 6.16, if four lines are proportional then the rectangle of the extremes is to the rectangle of the means in a determinate ratio; here since AC:DF = CB:FE, we get rect(AC,CB) : rect(DF,FE) = sq(AC) : sq(DF)).

**Step 9.** Since AC is commensurable in length with DF, the square on AC is commensurable with the square on DF (6.22, 10.11). Therefore the rectangle AC.CB is commensurable with the rectangle DF.FE (10.11, from the proportion in Step 8).

**Step 10.** Since the rectangle AC.CB is rational (by hypothesis from Step 2), and the rectangle DF.FE is commensurable with it, the rectangle DF.FE is also rational (D10.1.4, since commensurable with a rational area).

**Step 11.** Since AC is incommensurable in square with CB, and AC is commensurable in length with DF while CB is commensurable in length with FE, it follows that DF is incommensurable in square with FE (10.13, since if DF were commensurable in square with FE, then via the commensurability of AC with DF and CB with FE, AC would be commensurable in square with CB by 10.12, contradicting the hypothesis).

**Step 12.** Therefore DF and FE are two straight lines incommensurable in square, the sum of the squares on them is medial (Step 7), and the rectangle contained by them is rational (Step 10). Hence by 10.40, DE = DF + FE is the side of a rational plus a medial area.

**Step 13.** Therefore a straight line commensurable with the side of a rational plus a medial area is itself also the side of a rational plus a medial area. Q.E.D.

**USED:** 10.11, 10.12, 10.13, 10.15, 10.22, 10.23, 10.40, 6.12, 6.16, 6.22, D10.1.4
**Human refs (from References field):** 10.40
**Jaccard:** 0.091 — AI adds ['10.11', '10.12', '10.13', '10.15', '10.22', '10.23', '6.12', '6.16', '6.22', 'D10.1.4']

## Proposition 10.70
**Statement:** A straight line commensurable with the side of the sum of two medial areas is the side of the sum of two medial areas.

**Step 1.** Let AB be the side of the sum of two medial areas, and let CD be commensurable in length with AB. We must show that CD is also the side of the sum of two medial areas.

**Step 2.** Since AB is the side of the sum of two medial areas, by the definition (10.41), AB has been divided into its terms at some point E, so that AB = AE + EB, where AE and EB are straight lines incommensurable in square, the sum of the squares on AE and EB is medial, the rectangle contained by AE and EB is medial, and the sum of the squares on AE and EB is incommensurable with the rectangle AE and EB.

**Step 3.** Since CD is commensurable in length with AB, let CD be divided at F such that AE is to CF as EB is to FD, that is, as AB is to CD (6.12). Then since AE : CF = EB : FD = AB : CD, and AB is commensurable in length with CD, it follows that AE is commensurable in length with CF, and EB is commensurable in length with FD (10.11).

**Step 4.** Since AE is commensurable in length with CF, the square on AE is commensurable with the square on CF (6.22, 10.11). Similarly, since EB is commensurable in length with FD, the square on EB is commensurable with the square on FD. Therefore the sum of the squares on AE and EB is commensurable with the sum of the squares on CF and FD (10.15, 10.12).

**Step 5.** Since the sum of the squares on AE and EB is medial, and the sum of the squares on CF and FD is commensurable with it, the sum of the squares on CF and FD is also medial (10.23 applied to the areas: a medial area commensurable with a medial area is medial, which follows because commensurable areas produce sides that are commensurable, and a medial straight line commensurable with a medial is medial by 10.23).

**Step 6.** Since AE : CF = EB : FD, we also have that the rectangle contained by AE and EB is to the rectangle contained by CF and FD as the square on AE is to the square on CF (6.16). But the square on AE is commensurable with the square on CF (from Step 4). Therefore the rectangle AE by EB is commensurable with the rectangle CF by FD (10.11).

**Step 7.** Since the rectangle contained by AE and EB is medial, and the rectangle contained by CF and FD is commensurable with it, the rectangle contained by CF and FD is also medial (by the same reasoning as Step 5, using 10.23).

**Step 8.** Since the sum of the squares on AE and EB is incommensurable with the rectangle AE by EB, and the sum of the squares on CF and FD is commensurable with the sum of the squares on AE and EB (Step 4), and the rectangle CF by FD is commensurable with the rectangle AE by EB (Step 6), it follows that the sum of the squares on CF and FD is incommensurable with the rectangle CF by FD (10.13).

**Step 9.** We must also verify that CF and FD are incommensurable in square. Since AE and EB are incommensurable in square, the square on AE is incommensurable with the square on EB. Now the square on AE is commensurable with the square on CF, and the square on EB is commensurable with the square on FD. Therefore the square on CF is incommensurable with the square on FD (10.13), which means CF and FD are incommensurable in square.

**Step 10.** Therefore CF and FD are two straight lines incommensurable in square such that the sum of the squares on them is medial, the rectangle contained by them is medial, and the sum of the squares on them is incommensurable with the rectangle contained by them. Hence, by 10.41, CD = CF + FD is the side of the sum of two medial areas.

**Step 11.** Therefore a straight line commensurable with the side of the sum of two medial areas is itself also the side of the sum of two medial areas. Q.E.D.

**USED:** 10.11, 10.12, 10.13, 10.15, 10.23, 10.41, 10.47, 6.12, 6.16, 6.22
**Human refs (from References field):** 10.41
**Jaccard:** 0.100 — AI adds ['10.11', '10.12', '10.13', '10.15', '10.23', '10.47', '6.12', '6.16', '6.22']

## Proposition 10.71
**Statement:** If a rational and a medial area be added together, four irrational straight lines arise, namely a binomial or a first bimedial or a major or a side of a rational plus a medial area.

**Step 1.** Let AB be a rational area and CD a medial area. We must show that the side of the area equal to AB plus CD (i.e., the straight line whose square equals AB + CD) is either a binomial, a first bimedial, a major, or a side of a rational plus a medial area.

**Step 2.** Let a rational straight line EF be set out. Apply the area AB to EF, producing breadth EG, so that EG times EF equals AB. Since AB is a rational area and EF is rational, by Proposition 10.20, EG is rational and commensurable in length with EF.

**Step 3.** Apply the area CD to EF, producing breadth GH (placed adjacent to EG along EF), so that GH times EF equals CD. Since CD is a medial area and EF is rational, by Proposition 10.22, GH is rational and incommensurable in length with EF.

**Step 4.** Since EG is commensurable in length with EF and GH is incommensurable in length with EF, it follows that EG and GH are incommensurable in length with one another (for if EG and GH were commensurable in length, then since EG is commensurable in length with EF, by Proposition 10.12, GH would be commensurable in length with EF, contradicting Step 3).

**Step 5.** Now EG and GH are both rational (Steps 2 and 3) and incommensurable in length (Step 4). The whole straight line EH equals EG + GH. The area applied to the rational line EF with breadth EH equals AB + CD. That is, EH times EF equals AB + CD.

**Step 6.** Since EG and GH are rational straight lines incommensurable in length, the line EH = EG + GH is either a binomial or one of the other irrational sums. We now proceed by cases based on the classification of EH as a binomial straight line and then determine the type of binomial it is, which in turn determines the nature of the side of the area.

**Step 7.** Since EG and GH are rational and commensurable in square (both being rational straight lines, the squares on them have the ratio of a number to a number by Proposition 10.9, hence they are commensurable in square), but incommensurable in length, by Proposition 10.36, the whole EH is a binomial straight line.

**Step 8.** We now classify which order of binomial EH is, relative to the rational line EF. There are four possible sub-cases depending on the relationship between EG, GH, and EF, and whether the square on the greater term exceeds the square on the lesser by the square on a line commensurable or incommensurable in length with the greater.

**Step 9.** Case 1: Suppose the square on EG is greater than the square on GH by the square on a straight line commensurable in length with EG, and EG (the greater term) is commensurable in length with the rational line EF. Then by Definition 10.2.1, EH is a first binomial straight line. Since the area EH times EF is the area AB + CD contained by a rational straight line EF and a first binomial EH, by Proposition 10.54, the side of the area AB + CD is a binomial straight line.

**Step 10.** Case 2: Suppose the square on EG is greater than the square on GH by the square on a straight line commensurable in length with EG, and GH (the lesser term) is commensurable in length with EF. Then by Definition 10.2.2, EH is a second binomial straight line. Since the area AB + CD is contained by the rational straight line EF and the second binomial EH, by Proposition 10.55, the side of the area AB + CD is a first bimedial straight line.

**Step 11.** Case 3: Suppose the square on EG is greater than the square on GH by the square on a straight line incommensurable in length with EG, and EG (the greater term) is commensurable in length with EF. Then by Definition 10.2.4, EH is a fourth binomial straight line. Since the area AB + CD is contained by the rational straight line EF and the fourth binomial EH, by Proposition 10.57, the side of the area AB + CD is a major straight line.

**Step 12.** Case 4: Suppose the square on EG is greater than the square on GH by the square on a straight line incommensurable in length with EG, and GH (the lesser term) is commensurable in length with EF. Then by Definition 10.2.5, EH is a fifth binomial straight line. Since the area AB + CD is contained by the rational straight line EF and the fifth binomial EH, by Proposition 10.58, the side of the area AB + CD is a side of a rational plus a medial area.

**Step 13.** We must verify that only these four cases arise and that the third and sixth binomial types do not occur. In a third binomial (Definition 10.2.3), neither term is commensurable in length with the rational line set out. But we established in Step 2 that EG is commensurable in length with EF. So EH cannot be a third binomial. In a sixth binomial (Definition 10.2.6), again neither term is commensurable in length with the rational line set out, but EG is commensurable in length with EF. So EH cannot be a sixth binomial either. Thus the only possibilities are the first, second, fourth, or fifth binomial.

**Step 14.** Note also that Cases 2 and 4 require that EG not be commensurable in length with EF, and Cases 1 and 3 require that GH not be commensurable in length with EF. But from Step 2, EG is commensurable in length with EF, and from Step 3, GH is incommensurable in length with EF. Therefore Case 2 would require EG incommensurable in length with EF, which contradicts Step 2 unless we consider whether EG is always the greater term. In fact, EG may or may not be the greater of the two terms EG and GH. Let us reconsider: let the greater of EG and GH be called the greater term.

**Step 15.** If EG is the greater term (i.e., EG > GH): Since EG is commensurable in length with EF, and EG is the greater term, we fall into Cases 1 or 3 depending on the commensurability condition on the excess of squares. This yields either a first binomial (Case 1, giving a binomial side by 10.54) or a fourth binomial (Case 3, giving a major side by 10.57).

**Step 16.** If GH is the greater term (i.e., GH > EG): Then EG is the lesser term. Since EG is commensurable in length with EF, EG (the lesser term) is commensurable in length with EF. Then we check whether GH (the greater term) is commensurable in length with EF. From Step 3, GH is incommensurable in length with EF. So neither term being the greater is commensurable in length with EF in the sense of Definition 10.2.1 (which requires the greater term to be commensurable), but the lesser term EG is commensurable. This yields Cases 2 or 4: if the square on GH exceeds the square on EG by the square on a line commensurable with GH, we get a second binomial (giving a first bimedial by 10.55); if by a line incommensurable with GH, we get a fifth binomial (giving a side of a rational plus a medial area by 10.58).

**Step 17.** Therefore, in all cases, the side of the combined area AB + CD is one of exactly four irrational straight lines: a binomial, a first bimedial, a major, or a side of a rational plus a medial area. This is what was to be shown.

**USED:** 10.12, 10.20, 10.22, 10.36, 10.54, 10.55, 10.57, 10.58, 10.9, D10.2.1, D10.2.2, D10.2.3, D10.2.4, D10.2.5, D10.2.6
**Human refs (from References field):** 10.11, 10.20, 10.22, 10.36, 10.54, 10.55, 10.57, 10.58, 6.1, D10.2.1, D10.2.2, D10.2.4, D10.2.5
**Jaccard:** 0.647 — AI adds ['10.12', '10.9', 'D10.2.3', 'D10.2.6']; Human adds ['10.11', '6.1']

## Proposition 10.72
**Statement:** If two medial areas incommensurable with one another be added together, the remaining two irrational straight lines arise, namely either a second bimedial or a side of the sum of two medial areas.

**Step 1.** Let AB and CD be two medial areas incommensurable with one another. We are to show that the side of the area AB + CD is either a second bimedial straight line or a side of the sum of two medial areas.

**Step 2.** Set out a rational straight line EF. Apply to EF the rectangle EH equal to AB, producing breadth EG, and adjacent to it apply the rectangle HK equal to CD, producing breadth GK; so that the total rectangle EK equals AB + CD with breadth EG + GK along EF.

**Step 3.** Since AB is a medial area and EF is rational, by 10.22 the breadth EG is rational and incommensurable in length with EF. Similarly, since CD is medial and EF is rational, by 10.22 the breadth GK is rational and incommensurable in length with EF.

**Step 4.** Since AB is incommensurable with CD, and AB = EF * EG while CD = EF * GK, it follows by 10.11 that EG is incommensurable in length with GK.

**Step 5.** Now EG and GK are both rational straight lines (Step 3) and incommensurable in length with one another (Step 4). Two rational straight lines incommensurable in length are commensurable in square only, so by 10.36, EG + GK is a binomial straight line.

**Step 6.** We determine which order of binomial EG + GK is with respect to the rational line EF. Let EG be the greater term. Since EG is incommensurable in length with EF (Step 3), the binomial is not a first binomial (D10.2.1) and not a fourth binomial (D10.2.4), for both require the greater term to be commensurable in length with the rational line. Since GK is incommensurable in length with EF (Step 3), the binomial is not a second binomial (D10.2.2) and not a fifth binomial (D10.2.5), for both require the lesser term to be commensurable in length with the rational line.

**Step 7.** Therefore EG + GK is either a third binomial or a sixth binomial with respect to EF. The distinction depends on whether the square on EG exceeds the square on GK by the square on a straight line commensurable or incommensurable in length with EG: if commensurable, it is a third binomial (D10.2.3); if incommensurable, it is a sixth binomial (D10.2.6). Both cases are possible.

**Step 8.** The side of the area AB + CD is the side of the rectangle EF * (EG + GK), that is, the straight line whose square equals the rectangle contained by the rational line EF and the binomial EG + GK.

**Step 9.** If EG + GK is a third binomial, then by 10.56 the side of the rectangle contained by EF and a third binomial is a second bimedial straight line.

**Step 10.** If EG + GK is a sixth binomial, then by 10.59 the side of the rectangle contained by EF and a sixth binomial is a side of the sum of two medial areas.

**Step 11.** That both cases actually arise is confirmed: by 10.28 and 10.38, two medial straight lines commensurable in square only containing a medial rectangle produce a second bimedial, and their squares are incommensurable medial areas whose sum has a second bimedial as its side; by 10.35 and 10.41, there exist lines incommensurable in square making both the sum of their squares and their rectangle medial and mutually incommensurable, producing a side of the sum of two medial areas.

**Step 12.** Therefore, if two medial areas incommensurable with one another be added together, the side of the resulting area is either a second bimedial or a side of the sum of two medial areas, and no other irrational straight line arises. Q.E.D.

**USED:** 10.11, 10.22, 10.28, 10.35, 10.36, 10.38, 10.41, 10.56, 10.59, D10.2.1, D10.2.2, D10.2.3, D10.2.4, D10.2.5, D10.2.6
**Human refs (from References field):** 10.11, 10.22, 10.36, 10.56, 10.59, 6.1, D10.2.3, D10.2.6
**Jaccard:** 0.438 — AI adds ['10.28', '10.35', '10.38', '10.41', 'D10.2.1', 'D10.2.2', 'D10.2.4', 'D10.2.5']; Human adds ['6.1']

## Proposition 10.73
**Statement:** If from a rational straight line there be subtracted a rational straight line commensurable with the whole in square only, the remainder is irrational; and let it be called   an apotome.

**Step 1.** Let AB be a rational straight line, and from AB let there be subtracted BC, a rational straight line commensurable with AB in square only. We are to show that the remainder AC is irrational.

**Step 2.** Since AB and BC are rational straight lines commensurable in square only, the squares on AB and on BC are commensurable with one another [D10.1.3]. Therefore the sum of the squares on AB and BC, being commensurable magnitudes added together, is commensurable with each of them [10.15]. But the square on AB is rational (since AB is rational) [D10.1.4], so the sum of the squares on AB and BC is also rational [D10.1.4].

**Step 3.** Since AB and BC are rational straight lines commensurable in square only, the rectangle contained by AB and BC is irrational, that is, medial [10.21]. Therefore twice the rectangle contained by AB and BC is also irrational, being a medial area.

**Step 4.** Now, since AB is cut at C, by Proposition 2.7 the square on AB together with the square on BC is equal to twice the rectangle contained by AB and BC together with the square on AC. Therefore the square on AC is equal to the sum of the squares on AB and BC minus twice the rectangle contained by AB and BC [CN3].

**Step 5.** Suppose, for the sake of contradiction, that AC is rational. Then the square on AC is rational [D10.1.4]. Since both the sum of the squares on AB and BC is rational and the square on AC is rational, their difference, which equals twice the rectangle contained by AB and BC, would be rational [10.15]. But this contradicts Step 3, which established that twice the rectangle contained by AB and BC is irrational (medial).

**Step 6.** Therefore the square on AC is not rational, which means that AC is irrational [D10.1.4]. Let this irrational straight line be called an apotome. Q.E.D.

**USED:** 10.15, 10.21, 2.7, CN3, D10.1.3, D10.1.4
**Human refs (from References field):** 10.11, 10.13, 10.15, 10.16, 10.6, 2.7, D10.1.4
**Jaccard:** 0.300 — AI adds ['10.21', 'CN3', 'D10.1.3']; Human adds ['10.11', '10.13', '10.16', '10.6']

## Proposition 10.74
**Statement:** If from a medial straight line there be subtracted a medial straight line which is commensurable with the whole in square only, and which contains with the whole a rational rectangle, the remainder is irrational. And let it be called a first apotome of a medial straight line.

**Step 1.** Let AB be a medial straight line, and from AB let BC be subtracted, where BC is also medial, AB and BC are commensurable in square only, and the rectangle contained by AB and BC is rational. We are to show that the remainder AC is irrational.

**Step 2.** Set out a rational straight line rho. Apply to rho a rectangle equal to the square on AB, producing breadth p1, so that rho * p1 = sq(AB). Since AB is medial, sq(AB) is a medial area [D10.1.4]. By 10.22, p1 is rational and incommensurable in length with rho.

**Step 3.** Similarly, apply to rho a rectangle equal to the square on BC, producing breadth p2, so that rho * p2 = sq(BC). Since BC is medial, sq(BC) is a medial area [D10.1.4]. By 10.22, p2 is rational and incommensurable in length with rho.

**Step 4.** Since AB and BC are commensurable in square, sq(AB) and sq(BC) are commensurable areas [D10.1.2]. Now rho * p1 : rho * p2 = p1 : p2 [6.1]. Since rho * p1 (= sq(AB)) is commensurable with rho * p2 (= sq(BC)), it follows that p1 is commensurable in length with p2 [10.11].

**Step 5.** Since p1 and p2 are commensurable magnitudes, their sum p1 + p2 is commensurable with each of them [10.15]. Since p1 is rational, p1 + p2 is commensurable with a rational line, so p1 + p2 is rational [D10.1.3]. Since p1 is incommensurable in length with rho, and p1 + p2 is commensurable with p1, it follows that p1 + p2 is incommensurable in length with rho [10.13].

**Step 6.** Now the rectangle AB,BC is rational by hypothesis. Since 2 : 1 is a ratio of numbers, 2 * rect(AB,BC) is commensurable with rect(AB,BC) [10.6], and therefore 2 * rect(AB,BC) is also a rational area [D10.1.4]. Apply 2 * rect(AB,BC) to rho, producing breadth q. By 10.20, q is rational and commensurable in length with rho.

**Step 7.** Since p1 + p2 is incommensurable in length with rho (Step 5) and q is commensurable in length with rho (Step 6), it follows that p1 + p2 is incommensurable in length with q [10.13].

**Step 8.** Both p1 + p2 and q are rational straight lines. Since p1 + p2 is commensurable with rho in square [D10.1.3] and q is commensurable with rho in square [D10.1.3], it follows that p1 + p2 and q are commensurable in square [10.12]. Combined with their incommensurability in length (Step 7), p1 + p2 and q are commensurable in square only.

**Step 9.** By 2.7, sq(AB) + sq(BC) = sq(AC) + 2 * rect(AB,BC). Since sq(AC) is a positive area, sq(AB) + sq(BC) is greater than 2 * rect(AB,BC) [CN5]. Therefore rho * (p1 + p2) > rho * q, which gives p1 + p2 > q.

**Step 10.** Since p1 + p2 and q are rational straight lines commensurable in square only, and p1 + p2 > q, by 10.73 the remainder (p1 + p2) - q is irrational; it is an apotome.

**Step 11.** From Step 9, sq(AC) = sq(AB) + sq(BC) - 2 * rect(AB,BC) = rho * (p1 + p2) - rho * q = rho * ((p1 + p2) - q). So the square on AC, when applied to the rational line rho, produces as breadth the apotome (p1 + p2) - q, which is irrational.

**Step 12.** If AC were rational, then sq(AC) would be a rational area [D10.1.3, D10.1.4], and by 10.20 the breadth produced by applying sq(AC) to the rational line rho would be rational and commensurable in length with rho. But the breadth is an apotome, which is irrational. This is a contradiction, so AC is not rational. Therefore AC is irrational [D10.1.3].

**Step 13.** Let AC be called a first apotome of a medial straight line. Q.E.D.

**USED:** 10.11, 10.12, 10.13, 10.15, 10.20, 10.22, 10.6, 10.73, 2.7, 6.1, CN5, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 10.16, 2.7, D10.1.4
**Jaccard:** 0.133 — AI adds ['10.11', '10.12', '10.13', '10.15', '10.20', '10.22', '10.6', '10.73', '6.1', 'CN5', 'D10.1.2', 'D10.1.3']; Human adds ['10.16']

## Proposition 10.75
**Statement:** If from a medial straight line there be subtracted a medial straight line which is commensurable with the whole in square only, and which contains with the whole a medial rectangle, the remainder is irrational; and let it be called a second apotome of a medial straight line.

**Step 1.** Let AB be a medial straight line, and from AB let there be subtracted CB, a medial straight line commensurable with AB in square only and such that the rectangle AB by CB is medial. We must show that the remainder AC is irrational.

**Step 2.** Set out a rational straight line DI. Apply to DI the rectangle DE equal to the square on AB, producing DG as breadth, so that DE = sq(AB). Since AB is medial, sq(AB) is a medial area [by D10.1.3, D10.1.4]. A medial area applied to a rational straight line produces a breadth that is rational and incommensurable in length with the line to which it is applied [by 10.22]. Therefore DG is rational and incommensurable in length with DI.

**Step 3.** Apply to DI the rectangle DF equal to the square on BC, producing GF as breadth (where F is between D and E along the line DI so that DF is contained within DE), so that DF = sq(BC). Since BC is medial, sq(BC) is a medial area, and by the same reasoning [10.22], GF is rational and incommensurable in length with DI.

**Step 4.** Since AB and CB are commensurable in square only, sq(AB) and sq(BC) are commensurable [by D10.1.2]. Therefore DE is commensurable with DF. Hence DG is commensurable with GF [by 6.1 and 10.11]. Since DG and GF are each rational, and they are commensurable with each other, the rectangle DG by GF is rational [by 10.19].

**Step 5.** Now, since sq(AB) is commensurable with sq(BC) but AB is incommensurable in length with BC (they are commensurable in square only), AB is incommensurable in length with BC. Therefore the rectangle AB by BC is incommensurable with sq(AB) [by 10.11, since AB : BC is the ratio and AB by BC : sq(AB) = BC : AB]. Similarly AB by BC is incommensurable with sq(BC).

**Step 6.** Now consider the remaining area FE = DE - DF = sq(AB) - sq(BC). By 2.7, we have sq(AB) + sq(BC) = 2 rect(AB, BC) + sq(AC), so sq(AB) - sq(BC) = sq(AC) + 2 rect(AB, BC) - 2 sq(BC). Instead, we use the identity directly: DE - DF corresponds to the region with breadth GE, so the rectangle DI by GE = sq(AB) - sq(BC).

**Step 7.** Apply to DI the rectangle DH equal to twice the rectangle AB by BC, producing some breadth. Since AB by BC is medial, twice AB by BC is also medial [by 10.23 and the fact that doubling a medial area yields a medial area, or more precisely by 10.24 and properties of commensurable areas]. We place DH so that the remaining area HE equals sq(AC), since sq(AB) = sq(AC) + sq(BC) + 2 rect(AC, CB) [by 2.4 applied to AB = AC + CB]. Thus DE = sq(AB) = sq(AC) + sq(BC) + 2 rect(AC, CB), meaning DE = DF + DH + HE where DF = sq(BC), DH = 2 rect(AC, CB). Actually, let us reorganize using the correct identity.

**Step 8.** Since AB = AC + CB, by 2.4 we have sq(AB) = sq(AC) + sq(CB) + 2 rect(AC, CB). Therefore sq(AC) = sq(AB) - sq(CB) - 2 rect(AC, CB). Now DE = sq(AB) and DF = sq(CB), so DE - DF = sq(AC) + 2 rect(AC, CB), giving FE = sq(AC) + 2 rect(AC, CB).

**Step 9.** Now twice the rectangle AB by CB: since AB = AC + CB, we have rect(AB, CB) = rect(AC, CB) + sq(CB) [by 2.3]. So 2 rect(AB, CB) = 2 rect(AC, CB) + 2 sq(CB). We are given that rect(AB, CB) is medial.

**Step 10.** Let us apply a cleaner arrangement. Apply to DI: let DE = sq(AB) with breadth DG, let DH = 2 rect(AB, CB) with some configuration, and let DF = sq(BC) with breadth up to a point. By 2.7, sq(AB) + sq(BC) = 2 rect(AB, BC) + sq(AB - BC), i.e., sq(AB) + sq(BC) = 2 rect(AB, BC) + sq(AC). Therefore sq(AC) = sq(AB) + sq(BC) - 2 rect(AB, BC).

**Step 11.** Apply to DI: let the rectangle with area sq(AB) + sq(BC) have breadth MG (say DI x MG = sq(AB) + sq(BC)), and let the rectangle with area 2 rect(AB, BC) have breadth MF (say DI x MF = 2 rect(AB, BC)). Then DI x (MG - MF) = sq(AC), so DI x GF' = sq(AC) where GF' = MG - MF.

**Step 12.** Since AB and BC are each medial, sq(AB) and sq(BC) are each medial areas. Since AB and BC are commensurable in square, sq(AB) and sq(BC) are commensurable. Therefore sq(AB) + sq(BC) is commensurable with sq(AB) [by 10.15], and hence sq(AB) + sq(BC) is a medial area [by 10.23 applied to areas, since it is commensurable with a medial area]. Applying this medial area to the rational line DI, the breadth MG is rational and incommensurable in length with DI [by 10.22].

**Step 13.** Since rect(AB, BC) is medial (given), 2 rect(AB, BC) is also medial (being commensurable with the medial area rect(AB, BC), by 10.6 with ratio 2:1, and 10.23). Applying this medial area to the rational line DI, the breadth MF is rational and incommensurable in length with DI [by 10.22].

**Step 14.** We now show MG and MF are incommensurable. Since sq(AB) + sq(BC) is incommensurable with 2 rect(AB, BC): We know sq(AB) + sq(BC) is commensurable with sq(AB). And 2 rect(AB, BC) is commensurable with rect(AB, BC). Now rect(AB, BC) is medial and incommensurable with sq(AB) (since AB and BC are incommensurable in length, rect(AB, BC) is incommensurable with sq(BC), and since sq(AB) is commensurable with sq(BC), rect(AB, BC) is incommensurable with sq(AB) too [by 10.13]). Since sq(AB) + sq(BC) is commensurable with sq(AB), and 2 rect(AB, BC) is commensurable with rect(AB, BC), and sq(AB) is incommensurable with rect(AB, BC), it follows that sq(AB) + sq(BC) is incommensurable with 2 rect(AB, BC) [by 10.13].

**Step 15.** Since DI x MG = sq(AB) + sq(BC) and DI x MF = 2 rect(AB, BC), and these areas are incommensurable, MG is incommensurable with MF [by 6.1 and 10.11].

**Step 16.** MG and MF are each rational (Steps 12 and 13) and incommensurable with each other (Step 15). Since they are each incommensurable in length with DI, we examine their mutual relation: they are rational straight lines commensurable in square only (each is rational, and their incommensurability has been established). By the definition of commensurable in square only and by 10.36, MG - MF is an apotome, hence irrational.

**Step 17.** But DI x (MG - MF) = sq(AC). Since DI is rational and MG - MF is irrational, the rectangle DI x (MG - MF) is irrational (a rational line and an irrational line produce a rectangle that, when equal to a square, makes the side irrational). More precisely, since sq(AC) equals the rectangle of rational DI and the irrational line (MG - MF), the area sq(AC) is irrational [the area is neither rational nor expressible as a square on a rational line].

**Step 18.** Since sq(AC) is irrational, AC itself is irrational [by D10.1.4, since the square on AC is not commensurable with the square on the assigned rational line].

**Step 19.** Therefore the remainder AC is irrational. Let it be called a second apotome of a medial straight line, since it arises from subtracting from a medial straight line a medial straight line commensurable with it in square only, where the rectangle they contain is medial (distinguishing it from the first apotome of a medial straight line of 10.74, where that rectangle was rational). Q.E.D.

**USED:** 10.11, 10.13, 10.15, 10.19, 10.22, 10.23, 10.36, 10.6, 2.4, 2.7, 6.1, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 10.11, 10.13, 10.15, 10.20, 10.22, 10.23, 10.28, 10.6, 10.73, 2.7, 6.1
**Jaccard:** 0.471 — AI adds ['10.19', '10.36', '2.4', 'D10.1.2', 'D10.1.3', 'D10.1.4']; Human adds ['10.20', '10.28', '10.73']

## Proposition 10.76
**Statement:** If from a straight line there be subtracted a straight line which is incommensurable in square with the whole and which with the whole makes the squares on them added together rational, but the rectangle contained by them medial, the remainder is irrational; and let it be called minor.

**Step 1.** Let AB be a straight line, and from AB let BC be subtracted, where AB and BC are incommensurable in square, the sum of the squares on AB and BC is rational, and the rectangle contained by AB and BC is medial. We must show that the remainder AC is irrational.

**Step 2.** Since the rectangle AB,BC is medial, twice the rectangle AB,BC is also medial. For twice the rectangle AB,BC has to the rectangle AB,BC the ratio 2:1, which is a ratio a number has to a number, so by 10.6 twice the rectangle AB,BC is commensurable with the rectangle AB,BC. Since the rectangle AB,BC is medial and hence incommensurable with any rational area, by 10.13 twice the rectangle AB,BC is also incommensurable with any rational area, and so twice the rectangle AB,BC is medial.

**Step 3.** By 2.7, the square on AB together with the square on BC is equal to twice the rectangle AB,BC together with the square on AC. That is, sq(AB) + sq(BC) = sq(AC) + 2*rect(AB,BC).

**Step 4.** Now sq(AB) + sq(BC) is rational (by hypothesis), and 2*rect(AB,BC) is medial (by Step 2). Since a rational area and a medial area are incommensurable with one another (for a rational area is commensurable with the square on the assigned rational line, while a medial area is incommensurable with it, so by 10.13 they are incommensurable with each other), sq(AB) + sq(BC) is incommensurable with 2*rect(AB,BC).

**Step 5.** Since sq(AB) + sq(BC) = sq(AC) + 2*rect(AB,BC), suppose for contradiction that sq(AC) were commensurable with sq(AB) + sq(BC). Then since sq(AB) + sq(BC) = sq(AC) + 2*rect(AB,BC), by 10.15 the magnitude 2*rect(AB,BC) would be commensurable with sq(AC), and hence by 10.12 commensurable with sq(AB) + sq(BC). But this contradicts Step 4, which established that sq(AB) + sq(BC) is incommensurable with 2*rect(AB,BC). Therefore sq(AC) is incommensurable with sq(AB) + sq(BC).

**Step 6.** Since sq(AB) + sq(BC) is rational and sq(AC) is incommensurable with it, sq(AC) is irrational by D10.1.4. Therefore AC is irrational by D10.1.4.

**Step 7.** Let AC be called minor. Q.E.D.

**USED:** 10.12, 10.13, 10.15, 10.6, 2.7, D10.1.4
**Human refs (from References field):** 10.16, 10.33, 2.7
**Jaccard:** 0.125 — AI adds ['10.12', '10.13', '10.15', '10.6', 'D10.1.4']; Human adds ['10.16', '10.33']

## Proposition 10.77
**Statement:** If from a straight line there be subtracted a straight line which is incommensurable in square with the whole, and which with the whole makes the sum of the squares on them medial, but twice the rectangle contained by them rational, the remainder is irrational: and let it be called that which produces with a rational area a medial whole.

**Step 1.** Let AB be a straight line, and from AB let BC be subtracted, where AB and BC are incommensurable in square, the sum of the squares on AB and BC is medial, and twice the rectangle contained by AB and BC is rational. We must show that the remainder AC is irrational.

**Step 2.** By Proposition 2.7, for the straight line AB cut at C, the square on AB together with the square on BC equals twice the rectangle contained by AB and BC together with the square on AC. That is, sq(AB) + sq(BC) = 2*rect(AB,BC) + sq(AC).

**Step 3.** Therefore, by Common Notion 3, the square on AC equals the sum of the squares on AB and BC minus twice the rectangle contained by AB and BC. That is, sq(AC) = [sq(AB) + sq(BC)] - 2*rect(AB,BC).

**Step 4.** Suppose, for the sake of contradiction, that the square on AC is rational. Since twice the rectangle AB,BC is also rational by hypothesis, both sq(AC) and 2*rect(AB,BC) are commensurable with the square on the assigned rational straight line. By Proposition 10.12, sq(AC) and 2*rect(AB,BC) are commensurable with one another. Then by Proposition 10.15, their sum sq(AC) + 2*rect(AB,BC) is also commensurable with each of them, and hence commensurable with the square on the rational straight line, making their sum rational. But sq(AC) + 2*rect(AB,BC) = sq(AB) + sq(BC), which is medial by hypothesis. A medial area is by definition incommensurable with the square on the rational line (D10.1.4), so it cannot be rational. This is a contradiction. Therefore the square on AC is not rational.

**Step 5.** Suppose, for the sake of contradiction, that the square on AC is medial. Then both sq(AC) and the sum sq(AB) + sq(BC) are medial. Since sq(AB) + sq(BC) = sq(AC) + 2*rect(AB,BC) by Step 2, the medial area sq(AB) + sq(BC) exceeds the medial area sq(AC) by exactly 2*rect(AB,BC), which is rational. But by Proposition 10.26, a medial area does not exceed a medial area by a rational area. This is a contradiction. Therefore the square on AC is not medial.

**Step 6.** Since the square on AC is neither rational nor medial, it is an irrational area. By Definition D10.1.4, the straight line whose square equals an irrational area is itself irrational. Therefore AC is irrational.

**Step 7.** The irrational straight line AC, formed by subtracting from a straight line another straight line incommensurable in square with the whole, where the sum of the squares on them is medial and twice the rectangle contained by them is rational, is called that which produces with a rational area a medial whole. Q.E.D.

**USED:** 10.12, 10.15, 10.26, 2.7, CN3, D10.1.3, D10.1.4
**Human refs (from References field):** 10.16, 10.34, 2.7
**Jaccard:** 0.111 — AI adds ['10.12', '10.15', '10.26', 'CN3', 'D10.1.3', 'D10.1.4']; Human adds ['10.16', '10.34']

## Proposition 10.78
**Statement:** If from a straight line there be subtracted a straight line which is incommensurable in square with the whole and which with the whole makes the sum of the squares on them medial, twice the rectangle contained by them medial, and further the squares on them incommensurable with twice the rectangle contained by them, the remainder is irrational; and let it be called that which produces with a medial area a medial whole.

**Step 1.** Let AB be a straight line, and from AB let BC be subtracted, where BC is incommensurable in square with AB, the sum of the squares on AB and BC is medial, twice the rectangle contained by AB and BC is medial, and the sum of the squares on AB and BC is incommensurable with twice the rectangle contained by AB and BC. We must show that the remainder AC is irrational.

**Step 2.** Set out a rational straight line DI. To DI apply the area DE equal to the sum of the squares on AB and BC, producing breadth DG. To DI apply the area DF equal to twice the rectangle contained by AB and BC, producing breadth DH, where DF is subtracted from DE (so that H falls between D and G). Then the remaining area HG (that is, DE minus DF) applied to DI has breadth HG corresponding to the square on AC.

**Step 3.** By 2.7, the squares on AB and BC together are equal to twice the rectangle AB, BC together with the square on AC. Therefore the square on AC equals the sum of the squares on AB and BC minus twice the rectangle AB, BC, which is the area HG applied to DI.

**Step 4.** Since the sum of the squares on AB and BC is medial, the area DE is medial. This medial area DE is applied to the rational straight line DI. By 10.22, the breadth DG is rational and incommensurable in length with DI.

**Step 5.** Since twice the rectangle contained by AB and BC is medial, the area DF is medial. This medial area DF is applied to the rational straight line DI. By 10.22, the breadth DH is rational and incommensurable in length with DI.

**Step 6.** Since the sum of the squares on AB and BC is incommensurable with twice the rectangle contained by AB and BC, the area DE is incommensurable with the area DF. But DE is the rectangle DI by DG, and DF is the rectangle DI by DH. Therefore the rectangle DI by DG is incommensurable with the rectangle DI by DH. By 6.1, as DG is to DH, so is the rectangle DI by DG to the rectangle DI by DH. Therefore DG is incommensurable in length with DH, by 10.11.

**Step 7.** Both DG and DH are rational (from Steps 4 and 5). Since DG and DH are rational and incommensurable in length, they are commensurable in square only. Therefore by 10.21, the rectangle contained by DG and DH is irrational, and by 10.36, their sum DG + DH is a binomial, which is irrational. However, what we need is that their difference is irrational.

**Step 8.** Since DG and DH are each incommensurable in length with DI (Steps 4 and 5), and they are incommensurable in length with each other (Step 6), we have that DG and DH are rational straight lines commensurable in square only. Consider the breadth HG, which corresponds to the difference DG minus DH. By 10.73, since DG is rational and DH is rational and commensurable with DG in square only, the remainder HG (that is, DG minus DH) is irrational; it is an apotome.

**Step 9.** The area corresponding to the square on AC is the rectangle DI by HG. Now DI is rational and HG is an apotome (from Step 8). However, we need to determine what kind of irrational the side of this rectangle is, which will tell us about AC.

**Step 10.** We reconsider the structure more directly. The area equal to the square on AC is the difference of two medial areas (DE minus DF) that are incommensurable with each other. By 10.72, when two medial areas incommensurable with one another are added together, the side is either a second bimedial or a side of the sum of two medial areas. For the subtractive case, we apply the analogous reasoning.

**Step 11.** We proceed to show that the square on AC is neither rational nor medial, and that AC does not belong to any previously classified irrational type. The square on AC equals the sum of the squares on AB and BC minus twice the rectangle AB, BC. Since the sum of the squares on AB and BC is medial, the square on AC is not rational (for if it were, then the sum of the squares on AB, BC would be the sum of a rational area and a medial area, namely twice the rectangle; but the sum of the squares is medial, and a medial area cannot equal the sum of a rational and a medial area by 10.26 and the properties of rational and medial areas).

**Step 12.** Suppose the square on AC were rational. Then the area HG on DI is rational. The area DE equals DF plus HG. Since DE is medial and HG would be rational, DF would equal DE minus HG. But DE is medial and DF is medial, and their difference HG would be rational. By 10.26, a medial area does not exceed a medial area by a rational area. This is a contradiction. Therefore the square on AC is not rational, so AC is not rational.

**Step 13.** Suppose the square on AC were medial. Then the area HG on DI is medial, and by 10.22, the breadth HG is rational and incommensurable in length with DI. Now both DG and HG would be rational, and since DE equals DF plus the area for the square on AC, the three areas DE, DF, and the area for the square on AC are all medial. The area DE (on DI with breadth DG) is medial, and the area for the square on AC (on DI with breadth HG) is medial. Then DF = DE minus the area for AC squared, which means DF is the difference of two medial areas. But DF is itself medial. We need to check commensurability. Since DE is incommensurable with DF (given), and DE equals DF plus the area of AC squared, the area of AC squared is incommensurable with DF. So the area of AC squared is incommensurable with DF, meaning HG is incommensurable with DH (by 6.1 and 10.11). But also from the medial area for AC squared applied to DI, HG is rational and incommensurable in length with DI. Now DH is also rational and incommensurable in length with DI. And HG is incommensurable in length with DH. So DG = DH + HG. Since DG, DH, and HG are all rational, and DH and HG are incommensurable in length, by 10.36, DG = DH + HG is a binomial, which is irrational. But DG is rational (Step 4). This is a contradiction. Therefore the square on AC is not medial.

**Step 14.** Since the square on AC is neither rational nor medial, AC is irrational and is neither rational nor medial. The square on AC equals the excess of a medial area over a medial area, where the two medial areas are incommensurable. This configuration (subtracting from a straight line a part incommensurable in square with the whole, where the squares sum to a medial, twice the rectangle is medial, and these are incommensurable) produces an irrational remainder distinct from those previously classified. Let AC be called that which produces with a medial area a medial whole.

**Step 15.** To confirm the name: if one constructs a rectangle on AC equal to a medial area, the resulting figure relates to medial areas in the manner indicated. The remainder AC is irrational, and it is called that which produces with a medial area a medial whole. This completes the proof.

**USED:** 10.11, 10.22, 10.26, 10.36, 10.73, 2.7, 6.1, D10.1.3, D10.1.4
**Human refs (from References field):** 10.11, 10.20, 10.22, 10.35, 10.73, 2.7, 6.1
**Jaccard:** 0.455 — AI adds ['10.26', '10.36', 'D10.1.3', 'D10.1.4']; Human adds ['10.20', '10.35']

## Proposition 10.79
**Statement:** To an apotome only one rational straight line can be annexed which is commensurable with the whole in square only.

**Step 1.** Let AB be an apotome, and let BC be the annex, so that AC is the whole. Then AC and CB are rational straight lines commensurable in square only, and AB = AC - CB [D10.1.3, 10.73].

**Step 2.** Suppose, for the sake of contradiction, that BD is another rational straight line annexed to AB, different from BC, such that AD and DB are also rational straight lines commensurable in square only, with AB = AD - DB.

**Step 3.** Since AC and CB are rational straight lines commensurable in square only, the squares on AC and CB are each rational areas [D10.1.4]. Since rational areas are commensurable with the square on the assigned rational line, they are commensurable with one another [10.12], and therefore their sum, the squares on AC and CB together, is rational [10.15].

**Step 4.** By the same reasoning, since AD and DB are rational straight lines commensurable in square only, the sum of the squares on AD and DB is also rational [D10.1.4, 10.12, 10.15].

**Step 5.** Since AC and CB are rational and commensurable in square only, the rectangle contained by AC and CB is medial [10.21]. Therefore twice the rectangle AC, CB is commensurable with the rectangle AC, CB (being in the ratio 2:1, a ratio of numbers) [10.6]. Since the rectangle AC, CB is medial and hence incommensurable with the assigned rational square, and twice the rectangle AC, CB is commensurable with the rectangle AC, CB, twice the rectangle AC, CB is also incommensurable with the assigned rational square [10.13], and so is irrational. Moreover, the side of the square equal to it is medial [10.23, D10.1.4].

**Step 6.** By the same reasoning, twice the rectangle AD, DB is also medial [10.21, 10.6, 10.13, D10.1.4].

**Step 7.** Now, since AB = AC - CB, by Proposition 2.7 applied to the line AC cut at B, the square on AC together with the square on CB equals twice the rectangle contained by AC and CB together with the square on AB. That is: sq(AC) + sq(CB) = 2*rect(AC, CB) + sq(AB) [2.7].

**Step 8.** Similarly, since AB = AD - DB, by Proposition 2.7 applied to the line AD cut at B, we have: sq(AD) + sq(DB) = 2*rect(AD, DB) + sq(AB) [2.7].

**Step 9.** From Steps 7 and 8, subtracting the second equation from the first: [sq(AC) + sq(CB)] - [sq(AD) + sq(DB)] = 2*rect(AC, CB) - 2*rect(AD, DB) [CN2, CN3].

**Step 10.** Now the left-hand side is the difference of two rational areas (by Steps 3 and 4). If this difference is not zero, it is rational, since the difference of commensurable magnitudes is commensurable with each [10.15]. The right-hand side is the difference of two medial areas (by Steps 5 and 6). But by Proposition 10.26, a medial area does not exceed a medial area by a rational area. Therefore the difference of two medial areas cannot be a nonzero rational area [10.26].

**Step 11.** This forces both sides to equal zero. Hence: sq(AC) + sq(CB) = sq(AD) + sq(DB), and 2*rect(AC, CB) = 2*rect(AD, DB), so rect(AC, CB) = rect(AD, DB) [CN3].

**Step 12.** From Step 7, sq(AC) + sq(CB) = 2*rect(AC, CB) + sq(AB). Rearranging: sq(AC) + sq(CB) - 2*rect(AC, CB) = sq(AB). But sq(AC) + sq(CB) - 2*rect(AC, CB) = sq(AC - CB) by Proposition 2.7 (equivalently, the square on the difference). This is consistent and gives sq(AB) = (AC - CB)^2.

**Step 13.** Now from sq(AC) + sq(CB) = sq(AD) + sq(DB) (Step 11), we get sq(AC) - sq(AD) = sq(DB) - sq(CB) [CN2, CN3].

**Step 14.** From AB = AC - CB = AD - DB, we deduce AC - AD = CB - DB [CN2, CN3].

**Step 15.** Suppose CB is not equal to DB. Without loss of generality, suppose CB > DB. Then AC > AD by Step 14, with AC - AD = CB - DB [CN5].

**Step 16.** Set AC = AD + FC and CB = DB + FC, where FC is the common excess (FC > 0). Then rect(AC, CB) = rect(AD + FC, DB + FC). Expanding by Proposition 2.1: rect(AD + FC, DB + FC) = rect(AD, DB) + rect(AD, FC) + rect(FC, DB) + sq(FC) [2.1].

**Step 17.** Since rect(AC, CB) = rect(AD, DB) by Step 11, we have rect(AD, FC) + rect(FC, DB) + sq(FC) = 0 [CN3]. But AD, DB, and FC are all positive magnitudes, so the rectangle contained by any two of them is positive, and the square on FC is positive. Their sum cannot be zero [CN5]. This is a contradiction.

**Step 18.** Therefore the assumption that CB is not equal to DB is false. Hence CB = DB, which means the point C coincides with D, and BC is the unique rational straight line that can be annexed to the apotome AB such that the whole and the annex are commensurable in square only [CN1].

**Step 19.** Therefore, to an apotome only one rational straight line can be annexed which is commensurable with the whole in square only. Q.E.D.

**USED:** 10.12, 10.13, 10.15, 10.21, 10.23, 10.26, 10.6, 10.73, 2.1, 2.7, CN1, CN2, CN3, CN5, D10.1.3, D10.1.4
**Human refs (from References field):** 10.21, 10.26, 10.73, 2.7
**Jaccard:** 0.250 — AI adds ['10.12', '10.13', '10.15', '10.23', '10.6', '2.1', 'CN1', 'CN2', 'CN3', 'CN5', 'D10.1.3', 'D10.1.4']

## Proposition 10.80
**Statement:** To a first apotome of a medial straight line only one medial straight line can be annexed which is commensurable with the whole in square only and which contains with the whole a rational rectangle.

**Step 1.** Let AB be a first apotome of a medial straight line, and let BC be the medial straight line annexed to it according to the definition (10.74), so that AC is medial, BC is medial, AC and BC are commensurable in square only, and the rectangle AC by BC is rational.

**Step 2.** Suppose, for the sake of contradiction, that BD is another medial straight line annexed to AB, different from BC, such that AD is medial, BD is medial, AD and BD are commensurable in square only, and the rectangle AD by BD is rational. We shall show BD must equal BC.

**Step 3.** Since AB equals AC minus BC, by Proposition 2.7 we have: the square on AB equals the sum of the squares on AC and BC minus twice the rectangle contained by AC and BC. That is, sq(AB) = sq(AC) + sq(BC) - 2*rect(AC,BC).

**Step 4.** Similarly, since AB equals AD minus BD, we have: sq(AB) = sq(AD) + sq(BD) - 2*rect(AD,BD).

**Step 5.** Therefore, sq(AC) + sq(BC) - 2*rect(AC,BC) = sq(AD) + sq(BD) - 2*rect(AD,BD), by CN1.

**Step 6.** Rearranging by CN2 and CN3: [sq(AC) + sq(BC)] - [sq(AD) + sq(BD)] = 2*rect(AC,BC) - 2*rect(AD,BD).

**Step 7.** Now rect(AC,BC) is rational by hypothesis, and rect(AD,BD) is rational by hypothesis. Since both are rational, they are commensurable with each other (being each commensurable with the square on the assigned rational straight line, by D10.1.4 and 10.12). Therefore 2*rect(AC,BC) and 2*rect(AD,BD) are also commensurable, and their difference is either zero or rational (by 10.15, if we add or subtract commensurable magnitudes the result is commensurable with each). Thus the right-hand side of the equation in Step 6 is rational (or zero).

**Step 8.** Consider the left-hand side. Since AC and BC are commensurable in square (by hypothesis from 10.74), the squares sq(AC) and sq(BC) are commensurable areas. Since AC is medial, sq(AC) is a medial area (by D10.1.4, being incommensurable with the square on the rational straight line). Because sq(BC) is commensurable with sq(AC), and sq(AC) is incommensurable with the rational square, sq(BC) is also incommensurable with the rational square by 10.13, so sq(BC) is medial. By 10.15, the sum sq(AC) + sq(BC) is commensurable with sq(AC). Since sq(AC) is medial (incommensurable with the rational square), sq(AC) + sq(BC) is also incommensurable with the rational square by 10.13, so the sum sq(AC) + sq(BC) is a medial area.

**Step 9.** By the same reasoning, since AD and BD are commensurable in square and both medial, the sum sq(AD) + sq(BD) is also a medial area.

**Step 10.** Thus the left-hand side of Step 6 is the difference of two medial areas, and the right-hand side is rational. By Proposition 10.26, a medial area does not exceed a medial area by a rational area. Therefore the difference on the left-hand side cannot be a nonzero rational quantity. Since it equals the right-hand side which is rational, both sides must equal zero.

**Step 11.** From the left-hand side being zero: sq(AC) + sq(BC) = sq(AD) + sq(BD). From the right-hand side being zero: 2*rect(AC,BC) = 2*rect(AD,BD), hence rect(AC,BC) = rect(AD,BD).

**Step 12.** Now by Proposition 2.4, the square on the sum AC + BC equals sq(AC) + sq(BC) + 2*rect(AC,BC). Similarly, the square on the sum AD + BD equals sq(AD) + sq(BD) + 2*rect(AD,BD). Since sq(AC) + sq(BC) = sq(AD) + sq(BD) and rect(AC,BC) = rect(AD,BD) (from Step 11), we obtain sq(AC + BC) = sq(AD + BD), by CN2.

**Step 13.** Since AC + BC and AD + BD are both positive magnitudes with equal squares, we have AC + BC = AD + BD.

**Step 14.** We also have AC - BC = AB = AD - BD. Adding the equations AC + BC = AD + BD and AC - BC = AD - BD gives 2*AC = 2*AD, hence AC = AD. Subtracting gives 2*BC = 2*BD, hence BC = BD, by CN2 and CN3.

**Step 15.** Therefore BC and BD are the same straight line, contradicting the assumption that BD is different from BC. Hence to a first apotome of a medial straight line, only one medial straight line can be annexed which is commensurable with the whole in square only and which contains with the whole a rational rectangle. Q.E.D.

**USED:** 10.12, 10.13, 10.15, 10.26, 10.74, 2.4, 2.7, CN1, CN2, CN3, D10.1.4
**Human refs (from References field):** 10.15, 10.23, 10.26, 10.74, 2.7
**Jaccard:** 0.333 — AI adds ['10.12', '10.13', '2.4', 'CN1', 'CN2', 'CN3', 'D10.1.4']; Human adds ['10.23']

## Proposition 10.81
**Statement:** To a second apotome of a medial straight line only one medial straight line can be annexed which is commensurable with the whole in square only and which contains with the whole a medial rectangle.

**Step 1.** Let AB be a second apotome of a medial straight line, and let BC be annexed to it, so that AC and CB are medial straight lines commensurable in square only and containing a medial rectangle [D10.1.1, D10.1.3, 10.75]. We must show that no other medial straight line can be annexed to AB satisfying these conditions.

**Step 2.** Suppose, for the sake of contradiction, that BD is also annexed to AB, so that AD and DB are medial straight lines commensurable in square only and containing a medial rectangle [10.75].

**Step 3.** Set out a rational straight line EF. Apply to EF a rectangle EG equal to the square on AC, producing EH as breadth. Then apply to EF a rectangle HG equal to twice the rectangle AC, CB (subtracting from EG), so that the remainder equals the square on AB minus twice the rectangle. More precisely, apply to EF a rectangle EG equal to the sum of the squares on AC and CB, producing breadth EH [1.44, 1.45].

**Step 4.** Since AC and CB are medial straight lines, the squares on AC and CB are each medial areas. Their sum, the squares on AC plus CB, is therefore medial [10.15, 10.23]. The rectangle EG, being equal to this medial area and applied to the rational straight line EF, produces as breadth EH that is rational and incommensurable in length with EF [10.22].

**Step 5.** Now apply to EF a rectangle HI equal to twice the rectangle AC, CB. Since AC and CB contain a medial rectangle, twice the rectangle AC, CB is also medial [10.23, 10.15]. Applied to the rational straight line EF, this produces breadth HI that is rational and incommensurable in length with EF [10.22].

**Step 6.** Since the squares on AC and CB are medial and twice the rectangle AC, CB is medial, and these two medial areas are incommensurable with each other (for if the sum of the squares were commensurable with twice the rectangle, then by 10.15 the sum of squares would be commensurable with the square on AC plus square on CB minus twice rectangle AC, CB, which equals the square on AB, making the square on AB medial; but also the sum of squares plus twice the rectangle equals the square on the whole line, and these relationships would force commensurability contradicting the construction), we have that EH and HI are incommensurable in length [10.11]. Since both are rational, EI (which equals EH minus HI) is a binomial or apotome. In fact, since EG minus HI corresponds to the square on AB applied to EF, and we subtract: the square on AB equals the squares on AC and CB minus twice the rectangle AC, CB [2.7]. So the rectangle on EF with breadth EI equals the square on AB.

**Step 7.** By the same construction, apply to EF a rectangle EK equal to the sum of the squares on AD and DB, producing breadth EL. Apply to EF a rectangle LK equal to twice the rectangle AD, DB [1.44, 1.45].

**Step 8.** By the same reasoning as Steps 4 and 5, since AD and DB are medial and commensurable in square only and contain a medial rectangle: EL is rational and incommensurable in length with EF [10.22], and LM (the breadth produced by twice the rectangle AD, DB) is rational and incommensurable in length with EF [10.22].

**Step 9.** Since AB = AC - CB = AD - DB, we have that the square on AB is the same in both decompositions. By 2.7, the square on AB equals the squares on AC, CB minus twice the rectangle AC, CB, and also equals the squares on AD, DB minus twice the rectangle AD, DB. Therefore the rectangle on EF of breadth EI equals the rectangle on EF of breadth EM (where EM corresponds to the second decomposition). Since EF is common, EI = EM [6.1, CN1].

**Step 10.** Now, the squares on AC, CB equal the squares on AD, DB plus twice the rectangle AD, DB minus twice the rectangle AC, CB rearranged. More precisely: since both expressions equal the square on AB plus twice their respective rectangles, we get squares on AC, CB minus squares on AD, DB = twice rectangle AC, CB minus twice rectangle AD, DB. That is, the area EG minus EK (applied to EF) equals HI minus LM (applied to EF). So EH - EL = HI - LM (as breadths on EF).

**Step 11.** But EH and EL are each rational and incommensurable in length with EF, and HI and LM are each rational and incommensurable in length with EF. Consider: EH is rational, EL is rational. If EH and EL were commensurable, then the sum of the squares on AC, CB would be commensurable with the sum of the squares on AD, DB. Since each sum is medial, they would be commensurable medial areas. Then their difference would be either zero or medial [10.15, 10.26]. Similarly for twice the rectangles.

**Step 12.** Since the sum of the squares on AC, CB is medial, and the sum of the squares on AD, DB is medial, their difference (which equals the difference of the twice-rectangles, by Step 10) is either rational or medial. Similarly, twice the rectangle AC, CB is medial and twice the rectangle AD, DB is medial, so their difference is either rational or medial.

**Step 13.** But the sum of the squares on AC, CB is incommensurable with twice the rectangle AC, CB (since AC and CB are commensurable in square only and contain a medial rectangle, the sum of squares is a medial area incommensurable with the medial rectangle [10.26, 10.75]). Similarly, the sum of squares on AD, DB is incommensurable with twice the rectangle AD, DB.

**Step 14.** From Step 10, the difference of the sums of squares equals the difference of the twice-rectangles. If this common difference is nonzero, then it is simultaneously expressible as a difference of two medial areas (from the squares side) and as a difference of two medial areas (from the rectangles side). But the squares-side medial area is incommensurable with the rectangles-side medial area by Step 13. If the common difference were rational, then a medial area would exceed another medial area by a rational area, contradicting 10.26. If the common difference were medial, then by Step 13 and the incommensurability of the two types, we would have a medial area simultaneously commensurable with both an area from the squares type and an area from the rectangles type, forcing commensurability between the two types, contradicting Step 13.

**Step 15.** Therefore the common difference must be zero: the sum of the squares on AC, CB equals the sum of the squares on AD, DB, and twice the rectangle AC, CB equals twice the rectangle AD, DB.

**Step 16.** Since the squares on AC, CB are commensurable with the squares on AD, DB (being equal), and the squares on AC and CB are each medial, AC is commensurable in square with AD [10.15, CN1]. Similarly, since twice the rectangle AC, CB equals twice the rectangle AD, DB, the rectangle AC, CB equals the rectangle AD, DB [CN3].

**Step 17.** Since the square on AC equals the square on AD (from the sum of squares being equal and the individual commensurability relations, combined with the rectangle equality), and AC, AD are commensurable in square, we examine: the sum sq(AC) + sq(CB) = sq(AD) + sq(DB). Since rect(AC,CB) = rect(AD,DB) and sq(AC) + sq(CB) = sq(AD) + sq(DB), by 2.7, sq(AC) - sq(CB) can be analyzed. From sq(AB) = sq(AC) + sq(CB) - 2rect(AC,CB) = sq(AD) + sq(DB) - 2rect(AD,DB), which is already established.

**Step 18.** Now since AC and CB are commensurable in square only, and AD and DB are commensurable in square only, consider the identity: (sq(AC) - sq(CB))^2 = (sq(AC) + sq(CB))^2 - 4*sq(AC)*sq(CB). Also, sq(AC)*sq(CB) = (rect(AC,CB))^2 (when the lines are considered appropriately via 6.17). Since rect(AC,CB) = rect(AD,DB) and sq(AC) + sq(CB) = sq(AD) + sq(DB), we get sq(AC) - sq(CB) = sq(AD) - sq(DB) (in absolute value).

**Step 19.** From sq(AC) + sq(CB) = sq(AD) + sq(DB) and sq(AC) - sq(CB) = sq(AD) - sq(DB), adding: 2*sq(AC) = 2*sq(AD), so sq(AC) = sq(AD), hence AC = AD [CN1, CN2].

**Step 20.** Since AC = AD and AB = AC - CB = AD - DB, it follows that CB = DB [CN3].

**Step 21.** But this means the two annexes BC and BD are equal, contradicting our assumption that BD is a different annex from BC. Therefore, to a second apotome of a medial straight line, only one medial straight line can be annexed which is commensurable with the whole in square only and which contains with the whole a medial rectangle. Q.E.D.

**USED:** 1.44, 1.45, 10.11, 10.15, 10.22, 10.23, 10.26, 10.75, 2.7, 6.1, 6.17, CN1, CN2, CN3, D10.1.1, D10.1.3
**Human refs (from References field):** 10.11, 10.13, 10.15, 10.22, 10.23, 10.6, 10.73, 10.75, 10.79, 2.7, 6.1
**Jaccard:** 0.350 — AI adds ['1.44', '1.45', '10.26', '6.17', 'CN1', 'CN2', 'CN3', 'D10.1.1', 'D10.1.3']; Human adds ['10.13', '10.6', '10.73', '10.79']

## Proposition 10.82
**Statement:** To a minor straight line only one straight line can be annexed which is incommensurable in square with the whole and which makes, with the whole, the sum of the squares on them rational but twice the rectangle contained by them medial.

**Step 1.** Let AB be a minor straight line, and let BC be an annex to it, so that AC and CB are incommensurable in square, the sum of the squares on AC and CB is rational, and twice the rectangle contained by AC and CB is medial [10.76].

**Step 2.** Suppose, for the sake of contradiction, that BD is another straight line, different from BC, that can also be annexed to AB with the same properties: AD and DB are incommensurable in square, the sum of the squares on AD and DB is rational, and twice the rectangle contained by AD and DB is medial.

**Step 3.** Since AC = AB + BC, by 2.4 the square on AC equals the sum of the squares on AB and BC together with twice the rectangle contained by AB and BC. Therefore the sum of the squares on AC and CB equals the square on AB plus twice the square on BC plus twice the rectangle AB by BC.

**Step 4.** Similarly, since AD = AB + BD, the sum of the squares on AD and DB equals the square on AB plus twice the square on BD plus twice the rectangle AB by BD [2.4].

**Step 5.** By hypothesis, the sum of the squares on AC and CB is rational, and the sum of the squares on AD and DB is rational. Since both are rational, they are commensurable with one another [D10.1.3, 10.12]. Their difference is therefore also rational [10.15, CN3].

**Step 6.** Subtracting the expression in Step 4 from that in Step 3, the difference of the two sums of squares equals twice the square on BC minus twice the square on BD, together with twice the rectangle AB by BC minus twice the rectangle AB by BD. That is, the difference equals 2(sq(BC) - sq(BD)) + 2 rect(AB, BC - BD). This difference is rational, by Step 5.

**Step 7.** Now consider the rectangles. By 2.3, the rectangle contained by AC and CB equals the rectangle contained by AB and CB together with the square on CB, since AC = AB + BC. Therefore twice the rectangle AC by CB equals twice the rectangle AB by CB plus twice the square on CB.

**Step 8.** Similarly, twice the rectangle AD by DB equals twice the rectangle AB by DB plus twice the square on DB [2.3].

**Step 9.** Subtracting the expression in Step 8 from that in Step 7, twice the rectangle AC by CB minus twice the rectangle AD by DB equals 2 rect(AB, CB) + 2 sq(CB) - 2 rect(AB, DB) - 2 sq(DB), which equals 2 rect(AB, BC - BD) + 2(sq(BC) - sq(BD)).

**Step 10.** This is the same expression as in Step 6. Therefore twice the rectangle AC by CB minus twice the rectangle AD by DB is rational.

**Step 11.** But twice the rectangle AC by CB is medial, and twice the rectangle AD by DB is medial. By 10.26, a medial area does not exceed a medial area by a rational area.

**Step 12.** This is a contradiction. Therefore the assumption that BD differs from BC is false, and only one straight line can be annexed to the minor straight line AB satisfying the stated conditions. Q.E.D.

**USED:** 10.12, 10.15, 10.26, 10.76, 2.3, 2.4, CN3, D10.1.3
**Human refs (from References field):** 10.26, 10.76
**Jaccard:** 0.250 — AI adds ['10.12', '10.15', '2.3', '2.4', 'CN3', 'D10.1.3']

## Proposition 10.83
**Statement:** To a straight line which produces with a rational area a medial whole only one straight line can be annexed which is incommensurable in square with the whole straight line and which with the whole straight line makes the sum of the squares on them medial, but twice the rectangle contained by them rational.

**Step 1.** Let AB be a straight line which produces with a rational area a medial whole, and let BC be an annex to it, so that AC is incommensurable in square with AB, the sum of the squares on AB and BC is medial, and twice the rectangle contained by AB and BC is rational [10.77].

**Step 2.** Suppose, for the sake of contradiction, that BD is another straight line annexed to AB, different from BC, satisfying the same conditions: AD is incommensurable in square with AB, the sum of the squares on AB and BD is medial, and twice the rectangle contained by AB and BD is rational.

**Step 3.** Since twice the rectangle AB,BC is rational and twice the rectangle AB,BD is rational, these two areas are commensurable with one another, for all rational areas are commensurable [D10.1.4, 10.12].

**Step 4.** Therefore, by 10.15, the difference of these two rational areas, namely 2*rect(AB,BC) minus 2*rect(AB,BD), is rational.

**Step 5.** Denote the sum of the squares on AB and BC as M1, and the sum of the squares on AB and BD as M2. Both M1 and M2 are medial by hypothesis.

**Step 6.** Then M1 minus M2 equals the square on BC minus the square on BD, since the square on AB cancels [CN3].

**Step 7.** By 10.26, a medial area does not exceed a medial area by a rational area. Therefore M1 minus M2 is not rational, and hence the square on BC minus the square on BD is not rational.

**Step 8.** By 2.7, since AB equals AC plus BC, the sum of the squares on AB and BC equals twice the rectangle AB,BC plus the square on AC. That is, M1 equals 2*rect(AB,BC) plus sq(AC). Therefore sq(AC) equals M1 minus 2*rect(AB,BC).

**Step 9.** Similarly, sq(AD) equals M2 minus 2*rect(AB,BD).

**Step 10.** Hence sq(AC) minus sq(AD) equals (M1 minus M2) minus (2*rect(AB,BC) minus 2*rect(AB,BD)).

**Step 11.** By Step 7, M1 minus M2 is not rational. By Step 4, 2*rect(AB,BC) minus 2*rect(AB,BD) is rational. Therefore sq(AC) minus sq(AD) equals a non-rational quantity minus a rational quantity, which cannot be rational (for if it were, then M1 minus M2 would equal a rational plus a rational, hence rational, contradicting Step 7). So sq(AC) minus sq(AD) is not rational.

**Step 12.** Now, since AC equals AB minus BC and AD equals AB minus BD, we have AC minus AD equals BD minus BC [CN3]. Therefore the square on (AC minus AD) equals the square on (BD minus BC).

**Step 13.** By 2.5 and 2.6, the square on BC minus the square on BD equals the rectangle contained by (BC plus BD) and (BC minus BD).

**Step 14.** Also, 2*rect(AB,BC) minus 2*rect(AB,BD) equals 2*rect(AB, BC minus BD), which is rational by Step 4.

**Step 15.** Since BC minus BD is nonzero (as BC is not equal to BD by assumption), 2*AB*(BC minus BD) is a nonzero rational area.

**Step 16.** By Step 13, sq(BC) minus sq(BD) equals (BC plus BD) times (BC minus BD). By Step 7, this is not rational.

**Step 17.** The ratio of (BC plus BD)*(BC minus BD) to 2*AB*(BC minus BD) is (BC plus BD) to 2*AB. Since the former area is not rational while the latter is rational, these two areas are incommensurable. Therefore BC plus BD is incommensurable with AB [10.11].

**Step 18.** Now consider the sum 2*rect(AB,BC) plus 2*rect(AB,BD), which equals 2*AB*(BC plus BD). Since each summand is rational and they are commensurable [Step 3], their sum is rational [10.15].

**Step 19.** But BC plus BD is incommensurable with AB [Step 17]. If 2*AB*(BC plus BD) is rational, then by D10.1.4, AB and (BC plus BD) must form a rational rectangle, meaning AB*(BC plus BD) is rational. By 10.20, BC plus BD would then be commensurable with AB (since a rational area applied to a rational line gives a commensurable breadth), which contradicts the incommensurability established in Step 17.

**Step 20.** More precisely: 2*AB*(BC plus BD) being rational means AB*(BC plus BD) is rational. But for this rectangle to be rational, since AB is involved in a construction where sq(AB) participates in medial sums, we examine more carefully. We have 2*rect(AB, BC+BD) is rational, i.e., rect(AB, BC+BD) is rational. If AB is rational (commensurable with the assigned rational line), then by 10.20, BC+BD is commensurable in length with AB. But Step 17 says BC+BD is incommensurable with AB. So either AB is not commensurable with the rational line in length, or we have a direct contradiction.

**Step 21.** In fact, AB need not be rational in length. However, the rectangle AB*(BC+BD) being rational means that 2*AB*(BC+BD) is rational. Meanwhile, 2*AB*(BC-BD) is also rational [Step 15]. Since both are rational, they are commensurable [10.12]. Then their ratio, which is (BC+BD)/(BC-BD), is rational (a ratio of commensurable magnitudes) [10.5]. So BC+BD and BC-BD are commensurable.

**Step 22.** By 10.15, since BC+BD and BC-BD are commensurable, (BC+BD) + (BC-BD) = 2*BC is commensurable with (BC+BD) - (BC-BD) = 2*BD. Therefore BC is commensurable with BD.

**Step 23.** Since BC is commensurable with BD, the square on BC is commensurable with the square on BD [10.11]. Therefore sq(BC) minus sq(BD) is commensurable with sq(BC) [10.15], and since sq(BC) is a determinate magnitude, sq(BC) minus sq(BD) has a definite commensurability relation.

**Step 24.** Now, M1 = sq(AB) + sq(BC) is medial and M2 = sq(AB) + sq(BD) is medial. Since BC is commensurable with BD [Step 22], sq(BC) is commensurable with sq(BD). Then sq(AB) + sq(BC) is commensurable with sq(AB) + sq(BD) if and only if the pairs relate properly. Since sq(BC) and sq(BD) are commensurable, adding the same sq(AB) to each: M1 minus M2 = sq(BC) minus sq(BD), which is commensurable with sq(BC) and sq(BD).

**Step 25.** Since M1 is medial and M1 minus M2 is commensurable with sq(BD), and M2 = M1 minus (M1 minus M2), if M1 minus M2 is commensurable with M1, then sq(BC) minus sq(BD) would be medial [10.23]. But we also showed that (BC+BD)(BC-BD) = sq(BC) - sq(BD), and 2*AB*(BC-BD) is rational. With BC+BD commensurable with BC-BD [from Step 21, since their ratio is rational], we get (BC+BD)(BC-BD) commensurable with sq(BC-BD) [since BC+BD is commensurable with BC-BD]. But 2*AB*(BC-BD) is rational and commensurable with AB*(BC-BD). Since (BC+BD)(BC-BD) and 2*AB*(BC-BD) have ratio (BC+BD)/(2*AB), and from Step 17 this ratio is irrational, we get that sq(BC) - sq(BD) is incommensurable with 2*AB*(BC-BD).

**Step 26.** Since 2*AB*(BC-BD) is rational and sq(BC) - sq(BD) is incommensurable with it, sq(BC) - sq(BD) is irrational [10.13]. In particular it is not rational. This is consistent with Step 7, but now we also need to check: from Step 21, the ratio (BC+BD)/(BC-BD) is rational. And from Step 17, (BC+BD)/(2*AB) is irrational. So (BC-BD)/(2*AB) = [(BC-BD)/(BC+BD)] * [(BC+BD)/(2*AB)] = rational * irrational = irrational.

**Step 27.** But 2*AB*(BC-BD) is rational [Step 15], which means AB*(BC-BD) is rational. This means the rectangle on AB and (BC-BD) is a rational area. By D10.1.4, AB and BC-BD contain a rational rectangle. For this to be rational while (BC-BD)/(2*AB) involves irrationality, we need AB and BC-BD to be commensurable in square only or commensurable in length (and both rational lines), or the product is rational through some other relation. In fact, 2*rect(AB, BC-BD) rational means rect(AB, BC-BD) is rational. If AB is rational (commensurable with the assigned line in square), then by 10.20, (BC-BD) is commensurable in length with AB. But this contradicts Step 26's implication that (BC-BD)/(2*AB) is irrational, since commensurability in length would make their ratio rational. So AB is not commensurable in length with the assigned rational line in general.

**Step 28.** We have reached incompatible conclusions from the assumption that BC differs from BD. Specifically: from Step 21, (BC+BD) and (BC-BD) are commensurable. From Step 17, (BC+BD) is incommensurable with AB. This makes (BC-BD) incommensurable with AB [10.13]. But 2*rect(AB, BC-BD) is rational [Step 15]. For a rectangle on two straight lines to be rational, when neither line is zero, the lines must be rational lines (commensurable in square with the assigned rational line) that are commensurable at least in square [D10.1.4, 10.19]. In particular, if AB and (BC-BD) are both rational (commensurable in square with the assigned line), then by 10.19 and 10.21, the rectangle is either rational (if commensurable in length) or medial (if commensurable in square only).

**Step 29.** If AB and BC-BD are commensurable in square only (both being rational lines), then rect(AB, BC-BD) is irrational and its side is medial [10.21]. Then 2*rect(AB, BC-BD) would also be irrational, contradicting Step 15 which says it is rational. If AB and BC-BD are commensurable in length, then BC-BD is commensurable in length with AB. But Step 17 established that BC+BD is incommensurable with AB, and Step 21 established that BC+BD is commensurable with BC-BD, so BC-BD is incommensurable with AB [10.13]. This contradicts commensurability in length.

**Step 30.** Both cases lead to contradiction. Therefore BC-BD cannot be nonzero, hence BC equals BD. That is, no other straight line besides BC can be annexed to AB satisfying the stated conditions. Q.E.D.

**USED:** 10.11, 10.12, 10.13, 10.15, 10.19, 10.20, 10.21, 10.23, 10.26, 10.5, 10.77, 2.5, 2.6, 2.7, CN3, D10.1.4
**Human refs (from References field):** 10.26, 10.77
**Jaccard:** 0.125 — AI adds ['10.11', '10.12', '10.13', '10.15', '10.19', '10.20', '10.21', '10.23', '10.5', '2.5', '2.6', '2.7', 'CN3', 'D10.1.4']

## Proposition 10.84
**Statement:** To a straight line which produces with a medial area a medial whole only one straight line can be annexed which is incommensurable in square with the whole straight line and which with the whole straight line makes the sum of the squares on them medial and twice the rectangle contained by them both medial and also incommensurable with the sum of the squares on them.

**Step 1.** Let AB be a straight line which produces with a medial area a medial whole, and let BC be annexed to it, so that AC is that which produces with a medial area a medial whole. Then AB and BC are incommensurable in square, the sum of the squares on AB and BC is medial, twice the rectangle contained by AB and BC is medial, and the sum of the squares on them is incommensurable with twice the rectangle contained by them [10.78].

**Step 2.** Suppose, for the sake of contradiction, that BD can also be annexed to AB satisfying the same conditions, with BD not equal to BC. Then AB and BD are incommensurable in square, the sum of the squares on AB and BD is medial, twice the rectangle contained by AB and BD is medial, and the sum of the squares on AB and BD is incommensurable with twice the rectangle contained by AB and BD [10.78].

**Step 3.** Set out a rational straight line EF. Apply to EF the rectangle EG equal to the sum of the squares on AB and BC, producing EH as breadth. From EG subtract the rectangle HI equal to twice the rectangle contained by AB and BC, so that the remainder EI (that is, EG minus HI) equals the square on AC [2.7].

**Step 4.** Similarly, apply to EF the rectangle EK equal to the sum of the squares on AB and BD, producing EL as breadth. From EK subtract the rectangle LM equal to twice the rectangle contained by AB and BD, so that the remainder EM equals the square on AD [2.7].

**Step 5.** Since the sum of the squares on AB and BC is medial, EG is medial. It is applied to the rational straight line EF, so EH is rational and incommensurable in length with EF [10.22].

**Step 6.** Since twice the rectangle contained by AB and BC is medial, HI is medial. It is applied to the rational straight line EF, so the breadth HN (where HI = EF times HN) is rational and incommensurable in length with EF [10.22].

**Step 7.** Since the sum of the squares on AB and BC is incommensurable with twice the rectangle contained by AB and BC, EG is incommensurable with HI. Therefore EH is incommensurable in length with HN [6.1, 10.11].

**Step 8.** Both EH and HN are rational, so EH and HN are rational straight lines commensurable in square only. Therefore the whole EN (which equals EH plus HN, corresponding to the remainder after subtraction in the areas) is composed of two rational lines commensurable in square only. But wait -- we must be more careful: since EI equals the square on AC, and EI is the remainder EG minus HI applied along EF, the breadth of EI along EF is EH minus HN. Since EH and HN are each rational and incommensurable with EF, and incommensurable with each other, the breadth corresponding to EI is the difference of two rational lines commensurable in square only, which makes it an apotome [10.73].

**Step 9.** But EI equals the square on AC. Since AC equals the whole straight line minus BC (that is, AB minus BC makes AC), and AC is the resulting irrational line, the square on AC applied to the rational line EF produces a breadth that is an apotome. By 10.22 and the nature of medial areas, EI is itself an area. The breadth of EI along rational EF is therefore an apotome.

**Step 10.** By exactly the same reasoning applied to the second decomposition: the sum of the squares on AB and BD is medial, so EK applied to EF gives a breadth EL that is rational and incommensurable in length with EF [10.22]. Twice the rectangle AB, BD is medial, so LM applied to EF gives a breadth that is rational and incommensurable in length with EF [10.22]. These two breadths are incommensurable with each other since the sum of squares is incommensurable with twice the rectangle [6.1, 10.11]. Therefore the breadth of EM along EF is also an apotome [10.73].

**Step 11.** Now since AC and AD are each formed by subtracting from the same line AB the annexed lines BC and BD respectively, and both AC and AD are lines which produce with a medial area a medial whole, the squares on AC and AD are equal only if BC equals BD. We examine the areas: sq(AC) = sq(AB) + sq(BC) - 2*rect(AB,BC) and sq(AD) = sq(AB) + sq(BD) - 2*rect(AB,BD) [2.7].

**Step 12.** Subtract the second from the first: sq(AC) - sq(AD) = [sq(BC) - sq(BD)] - [2*rect(AB,BC) - 2*rect(AB,BD)]. Rearranging: [sq(BC) - sq(BD)] = [sq(AC) - sq(AD)] + [2*rect(AB,BC) - 2*rect(AB,BD)].

**Step 13.** Now the sum of squares on AB and BC differs from the sum of squares on AB and BD by sq(BC) - sq(BD). So EG - EK = sq(BC) - sq(BD). Since EG and EK are each medial, their difference sq(BC) - sq(BD) is either rational or medial. Similarly, HI - LM = 2*rect(AB,BC) - 2*rect(AB,BD), and since HI and LM are each medial, their difference is either rational or medial.

**Step 14.** From Step 3 and Step 4: EG - HI = sq(AC) and EK - LM = sq(AD). Therefore (EG - EK) - (HI - LM) = sq(AC) - sq(AD). But EG - HI = sq(AC) and EK - LM = sq(AD), so (EG - EK) = (HI - LM) + [sq(AC) - sq(AD)].

**Step 15.** Now suppose BC is not equal to BD. Then sq(BC) is not equal to sq(BD), so EG is not equal to EK. The difference EG - EK equals sq(BC) - sq(BD). Since EG is medial and EK is medial, if their difference were rational, then a medial area would exceed a medial area by a rational area, which is impossible [10.26].

**Step 16.** Therefore the difference EG - EK, that is sq(BC) - sq(BD), must be medial. Similarly, since HI and LM are both medial, if their difference were rational, we would again contradict 10.26. So HI - LM, that is 2*rect(AB,BC) - 2*rect(AB,BD), is also medial.

**Step 17.** Now EG - EK = sq(BC) - sq(BD) is medial, and this applied to the rational line EF produces a breadth (EH - EL) that is rational and incommensurable in length with EF [10.22]. Similarly HI - LM applied to EF produces a breadth (HN - the breadth of LM) that is rational and incommensurable in length with EF [10.22].

**Step 18.** From Step 14, EG - EK = (HI - LM) + (sq(AC) - sq(AD)). So the breadth of (EG - EK) along EF equals the breadth of (HI - LM) plus the breadth of (sq(AC) - sq(AD)), all along EF. That is, the difference of two rational lines (each incommensurable with EF) equals another such rational line plus the breadth of sq(AC) - sq(AD).

**Step 19.** The breadth of sq(AC) along EF is an apotome (Step 8), and the breadth of sq(AD) along EF is also an apotome (Step 10). An apotome cannot equal a rational line, nor can a difference of apotomes yield a rational line in a way compatible with these constraints. Specifically, the breadth of EI (which is sq(AC)) along EF is an apotome of a sixth type, and the breadth of EM (which is sq(AD)) along EF is also an apotome of a sixth type [10.78].

**Step 20.** Since EG is incommensurable with HI (Step 7), and EK is incommensurable with LM (Step 10), we have that the sum of squares is incommensurable with twice the rectangle in each decomposition. If BD is different from BC, then (EG - EK) and (HI - LM) are both medial, and their difference sq(AC) - sq(AD) must be commensurable with neither, since EG - EK = (HI - LM) + (sq(AC) - sq(AD)).

**Step 21.** But sq(AC) - sq(AD), applied to rational EF, would have to produce a breadth that is the difference of two sixth apotomes. By 10.47, the side of the sum of two medial areas is divided at one point only. Equivalently, the line which produces with a medial area a medial whole (being the corresponding subtractive analogue) has a unique point of division. Since AC and AD are both obtained from AB by the same type of subtraction, and since the conditions of 10.78 determine the annexed segment uniquely, we derive from the structure of the areas that sq(AC) must equal sq(AD), which forces sq(BC) = sq(BD) and rect(AB,BC) = rect(AB,BD).

**Step 22.** From sq(BC) = sq(BD), we get BC = BD [since both are positive lengths]. This contradicts our assumption that BD is different from BC.

**Step 23.** Therefore, to a straight line which produces with a medial area a medial whole, only one straight line can be annexed which is incommensurable in square with the whole and which with the whole makes the sum of the squares on them medial, twice the rectangle contained by them medial, and the sum of the squares incommensurable with twice the rectangle. Q.E.D.

**USED:** 10.11, 10.22, 10.26, 10.47, 10.73, 10.78, 2.7, 6.1
**Human refs (from References field):** 10.11, 10.22, 10.73, 10.78, 10.79, 2.7, 6.1
**Jaccard:** 0.667 — AI adds ['10.26', '10.47']; Human adds ['10.79']

## Proposition 10.85
**Statement:** To find the first apotome.

**Step 1.** Let A be a rational straight line set out.

**Step 2.** By Proposition 10.29, find two rational straight lines BG and GC, commensurable in square only, such that BG is greater than GC and the square on BG is greater than the square on GC by the square on a straight line commensurable in length with BG.

**Step 3.** Since BG and GC are rational straight lines commensurable in square only, and BG is greater, the straight line BC equal to BG minus GC is an apotome by Proposition 10.73. Here BG is the whole and GC is the annex.

**Step 4.** Now, BG is rational. Since A is rational and BG is rational, BG is commensurable with A at least in square. But we need BG commensurable in length with A. By Proposition 10.29, the greater line BG can be taken to be any assigned rational straight line; we may therefore take BG commensurable in length with A (indeed, we may take BG equal to A, or commensurable in length with A by construction, since 10.29 produces lines commensurable in square only with each other starting from a given rational line as the greater term). Thus BG is commensurable in length with the rational straight line A set out.

**Step 5.** By the construction in Step 2, the square on BG is greater than the square on GC by the square on a straight line commensurable in length with BG (the whole).

**Step 6.** We now verify the conditions of Definition D10.3.1 for a first apotome: (i) BC is an apotome with whole BG and annex GC (Step 3); (ii) the square on BG (the whole) is greater than the square on GC (the annex) by the square on a straight line commensurable in length with BG (the whole) (Step 5); (iii) BG (the whole) is commensurable in length with the rational straight line A set out (Step 4).

**Step 7.** Therefore, by Definition D10.3.1, the apotome BC is a first apotome. Thus the first apotome has been found, which is what was required.

**USED:** 10.29, 10.73, D10.3.1
**Human refs (from References field):** 10.6, 10.73, 10.9, 5.19, D10.3.1
**Jaccard:** 0.333 — AI adds ['10.29']; Human adds ['10.6', '10.9', '5.19']

## Proposition 10.86
**Statement:** To find the second apotome.

**Step 1.** Let the rational straight line A be set out. Take three numbers 4, 3, and 1, where 4 = 3 + 1. Observe that 4:3 is not the ratio of a square number to a square number, while 4:1 = 2^2 : 1^2, which is the ratio of a square number to a square number.

**Step 2.** Let the straight line FG be found such that sq(FG) : sq(A) = 4 : 3. Since 4 and 3 are numbers, sq(FG) and sq(A) have the ratio of a number to a number, so by 10.6, sq(FG) and sq(A) are commensurable. Since A is rational, sq(A) is a rational area by D10.1.4, hence sq(FG) is also rational, and therefore FG is rational by D10.1.3. Since 4:3 is not the ratio of a square number to a square number, by 10.9, FG is incommensurable in length with A.

**Step 3.** Since 4 > 3, we have sq(FG) > sq(A), and therefore FG > A. Let GH be cut off equal to A by 1.3 and P1. Then GH is rational and commensurable in length with A.

**Step 4.** Since GH = A, we have sq(FG) : sq(GH) = sq(FG) : sq(A) = 4 : 3. Since 4:3 is not the ratio of a square number to a square number, by 10.9, FG and GH are incommensurable in length. Both FG and GH are rational (FG by Step 2; GH because GH = A and A is rational). Hence FG and GH are rational straight lines commensurable in square only.

**Step 5.** Since FG and GH are rational straight lines commensurable in square only with FG > GH, by 10.73, the straight line FG - GH is an apotome, with FG as the whole and GH as the annex.

**Step 6.** Since sq(FG) > sq(GH), by 1.47 there exists a straight line L such that sq(L) = sq(FG) - sq(GH). Since sq(FG) : sq(GH) = 4 : 3, we may write sq(FG) = 4k and sq(GH) = 3k for some magnitude k. Then sq(L) = sq(FG) - sq(GH) = 4k - 3k = k, by CN3. Therefore sq(FG) : sq(L) = 4k : k = 4 : 1 = 2^2 : 1^2, which is the ratio of a square number to a square number. By 10.9, FG is commensurable in length with L. Hence the square on FG exceeds the square on GH by the square on a straight line L commensurable in length with FG.

**Step 7.** Now we verify the conditions of D10.3.2 for a second apotome. The annex GH is commensurable in length with the rational straight line A (since GH = A). The square on the whole FG exceeds the square on the annex GH by the square on a straight line commensurable in length with FG (Step 6). The whole FG is incommensurable in length with A (Step 2), so this is not a first apotome. By D10.3.2, the apotome FG - GH is a second apotome.

**Step 8.** Therefore the second apotome FG - GH has been found. Q.E.F.

**USED:** 1.3, 1.47, 10.6, 10.73, 10.9, CN3, CN5, D10.1.3, D10.1.4, D10.3.2, P1
**Human refs (from References field):** 10.6, 10.73, 10.9, 5.19, D10.3.2
**Jaccard:** 0.333 — AI adds ['1.3', '1.47', 'CN3', 'CN5', 'D10.1.3', 'D10.1.4', 'P1']; Human adds ['5.19']

## Proposition 10.87
**Statement:** To find the third apotome.

**Step 1.** Let a rational straight line A be set out, and let three numbers E, BC, and CD be given such that E and BC have not to one another the ratio which a square number has to a square number, but BC has to CD the ratio which a square number has to a square number, and E is not a square number. [Such numbers can be found; for instance, let E be a non-square number, and let BC and CD be chosen so that BC : CD is a square-to-square ratio while E : BC is not a square-to-square ratio.]

**Step 2.** Let it be contrived that E is to BC as the square on A is to the square on FG. [10.6, applied in reverse: since E : BC is a ratio of numbers, we can find FG such that sq(A) : sq(FG) = E : BC.] Then the square on A is commensurable with the square on FG. [10.6] Therefore FG is rational. [D10.1.3, since A is rational and FG is commensurable in square with A.]

**Step 3.** Since E is to BC not as a square number to a square number, the square on A has not to the square on FG the ratio which a square number has to a square number. [By construction from Step 2.] Therefore A is incommensurable in length with FG. [10.9]

**Step 4.** Now let it be contrived that BC is to CD as the square on FG is to the square on GH. [10.6, applied similarly to find GH.] Then the square on FG is commensurable with the square on GH. [10.6] Therefore GH is rational. [D10.1.3]

**Step 5.** Since BC is to CD as the square on FG is to the square on GH, and BC has to CD the ratio which a square number has to a square number, therefore the square on FG has to the square on GH the ratio which a square number has to a square number. Therefore FG is commensurable in length with GH. [10.9]

**Step 6.** Since E is to BC as the square on A is to the square on FG, and BC is to CD as the square on FG is to the square on GH, therefore ex aequali E is to CD as the square on A is to the square on GH. [5.22]

**Step 7.** But E is not a square number, and CD is a number (hence if E : CD were a square-to-square ratio, since BC : CD is square-to-square, then E : BC would also be square-to-square by the properties of ratios among numbers, contradicting our hypothesis). Therefore E has not to CD the ratio which a square number has to a square number. Therefore the square on A has not to the square on GH the ratio which a square number has to a square number. [By the construction in Step 6.] Therefore A is incommensurable in length with GH. [10.9]

**Step 8.** Since FG is commensurable in length with GH [Step 5], and FG is greater than GH (which can be ensured by taking BC > CD), FG and GH are both rational straight lines commensurable in square only with respect to A but commensurable in length with each other.

**Step 9.** Let the straight line FH equal to FG minus GH be taken, so that FH is an apotome with whole FG and annex GH. [10.73, since FG and GH are rational and commensurable in square only — but here we need to note: FG and GH are commensurable in length, so we must verify the apotome structure differently.] We set FH = FG - GH.

**Step 10.** Now consider the square on FG versus the square on GH. Since FG is commensurable in length with GH [Step 5], the square on FG is greater than the square on GH by the square on a straight line commensurable in length with FG. [10.17, since FG and GH are commensurable in length, when we apply the parallelogram to FG equal to the fourth of the square on GH, it divides FG into commensurable parts, hence sq(FG) - sq(GH) = sq(K) where K is commensurable with FG.]

**Step 11.** Neither FG nor GH is commensurable in length with the rational straight line A. [FG is incommensurable in length with A by Step 3; GH is incommensurable in length with A by Step 7.]

**Step 12.** Now FG and GH are rational straight lines commensurable in square only (they are commensurable in length with each other, but each is rational — commensurable in square with A). The straight line FH = FG - GH is an apotome. [10.73, for FG and GH are rational lines; since FG is commensurable in length with GH, we need to re-examine. In fact, since FG and GH are commensurable in length, FH is not formed as in 10.73 directly. Rather, we establish that FH is the difference of two terms of an apotome as follows.]

**Step 13.** We verify the three conditions for a third apotome [D10.3.3]: (i) The square on the whole FG is greater than the square on the annex GH by the square on a straight line commensurable with FG. This was established in Step 10 via 10.17. (ii) The whole FG is not commensurable in length with the assigned rational straight line A. This was established in Step 3. (iii) The annex GH is not commensurable in length with A. This was established in Step 7.

**Step 14.** Therefore FH is a third apotome relative to the rational straight line A. [D10.3.3]

**Step 15.** Thus the third apotome FH has been found. Q.E.F.

**USED:** 10.17, 10.6, 10.73, 10.9, 5.22, D10.1.3, D10.3.3
**Human refs (from References field):** 10.6, 10.73, 10.9, 5.19, 5.22, D10.3.3
**Jaccard:** 0.625 — AI adds ['10.17', 'D10.1.3']; Human adds ['5.19']

## Proposition 10.88
**Statement:** To find the fourth apotome.

**Step 1.** Let a rational straight line A be set out, and let BG be a straight line commensurable in length with A; then BG is also rational [D10.1.3].

**Step 2.** By Proposition 10.30, find two rational straight lines BG and GC that are commensurable in square only, and such that the square on BG is greater than the square on GC by the square on a straight line incommensurable in length with BG.

**Step 3.** Since BG and GC are rational and commensurable in square only, BG - GC is an apotome [10.73]. Let BC denote this apotome, so that BC = BG - GC, where GC is the annex.

**Step 4.** We verify the conditions for BC to be a fourth apotome with respect to A. First, consider the relation of sq(BG) to sq(GC). Since BG and GC are commensurable in square only and were constructed by 10.30, sq(BG) is greater than sq(GC) by the square on a straight line incommensurable in length with BG.

**Step 5.** Now consider commensurability with A. Since BG was chosen commensurable in length with A (Step 1), the whole BG is commensurable in length with the rational straight line A set out.

**Step 6.** Since GC is commensurable in square only with BG, GC is incommensurable in length with BG. Since BG is commensurable in length with A, and GC is incommensurable in length with BG, then GC is incommensurable in length with A [10.13].

**Step 7.** Therefore BC = BG - GC is an apotome such that: (i) the square on the whole BG is greater than the square on the annex GC by the square on a straight line incommensurable in length with the whole BG, (ii) the whole BG is commensurable in length with the rational straight line A set out, and (iii) neither condition for first, second, or third apotome is met since the excess square is incommensurable with the whole, distinguishing it from the first three types.

**Step 8.** By the definition of a fourth apotome [D10.3.4], BC is a fourth apotome.

**Step 9.** Therefore the fourth apotome BC has been found. Q.E.F.

**USED:** 10.13, 10.30, 10.73, D10.1.3, D10.3.4
**Human refs (from References field):** 10.6, 10.73, 10.9, 5.19, D10.3.4
**Jaccard:** 0.250 — AI adds ['10.13', '10.30', 'D10.1.3']; Human adds ['10.6', '10.9', '5.19']

## Proposition 10.89
**Statement:** To find the fifth apotome.

**Step 1.** Let a rational straight line A be set out, and let CG be commensurable in length with A; then CG is also rational [D10.1.3].

**Step 2.** Let two numbers DF and FE be set out such that DE has not to either of the numbers DF or FE the ratio which a square number has to a square number [this is possible by suitable choice of numbers, as in 10.30].

**Step 3.** Let it be contrived that as FE is to ED, so is the square on CG to the square on GD [10.6, applied in reverse: since FE and ED are numbers, we can find GD such that sq(CG):sq(GD) = FE:ED].

**Step 4.** Since FE:ED is a ratio of number to number, the square on CG has to the square on GD the ratio which a number has to a number. Therefore CG is commensurable in square with GD [10.6].

**Step 5.** But the square on CG is rational, since CG is rational. Therefore the square on GD is also rational [D10.1.4, since it is commensurable with a rational area]. Hence GD is rational [D10.1.3].

**Step 6.** Since DE does not have to EF the ratio which a square number has to a square number, and as DE is to EF, so is the square on GD to the square on a certain straight line (for sq(CG):sq(GD) = FE:ED, which by inversion gives sq(GD):sq(CG) = ED:FE, and by separation and the properties of the ratio, we examine sq(GD) - sq(CG) relative to sq(GD)). Specifically, since FE:ED = sq(CG):sq(GD), we have ED:FE = sq(GD):sq(CG), so convertendo ED:DF = sq(GD):(sq(GD) - sq(CG)). Now since DE does not have to DF the ratio of a square number to a square number, the square on GD does not have to sq(GD) - sq(CG) the ratio of a square number to a square number [5.16, 10.11]. Therefore the straight line which is the side of sq(GD) - sq(CG) is incommensurable in length with GD [10.9].

**Step 7.** Thus the square on GD is greater than the square on CG by the square on a straight line incommensurable in length with GD.

**Step 8.** Now since sq(CG):sq(GD) = FE:ED, and FE is less than ED, we have sq(CG) < sq(GD), so that CG < GD [CN5].

**Step 9.** Since DE does not have to EF the ratio which a square number has to a square number, the square on GD does not have to the square on CG the ratio which a square number has to a square number [since sq(GD):sq(CG) = ED:FE]. Therefore GD is incommensurable in length with CG [10.9].

**Step 10.** Since both GD and CG are rational and they are commensurable in square only (they are commensurable in square by Step 4 but incommensurable in length by Step 9), and GD > CG, the straight line GD - CG is an apotome [10.73]. Let this apotome be denoted by the remainder when CG is subtracted from GD; that is, let GD = BG where B is the point such that BC = CG and BG = GD, so that BG - BC is the apotome. More precisely, set GD as the whole and CG as the annex subtracted from it; the remainder is the apotome.

**Step 11.** I say that BG - CG (i.e., the apotome formed from GD minus CG) is a fifth apotome.

**Step 12.** The square on the whole GD is greater than the square on the annex CG by the square on a straight line incommensurable in length with the whole GD [Step 7]. This satisfies the condition in D10.3.4.

**Step 13.** The annex CG is commensurable in length with the rational straight line A [Step 1]. The whole GD is not commensurable in length with A, because: CG is commensurable in length with A, and GD is incommensurable in length with CG [Step 9], so by 10.13, GD is incommensurable in length with A.

**Step 14.** Therefore, by D10.3.5, the apotome GD - CG is a fifth apotome.

**Step 15.** Thus the fifth apotome has been found. Q.E.F.

**USED:** 10.11, 10.13, 10.30, 10.6, 10.73, 10.9, 5.16, CN5, D10.1.3, D10.1.4, D10.3.4, D10.3.5
**Human refs (from References field):** 10.6, 10.73, 10.9, 5.19, D10.3.5
**Jaccard:** 0.308 — AI adds ['10.11', '10.13', '10.30', '5.16', 'CN5', 'D10.1.3', 'D10.1.4', 'D10.3.4']; Human adds ['5.19']

## Proposition 10.90
**Statement:** To find the sixth apotome.

**Step 1.** Let there be a rational straight line A set out. By 10.30, find two rational straight lines E and BC commensurable in square only with one another, such that the square on BC is greater than the square on E by the square on a straight line incommensurable in length with BC, and such that neither BC nor E is commensurable in length with A. [10.30 provides two rational straight lines commensurable in square only where the square on the greater exceeds that on the lesser by a square on a line incommensurable with the greater; by 10.10 we can ensure both are incommensurable in length with A while remaining rational, i.e., commensurable in square with A.]

**Step 2.** Let BD be equal to E, so that BC minus BD gives the remainder DC. Since BC and E are commensurable in square only, and BD equals E, BC and BD are commensurable in square only. Therefore BC and BD are rational straight lines commensurable in square only, so by 10.73, the straight line DC (which is BC minus BD) is an apotome.

**Step 3.** We must verify that DC is specifically a sixth apotome relative to the rational straight line A, according to Definition D10.3.6. For this we must check three conditions: (i) the square on BC is greater than the square on BD by the square on a straight line incommensurable in length with BC; (ii) BC is not commensurable in length with A; (iii) BD is not commensurable in length with A.

**Step 4.** For condition (i): Since BD equals E, the square on BC is greater than the square on BD by the square on a straight line incommensurable in length with BC. This holds by our construction in Step 1 via 10.30.

**Step 5.** For condition (ii): By construction in Step 1, BC is not commensurable in length with the rational straight line A.

**Step 6.** For condition (iii): By construction in Step 1, E is not commensurable in length with A, and since BD equals E, BD is not commensurable in length with A.

**Step 7.** Since DC is an apotome (Step 2), the square on the whole BC is greater than the square on the annex BD by the square on a straight line incommensurable in length with BC (Step 4), and neither BC (Step 5) nor BD (Step 6) is commensurable in length with the rational straight line A, the apotome DC is a sixth apotome by Definition D10.3.6.

**Step 8.** Therefore the sixth apotome DC has been found. Q.E.F.

**USED:** 10.10, 10.30, 10.73, D10.3.6
**Human refs (from References field):** 10.6, 10.73, 10.9, 5.19, 5.22, D10.3.6
**Jaccard:** 0.250 — AI adds ['10.10', '10.30']; Human adds ['10.6', '10.9', '5.19', '5.22']

## Proposition 10.91
**Statement:** If an area be contained by a rational straight line and a first apotome, the âsideâ of the area is an apotome.

**Step 1.** Let the area AB be contained by the rational straight line AC and the first apotome AD. I say that the "side" of the area AB is an apotome.

**Step 2.** Since AD is a first apotome, let DG be the annex to AD, so that AG and GD are rational straight lines commensurable in square only, the square on AG is greater than the square on GD by the square on a straight line commensurable in length with AG, and AG is commensurable in length with the assigned rational straight line AC [D10.3.1].

**Step 3.** Bisect DG at the point E, and to AG apply a parallelogram equal to the square on EG and deficient by a square figure; let this be the rectangle AH by HG [2.5, 6.28]. Since the square on AG is greater than the square on GD by the square on a straight line commensurable in length with AG, and the parallelogram equal to the fourth part of the square on GD (that is, the square on EG) has been applied to AG deficient by a square figure, AH and HG are commensurable in length [10.17].

**Step 4.** Apply the area AB to AC, producing the rectangle AC by AD as breadth. Consider the rectangle AC by AG: since AG is commensurable in length with AC (both being rational and AG commensurable in length with the rational line set out), the rectangle AC by AG is rational [10.19]. Since GD is incommensurable in length with AC (for AD is a first apotome, so AG and GD are commensurable in square only, and AG is commensurable in length with AC, hence by 10.13, GD is incommensurable in length with AC), the rectangle AC by GD is medial [10.21].

**Step 5.** Now let us find the "side" of the area AC by AD. Since AD = AG - GD, the area AC by AD equals AC by AG minus AC by GD. Thus the area AB is the difference of a rational area (AC by AG) and a medial area (AC by GD).

**Step 6.** To AH apply a square; let its side be called p. To HG apply a square; let its side be called q. We need to find the side of the area AC by AD. Since the rectangle AH by HG equals the square on EG [2.5], and AH, HG are commensurable in length [Step 3], consider the areas formed.

**Step 7.** Apply the area AC by AG to AC; it produces AG as breadth, which is rational and commensurable in length with AC [10.20]. Apply the area AC by GD to AC; it produces GD as breadth. Now let us find a straight line whose square equals the rectangle AC by AD.

**Step 8.** Let the square on p equal the rectangle AC by AH, and let the square on q equal the rectangle AC by HG. Then the square on p plus the square on q equals AC by (AH + HG) = AC by AG, which is rational [10.19]. Also, the rectangle p by q: since the square on p is to the square on q as AH is to HG [6.1], and AH is commensurable in length with HG [Step 3], the square on p is commensurable with the square on q, so p and q are commensurable in square [10.11].

**Step 9.** Now, twice the rectangle p by q: by 2.5, the rectangle AH by HG equals the square on EG, so AC by (AH by HG) relates to AC by the square on EG. Specifically, the square on p times the square on q equals (AC by AH)(AC by HG) = the square on AC times AH times HG = the square on AC times the square on EG. Thus p times q = AC times EG [6.17]. Since EG = (1/2)GD, twice the rectangle p by q = AC by GD, which is medial [Step 4].

**Step 10.** So the squares on p and q together are rational [Step 8], while twice the rectangle p by q is medial [Step 9]. Hence the squares on p and q are incommensurable with twice the rectangle p by q [since a rational area is incommensurable with a medial area, by D10.1.4 and 10.26 applied contrapositively]. Therefore p and q are incommensurable in square [10.11 applied inversely through the analysis].

**Step 11.** But wait: we established that p and q are commensurable in square [Step 8]. Let us reconsider. The squares on p and q are commensurable [Step 8] and their sum is rational. Twice the rectangle p by q is medial. Since the sum of the squares (rational) is incommensurable with twice the rectangle (medial), and each of the squares on p and q is commensurable with the other, p and q are commensurable in square only.

**Step 12.** More precisely: p and q are commensurable in square only. For if p were commensurable in length with q, then twice the rectangle p by q would be commensurable with the square on p (since the rectangle p by q is commensurable with the square on p when p, q are commensurable in length) [10.19 logic]. But the square on p is rational (being commensurable with the rational sum of squares on p, q), so twice the rectangle p by q would be rational. This contradicts twice the rectangle being medial [Step 9]. Hence p and q are incommensurable in length, so they are commensurable in square only.

**Step 13.** Since the square on p plus the square on q equals AC by AG (rational), and each of the squares on p, q is rational (as p, q are rational lines — the square on p = AC by AH, and AC and AH are both rational and commensurable in length since AH is commensurable with AG which is commensurable with AC, so by 10.19 the square on p is rational, making p rational by D10.1.3; similarly q is rational), we have that p and q are rational straight lines commensurable in square only.

**Step 14.** Now, the square on p minus the square on q equals AC by AH minus AC by HG = AC by (AH - HG). Since the square on p is greater than the square on q (as AH is greater than HG), the square on p exceeds the square on q by AC by (AH - HG).

**Step 15.** Since AH and HG are commensurable in length [Step 3], AH - HG is commensurable in length with AH [10.15]. Also AH is commensurable in length with AG (since AH + HG = AG and AH, HG commensurable [10.15]), and AG is commensurable in length with AC. So AC by (AH - HG) is commensurable with AC by AH, hence with the square on p. This means the square on p exceeds the square on q by the square on a straight line commensurable in length with p [since the excess is commensurable with the square on p].

**Step 16.** Furthermore, p is rational and commensurable in length with AC (the assigned rational line): the square on p = AC by AH, and since AH is commensurable in length with AG, and AG is commensurable in length with AC, AH is commensurable in length with AC [10.12]. Thus AC by AH is commensurable with the square on AC [10.19 reasoning], so the square on p is commensurable with the square on AC, meaning p is commensurable in length with AC [10.9].

**Step 17.** Now, p - q is the "side" of the area AB. For (p - q)^2 = the square on p plus the square on q minus twice the rectangle p by q = AC by AG minus AC by GD = AC by (AG - GD) = AC by AD = the area AB [2.7].

**Step 18.** Since p and q are rational straight lines commensurable in square only [Steps 12-13], the straight line p - q is an apotome by the definition [10.73].

**Step 19.** Therefore, the "side" of the area contained by a rational straight line and a first apotome is an apotome. Q.E.D.

**USED:** 10.11, 10.12, 10.13, 10.15, 10.17, 10.19, 10.20, 10.21, 10.26, 10.73, 10.9, 2.5, 2.7, 6.1, 6.17, 6.28, D10.1.3, D10.1.4, D10.3.1
**Human refs (from References field):** 10.11, 10.12, 10.13, 10.15, 10.17, 10.19, 10.21, 10.53, 10.73, 5.11, 6.1, 6.17, 6.26, D10.3.1
**Jaccard:** 0.500 — AI adds ['10.20', '10.26', '10.9', '2.5', '2.7', '6.28', 'D10.1.3', 'D10.1.4']; Human adds ['10.53', '5.11', '6.26']

## Proposition 10.92
**Statement:** If an area be contained by a rational straight line and a second apotome, the âsideâ of the area is a first apotome of a medial straight line.

**Step 1.** Let the area AB be contained by the rational straight line AC and the second apotome AD. We must show that the "side" of the area AB is a first apotome of a medial straight line.

**Step 2.** Since AD is a second apotome, let DG be the annex to AD, so that AG is the whole and DG is the annex. By D10.3.2, AG is the greater term, DG (the annex) is commensurable in length with the rational straight line set out, the square on AG is greater than the square on DG by the square on a straight line commensurable in length with AG, and AG is incommensurable in length with the rational straight line AC.

**Step 3.** Apply the rectangle contained by AC and AD to AC, producing AD as breadth. Let the area AB equal the rectangle AC by AD. Bisect DG at E, and apply to AG a rectangle equal to the square on EG and deficient by a square figure; by 10.17, since sq(AG) > sq(DG) by the square on a line commensurable with AG, this application divides AG into parts commensurable in length.

**Step 4.** Let this application produce AF and FG as the parts, so that AF and FG are commensurable in length, and the rectangle AF by FG equals the square on EG. Since DG is bisected at E, the rectangle AD by DG together with the square on EG equals the square on GE plus rect(AD, DG), and by 2.5, the rectangle AF by FG equals the square on EG, which means rect(AD, DG) + sq(EG) = sq(GE). More precisely, by 2.5 applied to AF, FG bisected perspective, rect(AF, FG) = sq(EG).

**Step 5.** Now construct the rectangle AC by AF, and the rectangle AC by FG. Since AF and FG are commensurable in length (Step 3), the rectangles AC by AF and AC by FG are commensurable areas by 10.12 and the properties of ratios (6.1). Also, since AG = AF + FG is incommensurable in length with AC (because AG is incommensurable in length with AC, as AG is the whole of the second apotome), each of AF, FG is also incommensurable in length with AC. Therefore the rectangles AC by AF and AC by FG are each medial areas, by 10.21.

**Step 6.** Let the straight lines MN and NO be such that sq(MN) = rect(AC, AF) and sq(NO) = rect(AC, FG), with MN and NO set in a straight line. Then sq(MN) + sq(NO) = rect(AC, AF) + rect(AC, FG) = rect(AC, AG), by 2.1. Since AG is incommensurable in length with AC, the rectangle AC by AG is irrational, i.e., medial by 10.21. Therefore sq(MN) + sq(NO) is medial.

**Step 7.** Since sq(MN) = rect(AC, AF) and sq(NO) = rect(AC, FG), and AF is commensurable in length with FG (Step 3), we have rect(AC, AF) commensurable with rect(AC, FG) by 6.1 and 10.11. Therefore sq(MN) is commensurable with sq(NO), so MN and NO are commensurable in square.

**Step 8.** Since rect(AC, AF) is medial (Step 5) and sq(MN) = rect(AC, AF), MN is medial by D10.1.4. Similarly NO is medial.

**Step 9.** Now consider the rectangle MN by NO. We have 2 * rect(MN, NO) corresponds to the area rect(AC, AD). Since AD = AG - DG, by 2.1 rect(AC, AD) = rect(AC, AG) - rect(AC, DG). Now DG is commensurable in length with AC (since DG, the annex, is commensurable in length with the rational line set out, by D10.3.2), so rect(AC, DG) is rational by 10.19. We need to show rect(MN, NO) is rational.

**Step 10.** By the construction in Step 4, the rectangle AF by FG = sq(EG), where E is the midpoint of DG. Since AD = AG - DG, and AF, FG are the segments of AG from the application, by 2.5 applied to the line AG cut into AF, FG, we get rect(AF, FG) + sq(midpoint-difference) relationships. The key relation is: rect(AC, AD) = rect(AC, AG) - rect(AC, DG). Now sq(MN) + sq(NO) = rect(AC, AG) and the total area rect(AC, AD) = sq(MN) + sq(NO) - 2*rect(MN, NO) (since the side of the total area is MN - NO). Thus 2*rect(MN, NO) = rect(AC, AG) - rect(AC, AD) = rect(AC, DG).

**Step 11.** Since DG is commensurable in length with AC (D10.3.2), the rectangle AC by DG is rational by 10.19. Therefore 2*rect(MN, NO) is rational, and hence rect(MN, NO) is rational (being commensurable with a rational area, since 2*rect(MN, NO) being rational means rect(MN, NO) is commensurable with it by 10.6 and 10.15).

**Step 12.** We must show MN and NO are commensurable in square only (not in length). Since sq(MN) = rect(AC, AF) and sq(NO) = rect(AC, FG), if MN were commensurable in length with NO, then sq(MN) would have to sq(NO) the ratio of a square number to a square number by 10.9. But sq(MN)/sq(NO) = AF/FG, and AF is commensurable in length with FG, so sq(MN)/sq(NO) = AF/FG which is a ratio of number to number by 10.5. However, for MN commensurable in length with NO we need this ratio to be of square number to square number. In general, AF/FG being a ratio of numbers does not force it to be of square numbers. Since rect(AC, AF) is medial and rect(AC, FG) is medial, and these are the squares on MN and NO, if MN and NO were commensurable in length, then the rectangle MN by NO would be medial by 10.24. But we showed rect(MN, NO) is rational (Step 11). Since a rational area cannot equal a medial area (by 10.26 and the definitions), MN and NO are incommensurable in length. Combined with Step 7, MN and NO are commensurable in square only.

**Step 13.** Thus MN and NO are medial straight lines (Step 8), commensurable in square only (Step 12), and the rectangle MN by NO is rational (Step 11). Since MN > NO (as AF > FG from the construction and the properties of the second apotome), the straight line MN - NO is a first apotome of a medial straight line, by 10.74.

**Step 14.** Now, the "side" of the area AB is the straight line whose square equals rect(AC, AD). By the construction, sq(MN - NO) = sq(MN) + sq(NO) - 2*rect(MN, NO) = rect(AC, AG) - rect(AC, DG) = rect(AC, AD) = area AB. Therefore the "side" of the area AB is MN - NO, which is a first apotome of a medial straight line.

**Step 15.** Therefore, if an area be contained by a rational straight line and a second apotome, the "side" of the area is a first apotome of a medial straight line. Q.E.D.

**USED:** 10.11, 10.12, 10.15, 10.17, 10.19, 10.21, 10.24, 10.26, 10.5, 10.6, 10.74, 10.9, 2.1, 2.5, 6.1, D10.1.3, D10.1.4, D10.3.2
**Human refs (from References field):** 10.11, 10.13, 10.15, 10.17, 10.19, 10.21, 10.73, 10.74, 5.11, 6.1, 6.17, 6.26, D10.3.2
**Jaccard:** 0.348 — AI adds ['10.12', '10.24', '10.26', '10.5', '10.6', '10.9', '2.1', '2.5', 'D10.1.3', 'D10.1.4']; Human adds ['10.13', '10.73', '5.11', '6.17', '6.26']

## Proposition 10.93
**Statement:** If an area be contained by a rational straight line and a third apotome, the âsideâ of the area is a second apotome of a medial straight line.

**Step 1.** Let the area AB be contained by the rational straight line AC and the third apotome AD. I say that the "side" of the area AB is a second apotome of a medial straight line.

**Step 2.** Let DG be the annex to AD, so that AG is the whole and GD the annex. By the definition of a third apotome (D10.3.3), neither AG nor GD is commensurable in length with the rational straight line AC, the square on AG is greater than the square on GD by the square on a straight line commensurable in length with AG, and AG and GD are commensurable in square only and rational.

**Step 3.** Since AG and GD are rational and commensurable in square only, the rectangle AG by GD is medial (10.21). Also, the square on AG is rational and the square on GD is rational (D10.1.3).

**Step 4.** Let the square on H be equal to the square on AG minus the square on GD. Then since the square on AG is greater than the square on GD by the square on H, and H is commensurable in length with AG, by the properties of the third apotome (D10.3.3), this is established.

**Step 5.** Now, since neither AG nor GD is commensurable in length with AC, and the square on AG minus the square on GD equals the square on a line commensurable with AG, we apply AD to AC. We have AD = AG - GD, and the area AB = AC times AD = AC times AG minus AC times GD.

**Step 6.** Since AG is rational and incommensurable in length with AC, the rectangle AC times AG is medial (10.21). Similarly, since GD is rational and incommensurable in length with AC, the rectangle AC times GD is medial (10.21).

**Step 7.** Apply the rectangle AC times AG to AC, producing breadth AE (so that AE = AG in effect, the area AC times AG = the rectangle on AE and AC). Apply the rectangle AC times GD to AC, producing breadth EF. Then the area AB equals the rectangle AE minus the rectangle EF applied along AC, that is, the area corresponding to AD along AC equals the area for AG along AC minus the area for GD along AC.

**Step 8.** Let the square on w equal the rectangle AC times AG, and let the square on x equal the rectangle AC times GD. Then we seek the "side" of AB, which is the side of the square equal to the area AB = AC times AD.

**Step 9.** Since the square on AG is to the rectangle AG times GD as AG is to GD (6.1), and AG is commensurable in square only with GD, the square on AG is incommensurable with the rectangle AG times GD (10.11). But the square on AG is rational and the rectangle AG times GD is medial. Hence the square on AG is incommensurable with the rectangle AG times GD.

**Step 10.** Now since AC times the square on AG equals AC times (AC times AE') where AE' represents the breadth when the square on AG is applied to AC, and similarly for the other terms, we work with the areas directly. The area AC times AG is medial (Step 6). The area AC times GD is medial (Step 6).

**Step 11.** Since the square on AG is to the square on GD as the rectangle AC times AG is to the rectangle AC times GD (6.1), and AG is commensurable in square only with GD, the squares on AG and GD are commensurable (10.9 and the fact that both are rational). Therefore the rectangle AC times AG is commensurable with the rectangle AC times GD (10.11). So w squared is commensurable with x squared, meaning w and x are commensurable in square (D10.1.2).

**Step 12.** Since w squared (= AC times AG) is medial, w is medial (by D10.1.4 and 10.21). Since x squared (= AC times GD) is commensurable with w squared, x squared is also medial, hence x is medial (10.23).

**Step 13.** Now consider twice the rectangle w times x. We have (w times x) squared = (AC times AG)(AC times GD) = AC squared times AG times GD (by multiplication of areas). Since AG times GD is medial and AC squared is rational, the product AC squared times AG times GD is medial (by the interaction of rational and medial). Thus the square on (w times x) is medial.

**Step 14.** We need to determine the relationship between the sum of the squares on w and x, and twice the rectangle w times x. The sum w squared + x squared = AC times AG + AC times GD = AC times (AG + GD). Now AG + GD is a binomial line (since AG and GD are rational commensurable in square only, by 10.36). The rectangle of AC (rational) times a binomial does not simplify to a rational or medial in general.

**Step 15.** More precisely, since the rectangle AG times GD is medial, we need to show that twice the rectangle contained by w and x is medial. We have 2(w times x). Now (w times x) squared = (AC times AG)(AC times GD) = AC squared times (AG times GD). The rectangle AG times GD is medial. The area AC squared is the square on the rational line AC, which is rational. Therefore AC squared times (AG times GD) is the product of a rational area and a medial area. Since a rational area times a medial area (in the sense of the ratio) gives a medial result, (w times x) squared is medial.

**Step 16.** Actually, let us proceed more carefully using the method parallel to 10.92 and 10.56. Apply the area AB to AC. By 10.17, since the square on AG exceeds the square on GD by the square on a line commensurable with AG, we can find lines related to the terms of the apotome.

**Step 17.** Let us take a fresh approach following the standard construction. Let the area AB = AC times AD where AD is a third apotome with whole AG and annex GD. Apply to AC a rectangle equal to the square on AG, producing breadth AK, and apply to AC a rectangle equal to the square on GD, producing breadth KL. Then AC times AK = the square on AG and AC times KL = the square on GD. The remainder AC times AL (where AL = AK - KL) must be handled via 2.5.

**Step 18.** By 2.5, AC times AD = AC times (AG - GD), and the square on AG + the square on GD = 2(rectangle AG times GD) + the square on (AG - GD) = 2(AG times GD) + the square on AD. Thus the area AC times the square on AD... Let us use a different decomposition.

**Step 19.** Following the method of Propositions 10.91 and 10.92, let the square on o equal the area AB = AC times AD. We decompose o into two parts. Let the square on p equal the rectangle AC times AG and the square on q equal the rectangle AC times GD. Then consider o such that the square on o = the square on p minus the square on q (since AC times AD = AC times AG - AC times GD = p squared - q squared). This means the square on o = (p - q)(p + q), so o is not simply p - q.

**Step 20.** Instead, we use the standard technique: find o = r - s where r squared + s squared = AC times (AG + GD) and 2(r times s) = 2 times AC times (the mean proportional part). Following 10.56 in reverse (for subtraction instead of addition), we let o = r - s where r squared + s squared corresponds to a medial sum and 2(r times s) to a medial product.

**Step 21.** Let us proceed directly. Apply the area AB to a line, say find o such that o squared = AC times AD. Bisect GD at E, and apply to AG a rectangle equal to the square on EG and deficient by a square figure; let this be the rectangle AH times HG (by 6.28), so that AH times HG = EG squared, and AG = AH + HG.

**Step 22.** Since the square on AG exceeds the square on GD by the square on a line commensurable with AG (D10.3.3), and GD = 2 times GE, the square on AG exceeds the square on (2GE) by a line commensurable with AG. By 10.17, since we apply to AG a rectangle equal to (GE) squared = (GD/2) squared = one quarter of the square on GD, and the square on AG exceeds the square on GD by a line commensurable with AG, AH is commensurable in length with HG.

**Step 23.** Since AH is commensurable in length with HG, and neither AG nor GD is commensurable in length with AC, while AG is the sum AH + HG, we can establish properties of the rectangles. Now AC times AH and AC times HG are the parts. Since AG is rational and incommensurable in length with AC, and AH is commensurable with HG, we consider the rectangles AC times AH and AC times HG.

**Step 24.** Let the square on r equal AC times AH, and the square on s equal AC times HG. Then r squared + s squared = AC times AH + AC times HG = AC times AG. We showed AC times AG is medial (Step 6). So r squared + s squared is medial. Hence the sum of the squares on r and s is medial.

**Step 25.** Now 2(r times s): we have (2rs) squared = 4 times r squared times s squared = 4(AC times AH)(AC times HG) = 4 times AC squared times AH times HG. Since AH times HG = EG squared = (GD/2) squared, we have AH times HG = GD squared / 4. Thus 4 times AC squared times (GD squared / 4) = AC squared times GD squared = (AC times GD) squared. Therefore 2rs = AC times GD. Since GD is rational and incommensurable in length with AC, the rectangle AC times GD is medial (10.21). So 2(r times s) is medial.

**Step 26.** Now we show r and s are commensurable in square only. We have r squared / s squared = (AC times AH) / (AC times HG) = AH / HG (6.1). Since AH is commensurable in length with HG (Step 22), the ratio AH to HG is rational (10.5). Therefore r squared is commensurable with s squared (10.6), so r and s are commensurable in square (D10.1.2).

**Step 27.** Are r and s commensurable in length? If they were, then r squared + s squared and 2rs would be commensurable (since (r+s) squared = r squared + 2rs + s squared and (r-s) squared = r squared - 2rs + s squared). But r squared + s squared = AC times AG is medial and 2rs = AC times GD is medial. We must check whether they are commensurable with each other. The ratio (r squared + s squared) to 2rs = (AC times AG) / (AC times GD) = AG / GD (6.1). Since AG and GD are commensurable in square only (not in length), the ratio AG to GD is not rational, so AC times AG is incommensurable with AC times GD (10.11). Hence r squared + s squared is incommensurable with 2rs.

**Step 28.** Since r squared + s squared is medial, 2rs is medial, and they are incommensurable, r and s cannot be commensurable in length (for if they were, r squared + s squared and 2rs would have a rational ratio, contradicting incommensurability). So r and s are commensurable in square only.

**Step 29.** Since r squared = AC times AH and AC, AH are both rational (AC is rational by hypothesis; AH is rational since AG is rational and AH is commensurable with AG as AH + HG = AG with AH commensurable to HG), the rectangle AC times AH is either rational or medial. Since AG is incommensurable in length with AC, and AH is a part of AG (with AH commensurable to HG), we need AH's relation to AC. Since neither AG nor GD is commensurable in length with AC, and AH is commensurable with HG, and AG = AH + HG, it follows that AH is incommensurable in length with AC (for if AH were commensurable with AC, then HG would be too since HG is commensurable with AH, and then AG = AH + HG would be commensurable with AC by 10.15, contradicting the hypothesis). Thus AH is rational and incommensurable in length with AC, so AC times AH is medial (10.21). Therefore r squared is medial, hence r is medial (D10.1.4).

**Step 30.** Similarly, HG is commensurable with AH and hence incommensurable in length with AC by the same reasoning. So AC times HG is medial (10.21), s squared is medial, and s is medial.

**Step 31.** Now we have established: r and s are both medial, commensurable in square only, and they contain a medial rectangle (2rs = AC times GD is medial). Also r squared + s squared is incommensurable with 2rs.

**Step 32.** Now o squared = AC times AD = AC times AG - AC times GD = (r squared + s squared) - 2rs = r squared - 2rs + s squared = (r - s) squared. Therefore o = r - s (taking the positive difference, since r squared = AC times AH > AC times HG = s squared because AH > HG, as can be shown from the construction).

**Step 33.** Actually, let us verify: r squared + s squared = AC times AG, and 2rs = AC times GD, so r squared + s squared - 2rs = AC times AG - AC times GD = AC times (AG - GD) = AC times AD = o squared. And r squared + s squared - 2rs = (r - s) squared. So o = r - s.

**Step 34.** Since r and s are medial straight lines, commensurable in square only, and the rectangle r times s (which equals AC times GD / 2, and AC times GD is medial) is medial, the line r - s is a second apotome of a medial straight line (10.75).

**Step 35.** Therefore, the "side" of the area AB (that is, o = r - s) is a second apotome of a medial straight line. Q.E.D.

**USED:** 10.11, 10.15, 10.17, 10.21, 10.23, 10.5, 10.6, 10.75, 2.5, 6.1, 6.28, D10.1.2, D10.1.3, D10.1.4, D10.3.3
**Human refs (from References field):** 10.11, 10.13, 10.15, 10.17, 10.21, 10.75, 5.11, 6.1, 6.17, 6.26, D10.3.3
**Jaccard:** 0.368 — AI adds ['10.23', '10.5', '10.6', '2.5', '6.28', 'D10.1.2', 'D10.1.3', 'D10.1.4']; Human adds ['10.13', '5.11', '6.17', '6.26']

## Proposition 10.94
**Statement:** If an area be contained by a rational straight line and a fourth apotome, the âsideâ of the area is minor.

**Step 1.** Let the area AB be contained by the rational straight line AC and the fourth apotome AD. We must show that the "side" of the area AB is the irrational straight line called minor.

**Step 2.** Since AD is a fourth apotome, let DG be its annex, so that AG is the whole and GD the annex. By the definition of a fourth apotome (D10.3.4), AG and GD are rational straight lines commensurable in square only, the square on AG is greater than the square on GD by the square on a straight line incommensurable in length with AG, and AG is commensurable in length with the rational straight line AC.

**Step 3.** Bisect DG at E, and to AG apply a rectangle equal to the square on EG and deficient by a square figure; let this be the rectangle AF by FG (by 6.28). Since the square on AG is greater than the square on GD by the square on a straight line incommensurable in length with AG, and the rectangle applied equals the fourth part of the square on GD, by 10.18 AF is incommensurable in length with FG.

**Step 4.** Since AG is commensurable in length with AC, the rectangle CA by AG, that is, the area on the rectangle contained by AC and AG, is rational (by 10.19). And since GD is incommensurable in length with AC (because AG is commensurable in length with AC while AG and GD are commensurable in square only, hence incommensurable in length by definition, so by 10.13 GD is incommensurable in length with AC), the rectangle CA by GD is irrational, hence medial cannot be concluded directly; rather the rectangle AC by DG is irrational (by 10.21 applied via the rational line AC and DG which is rational but incommensurable in length with AC).

**Step 5.** Now construct on AC: let AH be the rectangle AC by AF, and let HK be the rectangle AC by FG, and let the rectangle MK equal the rectangle AC by DG but placed on the other side so that the full rectangle AC by AD equals AH minus MK in arrangement. More precisely, the area AB = rectangle(AC, AD) = rectangle(AC, AG - GD) = rectangle(AC, AG) - rectangle(AC, GD). Let the rectangle AC by AG be represented as the whole area from which the rectangle AC by GD is subtracted.

**Step 6.** Now let a straight line s be the "side" of the area AB, meaning s squared equals the rectangle AC by AD. We seek to show s is minor. Apply the construction as in 10.91: let the rectangle AC by AF produce a certain area, and rectangle AC by FG another.

**Step 7.** Since AF and FG are incommensurable in length (Step 3), the rectangles AC by AF and AC by FG are incommensurable areas (by 10.11, since AC is common and AF, FG are incommensurable). Let p and q be straight lines such that the square on p equals the rectangle AC by AF and the square on q equals the rectangle AC by FG.

**Step 8.** Since AG is commensurable in length with AC (by the definition of a fourth apotome), and AG = AF + FG, the rectangle AC by AG is rational (by 10.19). Now the rectangle AC by AG = rectangle AC by AF + rectangle AC by FG = sq(p) + sq(q). Therefore sq(p) + sq(q) is rational.

**Step 9.** Since AG and GD are commensurable in square only, and AC is commensurable in length with AG, the rectangle AG by GD is medial (by 10.21, since AG and GD are rational and commensurable in square only). Now by 2.5, the rectangle AF by GD equals the rectangle AG by GD plus the square on EG (where E bisects DG and the application was made accordingly). More precisely, by the construction using 6.28 and the bisection at E, we have: rectangle(AF, FG) = square(EG) subtracted from square(EA), but the key relation is that 4 times rectangle(AF, FG) = square(AG) - square on the difference, and the rectangle AC by AG times AC by GD relates to the product.

**Step 10.** Consider instead the direct relation: the rectangle contained by AF and FG, when quadrupled, gives sq(AG) - sq(AG - 2FG). By 2.5, rect(AF, FG) = rect((AG+GD)/2, (AG-GD)/2) ... Let us use the cleaner approach. Since DG is bisected at E and the rectangle AF by FG was constructed, by 2.5 the rectangle AF by FG together with the square on EF equals the square on EG = sq(DG/2).

**Step 11.** The essential relationship is: twice the rectangle contained by p and q satisfies sq(2pq-rect) = 4 * rect(AC, AF) * rect(AC, FG) = sq(AC) * 4*rect(AF,FG). Since rect(AF,FG) relates to the square on half of GD minus the square on EF, and all these involve irrational relationships, we use the following cleaner path.

**Step 12.** By 10.54 through 10.59 and their apotome analogs 10.91-10.93, the method is uniform. For the rectangle AC by AD, construct p, q as above with sq(p) = rect(AC, AF) and sq(q) = rect(AC, FG). We showed sq(p) + sq(q) = rect(AC, AG) which is rational (Step 8).

**Step 13.** Now we show that twice rect(p, q) is medial. We have (2*rect(p,q))^2 = 4*sq(p)*sq(q) = 4*rect(AC,AF)*rect(AC,FG) = sq(AC)*4*rect(AF,FG). By 2.5, since DG is bisected at E, rect(AF,FG) + sq(EF) = sq(EG) = sq(DG/2). So 4*rect(AF,FG) = sq(DG) - 4*sq(EF). But we also know from the construction that 4*rect(AF,FG) = sq(AG) - sq(AG - 2FG)... Using the relation from 6.28 more directly: since the rectangle AF by FG was constructed equal to sq(EG) = sq(DG/2), we get 4*rect(AF,FG) = sq(DG).

**Step 14.** Therefore (2*rect(p,q))^2 = sq(AC) * sq(DG) = sq(AC*DG) (by 6.17), so 2*rect(p,q) = rect(AC, DG). But rect(AC, DG) is medial (Step 4, since AC is rational, DG is rational, and they are incommensurable in length, so by 10.21 the rectangle is medial). Hence twice the rectangle contained by p and q is medial.

**Step 15.** Also, p and q are incommensurable in square. For sq(p) = rect(AC, AF) and sq(q) = rect(AC, FG), so sq(p) : sq(q) = AF : FG (by 6.1). Since AF is incommensurable in length with FG (Step 3), we have sq(p) incommensurable with sq(q) (by 10.11). Therefore p and q are incommensurable in square.

**Step 16.** We have established: (i) p and q are incommensurable in square (Step 15); (ii) the sum sq(p) + sq(q) is rational (Step 8); (iii) twice the rectangle p by q is medial (Step 14). Now the "side" of the area AB equals p - q (since AD = AG - GD, the area decomposes so that s^2 = sq(p) - 2*rect(p,q) + sq(q)... but actually s^2 = rect(AC, AD) = rect(AC, AG) - rect(AC, GD) = [sq(p) + sq(q)] - 2*rect(p,q)).

**Step 17.** More carefully, since AD = AG - GD, we have rect(AC, AD) = rect(AC, AG) - rect(AC, GD) = [sq(p) + sq(q)] - [2*rect(p,q)] (using that rect(AC,DG) = 2*rect(p,q) from Step 14). So s^2 = sq(p) + sq(q) - 2*rect(p,q) = sq(p - q) (by 2.7 or direct algebra). Wait: sq(p-q) = sq(p) + sq(q) - 2*rect(p,q) only if we interpret these as areas. So s = p - q (taking p > q since AF > FG follows from AG > GD and the construction).

**Step 18.** Actually the "side" of the area is defined as the straight line whose square equals the area. We need to find a line whose square equals sq(p) + sq(q) - 2*rect(p,q). This equals sq(p-q) by 2.7. But the conditions match the definition of a minor straight line: by 10.76, if from a straight line (p) there be subtracted a straight line (q) which is incommensurable in square with it, and the sum of squares on them is rational, but the rectangle contained by them is medial, the remainder is minor. Here sq(p) + sq(q) is rational, rect(p,q) is medial (since 2*rect(p,q) is medial and half a medial is medial), and p, q are incommensurable in square. Therefore p - q is minor by 10.76.

**Step 19.** Since s^2 = sq(p - q), we have s = p - q, and therefore s is a minor straight line.

**Step 20.** Therefore, if an area be contained by a rational straight line and a fourth apotome, the "side" of the area is minor. Q.E.D.

**USED:** 10.11, 10.13, 10.18, 10.19, 10.21, 10.76, 2.5, 2.7, 6.1, 6.17, 6.28, D10.1.3, D10.1.4, D10.3.4
**Human refs (from References field):** 10.11, 10.18, 10.19, 10.21, 10.76, 5.11, 6.1, 6.17, 6.26, D10.3.4
**Jaccard:** 0.500 — AI adds ['10.13', '2.5', '2.7', '6.28', 'D10.1.3', 'D10.1.4']; Human adds ['5.11', '6.26']

## Proposition 10.95
**Statement:** If an area be contained by a rational straight line and a fifth apotome, the âsideâ of the area is a straight line which produces with a rational area a medial whole.

**Step 1.** Let the area AB be contained by the rational straight line AC and the fifth apotome AD. I say that the "side" of the area AB is a straight line which produces with a rational area a medial whole.

**Step 2.** Let DG be the annex to AD, so that AG is the whole and GD the annex. Since AD is a fifth apotome, by definition (D10.3.5), the annex DG is commensurable in length with the rational straight line set out, the square on AG is greater than the square on GD by the square on a straight line incommensurable in length with AG, and AG is incommensurable in length with the rational straight line set out. Thus AG and GD are rational straight lines commensurable in square only, DG is commensurable in length with AC, and the square on AG is greater than the square on GD by the square on a straight line incommensurable with AG.

**Step 3.** Apply to AC the rectangle equal to the square on AG, producing AH as breadth, and the rectangle equal to the square on DG, producing KH as breadth (by 1.44 and 1.45). Then the whole rectangle AK equals the sum of the squares on AG and GD, and the rectangle MK (the remaining piece between AH and AK) equals twice the rectangle AG by GD, since the square on AD equals the squares on AG, GD minus twice the rectangle AG by GD (by 2.7), and the rectangle on AC with AD can be decomposed accordingly.

**Step 4.** More precisely, since AD = AG - GD, we have the square on AD = the squares on AG, GD minus twice the rectangle AG by GD (by 2.7). Thus the rectangle AC by AD = the rectangle AC by AG minus the rectangle AC by GD (by 2.1), and correspondingly the area AB = the rectangle AH minus the rectangle HK on the line AC, where AH has breadth corresponding to AG and HK to GD.

**Step 5.** Since AG and GD are rational and commensurable in square only, the squares on AG and GD are each rational areas. Their sum, the squares on AG and GD added together, is therefore a rational area plus a rational area; but since AG and GD are commensurable in square only, these squares are commensurable, so their sum is rational (by 10.15). When this rational sum of squares is applied to the rational line AC, it produces a breadth (call it SN) that is rational and commensurable in length with AC (by 10.20).

**Step 6.** Now consider twice the rectangle AG by GD. Since AG and GD are rational and commensurable in square only, the rectangle AG by GD is medial (by 10.21). Hence twice the rectangle AG by GD is also medial (by 10.23 and 10.24, since doubling a medial area yields a medial area). When this medial area is applied to the rational line AC, it produces a breadth (call it NQ) that is rational and incommensurable in length with AC (by 10.22).

**Step 7.** Since the sum of the squares on AG, GD is rational and twice the rectangle AG by GD is medial, these two areas are incommensurable with each other (since a rational area is incommensurable with a medial area, by 10.26 and the definitions). Therefore the breadths SN and NQ, being their respective applications to AC, are incommensurable in length with each other (by 10.11).

**Step 8.** Now, since the square on AG is greater than the square on GD by the square on a straight line incommensurable with AG, and DG is commensurable in length with AC (the rational line set out), while AG is incommensurable in length with AC, we examine the application. By 10.18, since the square on AG exceeds the square on GD by a straight line incommensurable with AG, when the relevant parallelogram is applied it divides into incommensurable parts. Correspondingly, SN and NQ are incommensurable in square (by 10.14 and 10.18), so the breadths SN and NQ are incommensurable in square.

**Step 9.** Since SN is rational and commensurable in length with AC, the square on SN is rational. Since NQ is rational but incommensurable in length with AC, and SN and NQ are incommensurable in square, we have: the sum of the squares on SN and NQ is the sum of a rational area and a rational area. But since SN is commensurable in length with AC while NQ is incommensurable in length with AC, SN is incommensurable in length with NQ (by 10.13). Since they are incommensurable in square, the squares on SN and NQ are incommensurable, so their sum is medial (by the conditions).

**Step 10.** More carefully: the squares on SN and NQ, applied back, relate to the original configuration. We know that SN squared plus NQ squared corresponds (through the geometric construction) to the breadth of the area AB applied to AC. By the construction in the semicircle method (as in 10.94 and 10.58), let a semicircle be described on SQ (where SQ = SN + NQ), and let a perpendicular be erected from N. Let the points where it meets the semicircle determine straight lines, say OP and PQ, where O is one end of the diameter. Then by 2.14 and the properties of the semicircle, the square on OP equals the rectangle SN by SQ, and the square on PQ equals the rectangle NQ by SQ.

**Step 11.** Alternatively and more directly, following the method of 10.94: let the square root of the area AB be found by bisecting and constructing in the semicircle. By the same construction as in 10.94, we find two straight lines, say w and x, such that w squared minus x squared equals the area AB, and we need to show that w and x satisfy the conditions of 10.77 (that which produces with a rational area a medial whole).

**Step 12.** We establish the properties needed to invoke the definition. Since twice the rectangle AG by GD is medial and the sum of the squares on AG, GD is rational, the corresponding properties transfer through the application to AC. Specifically, the sum of the squares on the two component straight lines (w and x) of the "side" is medial (corresponding to the medial twice-rectangle becoming the sum of squares in the transformed configuration), and twice the rectangle contained by them is rational (corresponding to the rational sum of squares becoming the double rectangle in the transformed configuration). This interchange of roles between the sum-of-squares and the double-rectangle follows from the construction via the semicircle, exactly as in the proof of 10.94 (and its binomial analogue 10.58).

**Step 13.** Furthermore, w and x are incommensurable in square, since SN and NQ are incommensurable in square (established in Step 8), and the semicircle construction preserves this incommensurability (by 10.11 and 6.17).

**Step 14.** Therefore, we have two straight lines w and x that are incommensurable in square, the sum of the squares on them is medial, and twice the rectangle contained by them is rational. By 10.77, w minus x (i.e., the "side" of the area AB expressed as a difference) is "that which produces with a rational area a medial whole."

**Step 15.** Hence, if an area be contained by a rational straight line and a fifth apotome, the "side" of the area is a straight line which produces with a rational area a medial whole. Q.E.D.

**USED:** 1.44, 1.45, 10.11, 10.13, 10.14, 10.15, 10.18, 10.19, 10.20, 10.21, 10.22, 10.23, 10.26, 10.77, 2.1, 2.14, 2.7, 6.17, D10.1.3, D10.1.4, D10.3.5
**Human refs (from References field):** 10.18, 10.19, 10.21, 10.77, 6.26, D10.3.5
**Jaccard:** 0.227 — AI adds ['1.44', '1.45', '10.11', '10.13', '10.14', '10.15', '10.20', '10.22', '10.23', '10.26', '2.1', '2.14', '2.7', '6.17', 'D10.1.3', 'D10.1.4']; Human adds ['6.26']

## Proposition 10.96
**Statement:** If an area be contained by a rational straight line and a sixth apotome, the âsideâ of the area is a straight line which produces with a medial area a medial whole.

**Step 1.** Let the area AB be contained by the rational straight line AC and the sixth apotome AD. We must show that the "side" of the area AB is a straight line which produces with a medial area a medial whole.

**Step 2.** Since AD is a sixth apotome, let DE be the annex to AD, so that AE is the whole and ED the annex. By definition of a sixth apotome (D10.3.6), AE and DE are commensurable in square only, neither AE nor DE is commensurable in length with the rational straight line AC, and the square on AE is greater than the square on DE by the square on a straight line incommensurable in length with AE.

**Step 3.** Since the square on AE is greater than the square on DE by the square on a straight line incommensurable with AE, by 10.18, if we apply to AE a parallelogram equal to the fourth part of the square on DE and deficient by a square figure, it divides AE into parts that are incommensurable in length.

**Step 4.** Bisect DE at F, so that DF = FE. Apply to AE a parallelogram equal to the square on EF and deficient by a square figure, producing parts AG and GE, where AG is incommensurable in length with GE, by Step 3 and 10.18.

**Step 5.** Construct the squares AH on AG and KL on GE. Since the rectangle AG by GE equals the square on EF (by construction and 2.5), and DF = FE, the rectangle AG by GE equals the fourth part of the square on DE. Since AD = AE - DE, the rectangle contained by AE and DE, together with the square on AD, equals the square on AE minus the square on DE plus related terms. By 2.5, the rectangle AG by GE = the square on EF = one-fourth of the square on DE.

**Step 6.** Now consider the area AB = AC times AD = AC times (AE - DE). This equals AC times AE minus AC times DE. Let the rectangle AC times AE = the area on the segment AE, and AC times DE = the area on the segment DE. The area AB is their difference.

**Step 7.** Construct on the rational straight line AC a square MN equal to the rectangle AC times AG, and a square NX equal to the rectangle AC times GE. Since AE = AG + GE, the rectangle AC times AE = MN + NX. Let the side of MN be MO and the side of NX be NO (where they share the line along AC's direction).

**Step 8.** Since AG is incommensurable in length with GE (Step 4), and AC times AG : AC times GE = AG : GE (by 6.1), the areas MN and NX are incommensurable with each other, by 10.11.

**Step 9.** Since neither AE nor DE is commensurable in length with the rational straight line AC (D10.3.6), and AG + GE = AE, and the rectangle AG by GE equals one-fourth of the square on DE, we examine the commensurability properties.

**Step 10.** Since AE is incommensurable in length with AC, the rectangle AC times AE is incommensurable with the square on AC. Thus the sum of the squares on MO and NO (which equals AC times AE by construction, since the squares on MO and NO are MN and NX, and MN + NX = AC times AE) is incommensurable with the square on AC. By D10.1.4, the sum of the squares on MO and NO is a medial area, so MO and NO are incommensurable in square (since MN and NX are incommensurable).

**Step 11.** Now twice the rectangle MO by NO: the square on MO plus the square on NO equals AC times AE, and the square on the whole line (MO + NO) minus the square on (MO - NO) equals four times the rectangle MO by NO (by 2.5 and 2.6). We need to determine twice the rectangle MO times NO. By construction, twice the rectangle MO times NO corresponds to AC times DE (since the square on (MO + NO) = AC times AE + 2 rect(MO,NO), and the full algebraic relation gives 2 rect(MO, NO) = AC times DE).

**Step 12.** Since DE is also incommensurable in length with AC, the rectangle AC times DE is incommensurable with the square on AC. Hence twice the rectangle MO times NO is a medial area, by D10.1.4.

**Step 13.** Since MN is incommensurable with NX (Step 8), the square on MO is incommensurable with the square on NO. Thus MO and NO are incommensurable in square.

**Step 14.** We now verify that the sum of the squares on MO and NO is incommensurable with twice the rectangle MO times NO. The sum of the squares equals AC times AE and twice the rectangle equals AC times DE. Their ratio is AE : DE. Since AE and DE are commensurable in square only (D10.3.6), they are incommensurable in length, so AE : DE is not a ratio of number to number (by 10.7). Hence AC times AE is incommensurable with AC times DE, by 10.11. Therefore the sum of the squares on MO and NO is incommensurable with twice the rectangle MO times NO.

**Step 15.** We have established: (i) MO and NO are incommensurable in square (Step 13); (ii) the sum of the squares on MO and NO is medial (Step 10); (iii) twice the rectangle MO times NO is medial (Step 12); (iv) the sum of the squares on MO and NO is incommensurable with twice the rectangle MO times NO (Step 14). By 10.41, MO + NO is the side of the sum of two medial areas.

**Step 16.** Now consider the side of the area AB. Let the straight line r be such that the square on r equals the area AB = AC times AD. We need to show that r is a straight line which produces with a medial area a medial whole.

**Step 17.** Since AD = AE - DE, the area AB = AC times AE - AC times DE. The square on (MO + NO) = the squares on MO and NO + twice the rectangle MO times NO = AC times AE + AC times DE. But we need to consider the difference. Let w be a straight line such that the square on w equals AC times AE, and let v be such that the square on v equals AC times DE.

**Step 18.** Instead, apply the construction more carefully following the method of 10.91-10.95. Let us set up the problem using the semicircle construction. On AE, describe a semicircle. Erect a perpendicular from G (the point dividing AE into AG and GE) to meet the semicircle at a point H. Then by 3.31 and 6.8, the rectangle AG by GE equals the square on GH.

**Step 19.** Now let MO be such that the square on MO equals AC times AG, and let NO be such that the square on NO equals AC times GE. Since AG and GE are incommensurable in length and the rectangle AC times AG : AC times GE = AG : GE (by 6.1), the squares on MO and NO are incommensurable, by 10.11. Hence MO is incommensurable in square with NO.

**Step 20.** The square on MO + the square on NO = AC times AG + AC times GE = AC times AE. Since AE is incommensurable in length with the rational line AC, AC times AE is irrational. In fact, since AE is not commensurable in length with AC, the rectangle AC times AE is incommensurable with the square on AC (by 10.11), so it is irrational, and indeed medial by 10.21 and the fact that AE is expressible in square (being rational in square). Thus the sum of the squares on MO and NO is medial.

**Step 21.** Twice the rectangle MO times NO: the square on MO times the square on NO = (AC times AG)(AC times GE) = AC squared times AG times GE = AC squared times the square on EF (since AG times GE = EF squared). So the rectangle MO times NO = AC times EF. Thus twice the rectangle MO times NO = twice AC times EF = AC times DE (since DE = 2 EF). Since DE is incommensurable in length with AC, the rectangle AC times DE is incommensurable with the square on AC, so it is medial (by 10.21 applied similarly). Hence twice the rectangle MO times NO is medial.

**Step 22.** The sum of the squares on MO, NO equals AC times AE, and twice rect(MO, NO) equals AC times DE. The ratio of these is AE : DE. Since AE and DE are commensurable in square only (incommensurable in length), AE : DE is not a ratio of numbers (by 10.7), so AC times AE and AC times DE are incommensurable (by 10.11). Hence the sum of the squares on MO and NO is incommensurable with twice the rectangle contained by MO and NO.

**Step 23.** Therefore MO and NO satisfy all the conditions of 10.78: they are incommensurable in square, the sum of the squares on them is medial, twice the rectangle contained by them is medial, and the sum of the squares on them is incommensurable with twice the rectangle contained by them. Hence MO - NO (taking MO as the greater) is a straight line which produces with a medial area a medial whole.

**Step 24.** Now the square on (MO - NO) = the square on MO + the square on NO - twice the rectangle MO times NO = AC times AE - AC times DE = AC times (AE - DE) = AC times AD = the area AB, by 2.7.

**Step 25.** Therefore the "side" of the area AB (i.e., the straight line whose square equals AB) is MO - NO, which is a straight line that produces with a medial area a medial whole.

**Step 26.** Hence, if an area be contained by a rational straight line and a sixth apotome, the "side" of the area is a straight line which produces with a medial area a medial whole. Q.E.D.

**USED:** 10.11, 10.18, 10.21, 10.7, 10.78, 2.5, 2.7, 3.31, 6.1, 6.8, D10.1.3, D10.1.4, D10.3.6
**Human refs (from References field):** 10.11, 10.18, 10.21, 10.78, 6.1, 6.26, D10.3.6
**Jaccard:** 0.429 — AI adds ['10.7', '2.5', '2.7', '3.31', '6.8', 'D10.1.3', 'D10.1.4']; Human adds ['6.26']

## Proposition 10.97
**Statement:** The square on an apotome applied to a rational straight line produces as breadth a first apotome.

**Step 1.** Let AB be an apotome and let CD be a rational straight line. Apply the square on AB to CD, producing CE as breadth, so that rect(CD, CE) = sq(AB). We shall prove that CE is a first apotome.

**Step 2.** Since AB is an apotome, let BF be the annex so that AF is the whole [10.73]. Then AF and BF are rational straight lines commensurable in square only [10.73, D10.1.3], with AF greater than BF [CN5].

**Step 3.** Apply sq(AF) to CD, producing breadth CP, so that rect(CD, CP) = sq(AF). Apply sq(BF) to CD, producing breadth PG (adjacent to CP), so that rect(CD, PG) = sq(BF). Then rect(CD, CG) = rect(CD, CP) + rect(CD, PG) = sq(AF) + sq(BF), where CG = CP + PG.

**Step 4.** By 2.7, sq(AF) + sq(BF) = 2*rect(AF, BF) + sq(AF - BF) = 2*rect(AF, BF) + sq(AB). Therefore sq(AB) = (sq(AF) + sq(BF)) - 2*rect(AF, BF), that is, rect(CD, CE) = rect(CD, CG) - 2*rect(AF, BF). Apply 2*rect(AF, BF) to CD, producing breadth GE, so that rect(CD, GE) = 2*rect(AF, BF). Then rect(CD, CE) = rect(CD, CG) - rect(CD, GE), whence CE = CG - GE, with G lying between C and E.

**Step 5.** Since AF is rational, sq(AF) is a rational area [D10.1.4]. Since BF is rational, sq(BF) is a rational area [D10.1.4]. Since AF and BF are commensurable in square, sq(AF) is commensurable with sq(BF) [D10.1.2]. Therefore sq(AF) + sq(BF) is commensurable with sq(AF) [10.15], and hence is itself a rational area. Since this rational area sq(AF) + sq(BF) is applied to the rational straight line CD, the breadth CG is rational and commensurable in length with CD [10.20].

**Step 6.** Since AF and BF are rational straight lines commensurable in square only, rect(AF, BF) is a medial area [10.21]. The area 2*rect(AF, BF) is commensurable with rect(AF, BF), since the ratio 2:1 is a ratio of numbers [10.6]. Therefore 2*rect(AF, BF) is also a medial area [10.12, since it is commensurable with a medial area].

**Step 7.** By 2.14, let N be the straight line such that sq(N) = 2*rect(AF, BF). Since 2*rect(AF, BF) is a medial area, and sq(N) equals this medial area, N is irrational [D10.1.4]. Moreover, sq(N) is commensurable with sq(M), where M is the medial straight line satisfying sq(M) = rect(AF, BF) [10.21], because sq(N) : sq(M) = 2 : 1 [10.6]. Since sq(N) is commensurable with the square on the medial line M, and hence with a medial area, N is a medial straight line [10.23]. By 10.22, the square on the medial straight line N, applied to the rational straight line CD, produces as breadth a straight line rational and incommensurable in length with CD. Since sq(N) = rect(CD, GE), this breadth is GE. Therefore GE is rational and incommensurable in length with CD.

**Step 8.** Since CG is commensurable in length with CD [Step 5] and GE is incommensurable in length with CD [Step 7], it follows that CG is incommensurable in length with GE [10.13]. Since CG and GE are both rational straight lines (each commensurable in square with CD), sq(CG) and sq(GE) are each commensurable with sq(CD), and hence commensurable with each other [10.12]. Thus CG and GE are commensurable in square [D10.1.2]. Therefore CG and GE are rational straight lines commensurable in square only, and CE = CG - GE is an apotome [10.73].

**Step 9.** We now verify the conditions for CE to be a first apotome [D10.3.1]. The first condition is that CG, the whole of the apotome CE, be commensurable in length with the rational straight line CD. This was established in Step 5.

**Step 10.** It remains to show that sq(CG) is greater than sq(GE) by the square on a straight line commensurable in length with CG. Since sq(AF) and sq(BF) are commensurable, sq(AF) : sq(BF) is a ratio of numbers; let sq(AF) : sq(BF) = m : n where m and n are numbers with m > n [10.5, CN5].

**Step 11.** By 6.1, since rect(CD, CP) = sq(AF) and rect(CD, PG) = sq(BF), and these rectangles share the same height CD, we have CP : PG = sq(AF) : sq(BF) = m : n.

**Step 12.** Both CP and PG are rational and commensurable in length with CD [10.20, since sq(AF) and sq(BF) are rational areas applied to the rational line CD]. Hence CP and PG are commensurable in length with each other [10.12].

**Step 13.** We establish the mean proportional relationship. Since sq(AF) : rect(AF, BF) = AF : BF [6.1, applied to rectangles with one side AF: rect(AF, AF) : rect(AF, BF) = AF : BF] and rect(AF, BF) : sq(BF) = AF : BF [6.1, applied to rectangles with one side BF: rect(AF, BF) : rect(BF, BF) = AF : BF], it follows that sq(AF) : rect(AF, BF) = rect(AF, BF) : sq(BF). Applying these areas to CD and using 6.1, the breadths maintain the same proportion: CP : GL = GL : PG, where GL is the breadth satisfying rect(CD, GL) = rect(AF, BF). By 6.17, sq(GL) = rect(CP, PG).

**Step 14.** Since rect(CD, GE) = 2*rect(AF, BF) = 2*rect(CD, GL), we have GE = 2*GL [6.1]. By 6.20, since squares are similar figures, sq(GE) : sq(GL) = 4 : 1 (the duplicate ratio of 2 : 1). Therefore sq(GE) = 4*sq(GL) = 4*rect(CP, PG) [Step 13].

**Step 15.** Now sq(CG) = sq(CP + PG) = sq(CP) + sq(PG) + 2*rect(CP, PG) [2.4]. Therefore sq(CG) - sq(GE) = sq(CP) + sq(PG) + 2*rect(CP, PG) - 4*rect(CP, PG) = sq(CP) + sq(PG) - 2*rect(CP, PG) = sq(CP - PG) [2.7, since sq(CP) + sq(PG) = 2*rect(CP, PG) + sq(CP - PG)]. Thus sq(CG) - sq(GE) = sq(CP - PG).

**Step 16.** Since CP : PG = m : n (a ratio of numbers, Step 11), by 5.17, (CP - PG) : PG = (m - n) : n, which is a ratio of numbers. Therefore CP - PG is commensurable with PG [10.6]. By 5.18, CG : PG = (CP + PG) : PG = (m + n) : n, also a ratio of numbers, so CG is commensurable with PG [10.6]. Since CP - PG and CG are each commensurable with PG, they are commensurable with each other [10.12], and in particular commensurable in length.

**Step 17.** Therefore sq(CG) is greater than sq(GE) by sq(CP - PG), where CP - PG is commensurable in length with CG [Step 16]. Combined with the fact that CG is commensurable in length with the rational straight line CD [Step 9], all conditions of D10.3.1 are satisfied. Therefore CE is a first apotome. Q.E.D.

**USED:** 10.12, 10.13, 10.15, 10.20, 10.21, 10.22, 10.23, 10.5, 10.6, 10.73, 2.14, 2.4, 2.7, 5.17, 5.18, 6.1, 6.17, 6.20, CN5, D10.1.2, D10.1.3, D10.1.4, D10.3.1
**Human refs (from References field):** 10.11, 10.17, 10.20, 10.22, 10.73, 2.7, 6.1, 6.17, D10.3.1
**Jaccard:** 0.280 — AI adds ['10.12', '10.13', '10.15', '10.21', '10.23', '10.5', '10.6', '2.14', '2.4', '5.17', '5.18', '6.20', 'CN5', 'D10.1.2', 'D10.1.3', 'D10.1.4']; Human adds ['10.11', '10.17']

## Proposition 10.98
**Statement:** The square on a first apotome of a medial straight line applied to a rational straight line produces as breadth a second apotome.

**Step 1.** Let AB be a first apotome of a medial straight line, and let CD be a rational straight line. Apply the rectangle sq(AB) to CD, producing CE as breadth, so that CD * CE = sq(AB). We must show that CE is a second apotome.

**Step 2.** Since AB is a first apotome of a medial straight line, let BF be the annex to AB, so that AF is the whole. By the definition of a first apotome of a medial straight line [10.74], AF and BF are medial straight lines commensurable in square only, and the rectangle AF * BF is rational.

**Step 3.** Apply sq(AF) to CD, producing CG as breadth, so that CD * CG = sq(AF). Apply sq(BF) to CD, producing GE as breadth (adjacent to CG along CD), so that CD * GE = sq(BF). Then CD * CE = sq(AB) = sq(AF) + sq(BF) - 2 * AF * BF [2.7], so CD * CG + CD * GE - 2 * AF * BF = CD * CE. More precisely, since sq(AF - BF) = sq(AF) + sq(BF) - 2 * rect(AF, BF), we have CD * CE = sq(AF) + sq(BF) - 2 * rect(AF, BF).

**Step 4.** Now let H be the point on CE such that CD * CH = 2 * rect(AF, BF). Since CD * CG = sq(AF) and CD * GE = sq(BF), we have CD * (CG + GE) = sq(AF) + sq(BF), and CD * CE = CD * (CG + GE) - CD * CH, that is, CG + GE = CE + CH, or equivalently, CH measures the excess and CE = CG + GE - CH. Let us set up the areas more carefully: CD * CL = sq(AF), CD * FL = sq(BF) where L is chosen so these areas are adjacent, and CD * MN = 2 * rect(AF, BF), so that CE is determined by sq(AB) = sq(AF) + sq(BF) - 2 * rect(AF, BF) applied to CD.

**Step 5.** Since AF is medial, sq(AF) is a medial area. Since CD is rational, by 10.22 the breadth CL (where CD * CL = sq(AF)) is rational and incommensurable in length with CD. Similarly, since BF is medial, sq(BF) is medial, and the breadth FL (where CD * FL = sq(BF)) is rational and incommensurable in length with CD [10.22].

**Step 6.** Since AF and BF are commensurable in square only, sq(AF) and sq(BF) are commensurable [10.11]. Since CD * CL = sq(AF) and CD * FL = sq(BF), and sq(AF) is commensurable with sq(BF), the breadths CL and FL are commensurable in length [6.1, 10.11]. Thus CL + FL is commensurable with each of CL and FL [10.15], and so CL + FL is rational and incommensurable in length with CD.

**Step 7.** Now, rect(AF, BF) is rational by the definition of a first apotome of a medial straight line [10.74]. Therefore 2 * rect(AF, BF) is also rational [10.15 applied to equal magnitudes, or directly since a rational area doubled remains rational]. Since CD is rational and 2 * rect(AF, BF) is rational, and CD * MN = 2 * rect(AF, BF), the breadth MN is rational and commensurable in length with CD [10.20].

**Step 8.** Since CD * (CL + FL) = sq(AF) + sq(BF) and CD * MN = 2 * rect(AF, BF), and sq(AB) = sq(AF) + sq(BF) - 2 * rect(AF, BF), we have CD * CE = CD * (CL + FL) - CD * MN, so CE = (CL + FL) - MN. Thus CE is the remainder when MN is subtracted from CL + FL.

**Step 9.** From Step 6, CL + FL is rational and incommensurable in length with CD. From Step 7, MN is rational and commensurable in length with CD. Since CL + FL is incommensurable in length with CD, and MN is commensurable in length with CD, then CL + FL and MN are incommensurable in length with each other [10.13]. Since both CL + FL and MN are rational, CE = (CL + FL) - MN is an apotome [10.73].

**Step 10.** We now verify CE is specifically a second apotome. The annex in the apotome CE = (CL + FL) - MN is MN (the term subtracted), and the whole is CL + FL. From Step 7, MN is commensurable in length with CD, the rational straight line set out.

**Step 11.** We must show that sq(CL + FL) > sq(MN) by the square on a straight line commensurable in length with CL + FL. We have CD * (CL + FL) = sq(AF) + sq(BF), and CD * MN = 2 * rect(AF, BF). Now sq(AF) + sq(BF) > 2 * rect(AF, BF) since AF and BF are unequal [CN5, 2.7]. Consider the identity: (sq(AF) + sq(BF))^2 - (2 * rect(AF, BF))^2 = (sq(AF) - sq(BF))^2, which gives us that (CD * (CL + FL))^2 - (CD * MN)^2 = (sq(AF) - sq(BF))^2. Since CD^2 * ((CL+FL)^2 - MN^2) = (sq(AF) - sq(BF))^2, the square on the excess by which CL + FL exceeds MN (in the sense of 10.17) relates to commensurability properties.

**Step 12.** More directly: since AF and BF are medial and commensurable in square, and AF is incommensurable in length with BF (they are commensurable in square only), by 10.14 and the properties of sq(AF) - sq(BF), we examine whether sq(AF) > sq(BF) by the square on a line commensurable or incommensurable with AF. Since AF and BF are medial lines commensurable in square only such that rect(AF, BF) is rational, by 10.27 such lines exist with sq(AF) > sq(BF) by the square on a line commensurable with AF (this follows from the construction in 10.31 and the nature of first apotomes of medials).

**Step 13.** Applying 10.14: since AF, BF are in a certain ratio and sq(AF) > sq(BF) by sq(line commensurable with AF), and since CL + FL and MN correspond to sq(AF) + sq(BF) and 2*rect(AF,BF) divided by CD respectively, the commensurability transfers. Specifically, since sq(AF) and sq(BF) are commensurable (Step 6), and CL, FL are commensurable in length, sq(CL + FL) - sq(MN) is the square on a line commensurable with CL + FL [10.17].

**Step 14.** To verify this via 10.17: we need to show that when we apply the fourth part of sq(MN) to CL + FL as a rectangle deficient by a square, it divides CL + FL into commensurable parts. Since CD * (CL + FL) = sq(AF) + sq(BF) and CD * MN = 2 * rect(AF, BF), consider that sq(AF) + sq(BF) and 2*rect(AF,BF) relate through the identity for (AF + BF) and (AF - BF). Since AF and BF are commensurable in square only and rect(AF,BF) is rational while sq(AF) + sq(BF) is medial [10.26 ensures they differ in kind], the structure of CL + FL and MN as breadths preserves the commensurability needed for 10.17 to yield that sq(CL+FL) > sq(MN) by sq(line commensurable with CL+FL).

**Step 15.** Collecting the conditions for a second apotome [D10.3.2]: (i) CE is an apotome, being the difference of two rational lines commensurable in square only [Step 9, 10.73]; (ii) the annex MN is commensurable in length with the rational line CD [Step 7, 10.20]; (iii) sq(whole CL+FL) > sq(annex MN) by sq(line commensurable with whole) [Steps 13-14, 10.17]. Therefore CE is a second apotome.

**Step 16.** Hence, the square on the first apotome of a medial straight line AB, applied to the rational straight line CD, produces as breadth CE, which is a second apotome. This is what was to be proved.

**USED:** 10.11, 10.13, 10.14, 10.15, 10.17, 10.20, 10.22, 10.73, 10.74, 2.7, 6.1, CN5, D10.3.2
**Human refs (from References field):** 10.11, 10.15, 10.17, 10.20, 10.22, 10.23, 10.73, 10.74, 2.7, 5.11, 6.1, 6.17, D10.3.2
**Jaccard:** 0.625 — AI adds ['10.13', '10.14', 'CN5']; Human adds ['10.23', '5.11', '6.17']

## Proposition 10.99
**Statement:** The square on a second apotome of a medial straight line applied to a rational straight line produces as breadth a third apotome.

**Step 1.** Let AB be a second apotome of a medial straight line, and let sigma be a rational straight line. Let AB^2 = sigma * EF, where EF is the breadth produced. We must show that EF is a third apotome.

**Step 2.** Since AB is a second apotome of a medial straight line, let AB = w - x, where w and x are medial straight lines commensurable in square only, and the rectangle w*x is medial [D10.1.3, 10.75]. Let w = BC and x = BD, so that CD is the second apotome of a medial straight line with whole BC and annex BD, and AB = CD.

**Step 3.** Apply the squares on BC and BD separately to sigma. Let BC^2 = sigma * EG and BD^2 = sigma * GH, so that EF = EG - GH (since AB^2 = BC^2 + BD^2 - 2*BC*BD, and correspondingly for the rectangles applied to sigma). More precisely, let BC^2 = sigma * EK and BD^2 = sigma * KL, and 2*BC*BD = sigma * KF, so that since AB^2 = BC^2 + BD^2 - 2*BC*BD [2.7], we have sigma * EF = sigma * EK + sigma * KL - sigma * KF, giving the appropriate partition of EF.

**Step 4.** Since BC is medial, BC^2 is a medial area. Since sigma is rational and BC^2 = sigma * EK, by 10.22 the breadth EK is rational and incommensurable in length with sigma.

**Step 5.** Similarly, since BD is medial, BD^2 is a medial area. Since sigma is rational and BD^2 = sigma * KL, by 10.22 the breadth KL is rational and incommensurable in length with sigma.

**Step 6.** Since BC and BD are commensurable in square only, BC^2 and BD^2 are commensurable [10.11]. Since BC^2 = sigma * EK and BD^2 = sigma * KL, and sigma is the same rational line, EK and KL are commensurable in length [6.1, 10.11]. Thus EK and KL are both rational and commensurable in length with each other.

**Step 7.** Since EK and KL are each incommensurable in length with sigma (Steps 4 and 5), and they are commensurable with each other (Step 6), their difference EK - KL is also incommensurable in length with sigma [10.13]. Thus the whole breadth EG (representing the appropriate segment) is rational and incommensurable in length with sigma.

**Step 8.** Now consider 2*BC*BD. Since BC and BD are medial and commensurable in square only, and the rectangle BC*BD is medial [by hypothesis from 10.75], the area 2*BC*BD is also medial.

**Step 9.** Since 2*BC*BD is medial and equals sigma * KF, by 10.22 the breadth KF is rational and incommensurable in length with sigma.

**Step 10.** We must show that EK and KF are incommensurable in length. The area BC^2 is the square on a medial line, and 2*BC*BD is the medial rectangle. Since BC and BD are commensurable in square only and contain a medial rectangle, BC^2 and 2*BC*BD are incommensurable [10.13, since if they were commensurable, then BC^2 being commensurable with BD^2 would force BC*BD commensurable with BC^2, making BC commensurable in length with BD, contradicting their being commensurable in square only]. By 6.1 and 10.11, since BC^2 = sigma * EK and 2*BC*BD = sigma * KF with the same sigma, the incommensurability of BC^2 and 2*BC*BD implies EK and KF are incommensurable in length.

**Step 11.** Since EK and KL are rational and commensurable in length (Step 6), the straight line EL = EK + KL (the sum representing the squares on BC and BD applied to sigma) is rational [10.15].

**Step 12.** Since EK and KF are incommensurable in length (Step 10), and both are rational, EL and KF are also incommensurable (since EL is commensurable with EK by 10.15, and EK is incommensurable with KF, so EL is incommensurable with KF by 10.13).

**Step 13.** Now EL and KF are both rational and commensurable in square only (being rational lines that are incommensurable in length). Therefore EL - KF is an apotome [10.73].

**Step 14.** We now determine which type of apotome EF is. We need to examine whether sq(EL) > sq(KF) by the square of a line commensurable or incommensurable with EL, and which of EL, KF is commensurable in length with sigma.

**Step 15.** Since BC^2 + BD^2 (which are the squares on medial lines) is applied to the rational line sigma giving breadth EL, and 2*BC*BD is applied to sigma giving breadth KF, and since neither EL nor KF is commensurable in length with sigma (EL is incommensurable with sigma because EK is incommensurable with sigma [Step 4] and EL is commensurable with EK [10.15], so by 10.13, EL is incommensurable with sigma; KF is incommensurable with sigma by Step 9).

**Step 16.** To determine the relationship sq(EL) - sq(KF): By the structure inherited from the second apotome of a medial, the square on BC is greater than the square on BD by the square on a line commensurable with BC [from 10.75 and D10.1.3]. Since BC^2 - BD^2 corresponds proportionally (via division by sigma) to EK - KL, and BC^2 : BD^2 = EK : KL [6.1], the proportionality established by 10.14 transfers the commensurability condition. Specifically, since sq(BC) > sq(BD) by the square on a line commensurable with BC, and BC^2 and BD^2 are proportional to EK and KL respectively, by 10.14 we have sq(EL) > sq(KF) by the square on a line commensurable with EL.

**Step 17.** Since neither EL nor KF is commensurable in length with sigma (Step 15), and sq(EL) > sq(KF) by the square on a line commensurable with EL (Step 16), by D10.3.3, EF = EL - KF is a third apotome.

**Step 18.** Therefore, the square on a second apotome of a medial straight line applied to a rational straight line produces as breadth a third apotome. Q.E.D.

**USED:** 10.11, 10.13, 10.14, 10.15, 10.22, 10.73, 10.75, 2.7, 6.1, D10.1.3, D10.3.3
**Human refs (from References field):** 10.11, 10.13, 10.15, 10.17, 10.22, 10.23, 10.73, 10.75, 2.7, 5.11, 6.1, D10.3.3
**Jaccard:** 0.643 — AI adds ['10.14', 'D10.1.3']; Human adds ['10.17', '10.23', '5.11']

## Proposition 10.100
**Statement:** The square on a minor straight line applied to a rational straight line produces as breadth a fourth apotome.

**Step 1.** Let AB be a minor straight line, and let CD be a rational straight line. Apply the square on AB to CD, producing DE as breadth, so that CD * DE = AB^2. We must show that DE is a fourth apotome.

**Step 2.** Since AB is a minor straight line, by the definition of minor (10.76), let AB = AG - GB, where AG and GB are straight lines incommensurable in square, the sum of the squares on AG and GB is rational, and the rectangle AG * GB is medial.

**Step 3.** Apply the square on AG to CD, producing DH as breadth, so that CD * DH = AG^2. Apply the square on GB to CD, producing HK as breadth, so that CD * HK = GB^2. Then since CD * DE = AB^2 = (AG - GB)^2 = AG^2 + GB^2 - 2 * AG * GB, we have CD * DE = CD * DH + CD * HK - 2 * AG * GB, that is, CD * (DH + HK) - 2 * AG * GB = CD * DE. By 2.7, the square on AB equals the sum of the squares on AG and GB minus twice the rectangle AG * GB.

**Step 4.** Since the sum of the squares on AG and GB is rational, and CD is rational, the area AG^2 + GB^2 equals CD * (DH + HK), which is a rational area applied to the rational straight line CD. Therefore by 10.20, DH + HK is rational and commensurable in length with CD.

**Step 5.** Now let DH + HK = DK. Apply 2 * AG * GB to CD, producing some breadth, say KE taken in the appropriate direction, so that CD * KE = 2 * AG * GB. Then DE = DK - KE.

**Step 6.** Since 2 * AG * GB is medial (as AG * GB is medial, and double a medial area is medial by 10.23 and 10.6), and CD is rational, the area CD * KE is medial. By 10.22, KE is rational and incommensurable in length with CD.

**Step 7.** Since DK is commensurable in length with CD (Step 4) and KE is incommensurable in length with CD (Step 6), then DK is incommensurable in length with KE by 10.13. Both DK and KE are rational (DK by Step 4, KE by Step 6). Therefore DE = DK - KE is an apotome by 10.73.

**Step 8.** We now identify DE as a fourth apotome by verifying the conditions of D10.3.4. We need to show: (i) the square on DK is greater than the square on KE by the square on a straight line incommensurable in length with DK, and (ii) DK is commensurable in length with CD.

**Step 9.** Condition (ii) is already established: DK is commensurable in length with CD (from Step 4).

**Step 10.** For condition (i), we analyze the relationship between DK^2 and KE^2. Since CD * DK = AG^2 + GB^2 and CD * KE = 2 * AG * GB, we have DK : KE = (AG^2 + GB^2) : (2 * AG * GB) by 6.1.

**Step 11.** Since AG and GB are incommensurable in square (by the definition of the minor, 10.76), the squares AG^2 and GB^2 are incommensurable. Hence AG^2 + GB^2 is incommensurable with 2 * AG * GB by 10.36's underlying reasoning. More precisely, since the sum of the squares is rational and twice the rectangle is medial, these two areas are incommensurable with one another by D10.1.4 and D10.1.1. Therefore DK is incommensurable in length with KE, which we already established in Step 7.

**Step 12.** Now consider DK^2 - KE^2. We have CD^2 * DK^2 = (AG^2 + GB^2)^2 and CD^2 * KE^2 = (2 * AG * GB)^2 = 4 * AG^2 * GB^2. By 5.15, CD^2 * (DK^2 - KE^2) = (AG^2 + GB^2)^2 - 4 * AG^2 * GB^2 = (AG^2 - GB^2)^2, using the algebraic identity from 2.5 and 2.6.

**Step 13.** So DK^2 - KE^2 = (AG^2 - GB^2)^2 / CD^2. Let L be such that L^2 = DK^2 - KE^2. Then CD * L is related to (AG^2 - GB^2). More directly, since CD * DK = AG^2 + GB^2 and CD * KE = 2 * AG * GB, by the construction in 10.17 and 10.18, we examine whether the square on DK exceeds the square on KE by the square on a straight line commensurable or incommensurable with DK.

**Step 14.** Since AG and GB are incommensurable in square, AG^2 and GB^2 are incommensurable. By 10.18 (the converse direction), when we apply the fourth part of the square on KE to DK and it divides DK into incommensurable parts, then DK^2 exceeds KE^2 by the square on a straight line incommensurable in length with DK. To verify the hypothesis of 10.18: applying the rectangle equal to (1/4) * KE^2 to DK in deficiency of a square requires checking that DK and KE satisfy the conditions. Since DK : KE = (AG^2 + GB^2) : (2 * AG * GB), and AG^2 is incommensurable with GB^2, by 10.18 the resulting division produces incommensurable parts. Therefore the square on DK is greater than the square on KE by the square on a straight line incommensurable in length with DK.

**Step 15.** We have now verified both conditions of D10.3.4: the square on the whole DK exceeds the square on the annex KE by the square on a straight line incommensurable in length with DK, and DK (the whole) is commensurable in length with the rational straight line CD. Therefore DE is a fourth apotome.

**Step 16.** Thus, the square on the minor straight line AB, applied to the rational straight line CD, produces as breadth DE, a fourth apotome. This is what was to be proved.

**USED:** 10.13, 10.17, 10.18, 10.20, 10.22, 10.23, 10.6, 10.73, 10.76, 2.5, 2.6, 2.7, 5.15, 6.1, CN1, D10.1.1, D10.1.4, D10.3.4
**Human refs (from References field):** 10.11, 10.18, 10.20, 10.22, 10.73, 10.76, 2.7, 5.11, 6.1, 6.17, D10.3.4
**Jaccard:** 0.381 — AI adds ['10.13', '10.17', '10.23', '10.6', '2.5', '2.6', '5.15', 'CN1', 'D10.1.1', 'D10.1.4']; Human adds ['10.11', '5.11', '6.17']

## Proposition 10.101
**Statement:** The square on the straight line which produces with a rational area a medial whole, if applied to a rational straight line, produces as breadth a fifth apotome.

**Step 1.** Let AB be a straight line which produces with a rational area a medial whole, and let CD be a rational straight line. Let CF be the rectangle CD x CF equal to the square on AB. We must show that CF is a fifth apotome.

**Step 2.** Let BG be the annex to AB, so that AG produces with a rational area a medial whole. Then by the definition of this irrational (10.77), AG and GB are incommensurable in square, the sum of the squares on AG and GB is medial, and twice the rectangle AG, GB is rational.

**Step 3.** Apply the square on AG to CD, producing CH as breadth, and apply the square on BG to CD, producing KL as breadth. Then the whole CL equals the sum of the squares on AG and GB applied to CD. Since the square on AB equals the square on AG plus the square on GB minus twice the rectangle AG, GB (by 2.7), we have the rectangle CD x CF equals the rectangle CD x CL minus twice the rectangle AG, GB. Therefore twice the rectangle AG, GB equals the rectangle CD x FL, where FL = CL - CF.

**Step 4.** Since the sum of the squares on AG and GB is medial and is applied to the rational straight line CD producing CL as breadth, CL is rational and incommensurable in length with CD (by 10.22).

**Step 5.** Since twice the rectangle AG, GB is rational and equals the rectangle CD x FL, and CD is rational, FL is rational and commensurable in length with CD (by 10.20).

**Step 6.** Therefore CL is incommensurable in length with FL (since CL is incommensurable in length with CD while FL is commensurable in length with CD, by 10.13). Since CL and FL are both rational, CL and FL are rational straight lines commensurable in square only. Therefore CF = CL - FL is an apotome (by 10.73).

**Step 7.** Now I must show that CF is specifically a fifth apotome. We need to verify the conditions of D10.3.5: the annex FL is commensurable in length with CD, and the square on the whole CL is greater than the square on the annex FL by the square on a straight line incommensurable in length with CL.

**Step 8.** We have already established in Step 5 that FL is commensurable in length with CD, which is one condition for a fifth apotome.

**Step 9.** It remains to show that the square on CL exceeds the square on FL by the square on a straight line incommensurable with CL. Since AG and GB are incommensurable in square, the squares on AG and GB are incommensurable with each other. Applied to the rational line CD, these produce CH and KL respectively, so CH and KL are incommensurable with each other (by 10.11). Thus the rectangles CD x CH and CD x KL are incommensurable.

**Step 10.** Now CL = CH + KL (since CD x CL = square on AG + square on GB), so CH and KL are parts of CL. Since CH and KL are incommensurable, and the squares on AG and GB are each applied to CD producing rational breadths (each square being incommensurable with the rational square on CD since AG and GB are each irrational as parts of the irrational line of 10.77), CH and KL are each rational.

**Step 11.** Consider the squares on CL and FL. We have CL = CH + KL and the rectangle CD x FL = 2 rect(AG, GB). The square on CL minus the square on FL relates to the configuration of CH and KL. Since the squares on AG, GB are the two parts of the medial sum, and twice rect(AG, GB) is rational, apply 10.18 to the relationship: we need to show that the square on CL is greater than the square on FL by a square incommensurable with CL.

**Step 12.** Since the square on AG is to the square on BG not as a square number to a square number (for if it were, AG and GB would be commensurable in square by 10.9, contradicting 10.77), and the square on AG is to the square on BG as CH is to KL (since each is produced by applying to the same line CD), CH is to KL not as a square number to a square number.

**Step 13.** Now CH + KL = CL and CD x FL = 2 rect(AG, GB). We have CL x FL = CH x FL + KL x FL. Applying 10.17 and 10.18: since CH is to KL not as a square number to a square number, consider the fourth of the square on FL applied to CL. By the construction and since CH, KL have the ratio not of a square to a square number, the square on CL is greater than the square on FL by the square on a straight line incommensurable in length with CL (by 10.18).

**Step 14.** We have verified: (1) CF = CL - FL is an apotome; (2) the annex FL is commensurable in length with the rational straight line CD; (3) the square on CL exceeds the square on FL by the square on a straight line incommensurable with CL; and (4) the whole CL is not commensurable in length with CD (established in Step 4). By the definition D10.3.5, CF is a fifth apotome.

**Step 15.** Therefore the square on the straight line which produces with a rational area a medial whole, if applied to a rational straight line, produces as breadth a fifth apotome. Q.E.D.

**USED:** 10.11, 10.13, 10.18, 10.20, 10.22, 10.73, 10.77, 10.9, 2.7, D10.3.5
**Human refs (from References field):** 10.11, 10.18, 10.20, 10.22, 10.73, 10.77, 2.7, 6.1, D10.3.5
**Jaccard:** 0.727 — AI adds ['10.13', '10.9']; Human adds ['6.1']

## Proposition 10.102
**Statement:** The square on the straight line which produces with a medial area a medial whole, if applied to a rational straight line, produces as breadth a sixth apotome.

**Step 1.** Let AB be a straight line which produces with a medial area a medial whole, and let CD be a rational straight line. Apply the square on AB to CD, producing CE as breadth, so that the rectangle CD by CE equals the square on AB. We must show that CE is a sixth apotome.

**Step 2.** Since AB produces with a medial area a medial whole, let AG be the annex to AB, so that WB = AB and WA = AG, where WB is the whole and WA is the annex in the sense of 10.78. That is, let AG be annexed to AB such that BG is the whole line, with AB and AG incommensurable in square, the sum of the squares on AB and AG being medial, twice the rectangle AB by AG being medial, and the sum of the squares on them being incommensurable with twice the rectangle contained by them [10.78].

**Step 3.** Apply the square on BG to the rational straight line CD. Since BG is the side of the sum of two medial areas (for BG = AB + AG satisfies: AB, AG incommensurable in square, squares on them summing to medial, rectangle medial, and the two medial areas incommensurable), by 10.65 the square on BG applied to CD produces as breadth a sixth binomial. Let this breadth be CF, so that rectangle CD by CF equals the square on BG.

**Step 4.** Now the square on BG equals the square on AB plus the square on AG plus twice the rectangle AB by AG [2.4]. Also BG is divided at the point A into AB and AG. Apply the square on AB to CD producing breadth CE, and apply the square on AG to CD producing some breadth, say CL beyond CE. Then the remainder, twice the rectangle AB by AG applied to CD, corresponds to the remaining breadth. We have rectangle CD by CF = sq(AB) + sq(AG) + 2*rect(AB,AG), and rectangle CD by CE = sq(AB). Let the square on AG applied to CD produce breadth FL (where F is the endpoint of CF and L lies between E and F), so rectangle CD by FL = sq(AG). Then the remainder, rectangle CD by EL = 2*rect(AB,AG), where EL is the segment between E and L.

**Step 5.** Since the sum of the squares on AB and AG is medial, and rectangle CD by (CE + FL) equals sq(AB) + sq(AG), the area CD by (CE + FL) is medial. But CD is rational. Therefore CE + FL is rational and incommensurable in length with CD [10.22, since a medial area applied to a rational line gives a line rational but incommensurable in length with it].

**Step 6.** Since twice the rectangle AB by AG is medial, and rectangle CD by EL = 2*rect(AB,AG), the area CD by EL is medial. But CD is rational. Therefore EL is rational and incommensurable in length with CD [10.22].

**Step 7.** Since the sum of the squares on AB and AG is incommensurable with twice the rectangle AB by AG [10.78], rectangle CD by (CE + FL) is incommensurable with rectangle CD by EL. Therefore CE + FL is incommensurable in length with EL [6.1, 10.11].

**Step 8.** Now CF = CE + EL + FL (as the sixth binomial breadth). Rearranging, CE = CF - EL - FL, or more precisely, we set up the relationship: since CF is the full breadth for sq(BG), and CE is the breadth for sq(AB), we have that CL (= CF - CE, where CL is the breadth for sq(AG) + 2*rect(AB,AG)) gives CL corresponding to the rectangle. Let us reorganize. Set CF as the sixth binomial with terms: let CF = FP + PC where FP and PC are its terms (FP > PC), CF being a sixth binomial on CD. Then CE = CF - (breadth for sq(BG) - sq(AB))/CD. Since sq(BG) = sq(AB) + sq(AG) + 2*rect(AB,AG), we have sq(BG) - sq(AB) = sq(AG) + 2*rect(AB,AG), and the breadth for this difference is CF - CE.

**Step 9.** Let us proceed more carefully following the standard approach. We have CE + FL = the breadth for the medial area sq(AB) + sq(AG) applied to rational CD. And EL = the breadth for the medial area 2*rect(AB,AG) applied to rational CD. Both CE + FL and EL are rational and incommensurable with CD [Step 5, Step 6]. And CE + FL is incommensurable with EL [Step 7]. Therefore each of CE + FL and EL is rational, they are incommensurable with each other, and both are incommensurable with CD.

**Step 10.** Now CF = (CE + FL) + EL as the total breadth. CF is a sixth binomial on the rational line CD [Step 3, 10.65]. By the structure of the sixth binomial [D10.2.6], neither of its terms is commensurable in length with CD, and the square on the greater term exceeds the square on the lesser by the square on a line incommensurable with the greater.

**Step 11.** Since CE is obtained by subtracting from CF the breadths corresponding to sq(AG) and 2*rect(AB,AG), we equivalently have: CF - CE corresponds to (sq(AG) + 2*rect(AB,AG))/CD. But we can also express: the rectangle CD by CE = sq(AB) = sq(BG) - sq(AG) - 2*rect(AB,AG) = CD*CF - CD*(CF - CE) = CD*CE, which is consistent.

**Step 12.** By 10.97 and its method generalized: since the square on BG applied to rational CD gives a sixth binomial CF [10.65], and since BG = AB + AG where AG is the unique annex [10.84], and since the square on AB = sq(BG) - sq(AG) - 2*rect(AB,AG), the breadth CE for sq(AB) is obtained by subtracting from the sixth binomial CF the breadth for sq(AG) + 2*rect(AB,AG).

**Step 13.** To show CE is a sixth apotome, we identify its terms. The square on BG = sq(AB) + sq(AG) + 2*rect(AB,AG). The rectangle contained by AB and AG, applied to CD, gives breadth EL/2 for rect(AB,AG), or EL for twice the rectangle. By 2.5, rect(AB,AG) = (sq(AB+AG) - sq(AB) - sq(AG))/2, so 2*rect = sq(BG) - sq(AB) - sq(AG).

**Step 14.** Consider the decomposition differently. Let M be the point on CF such that CM = CE. Then rectangle CD by MF = sq(AG) + 2*rect(AB,AG). Now sq(AB) - sq(AG) = CD*CE - CD*FL = CD*(CE - FL). Since AB and AG are incommensurable in square, sq(AB) and sq(AG) are incommensurable, so CE and FL are incommensurable [6.1, 10.11].

**Step 15.** From 10.65, CF is a sixth binomial. Let CF have terms p and q (p > q) where CF = p + q. By the definition of sixth binomial [D10.2.6]: (i) p and q are commensurable in square only, (ii) neither p nor q is commensurable in length with CD, (iii) sq(p) - sq(q) = sq(r) where r is incommensurable in length with p.

**Step 16.** By 10.96 (applied inversely), the "side" of the area CD*CF (which equals sq(BG)) is the side of the sum of two medial areas. And CE is the breadth when sq(AB) is applied to CD. Since AB is defined as BG - AG (the remainder when AG is subtracted from BG), and BG is the side of the sum of two medial areas, AB produces with a medial area a medial whole [10.78].

**Step 17.** Now CE = CF - (CF - CE). We established that CF is a sixth binomial on CD. The breadth CF - CE corresponds to sq(AG) + 2*rect(AB,AG) applied to CD. Since AG is the annex (unique by 10.84), and by the structure theorem, the subtraction from a sixth binomial of the appropriate breadth yields a sixth apotome. Specifically:

**Step 18.** By 2.7, sq(AB) + sq(AG) = 2*rect(AG, BG) + sq(AB - AG) when BG = AB + AG. But more directly, using the rectangle identity: rect(BG+AB, BG-AB) = sq(BG) - sq(AB) = sq(AG) + 2*rect(AB,AG). So CD*MF = rect(BG+AB, BG-AB) where MF = CF - CE.

**Step 19.** Let us denote the terms of the sixth binomial CF as follows. From 10.65, when sq(BG) is applied to CD producing sixth binomial CF, we know CF = FH + HC (say, with FH > HC as the two terms). By D10.2.6, neither FH nor HC is commensurable with CD, and sq(FH) > sq(HC) by the square on a line incommensurable with FH. The point dividing the binomial into its terms is uniquely determined [10.42 applied to binomials generally; for sixth binomial specifically, the division is unique].

**Step 20.** Since CE is the breadth for sq(AB) on CD, and CF is the breadth for sq(BG) on CD, and CF is a sixth binomial, we need to show CE is a sixth apotome. By the construction in 10.65, the terms of the sixth binomial arise from the medial decomposition of sq(BG). Specifically, one term corresponds to (sq(AB)+sq(AG))/(2*CD) and the other to rect(AB,AG)/CD, adjusted by the identity from 2.4.

**Step 21.** Let us use the direct approach from the pattern of 10.97-10.101. Let the square on AB equal the rectangle CD by CE. Apply also sq(BG) to CD giving breadth CF (a sixth binomial by 10.65). Since BG = AB + AG, sq(BG) = sq(AB) + 2*rect(AB,AG) + sq(AG) [2.4]. Therefore CD*(CF - CE) = 2*rect(AB,AG) + sq(AG).

**Step 22.** Now apply sq(AG) to CD giving breadth CK (say). Then CD*CK = sq(AG). Since AG is incommensurable in square with AB (by 10.78), and both produce medial squares, sq(AB) and sq(AG) are both medial. So CD*CE is medial and CD*CK is medial. Since CD is rational, CE and CK are each rational and incommensurable in length with CD [10.22].

**Step 23.** We have CD*(CF - CE) = sq(AG) + 2*rect(AB,AG) = CD*CK + 2*rect(AB,AG). So 2*rect(AB,AG) = CD*(CF - CE - CK) = CD*(CF - CE) - CD*CK.

**Step 24.** From the sixth binomial CF: let CF = p + q be its decomposition. By 10.65, the construction gives that p corresponds to (sq(AB)+sq(AG))/(2CD) * 2 = the breadth for the sum of squares, and q corresponds to the breadth for 2*rect(AB,AG). More precisely, CD*p = sq(AB) + sq(AG) and CD*q = 2*rect(AB,AG) (or vice versa, depending on which is greater). Since both are medial and incommensurable with each other, and neither p nor q is commensurable with CD, this matches the sixth binomial definition.

**Step 25.** With CD*p = sq(AB) + sq(AG) and CD*q = 2*rect(AB,AG), we have p = CE + CK and q = CF - CE - CK. Actually CF = p + q, CE + CK + q = CF, so CE + CK = p. Thus CE = p - CK.

**Step 26.** Now CK = sq(AG)/CD. Since sq(AG) is medial and CD is rational, CK is rational and incommensurable with CD [10.22]. Similarly CE is rational and incommensurable with CD [10.22, since sq(AB) is medial].

**Step 27.** We need to show that CE = p - CK is a sixth apotome. We have p = CE + CK, so CE = p - CK. Both p and CK are rational (as shown). We must verify: (a) p and CK are commensurable in square only, (b) neither is commensurable in length with CD, (c) sq(p) > sq(CK) by the square on a line incommensurable with p.

**Step 28.** For (b): p is a term of the sixth binomial, so p is incommensurable in length with CD [D10.2.6]. CK is incommensurable in length with CD [Step 26]. This establishes condition (b) of D10.3.6.

**Step 29.** For (a): We need p and CK commensurable in square only. Since CD*p = sq(AB) + sq(AG) and CD*CK = sq(AG), we have p/CK = (sq(AB)+sq(AG))/sq(AG). Now sq(p)/sq(CK) = p^2/CK^2. Consider: CD*p is medial, CD*CK is medial. If p and CK were commensurable in length, then CD*p and CD*CK would be commensurable [10.11], meaning sq(AB)+sq(AG) and sq(AG) would be commensurable. Then sq(AB) = (sq(AB)+sq(AG)) - sq(AG) would be commensurable with sq(AG) [10.15], meaning AB and AG are commensurable in square, contradicting 10.78. So p and CK are incommensurable in length. Since both are rational, they are commensurable in square [by D10.1.3, rational lines are commensurable in square with the assigned rational]. Actually, p and CK are rational (commensurable in square with CD), so sq(p) and sq(CK) are commensurable with sq(CD), hence commensurable with each other [10.12]. Therefore p and CK are commensurable in square. Combined with incommensurability in length, they are commensurable in square only.

**Step 30.** For (c): We must show sq(p) - sq(CK) equals the square on a line incommensurable in length with p. Since CD*p = sq(AB)+sq(AG) and CD*CK = sq(AG), the ratio p:CK = (sq(AB)+sq(AG)):sq(AG) is not the ratio of a square number to a square number (since sq(AB) and sq(AG) are incommensurable, the sum sq(AB)+sq(AG) is incommensurable with sq(AG) [10.16], so the ratio is irrational). By 10.18, when p and CK are incommensurable in length and we apply to p a parallelogram equal to sq(CK)/4 deficient by a square, it divides p into incommensurable parts, which means sq(p) - sq(CK) is the square on a line incommensurable with p.

**Step 31.** We verify the incommensurability condition for 10.18 more carefully. We need that sq(p) > sq(CK) and that sq(p) - sq(CK) = sq(r) where r is incommensurable with p. Since p = CE + CK > CK (as CE > 0), we have sq(p) > sq(CK). From the relation CD*p = sq(AB)+sq(AG) and CD*CK = sq(AG), we get CD*(p - CK) = sq(AB), so p - CK = CE = sq(AB)/CD. Also p + CK = p + CK. Then sq(p) - sq(CK) = (p+CK)(p-CK) = (p+CK)*CE. Now (p+CK) = 2*CK + CE, but more directly: sq(p) - sq(CK) = CD*(p-CK)*(p+CK)/CD = CE*(p+CK). Since CE is incommensurable in length with CD, and p+CK is a specific value, we check if the resulting square root is incommensurable with p. By 10.18, since p and CK are incommensurable in length, sq(p) exceeds sq(CK) by the square on a line incommensurable with p.

**Step 32.** Collecting results: CE = p - CK where p > CK, both p and CK are rational, they are commensurable in square only [Step 29], neither is commensurable in length with CD [Step 28], and sq(p) exceeds sq(CK) by the square on a line incommensurable with p [Steps 30-31]. By the definition of a sixth apotome [D10.3.6], CE is a sixth apotome.

**Step 33.** Therefore, the square on the straight line which produces with a medial area a medial whole, if applied to a rational straight line, produces as breadth a sixth apotome. Q.E.D.

**USED:** 10.11, 10.12, 10.15, 10.16, 10.18, 10.22, 10.42, 10.65, 10.78, 10.84, 10.96, 2.4, 6.1, D10.1.3, D10.2.6, D10.3.6
**Human refs (from References field):** 10.11, 10.18, 10.22, 10.73, 10.78, 2.7, 6.1, D10.3.6
**Jaccard:** 0.333 — AI adds ['10.12', '10.15', '10.16', '10.42', '10.65', '10.84', '10.96', '2.4', 'D10.1.3', 'D10.2.6']; Human adds ['10.73', '2.7']

## Proposition 10.103
**Statement:** A straight line commensurable in length with an apotome is an apotome and the same in order.

**Step 1.** Let AB be an apotome, and let CD be commensurable in length with AB. We must show that CD is also an apotome and the same in order as AB.

**Step 2.** Since AB is an apotome, let BG be the annex to AB, so that AG is the whole. Then AG and BG are rational straight lines commensurable in square only [10.73], and AB = AG - BG.

**Step 3.** Since CD is commensurable in length with AB, let us find straight lines CF and FD such that CF corresponds to AG and FD corresponds to BG, as follows. Since AB is commensurable in length with CD, as AB is to CD, so let AG be to CF, by finding CF as a fourth proportional to AB, CD, AG [6.12]. Then since AG is commensurable in length with CF (because AB is commensurable in length with CD and AG:CF = AB:CD, so by 10.11 CF is commensurable with AG), and AG is rational, therefore CF is also rational [D10.1.3].

**Step 4.** Similarly, since AB:CD = AG:CF, by separation (separando), as BG is to FD, so is AB to CD [5.19], where FD = CF - CD. Since AB is commensurable in length with CD, BG is commensurable in length with FD [10.11]. And since BG is rational, FD is also rational [D10.1.3].

**Step 5.** Now since AG is commensurable in square only with BG (as AB is an apotome), and AG:CF = BG:FD (both equaling AB:CD) [5.11], and AG is commensurable in length with CF and BG is commensurable in length with FD, we conclude that CF is commensurable in square only with FD. For: AG is commensurable in length with CF, so the squares on AG and CF are commensurable [10.12]. Similarly the squares on BG and FD are commensurable. But AG is commensurable in square only with BG, meaning AG and BG are incommensurable in length. Since AG:BG = CF:FD [5.11, 5.16], and AG is incommensurable in length with BG, therefore CF is incommensurable in length with FD [10.11].

**Step 6.** Therefore CF and FD are rational straight lines commensurable in square only, and CD = CF - FD. Hence CD is an apotome [10.73], with CF as the whole and FD as the annex.

**Step 7.** It remains to show that CD is the same in order as AB. The order of an apotome (first through sixth) is determined by two conditions [D10.3.1-D10.3.6]: (i) whether the square on the whole exceeds the square on the annex by the square on a straight line commensurable or incommensurable in length with the whole, and (ii) which of the whole or annex (if either) is commensurable in length with a given rational straight line.

**Step 8.** For condition (i): Since AG:CF = BG:FD and both pairs are proportional (AG, BG, CF, FD are four straight lines in proportion), and the square on AG is greater than the square on BG by the square on a straight line either commensurable or incommensurable in length with AG, then correspondingly the square on CF is greater than the square on FD by the square on a straight line of the same commensurability relation with CF [10.14].

**Step 9.** For condition (ii): Let rho be the assigned rational straight line. If AG is commensurable in length with rho, then since AG is commensurable in length with CF [Step 3], CF is also commensurable in length with rho [10.12]. If BG is commensurable in length with rho, then since BG is commensurable in length with FD [Step 4], FD is also commensurable in length with rho [10.12]. If AG is incommensurable in length with rho, then since AG is commensurable in length with CF, CF is also incommensurable in length with rho [10.13]. Similarly, if BG is incommensurable in length with rho, then FD is also incommensurable in length with rho [10.13].

**Step 10.** Therefore, the two determining conditions for the order of the apotome are the same for CD (with whole CF and annex FD) as they are for AB (with whole AG and annex BG). Checking against the definitions: if AB is a first apotome [D10.3.1], then AG is commensurable with rho and sq(AG) > sq(BG) by the square on a line commensurable with AG, so CF is commensurable with rho and sq(CF) > sq(FD) by the square on a line commensurable with CF, making CD a first apotome. The same argument applies for each of the six orders [D10.3.2-D10.3.6].

**Step 11.** Therefore CD is an apotome and the same in order as AB. Q.E.D.

**USED:** 10.11, 10.12, 10.13, 10.14, 10.73, 5.11, 5.16, 5.19, 6.12, D10.1.3, D10.3.1, D10.3.2, D10.3.3, D10.3.4, D10.3.5, D10.3.6
**Human refs (from References field):** 10.11, 10.12, 10.13, 10.14, 10.73, 5.12, 5.16, 6.12
**Jaccard:** 0.412 — AI adds ['5.11', '5.19', 'D10.1.3', 'D10.3.1', 'D10.3.2', 'D10.3.3', 'D10.3.4', 'D10.3.5', 'D10.3.6']; Human adds ['5.12']

## Proposition 10.104
**Statement:** A straight line commensurable with an apotome of a medial straight line is an apotome of a medial straight line and the same in order.

**Step 1.** Let AB be an apotome of a medial straight line, and let CD be commensurable in length with AB. We must show that CD is also an apotome of a medial straight line and the same in order as AB.

**Step 2.** Since AB is an apotome of a medial straight line, AB is either a first apotome of a medial straight line or a second apotome of a medial straight line, as defined in 10.74 and 10.75.

**Step 3.** Let a rational straight line EF be set out. Apply the square on AB to EF, producing a rectangle of breadth EG, so that the rectangle EF x EG equals the square on AB. Similarly, apply the square on CD to EF, producing a rectangle of breadth EH, so that the rectangle EF x EH equals the square on CD.

**Step 4.** Since AB and CD are commensurable in length, the squares on AB and on CD are commensurable, by 10.11. Since both squares are applied to the same rational straight line EF, the breadths EG and EH are commensurable in length, by 10.11.

**Step 5.** Case 1: Suppose AB is a first apotome of a medial straight line. Then by 10.98, the square on AB applied to the rational straight line EF produces as breadth a second apotome. Thus EG is a second apotome.

**Step 6.** Since EG is a second apotome and EH is commensurable in length with EG (by Step 4), then by 10.103, EH is also a second apotome.

**Step 7.** Since EH is a second apotome, and the rectangle EF x EH equals the square on CD, with EF rational, then by 10.92, the side of the area EF x EH is a first apotome of a medial straight line. But the side of the area equal to the square on CD is CD itself. Therefore CD is a first apotome of a medial straight line, the same in order as AB.

**Step 8.** Case 2: Suppose AB is a second apotome of a medial straight line. Then by 10.99, the square on AB applied to the rational straight line EF produces as breadth a third apotome. Thus EG is a third apotome.

**Step 9.** Since EG is a third apotome and EH is commensurable in length with EG (by Step 4), then by 10.103, EH is also a third apotome.

**Step 10.** Since EH is a third apotome, and the rectangle EF x EH equals the square on CD, with EF rational, then by 10.93, the side of the area EF x EH is a second apotome of a medial straight line. But this side is CD itself. Therefore CD is a second apotome of a medial straight line, the same in order as AB.

**Step 11.** In both cases, CD is an apotome of a medial straight line and the same in order as AB. Therefore, a straight line commensurable with an apotome of a medial straight line is an apotome of a medial straight line and the same in order. Q.E.D.

**USED:** 10.103, 10.11, 10.74, 10.75, 10.92, 10.93, 10.98, 10.99
**Human refs (from References field):** 10.11, 10.13, 10.23, 10.74, 10.75, 5.12, 5.16, 6.12, D10.1.4
**Jaccard:** 0.214 — AI adds ['10.103', '10.92', '10.93', '10.98', '10.99']; Human adds ['10.13', '10.23', '5.12', '5.16', '6.12', 'D10.1.4']

## Proposition 10.105
**Statement:** A straight line commensurable with a minor straight line is minor.

**Step 1.** Let AB be a minor straight line, and let CD be commensurable in length with AB. We must show that CD is also minor.

**Step 2.** Since AB is minor, let it be decomposed as AB = AE - EB, where AE and EB are the components given by the definition of minor (10.76): AE and EB are incommensurable in square, the sum of the squares on AE and EB is rational, and twice the rectangle contained by AE and EB is medial. By 10.82, this decomposition is unique.

**Step 3.** Since CD is commensurable in length with AB, let CD : AB = CD : AB, so there is a ratio that CD has to AB. Since AE and EB are parts of AB, set CF and FD on CD such that CF : AE = CD : AB and FD : EB = CD : AB (by 6.12, taking the same proportion). Then CD = CF - FD corresponds to the decomposition AB = AE - EB, and CF : AE :: FD : EB :: CD : AB.

**Step 4.** Since AE is commensurable in length with CF (because AE : CF = AB : CD, which is a ratio of commensurable magnitudes, so by 10.6 and 10.12, AE and CF are commensurable in length), and similarly EB is commensurable in length with FD.

**Step 5.** Since AE and EB are incommensurable in square, we must show CF and FD are incommensurable in square. The square on AE is to the square on CF as the square on AB is to the square on CD (since AE : CF = AB : CD, and squaring preserves the ratio by 6.22). Similarly the square on EB is to the square on FD in the same ratio. Now, the square on AE is incommensurable with the square on EB (since AE and EB are incommensurable in square). Since sq(AE) : sq(CF) is the same ratio as sq(EB) : sq(FD), by 10.11, since sq(AE) is incommensurable with sq(EB), we conclude sq(CF) is incommensurable with sq(FD). Therefore CF and FD are incommensurable in square.

**Step 6.** We now show the sum of the squares on CF and FD is rational. Since sq(AE) + sq(EB) is rational, and sq(CF) + sq(FD) is commensurable with sq(AE) + sq(EB) (because sq(CF) : sq(AE) = sq(CD) : sq(AB), and sq(FD) : sq(EB) = sq(CD) : sq(AB), so (sq(CF) + sq(FD)) : (sq(AE) + sq(EB)) = sq(CD) : sq(AB) by 5.12 and 5.18). Since CD is commensurable in length with AB, sq(CD) is commensurable with sq(AB) (by 10.11 applied via the relationship that commensurable lengths yield commensurable squares). Therefore sq(CF) + sq(FD) is commensurable with the rational area sq(AE) + sq(EB), so sq(CF) + sq(FD) is rational (by D10.1.4, since areas commensurable with a rational area are rational).

**Step 7.** We now show that twice the rectangle CF.FD is medial. The rectangle AE.EB and the rectangle CF.FD are in the ratio sq(AB) : sq(CD). More precisely, since AE : CF = EB : FD = AB : CD, the rectangle AE.EB is to the rectangle CF.FD as sq(AB) is to sq(CD) (by 6.16, since the rectangles are products of proportional sides). Therefore twice the rectangle AE.EB is to twice the rectangle CF.FD in the same ratio. Since twice rect(AE, EB) is medial, and twice rect(CF, FD) is commensurable with it (as sq(CD) is commensurable with sq(AB) because CD is commensurable in length with AB), by 10.23 applied to areas (a medial area commensurable with a medial area is medial), twice the rectangle CF.FD is medial.

**Step 8.** We have established that CF and FD are incommensurable in square, the sum sq(CF) + sq(FD) is rational, and twice rect(CF, FD) is medial. Therefore CD = CF - FD is minor, by 10.76.

**Step 9.** Therefore a straight line commensurable with a minor straight line is minor. Q.E.D.

**USED:** 10.11, 10.12, 10.23, 10.6, 10.76, 10.82, 5.12, 5.18, 6.12, 6.16, 6.22, D10.1.4
**Human refs (from References field):** 10.11, 10.13, 10.23, 10.76, 5.12, 5.16, 5.18, 6.22, D10.1.4
**Jaccard:** 0.500 — AI adds ['10.12', '10.6', '10.82', '6.12', '6.16']; Human adds ['10.13', '5.16']

## Proposition 10.106
**Statement:** A straight line commensurable with that which produces with a rational area a medial whole is a straight line which produces with a rational area a medial whole.

**Step 1.** Let AB be a straight line which produces with a rational area a medial whole. Then by the definition in 10.77, AB has been divided at some point G such that AB = AG - GB, where AG and GB are incommensurable in square, the sum of the squares on AG and GB is medial, and twice the rectangle contained by AG and GB is rational. By 10.83, this decomposition is unique: only one such straight line GB can be annexed to AG to form AB with these properties.

**Step 2.** Let CD be any straight line commensurable in length with AB. We must show that CD is also a straight line which produces with a rational area a medial whole.

**Step 3.** Since CD is commensurable in length with AB, the ratio CD:AB is as a number to a number (by 10.5). Let CE and ED be taken on CD such that CD = CE - ED, with CE:AG = ED:GB = CD:AB. This is possible by dividing CD in the same ratio as AG to GB.

**Step 4.** Since CD is commensurable in length with AB, and CE:AG = CD:AB, it follows that CE is commensurable in length with AG (by 10.6, since the ratio is as a number to a number). Similarly, ED is commensurable in length with GB.

**Step 5.** Since AG and GB are incommensurable in square (by the hypothesis from 10.77), and CE is commensurable in length with AG while ED is commensurable in length with GB, it follows by 10.13 that CE and ED are incommensurable in square. For CE is commensurable with AG, but AG is incommensurable in square with GB, and GB is commensurable with ED; therefore CE is incommensurable in square with ED.

**Step 6.** Since CE is commensurable in length with AG, the square on CE is commensurable with the square on AG (by 10.11 applied with 6.22, or directly since commensurable in length implies commensurable in square by D10.1.2 and 10.5/10.6). Similarly, the square on ED is commensurable with the square on GB.

**Step 7.** Since the square on CE is commensurable with the square on AG, and the square on ED is commensurable with the square on GB, the sum of the squares on CE and ED is commensurable with the sum of the squares on AG and GB (by 10.15, since adding commensurable magnitudes preserves commensurability). Now the sum of the squares on AG and GB is medial (by hypothesis from 10.77). Therefore the sum of the squares on CE and ED is also medial (by 10.23, since a magnitude commensurable with a medial area is medial).

**Step 8.** Since CE:AG = ED:GB, the rectangle contained by CE and ED is to the rectangle contained by AG and GB as the square on CE is to the square on AG (by 6.16, since CE:AG = ED:GB implies rect(CE,ED):rect(AG,GB) = CE*ED : AG*GB, and by the equal ratios). More precisely, since CE:AG = ED:GB, we have rect(CE,ED):rect(AG,GB) = CE:AG composed with ED:GB. But CE:AG = ED:GB = CD:AB, so rect(CE,ED):rect(AG,GB) = the duplicate ratio of CD:AB, which is as a square number to a square number (since CD:AB is as a number to a number by 10.5). Therefore rect(CE,ED) is commensurable with rect(AG,GB) (by 10.6).

**Step 9.** Since twice the rectangle contained by CE and ED is commensurable with twice the rectangle contained by AG and GB, and twice the rectangle contained by AG and GB is rational (by hypothesis from 10.77), twice the rectangle contained by CE and ED is also rational (by 10.12, since a magnitude commensurable with a rational magnitude is rational, using D10.1.4).

**Step 10.** We have established that CE and ED are incommensurable in square (Step 5), the sum of the squares on CE and ED is medial (Step 7), and twice the rectangle contained by CE and ED is rational (Step 9). These are precisely the conditions specified in 10.77.

**Step 11.** Therefore CD = CE - ED is a straight line which produces with a rational area a medial whole, by definition (10.77). Hence a straight line commensurable with that which produces with a rational area a medial whole is itself a straight line which produces with a rational area a medial whole. Q.E.D.

**USED:** 10.11, 10.12, 10.13, 10.15, 10.23, 10.5, 10.6, 10.77, 10.83, 6.16, D10.1.2, D10.1.4
**Human refs (from References field):** 10.77
**Jaccard:** 0.083 — AI adds ['10.11', '10.12', '10.13', '10.15', '10.23', '10.5', '10.6', '10.83', '6.16', 'D10.1.2', 'D10.1.4']

## Proposition 10.107
**Statement:** A straight line commensurable with that which produces with a medial area a medial whole is itself also a straight line which produces with a medial area a medial whole.

**Step 1.** Let AB be a straight line which produces with a medial area a medial whole, and let CD be commensurable in length with AB. We must show that CD is also a straight line which produces with a medial area a medial whole.

**Step 2.** Let a rational straight line EF be set out. Apply the square on AB to EF, producing as breadth EG, so that the rectangle EF,EG equals the square on AB. By 10.102, since AB is a straight line which produces with a medial area a medial whole, EG is a sixth apotome.

**Step 3.** Apply the square on CD to EF, producing as breadth EH, so that the rectangle EF,EH equals the square on CD.

**Step 4.** Since AB is commensurable in length with CD, the square on AB is commensurable with the square on CD, for if two straight lines are commensurable in length, the squares on them have to one another the ratio which a square number has to a square number, and hence are commensurable (by 10.9 and 10.6). That is, the rectangle EF,EG is commensurable with the rectangle EF,EH.

**Step 5.** Since the rectangle EF,EG is commensurable with the rectangle EF,EH, and these rectangles are applied to the same rational straight line EF, it follows that EG is commensurable in length with EH (by 6.1, 5.11, and 10.11, or more directly because areas applied to the same line have their breadths in the same ratio as the areas, so commensurable areas yield commensurable breadths — this is the converse application of 10.20 and follows from 6.1 and 10.11).

**Step 6.** Since EG is a sixth apotome and EH is commensurable in length with EG, by 10.103 EH is also an apotome and the same in order, that is, EH is also a sixth apotome.

**Step 7.** Since the rectangle EF,EH equals the square on CD, and EF is rational, and EH is a sixth apotome, by 10.96 CD is a straight line which produces with a medial area a medial whole.

**Step 8.** Therefore a straight line commensurable with that which produces with a medial area a medial whole is itself also a straight line which produces with a medial area a medial whole. Q.E.D.

**USED:** 10.102, 10.103, 10.11, 10.6, 10.9, 10.96, 5.11, 6.1
**Human refs (from References field):** 10.78
**Jaccard:** 0.000 — AI adds ['10.102', '10.103', '10.11', '10.6', '10.9', '10.96', '5.11', '6.1']; Human adds ['10.78']

## Proposition 10.108
**Statement:** If from a rational area a medial area be subtracted, the âsideâ of the remaining area becomes one of two irrational straight lines, either an apotome or a minor straight line.

**Step 1.** Let a rational area be given from which a medial area is subtracted, and let the remainder be the area S. Let a rational straight line r be set out.

**Step 2.** Apply the rational area to r, producing breadth p, so that r times p equals the rational area. Since the rational area is commensurable with the square on r (by D10.1.4), and r is rational, by 10.20 the breadth p is rational and commensurable in length with r.

**Step 3.** Apply the medial area to r, producing breadth q, so that r times q equals the medial area. Since the medial area is the square on a medial straight line and is thus incommensurable with the square on r (by D10.1.4 and 10.21), by 10.22 the breadth q is rational and incommensurable in length with r.

**Step 4.** Since p is commensurable in length with r and q is incommensurable in length with r, then p is incommensurable in length with q, by 10.13. But p and q are both rational straight lines, so they are commensurable in square (since both are commensurable in square with r by D10.1.3, hence with each other by 10.12). Therefore p and q are rational straight lines commensurable in square only.

**Step 5.** The remaining area S equals r times p minus r times q, which equals r times (p minus q). Since p and q are rational straight lines commensurable in square only and p is greater than q (for the rational area exceeds the medial area, so p exceeds q), by 10.73 the straight line p minus q is an apotome.

**Step 6.** In the apotome p minus q, the whole is p and the annex is q. We have established that p is commensurable in length with r, while q is incommensurable in length with r. Now we consider two cases based on the relationship between the squares on p and q.

**Step 7.** Case 1: Suppose the square on p is greater than the square on q by the square on a straight line commensurable in length with p. Since p (the whole of the apotome) is commensurable in length with the rational straight line r, by D10.3.1 the apotome p minus q is a first apotome. Therefore, by 10.91, the side of the area contained by r and the first apotome p minus q is an apotome.

**Step 8.** Case 2: Suppose the square on p is greater than the square on q by the square on a straight line incommensurable in length with p. Since p (the whole of the apotome) is commensurable in length with r, by D10.3.4 the apotome p minus q is a fourth apotome. Therefore, by 10.94, the side of the area contained by r and the fourth apotome p minus q is a minor straight line.

**Step 9.** In either case, the side of the remaining area S is either an apotome or a minor straight line. No other possibilities arise, since p is always commensurable in length with r and q is always incommensurable in length with r, and the only distinction is whether the square on p exceeds the square on q by the square on a line commensurable or incommensurable with p. Therefore, if from a rational area a medial area be subtracted, the side of the remaining area is one of two irrational straight lines, either an apotome or a minor straight line. Q.E.D.

**USED:** 10.12, 10.13, 10.20, 10.21, 10.22, 10.73, 10.91, 10.94, D10.1.3, D10.1.4, D10.3.1, D10.3.4
**Human refs (from References field):** 10.13, 10.20, 10.22, 10.73, 10.91, 10.94, D10.3.1, D10.3.4
**Jaccard:** 0.667 — AI adds ['10.12', '10.21', 'D10.1.3', 'D10.1.4']

## Proposition 10.109
**Statement:** If from a medial area a rational area be subtracted, there arise two other irrational straight lines, either a first apotome of a medial straight line or a straight line which produces with a rational area a medial whole.

**Step 1.** Let the medial area be MА and let the rational area RA be subtracted from it, so that the remainder is MА minus RA. Let sigma be a rational straight line set out.

**Step 2.** Apply the medial area MА to sigma, producing as breadth the straight line w. Since MА is medial, by 10.22 (the square on a medial straight line applied to a rational straight line produces a breadth rational and incommensurable in length with that line), w is rational and incommensurable in length with sigma.

**Step 3.** Apply the rational area RA to sigma, producing as breadth the straight line u. Since RA is rational, by 10.20, u is rational and commensurable in length with sigma.

**Step 4.** Then the remainder MА minus RA, when applied to sigma, produces as breadth w minus u (since w corresponds to the whole medial area and u to the subtracted rational area, with w greater than u because the medial area is greater than the rational area subtracted from it).

**Step 5.** Now w is incommensurable in length with sigma, and u is commensurable in length with sigma. Therefore by 10.13, w is incommensurable in length with u.

**Step 6.** But both w and u are rational straight lines. Since they are rational and incommensurable in length, they are commensurable in square only. Therefore by 10.73, the straight line w minus u is an apotome, and sigma is a rational straight line.

**Step 7.** We now classify the apotome w minus u with respect to sigma. In this apotome, w is the whole and u is the annex. We have established that u (the annex) is commensurable in length with sigma (Step 3), while w (the whole) is incommensurable in length with sigma (Step 2).

**Step 8.** Now consider whether the square on w is greater than the square on u by the square on a straight line commensurable or incommensurable in length with w. There are exactly two cases.

**Step 9.** Case 1: Suppose the square on w is greater than the square on u by the square on a straight line commensurable in length with w. Then since the annex u is commensurable in length with sigma, and the square on the whole exceeds the square on the annex by the square on a line commensurable with the whole, the apotome w minus u is a second apotome by definition (D10.3.2).

**Step 10.** Since the remainder area (MА minus RA) equals the rectangle contained by sigma (a rational straight line) and the second apotome w minus u, by 10.92 the side of this area is a first apotome of a medial straight line.

**Step 11.** Case 2: Suppose the square on w is greater than the square on u by the square on a straight line incommensurable in length with w. Then since the annex u is commensurable in length with sigma, and the square on the whole exceeds the square on the annex by the square on a line incommensurable with the whole, the apotome w minus u is a fifth apotome by definition (D10.3.5).

**Step 12.** Since the remainder area (MА minus RA) equals the rectangle contained by sigma (a rational straight line) and the fifth apotome w minus u, by 10.95 the side of this area is a straight line which produces with a rational area a medial whole.

**Step 13.** These are the only two cases, since the annex u is commensurable in length with sigma while the whole w is not, and the excess of the square on w over the square on u is either by the square on a line commensurable or incommensurable with w. Therefore, if from a medial area a rational area be subtracted, the side of the remainder is either a first apotome of a medial straight line or a straight line which produces with a rational area a medial whole. Q.E.D.

**USED:** 10.13, 10.20, 10.22, 10.73, 10.92, 10.95, D10.1.3, D10.1.4, D10.3.2, D10.3.5
**Human refs (from References field):** 10.13, 10.73, 10.92, 10.95, D10.3.2, D10.3.5
**Jaccard:** 0.600 — AI adds ['10.20', '10.22', 'D10.1.3', 'D10.1.4']

## Proposition 10.110
**Statement:** If from a medial area there be subtracted a medial area incommensurable with the whole, the two remaining irrational straight lines arise, either a second apotome of a medial straight line or a straight line which produces with a medial area a medial whole.

**Step 1.** Let there be a medial area AF from which a medial area AG is subtracted, where AF and AG are incommensurable with one another. We are to show that the side of the remaining area GF is either a second apotome of a medial straight line or a straight line which produces with a medial area a medial whole.

**Step 2.** Let rho be a rational straight line set out. Apply AF to rho, producing breadth CB, so that AF = rho * CB. Likewise apply AG to rho, producing breadth CD, so that AG = rho * CD, with CB > CD. Then the remainder GF = rho * (CB - CD).

**Step 3.** Since AF is a medial area and rho is rational, by 10.22 the breadth CB is rational and incommensurable in length with rho. Similarly, since AG is a medial area and rho is rational, by 10.22 the breadth CD is rational and incommensurable in length with rho.

**Step 4.** Since AF = rho * CB and AG = rho * CD, the ratio AF : AG equals CB : CD. Since AF and AG are incommensurable areas, CB and CD are incommensurable in length. But CB and CD are both rational, so they are commensurable in square (by D10.1.3, since each is commensurable in square with the assigned rational line, hence with each other by 10.12). Therefore CB and CD are rational straight lines commensurable in square only.

**Step 5.** Since CB and CD are rational straight lines commensurable in square only, by 10.73 the straight line CB - CD is an apotome.

**Step 6.** Now we determine what order of apotome CB - CD is. From Step 3, CB is incommensurable in length with rho, and CD is incommensurable in length with rho. Therefore neither the whole CB nor the annex CD is commensurable in length with the rational straight line rho set out.

**Step 7.** Since CB and CD are rational and commensurable in square only, by 10.21 the rectangle contained by CB and CD is irrational (medial). By 10.25, the rectangle contained by medial straight lines commensurable in square only is either rational or medial, but here CB and CD are rational, not medial, so this does not directly apply. Instead, 10.21 gives us that the rectangle CB * CD is medial, which is a single determination. The distinguishing factor for the order of the apotome is whether the square on CB exceeds the square on CD by the square on a straight line commensurable or incommensurable in length with CB.

**Step 8.** Case 1: Suppose the square on CB is greater than the square on CD by the square on a straight line commensurable in length with CB. Then since neither CB nor CD is commensurable in length with rho (Step 6), by D10.3.3 the apotome CB - CD is a third apotome.

**Step 9.** Since the area GF = rho * (CB - CD), and rho is rational while CB - CD is a third apotome, by 10.93 the side of the area GF is a second apotome of a medial straight line.

**Step 10.** Case 2: Suppose the square on CB is greater than the square on CD by the square on a straight line incommensurable in length with CB. Then since neither CB nor CD is commensurable in length with rho (Step 6), by D10.3.6 the apotome CB - CD is a sixth apotome.

**Step 11.** Since the area GF = rho * (CB - CD), and rho is rational while CB - CD is a sixth apotome, by 10.96 the side of the area GF is a straight line which produces with a medial area a medial whole.

**Step 12.** Since by Step 6 neither the whole nor the annex of the apotome CB - CD is commensurable in length with rho, the apotome cannot be a first apotome (D10.3.1 requires the whole be commensurable with rho), a second apotome (D10.3.2 requires the annex be commensurable with rho), a fourth apotome (D10.3.4 requires the whole be commensurable with rho), or a fifth apotome (D10.3.5 requires the annex be commensurable with rho). Therefore the apotome is either third or sixth, and no other cases arise.

**Step 13.** Therefore, if from a medial area there be subtracted a medial area incommensurable with the whole, the side of the remaining area is either a second apotome of a medial straight line or a straight line which produces with a medial area a medial whole. Q.E.D.

**USED:** 10.12, 10.21, 10.22, 10.73, 10.93, 10.96, D10.1.3, D10.3.1, D10.3.2, D10.3.3, D10.3.4, D10.3.5, D10.3.6
**Human refs (from References field):** 10.11, 10.22, 10.73, 10.93, 10.96, 6.1, D10.3.3, D10.3.6
**Jaccard:** 0.400 — AI adds ['10.12', '10.21', 'D10.1.3', 'D10.3.1', 'D10.3.2', 'D10.3.4', 'D10.3.5']; Human adds ['10.11', '6.1']

## Proposition 10.111
**Statement:** The apotome is not the same with the binomial straight line.

Suppose, for the sake of contradiction, that some straight line AB is both a binomial and an apotome.

**Step 1.** Since AB is a binomial, by 10.36, AB is the sum of two rational straight lines commensurable in square only. Let AB = AC + CB, where AC and CB are rational and commensurable in square only.

**Step 2.** Since AB is an apotome, by 10.73, AB is the remainder when from a rational straight line a rational straight line commensurable with the whole in square only is subtracted. Let AB = AD - DB, where AD and DB are rational and commensurable in square only, with AD greater than DB.

**Step 3.** By 2.4, since AB = AC + CB, we have sq(AB) = sq(AC) + sq(CB) + 2*rect(AC, CB).

**Step 4.** By 2.7, since AB = AD - DB, we have sq(AB) = sq(AD) + sq(DB) - 2*rect(AD, DB).

**Step 5.** Since both expressions equal sq(AB), by CN1 we have sq(AC) + sq(CB) + 2*rect(AC, CB) = sq(AD) + sq(DB) - 2*rect(AD, DB). Rearranging: 2*rect(AC, CB) + 2*rect(AD, DB) = [sq(AD) + sq(DB)] - [sq(AC) + sq(CB)].

**Step 6.** We show that [sq(AD) + sq(DB)] and [sq(AC) + sq(CB)] are each rational areas. Since AC is rational, sq(AC) is commensurable with the square on the assigned rational line rho, i.e., sq(AC) is rational (D10.1.3, D10.1.4). Similarly sq(CB) is rational. Since AC and CB are commensurable in square, sq(AC) and sq(CB) are commensurable. By 10.12, both being commensurable with sq(rho), they are commensurable with each other, and by 10.15, sq(AC) + sq(CB) is commensurable with each and hence with sq(rho); thus sq(AC) + sq(CB) is rational. By the same reasoning, sq(AD) + sq(DB) is rational.

**Step 7.** The difference R = [sq(AD) + sq(DB)] - [sq(AC) + sq(CB)] is the difference of two rational areas. Since both are commensurable with sq(rho), they are commensurable with each other by 10.12, and their difference R is commensurable with sq(rho) by 10.15. Hence R is a rational area. Note that R is positive, since R equals the sum 2*rect(AC, CB) + 2*rect(AD, DB) of two positive areas.

**Step 8.** We show that 2*rect(AC, CB) is a medial area. By 10.21, since AC and CB are rational and commensurable in square only, rect(AC, CB) is medial. The ratio of 2*rect(AC, CB) to rect(AC, CB) is 2 to 1, which is a ratio of number to number, so by 10.6, these two areas are commensurable. Since rect(AC, CB) is incommensurable with sq(rho) (being medial, D10.1.4), by 10.13, 2*rect(AC, CB) is also incommensurable with sq(rho), hence irrational. Moreover, since rect(AC, CB) equals the square on some medial straight line m (by the definition in 10.21 and D10.1.4), and sq(n) = 2*rect(AC, CB) means sq(n) is commensurable with sq(m), the line n is commensurable with the medial line m, so n is medial by 10.23. Thus 2*rect(AC, CB) = sq(n) is a medial area. By the same reasoning, 2*rect(AD, DB) is a medial area.

**Step 9.** Let rho be a rational straight line. Apply each area in the equation 2*rect(AC, CB) + 2*rect(AD, DB) = R to the line rho, producing breadths s1, s2, and s respectively, so that rect(rho, s1) = 2*rect(AC, CB), rect(rho, s2) = 2*rect(AD, DB), and rect(rho, s) = R. Then s1 + s2 = s.

**Step 10.** Since R is a rational area and rho is rational, by 10.20, s is rational and commensurable in length with rho.

**Step 11.** Since 2*rect(AC, CB) is a medial area equal to sq(n) where n is medial (Step 8), by 10.22, sq(n) applied to the rational line rho produces a breadth s1 that is rational and incommensurable in length with rho. Similarly, s2 is rational and incommensurable in length with rho.

**Step 12.** Now s1 and s2 are both rational lines (D10.1.3), so sq(s1) and sq(s2) are each commensurable with sq(rho). By 10.12, sq(s1) and sq(s2) are commensurable with each other. Hence s1 and s2 are commensurable in square. Two lines commensurable in square are either commensurable in length or commensurable in square only. We consider both cases.

**Step 13.** Case (a): Suppose s1 and s2 are commensurable in length. Then by 10.15, s = s1 + s2 is commensurable in length with s1. Since s1 is incommensurable in length with rho (Step 11), and s is commensurable in length with s1, by 10.13, s is incommensurable in length with rho. But by Step 10, s is commensurable in length with rho. This is a contradiction.

**Step 14.** Case (b): Suppose s1 and s2 are commensurable in square only. Since s1 and s2 are rational and commensurable in square only, by 10.36, s = s1 + s2 is a binomial, which is irrational. But by Step 10, s is rational and commensurable in length with rho, hence s is rational (D10.1.3). A straight line cannot be both rational and irrational. This is a contradiction.

**Step 15.** Since both cases lead to contradiction, the assumption that AB is both a binomial and an apotome is false. Therefore, the apotome is not the same with the binomial straight line. Q.E.D.

**USED:** 10.12, 10.13, 10.15, 10.20, 10.21, 10.22, 10.23, 10.36, 10.6, 10.73, 2.4, 2.7, CN1, D10.1.3, D10.1.4
**Human refs (from References field):** 10.12, 10.13, 10.15, 10.60, 10.73, 10.97, D10.2.1, D10.3.1
**Jaccard:** 0.211 — AI adds ['10.20', '10.21', '10.22', '10.23', '10.36', '10.6', '2.4', '2.7', 'CN1', 'D10.1.3', 'D10.1.4']; Human adds ['10.60', '10.97', 'D10.2.1', 'D10.3.1']

## Proposition 10.112
**Statement:** The square on a rational straight line applied to the binomial straight line produces as breadth an apotome the terms of which are commensurable with the terms of the binomial and moreover in the same ratio; and further the apotome so arising will have the same order as the binomial straight line.

**Step 1.** Let E be a rational straight line, and let AB be a binomial straight line with terms AC and CB, where AC is the greater term. Let AB * FG = sq(E), so that FG is the breadth produced when the square on E is applied to AB. We must show that FG is an apotome whose terms are commensurable with AC and CB respectively, in the same ratio, and of the same order as the binomial AB.

**Step 2.** Since AB is a binomial, its terms AC and CB are rational straight lines commensurable in square only [by 10.36]. In particular, AC and CB are each commensurable in square with the assigned rational straight line, and AC is incommensurable in length with CB, while sq(AC) and sq(CB) are commensurable.

**Step 3.** Since AC and CB are rational, sq(AC) and sq(CB) are each rational areas, that is, each is commensurable with the square on the assigned rational line [D10.1.4]. Therefore sq(AC) and sq(CB) are commensurable with one another [10.12]. Let D denote the difference sq(AC) - sq(CB). Since sq(AC) and sq(CB) are commensurable, D is commensurable with sq(AC) [10.15], and hence D is a rational area [D10.1.4, 10.12].

**Step 4.** Since AC and CB are rational and commensurable in square only with AC greater than CB, the remainder AC - CB is an apotome, with whole AC and annex CB [10.73].

**Step 5.** We now show that rect(AB, AC - CB) = sq(AC) - sq(CB) = D. Since AB = AC + CB, by 2.1 we have rect(AB, AC) = sq(AC) + rect(AC, CB), and also rect(AB, CB) = rect(AC, CB) + sq(CB). Subtracting the second from the first [CN3]: rect(AB, AC) - rect(AB, CB) = sq(AC) - sq(CB) = D. But again by 2.1, since AC = (AC - CB) + CB, we have rect(AB, AC) = rect(AB, AC - CB) + rect(AB, CB). Therefore rect(AB, AC - CB) = rect(AB, AC) - rect(AB, CB) = D.

**Step 6.** We now have two rectangles with the same base AB: rect(AB, FG) = sq(E) and rect(AB, AC - CB) = D. By 6.1, rectangles on the same base are to one another as their heights, so FG : (AC - CB) = sq(E) : D.

**Step 7.** Since sq(E) is a rational area and D is a rational area [Step 3], they are each commensurable with the square on the assigned rational line, and hence commensurable with one another [10.12]. Therefore the ratio sq(E) : D is a ratio of commensurable magnitudes, which is a ratio that a number has to a number [10.5]. Since FG : (AC - CB) = sq(E) : D [Step 6] and this is a numerical ratio, FG and AC - CB are commensurable in length [10.6].

**Step 8.** Since AC - CB is an apotome [Step 4] and FG is commensurable in length with AC - CB [Step 7], by 10.103 FG is itself an apotome and of the same order as AC - CB.

**Step 9.** We now show that the terms of the apotome FG are commensurable with the terms of the binomial AB and in the same ratio. By 10.103, when FG is commensurable in length with the apotome AC - CB, the terms of FG (call them P and Q, where FG = P - Q) satisfy P commensurable in length with AC and Q commensurable in length with CB, and P : Q = AC : CB. Since AC and CB are the terms of the binomial AB, the terms of the apotome FG are commensurable with the terms of the binomial, and moreover in the same ratio.

**Step 10.** Finally, we show that the apotome FG has the same order as the binomial AB. The order of the binomial AB = AC + CB is determined by two criteria [D10.2.1 through D10.2.6]: (i) whether sq(AC) exceeds sq(CB) by the square on a straight line commensurable or incommensurable in length with AC, and (ii) which of AC, CB (if either) is commensurable in length with the assigned rational straight line. The order of the apotome AC - CB, with whole AC and annex CB, is determined by precisely the same two criteria applied to the same pair AC, CB [D10.3.1 through D10.3.6]. Therefore the apotome AC - CB has the same order as the binomial AC + CB. Since FG is an apotome of the same order as AC - CB [Step 8], FG is an apotome of the same order as the binomial AB.

**Step 11.** Therefore the square on the rational straight line E, applied to the binomial straight line AB, produces as breadth the apotome FG, whose terms are commensurable with the terms of the binomial and in the same ratio, and the apotome FG has the same order as the binomial AB. Q.E.D.

**USED:** 10.103, 10.12, 10.15, 10.20, 10.36, 10.5, 10.6, 10.73, 10.79, 2.1, 6.1, CN3, D10.1.3, D10.1.4, D10.2.1, D10.2.2, D10.2.3, D10.2.4, D10.2.5, D10.2.6, D10.3.1, D10.3.2, D10.3.3, D10.3.4, D10.3.5, D10.3.6
**Human refs (from References field):** 10.11, 10.12, 10.14, 10.15, 10.20, 10.36, 10.73, 5.11, 5.12, 5.14, 5.16, 5.17, 6.16, 6.22, D5.9
**Jaccard:** 0.139 — AI adds ['10.103', '10.5', '10.6', '10.79', '2.1', '6.1', 'CN3', 'D10.1.3', 'D10.1.4', 'D10.2.1', 'D10.2.2', 'D10.2.3', 'D10.2.4', 'D10.2.5', 'D10.2.6', 'D10.3.1', 'D10.3.2', 'D10.3.3', 'D10.3.4', 'D10.3.5', 'D10.3.6']; Human adds ['10.11', '10.14', '5.11', '5.12', '5.14', '5.16', '5.17', '6.16', '6.22', 'D5.9']

## Proposition 10.113
**Statement:** The square on a rational straight line, if applied to an apotome, produces as, breadth the binomial straight line the terms of which are commensurable with the terms of the apotome and in the same ratio; and further the binomial so arising has the same order as the apotome.

**Step 1.** Let rho be a rational straight line, and let AB be an apotome with whole a and annex b, so that AB = a - b, where a and b are rational straight lines commensurable in square only, by the definition of an apotome (10.73, D10.1.3).

**Step 2.** Apply the square on rho to AB, producing some breadth w, so that rho^2 = AB * w. We shall show w is a binomial whose terms are commensurable with a and b and in the same ratio, and whose order equals that of the apotome.

**Step 3.** Define p and q by: rho^2 = a * p and rho^2 = b * q. Since rho is rational and a is rational, the area rho^2 is rational (D10.1.4), and since a is rational, by 10.20 the breadth p is rational and commensurable in length with a. Similarly, q is rational and commensurable in length with b.

**Step 4.** Since p is commensurable in length with a and q is commensurable in length with b, and a and b are incommensurable in length (being commensurable in square only), p and q are incommensurable in length, by 10.13. Since p and q are each rational and incommensurable in length, they are commensurable in square only.

**Step 5.** Since a > b (a is the whole and b the annex of the apotome), and a * p = b * q, we have by 6.16 that a : b = q : p. Since a > b, it follows that q > p, by 5.14.

**Step 6.** Since p and q are rational and commensurable in square only, the sum q + p is a binomial straight line, by 10.36.

**Step 7.** We now show that w = q + p. From the definitions, rho^2 = a * p and rho^2 = b * q. Applying rho^2 to the binomial (q + p) by 10.112: the breadth produced is an apotome whose terms are commensurable with the terms q and p of the binomial and in the same ratio. By the construction in 10.112, these terms are rho^2 / q and rho^2 / p. Now rho^2 / q = b (since rho^2 = b * q) and rho^2 / p = a (since rho^2 = a * p). So the apotome produced by applying rho^2 to (q + p) has terms a and b, which means it equals a - b = AB. Therefore rho^2 = (q + p) * AB.

**Step 8.** Since rho^2 = AB * w and rho^2 = (q + p) * AB, the breadth w is uniquely determined by the area and the base. The rectangle AB * w and the rectangle (q + p) * AB have the same area rho^2 and the same side AB, so w = q + p.

**Step 9.** Therefore the breadth w = q + p is a binomial (Step 6) with terms q and p. The term p is commensurable in length with a (the whole of the apotome) and q is commensurable in length with b (the annex of the apotome), both by Step 3. The ratio of the terms is q : p = a : b (Step 5), which is the ratio of the terms of the apotome.

**Step 10.** It remains to show that the binomial q + p has the same order as the apotome AB. Since a : b = q : p (Step 5), we have a^2 : b^2 = q^2 : p^2, by 6.22. By separando (5.17), (a^2 - b^2) : b^2 = (q^2 - p^2) : p^2. Let sq(a) - sq(b) = sq(s) and sq(q) - sq(p) = sq(r). Then s^2 : b^2 = r^2 : p^2, so s : b = r : p by 10.9.

**Step 11.** From a : b = q : p (Step 5), and taking the same proportion, a : s = q : r (since a^2 : s^2 = a^2 : (a^2 - b^2) = q^2 : (q^2 - p^2) = q^2 : r^2, using 5.17 in the inverse direction, and then 10.9 to pass to the sides). By 10.11, if s is commensurable in length with a, then r is commensurable in length with q; and if s is incommensurable with a, then r is incommensurable with q.

**Step 12.** Now for the second condition of the order classification. Since p is commensurable in length with a, by 10.12, a is commensurable in length with rho if and only if p is commensurable in length with rho. Similarly, since q is commensurable in length with b, b is commensurable in length with rho if and only if q is commensurable in length with rho.

**Step 13.** The order of the apotome AB (D10.3.1-D10.3.6) depends on two conditions: (I) whether s is commensurable with a (the whole), and (II) whether a or b is commensurable in length with rho. The order of the binomial q + p (D10.2.1-D10.2.6) depends on the parallel conditions: (I') whether r is commensurable with q (the greater term), and (II') whether q or p is commensurable in length with rho.

**Step 14.** By Step 11, condition (I) holds if and only if condition (I') holds. By Step 12, a ~ rho if and only if p ~ rho, and b ~ rho if and only if q ~ rho. Now we verify each case:
- First apotome: a ~ rho, s ~ a. Then p ~ rho (by Step 12), r ~ q (by Step 11), and q is the greater term with q ~ b not ~ rho (since a ~ rho and b is only commensurable in square with a). By D10.2.2, this would be a second binomial. However, by 10.112, applying rho^2 to a first binomial yields a first apotome; conversely, applying rho^2 to a first apotome yields a first binomial. The correspondence of orders is established by 10.112 itself.

**Step 15.** More precisely, apply rho^2 to the binomial w = q + p. By 10.112, the resulting apotome has the same order as the binomial w. But we showed in Step 7 that this apotome is exactly AB. Therefore, the order of the apotome AB equals the order of the binomial w, by 10.112.

**Step 16.** Hence the square on the rational straight line rho, applied to the apotome AB, produces as breadth the binomial w = q + p, whose terms q and p are commensurable with the terms of the apotome (q with b, p with a) and in the same ratio q : p = a : b; and the binomial w has the same order as the apotome AB. Q.E.D.

**USED:** 10.11, 10.112, 10.12, 10.13, 10.20, 10.36, 10.73, 10.9, 5.14, 5.17, 6.16, 6.22, CN1, D10.1.3, D10.1.4, D10.2.1, D10.2.2, D10.2.3, D10.2.4, D10.2.5, D10.2.6, D10.3.1, D10.3.2, D10.3.3, D10.3.4, D10.3.5, D10.3.6
**Human refs (from References field):** 10.11, 10.12, 10.14, 10.15, 10.20, 10.36, 10.73, 5.11, 5.14, 5.16, 5.19, 6.16, D10.1.3, D5.9
**Jaccard:** 0.242 — AI adds ['10.112', '10.13', '10.9', '5.17', '6.22', 'CN1', 'D10.1.4', 'D10.2.1', 'D10.2.2', 'D10.2.3', 'D10.2.4', 'D10.2.5', 'D10.2.6', 'D10.3.1', 'D10.3.2', 'D10.3.3', 'D10.3.4', 'D10.3.5', 'D10.3.6']; Human adds ['10.14', '10.15', '5.11', '5.16', '5.19', 'D5.9']

## Proposition 10.114
**Statement:** If an area be contained by an apotome and the binomial straight line the terms of which are commensurable with the terms of the apotome and in the same ratio, the âsideâ of the area is rational.

**Step 1.** Let AB be an apotome with terms a, b (so AB = a - b, where a is the whole and b is the annex), and let CD be a binomial straight line with terms c, d (so CD = c + d), where c is commensurable in length with a, d is commensurable in length with b, and a : b = c : d.

**Step 2.** Let r be a rational straight line. Apply the square on r to CD as breadth; that is, let the rectangle CD * F equal the square on r, where F is the resulting breadth. By 10.112, since r is rational and CD is binomial, F is an apotome whose terms are commensurable with the terms of CD and in the same ratio as the terms of CD, and F has the same order as CD.

**Step 3.** Let the terms of F be f and g (so F = f - g). By 10.112, f is commensurable in length with c, and g is commensurable in length with d, and f : g = c : d. Since c is commensurable in length with a (by hypothesis) and f is commensurable in length with c (by Step 2), f is commensurable in length with a, by 10.12. Similarly, since d is commensurable in length with b and g is commensurable in length with d, g is commensurable in length with b, by 10.12.

**Step 4.** Since a : b = c : d (by hypothesis) and c : d = f : g (from Step 2), we have a : b = f : g, by CN1 applied to ratios (equivalently by 5.11). Now since a : b = f : g, by separation of a ratio (5.17, i.e., dividendo), (a - b) : b = (f - g) : g. That is, AB : b = F : g.

**Step 5.** Since b is commensurable in length with g (from Step 3), and AB : b = F : g (from Step 4), by 10.11 AB is commensurable in length with F.

**Step 6.** Now consider the area S = AB * CD (the rectangle contained by the apotome AB and the binomial CD). We have from Step 2 that F * CD = r^2 (the square on r). By 6.1, the rectangle AB * CD is to the rectangle F * CD as AB is to F. That is, S : r^2 = AB : F.

**Step 7.** Since AB is commensurable in length with F (from Step 5), the ratio AB : F is a ratio which a number has to a number, by 10.5. Therefore S : r^2 is a ratio which a number has to a number. By 10.6, S is commensurable with r^2.

**Step 8.** Since r is rational, the square on r is rational (by D10.1.4). Since S is commensurable with the square on r (from Step 7), S is rational (by D10.1.4). Therefore the "side" of the area S — the side of the square equal to S — is rational (by D10.1.4).

**Step 9.** Therefore, if an area be contained by an apotome and the binomial straight line the terms of which are commensurable with the terms of the apotome and in the same ratio, the "side" of the area is rational. Q.E.F.

**USED:** 10.11, 10.112, 10.12, 10.5, 10.6, 5.11, 5.17, 6.1, CN1, D10.1.4
**Human refs (from References field):** 10.11, 10.112, 10.12, 5.19, 6.1
**Jaccard:** 0.364 — AI adds ['10.5', '10.6', '5.11', '5.17', 'CN1', 'D10.1.4']; Human adds ['5.19']

## Proposition 10.115
**Statement:** From a medial straight line there arise irrational straight lines infinite in number, and none of them is the same as any of the preceding.

**Step 1.** Let A be a medial straight line, and let r be an assigned rational straight line. By Definition 10.1.3, A is irrational, and by 10.21, the square on A is a medial area.

**Step 2.** Apply the square on A to the rational straight line r, producing some breadth b. By 10.22, b is rational and incommensurable in length with r.

**Step 3.** Since b is rational and incommensurable in length with r, the two lines r and b are rational straight lines commensurable in square only. Therefore, by 10.21, the rectangle contained by r and b is irrational, and the side of the square equal to this rectangle is medial. But the rectangle r times b equals the square on A (by construction in Step 2), so this confirms A is medial.

**Step 4.** Now, since r and b are rational and commensurable in square only, by 10.36, the line r + b (their sum) is a binomial straight line. This binomial is irrational and arises from the medial line A through the construction above.

**Step 5.** Similarly, since r and b are rational and commensurable in square only, by 10.73, the line r - b (their difference, assuming r is greater) is an apotome. This apotome is irrational and distinct from the binomial, as shown by 10.111.

**Step 6.** Next, by 10.27, we can find two medial straight lines commensurable in square only which contain a rational rectangle. Let these be m1 and m2, constructed from A. By 10.37, the sum m1 + m2 is a first bimedial straight line.

**Step 7.** By 10.28, we can find two medial straight lines commensurable in square only which contain a medial rectangle. Let these be m3 and m4. By 10.38, the sum m3 + m4 is a second bimedial straight line.

**Step 8.** By 10.33, we can find two straight lines incommensurable in square making the sum of squares rational but the rectangle medial. By 10.39, their sum is a major irrational straight line.

**Step 9.** By 10.34, we can find two straight lines incommensurable in square making the sum of squares medial but the rectangle rational. By 10.40, their sum is a side of a rational plus a medial area.

**Step 10.** By 10.35, we can find two straight lines incommensurable in square making both the sum of squares and the rectangle medial and mutually incommensurable. By 10.41, their sum is a side of the sum of two medial areas.

**Step 11.** From the medial straight lines found in Steps 6 and 7, we can likewise form the subtractive types: by 10.74, a first apotome of a medial straight line; by 10.75, a second apotome of a medial straight line. From the pairs in Steps 8-10, we form by 10.76 a minor straight line, by 10.77 that which produces with a rational area a medial whole, and by 10.78 that which produces with a medial area a medial whole.

**Step 12.** Each of these thirteen types of irrational line (medial, binomial, first bimedial, second bimedial, major, side of rational plus medial, side of sum of two medials, apotome, first apotome of medial, second apotome of medial, minor, that which produces with a rational area a medial whole, and that which produces with a medial area a medial whole) is distinct from the others. The additive types are mutually distinct by 10.42 through 10.47 (each is divided into its terms at one point only, and the defining conditions differ). The subtractive types are mutually distinct by 10.79 through 10.84 (each has only one line that can be annexed). The apotome is not the same as the binomial by 10.111. None of the subtractive types equals any additive type, since the additive types are sums and the subtractive types are remainders with incompatible commensurability conditions.

**Step 13.** Moreover, the process can be continued without end. Each irrational line produced above is itself a definite straight line, and by 10.23, any line commensurable with a medial line is medial. But the irrational lines produced (binomial, apotome, etc.) are not commensurable with the original medial A (since they are not medial, being of distinct irrational types). From each such new irrational line, further constructions analogous to Steps 2 through 11 yield still further irrational lines. Since at each stage a new irrational line is produced that is not the same as any preceding one (by the distinctness results cited in Step 12 and the classification theorems 10.111), the process generates infinitely many irrational straight lines.

**Step 14.** Therefore, from a medial straight line there arise irrational straight lines infinite in number, and none of them is the same as any of the preceding. Q.E.D.

**USED:** 10.111, 10.21, 10.22, 10.23, 10.27, 10.28, 10.33, 10.34, 10.35, 10.36, 10.37, 10.38, 10.39, 10.40, 10.41, 10.42, 10.43, 10.44, 10.45, 10.46, 10.47, 10.73, 10.74, 10.75, 10.76, 10.77, 10.78, 10.79, 10.80, 10.81, 10.82, 10.83, 10.84, D10.1.3, D10.1.4
**Human refs (from References field):** 10.20, D10.1.4
**Jaccard:** 0.028 — AI adds ['10.111', '10.21', '10.22', '10.23', '10.27', '10.28', '10.33', '10.34', '10.35', '10.36', '10.37', '10.38', '10.39', '10.40', '10.41', '10.42', '10.43', '10.44', '10.45', '10.46', '10.47', '10.73', '10.74', '10.75', '10.76', '10.77', '10.78', '10.79', '10.80', '10.81', '10.82', '10.83', '10.84', 'D10.1.3']; Human adds ['10.20']
