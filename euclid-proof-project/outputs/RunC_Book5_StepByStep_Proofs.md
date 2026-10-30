# Book 5 of Euclid's Elements — Step-by-Step AI Proofs (Run C)

## Proposition 5.1
**Statement:** If a magnitude be the same multiple of a magnitude that a part subtracted is of a part subtracted, the remainder will also be the same multiple of the remainder that the whole is of the whole.

**Step 1.** Let magnitude AB be the same multiple of magnitude CD that the part subtracted AE is of the part subtracted CF. We must show that the remainder EB is the same multiple of the remainder FD that the whole AB is of the whole CD.

**Step 2.** Since AB is the same multiple of CD that AE is of CF, let this common multiple be m. Then by the definition of multiple (D5.2), AB is composed of m magnitudes each equal to CD, and AE is composed of m magnitudes each equal to CF. Let AB = G_1 + G_2 + ... + G_m where each G_i equals CD, and let AE = H_1 + H_2 + ... + H_m where each H_i equals CF.

**Step 3.** Since CF is a part subtracted from CD, we have CF less than CD, and therefore each H_i is less than the corresponding G_i, since H_i = CF and G_i = CD.

**Step 4.** Now since G_1 = CD and H_1 = CF, and CF is a part of CD, subtracting equals from equals (specifically, subtracting H_1 from G_1), by CN3 the remainder G_1 - H_1 equals CD - CF, which is FD. Likewise G_2 - H_2 = FD, and so on for each pair up to G_m - H_m = FD.

**Step 5.** The remainder EB = AB - AE = (G_1 + G_2 + ... + G_m) - (H_1 + H_2 + ... + H_m). Since each G_i = CD and each H_i = CF, and these are equal magnitudes respectively, subtracting the sum of the H_i from the sum of the G_i yields (G_1 - H_1) + (G_2 - H_2) + ... + (G_m - H_m), by repeated application of CN3 (if equals be subtracted from equals, the remainders are equal) and CN2 (if equals be added to equals, the wholes are equal).

**Step 6.** From Step 4, each difference G_i - H_i equals FD. Therefore EB = FD + FD + ... + FD (taken m times).

**Step 7.** Since EB is composed of m magnitudes each equal to FD, by the definition of multiple (D5.2), EB is the same multiple of FD as m. But m is the same multiple that AB is of CD. Therefore the remainder EB is the same multiple of the remainder FD that the whole AB is of the whole CD.

**Step 8.** Therefore, if a magnitude be the same multiple of a magnitude that a part subtracted is of a part subtracted, the remainder will also be the same multiple of the remainder that the whole is of the whole. Q.E.D.

**USED:** CN2, CN3, D5.1, D5.2
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['CN2', 'CN3', 'D5.1', 'D5.2']

## Proposition 5.2
**Statement:** If a first magnitude be the same multiple of a second that a third is of a fourth, and a fifth also be the same multiple of the second that a sixth is of the fourth, the sum of the first and fifth will also be the same multiple of the second that the sum of the third and sixth is of the fourth.

**Step 1.** Let the first magnitude AB be the same multiple of the second C that the third DE is of the fourth F. And let the fifth BG be the same multiple of the second C that the sixth EH is of the fourth F. We must show that the sum AG (= AB + BG) is the same multiple of C that the sum DH (= DE + EH) is of F.

**Step 2.** Since AB is the same multiple of C that DE is of F, there are as many magnitudes equal to C in AB as there are magnitudes equal to F in DE [D5.2]. Likewise, since BG is the same multiple of C that EH is of F, there are as many magnitudes equal to C in BG as there are magnitudes equal to F in EH [D5.2].

**Step 3.** Let AB be divided into magnitudes equal to C, say AK, KL, LB, each equal to C. Then DE is divided into the same number of magnitudes equal to F, say DM, MN, NE, each equal to F, where the number of parts is the same [D5.2].

**Step 4.** Similarly, let BG be divided into magnitudes equal to C, say BP, PQ, QG, each equal to C. Then EH is divided into the same number of magnitudes equal to F, say ER, RS, SH, each equal to F [D5.2].

**Step 5.** Then the total number of magnitudes equal to C in AG (the whole of AB and BG together) equals the number in AB plus the number in BG. Likewise, the total number of magnitudes equal to F in DH (the whole of DE and EH together) equals the number in DE plus the number in EH [CN2].

**Step 6.** Since the number of parts equal to C in AB equals the number of parts equal to F in DE, and the number of parts equal to C in BG equals the number of parts equal to F in EH, the total number of parts equal to C in AG equals the total number of parts equal to F in DH.

**Step 7.** Therefore AG is the same multiple of C that DH is of F [D5.2]. That is, the sum of the first and fifth is the same multiple of the second that the sum of the third and sixth is of the fourth, which is what was to be proved.

**USED:** CN2, D5.2
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['CN2', 'D5.2']

## Proposition 5.3
**Statement:** If a first magnitude be the same multiple of a second that a third is of a fourth, and if equimultiples be taken of the first and third, then also ex aequali the magnitudes taken will be equimultiples respectively, the one of the second and the other of the fourth.

**Step 1.** Let A be the same multiple of B that C is of D, so that A = m*B and C = m*D for some multiplicity m [D5.2]. Let equimultiples be taken of A and C; that is, let E = n*A and F = n*C for some multiplicity n [D5.2]. We must show that E is the same multiple of B that F is of D.

**Step 2.** Since A = m*B, by the definition of multiple [D5.2], A is composed of m magnitudes each equal to B. Similarly, since C = m*D, C is composed of m magnitudes each equal to D. Thus A is the same multiple of B that C is of D.

**Step 3.** Now E = n*A means E is the sum of n magnitudes each equal to A. Write these as A_1, A_2, ..., A_n, where each A_i = A = m*B. Similarly F = n*C is the sum of n magnitudes each equal to C, written as C_1, C_2, ..., C_n, where each C_i = C = m*D.

**Step 4.** Since A_1 = m*B and C_1 = m*D, the first magnitude A_1 is the same multiple of B that C_1 is of D. Likewise A_2 = m*B and C_2 = m*D.

**Step 5.** By Proposition 5.2, since A_1 is the same multiple of B that C_1 is of D, and A_2 is the same multiple of B that C_2 is of D, the sum A_1 + A_2 is the same multiple of B that C_1 + C_2 is of D.

**Step 6.** But A_1 + A_2 = 2*A and C_1 + C_2 = 2*C. Also A_3 = m*B is the same multiple of B that C_3 = m*D is of D. By Proposition 5.2 again, the sum A_1 + A_2 + A_3 is the same multiple of B that C_1 + C_2 + C_3 is of D.

**Step 7.** Proceeding in this manner, at each stage the accumulated sum of k copies of A is the same multiple of B that the accumulated sum of k copies of C is of D, and by applying Proposition 5.2 with the next pair A_{k+1} = m*B and C_{k+1} = m*D, we obtain that the sum of k+1 copies of A is the same multiple of B that the sum of k+1 copies of C is of D.

**Step 8.** After n such applications, we conclude that A_1 + A_2 + ... + A_n is the same multiple of B that C_1 + C_2 + ... + C_n is of D. That is, n*A is the same multiple of B that n*C is of D [D5.2].

**Step 9.** Therefore E = n*A is the same multiple of B that F = n*C is of D, which is what was to be proved.

**USED:** 5.2, D5.2
**Human refs (from References field):** 5.2
**Jaccard:** 0.500 — AI adds ['D5.2']

## Proposition 5.4
**Statement:** If a first magnitude have to a second the same ratio as a third to a fourth, any equimultiples whatever of the first and third will also have the same ratio to any equimultiples whatever of the second and fourth respectively, taken in corresponding order.

**Step 1.** Let A, B, C, D be magnitudes such that A:B :: C:D. Let E and F be any equimultiples whatever of A and C respectively, so that E = mA and F = mC for some multiplier m. Let G and H be any equimultiples whatever of B and D respectively, so that G = nB and H = nD for some multiplier n. We must show that E:G :: F:H.

**Step 2.** By Definition D5.5, to prove that E:G :: F:H, we must show that for any equimultiples whatever K, L of E, F and any equimultiples whatever M, N of G, H, the former equimultiples alike exceed, are alike equal to, or alike fall short of the latter equimultiples taken in corresponding order.

**Step 3.** Take arbitrary equimultiples K and L of E and F respectively, so that K = pE and L = pF for some multiplier p. Take arbitrary equimultiples M and N of G and H respectively, so that M = qG and N = qH for some multiplier q.

**Step 4.** Since K = pE = p(mA), K is the p-multiple of the m-multiple of A. By Proposition 5.3, since E is the m-multiple of A and K is the p-multiple of E, K is the (pm)-multiple of A. Likewise, since L = pF = p(mC), and F is the m-multiple of C, by Proposition 5.3, L is the (pm)-multiple of C. Therefore K and L are equimultiples of A and C.

**Step 5.** Since M = qG = q(nB), M is the q-multiple of the n-multiple of B. By Proposition 5.3, since G is the n-multiple of B and M is the q-multiple of G, M is the (qn)-multiple of B. Likewise, since N = qH = q(nD), and H is the n-multiple of D, by Proposition 5.3, N is the (qn)-multiple of D. Therefore M and N are equimultiples of B and D.

**Step 6.** Now K and L are equimultiples of A and C (Step 4), and M and N are equimultiples of B and D (Step 5). Since A:B :: C:D by hypothesis, it follows by Definition D5.5 that: if K exceeds M then L also exceeds N, if K equals M then L also equals N, and if K falls short of M then L also falls short of N.

**Step 7.** Since K and L were taken as arbitrary equimultiples of E and F, and M and N were taken as arbitrary equimultiples of G and H, and the three cases of exceeding, equaling, or falling short hold in corresponding order (Step 6), it follows by Definition D5.5 that E:G :: F:H.

**Step 8.** That is, the equimultiples E and F of A and C have the same ratio to the equimultiples G and H of B and D respectively, taken in corresponding order. This is what was to be proved.

**USED:** 5.3, D5.5
**Human refs (from References field):** 5.3, D5.5
**Jaccard:** 1.000 — Perfect match.

## Proposition 5.5
**Statement:** If a magnitude be the same multiple of a magnitude that a part subtracted is of a part subtracted, the remainder will also be the same multiple of the remainder that the whole is of the whole.

**Step 1.** Let magnitude AB be the same multiple of magnitude CD that the part AE subtracted is of the part CF subtracted. We must show that the remainder EB is the same multiple of the remainder FD that the whole AB is of the whole CD.

**Step 2.** Since AB = n * CD, the magnitude AB is composed of n parts each equal to CD. Likewise, since AE = n * CF, the magnitude AE is composed of n parts each equal to CF. Here n denotes the common multiplicity, following the definition of multiple (D5.2).

**Step 3.** Since CD = CF + FD, each of the n copies of CD may be decomposed into a copy of CF and a copy of FD. Thus the n copies of CF together with the n copies of FD equal the n copies of CD. That is, n * CF + n * FD = n * CD, by Proposition 5.1, which states that if magnitudes are respectively equimultiples, the sum of the multiples is the same multiple of the sum.

**Step 4.** But n * CD = AB (given), and n * CF = AE (given). Substituting, we obtain AE + n * FD = AB.

**Step 5.** Since E lies between A and B, we also have AB = AE + EB. Therefore AE + n * FD = AE + EB (CN1).

**Step 6.** Subtracting the equal magnitude AE from both sides, we conclude that EB = n * FD (CN3).

**Step 7.** Thus the remainder EB is the same multiple of the remainder FD that the whole AB is of the whole CD, which is what was to be proved.

**USED:** 5.1, CN1, CN3, D5.1, D5.2
**Human refs (from References field):** 5.1
**Jaccard:** 0.200 — AI adds ['CN1', 'CN3', 'D5.1', 'D5.2']

## Proposition 5.6
**Statement:** If two magnitudes be equimultiples of two magnitudes, and any magnitudes subtracted from them be equimultiples of the same, the remainders also are either equal to the same or equimultiples of them.

**Step 1.** Let AB and DE be equimultiples of two magnitudes C and F respectively, so that AB = mC and DE = mF for some multiplier m (by D5.2, definition of multiple/equimultiple).

**Step 2.** Let AG be subtracted from AB and DH be subtracted from DE, where AG and DH are equimultiples of C and F respectively, so that AG = nC and DH = nF for some multiplier n with n < m (by D5.2).

**Step 3.** Let GB be the remainder AB - AG, and let HE be the remainder DE - DH. We must show that GB and HE are either equal to C and F, or are equimultiples of C and F.

**Step 4.** Since n < m, the difference m - n is at least 1. Consider the magnitude (m - n)C. If m - n = 1, then (m - n)C = C. If m - n > 1, then (m - n)C is a (m - n)-multiple of C (by D5.2).

**Step 5.** Now, AG = nC is an n-multiple of C, and (m - n)C is a (m - n)-multiple of C. By 5.2, the sum of two equimultiples of the same magnitude is also an equimultiple: nC + (m - n)C = (n + (m - n))C = mC.

**Step 6.** But AB = mC. Therefore AG + (m - n)C = nC + (m - n)C = mC = AB.

**Step 7.** Also, AG + GB = AB, since GB is the remainder when AG is subtracted from AB.

**Step 8.** From Steps 6 and 7, AG + (m - n)C = AG + GB. Since AG = nC is equal in both sums, subtracting the equal magnitude AG from both equal wholes, the remainders are equal (by CN3). Therefore GB = (m - n)C.

**Step 9.** By the same reasoning applied to DE and DH: DH = nF is an n-multiple of F, and (m - n)F is a (m - n)-multiple of F. By 5.2, nF + (m - n)F = mF = DE.

**Step 10.** Also, DH + HE = DE. Therefore DH + (m - n)F = DH + HE. Subtracting the equal magnitude DH from both equal wholes, the remainders are equal (by CN3). Therefore HE = (m - n)F.

**Step 11.** Now, if m - n = 1, then GB = C and HE = F, so the remainders are equal to C and F respectively.

**Step 12.** If m - n > 1, then GB = (m - n)C and HE = (m - n)F, so the remainders are equimultiples of C and F with the same multiplier m - n (by D5.2).

**Step 13.** Therefore, in either case, the remainders GB and HE are either equal to C and F, or are equimultiples of them. Q.E.D.

**USED:** 5.2, CN3, D5.2
**Human refs (from References field):** 5.2
**Jaccard:** 0.333 — AI adds ['CN3', 'D5.2']

## Proposition 5.7
**Statement:** Equal magnitudes have to the same the same ratio, as also has the same to equal magnitudes.

**Step 1.** Let A and B be equal magnitudes, and let C be any magnitude of the same kind. We are to prove two things: (i) A:C = B:C, and (ii) C:A = C:B.

**Step 2.** Proof of Part (i): A:C = B:C. Take any positive integer m and any positive integer n. Form the equimultiples mA and mB of A and B respectively, and form the equimultiple nC of C. Since A = B, by repeatedly applying CN2 (if equals be added to equals, the wholes are equal) — adding A to itself m times yields the same result as adding B to itself m times — we conclude that mA = mB.

**Step 3.** Since mA = mB (by Step 2), whenever mA exceeds nC then mB also exceeds nC; whenever mA equals nC then mB also equals nC; and whenever mA falls short of nC then mB also falls short of nC. This holds because equal magnitudes bear the same relation of excess, equality, or deficiency to any given magnitude, by CN1.

**Step 4.** Since the equimultiples mA and mB of the first and third magnitudes alike exceed, are alike equal to, or alike fall short of the equimultiple nC of the second and fourth magnitudes, for any m and n whatsoever, it follows by D5.5 that A:C = B:C. This completes Part (i).

**Step 5.** Proof of Part (ii): C:A = C:B. Again take any positive integers m and n. Form the equimultiple nC of C (taken as both the first and third magnitudes) and form the equimultiples mA and mB of A and B respectively. Since A = B, we have mA = mB by the same reasoning as in Step 2 (CN2 applied repeatedly).

**Step 6.** Since mA = mB, whenever nC exceeds mA then nC also exceeds mB; whenever nC equals mA then nC also equals mB; and whenever nC falls short of mA then nC also falls short of mB. This again follows because replacing one of two equal magnitudes by the other preserves every relation of order, by CN1.

**Step 7.** Since the equimultiples nC and nC of the first and third magnitudes alike exceed, are alike equal to, or alike fall short of the equimultiples mA and mB of the second and fourth magnitudes, for any m and n whatsoever, it follows by D5.5 that C:A = C:B. This completes Part (ii).

**Step 8.** Therefore equal magnitudes have to the same the same ratio, and the same has to equal magnitudes the same ratio. Q.E.D.

**USED:** CN1, CN2, D5.2, D5.5
**Human refs (from References field):** D5.5
**Jaccard:** 0.250 — AI adds ['CN1', 'CN2', 'D5.2']

## Proposition 5.8
**Statement:** Of unequal magnitudes, the greater has to the same a greater ratio than the less has; and the same has to the less a greater ratio than it has to the greater.

**Step 1.** Let A and C be magnitudes of the same kind with A greater than C, and let B be any magnitude of the same kind. We must show two things: (i) A has to B a greater ratio than C has to B, and (ii) B has to C a greater ratio than B has to A.

**Step 2.** Since A is greater than C, the excess A minus C is itself a magnitude. Denote this excess by E, so that A equals C together with E, and E is a magnitude. Since E and B are magnitudes of the same kind, they are capable, when multiplied, of exceeding one another [D5.4]. Therefore there exists a positive integer m such that mE is greater than B.

**Step 3.** Since A equals C together with E, the magnitude mA equals mC together with mE. More precisely, mA is the same multiple of A that mC is of C and mE is of E, and since A equals C together with E, we have mA equals mC together with mE [5.1 applied to the whole A and the part C subtracted, giving remainder E: the m-multiple of the whole minus the m-multiple of the part equals the m-multiple of the remainder]. Thus mA minus mC equals mE, and since mE is greater than B, we conclude mA is greater than mC together with B.

**Step 4.** Now consider the sequence of multiples B, 2B, 3B, and so on. Since mC and B are magnitudes of the same kind, by the Archimedean property [D5.4] some multiple of B exceeds mC. Let n be the least positive integer such that nB is greater than or equal to mC. Such an n exists because multiples of B eventually exceed mC. By the minimality of n, we have (n minus 1) times B is less than mC, so nB, which equals (n minus 1) times B together with B, is less than mC together with B.

**Step 5.** From Step 3, mA is greater than mC together with B. From Step 4, nB is less than mC together with B. Therefore mA is greater than nB. Also by the choice of n, nB is greater than or equal to mC, which means mC is not greater than nB.

**Step 6.** We have produced equimultiples mA and mC of A and C, and an equimultiple nB of B (serving as equimultiple of both the second and fourth magnitudes, since the second and fourth are the same magnitude B), such that mA exceeds nB but mC does not exceed nB. By the definition of greater ratio [D5.7], A has to B a greater ratio than C has to B. This establishes Part (i).

**Step 7.** For Part (ii), we must show B has to C a greater ratio than B has to A. By D5.7, we need equimultiples of the first and third (here both are B, so we take the same multiple of B for both) and equimultiples of the second and fourth (here mC and mA for some multiplier m) such that the multiple of B exceeds mC but does not exceed mA.

**Step 8.** Using the same m from Step 2, consider two cases. Case 1: nB is strictly greater than mC. Then from Step 5, nB is greater than mC, and mA is greater than nB, so nB does not exceed mA. Taking equimultiples nB and nB of the first and third, and equimultiples mC and mA of the second and fourth, D5.7 gives B to C a greater ratio than B to A.

**Step 9.** Case 2: nB equals mC exactly. Then nB is not strictly greater than mC, so we consider (n plus 1) times B instead. We have (n plus 1) times B equals nB together with B, which equals mC together with B. From Step 3, mA is greater than mC together with B, so mA is greater than (n plus 1) times B, meaning (n plus 1) times B does not exceed mA. Also (n plus 1) times B equals mC together with B, and since B is a magnitude, mC together with B is greater than mC [CN5], so (n plus 1) times B is greater than mC. Taking the equimultiple (n plus 1) times B for both first and third magnitudes, and equimultiples mC and mA for second and fourth, D5.7 gives B to C a greater ratio than B to A.

**Step 10.** In both cases, B has to C a greater ratio than B has to A. This establishes Part (ii).

**Step 11.** Therefore, of unequal magnitudes, the greater has to the same a greater ratio than the less has; and the same has to the less a greater ratio than it has to the greater. Q.E.D.

**USED:** 5.1, CN5, D5.4, D5.7
**Human refs (from References field):** 5.1, D5.4, D5.7
**Jaccard:** 0.750 — AI adds ['CN5']

## Proposition 5.9
**Statement:** Magnitudes which have the same ratio to the same are equal to one another; and magnitudes to which the same has the same ratio are equal.

**Step 1.** Let A and B be magnitudes which have the same ratio to a magnitude C, so that A:C = B:C. We claim that A = B.

**Step 2.** Suppose for contradiction that A is not equal to B. Then one of them is greater than the other. Assume without loss of generality that A > B.

**Step 3.** Since A > B, by Proposition 5.8 (of unequal magnitudes, the greater has to the same a greater ratio than the less has), A:C > B:C.

**Step 4.** But this contradicts the hypothesis that A:C = B:C. The assumption that A > B is therefore false. By the same argument, B > A also leads to a contradiction (since then B:C > A:C, again contradicting A:C = B:C). Therefore A = B.

**Step 5.** Now let C be a magnitude which has the same ratio to magnitudes A and B, so that C:A = C:B. We claim that A = B.

**Step 6.** Suppose for contradiction that A is not equal to B. Assume without loss of generality that A > B, so that B is less than A.

**Step 7.** Since A > B, by Proposition 5.8 (the same has to the less a greater ratio than it has to the greater), C:B > C:A.

**Step 8.** But this contradicts the hypothesis that C:A = C:B. The assumption that A > B is therefore false. By the same argument, B > A also leads to a contradiction (since then C:A > C:B, again contradicting C:A = C:B). Therefore A = B.

**Step 9.** Hence magnitudes which have the same ratio to the same are equal to one another, and magnitudes to which the same has the same ratio are equal. Q.E.D.

**USED:** 5.8
**Human refs (from References field):** 5.8
**Jaccard:** 1.000 — Perfect match.

## Proposition 5.10
**Statement:** Of magnitudes which have a ratio to the same, that which has a greater ratio is greater; and that to which the same has a greater ratio is less.

**Step 1.** Let A and B be magnitudes each having a ratio to the same magnitude C. Suppose first that A has a greater ratio to C than B has to C, that is, A : C > B : C in the sense of D5.7. We claim that A > B.

**Step 2.** There are three exhaustive possibilities: A = B, A < B, or A > B.

**Step 3.** Suppose A = B. Then by 5.7, since equal magnitudes have to the same magnitude the same ratio, we would have A : C = B : C. But this contradicts the hypothesis that A : C > B : C. Therefore A is not equal to B.

**Step 4.** Suppose A < B. Then since A and B are unequal magnitudes having a ratio to C, by 5.8 the greater has to the same a greater ratio than the less has, so B : C > A : C, which means A : C < B : C. But this contradicts the hypothesis that A : C > B : C. Therefore A is not less than B.

**Step 5.** Since A is neither equal to B nor less than B, it follows that A > B. This concludes the first part.

**Step 6.** Now suppose that C has a greater ratio to A than C has to B, that is, C : A > C : B. We claim that A < B.

**Step 7.** Again there are three exhaustive possibilities: A = B, A > B, or A < B.

**Step 8.** Suppose A = B. Then by 5.7, since the same magnitude has to equal magnitudes the same ratio, we would have C : A = C : B. But this contradicts the hypothesis that C : A > C : B. Therefore A is not equal to B.

**Step 9.** Suppose A > B. Then since A and B are unequal and C has a ratio to both, by 5.8 the same has to the less a greater ratio than it has to the greater, so C : B > C : A, which means C : A < C : B. But this contradicts the hypothesis that C : A > C : B. Therefore A is not greater than B.

**Step 10.** Since A is neither equal to B nor greater than B, it follows that A < B. This concludes the second part.

**Step 11.** Therefore, of magnitudes which have a ratio to the same, that which has a greater ratio is greater; and that to which the same has a greater ratio is less. Q.E.D.

**USED:** 5.7, 5.8, D5.7
**Human refs (from References field):** 5.7, 5.8
**Jaccard:** 0.667 — AI adds ['D5.7']

## Proposition 5.11
**Statement:** Ratios which are the same with the same ratio are also the same with one another.

**Step 1.** Let A, B, C, D, E, F be magnitudes such that A:B :: C:D and C:D :: E:F. We aim to show that A:B :: E:F.

**Step 2.** Take any equimultiples mA, mC, mE of A, C, E respectively, and any equimultiples nB, nD, nF of B, D, F respectively, where m and n are arbitrary positive integers.

**Step 3.** Since A:B :: C:D, by Definition 5.5 the equimultiples mA of the first and mC of the third, and nB of the second and nD of the fourth, satisfy: if mA exceeds nB then mC exceeds nD, if mA equals nB then mC equals nD, and if mA falls short of nB then mC falls short of nD.

**Step 4.** Since C:D :: E:F, by Definition 5.5 the equimultiples mC of the first and mE of the third, and nD of the second and nF of the fourth, satisfy: if mC exceeds nD then mE exceeds nF, if mC equals nD then mE equals nF, and if mC falls short of nD then mE falls short of nF.

**Step 5.** Now consider any such equimultiples mA and nB. If mA exceeds nB, then by Step 3, mC exceeds nD, and then by Step 4, mE exceeds nF. If mA equals nB, then by Step 3, mC equals nD, and then by Step 4, mE equals nF. If mA falls short of nB, then by Step 3, mC falls short of nD, and then by Step 4, mE falls short of nF.

**Step 6.** Since this holds for any equimultiples whatever mA, mE of A, E and any equimultiples whatever nB, nF of B, F — namely that mA and mE alike exceed, are alike equal to, or alike fall short of nB and nF respectively — it follows by Definition 5.5 that A:B :: E:F.

**Step 7.** Therefore ratios which are the same with the same ratio are also the same with one another. Q.E.D.

**USED:** D5.5
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['D5.5']

## Proposition 5.12
**Statement:** If any number of magnitudes be proportional, as one of the antecedents is to one of the consequents, so will all the antecedents be to all the consequents.

**Step 1.** Let any number of magnitudes A1, A2, ..., An and B1, B2, ..., Bn be proportional, so that A1:B1 = A2:B2 = ... = An:Bn. We must show that A1:B1 = (A1 + A2 + ... + An):(B1 + B2 + ... + Bn).

**Step 2.** Take arbitrary equimultiples: let m*A1 and m*(A1 + A2 + ... + An) be equimultiples of A1 and (A1 + A2 + ... + An), and let n*B1 and n*(B1 + B2 + ... + Bn) be equimultiples of B1 and (B1 + B2 + ... + Bn), for any positive integers m and n.

**Step 3.** Since m*(A1 + A2 + ... + An) = m*A1 + m*A2 + ... + m*An, the multiple of a sum equals the sum of the equimultiples. Likewise n*(B1 + B2 + ... + Bn) = n*B1 + n*B2 + ... + n*Bn. This follows from the distributive property of equimultiples, established by repeated application of 5.1 (equimultiple subtraction/addition structure).

**Step 4.** Now, since A1:B1 = A2:B2, by Definition 5.5, for any equimultiples m*A1, m*A2 of A1, A2 and any equimultiples n*B1, n*B2 of B1, B2: if m*A1 > n*B1 then m*A2 > n*B2, if m*A1 = n*B1 then m*A2 = n*B2, and if m*A1 < n*B1 then m*A2 < n*B2. The same holds for each pair A1:B1 = Ak:Bk, so that m*A1 and n*B1 always compare the same way as m*Ak and n*Bk, for every k.

**Step 5.** Suppose m*A1 > n*B1. Then by Step 4, m*A2 > n*B2, m*A3 > n*B3, ..., m*An > n*Bn. Since each m*Ak > n*Bk, adding these inequalities gives m*A1 + m*A2 + ... + m*An > n*B1 + n*B2 + ... + n*Bn, that is, m*(A1 + A2 + ... + An) > n*(B1 + B2 + ... + Bn). This addition of inequalities follows from repeated application of Common Notion 5 and the ordering of magnitudes.

**Step 6.** Suppose m*A1 = n*B1. Then by Step 4, m*A2 = n*B2, m*A3 = n*B3, ..., m*An = n*Bn. Adding equals to equals repeatedly by CN2 gives m*A1 + m*A2 + ... + m*An = n*B1 + n*B2 + ... + n*Bn, that is, m*(A1 + A2 + ... + An) = n*(B1 + B2 + ... + Bn).

**Step 7.** Suppose m*A1 < n*B1. Then by Step 4, m*A2 < n*B2, m*A3 < n*B3, ..., m*An < n*Bn. By reasoning symmetric to Step 5, adding these inequalities gives m*(A1 + A2 + ... + An) < n*(B1 + B2 + ... + Bn).

**Step 8.** We have shown that for arbitrary positive integers m and n: m*A1 exceeds, equals, or falls short of n*B1 according as m*(A1 + A2 + ... + An) exceeds, equals, or falls short of n*(B1 + B2 + ... + Bn). Therefore, by Definition 5.5, A1:B1 = (A1 + A2 + ... + An):(B1 + B2 + ... + Bn).

**Step 9.** Thus, if any number of magnitudes be proportional, as one of the antecedents is to one of the consequents, so will all the antecedents be to all the consequents. Q.E.D.

**USED:** 5.1, CN2, D5.1, D5.2, D5.3, D5.4, D5.5
**Human refs (from References field):** 5.1, D5.5
**Jaccard:** 0.286 — AI adds ['CN2', 'D5.1', 'D5.2', 'D5.3', 'D5.4']

## Proposition 5.13
**Statement:** If a first magnitude have to a second the same ratio as a third to a fourth, and the third have to the fourth a greater ratio than a fifth has to a sixth, the first will also have to the second a greater ratio than the fifth to the sixth.

**Step 1.** Let A, B, C, D, E, F be magnitudes such that A:B :: C:D, and C:D > E:F. We wish to show that A:B > E:F.

**Step 2.** Since C has to D a greater ratio than E has to F, by Definition 5.7 there exist equimultiples mC and mE of C and E, and equimultiples nD and nF of D and F, such that mC > nD but mE is not greater than nF (that is, mE <= nF).

**Step 3.** Now consider the same multipliers m and n applied to A, B respectively, yielding equimultiples mA of A and nB of B. Since A:B :: C:D, by Definition 5.5 (the definition of same ratio), for any equimultiples whatever of the first and third (here mA and mC) and any equimultiples whatever of the second and fourth (here nB and nD), if mC > nD then mA > nB.

**Step 4.** From Step 2 we have mC > nD. Therefore by Step 3, mA > nB.

**Step 5.** We now have equimultiples mA and mE of A and E, and equimultiples nB and nF of B and F, such that mA > nB (from Step 4) while mE is not greater than nF (from Step 2). By Definition 5.7, this means that A has to B a greater ratio than E has to F, that is, A:B > E:F.

**Step 6.** Therefore, if a first magnitude has to a second the same ratio as a third to a fourth, and the third has to the fourth a greater ratio than a fifth has to a sixth, the first will also have to the second a greater ratio than the fifth to the sixth. Q.E.D.

**USED:** D5.5, D5.7
**Human refs (from References field):** D5.5, D5.7
**Jaccard:** 1.000 — Perfect match.

## Proposition 5.14
**Statement:** If a first magnitude have to a second the same ratio as a third has to a fourth, and the first be greater than the third, the second will also be greater than the fourth; if equal, equal; and if less, less.

**Step 1.** Let A, B, C, D be magnitudes such that A : B = C : D (D5.5). We must show: if A > C then B > D; if A = C then B = D; if A < C then B < D.

**Step 2.** Case 1: Suppose A > C. Since A and C are unequal magnitudes both having a ratio to B, and A is the greater, by 5.8 (the greater has to the same a greater ratio than the less has), A : B > C : B.

**Step 3.** By hypothesis, A : B = C : D. By the symmetry of the definition of same ratio (D5.5), C : D = A : B. By 5.13 (if a first magnitude have to a second the same ratio as a third to a fourth, and the third have to the fourth a greater ratio than a fifth has to a sixth, the first will also have to the second a greater ratio than the fifth to the sixth), since C : D = A : B and A : B > C : B, we conclude C : D > C : B.

**Step 4.** By 5.10 (that to which the same has a greater ratio is less), since C has a greater ratio to D than it has to B, we have D < B, that is, B > D.

**Step 5.** Case 2: Suppose A = C. By 5.7 (equal magnitudes have to the same the same ratio), since A = C and both have a ratio to B, we have A : B = C : B.

**Step 6.** By hypothesis, A : B = C : D. By 5.11 (ratios which are the same with the same ratio are also the same with one another), since C : B = A : B (from Step 5) and A : B = C : D (given), we conclude C : B = C : D.

**Step 7.** By 5.9 (magnitudes to which the same has the same ratio are equal), since C : B = C : D, we have B = D.

**Step 8.** Case 3: Suppose A < C. Then C > A. By 5.8, since C is greater than A and both have a ratio to B, C : B > A : B.

**Step 9.** By hypothesis, A : B = C : D. By 5.13, since A : B = C : D and C : B > A : B, we conclude C : B > C : D.

**Step 10.** By 5.10, since C has a greater ratio to B than it has to D, we have B < D.

**Step 11.** Therefore, in all three cases: if A > C then B > D; if A = C then B = D; if A < C then B < D. Q.E.D.

**USED:** 5.10, 5.11, 5.13, 5.7, 5.8, 5.9, D5.5
**Human refs (from References field):** 5.10, 5.13, 5.8
**Jaccard:** 0.429 — AI adds ['5.11', '5.7', '5.9', 'D5.5']

## Proposition 5.15
**Statement:** Parts have the same ratio as the same multiples of them taken in corresponding order.

**Step 1.** Let A and B be any two magnitudes, and let m be any positive integer. Let mA and mB denote the m-th multiples of A and B respectively. We must prove that A : B = mA : mB.

**Step 2.** By Definition 5.5, we must show that for any equimultiples p(A) and p(mA) of A and mA, and any equimultiples q(B) and q(mB) of B and mB, whenever p(A) exceeds, equals, or falls short of q(B), then p(mA) likewise exceeds, equals, or falls short of q(mB).

**Step 3.** Take any positive integers p and q. Form pA and p(mA), which are equimultiples of A and mA respectively. Form qB and q(mB), which are equimultiples of B and mB respectively.

**Step 4.** By Proposition 5.3, since mA is the m-th multiple of A and we take the p-th multiple of mA, we have p(mA) = (pm)A. That is, the p-th multiple of the m-th multiple of A equals the (pm)-th multiple of A. Similarly, q(mB) = (qm)B.

**Step 5.** Now (pm)A is the same as m(pA), since both represent pA taken m times, which by 5.3 (applied with pA as the magnitude and m as the multiplier, noting that pm copies of A can be grouped as m groups of p copies) gives m(pA) = (pm)A. Likewise, (qm)B = m(qB).

**Step 6.** Therefore p(mA) = m(pA) and q(mB) = m(qB), so comparing p(mA) with q(mB) is the same as comparing m(pA) with m(qB).

**Step 7.** Suppose pA > qB. Then pA exceeds qB by some magnitude. Since pA > qB, taking m equimultiples of each, the m-th multiple of pA exceeds the m-th multiple of qB. For pA = qB + R for some remainder R (by the meaning of exceeding), and m(pA) = m(qB) + mR by Common Notion 2 applied (m-1) times, hence m(pA) > m(qB). Thus p(mA) > q(mB).

**Step 8.** Suppose pA = qB. Then taking the same multiple m of each, m(pA) = m(qB) by Common Notion 2 applied repeatedly (equals added to equals remain equal). Thus p(mA) = q(mB).

**Step 9.** Suppose pA < qB. Then by the same reasoning as Step 7 with roles reversed, qB > pA implies m(qB) > m(pA), hence q(mB) > p(mA), which means p(mA) < q(mB).

**Step 10.** We have shown that for arbitrary positive integers p and q: pA exceeds, equals, or falls short of qB if and only if p(mA) exceeds, equals, or falls short of q(mB). Therefore, by Definition 5.5, A : B = mA : mB.

**Step 11.** Since A and B were arbitrary magnitudes and m was an arbitrary positive integer, parts have the same ratio as the same multiples of them taken in corresponding order, which is what was to be proved.

**USED:** 5.3, CN2, D5.2, D5.5
**Human refs (from References field):** 5.12, 5.7
**Jaccard:** 0.000 — AI adds ['5.3', 'CN2', 'D5.2', 'D5.5']; Human adds ['5.12', '5.7']

## Proposition 5.16
**Statement:** If four magnitudes be proportional, they will also be proportional alternately.

**Step 1.** Let A, B, C, D be four magnitudes such that A:B :: C:D, where A and C are magnitudes of the same kind, and B and D are magnitudes of the same kind. We wish to show that they are proportional alternately, that is, A:C :: B:D. [D5.12]

**Step 2.** Take any equimultiples mA and mB of A and B respectively, and take any equimultiples nC and nD of C and D respectively, where m and n are arbitrary positive integers.

**Step 3.** Since mA and mB are equimultiples of A and B, by Proposition 5.15, mA:mB :: A:B. Likewise, since nC and nD are equimultiples of C and D, nC:nD :: C:D. [5.15]

**Step 4.** We are given that A:B :: C:D. Since mA:mB :: A:B and A:B :: C:D, by transitivity of ratios (Proposition 5.11), mA:mB :: C:D. Since C:D :: nC:nD, applying 5.11 again, mA:mB :: nC:nD. [5.11]

**Step 5.** Since mA:mB :: nC:nD, by Proposition 5.14, if mA is greater than nC then mB is greater than nD; if mA is equal to nC then mB is equal to nD; and if mA is less than nC then mB is less than nD. [5.14]

**Step 6.** Now mA and mB are arbitrary equimultiples of A and B, and nC and nD are arbitrary equimultiples of C and D. We have shown that for any such equimultiples, the multiple of the first (mA) and the multiple of the second (nC) compare in the same way as the multiple of the third (mB) and the multiple of the fourth (nD). Therefore, by the definition of proportion (D5.5), A:C :: B:D. [D5.5]

**Step 7.** Therefore, if four magnitudes be proportional, they will also be proportional alternately. Q.E.D.

**USED:** 5.11, 5.14, 5.15, D5.12, D5.5
**Human refs (from References field):** 5.11, 5.14, 5.15, D5.5
**Jaccard:** 0.800 — AI adds ['D5.12']

## Proposition 5.17
**Statement:** If magnitudes be proportional componendo, they will also be proportional separando.

**Step 1.** Let A, B, C, D be magnitudes such that (A + B) : B :: (C + D) : D; that is, they are proportional componendo (D5.14). We are to show that A : B :: C : D, i.e., they are proportional separando (D5.15).

**Step 2.** Take any equimultiples mA and mC of A and C respectively, and any equimultiples nB and nD of B and D respectively, where m and n are arbitrary positive integers.

**Step 3.** Since mA is the same multiple of A that mB is of B (both being m-fold multiples), we have that mA + mB is the same multiple of A + B that mC + mD is of C + D. In other words, m(A + B) = mA + mB and m(C + D) = mC + mD, where m(A + B) and m(C + D) are equimultiples of (A + B) and (C + D) respectively [by 5.1 applied inversely: since the m-fold multiple of the whole (A + B) exceeds the m-fold multiple of the part B by the m-fold multiple of A, we have m(A + B) = mA + mB; similarly for C + D].

**Step 4.** Since mB is the same multiple of B that mD is of D, and nB is the same multiple of B that nD is of D, the sum mB + nB is the same multiple of B that mD + nD is of D [by 5.2]. That is, (m + n)B and (m + n)D are equimultiples of B and D.

**Step 5.** Now m(A + B) and m(C + D) are equimultiples of (A + B) and (C + D), and (m + n)B and (m + n)D are equimultiples of B and D. Since by hypothesis (A + B) : B :: (C + D) : D, the definition of proportion (D5.5) gives us: if m(A + B) > (m + n)B then m(C + D) > (m + n)D; if m(A + B) = (m + n)B then m(C + D) = (m + n)D; if m(A + B) < (m + n)B then m(C + D) < (m + n)D.

**Step 6.** But m(A + B) = mA + mB (Step 3) and (m + n)B = mB + nB (Step 4). Therefore m(A + B) > (m + n)B if and only if mA + mB > mB + nB. Since mB is a common magnitude on both sides, mA + mB > mB + nB if and only if mA > nB [CN3 and CN5: if equals (mB) be subtracted from unequals, the remainders are unequal in the same sense; and conversely by CN2, if equals be added to unequals, the wholes are unequal in the same sense]. By the same reasoning, mA + mB = mB + nB if and only if mA = nB [CN2, CN3], and mA + mB < mB + nB if and only if mA < nB.

**Step 7.** Similarly, m(C + D) = mC + mD and (m + n)D = mD + nD, so m(C + D) > (m + n)D if and only if mC > nD; m(C + D) = (m + n)D if and only if mC = nD; and m(C + D) < (m + n)D if and only if mC < nD [by the same reasoning using CN2, CN3, CN5].

**Step 8.** Combining Steps 5, 6, and 7: if mA > nB then mC > nD; if mA = nB then mC = nD; if mA < nB then mC < nD.

**Step 9.** Since m and n were arbitrary, and the equimultiples mA, mC of A, C and the equimultiples nB, nD of B, D satisfy exactly the conditions of D5.5, we conclude that A : B :: C : D.

**Step 10.** Therefore, if magnitudes be proportional componendo, they will also be proportional separando. Q.E.D.

**USED:** 5.1, 5.2, CN2, CN3, CN5, D5.14, D5.15, D5.5
**Human refs (from References field):** 5.1, 5.2
**Jaccard:** 0.250 — AI adds ['CN2', 'CN3', 'CN5', 'D5.14', 'D5.15', 'D5.5']

## Proposition 5.18
**Statement:** If magnitudes be proportional separando, they will also be proportional componendo.

**Step 1.** Let AE, EB, CF, FD be magnitudes such that they are proportional separando, that is, AE : EB :: CF : FD, where AE is the excess of the first magnitude AB over the second EB, and CF is the excess of the third magnitude CD over the fourth FD. Thus AB = AE + EB and CD = CF + FD, and we must prove the proportion componendo: AB : EB :: CD : FD. [D5.14, D5.15]

**Step 2.** By the definition of proportion (D5.5), the hypothesis AE : EB :: CF : FD means: for any equimultiples m*AE and m*CF of the first and third, and any equimultiples n*EB and n*FD of the second and fourth, if m*AE exceeds n*EB then m*CF exceeds n*FD, if m*AE equals n*EB then m*CF equals n*FD, and if m*AE falls short of n*EB then m*CF falls short of n*FD. [D5.5]

**Step 3.** We must show that for any positive integers m and n, the equimultiples m*AB and m*CD on the one hand, and n*EB and n*FD on the other, satisfy the threefold condition of D5.5. Since AB = AE + EB, we have m*AB = m*AE + m*EB. Similarly, since CD = CF + FD, we have m*CD = m*CF + m*FD. [CN2]

**Step 4.** Consider first the case n > m. Then m*AB > n*EB if and only if m*AE + m*EB > n*EB, which holds if and only if m*AE > (n - m)*EB, since n - m is a positive integer and equals are subtracted from both sides. Likewise m*CD > n*FD if and only if m*CF + m*FD > n*FD, which holds if and only if m*CF > (n - m)*FD. Now (n - m) is a positive integer, so m*AE and m*CF are equimultiples of AE and CF, and (n - m)*EB and (n - m)*FD are equimultiples of EB and FD. By the hypothesis (Step 2), m*AE > (n - m)*EB if and only if m*CF > (n - m)*FD. Therefore m*AB > n*EB if and only if m*CD > n*FD. The same reasoning applies when m*AE equals (n - m)*EB or falls short of it, yielding respectively m*AB = n*EB if and only if m*CD = n*FD, and m*AB < n*EB if and only if m*CD < n*FD. [D5.5, CN3]

**Step 5.** Consider next the case n = m. Then m*AB = m*AE + m*EB, and since AE is a positive magnitude, m*AE is a positive magnitude, so m*AB > m*EB = n*EB. The whole m*AB is greater than the part m*EB. Similarly m*CD = m*CF + m*FD > m*FD = n*FD. Thus both m*AB > n*EB and m*CD > n*FD hold, and the threefold condition is satisfied. [CN5]

**Step 6.** Consider finally the case n < m. Then m*EB > n*EB since m > n, and therefore m*AB = m*AE + m*EB > m*EB > n*EB. Similarly m*CD = m*CF + m*FD > m*FD > n*FD. So both m*AB > n*EB and m*CD > n*FD hold, and the threefold condition is again satisfied. [CN5]

**Step 7.** Since in every case the equimultiples m*AB and m*CD, and the equimultiples n*EB and n*FD, satisfy the threefold condition alike exceed, are alike equal to, or alike fall short of one another respectively, it follows by the definition of same ratio (D5.5) that AB : EB :: CD : FD. That is, the magnitudes are proportional componendo. [D5.5, D5.14]

**USED:** CN2, CN3, CN5, D5.14, D5.15, D5.5
**Human refs (from References field):** 5.11, 5.14, 5.17
**Jaccard:** 0.000 — AI adds ['CN2', 'CN3', 'CN5', 'D5.14', 'D5.15', 'D5.5']; Human adds ['5.11', '5.14', '5.17']

## Proposition 5.19
**Statement:** If, as a whole is to a whole, so is a part subtracted to a part subtracted, the remainder will also be to the remainder as whole to whole.

**Step 1.** Let AB and CD be whole magnitudes, and let AE and CF be parts subtracted from them respectively, so that EB is the remainder of AB after AE is subtracted, and FD is the remainder of CD after CF is subtracted. Suppose AB:CD = AE:CF. We wish to show that EB:FD = AB:CD.

**Step 2.** Since AB:CD = AE:CF, by alternando (5.16) we obtain AB:AE = CD:CF.

**Step 3.** Since AB:AE = CD:CF, and AE is a part of AB (so AB > AE) and CF is a part of CD (so CD > CF), we may apply separando (5.17). This yields (AB - AE):AE = (CD - CF):CF, that is, EB:AE = FD:CF.

**Step 4.** Since EB:AE = FD:CF, by alternando (5.16) we obtain EB:FD = AE:CF.

**Step 5.** Now we have AB:CD = AE:CF (given, Step 1) and EB:FD = AE:CF (Step 4). Since both ratios AB:CD and EB:FD are the same as the ratio AE:CF, by the transitivity of ratios (5.11) we conclude EB:FD = AB:CD.

**Step 6.** Therefore the remainder EB is to the remainder FD as the whole AB is to the whole CD, which is what was to be proved.

**USED:** 5.11, 5.16, 5.17
**Human refs (from References field):** 5.11, 5.16, 5.17
**Jaccard:** 1.000 — Perfect match.

## Proposition 5.20
**Statement:** If there be three magnitudes, and others equal to them in multitude, which taken two and two are in the same ratio, and if ex aequali the first be greater than the third, the fourth will also be greater than the sixth; if equal, equal; and, if less, less.

**Step 1.** Let A, B, C be three magnitudes and D, E, F be three other magnitudes such that A:B = D:E and B:C = E:F. We must show that if A > C then D > F, if A = C then D = F, and if A < C then D < F.

**Step 2.** Note that from B:C = E:F, by the definition of same ratio (D5.5), we may deduce C:B = F:E. For D5.5 states that a:b = c:d holds when for any equimultiples m*a, m*c of the first and third and any equimultiples n*b, n*d of the second and fourth, m*a exceeds, equals, or falls short of n*b according as m*c exceeds, equals, or falls short of n*d. Applying this to B:C = E:F with the roles of antecedent and consequent exchanged (taking equimultiples of C and F, and equimultiples of B and E), we obtain C:B = F:E.

**Step 3.** (Case A > C.) Since A > C and both A and C have a ratio to B, by 5.8 the greater magnitude A has to B a greater ratio than the lesser magnitude C has to B. That is, A:B > C:B.

**Step 4.** Since A:B = D:E (given) and A:B > C:B, by 5.13 we conclude D:E > C:B.

**Step 5.** Since C:B = F:E (from Step 2) and D:E > C:B, by 5.13 we conclude D:E > F:E.

**Step 6.** Since D has to E a greater ratio than F has to E, by 5.10 the magnitude with the greater ratio is greater, so D > F.

**Step 7.** (Case A = C.) Since A = C, by 5.7 equal magnitudes have the same ratio to the same magnitude, so A:B = C:B.

**Step 8.** Since A:B = D:E (given) and A:B = C:B, by 5.11 (ratios equal to the same ratio are equal to one another) D:E = C:B.

**Step 9.** Since C:B = F:E (from Step 2) and D:E = C:B, by 5.11 we conclude D:E = F:E.

**Step 10.** Since D:E = F:E, by 5.9 magnitudes which have the same ratio to the same are equal, so D = F.

**Step 11.** (Case A < C.) Since A < C, by 5.8 the same magnitude B has to the less magnitude A a greater ratio than it has to the greater magnitude C. Equivalently, C has to B a greater ratio than A has to B, that is, C:B > A:B.

**Step 12.** Since A:B = D:E (given), we have C:B > D:E. Since C:B = F:E (from Step 2), we have F:E > D:E.

**Step 13.** Since F has to E a greater ratio than D has to E, by 5.10 the magnitude with the greater ratio is greater, so F > D, which means D < F.

**Step 14.** Therefore, if ex aequali the first magnitude A is greater than the third C, the fourth D is also greater than the sixth F; if A equals C, then D equals F; and if A is less than C, then D is less than F. Q.E.D.

**USED:** 5.10, 5.11, 5.13, 5.7, 5.8, 5.9, D5.5
**Human refs (from References field):** 5.10, 5.13, 5.8
**Jaccard:** 0.429 — AI adds ['5.11', '5.7', '5.9', 'D5.5']

## Proposition 5.21
**Statement:** If there be three magnitudes, and others equal to them in multitude, which taken two and two together are in the same ratio, and the proportion of them be perturbed, then, if ex aequali the first magnitude is greater than the third, the fourth will also be greater than the sixth; if equal, equal; and if less, less.

**Step 1.** Let A, B, C be three magnitudes and D, E, F be three others such that A:B = E:F and B:C = D:E, so that the proportion is perturbed (D5.18). We must show that if A > C then D > F, if A = C then D = F, and if A < C then D < F.

**Step 2.** (Case 1: A > C.) Since A > C, by 5.8, A has to B a greater ratio than C has to B, that is, A:B > C:B.

**Step 3.** By D5.7 (definition of greater ratio), there exist positive integers m and n such that mA > nB while mC does not exceed nB, that is, mC <= nB.

**Step 4.** From mA > nB and the hypothesis A:B = E:F, by D5.5 (definition of same ratio, taking m-multiples of A and E, and n-multiples of B and F), we conclude mE > nF.

**Step 5.** We consider two subcases for mC <= nB. First suppose mC < nB, so that nB > mC. From the hypothesis B:C = D:E, by D5.5 (taking n-multiples of B and D, and m-multiples of C and E), nB > mC implies nD > mE. Combined with mE > nF from Step 4, we get nD > mE > nF, hence nD > nF, and therefore D > F.

**Step 6.** Now suppose mC = nB. From B:C = D:E, by D5.5 (same multipliers as Step 5), nB = mC implies nD = mE. Combined with mE > nF from Step 4, we get nD = mE > nF, hence nD > nF, and therefore D > F. This completes Case 1.

**Step 7.** (Case 2: A = C.) Suppose for contradiction that D is not equal to F. First assume D > F. Since D > F, by 5.8, D:E > F:E.

**Step 8.** By D5.7, there exist positive integers p and q such that pD > qE while pF does not exceed qE, that is, pF <= qE.

**Step 9.** From the hypothesis B:C = D:E, by D5.5 (taking p-multiples of B and D, and q-multiples of C and E), pD > qE implies pB > qC.

**Step 10.** We consider two subcases. First suppose pF < qE. From the hypothesis A:B = E:F, by D5.5 (taking q-multiples of A and E, and p-multiples of B and F), qE > pF implies qA > pB. Combined with pB > qC from Step 9, we get qA > pB > qC, hence qA > qC, so A > C. This contradicts A = C.

**Step 11.** Now suppose pF = qE. From A:B = E:F, by D5.5, qE = pF implies qA = pB. But pB > qC from Step 9, so qA = pB > qC, giving qA > qC, hence A > C. This again contradicts A = C.

**Step 12.** So D > F is impossible. By a symmetric argument, assume D < F. Then F > D, so by 5.8, F:E > D:E. By D5.7 there exist p, q such that pF > qE while pD <= qE. From A:B = E:F, by D5.5 (taking q-multiples of A and E, and p-multiples of B and F), pF > qE implies pB > qA, that is, qA < pB. From B:C = D:E, by D5.5, if pD < qE then pB < qC, and if pD = qE then pB = qC. In either subcase, pB <= qC. But then qA < pB <= qC gives qA < qC, so A < C, contradicting A = C. Hence D < F is also impossible. Therefore D = F.

**Step 13.** (Case 3: A < C.) Since A < C, C > A. By 5.8, C:B > A:B. By D5.7, there exist positive integers m and n such that mC > nB while mA does not exceed nB, that is, mA <= nB.

**Step 14.** From mC > nB, that is, nB < mC. From B:C = D:E, by D5.5 (taking n-multiples of B and D, and m-multiples of C and E), since nB < mC, we conclude nD < mE.

**Step 15.** Now consider mA <= nB. If mA < nB, then from A:B = E:F, by D5.5 (taking m-multiples of A and E, and n-multiples of B and F), mA < nB implies mE < nF. Combined with nD < mE from Step 14, we get nD < mE < nF, hence nD < nF, so D < F.

**Step 16.** If mA = nB, then from A:B = E:F, by D5.5, mA = nB implies mE = nF. Combined with nD < mE from Step 14, we get nD < mE = nF, hence nD < nF, so D < F. This completes Case 3.

**Step 17.** Therefore in all cases: if A > C then D > F, if A = C then D = F, and if A < C then D < F. Q.E.D.

**USED:** 5.8, D5.18, D5.5, D5.7
**Human refs (from References field):** 5.10, 5.13, 5.8
**Jaccard:** 0.167 — AI adds ['D5.18', 'D5.5', 'D5.7']; Human adds ['5.10', '5.13']

## Proposition 5.22
**Statement:** If there be any number of magnitudes whatever, and others equal to them in multitude, which taken two and two together are in the same ratio, they will also be in the same ratio ex aequali.

**Step 1.** Let there be any number of magnitudes A1, A2, ..., An, and others equal to them in multitude B1, B2, ..., Bn, which taken two and two are in the same ratio, so that A1:A2 = B1:B2, A2:A3 = B2:B3, and so on up to A(n-1):An = B(n-1):Bn. We are to prove that A1:An = B1:Bn (the ratio ex aequali), in accordance with D5.17.

**Step 2.** We first establish the result for three magnitudes: let A, B, C and D, E, F satisfy A:B = D:E and B:C = E:F. We shall show A:C = D:F. Take any equimultiples mA of A and mD of D, and any equimultiples nC of C and nF of F.

**Step 3.** Since A:B = D:E, by 5.4 (taking m-multiples of the first and third, and any multiples of the second and fourth), for any multiple pB of B and pE of E we have that mA and mD bear the same ratio-relation to pB and pE respectively: mA:pB = mD:pE in the sense of D5.5. In particular, by 5.15, mA:mB = mD:mE, since A:B = mA:mB and D:E = mD:mE, and so by 5.11, mA:mB = mD:mE.

**Step 4.** Since B:C = E:F, by 5.4 (taking m-multiples of the first and third, and n-multiples of the second and fourth), mB:nC = mE:nF.

**Step 5.** Now we have three magnitudes mA, mB, nC and three magnitudes mD, mE, nF, with mA:mB = mD:mE (Step 3) and mB:nC = mE:nF (Step 4). By 5.20 (the ex aequali ordering result for three magnitudes), if mA > nC then mD > nF, if mA = nC then mD = nF, and if mA < nC then mD < nF.

**Step 6.** Since mA, mD are arbitrary equimultiples of A, D, and nC, nF are arbitrary equimultiples of C, F, by D5.5 (the definition of same ratio) we conclude that A:C = D:F. This establishes the result for three magnitudes.

**Step 7.** Now for the general case, proceed by reducing the number of magnitudes. Given A1, A2, ..., An and B1, B2, ..., Bn with the consecutive ratios equal, consider the subsequence A1, A2, ..., A(n-1) and B1, B2, ..., B(n-1). These n-1 magnitudes on each side satisfy the same hypothesis (consecutive ratios equal). By repeating the three-magnitude argument, we can reduce from n magnitudes to n-1: from A1:A(n-1) = B1:B(n-1) (obtained by applying the same procedure to the first n-1 magnitudes) and A(n-1):An = B(n-1):Bn (given), the three-magnitude case (Steps 2-6) yields A1:An = B1:Bn.

**Step 8.** The reduction terminates because the base case of three magnitudes has been established in Steps 2-6. At each stage the three-magnitude result (using 5.4, 5.11, 5.15, and 5.20 via D5.5) reduces the count by one until only three remain.

**Step 9.** Therefore, if there be any number of magnitudes whatever, and others equal to them in multitude, which taken two and two together are in the same ratio, they will also be in the same ratio ex aequali. Q.E.D.

**USED:** 5.11, 5.15, 5.20, 5.4, D5.17, D5.5
**Human refs (from References field):** 5.20, 5.4, D5.5
**Jaccard:** 0.500 — AI adds ['5.11', '5.15', 'D5.17']

## Proposition 5.23
**Statement:** If there be three magnitudes, and others equal to them in multitude, which taken two and two together are in the same ratio, and the proportion of them be perturbed, they will also be in the same ratio ex aequali.

**Step 1.** Let A, B, C be three magnitudes and D, E, F be three other magnitudes such that A:B = E:F and B:C = D:E, so that the proportion is perturbed (D5.18). We are to prove that A:C = D:F, which is the ratio ex aequali (D5.17).

**Step 2.** To establish A:C = D:F by D5.5, let m and n be any positive integers whatever. We must show that mA > nC implies mD > nF, that mA = nC implies mD = nF, and that mA < nC implies mD < nF.

**Step 3.** Consider the six magnitudes mA, mB, nC and mD, nE, nF. We shall show these satisfy a perturbed proportion.

**Step 4.** Since A:B = E:F, by 5.15 (parts have the same ratio as equimultiples taken in corresponding order) we have A:B = mA:mB and E:F = nE:nF. Then by 5.11 (ratios which are the same with the same ratio are also the same with one another), mA:mB = nE:nF.

**Step 5.** Since B:C = D:E, by 5.4 (equimultiples of the first and third have the same ratio to equimultiples of the second and fourth), taking m-multiples of B and D, and n-multiples of C and E, we obtain mB:nC = mD:nE.

**Step 6.** From Steps 4 and 5, the six magnitudes mA, mB, nC and mD, nE, nF satisfy the perturbed proportion: mA:mB = nE:nF and mB:nC = mD:nE.

**Step 7.** By 5.21 (if three magnitudes and others equal to them in multitude are in the same ratio with the proportion perturbed, then the ex aequali ordering is preserved), since mA, mB, nC and mD, nE, nF are in perturbed proportion, we conclude: if mA > nC then mD > nF; if mA = nC then mD = nF; if mA < nC then mD < nF.

**Step 8.** Since m and n were taken as any positive integers whatever, by D5.5 (the definition of same ratio) we conclude A:C = D:F.

**Step 9.** Therefore, if there be three magnitudes and others equal to them in multitude, which taken two and two together are in the same ratio, and the proportion of them be perturbed, they will also be in the same ratio ex aequali. Q.E.D.

**USED:** 5.11, 5.15, 5.21, 5.4, D5.17, D5.18, D5.5
**Human refs (from References field):** 5.11, 5.15, 5.16, 5.21
**Jaccard:** 0.375 — AI adds ['5.4', 'D5.17', 'D5.18', 'D5.5']; Human adds ['5.16']

## Proposition 5.24
**Statement:** If a first magnitude have to a second the same ratio as a third has to a fourth, and also a fifth have to the second the same ratio as a sixth to the fourth, the first and fifth added together will have to the second the same ratio as the third and sixth have to the fourth.

**Step 1.** Let the first magnitude A have to the second B the same ratio as the third C has to the fourth D, and let also the fifth E have to the second B the same ratio as the sixth F has to the fourth D. That is, A:B :: C:D and E:B :: F:D. We are to prove that (A+E):B :: (C+F):D.

**Step 2.** Since E:B :: F:D, by the definition of same ratio (D5.5), for any equimultiples mE, mF of E, F and any equimultiples nB, nD of B, D, the order relations are preserved: mE exceeds, equals, or falls short of nB according as mF exceeds, equals, or falls short of nD. By swapping the roles of the multipliers (taking n as the multiplier of E, F and m as the multiplier of B, D), we obtain: for any positive integers m and n, mB exceeds, equals, or falls short of nE according as mD exceeds, equals, or falls short of nF. Therefore, by D5.5 and the definition of inverse ratio (D5.13), B:E :: D:F.

**Step 3.** We now have two proportions with linked middle terms: A:B :: C:D (given) and B:E :: D:F (Step 2). These are three magnitudes A, B, E and another three C, D, F, taken two and two in the same ratio. By Proposition 5.22 (ex aequali), A:E :: C:F.

**Step 4.** Since A:E :: C:F, by Proposition 5.18 (if magnitudes be proportional separando, they will also be proportional componendo), we conclude that (A+E):E :: (C+F):F. Here A is the excess of (A+E) over E, and C is the excess of (C+F) over F, so the separated proportion A:E :: C:F yields the composed proportion (A+E):E :: (C+F):F.

**Step 5.** We now have two proportions with linked middle terms: (A+E):E :: (C+F):F (Step 4) and E:B :: F:D (given). These are three magnitudes (A+E), E, B and another three (C+F), F, D, taken two and two in the same ratio. By Proposition 5.22 (ex aequali), (A+E):B :: (C+F):D.

**Step 6.** Therefore, the first and fifth added together have to the second the same ratio as the third and sixth have to the fourth. Q.E.D.

**USED:** 5.18, 5.22, D5.13, D5.5
**Human refs (from References field):** 5.18, 5.22
**Jaccard:** 0.500 — AI adds ['D5.13', 'D5.5']

## Proposition 5.25
**Statement:** If four magnitudes be proportional, the greatest and the least are greater than the remaining two.

**Step 1.** Let A, B, C, D be four magnitudes such that A : B :: C : D, where A is the greatest and D is the least of the four.

**Step 2.** Since A : B :: C : D, by alternando (5.16), A : C :: B : D. Since A is the greatest of the four magnitudes, A > B. Therefore, since A : C :: B : D and A > B, by 5.14 we have C > D. Likewise, since A is the greatest, A > C, so by 5.14 applied to A : C :: B : D, we have B > D.

**Step 3.** Since A : B :: C : D and A > B (from Step 2), the excess A - B is well defined. Likewise, since C > D (from Step 2), the excess C - D is well defined. By separando (5.17), (A - B) : B :: (C - D) : D.

**Step 4.** Applying alternando (5.16) to the proportion (A - B) : B :: (C - D) : D, we obtain (A - B) : (C - D) :: B : D. Since B > D (from Step 2), by 5.14, A - B > C - D.

**Step 5.** Since A - B > C - D, the magnitude A - B exceeds C - D by some magnitude E, so that A - B = (C - D) + E, where E is a positive magnitude. Adding B + D to both sides by CN2 (if equals be added to equals, the wholes are equal), we obtain A - B + B + D = (C - D) + E + B + D, which gives A + D = B + C + E. Since A + D = B + C + E, the magnitude A + D is the whole of which B + C is a part. Therefore, by CN5, A + D > B + C.

**Step 6.** Hence the greatest A and the least D together are greater than the remaining two magnitudes B and C together. Q.E.D.

**USED:** 5.14, 5.16, 5.17, CN2, CN5
**Human refs (from References field):** 5.19
**Jaccard:** 0.000 — AI adds ['5.14', '5.16', '5.17', 'CN2', 'CN5']; Human adds ['5.19']
