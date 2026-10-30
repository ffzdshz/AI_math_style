# Book 5 of Euclid's Elements — Step-by-Step AI Proofs (Run A)

## Proposition 5.1
**Statement:** If a magnitude be the same multiple of a magnitude that a part subtracted is of a part subtracted, the remainder will also be the same multiple of the remainder that the whole is of the whole.

**Step 1.** Let magnitude AB be the same multiple of magnitude CD that the part subtracted AE is of the part subtracted CF. We must show that the remainder EB is the same multiple of the remainder FD that the whole AB is of the whole CD.

**Step 2.** Since AB is the same multiple of CD that AE is of CF, let this common multiple be n. That is, AB = n times CD, and AE = n times CF. By the definition of multiple (D5.2), AB is measured by CD exactly n times, and AE is measured by CF exactly n times.

**Step 3.** Since AB = n times CD, we can decompose AB into n parts each equal to CD. Let AB be divided into magnitudes each equal to CD, say AG, GH, HB, where each equals CD and there are n such parts. Similarly, since AE = n times CF, let AE be divided into magnitudes each equal to CF, say AK, KL, LE, where each equals CF and there are n such parts.

**Step 4.** Now since AE is a part of AB (as AE = n times CF and AB = n times CD, and CF is a part of CD by the setup, so AE is less than AB), the remainder EB = AB - AE.

**Step 5.** Consider the first part AG = CD and the first part AK = CF. Since CF is a part subtracted from CD, the remainder CD - CF = FD. Thus AG - AK = CD - CF = FD. That is, KG = FD (CN3).

**Step 6.** Consider the second part GH = CD and the second part KL = CF. Similarly, GH - KL = CD - CF = FD. That is, LH = FD (CN3).

**Step 7.** Continuing in this manner for each of the n pairs of parts, each difference equals FD. That is, for every pair consisting of a part equal to CD and the corresponding part equal to CF, their difference equals FD (CN3 applied at each stage).

**Step 8.** Now EB, the remainder when AE is subtracted from AB, is composed of exactly these n individual differences. Since each of the n differences equals FD, the remainder EB equals n times FD (D5.2).

**Step 9.** But n is the same multiple by which AB is of CD. Therefore the remainder EB is the same multiple of the remainder FD that the whole AB is of the whole CD. This is what was to be proved.

**USED:** CN3, D5.1, D5.2
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['CN3', 'D5.1', 'D5.2']

## Proposition 5.2
**Statement:** If a first magnitude be the same multiple of a second that a third is of a fourth, and a fifth also be the same multiple of the second that a sixth is of the fourth, the sum of the first and fifth will also be the same multiple of the second that the sum of the third and sixth is of the fourth.

**Step 1.** Let A be the same multiple of B that C is of D, and let E also be the same multiple of B that F is of D. We must show that (A + E) is the same multiple of B that (C + F) is of D.

**Step 2.** Since A is the same multiple of B that C is of D, there is some number m such that A contains B exactly m times and C contains D exactly m times [D5.2]. That is, A is composed of m magnitudes each equal to B, and C is composed of m magnitudes each equal to D.

**Step 3.** Since E is the same multiple of B that F is of D, there is some number n such that E contains B exactly n times and F contains D exactly n times [D5.2]. That is, E is composed of n magnitudes each equal to B, and F is composed of n magnitudes each equal to D.

**Step 4.** Now consider the sum A + E. Since A is composed of m magnitudes each equal to B, and E is composed of n magnitudes each equal to B, their sum A + E is composed of (m + n) magnitudes each equal to B. Therefore A + E is the (m + n)-fold multiple of B [D5.2].

**Step 5.** Similarly, consider the sum C + F. Since C is composed of m magnitudes each equal to D, and F is composed of n magnitudes each equal to D, their sum C + F is composed of (m + n) magnitudes each equal to D. Therefore C + F is the (m + n)-fold multiple of D [D5.2].

**Step 6.** Since A + E equals (m + n) times B and C + F equals (m + n) times D, the sum of the first and fifth is the same multiple of the second that the sum of the third and sixth is of the fourth, namely the (m + n)-fold multiple [D5.2, CN2].

**Step 7.** Therefore, if a first magnitude be the same multiple of a second that a third is of a fourth, and a fifth also be the same multiple of the second that a sixth is of the fourth, the sum of the first and fifth will also be the same multiple of the second that the sum of the third and sixth is of the fourth. Q.E.D.

**USED:** CN2, D5.2
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['CN2', 'D5.2']

## Proposition 5.3
**Statement:** If a first magnitude be the same multiple of a second that a third is of a fourth, and if equimultiples be taken of the first and third, then also ex aequali the magnitudes taken will be equimultiples respectively, the one of the second and the other of the fourth.

**Step 1.** Let A be the same multiple of B that C is of D, so that A = m·B and C = m·D for some count m. Let equimultiples be taken of A and C; that is, let EF = n·A and GH = n·C for some count n. We must show that EF is the same multiple of B that GH is of D.

**Step 2.** Since EF = n·A, we may divide EF into n magnitudes each equal to A; call them E1, E2, ..., En, so that EF = E1 + E2 + ... + En where each Ei = A. Likewise, divide GH into n magnitudes each equal to C; call them G1, G2, ..., Gn, so that GH = G1 + G2 + ... + Gn where each Gi = C. This follows from the definition of equimultiple [D5.2].

**Step 3.** Since A is the same multiple of B that C is of D, each Ei is the same multiple of B that the corresponding Gi is of D. That is, E1 is the same multiple of B that G1 is of D, and E2 is the same multiple of B that G2 is of D, and so on for all n pairs.

**Step 4.** Consider the first two parts: E1 is the same multiple of B that G1 is of D, and E2 is the same multiple of B that G2 is of D. By Proposition 5.2, the sum E1 + E2 is the same multiple of B that G1 + G2 is of D.

**Step 5.** Now E1 + E2 is the same multiple of B that G1 + G2 is of D, and E3 is the same multiple of B that G3 is of D. Applying Proposition 5.2 again, E1 + E2 + E3 is the same multiple of B that G1 + G2 + G3 is of D.

**Step 6.** Proceeding in this manner, applying Proposition 5.2 at each stage to adjoin the next pair of equal parts, after n - 1 applications we conclude that E1 + E2 + ... + En is the same multiple of B that G1 + G2 + ... + Gn is of D.

**Step 7.** But E1 + E2 + ... + En = EF and G1 + G2 + ... + Gn = GH. Therefore EF is the same multiple of B that GH is of D.

**Step 8.** Thus, if equimultiples be taken of the first and third, the magnitudes so taken are equimultiples respectively, the one of the second and the other of the fourth. This is what was to be proved.

**USED:** 5.2, D5.2
**Human refs (from References field):** 5.2
**Jaccard:** 0.500 — AI adds ['D5.2']

## Proposition 5.4
**Statement:** If a first magnitude have to a second the same ratio as a third to a fourth, any equimultiples whatever of the first and third will also have the same ratio to any equimultiples whatever of the second and fourth respectively, taken in corresponding order.

**Step 1.** Let A, B, C, D be magnitudes such that A:B :: C:D. Let m and n be any positive integers. Let E = mA (the m-th multiple of A), F = mC (the m-th multiple of C), G = nB (the n-th multiple of B), and H = nD (the n-th multiple of D). We are to prove that E:G :: F:H, that is, mA:nB :: mC:nD.

**Step 2.** By Definition D5.5, to show that E:G :: F:H, we must show that for any equimultiples whatever of E and F, and any equimultiples whatever of G and H, the former equimultiples alike exceed, are alike equal to, or alike fall short of the latter equimultiples respectively. That is, for arbitrary positive integers p and q: pE and pF simultaneously exceed, equal, or fall short of qG and qH.

**Step 3.** Take any equimultiples pE and pF of E and F, and any equimultiples qG and qH of G and H. Now pE = p(mA), which is the p-th multiple of the m-th multiple of A. By Proposition 5.3, since A is a magnitude, mA is the m-th multiple of A, and p(mA) is the p-th multiple of mA, we conclude that p(mA) is the (pm)-th multiple of A. That is, pE is an equimultiple of A with multiplier pm.

**Step 4.** Similarly, by Proposition 5.3, pF = p(mC) is the (pm)-th multiple of C. Thus pE and pF are equimultiples of A and C respectively, both taken pm times.

**Step 5.** Likewise, qG = q(nB) is the q-th multiple of the n-th multiple of B. By Proposition 5.3, q(nB) is the (qn)-th multiple of B. Similarly, qH = q(nD) is the (qn)-th multiple of D. Thus qG and qH are equimultiples of B and D respectively, both taken qn times.

**Step 6.** Since A:B :: C:D by hypothesis, Definition D5.5 guarantees that for any equimultiples whatever of A and C, and any equimultiples whatever of B and D, the former alike exceed, are alike equal to, or alike fall short of the latter. Applying this with the (pm)-th multiples of A and C, and the (qn)-th multiples of B and D, we conclude: if the (pm)-th multiple of A exceeds the (qn)-th multiple of B, then the (pm)-th multiple of C exceeds the (qn)-th multiple of D; if equal, then equal; if less, then less.

**Step 7.** But as established in Steps 3-5, the (pm)-th multiple of A is pE, the (pm)-th multiple of C is pF, the (qn)-th multiple of B is qG, and the (qn)-th multiple of D is qH. Therefore: if pE exceeds qG, then pF exceeds qH; if pE equals qG, then pF equals qH; if pE falls short of qG, then pF falls short of qH.

**Step 8.** Since p and q were arbitrary positive integers, this holds for any equimultiples whatever of E and F and any equimultiples whatever of G and H. Therefore, by Definition D5.5, E:G :: F:H, that is, mA:nB :: mC:nD.

**Step 9.** Since m and n were any positive integers whatever, any equimultiples whatever of A and C have the same ratio to any equimultiples whatever of B and D respectively, taken in corresponding order. This is what was to be proved.

**USED:** 5.3, D5.5
**Human refs (from References field):** 5.3, D5.5
**Jaccard:** 1.000 — Perfect match.

## Proposition 5.5
**Statement:** If a magnitude be the same multiple of a magnitude that a part subtracted is of a part subtracted, the remainder will also be the same multiple of the remainder that the whole is of the whole.

**Step 1.** Let magnitude AB be the same multiple of magnitude CD that the part AE subtracted is of the part CF subtracted. We must show that the remainder EB is the same multiple of the remainder FD that the whole AB is of the whole CD. [Setup from the hypothesis]

**Step 2.** Since AB is the same multiple of CD that AE is of CF, let this common multiplicity be m. Then AB = m times CD, and AE = m times CF, meaning AB is made up of m magnitudes each equal to CD, and AE is made up of m magnitudes each equal to CF. [D5.2]

**Step 3.** Decompose AB into m parts, each equal to CD: let these be CD_1, CD_2, ..., CD_m, so that AB = CD_1 + CD_2 + ... + CD_m where each CD_i equals CD. Likewise, decompose AE into m parts, each equal to CF: let these be CF_1, CF_2, ..., CF_m, so that AE = CF_1 + CF_2 + ... + CF_m where each CF_i equals CF. [D5.2]

**Step 4.** Since CF is a part of CD (CF is subtracted from CD to leave remainder FD), we have CF less than CD, and FD = CD - CF. For each i from 1 to m, let FD_i = CD_i - CF_i. Since CD_i = CD and CF_i = CF for each i, each remainder FD_i = CD - CF = FD. [CN3]

**Step 5.** Now the remainder EB = AB - AE = (CD_1 + CD_2 + ... + CD_m) - (CF_1 + CF_2 + ... + CF_m). Since we subtract equals from equals in corresponding pairs, EB = (CD_1 - CF_1) + (CD_2 - CF_2) + ... + (CD_m - CF_m) = FD_1 + FD_2 + ... + FD_m. [CN3]

**Step 6.** Since each FD_i equals FD (from Step 4), the sum FD_1 + FD_2 + ... + FD_m consists of m magnitudes each equal to FD. Therefore EB is the same multiple of FD as AB is of CD, namely m times FD. [D5.2]

**Step 7.** Therefore the remainder EB is the same multiple of the remainder FD that the whole AB is of the whole CD, which is what was to be proved.

**USED:** CN3, D5.1, D5.2
**Human refs (from References field):** 5.1
**Jaccard:** 0.000 — AI adds ['CN3', 'D5.1', 'D5.2']; Human adds ['5.1']

## Proposition 5.6
**Statement:** If two magnitudes be equimultiples of two magnitudes, and any magnitudes subtracted from them be equimultiples of the same, the remainders also are either equal to the same or equimultiples of them.

**Step 1.** Let AB and CD be equimultiples of E and F respectively, so that AB is the same multiple of E that CD is of F. Let AG subtracted from AB and CH subtracted from CD be equimultiples of E and F respectively, so that AG is the same multiple of E that CH is of F. We must show that the remainders GB and HD are either equal to E and F respectively, or are equimultiples of them.

**Step 2.** Since AB is the same multiple of E that CD is of F, there is some whole number m such that AB contains E exactly m times and CD contains F exactly m times. That is, AB = mE and CD = mF. [D5.2]

**Step 3.** Since AG is the same multiple of E that CH is of F, there is some whole number n such that AG = nE and CH = nF. [D5.2]

**Step 4.** Since AG is a part subtracted from AB, and AB is a multiple of E while AG is also a multiple of E, we have n < m, so that the subtracted part does not exceed the whole. [CN5]

**Step 5.** Case 1: Suppose m - n = 1, that is, m = n + 1. Then AB = (n+1)E and AG = nE. Since AG is the same multiple of E that AB is of E diminished by one copy, the remainder GB equals E. By the same reasoning, since CD = (n+1)F and CH = nF, the remainder HD equals F. Thus the remainders GB and HD are equal to E and F respectively.

**Step 6.** To see Step 5 more precisely: AB is the same multiple of E that CD is of F, and AG subtracted from AB is the same multiple of E that CH subtracted from CD is of F. By Proposition 5.1, the remainder GB is the same multiple of E that the remainder HD is of F. But since m - n = 1, GB = 1 times E = E, and HD = 1 times F = F. So the remainders are equal to E and F. [5.1]

**Step 7.** Case 2: Suppose m - n > 1. Again, AB is the same multiple of E that CD is of F, and AG is the same multiple of E that CH is of F. By Proposition 5.1, the remainder GB is the same multiple of E that the remainder HD is of F. Since m - n > 1, GB = (m-n)E and HD = (m-n)F, so GB and HD are equimultiples of E and F. [5.1, D5.2]

**Step 8.** Therefore, in both cases the remainders GB and HD are either equal to E and F respectively, or are equimultiples of them. This is what was to be proved.

**USED:** 5.1, CN5, D5.2
**Human refs (from References field):** 5.2
**Jaccard:** 0.000 — AI adds ['5.1', 'CN5', 'D5.2']; Human adds ['5.2']

## Proposition 5.7
**Statement:** Equal magnitudes have to the same the same ratio, as also has the same to equal magnitudes.

**Step 1.** Let A and B be equal magnitudes, and let C be any magnitude of the same kind. We are to prove two things: first, that A:C = B:C; and second, that C:A = C:B.

**Step 2.** [Proof that A:C = B:C.] Take any equimultiples mA of A and mB of B, and any equimultiple nC of C. Since A = B, by repeated application of CN2 (if equals be added to equals, the wholes are equal), we have mA = mB. That is, the same multiple taken of equal magnitudes yields equal magnitudes.

**Step 3.** Since mA = mB, whenever mA exceeds nC, mB also exceeds nC; whenever mA equals nC, mB also equals nC; and whenever mA falls short of nC, mB also falls short of nC. This holds for all equimultiples m and n whatsoever.

**Step 4.** Therefore, by D5.5 (the definition of magnitudes being in the same ratio), A:C = B:C.

**Step 5.** [Proof that C:A = C:B.] Now take any equimultiple mC of C, and any equimultiples nA of A and nB of B. Since A = B, by repeated application of CN2, we have nA = nB.

**Step 6.** Since nA = nB, whenever mC exceeds nA, mC also exceeds nB; whenever mC equals nA, mC also equals nB; and whenever mC falls short of nA, mC also falls short of nB. This holds for all equimultiples m and n whatsoever.

**Step 7.** Therefore, by D5.5, C:A = C:B.

**Step 8.** Hence equal magnitudes have to the same magnitude the same ratio, and the same magnitude has to equal magnitudes the same ratio. Q.E.D.

**USED:** CN2, D5.5
**Human refs (from References field):** D5.5
**Jaccard:** 0.500 — AI adds ['CN2']

## Proposition 5.8
**Statement:** Of unequal magnitudes, the greater has to the same a greater ratio than the less has; and the same has to the less a greater ratio than it has to the greater.

**Step 1.** Let A and B be unequal magnitudes with A greater than B, and let C be any magnitude of the same kind. We must show (i) that A has to C a greater ratio than B has to C, and (ii) that C has to B a greater ratio than C has to A.

**Step 2.** Since A is greater than B, A exceeds B by some magnitude E, so that A = B + E, where E is positive (CN5: A, as the whole, is greater than B, its part, so the excess E exists as a magnitude).

**Step 3.** Since E and C are magnitudes of the same kind, they are capable, when multiplied, of exceeding one another (D5.4). Therefore there exists a positive integer m such that mE > C.

**Step 4.** Since C and B are magnitudes of the same kind, multiples of C can exceed any given magnitude of that kind (D5.4). In particular, there exists a positive integer n such that nC > mB. Let n be the least positive integer with this property, so that nC > mB and (n-1)C is not greater than mB, that is, mB >= (n-1)C.

**Step 5.** Now mA is the same multiple of A that mE is of E, and E is a part of A (since A = B + E and E is less than A). By Proposition 5.1, the remainder when mE is subtracted from mA is the same multiple of the remainder B that mA is of A. That is, mA - mE = mB, or equivalently, mA = mB + mE.

**Step 6.** We show that mA > nC. Since mB >= (n-1)C (from Step 4) and mE > C (from Step 3), we have mA = mB + mE > (n-1)C + C = nC. Therefore mA > nC.

**Step 7.** We also have from Step 4 that nC > mB, which means mB is less than nC, so in particular the m-multiple of B does not exceed the n-multiple of C.

**Step 8.** [Proof of Part (i)] Consider the magnitudes A, C, B, C. Take equimultiples mA of A and mB of B (both using multiplier m), and equimultiples nC of C and nC of C (both using multiplier n). By Step 6, mA > nC (the multiple of the first exceeds the multiple of the second), and by Step 7, mB does not exceed nC (the multiple of the third does not exceed the multiple of the fourth). Therefore, by Definition 5.7, A has to C a greater ratio than B has to C.

**Step 9.** [Proof of Part (ii)] Now consider the magnitudes C, B, C, A. Take equimultiples nC of C and nC of C (both using multiplier n), and equimultiples mB of B and mA of A (both using multiplier m). By Step 7, nC > mB (the multiple of the first exceeds the multiple of the second), and by Step 6, mA > nC, which means nC does not exceed mA (the multiple of the third does not exceed the multiple of the fourth). Therefore, by Definition 5.7, C has to B a greater ratio than C has to A.

**Step 10.** Therefore, of unequal magnitudes, the greater has to the same a greater ratio than the less has; and the same has to the less a greater ratio than it has to the greater. Q.E.F.

**USED:** 5.1, CN5, D5.4, D5.7
**Human refs (from References field):** 5.1, D5.4, D5.7
**Jaccard:** 0.750 — AI adds ['CN5']

## Proposition 5.9
**Statement:** Magnitudes which have the same ratio to the same are equal to one another; and magnitudes to which the same has the same ratio are equal.

**Step 1.** Let A and B be magnitudes which each have the same ratio to a magnitude C, so that A:C = B:C. We claim A = B.

**Step 2.** Suppose A is not equal to B. Then one of them is greater. Without loss of generality, assume A > B.

**Step 3.** Since A > B, by Proposition 5.8, the greater magnitude has to the same a greater ratio than the less has. Therefore A:C > B:C.

**Step 4.** But this contradicts the hypothesis that A:C = B:C. Hence the assumption that A > B is false.

**Step 5.** Similarly, if B > A, then by Proposition 5.8, B:C > A:C, which again contradicts A:C = B:C. Hence B > A is also false.

**Step 6.** Since A is neither greater than nor less than B, we conclude A = B. This completes the first part.

**Step 7.** Now let C be a magnitude which has the same ratio to each of two magnitudes A and B, so that C:A = C:B. We claim A = B.

**Step 8.** Suppose A is not equal to B. Without loss of generality, assume A > B.

**Step 9.** Since A > B, the same magnitude has to the less a greater ratio than it has to the greater (by Proposition 5.8). Therefore C:B > C:A.

**Step 10.** But this contradicts the hypothesis that C:A = C:B. Hence A > B is false.

**Step 11.** Similarly, if B > A, then by Proposition 5.8, C:A > C:B, which again contradicts C:A = C:B. Hence B > A is also false.

**Step 12.** Since A is neither greater than nor less than B, we conclude A = B. This completes the second part.

**Step 13.** Therefore, magnitudes which have the same ratio to the same are equal to one another; and magnitudes to which the same has the same ratio are equal. Q.E.D.

**USED:** 5.8
**Human refs (from References field):** 5.8
**Jaccard:** 1.000 — Perfect match.

## Proposition 5.10
**Statement:** Of magnitudes which have a ratio to the same, that which has a greater ratio is greater; and that to which the same has a greater ratio is less.

**Step 1.** The proposition has two parts. For the first part, let A and B be magnitudes each having a ratio to the same magnitude C, and suppose that A has a greater ratio to C than B has to C. We claim that A is greater than B.

**Step 2.** Consider the three exhaustive cases: either A equals B, A is less than B, or A is greater than B.

**Step 3.** Suppose A equals B. Then by Proposition 5.7, since equal magnitudes have to the same magnitude the same ratio, A has to C the same ratio as B has to C. But this contradicts our hypothesis that A has a greater ratio to C than B has to C. Therefore A does not equal B.

**Step 4.** Suppose A is less than B. Then by Proposition 5.8, since of unequal magnitudes the less has to the same a lesser ratio than the greater has, A has to C a lesser ratio than B has to C. That is, B has to C a greater ratio than A has to C. But this contradicts our hypothesis that A has a greater ratio to C than B has to C. Therefore A is not less than B.

**Step 5.** Since A neither equals B nor is less than B, it follows that A is greater than B. This completes the first part.

**Step 6.** For the second part, let C have a greater ratio to A than C has to B. We claim that A is less than B.

**Step 7.** Again consider the three exhaustive cases: either A equals B, A is greater than B, or A is less than B.

**Step 8.** Suppose A equals B. Then by Proposition 5.7, since the same magnitude has to equal magnitudes the same ratio, C has to A the same ratio as C has to B. But this contradicts our hypothesis that C has a greater ratio to A than C has to B. Therefore A does not equal B.

**Step 9.** Suppose A is greater than B. Then by Proposition 5.8, since the same magnitude has to the less a greater ratio than it has to the greater, C has to B a greater ratio than C has to A. But this contradicts our hypothesis that C has a greater ratio to A than C has to B. Therefore A is not greater than B.

**Step 10.** Since A neither equals B nor is greater than B, it follows that A is less than B. This completes the second part.

**Step 11.** Therefore, of magnitudes which have a ratio to the same, that which has a greater ratio is greater; and that to which the same has a greater ratio is less. Q.E.D.

**USED:** 5.7, 5.8
**Human refs (from References field):** 5.7, 5.8
**Jaccard:** 1.000 — Perfect match.

## Proposition 5.11
**Statement:** Ratios which are the same with the same ratio are also the same with one another.

**Step 1.** Let A, B, C, D, E, F be magnitudes such that A:B :: C:D and C:D :: E:F. We must show that A:B :: E:F.

**Step 2.** Let m and n be any positive integers whatsoever. Take equimultiples mA and mC of A and C, and equimultiples nB and nD of B and D. Since A:B :: C:D, by Definition 5.5, mA and mC alike exceed, are alike equal to, or alike fall short of nB and nD respectively. That is: if mA > nB then mC > nD; if mA = nB then mC = nD; if mA < nB then mC < nD.

**Step 3.** Now take equimultiples mC and mE of C and E (using the same multiplier m), and equimultiples nD and nF of D and F (using the same multiplier n). Since C:D :: E:F, by Definition 5.5, mC and mE alike exceed, are alike equal to, or alike fall short of nD and nF respectively. That is: if mC > nD then mE > nF; if mC = nD then mE = nF; if mC < nD then mE < nF.

**Step 4.** Combining the results of Steps 2 and 3: if mA > nB, then mC > nD (by Step 2), and hence mE > nF (by Step 3). If mA = nB, then mC = nD (by Step 2), and hence mE = nF (by Step 3). If mA < nB, then mC < nD (by Step 2), and hence mE < nF (by Step 3).

**Step 5.** Thus for any equimultiples mA, mE of A and E, and any equimultiples nB, nF of B and F, mA and mE alike exceed, are alike equal to, or alike fall short of nB and nF respectively. Therefore, by Definition 5.5, A:B :: E:F.

**Step 6.** Hence ratios which are the same with the same ratio are also the same with one another. Q.E.D.

**USED:** D5.5
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['D5.5']

## Proposition 5.12
**Statement:** If any number of magnitudes be proportional, as one of the antecedents is to one of the consequents, so will all the antecedents be to all the consequents.

**Step 1.** Let A1, A2, ..., An and B1, B2, ..., Bn be magnitudes such that A1:B1 = A2:B2 = ... = An:Bn. We must show that A1:B1 = (A1 + A2 + ... + An):(B1 + B2 + ... + Bn). It suffices to prove the case for two pairs and then extend by induction; we demonstrate the general argument directly for any number of terms.

**Step 2.** Let m and n be any positive integers. Take the equimultiples m*A1, m*A2, ..., m*An of A1, A2, ..., An respectively, and the equimultiples n*B1, n*B2, ..., n*Bn of B1, B2, ..., Bn respectively.

**Step 3.** By repeated application of Proposition 5.1, the m-fold multiple of the sum A1 + A2 + ... + An equals the sum of the m-fold multiples: m*(A1 + A2 + ... + An) = m*A1 + m*A2 + ... + m*An. To see this: let S = A1 + A2 + ... + An. Since m*S is the same multiple of S that m*A1 is of A1, and A1 is a part of S, by 5.1 the remainder m*S - m*A1 is the same multiple of S - A1 = A2 + ... + An. Continuing this peeling-off process, we obtain m*S = m*A1 + m*A2 + ... + m*An.

**Step 4.** By the same reasoning using 5.1, n*(B1 + B2 + ... + Bn) = n*B1 + n*B2 + ... + n*Bn.

**Step 5.** Since A1:B1 = A2:B2, by Definition 5.5 the equimultiples m*A1 and m*A2 of the antecedents and the equimultiples n*B1 and n*B2 of the consequents satisfy: if m*A1 > n*B1 then m*A2 > n*B2; if m*A1 = n*B1 then m*A2 = n*B2; if m*A1 < n*B1 then m*A2 < n*B2. The same holds for each pair A1:B1 = Ak:Bk, yielding: if m*A1 > n*B1 then m*Ak > n*Bk for every k; and likewise for equality and the less-than case.

**Step 6.** Suppose m*A1 > n*B1. Then by Step 5, m*Ak > n*Bk for every k = 1, 2, ..., n. Since each m*Ak exceeds the corresponding n*Bk, adding these inequalities yields m*A1 + m*A2 + ... + m*An > n*B1 + n*B2 + ... + n*Bn. This follows because if a > b and c > d then a + c > b + d (by CN2 and CN5: a = b + e where e > 0, c = d + f where f > 0, so a + c = (b + d) + (e + f), and the whole b + d + e + f is greater than the part b + d).

**Step 7.** By Steps 3 and 4, this means m*(A1 + A2 + ... + An) > n*(B1 + B2 + ... + Bn).

**Step 8.** By identical reasoning, if m*A1 = n*B1, then m*Ak = n*Bk for all k, so by repeated application of CN2, m*A1 + ... + m*An = n*B1 + ... + n*Bn, that is, m*(A1 + ... + An) = n*(B1 + ... + Bn).

**Step 9.** Similarly, if m*A1 < n*B1, then m*Ak < n*Bk for all k, and summing these inequalities (by the same reasoning as Step 6 with the roles reversed) gives m*(A1 + ... + An) < n*(B1 + ... + Bn).

**Step 10.** Since for arbitrary positive integers m and n, the m-fold multiple of A1 and the m-fold multiple of (A1 + ... + An) alike exceed, are alike equal to, or alike fall short of the n-fold multiple of B1 and the n-fold multiple of (B1 + ... + Bn) respectively, by Definition 5.5 we conclude that A1:B1 = (A1 + A2 + ... + An):(B1 + B2 + ... + Bn).

**Step 11.** Therefore, if any number of magnitudes be proportional, as one of the antecedents is to one of the consequents, so will all the antecedents be to all the consequents. Q.E.D.

**USED:** 5.1, CN2, CN5, D5.5
**Human refs (from References field):** 5.1, D5.5
**Jaccard:** 0.500 — AI adds ['CN2', 'CN5']

## Proposition 5.13
**Statement:** If a first magnitude have to a second the same ratio as a third to a fourth, and the third have to the fourth a greater ratio than a fifth has to a sixth, the first will also have to the second a greater ratio than the fifth to the sixth.

**Step 1.** Let A, B, C, D, E, F be magnitudes such that A:B = C:D, and C:D > E:F. We wish to show that A:B > E:F.

**Step 2.** Since C has to D a greater ratio than E has to F, by the definition of greater ratio (D5.7), there exist equimultiples mC, mE of C, E and equimultiples nD, nF of D, F such that mC > nD but mE is not greater than nF.

**Step 3.** Now mC and mA are equimultiples of C and A respectively (both taken m times), and nD and nB are equimultiples of D and B respectively (both taken n times). Since A:B = C:D, by the definition of same ratio (D5.5), for any equimultiples whatever of A and C, and any equimultiples whatever of B and D, the former equimultiples alike exceed, are alike equal to, or alike fall short of the latter equimultiples taken in corresponding order. In particular, since mC > nD, it follows that mA > nB.

**Step 4.** We have now established that there exist equimultiples mA, mE of A, E and equimultiples nB, nF of B, F such that mA > nB while mE is not greater than nF. Therefore, by the definition of greater ratio (D5.7), A has to B a greater ratio than E has to F. That is, A:B > E:F.

**Step 5.** Therefore, if a first magnitude have to a second the same ratio as a third to a fourth, and the third have to the fourth a greater ratio than a fifth has to a sixth, the first will also have to the second a greater ratio than the fifth to the sixth. Q.E.D.

**USED:** D5.5, D5.7
**Human refs (from References field):** D5.5, D5.7
**Jaccard:** 1.000 — Perfect match.

## Proposition 5.14
**Statement:** If a first magnitude have to a second the same ratio as a third has to a fourth, and the first be greater than the third, the second will also be greater than the fourth; if equal, equal; and if less, less.

**Step 1.** Let A, B, C, D be magnitudes such that A:B = C:D, where A and C are of the same kind, and B and D are of the same kind.

**Step 2.** [Case 1: A > C implies B > D.] Suppose A > C. Assume for contradiction that B is not greater than D; then either B = D or B < D.

**Step 3.** First suppose B = D. Since A = C is false (we have A > C), consider: because B = D, the ratio C:D is the same as C:B. Since A:B = C:D (given) and C:D = C:B, by 5.11 (ratios which are the same with the same ratio are also the same with one another), A:B = C:B.

**Step 4.** By 5.9 (magnitudes which have the same ratio to the same are equal to one another), since A:B = C:B, we conclude A = C. This contradicts A > C.

**Step 5.** Now suppose B < D. By 5.8 (the same has to the less a greater ratio than it has to the greater), since B < D, C:B > C:D. Since A:B = C:D (given), we have C:B > A:B.

**Step 6.** By 5.10 (of magnitudes which have a ratio to the same, that which has a greater ratio is greater), since C:B > A:B, we conclude C > A. This contradicts A > C.

**Step 7.** Since both alternatives B = D and B < D lead to contradictions, we conclude B > D.

**Step 8.** [Case 2: A = C implies B = D.] Suppose A = C. By 5.7 (equal magnitudes have to the same the same ratio), since A = C, A:B = C:B.

**Step 9.** But A:B = C:D (given). By 5.11, C:B = C:D.

**Step 10.** By 5.9 (magnitudes to which the same has the same ratio are equal), since C:B = C:D, we conclude B = D.

**Step 11.** [Case 3: A < C implies B < D.] Suppose A < C. Assume for contradiction that B is not less than D; then either B = D or B > D.

**Step 12.** First suppose B = D. Then as in Step 3, C:D = C:B, so A:B = C:B by 5.11. By 5.9, A = C. This contradicts A < C.

**Step 13.** Now suppose B > D. By 5.8, since B > D, C:D > C:B (the same has to the less a greater ratio than it has to the greater). Since A:B = C:D, we have A:B > C:B.

**Step 14.** By 5.10, since A:B > C:B, A > C. This contradicts A < C.

**Step 15.** Since both alternatives lead to contradictions, B < D.

**Step 16.** Therefore, if a first magnitude have to a second the same ratio as a third has to a fourth, and the first be greater than the third, the second will also be greater than the fourth; if equal, equal; and if less, less. Q.E.D.

**USED:** 5.10, 5.11, 5.7, 5.8, 5.9
**Human refs (from References field):** 5.10, 5.13, 5.8
**Jaccard:** 0.333 — AI adds ['5.11', '5.7', '5.9']; Human adds ['5.13']

## Proposition 5.15
**Statement:** Parts have the same ratio as the same multiples of them taken in corresponding order.

**Step 1.** Let A and B be any two magnitudes, and let mA and mB be equimultiples of them, that is, let mA be m times A and mB be m times B, for some positive integer m [D5.2]. We are to prove that A : B = mA : mB.

**Step 2.** By D5.5, it suffices to show that for any positive integers n and p, if we take the n-th multiple of A and the n-th multiple of mA (the first and third magnitudes), and the p-th multiple of B and the p-th multiple of mB (the second and fourth magnitudes), then n(mA) exceeds, equals, or falls short of p(mB) according as nA exceeds, equals, or falls short of pB.

**Step 3.** Since mA is m times A and we take the n-th multiple of mA, by 5.3 (equimultiples of equimultiples), n(mA) = (nm) times A. Similarly, since mB is m times B and we take the p-th multiple of mB, by 5.3, p(mB) = (pm) times B.

**Step 4.** Now, nA is n times A, and taking the m-th multiple of nA, by 5.3 again, m(nA) = (mn) times A. Since nm = mn, we have (nm) times A equals (mn) times A, so n(mA) = m(nA). By the same reasoning, pB is p times B, and m(pB) = (mp) times B. Since pm = mp, p(mB) = m(pB).

**Step 5.** It remains to show that m(nA) and m(pB) compare in the same way as nA and pB. We consider three cases.

**Step 6.** Case 1: Suppose nA > pB. Then nA exceeds pB by some magnitude E, so that nA = pB + E. Now m(nA) is m times the whole nA, and m(pB) is m times the part pB. By 5.1 (if a magnitude is the same multiple of a magnitude that a part subtracted is of a part subtracted, the remainder is the same multiple of the remainder), m(nA) minus m(pB) equals mE. Therefore m(nA) = m(pB) + mE. Since E is a positive magnitude, mE is a magnitude that contains E as a part, so mE is greater than zero [CN5]. Hence m(nA) > m(pB), that is, n(mA) > p(mB).

**Step 7.** Case 2: Suppose nA = pB. Then nA and pB are equal magnitudes. Taking the same multiple m of each, m(nA) = m(pB) [CN1, since equal magnitudes taken the same number of times yield equal results]. Hence n(mA) = p(mB).

**Step 8.** Case 3: Suppose nA < pB. Then pB > nA, and by the same argument as Case 1 (with the roles of nA and pB exchanged), m(pB) > m(nA), that is, p(mB) > n(mA), which means n(mA) < p(mB).

**Step 9.** Therefore, in all three cases, n(mA) exceeds, equals, or falls short of p(mB) according as nA exceeds, equals, or falls short of pB. Since n and p were arbitrary, the definition of same ratio [D5.5] is satisfied, and we conclude that A : B = mA : mB. That is, parts have the same ratio as the same multiples of them taken in corresponding order. Q.E.D.

**USED:** 5.1, 5.3, CN1, CN5, D5.2, D5.5
**Human refs (from References field):** 5.12, 5.7
**Jaccard:** 0.000 — AI adds ['5.1', '5.3', 'CN1', 'CN5', 'D5.2', 'D5.5']; Human adds ['5.12', '5.7']

## Proposition 5.16
**Statement:** If four magnitudes be proportional, they will also be proportional alternately.

**Step 1.** Let A, B, C, D be four magnitudes such that A : B :: C : D, where A and C are of the same kind, and B and D are of the same kind. We are to show that they are proportional alternately, that is, A : C :: B : D. [D5.5, D5.12]

**Step 2.** Take any equimultiples mA, mB of A, B respectively, and any equimultiples nC, nD of C, D respectively.

**Step 3.** Since mA, mB are the same multiples of A, B respectively, by Proposition 5.15, A : B :: mA : mB. That is, the ratio of A to B equals the ratio of their equimultiples mA to mB. [5.15]

**Step 4.** Since nC, nD are the same multiples of C, D respectively, by Proposition 5.15, C : D :: nC : nD. [5.15]

**Step 5.** But A : B :: C : D by hypothesis. Therefore, by Step 3 and Step 4, mA : mB :: A : B :: C : D :: nC : nD. Hence mA : mB :: nC : nD, since ratios which are the same with the same ratio are also the same with one another. [5.11]

**Step 6.** Since mA : mB :: nC : nD, by Proposition 5.14: if mA is greater than nC, then mB is greater than nD; if mA is equal to nC, then mB is equal to nD; and if mA is less than nC, then mB is less than nD. [5.14]

**Step 7.** Now mA, mB are arbitrary equimultiples of A, B, and nC, nD are arbitrary equimultiples of C, D. Since for all such equimultiples, mA exceeds, equals, or falls short of nC according as mB exceeds, equals, or falls short of nD, it follows by Definition 5.5 that A : C :: B : D. [D5.5]

**Step 8.** Therefore, if four magnitudes be proportional, they will also be proportional alternately. Q.E.D.

**USED:** 5.11, 5.14, 5.15, D5.12, D5.5
**Human refs (from References field):** 5.11, 5.14, 5.15, D5.5
**Jaccard:** 0.800 — AI adds ['D5.12']

## Proposition 5.17
**Statement:** If magnitudes be proportional componendo, they will also be proportional separando.

**Step 1.** Let AE, EB, CF, FD be four magnitudes proportional componendo, so that AE:EB :: CF:FD, where AE is the whole, EB the part, CF the whole, and FD the part. We must show that they are proportional separando, that is, AB:EB :: CD:FD, where AB is the excess of AE over EB, and CD is the excess of CF over FD. [D5.14, D5.15]

**Step 2.** Let G, H be any equimultiples whatever of AB, CD, and let K, L be any equimultiples whatever of EB, FD. We must show that G and K satisfy the same order relation (greater, equal, or less) as H and L, so that AB:EB :: CD:FD by the definition of proportion. [D5.5]

**Step 3.** Since G is the same multiple of AB that H is of CD, and K is the same multiple of EB that L is of FD, consider G + K and H + L. Now G is m times AB and K is n times EB for some positive integers m, n. Then G + K = m·AB + n·EB. By Proposition 5.1, since AE = AB + EB, we have that m·AE = m·AB + m·EB. So G + K = m·AB + n·EB is not directly a multiple of AE unless m = n, which need not hold. We must proceed differently. [5.1]

**Step 4.** Since G is m times AB, and AB = AE - EB, we have G = m·AE - m·EB. Therefore G + K = m·AE - m·EB + K = m·AE + (K - m·EB). Let us instead work directly with the equimultiple characterization.

**Step 5.** Take any equimultiples: let G = m·AB and H = m·CD, and let K = n·EB and L = n·FD, for arbitrary positive integers m, n. We need to show: if G > K then H > L, if G = K then H = L, and if G < K then H < L.

**Step 6.** Form (G + K) and (H + L). We compute: G + K = m·AB + n·EB. Since AB = AE - EB, this equals m·AE - m·EB + n·EB = m·AE + (n - m)·EB. Similarly, H + L = m·CD + n·FD = m·CF - m·FD + n·FD = m·CF + (n - m)·FD.

**Step 7.** Now m·AE is the same multiple of AE that m·CF is of CF, and (n - m)·EB is the same multiple of EB that (n - m)·FD is of FD. But (n - m) may be negative, so let us handle this more carefully using Euclid's framework.

**Step 8.** Consider instead: G + K = m·AB + n·EB, and note that m·AE = m·AB + m·EB by Proposition 5.1 (since AE = AB + EB, taking m-multiples). So G + K = m·AE + (n - m)·EB, which we can write as G + K = m·AE - m·EB + n·EB. That is, G + K + m·EB = m·AE + n·EB. [5.1]

**Step 9.** Let M = G + K + m·EB and N = H + L + m·FD. Then M = m·AE + n·EB and N = m·CF + n·FD. Now m·AE is the same multiple of AE that m·CF is of CF, and n·EB is the same multiple of EB that n·FD is of FD. By Proposition 5.2, M = m·AE + n·EB is the same relation to AE and EB as N = m·CF + n·FD is to CF and FD. [5.2]

**Step 10.** More precisely: m·AE and n·EB are equimultiples of AE and EB (with multipliers m and n respectively), and m·CF and n·FD are equimultiples of CF and FD (with the same multipliers m and n). Since AE:EB :: CF:FD by hypothesis, and since m·AE, m·CF are any equimultiples of the first and third, while n·EB, n·FD are any equimultiples of the second and fourth, the definition of proportion (D5.5) tells us: m·AE > n·EB if and only if m·CF > n·FD, m·AE = n·EB if and only if m·CF = n·FD, and m·AE < n·EB if and only if m·CF < n·FD. [D5.5]

**Step 11.** Now M = m·AE + n·EB and the comparison of m·AE with n·EB determines the relationship. But we need the comparison of G = m·AB with K = n·EB. Since m·AE = m·AB + m·EB (by 5.1, as AE = AB + EB), we have m·AE > n·EB if and only if m·AB + m·EB > n·EB, which holds if and only if m·AB > n·EB - m·EB = (n - m)·EB. This approach requires case analysis on whether n >= m. [5.1]

**Step 12.** Let us use a cleaner approach. We rewrite the condition. Since AE = AB + EB and CF = CD + FD, we have m·AE = m·AB + m·EB and m·CF = m·CD + m·FD by Proposition 5.1. [5.1]

**Step 13.** Now consider equimultiples m·AE and m·CF of the first and third magnitudes AE, CF, and equimultiples (m + n)·EB and (m + n)·FD of the second and fourth magnitudes EB, FD, where m and n are any positive integers. By hypothesis AE:EB :: CF:FD (D5.5), so: m·AE > (m + n)·EB iff m·CF > (m + n)·FD; m·AE = (m + n)·EB iff m·CF = (m + n)·FD; m·AE < (m + n)·EB iff m·CF < (m + n)·FD. [D5.5]

**Step 14.** Since m·AE = m·AB + m·EB (Step 12), the condition m·AE > (m + n)·EB is equivalent to m·AB + m·EB > (m + n)·EB, which simplifies to m·AB > n·EB. Similarly, m·CF = m·CD + m·FD, so m·CF > (m + n)·FD is equivalent to m·CD + m·FD > (m + n)·FD, which simplifies to m·CD > n·FD. The same equivalences hold for equality and less-than. [CN1, CN2, CN3]

**Step 15.** Therefore: m·AB > n·EB if and only if m·CD > n·FD; m·AB = n·EB if and only if m·CD = n·FD; m·AB < n·EB if and only if m·CD < n·FD. Since m and n are arbitrary positive integers, and m·AB, m·CD are equimultiples of AB and CD while n·EB, n·FD are equimultiples of EB and FD, by Definition 5.5 we conclude AB:EB :: CD:FD. [D5.5]

**Step 16.** This is exactly the statement that the magnitudes are proportional separando (D5.15): the excess-to-part ratios are equal. Therefore, if magnitudes be proportional componendo, they will also be proportional separando. [D5.15]

**USED:** 5.1, CN2, CN3, D5.14, D5.15, D5.5
**Human refs (from References field):** 5.1, 5.2
**Jaccard:** 0.143 — AI adds ['CN2', 'CN3', 'D5.14', 'D5.15', 'D5.5']; Human adds ['5.2']

## Proposition 5.18
**Statement:** If magnitudes be proportional separando, they will also be proportional componendo.

**Step 1.** Let AE, EB, CF, FD be magnitudes such that AE : EB :: CF : FD (proportional separando), where AE is the excess of AB over BE (so AB = AE + BE), and CF is the excess of CD over DF (so CD = CF + FD). We are to show that AB : BE :: CD : DF (proportional componendo). [D5.14, D5.15]

**Step 2.** By D5.5, to prove AB : BE :: CD : DF, we must show that for any equimultiples m·AB and m·CD of the first and third, and any equimultiples n·BE and n·DF of the second and fourth, the former equimultiples alike exceed, are alike equal to, or alike fall short of the latter equimultiples taken in corresponding order. That is, we must establish: (i) if m·AB > n·BE then m·CD > n·DF, (ii) if m·AB = n·BE then m·CD = n·DF, and (iii) if m·AB < n·BE then m·CD < n·DF. [D5.5]

**Step 3.** Since AB = AE + BE and AE is the same multiple of AE that BE is of BE (namely, both taken m times), by 5.1, m·AE = m·AB - m·BE, which gives m·AB = m·AE + m·BE. Similarly, m·CD = m·CF + m·DF. [5.1]

**Step 4.** Also, by 5.2, since (n - m)·BE and m·BE are equimultiples of BE, their sum (n - m)·BE + m·BE equals n·BE. Likewise, (n - m)·DF + m·DF = n·DF. This identity will be used when n > m. [5.2]

**Step 5.** We now prove case (i). Suppose m·AB > n·BE. Then m·AE + m·BE > n·BE. If n > m, subtracting m·BE from both sides yields m·AE > (n - m)·BE (the subtraction being valid since m·BE < n·BE when n > m). Now m·AE and m·CF are equimultiples of AE and CF, and (n - m)·BE and (n - m)·DF are equimultiples of BE and DF. Since AE : EB :: CF : FD by hypothesis, D5.5 gives m·CF > (n - m)·DF. Adding m·DF to both sides, m·CF + m·DF > (n - m)·DF + m·DF, that is, m·CD > n·DF. [D5.5, CN2, CN3]

**Step 6.** Still in case (i), if n is less than or equal to m, then since m is at least n, the magnitude m·DF is at least n·DF. Moreover, m·CF is a positive magnitude (as CF is a magnitude and m is at least 1). Therefore m·CD = m·CF + m·DF > n·DF. Thus in all sub-cases, m·AB > n·BE implies m·CD > n·DF. [CN5]

**Step 7.** We prove case (ii). Suppose m·AB = n·BE. Then m·AE + m·BE = n·BE. Since m·AE is a positive magnitude, this requires n > m. Subtracting m·BE from both sides, m·AE = (n - m)·BE. Since AE : EB :: CF : FD by hypothesis, D5.5 gives m·CF = (n - m)·DF. Adding m·DF to both sides, m·CF + m·DF = (n - m)·DF + m·DF, that is, m·CD = n·DF. [D5.5, CN2, CN3]

**Step 8.** We prove case (iii). Suppose m·AB < n·BE. Then m·AE + m·BE < n·BE, so n > m (since if n were at most m, we would have n·BE at most m·BE, and then m·AE + m·BE > m·BE, giving m·AB > n·BE, a contradiction). Subtracting m·BE from both sides, m·AE < (n - m)·BE. Since AE : EB :: CF : FD by hypothesis, D5.5 gives m·CF < (n - m)·DF. Adding m·DF to both sides, m·CF + m·DF < (n - m)·DF + m·DF, that is, m·CD < n·DF. [D5.5, CN2, CN3]

**Step 9.** Since in every case the equimultiples m·AB, m·CD of the first and third alike exceed, are alike equal to, or alike fall short of the equimultiples n·BE, n·DF of the second and fourth, it follows by D5.5 that AB : BE :: CD : DF. That is, the magnitudes are proportional componendo. [D5.5, D5.14]

**Step 10.** Therefore, if magnitudes be proportional separando, they will also be proportional componendo. Q.E.D.

**USED:** 5.1, 5.2, CN2, CN3, CN5, D5.14, D5.15, D5.5
**Human refs (from References field):** 5.11, 5.14, 5.17
**Jaccard:** 0.000 — AI adds ['5.1', '5.2', 'CN2', 'CN3', 'CN5', 'D5.14', 'D5.15', 'D5.5']; Human adds ['5.11', '5.14', '5.17']

## Proposition 5.19
**Statement:** If, as a whole is to a whole, so is a part subtracted to a part subtracted, the remainder will also be to the remainder as whole to whole.

**Step 1.** Let AB and CD be whole magnitudes, and let AE and CF be parts subtracted from them respectively, so that AB:CD = AE:CF. Let EB be the remainder AB minus AE, and FD be the remainder CD minus CF. We must show that EB:FD = AB:CD.

**Step 2.** Since AB:CD = AE:CF, by alternation (5.16), we have AB:AE = CD:CF.

**Step 3.** Since AB:AE = CD:CF, and these magnitudes are proportional componendo (that is, the whole AB to the part AE, and the whole CD to the part CF), by 5.17 (if magnitudes be proportional componendo, they will also be proportional separando), we obtain EB:AE = FD:CF, where EB = AB - AE and FD = CD - CF.

**Step 4.** Since EB:AE = FD:CF, by alternation (5.16), we have EB:FD = AE:CF.

**Step 5.** But AB:CD = AE:CF was given. Therefore, since EB:FD = AE:CF and AB:CD = AE:CF, by 5.11 (ratios which are the same with the same ratio are also the same with one another), we conclude EB:FD = AB:CD.

**Step 6.** Therefore, if as a whole is to a whole so is a part subtracted to a part subtracted, the remainder is also to the remainder as whole to whole. Q.E.D.

**USED:** 5.11, 5.16, 5.17
**Human refs (from References field):** 5.11, 5.16, 5.17
**Jaccard:** 1.000 — Perfect match.

## Proposition 5.20
**Statement:** If there be three magnitudes, and others equal to them in multitude, which taken two and two are in the same ratio, and if ex aequali the first be greater than the third, the fourth will also be greater than the sixth; if equal, equal; and, if less, less.

**Step 1.** Let A, B, C be three magnitudes and D, E, F be another three magnitudes such that A:B = D:E and B:C = E:F. We must show that if A > C then D > F; if A = C then D = F; and if A < C then D < F.

**Step 2.** Since B:C = E:F, by the definition of same ratio (D5.5), for any equimultiples nB, nE of B, E and mC, mF of C, F: nB > mC if and only if nE > mF, nB = mC if and only if nE = mF, and nB < mC if and only if nE < mF. In particular, this means that C:B = F:E, since the equimultiple conditions for the ratio C:B are precisely the equimultiple conditions for the ratio F:E when we apply D5.5 to B:C = E:F with the roles of the multipliers exchanged.

**Step 3.** Case 1: Suppose A > C. Since A is greater than C and both have a ratio to B, by 5.8, A has to B a greater ratio than C has to B, that is, A:B > C:B.

**Step 4.** Since A:B = D:E (given), and A:B > C:B (Step 3), by 5.13 (if a first magnitude has to a second the same ratio as a third to a fourth, and the third to the fourth a greater ratio than a fifth to a sixth, then the first also has to the second a greater ratio than the fifth to the sixth), taking D:E as the first-to-second, A:B as the third-to-fourth, and C:B as the fifth-to-sixth, we conclude D:E > C:B.

**Step 5.** By D5.7, since D:E > C:B, there exist positive integers m and n such that mD > nE but mC does not exceed nB, that is, nB >= mC.

**Step 6.** Since B:C = E:F (given) and nB >= mC: if nB > mC, then nE > mF by D5.5; if nB = mC, then nE = mF by D5.5. In either case, nE >= mF.

**Step 7.** From Steps 5 and 6, mD > nE and nE >= mF, so mD > mF. Since mD = m times D and mF = m times F with m a positive integer, it follows that D > F.

**Step 8.** Case 2: Suppose A = C. Since A and C are equal, by 5.7, A and C have to B the same ratio, that is, A:B = C:B.

**Step 9.** Since A:B = D:E (given) and A:B = C:B (Step 8), by 5.11 (ratios which are the same with the same ratio are also the same with one another), D:E = C:B.

**Step 10.** From Step 2, C:B = F:E. Combined with D:E = C:B (Step 9), by 5.11 again, D:E = F:E.

**Step 11.** Since D:E = F:E, that is, D and F have the same ratio to E, by 5.9 (magnitudes which have the same ratio to the same are equal to one another), D = F.

**Step 12.** Case 3: Suppose A < C. Since C is greater than A, by 5.8, C has to B a greater ratio than A has to B, that is, C:B > A:B.

**Step 13.** Since A:B = D:E (given), by D5.5, for any equimultiples mA, mD of A, D and nB, nE of B, E: mA > nB if and only if mD > nE, and mA <= nB if and only if mD <= nE. Since C:B > A:B, by D5.7 there exist positive integers m and n such that mC > nB and mA <= nB. By the equivalence just stated, mA <= nB gives mD <= nE. Thus mC > nB and mD <= nE, which by D5.7 means C:B > D:E.

**Step 14.** From Step 2, C:B = F:E. Since C:B > D:E (Step 13), and C:B = F:E, by D5.5 and D5.7, the equimultiple conditions witnessing C:B > D:E are identical to those witnessing F:E > D:E. Therefore F:E > D:E.

**Step 15.** Since F:E > D:E, that is, F has to E a greater ratio than D has to E, by 5.10 (of magnitudes which have a ratio to the same, that which has a greater ratio is greater), F > D, and therefore D < F.

**Step 16.** Thus in all three cases the result holds: if A > C then D > F; if A = C then D = F; if A < C then D < F. This is what was to be proved.

**USED:** 5.10, 5.11, 5.13, 5.7, 5.8, 5.9, D5.5, D5.7
**Human refs (from References field):** 5.10, 5.13, 5.8
**Jaccard:** 0.375 — AI adds ['5.11', '5.7', '5.9', 'D5.5', 'D5.7']

## Proposition 5.21
**Statement:** If there be three magnitudes, and others equal to them in multitude, which taken two and two together are in the same ratio, and the proportion of them be perturbed, then, if ex aequali the first magnitude is greater than the third, the fourth will also be greater than the sixth; if equal, equal; and if less, less.

**Step 1.** Let A, B, C be three magnitudes, and D, E, F be others equal to them in multitude, which taken two and two are in the same ratio with the proportion perturbed, so that A:B = E:F and B:C = D:E. We must show that, ex aequali, if A > C then D > F; if A = C then D = F; and if A < C then D < F. [D5.17, D5.18]

**Step 2.** Note that from B:C = D:E, by the definition of same ratio (D5.5) and inverse ratio (D5.13), we have C:B = E:D. For if for all equimultiples m and n, mB exceeds, equals, or falls short of nC according as mD exceeds, equals, or falls short of nE, then equally nC exceeds, equals, or falls short of mB according as nE exceeds, equals, or falls short of mD. Thus C:B = E:D.

**Step 3.** [Case 1: A > C.] Since A > C, by 5.8, A has to B a greater ratio than C has to B, that is, A:B > C:B.

**Step 4.** Since A:B = E:F (given) and A:B > C:B (Step 3), by 5.13 (with E:F as the ratio equal to A:B, and C:B as the lesser ratio), we conclude E:F > C:B.

**Step 5.** Since C:B = E:D (Step 2) and E:F > C:B (Step 4), by 5.13, E:F > E:D.

**Step 6.** Since E has to F a greater ratio than E has to D, by the second part of 5.10 (that to which the same magnitude has a greater ratio is less), F < D, that is, D > F.

**Step 7.** [Case 2: A = C.] Since A = C, by 5.7, A:B = C:B.

**Step 8.** Since A:B = E:F (given) and A:B = C:B (Step 7), by 5.11, E:F = C:B.

**Step 9.** Since C:B = E:D (Step 2) and E:F = C:B (Step 8), by 5.11, E:F = E:D.

**Step 10.** Since E has the same ratio to F as E has to D, by 5.9 (magnitudes to which the same has the same ratio are equal), D = F.

**Step 11.** [Case 3: A < C.] Since C > A, by 5.8, C has to B a greater ratio than A has to B, that is, C:B > A:B.

**Step 12.** Since A:B = E:F (given) and C:B > A:B (Step 11), then C:B > E:F. Since C:B = E:D (Step 2), by 5.13, E:D > E:F.

**Step 13.** Since E has to D a greater ratio than E has to F, by the second part of 5.10, D < F.

**Step 14.** Therefore, if A > C then D > F; if A = C then D = F; and if A < C then D < F. Q.E.D.

**USED:** 5.10, 5.11, 5.13, 5.7, 5.8, 5.9, D5.13, D5.17, D5.18, D5.5
**Human refs (from References field):** 5.10, 5.13, 5.8
**Jaccard:** 0.300 — AI adds ['5.11', '5.7', '5.9', 'D5.13', 'D5.17', 'D5.18', 'D5.5']

## Proposition 5.22
**Statement:** If there be any number of magnitudes whatever, and others equal to them in multitude, which taken two and two together are in the same ratio, they will also be in the same ratio ex aequali.

**Step 1.** Let A1, A2, ..., An be any number of magnitudes, and B1, B2, ..., Bn others equal to them in multitude, which taken two and two together are in the same ratio, so that A1:A2 = B1:B2, A2:A3 = B2:B3, ..., A(n-1):An = B(n-1):Bn. We must show that A1:An = B1:Bn, that is, the ratio ex aequali holds [D5.17].

**Step 2.** We first prove the result for three magnitudes on each side. Let A, B, C be magnitudes and D, E, F be others such that A:B = D:E and B:C = E:F. We shall show A:C = D:F.

**Step 3.** Take any equimultiples whatever mA and mD of A and D respectively, and any equimultiples whatever nC and nF of C and F respectively.

**Step 4.** Since A:B = D:E, by Proposition 5.4 (equimultiples of the first and third have the same ratio to equimultiples of the second and fourth), taking m-fold equimultiples of the first and third, and m-fold equimultiples of the second and fourth, we obtain mA:mB = mD:mE.

**Step 5.** Since B:C = E:F, by Proposition 5.4 again, taking m-fold equimultiples of the first and third, and n-fold equimultiples of the second and fourth, we obtain mB:nC = mE:nF.

**Step 6.** Now mA, mB, nC are three magnitudes, and mD, mE, nF are three others equal to them in multitude, which taken two and two are in the same ratio: mA:mB = mD:mE and mB:nC = mE:nF.

**Step 7.** Therefore, by Proposition 5.20 (for three magnitudes taken two and two in the same ratio, the ex aequali ordering is preserved): if mA > nC then mD > nF; if mA = nC then mD = nF; and if mA < nC then mD < nF.

**Step 8.** But mA, mD are arbitrary equimultiples of A, D and nC, nF are arbitrary equimultiples of C, F. Since the equimultiples of the first and third alike exceed, are alike equal to, or alike fall short of the equimultiples of the second and fourth respectively taken in corresponding order, by the definition of same ratio [D5.5], A:C = D:F. This establishes the result for three magnitudes.

**Step 9.** Now we prove the general case by induction on the number of magnitudes. The case of three magnitudes on each side has been established in Steps 2-8. Suppose the result holds for any collection of (n-1) magnitudes on each side, and consider n magnitudes A1, A2, ..., An with corresponding B1, B2, ..., Bn satisfying A1:A2 = B1:B2, A2:A3 = B2:B3, ..., A(n-1):An = B(n-1):Bn.

**Step 10.** By the inductive hypothesis applied to the (n-1) magnitudes A1, A2, ..., A(n-1) and B1, B2, ..., B(n-1), since they are taken two and two in the same ratio, we conclude that A1:A(n-1) = B1:B(n-1).

**Step 11.** Now we have three magnitudes A1, A(n-1), An and three others B1, B(n-1), Bn with A1:A(n-1) = B1:B(n-1) (from Step 10) and A(n-1):An = B(n-1):Bn (given). By the three-magnitude case established in Steps 2-8, A1:An = B1:Bn.

**Step 12.** Therefore, by induction, for any number of magnitudes whatever, and others equal to them in multitude, which taken two and two together are in the same ratio, they will also be in the same ratio ex aequali. Q.E.D.

**USED:** 5.20, 5.4, D5.17, D5.5
**Human refs (from References field):** 5.20, 5.4, D5.5
**Jaccard:** 0.750 — AI adds ['D5.17']

## Proposition 5.23
**Statement:** If there be three magnitudes, and others equal to them in multitude, which taken two and two together are in the same ratio, and the proportion of them be perturbed, they will also be in the same ratio ex aequali.

**Step 1.** Let A, B, C be three magnitudes and D, E, F be others equal to them in multitude, which taken two and two together are in the same ratio and the proportion of them is perturbed. That is, A : B :: E : F, and B : C :: D : E. We must show that A : C :: D : F (the ratio ex aequali) [D5.17, D5.18].

**Step 2.** Let m and n be any two positive integers. Take equimultiples G, H, K of A, B, D respectively, so that G = mA, H = mB, K = mD. Take equimultiples L, M, N of C, E, F respectively, so that L = nC, M = nE, N = nF.

**Step 3.** Since A : B :: E : F (given), by 5.15 we have mA : mB :: A : B, that is, G : H :: A : B. Likewise by 5.15, nE : nF :: E : F, that is, M : N :: E : F. Since A : B :: E : F and G : H :: A : B and M : N :: E : F, by 5.11 (transitivity of equal ratios), G : H :: M : N.

**Step 4.** Since B : C :: D : E (given), by 5.4, taking m-multiples of the first and third (B and D) and n-multiples of the second and fourth (C and E), we obtain mB : nC :: mD : nE, that is, H : L :: K : M.

**Step 5.** Now G, H, L are three magnitudes and K, M, N are three magnitudes taken two and two in the same ratio with the proportion perturbed: G : H :: M : N (Step 3) and H : L :: K : M (Step 4). By 5.21, if G is greater than L then K is greater than N; if G equals L then K equals N; and if G is less than L then K is less than N.

**Step 6.** That is, for any positive integers m and n: if mA > nC then mD > nF; if mA = nC then mD = nF; if mA < nC then mD < nF.

**Step 7.** Since this holds for all equimultiples mA, mD of A, D and all equimultiples nC, nF of C, F, by the definition of proportion (D5.5), A : C :: D : F. This is the ratio ex aequali, which is what was to be proved.

**USED:** 5.11, 5.15, 5.21, 5.4, D5.17, D5.18, D5.5
**Human refs (from References field):** 5.11, 5.15, 5.16, 5.21
**Jaccard:** 0.375 — AI adds ['5.4', 'D5.17', 'D5.18', 'D5.5']; Human adds ['5.16']

## Proposition 5.24
**Statement:** If a first magnitude have to a second the same ratio as a third has to a fourth, and also a fifth have to the second the same ratio as a sixth to the fourth, the first and fifth added together will have to the second the same ratio as the third and sixth have to the fourth.

**Step 1.** Let A, B, C, D, E, F be magnitudes such that A:B = C:D and E:B = F:D. We wish to show that (A+E):B = (C+F):D.

**Step 2.** By D5.5, it suffices to show that for any equimultiples m(A+E), m(C+F) of (A+E) and (C+F), and any equimultiples nB, nD of B and D, we have m(A+E) >, =, or < nB according as m(C+F) >, =, or < nD.

**Step 3.** By D5.2 (the definition of equimultiples), m(A+E) = mA + mE and m(C+F) = mC + mF, since taking a sum m times yields the sum of each part taken m times.

**Step 4.** Since A:B = C:D, by 5.4, mA:nB = mC:nD. Therefore by D5.5, mA >, =, or < nB according as mC >, =, or < nD.

**Step 5.** Since E:B = F:D, by 5.4, mE:nB = mF:nD. Therefore by D5.5, mE >, =, or < nB according as mF >, =, or < nD.

**Step 6.** (Case A: mA is not less than nB.) If mA >= nB, then by Step 4, mC >= nD. Since mE is a positive magnitude, mA + mE > mA by CN5, so mA + mE > nB. Similarly, since mF is a positive magnitude, mC + mF > mC >= nD, so mC + mF > nD. Thus both m(A+E) > nB and m(C+F) > nD.

**Step 7.** (Case B: mA < nB but mE is not less than nB.) If mA < nB and mE >= nB, then by Step 5, mF >= nD. Since mA is a positive magnitude, mA + mE > mE >= nB by CN5, so mA + mE > nB. Similarly, mC + mF > mF >= nD, so mC + mF > nD. Thus both m(A+E) > nB and m(C+F) > nD.

**Step 8.** (Case C: mA < nB and mE < nB.) By Step 4, mC < nD. By Step 5, mF < nD. Since mA < nB, let P be the excess of nB over mA, so that mA + P = nB. Since mC < nD, let Q be the excess of nD over mC, so that mC + Q = nD.

**Step 9.** From Step 4, mA:nB = mC:nD. By 5.16 (alternando), mA:mC = nB:nD.

**Step 10.** Since nB:nD = mA:mC and mA is a part of nB (as mA < nB) and mC is the corresponding part of nD (as mC < nD), by 5.19 the remainder is to the remainder as the whole to the whole. That is, (nB - mA):(nD - mC) = nB:nD, which gives P:Q = nB:nD.

**Step 11.** From Step 5, mE:nB = mF:nD. By 5.16 (alternando), mE:mF = nB:nD.

**Step 12.** From Steps 10 and 11, we have P:Q = nB:nD and mE:mF = nB:nD. By 5.11 (ratios equal to the same ratio are equal to one another), mE:mF = P:Q.

**Step 13.** From mE:mF = P:Q, by 5.16 (alternando), mE:P = mF:Q.

**Step 14.** Since mE:P = mF:Q, by D5.5 (taking the trivial equimultiples with multiplier 1), mE >, =, or < P according as mF >, =, or < Q.

**Step 15.** But mE > P means mA + mE > mA + P = nB, i.e., m(A+E) > nB. And mF > Q means mC + mF > mC + Q = nD, i.e., m(C+F) > nD. Likewise, mE = P gives m(A+E) = nB and mF = Q gives m(C+F) = nD. And mE < P gives m(A+E) < nB while mF < Q gives m(C+F) < nD.

**Step 16.** Therefore in Case C, m(A+E) >, =, or < nB according as m(C+F) >, =, or < nD.

**Step 17.** Combining Cases A, B, and C (Steps 6, 7, and 16), for all equimultiples m(A+E), m(C+F) and all equimultiples nB, nD, we have m(A+E) >, =, or < nB according as m(C+F) >, =, or < nD.

**Step 18.** Therefore by D5.5, (A+E):B = (C+F):D. Q.E.D.

**USED:** 5.11, 5.16, 5.19, 5.4, CN5, D5.2, D5.5
**Human refs (from References field):** 5.18, 5.22
**Jaccard:** 0.000 — AI adds ['5.11', '5.16', '5.19', '5.4', 'CN5', 'D5.2', 'D5.5']; Human adds ['5.18', '5.22']

## Proposition 5.25
**Statement:** If four magnitudes be proportional, the greatest and the least are greater than the remaining two.

**Step 1.** Let A, B, C, D be four magnitudes of the same kind such that A:B :: C:D, with A the greatest and D the least among them. We are to prove that A + D > B + C.

**Step 2.** Since A:B :: C:D, by alternando (5.16), A:C :: B:D.

**Step 3.** Since A is the greatest of the four magnitudes, A > C. Applying 5.14 to the proportion A:C :: B:D, since the first term A is greater than the third term C, the second term B is greater than the fourth term D. That is, B > D.

**Step 4.** Since A:B :: C:D, and C is less than A while D is less than B, the conditions for 5.19 are satisfied. By 5.19, the remainder is to the remainder as whole to whole: (A - C):(B - D) :: A:B.

**Step 5.** Applying alternando (5.16) to the proportion (A - C):(B - D) :: A:B, we obtain (A - C):A :: (B - D):B.

**Step 6.** Since A is the greatest of the four magnitudes, A > B. We now show that A - C > B - D by elimination. Suppose A - C were equal to B - D. Then applying 5.14 to the proportion (A - C):A :: (B - D):B, since the first term equals the third term, the second term A would equal the fourth term B. But A > B, a contradiction. Suppose instead that A - C were less than B - D. Then by 5.14, since the first term is less than the third term, A would be less than B. But A > B, again a contradiction. Therefore A - C > B - D.

**Step 7.** Since A - C > B - D, there exists a magnitude E such that A - C = (B - D) + E. Then A + D = (A - C) + C + D = (B - D) + E + C + D = (B + C) + E. Since A + D is the sum of B + C together with a further magnitude E, by CN5 the whole A + D is greater than the part B + C. Therefore A + D > B + C.

**Step 8.** Hence the greatest A and the least D taken together are greater than the remaining two magnitudes B and C taken together, which is what was to be proved.

**USED:** 5.14, 5.16, 5.19, CN5
**Human refs (from References field):** 5.19
**Jaccard:** 0.250 — AI adds ['5.14', '5.16', 'CN5']
