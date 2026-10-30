# Book 5 of Euclid's Elements — Step-by-Step AI Proofs (Run B)

## Proposition 5.1
**Statement:** If a magnitude be the same multiple of a magnitude that a part subtracted is of a part subtracted, the remainder will also be the same multiple of the remainder that the whole is of the whole.

**Step 1.** Let magnitude AB be the same multiple of magnitude CD that the part AE subtracted is of the part CF subtracted. We must show that the remainder EB is the same multiple of the remainder FD that the whole AB is of the whole CD.

**Step 2.** Since AB is the same multiple of CD that AE is of CF, let this common multiple be m. Then by Definition 5.2 (the greater is a multiple of the less when it is measured by the less), there exist magnitudes equal to CD, say CD_1, CD_2, ..., CD_m, such that AB is composed of these m parts each equal to CD. Similarly, AE is composed of m parts each equal to CF, say CF_1, CF_2, ..., CF_m.

**Step 3.** Arrange the construction so that AB is divided into m parts each equal to CD: let AB = CD_1 + CD_2 + ... + CD_m, and AE is divided into m parts each equal to CF: let AE = CF_1 + CF_2 + ... + CF_m, where AE is a part of AB and CF is a part of CD.

**Step 4.** Since CD is a magnitude and CF is a part subtracted from it, the remainder is FD = CD - CF. Consider each pair: CD_i and CF_i for i = 1, 2, ..., m. Each CD_i equals CD and each CF_i equals CF. Since CF is a part of CD (CF is less than CD, as AE being a part subtracted from AB requires CF to be a part subtracted from CD), each CF_i is a part of the corresponding CD_i.

**Step 5.** For each i, the magnitude CD_i equals CD, and the magnitude CF_i equals CF. By Common Notion 3 (if equals be subtracted from equals, the remainders are equal), subtracting CF_i from CD_i yields a remainder equal to CD - CF = FD. That is, CD_i - CF_i = FD for each i = 1, 2, ..., m.

**Step 6.** Now, EB = AB - AE = (CD_1 + CD_2 + ... + CD_m) - (CF_1 + CF_2 + ... + CF_m). Regrouping term by term: EB = (CD_1 - CF_1) + (CD_2 - CF_2) + ... + (CD_m - CF_m). By Common Notion 2 (if equals be added to equals, the wholes are equal), this regrouping preserves equality since each subtraction is of a part from its corresponding whole.

**Step 7.** From Step 5, each term (CD_i - CF_i) equals FD. Therefore EB = FD + FD + ... + FD (m times). By Definition 5.2, EB is the same multiple of FD as m, which is the same multiple that AB is of CD.

**Step 8.** Therefore, the remainder EB is the same multiple of the remainder FD that the whole AB is of the whole CD. Q.E.D.

**USED:** CN2, CN3, D5.1, D5.2
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['CN2', 'CN3', 'D5.1', 'D5.2']

## Proposition 5.2
**Statement:** If a first magnitude be the same multiple of a second that a third is of a fourth, and a fifth also be the same multiple of the second that a sixth is of the fourth, the sum of the first and fifth will also be the same multiple of the second that the sum of the third and sixth is of the fourth.

**Step 1.** Let A be the same multiple of B that C is of D, and let E be the same multiple of B that F is of D. We must show that A + E is the same multiple of B that C + F is of D.

**Step 2.** Since A is the same multiple of B that C is of D, there are as many magnitudes equal to B in A as there are magnitudes equal to D in C [D5.2]. Let the magnitudes equal to B in A be B1, B2, ..., Bm, so that A = B1 + B2 + ... + Bm, where each Bi equals B. Correspondingly, let the magnitudes equal to D in C be D1, D2, ..., Dm, so that C = D1 + D2 + ... + Dm, where each Di equals D.

**Step 3.** Since E is the same multiple of B that F is of D, there are as many magnitudes equal to B in E as there are magnitudes equal to D in F [D5.2]. Let the magnitudes equal to B in E be B(m+1), B(m+2), ..., B(m+n), so that E = B(m+1) + ... + B(m+n), where each equals B. Correspondingly, let the magnitudes equal to D in F be D(m+1), D(m+2), ..., D(m+n), so that F = D(m+1) + ... + D(m+n), where each equals D.

**Step 4.** Since A = B1 + B2 + ... + Bm and E = B(m+1) + ... + B(m+n), we have A + E = B1 + B2 + ... + Bm + B(m+1) + ... + B(m+n) [CN2]. This is a sum of (m + n) magnitudes, each equal to B.

**Step 5.** Similarly, since C = D1 + D2 + ... + Dm and F = D(m+1) + ... + D(m+n), we have C + F = D1 + D2 + ... + Dm + D(m+1) + ... + D(m+n) [CN2]. This is a sum of (m + n) magnitudes, each equal to D.

**Step 6.** Therefore A + E contains as many magnitudes equal to B as C + F contains magnitudes equal to D, namely (m + n) of each. By the definition of equimultiple [D5.2], A + E is the same multiple of B that C + F is of D.

**Step 7.** Therefore, if a first magnitude be the same multiple of a second that a third is of a fourth, and a fifth also be the same multiple of the second that a sixth is of the fourth, the sum of the first and fifth will also be the same multiple of the second that the sum of the third and sixth is of the fourth. Q.E.D.

**USED:** CN2, D5.2
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['CN2', 'D5.2']

## Proposition 5.3
**Statement:** If a first magnitude be the same multiple of a second that a third is of a fourth, and if equimultiples be taken of the first and third, then also ex aequali the magnitudes taken will be equimultiples respectively, the one of the second and the other of the fourth.

**Step 1.** Let A be the same multiple of B that C is of D, so that A = m·B and C = m·D for some multiplicity m [D5.2]. Let equimultiples be taken of A and C; call them E and F, so that E = n·A and F = n·C for some multiplicity n [D5.2].

**Step 2.** Since E = n·A, we may write E as the sum of n magnitudes each equal to A: E = A₁ + A₂ + ... + Aₙ, where each Aᵢ = A. Similarly, F = C₁ + C₂ + ... + Cₙ, where each Cᵢ = C.

**Step 3.** Since A = m·B, each Aᵢ is the same multiple of B, namely m·B. Likewise, since C = m·D, each Cᵢ is the same multiple of D, namely m·D.

**Step 4.** Consider A₁ and A₂. Since A₁ = m·B and A₂ = m·B, by Proposition 5.2, A₁ + A₂ = 2m·B. Likewise, since C₁ = m·D and C₂ = m·D, by the same proposition, C₁ + C₂ = 2m·D. Thus A₁ + A₂ is the same multiple of B that C₁ + C₂ is of D.

**Step 5.** Now consider (A₁ + A₂) and A₃. Since A₁ + A₂ = 2m·B and A₃ = m·B, by Proposition 5.2, A₁ + A₂ + A₃ = 3m·B. Likewise C₁ + C₂ + C₃ = 3m·D.

**Step 6.** Continuing in this manner, at each stage the accumulated sum of k copies of A equals km·B and the accumulated sum of k copies of C equals km·D. Adding the next copy of A (which is m·B) and the next copy of C (which is m·D) by Proposition 5.2 yields (k+1)m·B and (k+1)m·D respectively.

**Step 7.** After all n additions, we obtain E = A₁ + A₂ + ... + Aₙ = nm·B, and F = C₁ + C₂ + ... + Cₙ = nm·D.

**Step 8.** Therefore E is the same multiple of B that F is of D, both being nm-times multiples [D5.2]. That is, the equimultiples taken of A and C are equimultiples respectively of B and of D.

**Step 9.** Therefore, if a first magnitude be the same multiple of a second that a third is of a fourth, and if equimultiples be taken of the first and third, then also ex aequali the magnitudes taken will be equimultiples respectively, the one of the second and the other of the fourth. Q.E.D.

**USED:** 5.2, D5.2
**Human refs (from References field):** 5.2
**Jaccard:** 0.500 — AI adds ['D5.2']

## Proposition 5.4
**Statement:** If a first magnitude have to a second the same ratio as a third to a fourth, any equimultiples whatever of the first and third will also have the same ratio to any equimultiples whatever of the second and fourth respectively, taken in corresponding order.

**Step 1.** Let A, B, C, D be magnitudes such that A:B :: C:D. Let m and n be any positive integers, and let mA, mC be equimultiples of A and C, and nB, nD be equimultiples of B and D. We wish to show that mA:nB :: mC:nD.

**Step 2.** By Definition D5.5, to prove mA:nB :: mC:nD, we must show that for any equimultiples whatever p(mA) and p(mC) of mA and mC, and any equimultiples whatever q(nB) and q(nD) of nB and nD, the former equimultiples alike exceed, are alike equal to, or alike fall short of the latter equimultiples, taken in corresponding order.

**Step 3.** Let p and q be any positive integers whatever. Take p(mA) and p(mC) as equimultiples of mA and mC, and q(nB) and q(nD) as equimultiples of nB and nD.

**Step 4.** Now mA is the same multiple of A that mC is of C (both being the m-th multiple). Since p(mA) and p(mC) are equimultiples of mA and mC respectively, by Proposition 5.3 (if a first magnitude is the same multiple of a second that a third is of a fourth, and equimultiples are taken, then ex aequali the resulting magnitudes are equimultiples respectively of the second and fourth), p(mA) is the same multiple of A that p(mC) is of C. That is, p(mA) = (pm)A and p(mC) = (pm)C, so p(mA) and p(mC) are equimultiples of A and C.

**Step 5.** Similarly, nB is the same multiple of B that nD is of D (both being the n-th multiple). Since q(nB) and q(nD) are equimultiples of nB and nD respectively, by Proposition 5.3 again, q(nB) is the same multiple of B that q(nD) is of D. That is, q(nB) = (qn)B and q(nD) = (qn)D, so q(nB) and q(nD) are equimultiples of B and D.

**Step 6.** Since A:B :: C:D by hypothesis, Definition D5.5 guarantees that for any equimultiples whatever of A and C, and any equimultiples whatever of B and D, the former alike exceed, are alike equal to, or alike fall short of the latter. Applying this to the equimultiples (pm)A, (pm)C of A, C and (qn)B, (qn)D of B, D: if (pm)A exceeds (qn)B then (pm)C exceeds (qn)D; if (pm)A equals (qn)B then (pm)C equals (qn)D; and if (pm)A falls short of (qn)B then (pm)C falls short of (qn)D.

**Step 7.** But (pm)A = p(mA), (pm)C = p(mC), (qn)B = q(nB), and (qn)D = q(nD). Therefore: if p(mA) exceeds q(nB) then p(mC) exceeds q(nD); if p(mA) equals q(nB) then p(mC) equals q(nD); and if p(mA) falls short of q(nB) then p(mC) falls short of q(nD).

**Step 8.** Since p and q were arbitrary positive integers, this holds for any equimultiples whatever of mA, mC and any equimultiples whatever of nB, nD. Therefore, by Definition D5.5, mA:nB :: mC:nD.

**Step 9.** Since m and n were any positive integers whatever, any equimultiples whatever of the first and third have the same ratio to any equimultiples whatever of the second and fourth respectively, taken in corresponding order. Q.E.D.

**USED:** 5.3, D5.2, D5.5
**Human refs (from References field):** 5.3, D5.5
**Jaccard:** 0.667 — AI adds ['D5.2']

## Proposition 5.5
**Statement:** If a magnitude be the same multiple of a magnitude that a part subtracted is of a part subtracted, the remainder will also be the same multiple of the remainder that the whole is of the whole.

**Step 1.** Let magnitude AB be the same multiple of magnitude CD that the part AE subtracted is of the part CF subtracted. We must show that the remainder EB is the same multiple of the remainder FD that the whole AB is of the whole CD. That is, suppose AB = m times CD and AE = m times CF, for some multiplicity m; we must show EB = m times FD.

**Step 2.** Since FD is the remainder when CF is subtracted from CD, we have CD = CF + FD. By Definition 5.2, AB being the same multiple of CD means AB = m times CD, and AE being the same multiple of CF means AE = m times CF.

**Step 3.** Consider the magnitude that is the same multiple of FD that AE is of CF, namely m times FD. By Proposition 5.1 (whatever multiple one magnitude is of one, that multiple also will all be of all), since AE = m times CF and m times FD is the same multiple of FD, it follows that AE together with m times FD equals m times (CF + FD). That is, AE + m*FD = m*(CF + FD) = m*CD.

**Step 4.** But AB = m times CD by hypothesis. Therefore AE + m*FD = AB, by Common Notion 1 (things equal to the same thing are equal to one another), since both equal m times CD.

**Step 5.** Subtracting AE from both sides, by Common Notion 3 (if equals be subtracted from equals, the remainders are equal), we obtain m*FD = AB - AE = EB.

**Step 6.** Therefore EB is the same multiple of FD that AB is of CD (both being m times their respective magnitudes), by Definition 5.2. This is what was to be proved.

**USED:** 5.1, CN1, CN3, D5.2
**Human refs (from References field):** 5.1
**Jaccard:** 0.250 — AI adds ['CN1', 'CN3', 'D5.2']

## Proposition 5.6
**Statement:** If two magnitudes be equimultiples of two magnitudes, and any magnitudes subtracted from them be equimultiples of the same, the remainders also are either equal to the same or equimultiples of them.

**Step 1.** Let A and B be equimultiples of magnitudes C and D respectively; that is, let A = mC and B = mD for some multiplier m [D5.2]. Let E and F be subtracted from A and B respectively, where E and F are equimultiples of the same C and D; that is, let E = nC and F = nD for some multiplier n, with n less than m so that the subtraction is possible [D5.2, CN5].

**Step 2.** We must show that the remainders A - E and B - F are either equal to C and D respectively, or equimultiples of them.

**Step 3.** Since E = nC and A = mC, let G = (m - n)C and H = (m - n)D. The magnitudes G and H are well-defined since m > n. If m - n = 1, then G = C and H = D. If m - n > 1, then G and H are equimultiples of C and D respectively [D5.2].

**Step 4.** Now E = nC is an equimultiple of C, and G = (m - n)C is either equal to C or a multiple of C. By Proposition 5.2, the sum of two equimultiples of the same magnitude is also a multiple of that magnitude: since E is n times C and G is (m - n) times C, the sum E + G is (n + (m - n)) times C, that is, m times C [5.2]. Therefore E + G = mC = A.

**Step 5.** Similarly, F = nD and H = (m - n)D, so by Proposition 5.2, F + H = (n + (m - n))D = mD = B [5.2].

**Step 6.** From Step 4, since E + G = A, subtracting E from both sides gives G = A - E [CN3]. From Step 5, since F + H = B, subtracting F from both sides gives H = B - F [CN3].

**Step 7.** Therefore the remainder A - E = G = (m - n)C and the remainder B - F = H = (m - n)D.

**Step 8.** Case 1: If m - n = 1, then A - E = C and B - F = D, so the remainders are equal to the original magnitudes C and D.

**Step 9.** Case 2: If m - n > 1, then A - E = (m - n)C and B - F = (m - n)D, so the remainders are equimultiples of C and D with the same multiplier (m - n) [D5.2].

**Step 10.** Therefore the remainders are either equal to C and D, or equimultiples of them. Q.E.D.

**USED:** 5.2, CN3, CN5, D5.2
**Human refs (from References field):** 5.2
**Jaccard:** 0.250 — AI adds ['CN3', 'CN5', 'D5.2']

## Proposition 5.7
**Statement:** Equal magnitudes have to the same the same ratio, as also has the same to equal magnitudes.

**Step 1.** Let A and B be equal magnitudes, and let C be any other magnitude. We are to prove two things: (i) A:C = B:C, and (ii) C:A = C:B.

**Step 2.** [Proof of Part (i): A:C = B:C.] Take any equimultiples mA and mB of A and B respectively, and take any equimultiple nC of C. That is, let mA = m times A and mB = m times B for some whole number m, and let nC = n times C for some whole number n.

**Step 3.** Since A equals B, by repeatedly applying CN2 (if equals be added to equals, the wholes are equal), adding A to itself m times yields the same magnitude as adding B to itself m times. That is, mA = mB. More precisely, A = B, so A + A = B + B by CN2, and continuing in this manner, m times A equals m times B.

**Step 4.** Since mA = mB, whenever mA exceeds nC, mB also exceeds nC; whenever mA equals nC, mB also equals nC; and whenever mA falls short of nC, mB also falls short of nC. This follows directly from CN1, since mA and mB, being equal, stand in the same relation to nC.

**Step 5.** Since this holds for all equimultiples mA, mB of A, B and all equimultiples nC of C, by D5.5 (the definition of same ratio), A has to C the same ratio that B has to C. That is, A:C = B:C.

**Step 6.** [Proof of Part (ii): C:A = C:B.] Now take any equimultiple mC of C, and take any equimultiples nA and nB of A and B respectively, where nA = n times A and nB = n times B for the same whole number n.

**Step 7.** Since A equals B, by the same reasoning as in Step 3 (repeatedly applying CN2), nA = nB.

**Step 8.** Since nA = nB, whenever mC exceeds nA, mC also exceeds nB; whenever mC equals nA, mC also equals nB; and whenever mC falls short of nA, mC also falls short of nB. Again this follows from CN1, since nA and nB are equal.

**Step 9.** Since this holds for all equimultiples mC of C and all equimultiples nA, nB of A, B, by D5.5, C has to A the same ratio that C has to B. That is, C:A = C:B.

**Step 10.** Therefore equal magnitudes have to the same magnitude the same ratio, and the same magnitude has to equal magnitudes the same ratio, which is what was to be proved. Q.E.D.

**USED:** CN1, CN2, D5.2, D5.5
**Human refs (from References field):** D5.5
**Jaccard:** 0.250 — AI adds ['CN1', 'CN2', 'D5.2']

## Proposition 5.8
**Statement:** Of unequal magnitudes, the greater has to the same a greater ratio than the less has; and the same has to the less a greater ratio than it has to the greater.

**Step 1.** Let A and B be unequal magnitudes with A greater than B, and let C be any magnitude of the same kind. We must show two things: (i) A has to C a greater ratio than B has to C, and (ii) C has to B a greater ratio than C has to A.

**Step 2.** Since A is greater than B, let D be the excess of A over B, so that A equals B together with D, and D is greater than nothing [CN5].

**Step 3.** Since D and C are magnitudes of the same kind, they are capable, when multiplied, of exceeding one another [D5.4]. Therefore there exists a positive integer m such that mD is greater than C.

**Step 4.** Since mA equals mB together with mD (for A equals B together with D, and if a magnitude is the same multiple of a magnitude that a part subtracted is of a part subtracted, the remainder is also the same multiple of the remainder that the whole is of the whole) [5.1], we have mA equal to mB together with mD.

**Step 5.** Since C and B are magnitudes of the same kind, they are capable, when multiplied, of exceeding one another [D5.4]. Therefore multiples of C eventually exceed mB. Let n be the greatest positive integer such that nC is not greater than mB. Then nC is not greater than mB, and (n+1)C is greater than mB.

**Step 6.** Now (n+1)C equals nC together with C [5.2, taking nC as n times C and C as 1 times C, their sum is (n+1) times C]. Since nC is not greater than mB, adding C to nC and C to mB respectively, we have (n+1)C, which equals nC together with C, is not greater than mB together with C [CN2].

**Step 7.** Since mD is greater than C (Step 3), the sum mB together with mD is greater than the sum mB together with C [CN5, since mB together with mD contains mB together with C as a part, the excess being mD minus C]. Therefore mA, which equals mB together with mD (Step 4), is greater than mB together with C.

**Step 8.** Since mA is greater than mB together with C (Step 7), and mB together with C is not less than (n+1)C (Step 6), it follows that mA is greater than (n+1)C.

**Step 9.** Also, (n+1)C is greater than mB (Step 5), so mB is less than (n+1)C, meaning mB does not exceed (n+1)C.

**Step 10.** We have found equimultiples mA and mB of A and B respectively (with multiplier m), and an equimultiple (n+1)C of C (with multiplier n+1), such that mA exceeds (n+1)C but mB does not exceed (n+1)C. Therefore, by the definition of greater ratio, A has to C a greater ratio than B has to C [D5.7]. This proves part (i).

**Step 11.** For part (ii), we must show that C has to B a greater ratio than C has to A. Using the same multipliers as above, consider equimultiples (n+1)C and (n+1)C of C (the first and third magnitudes, both with multiplier n+1), and equimultiples mB and mA of B and A respectively (the second and fourth magnitudes, both with multiplier m).

**Step 12.** From Step 9, (n+1)C is greater than mB, so the multiple of the first magnitude (C in the ratio C:B) exceeds the multiple of the second magnitude (B in the ratio C:B).

**Step 13.** From Step 8, mA is greater than (n+1)C, so (n+1)C does not exceed mA. That is, the multiple of the third magnitude (C in the ratio C:A) does not exceed the multiple of the fourth magnitude (A in the ratio C:A).

**Step 14.** Since the equimultiple of the first exceeds the equimultiple of the second, but the equimultiple of the third does not exceed the equimultiple of the fourth, by the definition of greater ratio, C has to B a greater ratio than C has to A [D5.7]. This proves part (ii).

**Step 15.** Therefore, of unequal magnitudes, the greater has to the same a greater ratio than the less has; and the same has to the less a greater ratio than it has to the greater. Q.E.D.

**USED:** 5.1, 5.2, CN2, CN5, D5.4, D5.7
**Human refs (from References field):** 5.1, D5.4, D5.7
**Jaccard:** 0.500 — AI adds ['5.2', 'CN2', 'CN5']

## Proposition 5.9
**Statement:** Magnitudes which have the same ratio to the same are equal to one another; and magnitudes to which the same has the same ratio are equal.

**Step 1.** Let A and B be magnitudes, and let C be another magnitude of the same kind, such that A:C :: B:C (i.e., A and B have the same ratio to C). We wish to show that A = B.

**Step 2.** Suppose, for contradiction, that A is not equal to B. Then one of them is greater than the other; assume without loss of generality that A > B.

**Step 3.** Since A > B, by Proposition 5.8, the greater magnitude has to the same a greater ratio than the less has. Therefore A:C > B:C (Definition 5.7).

**Step 4.** But we were given that A:C :: B:C (Definition 5.5), meaning the ratios are the same. This contradicts Step 3, since the same ratio cannot simultaneously be greater and equal. The case B > A leads to the same contradiction by symmetry. Therefore A = B.

**Step 5.** Now let C:A :: C:B (i.e., the same magnitude C has the same ratio to both A and B). We wish to show that A = B.

**Step 6.** Suppose, for contradiction, that A is not equal to B. Without loss of generality, assume A > B.

**Step 7.** Since A > B, by Proposition 5.8 (second part), the same magnitude has to the less a greater ratio than it has to the greater. Therefore C:B > C:A.

**Step 8.** But we were given that C:A :: C:B, meaning the ratios are the same. This contradicts Step 7. The case B > A leads to the same contradiction by symmetry. Therefore A = B.

**Step 9.** Both parts are established: magnitudes which have the same ratio to the same are equal to one another, and magnitudes to which the same has the same ratio are equal. Q.E.D.

**USED:** 5.8, D5.5, D5.7
**Human refs (from References field):** 5.8
**Jaccard:** 0.333 — AI adds ['D5.5', 'D5.7']

## Proposition 5.10
**Statement:** Of magnitudes which have a ratio to the same, that which has a greater ratio is greater; and that to which the same has a greater ratio is less.

**Step 1.** The proposition has two parts. For Part 1, let A and B be magnitudes each having a ratio to a magnitude C, and suppose that A has a greater ratio to C than B has to C (i.e., A:C > B:C in the sense of D5.7). We must show that A is greater than B.

**Step 2.** Assume for contradiction that A is not greater than B. Then either A equals B, or A is less than B.

**Step 3.** If A equals B, then by 5.7, A and B have the same ratio to C, that is, A:C = B:C. But this contradicts the hypothesis that A:C > B:C. So A does not equal B.

**Step 4.** If A is less than B, then B is greater than A. By 5.8 (the greater has to the same a greater ratio than the less), B:C > A:C. But this contradicts the hypothesis that A:C > B:C. So A is not less than B.

**Step 5.** Since A is neither equal to B nor less than B, we conclude that A is greater than B. This completes Part 1.

**Step 6.** For Part 2, let C be a magnitude having a ratio to magnitudes A and B, and suppose that C has a greater ratio to A than C has to B (i.e., C:A > C:B in the sense of D5.7). We must show that A is less than B.

**Step 7.** Assume for contradiction that A is not less than B. Then either A equals B, or A is greater than B.

**Step 8.** If A equals B, then by 5.7, the same magnitude C has the same ratio to A as to B, that is, C:A = C:B. But this contradicts the hypothesis that C:A > C:B. So A does not equal B.

**Step 9.** If A is greater than B, then by 5.8 (the same has to the less a greater ratio than it has to the greater), C:B > C:A. But this contradicts the hypothesis that C:A > C:B. So A is not greater than B.

**Step 10.** Since A is neither equal to B nor greater than B, we conclude that A is less than B. This completes Part 2.

**Step 11.** Therefore, of magnitudes which have a ratio to the same, that which has a greater ratio is greater; and that to which the same has a greater ratio is less. Q.E.D.

**USED:** 5.7, 5.8, D5.7
**Human refs (from References field):** 5.7, 5.8
**Jaccard:** 0.667 — AI adds ['D5.7']

## Proposition 5.11
**Statement:** Ratios which are the same with the same ratio are also the same with one another.

**Step 1.** Let A, B, C, D, E, F be magnitudes such that A:B :: C:D and C:D :: E:F. We must show that A:B :: E:F.

**Step 2.** Take any equimultiples mA, mC, mE of A, C, E respectively (all by the same multiplier m), and take any equimultiples nB, nD, nF of B, D, F respectively (all by the same multiplier n).

**Step 3.** Since A:B :: C:D, by D5.5, for these equimultiples mA, mC of A, C and equimultiples nB, nD of B, D: if mA exceeds nB then mC exceeds nD; if mA equals nB then mC equals nD; and if mA falls short of nB then mC falls short of nD.

**Step 4.** Since C:D :: E:F, by D5.5, for these equimultiples mC, mE of C, E and equimultiples nD, nF of D, F: if mC exceeds nD then mE exceeds nF; if mC equals nD then mE equals nF; and if mC falls short of nD then mE falls short of nF.

**Step 5.** Chaining the results of Steps 3 and 4: if mA exceeds nB, then mC exceeds nD (Step 3), and therefore mE exceeds nF (Step 4). If mA equals nB, then mC equals nD (Step 3), and therefore mE equals nF (Step 4). If mA falls short of nB, then mC falls short of nD (Step 3), and therefore mE falls short of nF (Step 4).

**Step 6.** Since the equimultiples m and n were taken arbitrarily, and in every case mA and mE (equimultiples of A and E) simultaneously exceed, are equal to, or fall short of nB and nF (equimultiples of B and F) respectively, it follows by D5.5 that A:B :: E:F.

**Step 7.** Therefore ratios which are the same with the same ratio are also the same with one another. Q.E.D.

**USED:** D5.5
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['D5.5']

## Proposition 5.12
**Statement:** If any number of magnitudes be proportional, as one of the antecedents is to one of the consequents, so will all the antecedents be to all the consequents.

**Step 1.** Let any number of magnitudes be proportional. For clarity, let there be three proportions (the argument generalizes to any number): let A, C, E be antecedents and B, D, F be consequents, such that A:B = C:D = E:F. We are to show that A:B = (A + C + E):(B + D + F).

**Step 2.** Take any equimultiples of the antecedents and the sum of antecedents: let G = mA, H = mC, and K = mE, where m is any positive integer. Then G, H, K are equimultiples of A, C, E respectively. By the definition of equimultiples and repeated application of CN2, we have G + H + K = mA + mC + mE = m(A + C + E). That is, the sum G + H + K is the same multiple of (A + C + E) that G is of A.

**Step 3.** Similarly, take any equimultiples of the consequents and the sum of consequents: let L = nB, M = nD, and N = nF, where n is any positive integer. Then L + M + N = nB + nD + nF = n(B + D + F), again by the definition of equimultiples and CN2.

**Step 4.** Since A:B = C:D, by D5.5, for the chosen m and n: if G > L then H > M, if G = L then H = M, and if G < L then H < M.

**Step 5.** Since A:B = E:F, by D5.5, for the same m and n: if G > L then K > N, if G = L then K = N, and if G < L then K < N.

**Step 6.** Suppose G > L. Then by Step 4, H > M, and by Step 5, K > N. Since G > L, H > M, and K > N, adding these inequalities by repeated application of CN2 yields G + H + K > L + M + N. That is, m(A + C + E) > n(B + D + F).

**Step 7.** Suppose G = L. Then by Step 4, H = M, and by Step 5, K = N. Adding these equalities by CN2 yields G + H + K = L + M + N. That is, m(A + C + E) = n(B + D + F).

**Step 8.** Suppose G < L. Then by Step 4, H < M, and by Step 5, K < N. Adding these inequalities by repeated application of CN2 yields G + H + K < L + M + N. That is, m(A + C + E) < n(B + D + F).

**Step 9.** We have shown that for arbitrary positive integers m and n: the equimultiple m(A + C + E) exceeds, equals, or falls short of the equimultiple n(B + D + F) according as the equimultiple mA exceeds, equals, or falls short of the equimultiple nB. Therefore, by D5.5, A:B = (A + C + E):(B + D + F).

**Step 10.** Since A:B is any one of the original equal ratios, and (A + C + E):(B + D + F) is the ratio of all antecedents to all consequents, we conclude: as one of the antecedents is to one of the consequents, so are all the antecedents to all the consequents. The same argument applies by induction to any number of proportional magnitudes. Q.E.F.

**USED:** CN2, D5.2, D5.5, D5.6
**Human refs (from References field):** 5.1, D5.5
**Jaccard:** 0.200 — AI adds ['CN2', 'D5.2', 'D5.6']; Human adds ['5.1']

## Proposition 5.13
**Statement:** If a first magnitude have to a second the same ratio as a third to a fourth, and the third have to the fourth a greater ratio than a fifth has to a sixth, the first will also have to the second a greater ratio than the fifth to the sixth.

**Step 1.** Let A, B, C, D, E, F be magnitudes such that A : B :: C : D, and C : D > E : F. We are to show that A : B > E : F.

**Step 2.** Since C : D > E : F, by D5.7 (definition of greater ratio) there exist equimultiples mC and mE of C and E, and equimultiples nD and nF of D and F, such that mC > nD but mE does not exceed nF.

**Step 3.** Now mC and mA are equimultiples of C and A respectively (both taken m times), and nD and nB are equimultiples of D and B respectively (both taken n times).

**Step 4.** Since A : B :: C : D, by D5.5 (definition of same ratio), for any equimultiples whatever of the first and third (here mA and mC) and any equimultiples whatever of the second and fourth (here nB and nD), the former equimultiples alike exceed, are alike equal to, or alike fall short of the latter equimultiples taken in corresponding order. Since mC > nD, it follows that mA > nB.

**Step 5.** We have thus found equimultiples mA and mE of A and E, and equimultiples nB and nF of B and F, such that mA > nB but mE does not exceed nF.

**Step 6.** Therefore, by D5.7 (definition of greater ratio), A : B > E : F. This is what was to be proved.

**USED:** D5.5, D5.7
**Human refs (from References field):** D5.5, D5.7
**Jaccard:** 1.000 — Perfect match.

## Proposition 5.14
**Statement:** If a first magnitude have to a second the same ratio as a third has to a fourth, and the first be greater than the third, the second will also be greater than the fourth; if equal, equal; and if less, less.

**Step 1.** Let A, B, C, D be magnitudes such that A:B = C:D (given hypothesis, by D5.5).

**Step 2.** (Case 1: A > C) Since A > C and both A and C have a ratio to B, by 5.8 (of unequal magnitudes, the greater has to the same a greater ratio than the less has), A:B > C:B.

**Step 3.** Since A:B = C:D (given), we may write C:D = A:B. We have A:B > C:B from Step 2. Setting first = C, second = D, third = A, fourth = B, fifth = C, sixth = B in 5.13: since C:D = A:B and A:B > C:B, it follows by 5.13 that C:D > C:B.

**Step 4.** Since C:D > C:B, by 5.10 (that to which the same has a greater ratio is less), D < B, that is, B > D. This completes Case 1.

**Step 5.** (Case 2: A = C) Since A = C, by 5.7 (equal magnitudes have to the same the same ratio), A:B = C:B.

**Step 6.** But A:B = C:D (given). Therefore C:B = C:D by 5.11 (ratios which are the same with the same ratio are also the same with one another), since both C:B and C:D equal A:B.

**Step 7.** Since C:B = C:D, by 5.9 (magnitudes to which the same has the same ratio are equal), B = D. This completes Case 2.

**Step 8.** (Case 3: A < C) Since A < C, equivalently C > A, and both have a ratio to B, by 5.8, C:B > A:B.

**Step 9.** Since A:B = C:D (given), setting first = C, second = B, third = C, fourth = B, fifth = C, sixth = D: we have C:B > A:B and A:B = C:D. By 5.13 (if first:second = third:fourth and third:fourth > fifth:sixth, then first:second > fifth:sixth), taking C:B as first:second, A:B as third:fourth equal to C:D as fifth:sixth — but we need to apply this correctly. We have C:B > A:B. Since A:B = C:D, substituting gives C:B > C:D.

**Step 10.** Since C:B > C:D, by 5.10 (that to which the same has a greater ratio is less), B < D. This completes Case 3.

**Step 11.** Therefore, if A:B = C:D, then: if A > C, then B > D; if A = C, then B = D; if A < C, then B < D. Q.E.D.

**USED:** 5.10, 5.11, 5.13, 5.7, 5.8, 5.9, D5.5
**Human refs (from References field):** 5.10, 5.13, 5.8
**Jaccard:** 0.429 — AI adds ['5.11', '5.7', '5.9', 'D5.5']

## Proposition 5.15
**Statement:** Parts have the same ratio as the same multiples of them taken in corresponding order.

**Step 1.** Let A and B be magnitudes, and let C = mA and D = mB be equimultiples of A and B respectively, where m is a positive integer. We must show that A : B = C : D.

**Step 2.** By Definition 5.5, to prove A : B = C : D, we must show that for any positive integers n and p, if we take equimultiples nA and nC of A and C, and equimultiples pB and pD of B and D, then nA and pB stand in the same order relation (greater, equal, or less) as nC and pD.

**Step 3.** Take any positive integers n and p. Form the equimultiples nA, nC of A and C, and pB, pD of B and D. Since C = mA, by Proposition 5.3, nC = n(mA) = (nm)A. Similarly, since D = mB, by Proposition 5.3, pD = p(mB) = (pm)B.

**Step 4.** Now by Proposition 5.3 applied in the reverse order, (nm)A = m(nA), since nA is the n-fold multiple of A and taking the m-fold multiple of nA yields the (mn)-fold multiple of A, which equals the (nm)-fold multiple as mn = nm. Similarly, (pm)B = m(pB). Therefore nC = m(nA) and pD = m(pB).

**Step 5.** Case 1: Suppose nA = pB. Then nC = m(nA) = m(pB) = pD, where the middle equality follows from CN2 applied repeatedly: since nA = pB, adding nA to nA yields the same result as adding pB to pB, and continuing for all m copies, we obtain m(nA) = m(pB). Thus nA = pB implies nC = pD.

**Step 6.** Case 2: Suppose nA > pB. Then nA exceeds pB by some magnitude E, so nA = pB + E where E is a positive magnitude. Now nC = m(nA) = m(pB + E). Since m(pB + E) consists of m copies of (pB + E) added together, by repeated application of CN2, this equals m(pB) + m(E), grouping the m copies of pB together and the m copies of E together. Since E is a positive magnitude, m(E) is also a positive magnitude. Therefore m(nA) = m(pB) + m(E) > m(pB) by CN5, since the whole m(pB) + m(E) is greater than the part m(pB). Hence nC > pD.

**Step 7.** Case 3: Suppose nA < pB. By the same reasoning as Case 2 with the roles of nA and pB interchanged, pB exceeds nA by some magnitude F, and m(pB) = m(nA) + m(F) > m(nA) by CN5. Therefore pD > nC, that is, nC < pD.

**Step 8.** In all three cases, the order relation between nA and pB is the same as the order relation between nC and pD. Since n and p were arbitrary positive integers, the condition of Definition 5.5 is satisfied. Therefore A : B = C : D, that is, parts have the same ratio as the same multiples of them taken in corresponding order.

**USED:** 5.3, CN2, CN5, D5.2, D5.5
**Human refs (from References field):** 5.12, 5.7
**Jaccard:** 0.000 — AI adds ['5.3', 'CN2', 'CN5', 'D5.2', 'D5.5']; Human adds ['5.12', '5.7']

## Proposition 5.16
**Statement:** If four magnitudes be proportional, they will also be proportional alternately.

**Step 1.** Let A, B, C, D be four magnitudes such that A:B :: C:D, where A and C are magnitudes of the same kind, and B and D are magnitudes of the same kind. We are to show that A:C :: B:D. [D5.5, D5.12]

**Step 2.** Take any equimultiples mA and mB of A and B respectively, and take any equimultiples nC and nD of C and D respectively, where m and n are arbitrary positive integers.

**Step 3.** By 5.15, parts have the same ratio as the same multiples of them taken in corresponding order. Therefore mA:mB :: A:B. [5.15]

**Step 4.** By hypothesis, A:B :: C:D. Therefore by 5.11 (ratios which are the same with the same ratio are also the same with one another), mA:mB :: C:D. [5.11]

**Step 5.** Again by 5.15, C:D :: nC:nD. [5.15]

**Step 6.** Combining Step 4 and Step 5 by 5.11, we obtain mA:mB :: nC:nD. [5.11]

**Step 7.** Now mA and nC are magnitudes of the same kind (since A and C are of the same kind), and mB and nD are magnitudes of the same kind (since B and D are of the same kind). By 5.14, since mA:mB :: nC:nD, it follows that: if mA > nC, then mB > nD; if mA = nC, then mB = nD; if mA < nC, then mB < nD. [5.14]

**Step 8.** Since m and n were chosen arbitrarily, Step 7 holds for all equimultiples mA, mB of A and B, and all equimultiples nC, nD of C and D. By D5.5, this is precisely the condition for A:C :: B:D. [D5.5]

**Step 9.** Therefore, if four magnitudes be proportional, they will also be proportional alternately. Q.E.D.

**USED:** 5.11, 5.14, 5.15, D5.12, D5.5
**Human refs (from References field):** 5.11, 5.14, 5.15, D5.5
**Jaccard:** 0.800 — AI adds ['D5.12']

## Proposition 5.17
**Statement:** If magnitudes be proportional componendo, they will also be proportional separando.

**Step 1.** Let AE, EB, CF, FD be four magnitudes proportional componendo, so that AB:BE :: CD:DF, where AB = AE + EB and CD = CF + FD. We must show that they are proportional separando, i.e., AE:EB :: CF:FD (D5.14, D5.15).

**Step 2.** Take any equimultiples mAE and mCF of AE and CF respectively, and any equimultiples nEB and nFD of EB and FD respectively (where m and n are arbitrary positive integers).

**Step 3.** Since mAE is the m-th multiple of AE and mEB is the m-th multiple of EB, and since AB = AE + EB, by 5.1 we have that mAE + mEB = m(AE + EB) = mAB. That is, mAB is the m-th multiple of AB. Similarly, mCF + mFD = m(CF + FD) = mCD, so mCD is the m-th multiple of CD. Therefore mAB and mCD are equimultiples of AB and CD.

**Step 4.** Since mEB is the m-th multiple of EB and nEB is the n-th multiple of EB, by 5.2 the sum mEB + nEB is the (m+n)-th multiple of EB. Similarly, mFD + nFD is the (m+n)-th multiple of FD. Therefore (m+n)EB and (m+n)FD are equimultiples of BE and DF.

**Step 5.** Since AB:BE :: CD:DF by hypothesis, and mAB, mCD are equimultiples of AB, CD while (m+n)BE, (m+n)DF are equimultiples of BE, DF, by D5.5 the three cases hold simultaneously: if mAB > (m+n)BE then mCD > (m+n)DF; if mAB = (m+n)BE then mCD = (m+n)DF; if mAB < (m+n)BE then mCD < (m+n)DF.

**Step 6.** Now mAB = mAE + mEB (from Step 3). So mAB > (m+n)EB, i.e., mAE + mEB > mEB + nEB, holds if and only if mAE > nEB (by CN3, subtracting the common magnitude mEB from both sides). Similarly mAB = (m+n)EB if and only if mAE = nEB, and mAB < (m+n)EB if and only if mAE < nEB.

**Step 7.** Likewise, mCD = mCF + mFD (from Step 3). So mCD > (m+n)FD, i.e., mCF + mFD > mFD + nFD, holds if and only if mCF > nFD (by CN3, subtracting mFD from both sides). Similarly mCD = (m+n)FD if and only if mCF = nFD, and mCD < (m+n)FD if and only if mCF < nFD.

**Step 8.** Combining Steps 5, 6, and 7: for arbitrary equimultiples mAE, mCF of AE, CF and arbitrary equimultiples nEB, nFD of EB, FD, if mAE > nEB then mCF > nFD; if mAE = nEB then mCF = nFD; if mAE < nEB then mCF < nFD.

**Step 9.** Therefore, by D5.5, AE:EB :: CF:FD. That is, the magnitudes are proportional separando (D5.15). Q.E.D.

**USED:** 5.1, 5.2, CN3, D5.14, D5.15, D5.5
**Human refs (from References field):** 5.1, 5.2
**Jaccard:** 0.333 — AI adds ['CN3', 'D5.14', 'D5.15', 'D5.5']

## Proposition 5.18
**Statement:** If magnitudes be proportional separando, they will also be proportional componendo.

**Step 1.** Let AE, EB, CF, FD be magnitudes such that AE : EB :: CF : FD (proportional separando). Let AB = AE + EB and CD = CF + FD. We must show that AB : BE :: CD : DF (proportional componendo), where we write BE for EB and DF for FD.

**Step 2.** By D5.5, to establish AB : BE :: CD : DF, we must show that for any equimultiples m*AB and m*CD of the first and third, and any equimultiples n*BE and n*DF of the second and fourth, the former equimultiples alike exceed, are alike equal to, or alike fall short of the latter equimultiples taken in corresponding order.

**Step 3.** Take arbitrary equimultiples m*AB and m*CD, and arbitrary equimultiples n*BE and n*DF. Since AB = AE + EB, by 5.1 we have m*AB = m*AE + m*EB. Similarly, since CD = CF + FD, we have m*CD = m*CF + m*FD.

**Step 4.** Consider first the case where n > m. Then (n - m) is a positive integer and (n - m)*BE and (n - m)*DF are well-defined equimultiples. We have m*AB compared with n*BE, that is, m*AE + m*EB compared with n*BE. By CN3 (subtracting equals from both sides, namely m*EB from each), m*AE + m*EB is greater than, equal to, or less than n*BE according as m*AE is greater than, equal to, or less than (n - m)*BE. Likewise, m*CD is greater than, equal to, or less than n*DF according as m*CF is greater than, equal to, or less than (n - m)*DF.

**Step 5.** Now m*AE and m*CF are equimultiples of AE and CF, and (n - m)*BE and (n - m)*DF are equimultiples of BE and DF. Since AE : EB :: CF : FD by hypothesis, D5.5 tells us that m*AE is greater than, equal to, or less than (n - m)*BE according as m*CF is greater than, equal to, or less than (n - m)*DF. Therefore, by Step 4, m*AB is greater than, equal to, or less than n*BE according as m*CD is greater than, equal to, or less than n*DF.

**Step 6.** Now consider the case where n is less than or equal to m. Since AE is a magnitude, m*AE is positive, so m*AE + m*EB > m*EB. Since n is less than or equal to m, we have m*EB is greater than or equal to n*EB (by the nature of equimultiples), hence m*AE + m*EB > n*EB, that is, m*AB > n*BE. By the same reasoning, m*CF is positive, so m*CF + m*FD > n*FD, that is, m*CD > n*DF. Thus both equimultiples of the first and third exceed the corresponding equimultiples of the second and fourth, and the condition of D5.5 is satisfied in this case as well.

**Step 7.** Since in every case — whether n > m, n = m, or n < m — the equimultiples m*AB and m*CD alike exceed, are alike equal to, or alike fall short of n*BE and n*DF respectively, it follows by D5.5 that AB : BE :: CD : DF. That is, the magnitudes are proportional componendo. Q.E.D.

**USED:** 5.1, CN2, CN3, CN5, D5.14, D5.15, D5.5
**Human refs (from References field):** 5.11, 5.14, 5.17
**Jaccard:** 0.000 — AI adds ['5.1', 'CN2', 'CN3', 'CN5', 'D5.14', 'D5.15', 'D5.5']; Human adds ['5.11', '5.14', '5.17']

## Proposition 5.19
**Statement:** If, as a whole is to a whole, so is a part subtracted to a part subtracted, the remainder will also be to the remainder as whole to whole.

**Step 1.** Let AB and CD be two magnitudes, and let AE be a part subtracted from AB and CF a part subtracted from CD, such that AB : CD = AE : CF. We must show that the remainder EB is to the remainder FD as AB is to CD, that is, EB : FD = AB : CD.

**Step 2.** Since AB : CD = AE : CF, by alternating the proportion (5.16) we obtain AB : AE = CD : CF.

**Step 3.** Now AB is composed of AE and EB, so AB = AE + EB. Similarly, CD is composed of CF and FD, so CD = CF + FD. Therefore AB : AE = CD : CF can be written as (AE + EB) : AE = (CF + FD) : CF. This is a proportion in the "componendo" form.

**Step 4.** Since the magnitudes are proportional componendo, by Proposition 5.17 (separando) they are also proportional separando: EB : AE = FD : CF.

**Step 5.** From EB : AE = FD : CF, by alternating the proportion (5.16) we obtain EB : FD = AE : CF.

**Step 6.** But we were given that AB : CD = AE : CF. Since EB : FD = AE : CF and AB : CD = AE : CF, both ratios are the same as the ratio AE : CF. Therefore by Proposition 5.11 (ratios which are the same with the same ratio are also the same with one another), EB : FD = AB : CD.

**Step 7.** Therefore the remainder EB is to the remainder FD as the whole AB is to the whole CD, which is what was to be proved.

**USED:** 5.11, 5.16, 5.17
**Human refs (from References field):** 5.11, 5.16, 5.17
**Jaccard:** 1.000 — Perfect match.

## Proposition 5.20
**Statement:** If there be three magnitudes, and others equal to them in multitude, which taken two and two are in the same ratio, and if ex aequali the first be greater than the third, the fourth will also be greater than the sixth; if equal, equal; and, if less, less.

**Step 1.** Let A, B, C be three magnitudes and D, E, F be three other magnitudes such that A:B = D:E and B:C = E:F. We must show that if A > C then D > F, if A = C then D = F, and if A < C then D < F. [D5.17]

**Step 2.** [Case A > C.] Since A > C, the greater magnitude A has to B a greater ratio than the lesser magnitude C has to B; that is, A:B > C:B. [5.8]

**Step 3.** Since A:B = D:E and A:B > C:B, it follows that D:E > C:B. [5.13]

**Step 4.** By the definition of greater ratio, there exist positive integers m and n such that mD > nE while mC does not exceed nB, that is, nB >= mC. [D5.7]

**Step 5.** Since B:C = E:F, by the definition of same ratio applied with equimultiples nB, nE of B, E and mC, mF of C, F: the comparison of nB to mC corresponds to the comparison of nE to mF. Since nB >= mC, it follows that nE >= mF. [D5.5]

**Step 6.** From Step 4 we have mD > nE, and from Step 5 we have nE >= mF. Therefore mD > mF.

**Step 7.** Since mD and mF are equimultiples of D and F respectively, by Proposition 5.15 we have D:F = mD:mF. Applying the definition of same ratio with unit equimultiples, mD > mF implies D > F. Therefore when A > C, we conclude D > F. [5.15, D5.5]

**Step 8.** [Case A = C.] Since A = C, equal magnitudes have the same ratio to the same magnitude B, so A:B = C:B. [5.7]

**Step 9.** Since A:B = D:E and A:B = C:B, ratios which are the same with the same ratio are the same with one another, so D:E = C:B. [5.11]

**Step 10.** Suppose for contradiction that D > F. Then by 5.8, D:E > F:E. Since D:E = C:B and D:E > F:E, it follows that C:B > F:E. [5.8, 5.13]

**Step 11.** By the definition of greater ratio applied to C:B > F:E, there exist positive integers m and n such that mC > nB and mF does not exceed nE, that is, nE >= mF. [D5.7]

**Step 12.** From B:C = E:F and the definition of same ratio with equimultiples nB, nE and mC, mF: since mC > nB (i.e., nB < mC), it follows that nE < mF, that is, mF > nE. But Step 11 requires nE >= mF, i.e., mF <= nE. This is a contradiction. Therefore D is not greater than F. [D5.5]

**Step 13.** Now suppose for contradiction that D < F. Then by 5.8, F:E > D:E. Since D:E = C:B, it follows that F:E > C:B. By the definition of greater ratio, there exist positive integers m and n such that mF > nE and mC does not exceed nB, that is, nB >= mC. [5.8, 5.13, D5.7]

**Step 14.** From B:C = E:F and the definition of same ratio with equimultiples nB, nE and mC, mF: since nB >= mC, it follows that nE >= mF, that is, mF <= nE. But Step 13 requires mF > nE. This is a contradiction. Therefore D is not less than F. [D5.5]

**Step 15.** Since D is neither greater than F nor less than F, we conclude D = F. Therefore when A = C, D = F.

**Step 16.** [Case A < C.] Since A < C, the greater magnitude C has to B a greater ratio than the lesser magnitude A has to B; that is, C:B > A:B. [5.8]

**Step 17.** Since A:B = D:E and C:B > A:B, by the definition of greater ratio there exist m and n such that mC > nB and mA does not exceed nB. By the definition of same ratio applied to A:B = D:E, since mA does not exceed nB, mD does not exceed nE. So we have mC > nB and mD <= nE, which means C:B > D:E. [D5.7, D5.5]

**Step 18.** By the definition of greater ratio applied to C:B > D:E, there exist positive integers m and n such that mC > nB and mD does not exceed nE, that is, nE >= mD. [D5.7]

**Step 19.** From B:C = E:F and the definition of same ratio with equimultiples nB, nE and mC, mF: since mC > nB (i.e., nB < mC), it follows that nE < mF, that is, mF > nE. [D5.5]

**Step 20.** From Step 18 we have nE >= mD, and from Step 19 we have mF > nE. Therefore mF > mD.

**Step 21.** Since mF and mD are equimultiples of F and D respectively, by Proposition 5.15 we have F:D = mF:mD. Applying the definition of same ratio with unit equimultiples, mF > mD implies F > D, that is, D < F. Therefore when A < C, we conclude D < F. [5.15, D5.5]

**Step 22.** We have shown all three cases: if A > C then D > F; if A = C then D = F; and if A < C then D < F. This is what was to be proved.

**USED:** 5.11, 5.13, 5.15, 5.7, 5.8, D5.17, D5.5, D5.7
**Human refs (from References field):** 5.10, 5.13, 5.8
**Jaccard:** 0.222 — AI adds ['5.11', '5.15', '5.7', 'D5.17', 'D5.5', 'D5.7']; Human adds ['5.10']

## Proposition 5.21
**Statement:** If there be three magnitudes, and others equal to them in multitude, which taken two and two together are in the same ratio, and the proportion of them be perturbed, then, if ex aequali the first magnitude is greater than the third, the fourth will also be greater than the sixth; if equal, equal; and if less, less.

**Step 1.** Let A, B, C be three magnitudes and D, E, F be three others equal to them in multitude, and let the proportion of them be perturbed, so that A : B :: E : F and B : C :: D : E [D5.18].

**Step 2.** We must show: if A > C then D > F; if A = C then D = F; if A < C then D < F.

**Step 3.** From B : C :: D : E, we derive that C : B :: E : D. This follows from the definition of same ratio [D5.5] and the definition of inverse ratio [D5.13]: since B : C :: D : E means that for all equimultiples mB and nC, mB exceeds, equals, or falls short of nC precisely when mD exceeds, equals, or falls short of nE, it follows that for all equimultiples mC and nB, mC exceeds, equals, or falls short of nB precisely when mE exceeds, equals, or falls short of nD, which is exactly C : B :: E : D.

**Step 4.** Case I: Suppose A > C. Since A > C, the ratio A : B is greater than the ratio C : B [5.8]. Since A : B :: E : F, by 5.13 applied to E : F :: A : B and A : B > C : B, we conclude E : F > C : B. But C : B :: E : D (Step 3), so again by 5.13, E : D has the same ratio as C : B, and since E : F > C : B :: E : D, we have E : F > E : D. Since E has a greater ratio to F than it has to D, by 5.10 (that to which the same has a greater ratio is less), F < D, that is, D > F.

**Step 5.** Case II: Suppose A = C. Since A and C are equal, A : B :: C : B [5.7]. Since A : B :: E : F, by 5.11 (transitivity of same ratio), E : F :: C : B. But C : B :: E : D (Step 3), so by 5.11 again, E : F :: E : D. Since E has the same ratio to F as it has to D, by 5.9 (magnitudes to which the same has the same ratio are equal), D = F.

**Step 6.** Case III: Suppose A < C. Since A < C, the ratio C : B is greater than the ratio A : B [5.8]. Since A : B :: E : F, we have C : B > E : F. But C : B :: E : D (Step 3), so by 5.13 applied to E : D :: C : B and C : B > E : F, we conclude E : D > E : F. Since E has a greater ratio to D than it has to F, by 5.10, D < F.

**Step 7.** Therefore, in a perturbed proportion of three magnitudes and three others, if ex aequali the first is greater than the third, the fourth is also greater than the sixth; if equal, equal; and if less, less. Q.E.D.

**USED:** 5.10, 5.11, 5.13, 5.7, 5.8, 5.9, D5.13, D5.18, D5.5
**Human refs (from References field):** 5.10, 5.13, 5.8
**Jaccard:** 0.333 — AI adds ['5.11', '5.7', '5.9', 'D5.13', 'D5.18', 'D5.5']

## Proposition 5.22
**Statement:** If there be any number of magnitudes whatever, and others equal to them in multitude, which taken two and two together are in the same ratio, they will also be in the same ratio ex aequali.

**Step 1.** We first prove the result for three magnitudes. Let A, B, C be magnitudes and D, E, F be others equal to them in multitude, such that A:B = D:E and B:C = E:F. We shall show that A:C = D:F (the ratio ex aequali, per D5.17).

**Step 2.** Take any equimultiples whatever G and H of A and D respectively, and take any equimultiples whatever K and L of C and F respectively. We must show that if G > K then H > L, if G = K then H = L, and if G < K then H < L, for then A:C = D:F by D5.5.

**Step 3.** Take any equimultiples whatever M and N of B and E respectively.

**Step 4.** Since A:B = D:E (given), by 5.4 any equimultiples of A and D have the same ratio to any equimultiples of B and E. Therefore G:M = H:N (where G, H are equimultiples of A, D and M, N are equimultiples of B, E).

**Step 5.** Since B:C = E:F (given), by 5.4 any equimultiples of B and E have the same ratio to any equimultiples of C and F. Therefore M:K = N:L (where M, N are equimultiples of B, E and K, L are equimultiples of C, F).

**Step 6.** Now G, M, K are three magnitudes and H, N, L are three others equal to them in multitude. We have shown that G:M = H:N (Step 4) and M:K = N:L (Step 5), so taken two and two they are in the same ratio. By 5.20, if ex aequali G > K then H > L; if G = K then H = L; and if G < K then H < L.

**Step 7.** Since G, H are arbitrary equimultiples of A, D and K, L are arbitrary equimultiples of C, F, and in every case G exceeds, equals, or falls short of K precisely when H exceeds, equals, or falls short of L, it follows by D5.5 that A:C = D:F. This is the ratio ex aequali for three magnitudes (D5.17).

**Step 8.** Now we prove the general case. Let A1, A2, ..., An be any number of magnitudes (n greater than or equal to 3) and B1, B2, ..., Bn be others equal to them in multitude, such that for each consecutive pair A_i:A_{i+1} = B_i:B_{i+1}. We show A1:An = B1:Bn by induction on n.

**Step 9.** The base case n = 3 has been established in Steps 1 through 7.

**Step 10.** For the inductive step, suppose the result holds for any sequence of n-1 magnitudes. Given n magnitudes A1, ..., An with the stated ratio conditions, consider the first n-1 magnitudes A1, ..., A_{n-1} and B1, ..., B_{n-1}. These satisfy A_i:A_{i+1} = B_i:B_{i+1} for i = 1, ..., n-2. By the inductive hypothesis, A1:A_{n-1} = B1:B_{n-1}.

**Step 11.** We also have A_{n-1}:An = B_{n-1}:Bn (given). Now A1, A_{n-1}, An are three magnitudes and B1, B_{n-1}, Bn are three others, with A1:A_{n-1} = B1:B_{n-1} (Step 10) and A_{n-1}:An = B_{n-1}:Bn (given). By the three-magnitude case (Steps 1-7), A1:An = B1:Bn.

**Step 12.** Therefore, by induction, for any number of magnitudes whatever, and others equal to them in multitude, which taken two and two together are in the same ratio, the extreme terms are also in the same ratio ex aequali (D5.17). Q.E.D.

**USED:** 5.20, 5.4, D5.17, D5.5
**Human refs (from References field):** 5.20, 5.4, D5.5
**Jaccard:** 0.750 — AI adds ['D5.17']

## Proposition 5.23
**Statement:** If there be three magnitudes, and others equal to them in multitude, which taken two and two together are in the same ratio, and the proportion of them be perturbed, they will also be in the same ratio ex aequali.

**Step 1.** Let A, B, C be three magnitudes and D, E, F be others equal to them in multitude, which taken two and two are in the same ratio with the proportion perturbed. That is, A:B = E:F and B:C = D:E. We are to prove that A:C = D:F (the ratio ex aequali).

**Step 2.** Take arbitrary equimultiples: let G = m*A, H = m*D, K = m*E be equimultiples of A, D, E respectively by any multiplier m. Let L = n*B, M = n*C, N = n*F be equimultiples of B, C, F respectively by any multiplier n.

**Step 3.** Since A:B = E:F (given), by Proposition 5.4 (taking m-multiples of the first and third, and n-multiples of the second and fourth), we have m*A : n*B = m*E : n*F, that is, G:L = K:N.

**Step 4.** Since B:C = D:E (given), by Proposition 5.15 (equimultiples have the same ratio as the magnitudes themselves), n*B : n*C = B:C and m*D : m*E = D:E. Since B:C = D:E, by Proposition 5.11 (ratios equal to the same ratio are equal to one another), we conclude n*B : n*C = m*D : m*E, that is, L:M = H:K.

**Step 5.** Now consider the three magnitudes G, L, M (that is, m*A, n*B, n*C) and the three magnitudes H, K, N (that is, m*D, m*E, n*F). From Step 3, G:L = K:N, which says the ratio of the first to the second among the first magnitudes equals the ratio of the second to the third among the second magnitudes. From Step 4, L:M = H:K, which says the ratio of the second to the third among the first magnitudes equals the ratio of the first to the second among the second magnitudes. By Definition 5.18, these six magnitudes are in perturbed proportion.

**Step 6.** By Proposition 5.21 (for three magnitudes in perturbed proportion): if ex aequali G is greater than M, then H is greater than N; if G equals M, then H equals N; and if G is less than M, then H is less than N. That is: if m*A > n*C then m*D > n*F; if m*A = n*C then m*D = n*F; and if m*A < n*C then m*D < n*F.

**Step 7.** Since m and n are arbitrary equimultiples, by Definition 5.5 (the definition of same ratio), A:C = D:F. By Definition 5.17 (ratio ex aequali), this is the ratio of the extreme terms, which is what was to be proved. Therefore, if there be three magnitudes and others equal to them in multitude, which taken two and two together are in the same ratio and the proportion of them be perturbed, they will also be in the same ratio ex aequali. Q.E.D.

**USED:** 5.11, 5.15, 5.21, 5.4, D5.17, D5.18, D5.5
**Human refs (from References field):** 5.11, 5.15, 5.16, 5.21
**Jaccard:** 0.375 — AI adds ['5.4', 'D5.17', 'D5.18', 'D5.5']; Human adds ['5.16']

## Proposition 5.24
**Statement:** If a first magnitude have to a second the same ratio as a third has to a fourth, and also a fifth have to the second the same ratio as a sixth to the fourth, the first and fifth added together will have to the second the same ratio as the third and sixth have to the fourth.

**Step 1.** Let A, B, C, D, E, F be magnitudes such that A:B = C:D and E:B = F:D. We are to prove that (A+E):B = (C+F):D.

**Step 2.** Since E:B = F:D, then by inversion B:E = D:F. For if E:B = F:D, then by D5.5, for any equimultiples mE, mF of E, F and any equimultiples nB, nD of B, D, we have mE > nB iff mF > nD, mE = nB iff mF = nD, and mE < nB iff mF < nD. Equivalently, nB > mE iff nD > mF, nB = mE iff nD = mF, and nB < mE iff nD < mF. Since n and m range over all positive integers, this establishes B:E = D:F by D5.5 (with D5.13, the definition of inverse ratio).

**Step 3.** Now we have A:B = C:D and B:E = D:F. Applying 5.22 (ex aequali) to the chain A:B:E on one side and C:D:F on the other — since A:B = C:D and B:E = D:F — we conclude A:E = C:F.

**Step 4.** From A:E = C:F, we apply 5.18 (if magnitudes be proportional separando, they will also be proportional componendo). Viewing A:E = C:F as the separated form, the composed form gives (A+E):E = (C+F):F.

**Step 5.** We now have two proportions: (A+E):E = (C+F):F (from Step 4) and E:B = F:D (given). Applying 5.22 (ex aequali) to the chain (A+E):E:B on one side and (C+F):F:D on the other — since (A+E):E = (C+F):F and E:B = F:D — we conclude (A+E):B = (C+F):D.

**Step 6.** Therefore, if a first magnitude have to a second the same ratio as a third has to a fourth, and also a fifth have to the second the same ratio as a sixth to the fourth, then the first and fifth added together have to the second the same ratio as the third and sixth have to the fourth. Q.E.D.

**USED:** 5.18, 5.22, D5.13, D5.5
**Human refs (from References field):** 5.18, 5.22
**Jaccard:** 0.500 — AI adds ['D5.13', 'D5.5']

## Proposition 5.25
**Statement:** If four magnitudes be proportional, the greatest and the least are greater than the remaining two.

**Step 1.** Let A, B, C, D be four magnitudes such that A : B :: C : D, with A the greatest and D the least. We are to prove that A + D > B + C.

**Step 2.** Since A : B :: C : D and A is the greatest of the four magnitudes, we have in particular A > C (since A is the greatest). By Proposition 5.14, since the first magnitude A is greater than the third magnitude C, the second magnitude B is greater than the fourth magnitude D. [5.14]

**Step 3.** Since A : B :: C : D and A is the greatest, we also have A > B. By Proposition 5.14 again, since A : B :: C : D and A (first) is greater than C (third), we already established B > D. But we also need: since A > B, applying 5.14 to the alternate proportion. By Proposition 5.16, since A : B :: C : D, we have alternately A : C :: B : D. Now since A > B (A is greatest), by Proposition 5.14 applied to A : C :: B : D (first A greater than third B), the second C is greater than the fourth D. [5.16, 5.14]

**Step 4.** Since A > B (A is greatest), there exists a magnitude G such that A = B + G, that is, G is the excess of A over B. Since C > D (established in Step 3), there exists a magnitude H such that C = D + H, that is, H is the excess of C over D.

**Step 5.** Since A : B :: C : D and A > B (so that the antecedent exceeds the consequent), by Proposition 5.17 (separando), (A - B) : B :: (C - D) : D. That is, G : B :: H : D. [5.17]

**Step 6.** We have shown that B > D (Step 2). Now from the proportion G : B :: H : D, we apply the full trichotomy of Proposition 5.14. Suppose for contradiction that G were less than H: then by 5.14 (if first is less than third, second is less than fourth), B would be less than D. But B > D, a contradiction. Suppose G were equal to H: then by 5.14, B would equal D. But B > D, again a contradiction. Therefore G > H, that is, A - B > C - D. [5.14]

**Step 7.** From A - B > C - D, adding B + D to both sides (by Common Notion 2, adding equals to unequals preserves the inequality, and by the general principle that if X > Y then X + Z > Y + Z), we obtain (A - B) + B + D > (C - D) + B + D, that is, A + D > B + C. [CN2]

**Step 8.** Therefore, if four magnitudes be proportional, the greatest and the least together are greater than the remaining two together. Q.E.D.

**USED:** 5.14, 5.16, 5.17, CN2
**Human refs (from References field):** 5.19
**Jaccard:** 0.000 — AI adds ['5.14', '5.16', '5.17', 'CN2']; Human adds ['5.19']
