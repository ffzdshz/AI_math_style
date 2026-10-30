# Book 7 of Euclid's Elements — Step-by-Step AI Proofs (Run C)

## Proposition 7.1
**Statement:** Two unequal numbers being set out, and the less being continually subtracted in turn from the greater, if the number which is left never measures the one before it until an unit is left, the original numbers will be prime to one another.

**Step 1.** Let A and B be two unequal numbers such that when the less is continually subtracted from the greater in turn, the number which is left never measures the one before it until a unit is left. We must prove that A and B are prime to one another.

**Step 2.** Suppose, for the sake of contradiction, that A and B are not prime to one another. Then by D7.12, they are not measured by a unit alone as a common measure. Hence by D7.14, some number C, which is greater than a unit, measures both A and B.

**Step 3.** Since C measures A and C measures B, we may assume without loss of generality that A > B (if B > A, relabel). Because C measures B, B is a multiple of C by D7.5, so B = p * C for some number p, by D7.15. Similarly, C measures A, so A = q * C for some number q.

**Step 4.** Consider the first step of the subtraction process. We subtract B from A as many times as possible. The remainder after subtracting B from A is A - B = q * C - p * C = (q - p) * C, by D7.15 and CN3. Since (q - p) is either a unit or a number (the process has not yet terminated at a unit, so A - B does not measure B or further remainders continue), C measures this remainder. If we subtract B multiple times, each intermediate result A - k*B = (q - k*p) * C is likewise measured by C, by repeated application of CN3 and D7.15. Hence C measures whatever remainder is left after B has been subtracted from A as many times as possible without the remainder becoming negative.

**Step 5.** Call this remainder R1. We have shown C measures R1. Now the process continues: we subtract R1 from B continually. By the same reasoning as in Step 4, since C measures both B and R1, C measures every remainder produced by subtracting R1 from B repeatedly. Call the final remainder R2. Then C measures R2.

**Step 6.** Continuing in this manner through every stage of the successive subtraction process, at each stage C measures both the number being subtracted and the number from which it is subtracted, and therefore C measures the remainder at each step, by the same argument using D7.5, D7.15, and CN3.

**Step 7.** By hypothesis, this process of continual subtraction terminates when a unit is left. Therefore C must measure this unit. But by D7.1, a unit is that by which each thing is called one, and by D7.3, for C to measure the unit, C would have to be a part of the unit with the unit being a multiple of C. By D7.5, the unit would then be a multiple of C, meaning the unit equals some number times C. But C is greater than a unit (Step 2), so any multiple of C by a number (which is at least a unit, i.e., at least one) is at least C, which is greater than a unit. This means C cannot measure the unit. We have a contradiction.

**Step 8.** Since the assumption that A and B are not prime to one another leads to a contradiction, we conclude that A and B are prime to one another, which is what was to be proved. Q.E.D.

**USED:** CN3, CN5, D7.1, D7.12, D7.14, D7.15, D7.3, D7.5
**Human refs (from References field):** D7.12
**Jaccard:** 0.125 — AI adds ['CN3', 'CN5', 'D7.1', 'D7.14', 'D7.15', 'D7.3', 'D7.5']

## Proposition 7.2
**Statement:** Given two numbers not prime to one another, to find their greatest common measure.

**Step 1.** Let AB and CD be two numbers not prime to one another. It is required to find their greatest common measure. Since AB and CD are not prime to one another, by D7.12, some number E measures both AB and CD.

**Step 2.** Now CD either measures AB or it does not. If CD measures AB, then CD also measures itself. So CD is a common measure of AB and CD. CD is then the greatest common measure, since no number greater than CD can measure CD itself (by CN5, the whole is greater than the part, so any measure of CD is at most CD).

**Step 3.** Suppose CD does not measure AB. Then perform the successive subtraction (antenaresis): continually subtract the less from the greater. Since some number E measures both AB and CD, the process cannot reduce to a unit, for if it did, then by 7.1 the numbers AB and CD would be prime to one another, contradicting the hypothesis.

**Step 4.** Since the remainders are always positive numbers (by D7.2, multitudes composed of units) and each is strictly less than the preceding remainder (by CN5), and the process cannot reach a unit (Step 3), the process must terminate when some remainder exactly measures the one before it.

**Step 5.** Carry out the process: subtract CD from AB as many times as possible. Let the remainder be less than CD; call it FB (the part of AB left after removing multiples of CD). If FB measures CD, go to Step 6. If not, subtract FB from CD as many times as possible, leaving remainder GC less than FB. If GC measures FB, go to Step 6. Continue in this way. By Step 4, the process terminates at some stage where the last remainder exactly measures the one before it.

**Step 6.** Suppose the process terminates when GC measures FB. We claim GC is the greatest common measure of AB and CD. Since GC measures FB, and CD is composed of multiples of FB plus GC (and GC measures FB), GC measures CD. Now since GC measures both FB and CD, and AB is composed of multiples of CD plus FB, GC measures AB. Therefore GC is a common measure of AB and CD.

**Step 7.** Now we show GC is the greatest common measure. Let H be any common measure of AB and CD. Since H measures AB and H measures CD, and FB is the remainder when multiples of CD are subtracted from AB, H must also measure FB (for AB equals a multiple of CD plus FB, and H measures both AB and CD, so by CN3, H measures the remainder FB). Similarly, since H measures CD and H measures FB, and GC is the remainder when multiples of FB are subtracted from CD, H measures GC.

**Step 8.** Therefore every common measure H of AB and CD also measures GC. Since H measures GC, we have H is at most GC (by CN5, the whole is greater than the part, so a measure of GC cannot exceed GC). Therefore GC is the greatest common measure of AB and CD.

**Step 9.** Therefore, given two numbers not prime to one another, we have found their greatest common measure. Q.E.F.

**USED:** 7.1, CN3, CN5, D7.12, D7.2
**Human refs (from References field):** 7.1
**Jaccard:** 0.200 — AI adds ['CN3', 'CN5', 'D7.12', 'D7.2']

## Proposition 7.3
**Statement:** Given three numbers not prime to one another, to find their greatest common measure.

**Step 1.** Let A, B, C be three numbers not prime to one another. Since they are not prime to one another, some number greater than the unit measures all three [D7.12].

**Step 2.** Since A, B, C have a common measure greater than the unit, that common measure in particular measures both A and B. Therefore A and B are not prime to one another [D7.12].

**Step 3.** Since A and B are not prime to one another, by Proposition 7.2 we can find their greatest common measure. Let it be D. Then D measures both A and B [7.2].

**Step 4.** Now consider D and C. Any number that measures all three of A, B, C in particular measures A and B. By Proposition 7.2, any common measure of A and B also measures D. So any common measure of A, B, and C measures both D and C.

**Step 5.** Since A, B, C are not prime to one another, some number F greater than the unit measures all three. By Step 4, F measures both D and C. Therefore D and C are not prime to one another [D7.12].

**Step 6.** Case 1: Suppose D itself measures C. Then D measures each of A, B, and C. Now let G be any number that measures A, B, and C. Then G measures A and B, so by 7.2, G measures D. Since every common measure of A, B, C measures D, and D itself is a common measure of A, B, C, D is the greatest common measure of A, B, C.

**Step 7.** Case 2: Suppose D does not measure C. Since D and C are not prime to one another (Step 5), by Proposition 7.2 we can find their greatest common measure. Let it be E. Then E measures both D and C [7.2].

**Step 8.** Since E measures D, and D measures A and B (Step 3), E also measures A and B. Since E also measures C, E measures each of A, B, and C.

**Step 9.** Now let G be any number that measures A, B, and C. Since G measures A and B, by 7.2 G measures D. Since G measures both D and C, and E is the greatest common measure of D and C, by 7.2 G measures E.

**Step 10.** Since every common measure of A, B, C measures E (Step 9), and E itself is a common measure of A, B, C (Step 8), E is the greatest common measure of A, B, C.

**Step 11.** Therefore, given three numbers not prime to one another, their greatest common measure has been found: it is D if D measures C, and otherwise it is the greatest common measure of D and C. Q.E.F.

**USED:** 7.2, D7.12
**Human refs (from References field):** 7.2
**Jaccard:** 0.500 — AI adds ['D7.12']

## Proposition 7.4
**Statement:** Any number is either a part or parts of any number, the less of the greater.

**Step 1.** Let A and B be numbers with A less than B. We must show that A is either a part or parts of B.

**Step 2.** There are exactly two possibilities: either A measures B, or A does not measure B.

**Step 3.** Suppose A measures B. Then by Definition 7.3, A is a part of B, since a number is a part of a number, the less of the greater, when it measures the greater. In this case, A is a part of B.

**Step 4.** Now suppose A does not measure B. Then by Definition 7.4, A is parts of B, since a number is parts of another when it does not measure it. In this case, A is parts of B.

**Step 5.** Since these two cases — A measures B, or A does not measure B — are exhaustive and mutually exclusive, it follows that A is either a part or parts of B.

**Step 6.** Therefore, any number is either a part or parts of any number, the less of the greater. Q.E.D.

**USED:** D7.3, D7.4
**Human refs (from References field):** 7.2
**Jaccard:** 0.000 — AI adds ['D7.3', 'D7.4']; Human adds ['7.2']

## Proposition 7.5
**Statement:** If a number be a part of a number, and another be the same part of another, the sum will also be the same part of the sum that the one is of the one.

**Step 1.** Let A be a part of number B, and let C be the same part of number D. We must show that A + C is the same part of B + D that A is of B.

**Step 2.** Since A is a part of B, by Definition D7.3, A measures B. That is, there exists some number n such that B is made up of n copies of A. By Definition D7.5, B is a multiple of A, and by Definition D7.15, B equals A taken n times, so B = n * A.

**Step 3.** Since C is the same part of D that A is of B, C measures D the same number of times. That is, D is made up of n copies of C (the same n as in Step 2). By D7.5 and D7.15, D = n * C.

**Step 4.** From Step 2, B = n * A, and from Step 3, D = n * C. Adding equals to equals (CN2), we obtain B + D = n * A + n * C.

**Step 5.** But n * A + n * C equals n * (A + C), since taking A + C a total of n times is the same as taking A n times and C n times and combining them (by D7.15, multiplication is repeated addition, and the order of aggregation does not alter the sum, by CN2 applied iteratively).

**Step 6.** Therefore B + D = n * (A + C). By Definition D7.5, B + D is a multiple of A + C, being measured by A + C exactly n times. By Definition D7.3, A + C is a part of B + D.

**Step 7.** Since A + C measures B + D exactly n times, and A measures B exactly n times, A + C is the same part of B + D that A is of B. This is what was to be proved.

**USED:** CN2, D7.15, D7.3, D7.5
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['CN2', 'D7.15', 'D7.3', 'D7.5']

## Proposition 7.6
**Statement:** If a number be parts of a number, and another be the same parts of another, the sum will also be the same parts of the sum that the one is of the one.

**Step 1.** Let AB be parts of the number C, and let DE be the same parts of the number F. I say that AB + DE is the same parts of C + F that AB is of C.

**Step 2.** Since AB is the same parts of C that DE is of F, there are as many parts of C in AB as there are parts of F in DE. Divide AB into the parts of C, namely AG and GB, and divide DE into the parts of F, namely DH and HE. Then the multitude of the parts AG, GB equals the multitude of the parts DH, HE. [D7.3, D7.4]

**Step 3.** Since AG is the same part of C that DH is of F, by Proposition 7.5, the sum AG + DH is the same part of C + F that AG is of C. [7.5]

**Step 4.** For the same reason, since GB is the same part of C that HE is of F, by Proposition 7.5, the sum GB + HE is the same part of C + F that GB is of C. [7.5]

**Step 5.** Now AB + DE = (AG + DH) + (GB + HE). From Steps 3 and 4, AG + DH is the same part of C + F that AG is of C, and GB + HE is the same part of C + F that GB is of C. Since AG and GB are all the parts of C that make up AB, the corresponding sums AG + DH and GB + HE are the same parts of C + F that AG and GB respectively are of C.

**Step 6.** Therefore the total AB + DE is the same parts of C + F that AB is of C. That is, the sum is the same parts of the sum that the one is of the one. Q.E.D.

**USED:** 7.5, D7.3, D7.4
**Human refs (from References field):** 7.5
**Jaccard:** 0.333 — AI adds ['D7.3', 'D7.4']

## Proposition 7.7
**Statement:** If a number be that part of a number, which a number subtracted is of a number subtracted, the remainder will also be the same part of the remainder that the whole is of the whole.

**Step 1.** Let the number A be that part of the number BC which the number D subtracted is of the number E subtracted. We must show that the remainder (A minus D) is the same part of the remainder (BC minus E) that A is of BC.

**Step 2.** Since A is that part of BC which D is of E, let A be the 1/n-th part of BC for some number n. Then by Definition 7.3 and Definition 7.5, A measures BC, and BC is a multiple of A, so that BC equals n copies of A. Likewise, D is the 1/n-th part of E, so E equals n copies of D.

**Step 3.** Decompose BC into the n equal parts each equal to A. That is, let BC = A_1 + A_2 + ... + A_n, where each A_i equals A. Similarly decompose E into n equal parts each equal to D. That is, E = D_1 + D_2 + ... + D_n, where each D_i equals D.

**Step 4.** Since D is subtracted from A (and E is subtracted from BC, with E less than BC by Common Notion 5, as E is a part subtracted from the whole), we have D less than A. For each index i, since A_i equals A and D_i equals D, we may subtract D_i from A_i. By Common Notion 3, since A_i equals A_j and D_i equals D_j for all i and j, the remainders are all equal: A_i minus D_i equals A minus D for each i.

**Step 5.** Therefore, BC minus E equals (A_1 minus D_1) + (A_2 minus D_2) + ... + (A_n minus D_n). Each of these n terms equals A minus D, by Step 4.

**Step 6.** Hence BC minus E equals n copies of (A minus D). By Definition 7.3 and Definition 7.5, (A minus D) is the 1/n-th part of (BC minus E), which is the same part that A is of BC.

**Step 7.** Therefore, the remainder (A minus D) is the same part of the remainder (BC minus E) that the whole A is of the whole BC. Q.E.D.

**USED:** CN3, CN5, D7.3, D7.5
**Human refs (from References field):** 7.5
**Jaccard:** 0.000 — AI adds ['CN3', 'CN5', 'D7.3', 'D7.5']; Human adds ['7.5']

## Proposition 7.8
**Statement:** If a number be the same parts of a number that a number subtracted is of a number subtracted, the remainder will also be the same parts of the remainder that the whole is of the whole.

**Step 1.** Let AB be the same parts of CD that the subtracted number AE is of the subtracted number CF. We must show that the remainder EB is the same parts of the remainder FD that the whole AB is of the whole CD.

**Step 2.** Since AB is the same parts of CD that AE is of CF, there are as many parts of CD in AB as there are parts of CF in AE. Divide AB into parts equal to the parts of CD, namely AG and GB, and divide AE into parts equal to the parts of CF, namely AH and HE. The number of these parts is equal, so AG is the same part of CD that AH is of CF, and GB is the same part of CD that HE is of CF. [D7.4, D7.3]

**Step 3.** Since AG is the same part of CD that AH is of CF, and AH is subtracted from AG while CF is subtracted from CD (with AH being the same part of CF that AG is of CD), by Proposition 7.7 the remainder (AG minus AH) is the same part of the remainder FD that the whole AG is of the whole CD. [7.7]

**Step 4.** Similarly, since GB is the same part of CD that HE is of CF, by the same reasoning (Proposition 7.7), the remainder (GB minus HE) is the same part of the remainder FD that the whole GB is of the whole CD. [7.7]

**Step 5.** Now, the remainder EB equals AB minus AE. Since AB is composed of the parts AG and GB, and AE is composed of the parts AH and HE, the remainder EB equals (AG minus AH) plus (GB minus HE).

**Step 6.** From Steps 3 and 4, each of these partial remainders — (AG minus AH) and (GB minus HE) — is the same part of FD that the corresponding part of AB is of CD. That is, (AG minus AH) is the same part of FD that AG is of CD, and (GB minus HE) is the same part of FD that GB is of CD.

**Step 7.** Therefore the remainder EB is the same parts of the remainder FD that the whole AB is of the whole CD. For EB is composed of parts of FD in exactly the same way that AB is composed of parts of CD. [D7.4]

**Step 8.** Hence, if a number be the same parts of a number that a number subtracted is of a number subtracted, the remainder will also be the same parts of the remainder that the whole is of the whole. Q.E.D.

**USED:** 7.7, D7.3, D7.4
**Human refs (from References field):** 7.7
**Jaccard:** 0.333 — AI adds ['D7.3', 'D7.4']

## Proposition 7.9
**Statement:** If a number be a part of a number, and another be the same part of another, alternately also, whatever part or parts the first is of the third, the same part, or the same parts, will the second also be of the fourth.

**Step 1.** Let A be the same part of B that C is of D. We must show that whatever part or parts A is of C, the same part or the same parts B is of D.

**Step 2.** Since A is the same part of B that C is of D, by D7.3 and D7.20, A measures B and C measures D, and there exists some number n such that B is composed of n copies of A, and D is composed of n copies of C. That is, B = A + A + ... + A (n times) and D = C + C + ... + C (n times).

**Step 3.** By D7.3 and D7.4, A is either a part of C or parts of C.

**Step 4.** Case 1: Suppose A is a part of C. Then A is the (1/m)-th part of C for some number m, meaning that A measures C and C is composed of m copies of A. Now consider the n summands that compose B and D respectively. Each summand A of B is the same part (namely the 1/m-th part) of the corresponding summand C of D. By repeated application of 7.5 (which states that if a number is a part of a number and another is the same part of another, the sum is the same part of the sum), combining the first two copies: A + A is the same part of C + C that A is of C. Adding the third copy by 7.5 again: A + A + A is the same part of C + C + C that A is of C. Continuing in this manner for all n copies, we conclude that nA is the same part of nC that A is of C, that is, B is the same part of D that A is of C.

**Step 5.** Case 2: Suppose A is parts of C, that is, A does not measure C but A bears the relation of certain parts to C. Again, each summand A of B bears the same relation (the same parts) to the corresponding summand C of D. By repeated application of 7.6 (which states that if a number is the same parts of a number and another is the same parts of another, the sum is the same parts of the sum), combining all n copies as in Step 4, we conclude that nA is the same parts of nC that A is of C, that is, B is the same parts of D that A is of C.

**Step 6.** Therefore, in both cases, whatever part or parts A is of C, the same part or the same parts B is of D, which is what was to be proved.

**USED:** 7.5, 7.6, D7.20, D7.3, D7.4, D7.5
**Human refs (from References field):** 7.5, 7.6
**Jaccard:** 0.333 — AI adds ['D7.20', 'D7.3', 'D7.4', 'D7.5']

## Proposition 7.10
**Statement:** If a number be parts of a number, and another be the same parts of another, alternately also, whatever parts or part the first is of the third, the same parts or the same part will the second also be of the fourth.

**Step 1.** Let AB be the same parts of C that DE is of F. We must show that, alternately, whatever parts or part AB is of DE, the same parts or the same part C is of F.

**Step 2.** Since AB is the same parts of C that DE is of F, there are as many parts of C in AB as there are parts of F in DE (D7.4). Let AB be divided into the parts of C equal to AG, GB, and let DE be divided into the parts of F equal to DH, HE. Then the multitude of AG, GB is equal to the multitude of DH, HE.

**Step 3.** Since AG is the same part of C that DH is of F (each being one of the equal aliquot parts into which AB and DE were respectively divided), by Proposition 7.9, alternately, whatever part or parts AG is of DH, the same part or the same parts C is of F.

**Step 4.** For the same reason, whatever part or parts GB is of HE, the same part or the same parts C is of F (again by 7.9, since GB is the same part of C that HE is of F).

**Step 5.** Now, since the multitude of AG, GB equals the multitude of DH, HE (Step 2), whatever part or parts AG is of DH, the same part or parts GB is of HE. For AG equals GB and DH equals HE, being equal aliquot parts within AB and DE respectively.

**Step 6.** Since whatever part or parts AG is of DH, the same part or parts C is of F (Step 3), and whatever part or parts GB is of HE, the same part or parts C is of F (Step 4), therefore whatever parts or part the sum AG + GB is of the sum DH + HE, the same parts or part C is of F. This follows because the sums are assembled from equal corresponding components: by Proposition 7.5 if each component is a part, or by Proposition 7.6 if each component is parts.

**Step 7.** But AG + GB = AB and DH + HE = DE. Therefore whatever parts or part AB is of DE, the same parts or the same part C is of F (D7.3, D7.4).

**Step 8.** Therefore, if a number be parts of a number, and another be the same parts of another, alternately also, whatever parts or part the first is of the third, the same parts or the same part will the second also be of the fourth. Q.E.D.

**USED:** 7.5, 7.6, 7.9, D7.3, D7.4
**Human refs (from References field):** 7.5, 7.6, 7.9
**Jaccard:** 0.600 — AI adds ['D7.3', 'D7.4']

## Proposition 7.11
**Statement:** If, as whole is to whole, so is a number subtracted to a number subtracted, the remainder will also be to the remainder as whole to whole.

**Step 1.** Let AB and CD be numbers, and let AE be subtracted from AB and CF be subtracted from CD, such that AB is to CD as AE is to CF. We must show that the remainder EB is to the remainder FD as AB is to CD.

**Step 2.** Since AB is to CD as AE is to CF, by D7.20 (numbers are proportional when the first is the same part, the same parts, or the same multiple of the second that the third is of the fourth), AE is the same part or the same parts of CF that AB is of CD.

**Step 3.** By 7.4, any number is either a part or parts of any number, the less of the greater. So we consider two cases according to whether AE is a part of CF or parts of CF.

**Step 4.** Case 1: Suppose AE is a part of CF (D7.3). Then AB is the same part of CD. By 7.7, if a number be that part of a number which a number subtracted is of a number subtracted, the remainder will also be the same part of the remainder that the whole is of the whole. Therefore EB is the same part of FD that AB is of CD.

**Step 5.** Case 2: Suppose AE is parts of CF (D7.4). Then AB is the same parts of CD. By 7.8, if a number be the same parts of a number that a number subtracted is of a number subtracted, the remainder will also be the same parts of the remainder that the whole is of the whole. Therefore EB is the same parts of FD that AB is of CD.

**Step 6.** In both cases, EB bears to FD the same relation (the same part or the same parts) that AB bears to CD. Therefore by D7.20, the remainder EB is to the remainder FD as the whole AB is to the whole CD. Q.E.D.

**USED:** 7.4, 7.7, 7.8, D7.20, D7.3, D7.4
**Human refs (from References field):** 7.7, 7.8, D7.20
**Jaccard:** 0.500 — AI adds ['7.4', 'D7.3', 'D7.4']

## Proposition 7.12
**Statement:** If there be as many numbers as we please in proportion, then, as one of the antecedents is to one of the consequents, so are all the antecedents to all the consequents.

**Step 1.** Let there be as many numbers as we please in proportion: let A1, A2, ..., An be the antecedents and B1, B2, ..., Bn be the corresponding consequents, so that A1:B1 = A2:B2 = ... = An:Bn. We must show that A1:B1 = (A1 + A2 + ... + An):(B1 + B2 + ... + Bn).

**Step 2.** By Definition D7.20, since the numbers are proportional, A1 is the same part, or the same parts, of B1 that A2 is of B2, that A3 is of B3, and so on for each pair.

**Step 3.** By Proposition 7.4, A1 is either a part of B1, or parts of B1. We consider each case.

**Step 4.** Case 1: Suppose A1 is a part of B1. Then by D7.20, since all ratios are equal, A2 is the same part of B2, A3 is the same part of B3, and so on for each index through An and Bn.

**Step 5.** By Proposition 7.5, if a number is a part of a number and another is the same part of another, the sum is also the same part of the sum. Applying 7.5 to A1 and A2 (which are the same part of B1 and B2 respectively), we obtain that A1 + A2 is the same part of B1 + B2 that A1 is of B1.

**Step 6.** Applying 7.5 again, since A1 + A2 is the same part of B1 + B2 that A3 is of B3, we obtain that A1 + A2 + A3 is the same part of B1 + B2 + B3 that A1 is of B1. Continuing this process successively for each remaining pair (A4, B4), ..., (An, Bn), we conclude that A1 + A2 + ... + An is the same part of B1 + B2 + ... + Bn that A1 is of B1.

**Step 7.** Therefore, by D7.20, A1:B1 = (A1 + A2 + ... + An):(B1 + B2 + ... + Bn) in this case.

**Step 8.** Case 2: Suppose A1 is parts of B1. Then by D7.20, since all ratios are equal, A2 is the same parts of B2, A3 is the same parts of B3, and so on for each index through An and Bn.

**Step 9.** By Proposition 7.6, if a number is parts of a number and another is the same parts of another, the sum is also the same parts of the sum. Applying 7.6 to A1 and A2 (which are the same parts of B1 and B2 respectively), we obtain that A1 + A2 is the same parts of B1 + B2 that A1 is of B1.

**Step 10.** Applying 7.6 again, since A1 + A2 is the same parts of B1 + B2 that A3 is of B3, we obtain that A1 + A2 + A3 is the same parts of B1 + B2 + B3 that A1 is of B1. Continuing this process successively for each remaining pair (A4, B4), ..., (An, Bn), we conclude that A1 + A2 + ... + An is the same parts of B1 + B2 + ... + Bn that A1 is of B1.

**Step 11.** Therefore, by D7.20, A1:B1 = (A1 + A2 + ... + An):(B1 + B2 + ... + Bn) in this case as well.

**Step 12.** In both cases, as one of the antecedents (A1) is to one of the consequents (B1), so are all the antecedents (A1 + A2 + ... + An) to all the consequents (B1 + B2 + ... + Bn). Q.E.D.

**USED:** 7.4, 7.5, 7.6, D7.20
**Human refs (from References field):** 7.5, 7.6, D7.20
**Jaccard:** 0.750 — AI adds ['7.4']

## Proposition 7.13
**Statement:** If four numbers be proportional, they will also be proportional alternately.

**Step 1.** Let A, B, C, D be four numbers such that A:B :: C:D. By Definition D7.20, this means A is the same multiple, or the same part, or the same parts of B that C is of D. We must show that alternately A:C :: B:D.

**Step 2.** Case I: Suppose A is the same part of B that C is of D. Then by Proposition 7.9, alternately, whatever part or parts A is of C, the same part or the same parts is B of D. Therefore A:C :: B:D by D7.20.

**Step 3.** Case II: Suppose A is the same parts of B that C is of D. Then by Proposition 7.10, alternately, whatever parts or part A is of C, the same parts or the same part is B of D. Therefore A:C :: B:D by D7.20.

**Step 4.** Case III: Suppose A is the same multiple of B that C is of D. Then there exists a number n such that A equals n times B and C equals n times D. By Definition D7.5, B measures A, and D measures C. By Definition D7.3, B is a part of A, and D is a part of C. Moreover, B is the same part of A that D is of C, namely the one-nth part.

**Step 5.** Since B is the same part of A that D is of C, we may apply Proposition 7.9 to the numbers B, A, D, C: alternately, whatever part or parts B is of D, the same part or the same parts is A of C. Therefore B:D :: A:C, which is to say A:C :: B:D by D7.20.

**Step 6.** In all three cases, A:C :: B:D. Therefore, if four numbers be proportional, they will also be proportional alternately. Q.E.D.

**USED:** 7.10, 7.9, D7.20, D7.3, D7.5
**Human refs (from References field):** 7.10, D7.20
**Jaccard:** 0.400 — AI adds ['7.9', 'D7.3', 'D7.5']

## Proposition 7.14
**Statement:** If there be as many numbers as we please, and others equal to them in multitude, which taken two and two are in the same ratio, they will also be in the same ratio ex aequali.

**Step 1.** Let there be as many numbers as we please: A1, A2, ..., An, and others equal to them in multitude: B1, B2, ..., Bn, which taken two and two are in the same ratio, so that A1:A2 = B1:B2, A2:A3 = B2:B3, and so on up to A(n-1):An = B(n-1):Bn. We must show that A1:An = B1:Bn (ex aequali), that is, that A1 is the same part, parts, or multiple of An as B1 is of Bn [D5.17, D7.20].

**Step 2.** First consider the case of three numbers: let A, B, C and D, E, F be such that A:B = D:E and B:C = E:F. We must show A:C = D:F.

**Step 3.** Since A:B = D:E, by alternation [7.13] we have A:D = B:E.

**Step 4.** Since B:C = E:F, by alternation [7.13] we have B:E = C:F.

**Step 5.** From Steps 3 and 4, A:D = B:E and B:E = C:F. Since A:D equals B:E, and B:E equals C:F, we have A:D = C:F [CN1].

**Step 6.** Since A:D = C:F, by alternation [7.13] we have A:C = D:F. This establishes the result for the case of three numbers.

**Step 7.** Now consider the general case. Suppose the result holds for any collection of (n-1) numbers taken pairwise in the same ratio. Given A1, A2, ..., An and B1, B2, ..., Bn with A1:A2 = B1:B2, A2:A3 = B2:B3, ..., A(n-1):An = B(n-1):Bn, consider the subsequences A1, A2, ..., A(n-1) and B1, B2, ..., B(n-1).

**Step 8.** These (n-1) numbers taken two and two satisfy the same ratio conditions: A1:A2 = B1:B2, ..., A(n-2):A(n-1) = B(n-2):B(n-1). By the result for (n-1) numbers, A1:A(n-1) = B1:B(n-1).

**Step 9.** We also have A(n-1):An = B(n-1):Bn (given). So now we have three numbers A1, A(n-1), An and three numbers B1, B(n-1), Bn with A1:A(n-1) = B1:B(n-1) and A(n-1):An = B(n-1):Bn.

**Step 10.** By the result for three numbers established in Steps 2-6, we conclude A1:An = B1:Bn.

**Step 11.** Therefore, if there be as many numbers as we please, and others equal to them in multitude, which taken two and two are in the same ratio, they will also be in the same ratio ex aequali. Q.E.D.

**USED:** 7.13, CN1, D5.17, D7.20
**Human refs (from References field):** 7.13
**Jaccard:** 0.250 — AI adds ['CN1', 'D5.17', 'D7.20']

## Proposition 7.15
**Statement:** If an unit measure any number, and another number measure any other number the same number of times, alternately also, the unit will measure the third number the same number of times that the second measures the fourth.

**Step 1.** Let the unit A measure a number BC, and let another number D measure a number EF the same number of times that A measures BC. We must show that, alternately, A measures D the same number of times that BC measures EF.

**Step 2.** Since A measures BC some number of times, say n times, BC is n times A. Since A is a unit, BC equals n units. Likewise, since D measures EF n times, EF is n times D. [D7.1, D7.2, D7.15]

**Step 3.** Since A measures BC n times, A is the same part of BC that D is of EF (for D also measures EF n times). That is, A is the n-th part of BC, and D is the n-th part of EF. [D7.3]

**Step 4.** Therefore, by the definition of proportional numbers, since the first (A) is the same part of the second (BC) as the third (D) is of the fourth (EF), the four numbers A, BC, D, EF are proportional: A is to BC as D is to EF. [D7.20]

**Step 5.** Since A, BC, D, EF are four proportional numbers, by Proposition 7.13 they are also proportional alternately: A is to D as BC is to EF. [7.13]

**Step 6.** Since A is to D as BC is to EF, whatever part (or multiple, or parts) A is of D, BC is the same of EF. Now A is a unit, and D is a number, so A measures D a certain number of times, say m times. Then BC also measures EF m times. [D7.20]

**Step 7.** Therefore, alternately, the unit A measures D the same number of times that BC measures EF, which is what was to be proved.

**USED:** 7.13, D7.1, D7.15, D7.2, D7.20, D7.3
**Human refs (from References field):** 7.12
**Jaccard:** 0.000 — AI adds ['7.13', 'D7.1', 'D7.15', 'D7.2', 'D7.20', 'D7.3']; Human adds ['7.12']

## Proposition 7.16
**Statement:** If two numbers by multiplying one another make certain numbers, the numbers so produced will be equal to one another.

**Step 1.** Let A and B be two numbers, and let A by multiplying B make C, and B by multiplying A make D. We must show that C equals D.

**Step 2.** Since A multiplied B to make C, by the definition of multiplication (D7.15), B is added to itself as many times as there are units in A. That is, A measures C according to B, meaning B measures C as many times as there are units in A. Equivalently, the unit measures A the same number of times that B measures C.

**Step 3.** Since the unit measures A the same number of times that B measures C, by Proposition 7.15 (alternation involving units), alternately the unit measures B the same number of times that A measures C.

**Step 4.** Since B multiplied A to make D, by the definition of multiplication (D7.15), A is added to itself as many times as there are units in B. That is, the unit measures B the same number of times that A measures D.

**Step 5.** From Step 3, the unit measures B the same number of times that A measures C. From Step 4, the unit measures B the same number of times that A measures D. Therefore A measures both C and D the same number of times.

**Step 6.** Since A measures C and A measures D the same number of times, it follows that C equals D (for if A is contained in C exactly n times and in D exactly n times, then C = n times A = D).

**Step 7.** Therefore, if two numbers by multiplying one another make certain numbers, the numbers so produced are equal to one another. Q.E.D.

**USED:** 7.15, D7.15
**Human refs (from References field):** 7.15
**Jaccard:** 0.500 — AI adds ['D7.15']

## Proposition 7.17
**Statement:** If a number by multiplying two numbers make certain numbers, the numbers so produced will have the same ratio as the numbers multiplied.

**Step 1.** Let A be a number which by multiplying B makes D and by multiplying C makes E. We must show that B is to C as D is to E.

**Step 2.** Since A multiplies B to produce D, by Definition D7.15, D equals B added to itself as many times as there are units in A. That is, D is the sum of as many numbers each equal to B as there are units in A.

**Step 3.** Similarly, since A multiplies C to produce E, by Definition D7.15, E equals C added to itself as many times as there are units in A. That is, E is the sum of as many numbers each equal to C as there are units in A.

**Step 4.** We now have as many numbers equal to B as there are units in A, namely B, B, ..., B, and as many numbers equal to C as there are units in A, namely C, C, ..., C. Taking these pairwise, each B is to the corresponding C as B is to C; that is, all the pairs are in the same ratio B to C, by Definition D7.20.

**Step 5.** Since there are as many numbers as we please in proportion -- namely the pairs B, C taken as many times as there are units in A, with each antecedent B to each consequent C being in the same ratio -- by Proposition 7.12, as one of the antecedents is to one of the consequents, so are all the antecedents to all the consequents. That is, B is to C as the sum of all the B's is to the sum of all the C's.

**Step 6.** But the sum of all the B's is D (Step 2), and the sum of all the C's is E (Step 3). Therefore B is to C as D is to E, which is what was to be proved.

**USED:** 7.12, D7.15, D7.20
**Human refs (from References field):** 7.13, D7.20
**Jaccard:** 0.250 — AI adds ['7.12', 'D7.15']; Human adds ['7.13']

## Proposition 7.18
**Statement:** If two numbers by multiplying any number make certain numbers, the numbers so produced will have the same ratio as the multipliers.

**Step 1.** Let A and B be two numbers, and let C be any number. Let A multiplying C produce D, and let B multiplying C produce E. We are to show that A is to B as D is to E.

**Step 2.** Since A multiplying C produces D, by Definition 7.15, D equals C added to itself A times, that is, D = A * C. Likewise, since B multiplying C produces E, we have E = B * C.

**Step 3.** Now by Proposition 7.16, if two numbers multiply one another, the products are equal to one another. Therefore A multiplying C produces the same number as C multiplying A, so that D is also the number produced by C multiplying A. Similarly, B multiplying C produces the same number as C multiplying B, so that E is also the number produced by C multiplying B.

**Step 4.** Since C is a single number which by multiplying A produces D and by multiplying B produces E, by Proposition 7.17 the numbers so produced have the same ratio as the numbers multiplied. That is, D is to E as A is to B.

**Step 5.** Therefore, if two numbers by multiplying any number make certain numbers, the numbers so produced have the same ratio as the multipliers. Q.E.D.

**USED:** 7.16, 7.17, D7.15, D7.20
**Human refs (from References field):** 7.16, 7.17
**Jaccard:** 0.500 — AI adds ['D7.15', 'D7.20']

## Proposition 7.19
**Statement:** If four numbers be proportional, the number produced from the first and fourth will be equal to the number produced from the second and third; and, if the number produced from the first and fourth be equal to that produced from the second and third, the four numbers will be proportional.

**Step 1.** Let A, B, C, D be four numbers. We prove both directions of the proposition.

**(Forward direction):** Suppose A : B :: C : D.

**Step 2.** Since A and B multiplying D produce A*D and B*D respectively, by 7.18 we have A*D : B*D = A : B.

**Step 3.** Since A : B :: C : D by hypothesis, it follows that A*D : B*D = C : D.

**Step 4.** Since B multiplying C and D produces B*C and B*D respectively, by 7.17 we have B*C : B*D = C : D.

**Step 5.** From Steps 3 and 4, A*D : B*D = B*C : B*D, since both ratios equal C : D. By D7.20, since A*D is the same multiple, part, or parts of B*D as B*C is of B*D, it follows that A*D = B*C. That is, the number produced from the first and fourth equals the number produced from the second and third.

**(Converse direction):** Suppose A*D = B*C.

**Step 6.** Since B multiplying C and D produces B*C and B*D respectively, by 7.17 we have B*C : B*D = C : D.

**Step 7.** Since A*D = B*C, substituting gives A*D : B*D = C : D.

**Step 8.** Since A and B multiplying D produce A*D and B*D respectively, by 7.18 we have A*D : B*D = A : B.

**Step 9.** From Steps 7 and 8, A : B = C : D. Therefore the four numbers are proportional.

**Step 10.** Therefore, if four numbers be proportional, the number produced from the first and fourth equals that from the second and third; and conversely, if the products are equal, the four numbers are proportional. Q.E.D.

**USED:** 7.17, 7.18, D7.20
**Human refs (from References field):** 5.7, 5.9, 7.17, 7.18
**Jaccard:** 0.400 — AI adds ['D7.20']; Human adds ['5.7', '5.9']

## Proposition 7.20
**Statement:** The least numbers of those which have the same ratio with them measure those which have the same ratio the same number of times, the greater the greater and the less the less.

**Step 1.** Let A and B be numbers, and let C and D be the least numbers of those which have the same ratio with A and B, so that C:D = A:B. We must show that C measures A and D measures B, and that the number of times C measures A equals the number of times D measures B.

**Step 2.** First, C is not greater than A and D is not greater than B. For suppose C were greater than A. Since C:D = A:B, and C > A, if D were less than or equal to B, then a greater number would have to a number the same ratio as a lesser number has to one that is equal or greater, which is impossible. If D were also greater than B, then A and B would be numbers less than C and D having the same ratio C:D, contradicting the hypothesis that C and D are the least numbers in that ratio. Therefore C is not greater than A. By symmetric reasoning, D is not greater than B.

**Step 3.** If C equals A, then since C:D = A:B, we have A:D = A:B, so D = B. In this case C measures A once and D measures B once, and the proposition holds.

**Step 4.** Now suppose C is less than A (so that also D is less than B, from the proportion). We claim C measures A. Suppose for contradiction that C does not measure A. Then by the division algorithm, there exist a number q and a remainder R with 0 < R < C such that A = qC + R, where q is at least 1 (since C < A).

**Step 5.** Since C:D = A:B, by Proposition 7.19 the number produced from C and B equals the number produced from D and A, that is, CB = DA.

**Step 6.** From A = qC + R, we compute DA = D(qC + R) = qCD + DR. Since CB = DA, we have CB = qCD + DR. Subtracting qCD from both sides gives CB - qCD = DR, that is, C(B - qD) = DR.

**Step 7.** Let S = B - qD. We must verify that S is a positive number less than D. Since CB = DA and A = qC + R, we have CB = qCD + DR, so CS = DR. Since R > 0 and D > 0, we have CS > 0, so S > 0. Since R < C, we have DR < DC, so CS < DC, hence S < D. Thus S is a positive number less than D.

**Step 8.** From CS = DR, by Proposition 7.19 (converse part), the four numbers R, C, S, D are proportional: R:C = S:D. By Proposition 7.13 (alternate proportion), R:S = C:D.

**Step 9.** But R < C and S < D, so R and S are numbers less than C and D that have the same ratio as C:D. This contradicts the hypothesis that C and D are the least numbers having this ratio.

**Step 10.** Therefore the supposition is false, and C must measure A. Let A = eC for some number e.

**Step 11.** Since C:D = A:B, we have C:D = eC:B. By Proposition 7.17, since C multiplied by e gives eC = A and C multiplied by (B/D) would give CB/D, but more directly: from CB = DA (Step 5) and A = eC, we get CB = DeC, so B = eD. Therefore D measures B, and B = eD.

**Step 12.** Since A = eC and B = eD, C measures A exactly e times and D measures B exactly e times. Thus the least numbers C and D measure the numbers A and B having the same ratio the same number of times, the greater the greater and the less the less, which is what was to be proved.

**USED:** 7.13, 7.17, 7.19, 7.4, CN5, D7.20, D7.3
**Human refs (from References field):** 7.12, 7.13, 7.4, D7.20
**Jaccard:** 0.375 — AI adds ['7.17', '7.19', 'CN5', 'D7.3']; Human adds ['7.12']

## Proposition 7.21
**Statement:** Numbers prime to one another are the least of those which have the same ratio with them.

**Step 1.** Let A and B be numbers prime to one another. We must show that A and B are the least of those numbers which have the same ratio with them. [D7.12: numbers prime to one another are measured by a unit alone as a common measure.]

**Step 2.** Suppose, for the sake of argument, that A and B are not the least numbers having the ratio A:B. Then there exist numbers less than A and B that have the same ratio.

**Step 3.** Let E and F be the least numbers having the same ratio as A:B. By 7.20, the least numbers of those which have the same ratio measure those which have the same ratio the same number of times, the greater the greater and the less the less. Therefore E measures A and F measures B the same number of times. Let each measure its respective number m times, so that A = mE and B = mF.

**Step 4.** Since A = mE, the number m measures A (it measures A according to E). Since B = mF, the number m measures B (it measures B according to F). Therefore m is a common measure of A and B.

**Step 5.** But A and B are prime to one another, so by D7.12, a unit alone is their common measure. Therefore m = 1.

**Step 6.** Since m = 1, we have A = E and B = F. Therefore A and B are the least numbers of those which have the same ratio with them. Q.E.D.

**USED:** 7.20, D7.12
**Human refs (from References field):** 7.16, 7.20, D7.12
**Jaccard:** 0.667 — Human adds ['7.16']

## Proposition 7.22
**Statement:** The least numbers of those which have the same ratio with them are prime to one another.

**Step 1.** Let A and B be the least numbers of those which have the same ratio with them. We must show that A and B are prime to one another.

**Step 2.** Suppose, for the sake of contradiction, that A and B are not prime to one another. Then by Definition D7.12, there exists some number C greater than a unit that measures both A and B.

**Step 3.** Since C measures A, let C measure A according to the number D, so that C multiplied by D produces A (D7.15). Since C measures B, let C measure B according to the number E, so that C multiplied by E produces B (D7.15).

**Step 4.** Since C is greater than a unit and C multiplied by D equals A, the whole A is greater than D (CN5). Likewise, since C multiplied by E equals B, the whole B is greater than E (CN5). Therefore D is less than A and E is less than B.

**Step 5.** Now, since C by multiplying D makes A, and by multiplying E makes B, by Proposition 7.17, the numbers so produced have the same ratio as the numbers multiplied. That is, A is to B as D is to E.

**Step 6.** Therefore D and E are numbers less than A and B respectively, yet having the same ratio as A to B. This contradicts the hypothesis that A and B are the least numbers of those which have the same ratio with them, since D and E are smaller numbers in the same ratio.

**Step 7.** Therefore the supposition is false, and A and B must be prime to one another. Q.E.D.

**USED:** 7.17, CN5, D7.12, D7.15, D7.3
**Human refs (from References field):** 7.17, D7.15
**Jaccard:** 0.400 — AI adds ['CN5', 'D7.12', 'D7.3']

## Proposition 7.23
**Statement:** If two number be prime to one another, the number which measures the one of them will be prime to the remaining number.

**Step 1.** Let A and B be two numbers prime to one another, and let C be a number which measures A. I say that C and B are also prime to one another.

**Step 2.** Suppose, for the sake of contradiction, that C and B are not prime to one another. Then by definition [D7.12], they are not measured by a unit alone as a common measure, so there exists some number D, greater than a unit, which measures both C and B [D7.14].

**Step 3.** Since D measures C, and C measures A, it follows that D measures A. For since C measures A, there is a number such that A equals C taken that number of times [D7.3, D7.15]. And since D measures C, there is a number such that C equals D taken some number of times [D7.3, D7.15]. Therefore A equals D taken some number of times, which means D measures A.

**Step 4.** Thus D measures A (from Step 3), and D also measures B (from Step 2). Therefore D is a common measure of A and B that is greater than a unit.

**Step 5.** But A and B are prime to one another, meaning they are measured by a unit alone as a common measure [D7.12]. This contradicts the existence of D as a common measure greater than a unit.

**Step 6.** Therefore our supposition is false, and C and B are prime to one another [D7.12]. Q.E.D.

**USED:** D7.12, D7.14, D7.15, D7.3
**Human refs (from References field):** D7.12
**Jaccard:** 0.250 — AI adds ['D7.14', 'D7.15', 'D7.3']

## Proposition 7.24
**Statement:** If two numbers be prime to any number, their product also will be prime to the same.

**Step 1.** Let A and B be two numbers, each prime to a number C. We wish to show that the product A*B is also prime to C. [D7.12, D7.15]

**Step 2.** Suppose, for the sake of contradiction, that A*B is not prime to C. Then there exists some number D, greater than a unit, which measures both A*B and C. [D7.12, D7.1]

**Step 3.** Since D measures C, and A is prime to C, by Proposition 7.23, D is prime to A. [7.23]

**Step 4.** Since D measures C, and B is prime to C, by Proposition 7.23, D is prime to B. [7.23]

**Step 5.** Since D measures A*B, there exists a number K such that D*K = A*B. By the converse part of Proposition 7.19, since the product of D and K equals the product of A and B, the four numbers D, A, B, K are proportional, that is, D is to A as B is to K. [7.19]

**Step 6.** Since D is prime to A, by Proposition 7.21, D and A are the least numbers of those which have the same ratio with them. [7.21]

**Step 7.** Since D and A are the least numbers in their ratio, and B and K are in the same ratio as D and A, by Proposition 7.20, D measures B. [7.20]

**Step 8.** But D measures B means that D is a common measure of D and B, and since D is greater than a unit, D and B have a common measure greater than a unit. This contradicts Step 4, which established that D is prime to B, meaning that the only common measure of D and B is the unit. [D7.12]

**Step 9.** Therefore the assumption in Step 2 is false, and A*B is indeed prime to C. [D7.12]

**USED:** 7.19, 7.20, 7.21, 7.23, D7.1, D7.12, D7.15
**Human refs (from References field):** 7.16, 7.19, 7.20, 7.21, 7.23, D7.12, D7.15
**Jaccard:** 0.750 — AI adds ['D7.1']; Human adds ['7.16']

## Proposition 7.25
**Statement:** If two numbers be prime to one another, the product of one of them into itself will be prime to the remaining one.

**Step 1.** Let A and B be two numbers prime to one another. We are to show that A multiplied by A (that is, A*A) is prime to B.

**Step 2.** Since A and B are prime to one another, A is prime to B. [Given, D7.12]

**Step 3.** Consider A and A as two numbers, each of which is prime to B. The first A is prime to B by the hypothesis, and the second A is likewise prime to B by the same hypothesis.

**Step 4.** Since two numbers A and A are both prime to B, by Proposition 7.24, the product of A and A is also prime to B. [7.24]

**Step 5.** But the product of A into itself is A*A. Therefore A*A is prime to B.

**Step 6.** Hence, if two numbers be prime to one another, the product of one of them into itself is prime to the remaining one. Q.E.D.

**USED:** 7.24, D7.12
**Human refs (from References field):** 7.24
**Jaccard:** 0.500 — AI adds ['D7.12']

## Proposition 7.26
**Statement:** If two numbers be prime to two numbers, both to each, their products also will be prime to one another.

**Step 1.** Let A, B be two numbers prime to two numbers C, D, both to each; that is, let A be prime to C, A be prime to D, B be prime to C, and B be prime to D. We are to prove that the product A*B is prime to the product C*D.

**Step 2.** Since A is prime to C and A is prime to D, and C, D are two numbers each prime to A, by Proposition 7.24 (if two numbers be prime to any number, their product also will be prime to the same), the product C*D is prime to A. By Definition D7.12, numbers prime to one another are those measured by a unit alone as a common measure, so equivalently A is prime to C*D.

**Step 3.** Since B is prime to C and B is prime to D, by the same reasoning using Proposition 7.24, the product C*D is prime to B, and equivalently B is prime to C*D.

**Step 4.** Now A is prime to C*D and B is prime to C*D. Applying Proposition 7.24 again (with A and B both prime to the number C*D), the product A*B is prime to C*D.

**Step 5.** Therefore, if two numbers be prime to two numbers, both to each, their products also will be prime to one another. Q.E.D.

**USED:** 7.24, D7.12, D7.15
**Human refs (from References field):** 7.24
**Jaccard:** 0.333 — AI adds ['D7.12', 'D7.15']

## Proposition 7.27
**Statement:** If two numbers be prime to one another, and each by multiplying itself make a certain number, the products will be prime to one another; and, if the original numbers by multiplying the products make certain numbers, the latter will also be prime to one another [and this is always the case with the extremes].

**Step 1.** Let A and B be two numbers prime to one another. Let A multiplying itself make C, so that C = A * A. Let B multiplying itself make D, so that D = B * B. We must first show that C and D are prime to one another.

**Step 2.** Since A and B are prime to one another, we may apply Proposition 7.26, which states: if two numbers be prime to two numbers, both to each, their products also will be prime to one another. Taking the two pairs as (A, A) and (B, B), we need to verify that each element of the first pair is prime to each element of the second pair. Since A is prime to B by hypothesis, all four conditions (A prime to B, A prime to B, A prime to B, A prime to B) are satisfied. Therefore by 7.26, A * A is prime to B * B, that is, C is prime to D.

**Step 3.** Now let A multiplying C make E, so that E = A * C. Let B multiplying D make F, so that F = B * D. We must show that E and F are prime to one another.

**Step 4.** Since A and B are prime to one another, by Proposition 7.25, the product of A into itself, namely C, is prime to B. That is, C and B are prime to one another.

**Step 5.** Since A and B are prime to one another, by Proposition 7.25 applied with B and A, the product of B into itself, namely D, is prime to A. That is, A and D are prime to one another.

**Step 6.** We now apply Proposition 7.26 to the pairs (A, C) and (B, D). We must verify that each element of the first pair is prime to each element of the second pair: A is prime to B (given), A is prime to D (Step 5), C is prime to B (Step 4), and C is prime to D (Step 2). All four conditions are satisfied. Therefore by 7.26, A * C is prime to B * D, that is, E is prime to F.

**Step 7.** Therefore, if two numbers be prime to one another, their squares are prime to one another; and their cubes are prime to one another. By the same method, continuing to multiply by the original numbers and applying 7.25 and 7.26 at each stage, we can show that all successive powers are prime to one another. This is always the case with the extremes. Q.E.D.

**USED:** 7.25, 7.26
**Human refs (from References field):** 7.25, 7.26
**Jaccard:** 1.000 — Perfect match.

## Proposition 7.28
**Statement:** If two numbers be prime to one another, the sum will also be prime to each of them; and, if the sum of two numbers be prime to any one of them, the original numbers will also be prime to one another.

**Step 1.** Let A and B be two numbers. The proposition asserts two things: (i) if A and B are prime to one another, then A + B is also prime to each of them; and (ii) if A + B is prime to one of them, then A and B are prime to one another.

**Step 2.** (Part i) Suppose A and B are prime to one another [D7.12]. We must show that A + B is prime to A, and similarly to B.

**Step 3.** Assume for contradiction that A + B is not prime to A. Then there exists some number C greater than a unit which measures both A + B and A [D7.12, negated].

**Step 4.** Since C measures A, by Proposition 7.23 (if two numbers are prime to one another, any number measuring one of them is prime to the remaining number), C is prime to B [7.23].

**Step 5.** Since C measures A, there exists a number p such that A equals the product of C and p [D7.3, D7.15]. Since C measures A + B, there exists a number q such that A + B equals the product of C and q [D7.3, D7.15].

**Step 6.** Therefore B equals A + B minus A, which equals the product of C and q minus the product of C and p, which equals the product of C and (q minus p). Hence C measures B [D7.3, D7.15].

**Step 7.** But from Step 4, C is prime to B, meaning the only common measure of C and B is a unit [D7.12]. Since C measures both C (trivially) and B, C must be a common measure of C and B, whence C must equal a unit. This contradicts our assumption that C is greater than a unit.

**Step 8.** Therefore A + B is prime to A. By an entirely symmetric argument (exchanging the roles of A and B, and again applying 7.23), A + B is also prime to B.

**Step 9.** (Part ii) Now suppose that A + B is prime to A. We must show that A and B are prime to one another.

**Step 10.** Assume for contradiction that A and B are not prime to one another. Then there exists some number D greater than a unit which measures both A and B [D7.12, negated].

**Step 11.** Since D measures A, there exists a number m such that A equals the product of D and m [D7.3, D7.15]. Since D measures B, there exists a number n such that B equals the product of D and n [D7.3, D7.15].

**Step 12.** Therefore A + B equals the product of D and m plus the product of D and n, which equals the product of D and (m + n). Hence D measures A + B [D7.3, D7.15].

**Step 13.** Since D measures both A + B and A, D is a common measure of A + B and A with D greater than a unit. This contradicts the hypothesis that A + B is prime to A [D7.12].

**Step 14.** Therefore A and B are prime to one another. Q.E.D.

**USED:** 7.23, D7.12, D7.15, D7.3
**Human refs (from References field):** D7.12
**Jaccard:** 0.250 — AI adds ['7.23', 'D7.15', 'D7.3']

## Proposition 7.29
**Statement:** Any prime number is prime to any number which it does not measure.

**Step 1.** Let p be a prime number and let A be any number which p does not measure. We aim to show that p and A are prime to one another.

**Step 2.** Suppose, for the sake of contradiction, that p and A are not prime to one another. Then by Definition D7.12, there exists some number c, greater than a unit, which is a common measure of both p and A.

**Step 3.** Since c measures p, we consider what c can be. By Definition D7.11, a prime number is measured by a unit alone. Since p is prime, the only number that measures p is the unit. Therefore c must be a unit.

**Step 4.** But in Step 2 we required c to be greater than a unit (since p and A are assumed not prime to one another). This contradicts Step 3, which shows c is a unit.

**Step 5.** Therefore the assumption in Step 2 is false, and no number greater than a unit can be a common measure of p and A. Hence p and A are prime to one another by Definition D7.12. This is what was to be proved.

**USED:** D7.11, D7.12
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['D7.11', 'D7.12']

## Proposition 7.30
**Statement:** If two numbers by multiplying one another make some number, and any prime number measure the product, it will also measure one of the original numbers.

**Step 1.** Let A and B be two numbers, and let C = A * B be their product [D7.15]. Let P be a prime number that measures C.

**Step 2.** Either P measures A or P does not measure A.

**Step 3.** If P measures A, then P measures one of the original numbers and the conclusion holds.

**Step 4.** Suppose P does not measure A. Since P is a prime number [D7.11] and P does not measure A, by 7.29 (any prime number is prime to any number which it does not measure), P and A are prime to one another.

**Step 5.** Since P and A are prime to one another, by 7.21 (numbers prime to one another are the least of those which have the same ratio with them), P and A are the least numbers of those having the ratio P : A.

**Step 6.** Since P measures C, there exists a number K such that C = P * K [D7.15]. Therefore P * K = A * B.

**Step 7.** Since the product of P and K equals the product of A and B, by 7.19 (if the number produced from the first and fourth be equal to that produced from the second and third, the four numbers will be proportional), the four numbers P, A, B, K are proportional, that is, P : A = B : K.

**Step 8.** Since P and A are the least numbers of those having the ratio P : A [Step 5], and P : A = B : K [Step 7], by 7.20 (the least numbers of those which have the same ratio measure those which have the same ratio the same number of times, the greater the greater and the less the less), P measures B.

**Step 9.** Therefore, in either case, P measures one of the original numbers A or B. Q.E.D.

**USED:** 7.19, 7.20, 7.21, 7.29, D7.11, D7.15
**Human refs (from References field):** 7.19, 7.20, 7.21, 7.29, D7.15
**Jaccard:** 0.833 — AI adds ['D7.11']

## Proposition 7.31
**Statement:** Any composite number is measured by some prime number.

**Step 1.** Let A be a composite number. By Definition D7.13, since A is composite, it is measured by some number. Let B be a number that measures A, where B is not a unit.

**Step 2.** Now B is either prime or not prime. If B is prime, then the composite number A is measured by the prime number B, and the proposition is proved.

**Step 3.** Suppose B is not prime. Then B is composite (by D7.13, since it is greater than a unit and is measured by some number other than a unit). Let C be a number that measures B, where C is not a unit.

**Step 4.** Since C measures B and B measures A, C also measures A. For B measures A, so A is a multiple of B (D7.5); and C measures B, so B is a multiple of C (D7.5). Since B equals C taken some number of times and A equals B taken some number of times, A equals C taken some number of times, hence C measures A.

**Step 5.** If C is prime, then we have found a prime number C that measures the composite number A, and the proposition is proved.

**Step 6.** If C is not prime, then by the same reasoning as before, C is composite and is measured by some number D (not a unit), and D in turn measures A.

**Step 7.** Continuing in this manner, we obtain a decreasing sequence of numbers A > B > C > D > ..., each of which measures A, since each successive number is a proper divisor of the one before it (the divisor is less than the number it measures, because it is not a unit and not the number itself, by CN5, as the part is less than the whole). Each number in this sequence is greater than a unit.

**Step 8.** Since A is a finite multitude of units (D7.2), this decreasing sequence of numbers greater than a unit cannot continue indefinitely. Therefore, at some stage we reach a number that is prime.

**Step 9.** This prime number, by the chain of divisibility established above, measures A. Therefore any composite number is measured by some prime number. Q.E.D.

**USED:** CN5, D7.11, D7.13, D7.2, D7.5
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['CN5', 'D7.11', 'D7.13', 'D7.2', 'D7.5']

## Proposition 7.32
**Statement:** Any number either is prime or is measured by some prime number.

**Step 1.** Let A be any number. We must show that A is either prime or is measured by some prime number.

**Step 2.** Consider two exhaustive cases: either A is measured by a unit alone, or A is measured by some number other than a unit.

**Step 3.** Case 1: Suppose A is measured by a unit alone. Then by Definition 7.11, A is prime. The conclusion holds.

**Step 4.** Case 2: Suppose A is not measured by a unit alone. Then some number other than a unit measures A, so by Definition 7.13, A is composite.

**Step 5.** Since A is composite, by Proposition 7.31 (any composite number is measured by some prime number), there exists a prime number that measures A. The conclusion holds.

**Step 6.** Therefore, since the two cases are exhaustive, any number either is prime or is measured by some prime number. Q.E.D.

**USED:** 7.31, D7.11, D7.13
**Human refs (from References field):** 7.31
**Jaccard:** 0.333 — AI adds ['D7.11', 'D7.13']

## Proposition 7.33
**Statement:** Given as many numbers as we please, to find the least of those which have the same ratio with them.

**Step 1.** Let A, B, C be the given numbers (the argument extends to any quantity of numbers). We seek the least numbers having the same ratio as A, B, C.

**Step 2.** If A, B, C are measured by no common measure other than the unit, then A, B, C are themselves the least in their ratio. (The proof of minimality below, with D equal to 1, covers this case.)

**Step 3.** Suppose A, B, C do have a common measure greater than 1. By 7.3, find D, the greatest common measure of A, B, C. Then D measures each of A, B, C. Let D measure A the number E times, B the number F times, and C the number G times, so that A = DE, B = DF, and C = DG.

**Step 4.** Since D multiplying E produces A, and D multiplying F produces B, by 7.17 the ratio A to B equals the ratio E to F. Similarly, since D multiplying F produces B and D multiplying G produces C, by 7.17 the ratio B to C equals the ratio F to G. Therefore E, F, G have the same ratio as A, B, C [D7.20].

**Step 5.** I say that E, F, G are the least numbers having this ratio. First, I show that the greatest common measure of E, F, G is the unit. Suppose, for contradiction, that some number M greater than 1 measures each of E, F, G. Since M measures E and D measures E times M gives DM, we see that DM measures DE, that is, DM measures A. Likewise DM measures B and C. So DM is a common measure of A, B, C. But since M is greater than 1, the product DM is greater than D [CN5]. This contradicts D being the greatest common measure of A, B, C. Therefore no number greater than 1 measures all of E, F, G; their greatest common measure is the unit.

**Step 6.** Now suppose H, K, L are any numbers whatever such that H to K equals E to F and K to L equals F to G (that is, H, K, L are in the same ratio as E, F, G). I will show that H, K, L are multiples of E, F, G respectively.

**Step 7.** Since E to F equals H to K, by 7.20 the least numbers in the ratio E to F measure both E and H the same number of times, and F and K the same number of times. Let these least numbers be p and q. Then there exist numbers alpha and beta such that E equals alpha times p, F equals alpha times q, H equals beta times p, and K equals beta times q, where alpha equals E divided by p and beta equals H divided by p.

**Step 8.** Similarly, since F to G equals K to L, by 7.20 the least numbers in the ratio F to G measure both F and K, and G and L, the same number of times. Let these least numbers be r and s. Then there exist numbers gamma and delta such that F equals gamma times r, G equals gamma times s, K equals delta times r, and L equals delta times s.

**Step 9.** From Step 7, K equals beta times q. From Step 8, K equals delta times r. So beta times q equals delta times r. Similarly, from F equals alpha times q and F equals gamma times r, we get alpha times q equals gamma times r. Dividing, alpha over beta equals gamma over delta. That is, the ratio alpha to beta equals the ratio gamma to delta.

**Step 10.** By 7.20, let m and n be the least numbers in the ratio alpha to beta (which equals gamma to delta). Then m measures alpha and m measures gamma, and n measures beta and n measures delta, with alpha divided by m equal to beta divided by n.

**Step 11.** Since m measures alpha, and E equals alpha times p, it follows that m measures E. Since m measures alpha, and F equals alpha times q, it follows that m measures F. Since m measures gamma, and G equals gamma times s, it follows that m measures G. Therefore m is a common measure of E, F, G.

**Step 12.** But by Step 5, the greatest common measure of E, F, G is the unit. Since m is a common measure of E, F, G, m must equal 1.

**Step 13.** Since m equals 1 and the ratio alpha to beta equals m to n equals 1 to n, we have beta equals n times alpha. Therefore H equals beta times p equals n times alpha times p equals n times E. Similarly K equals beta times q equals n times alpha times q equals n times F. And since gamma over delta equals alpha over beta equals 1 over n, we get delta equals n times gamma, so L equals delta times s equals n times gamma times s equals n times G.

**Step 14.** Thus H equals nE, K equals nF, and L equals nG, where n is a positive integer no less than 1. Therefore H is not less than E, K is not less than F, and L is not less than G. Since this holds for any numbers H, K, L in the same ratio as E, F, G, the numbers E, F, G are the least of those having this ratio.

**Step 15.** Therefore, given numbers A, B, C, we have found E, F, G as the least numbers having the same ratio with them: divide each given number by their greatest common measure. Q.E.F.

**USED:** 7.17, 7.20, 7.3, CN5, D7.20
**Human refs (from References field):** 7.16, 7.19, 7.21, 7.3, D7.15, D7.20
**Jaccard:** 0.222 — AI adds ['7.17', '7.20', 'CN5']; Human adds ['7.16', '7.19', '7.21', 'D7.15']

## Proposition 7.34
**Statement:** Given two numbers, to find the least number which they measure.

**Step 1.** Let A and B be the two given numbers. We seek the least number E such that both A and B measure E.

**Step 2.** By Proposition 7.33, find the least numbers C and D which have the same ratio as A to B. That is, A : B = C : D, and C, D are the least such pair.

**Step 3.** By Proposition 7.20, since C and D are the least numbers of those having the same ratio as A to B, C measures A and D measures B the same number of times. Let each measure its corresponding number m times, so that A = m times C and B = m times D, for some number m.

**Step 4.** Let E be the number produced by multiplying A by D (Definition 7.15). Then E = A multiplied by D.

**Step 5.** Since A : B = C : D (from Step 2), these four numbers are proportional (Definition 7.20). Therefore by Proposition 7.19, the product of the first and fourth equals the product of the second and third, that is, A multiplied by D equals B multiplied by C. Hence E also equals B multiplied by C.

**Step 6.** Since E = A multiplied by D, it follows that A measures E (Definition 7.5), for E is a multiple of A. Since E = B multiplied by C (from Step 5), it follows that B measures E, for E is a multiple of B. Therefore E is a common multiple of A and B, that is, both A and B measure E.

**Step 7.** Now we show E is the least such number. Suppose for contradiction that there exists a number F less than E such that both A and B measure F. Since A measures F, let F = q times A for some number q. Since B measures F, let F = r times B for some number r.

**Step 8.** From Step 7, q times A = r times B, so A : B = r : q (the ratio holds since the products are equal). But A : B = C : D from Step 2, so C : D = r : q.

**Step 9.** By Proposition 7.20, since C and D are the least numbers having this ratio, C measures r and D measures q. In particular, since D measures q, we have q is at least as great as D (for D, being a number, is at least one unit, and any number measured by D is a multiple of D, hence at least D).

**Step 10.** Since q is at least D, and F = q times A, we have F is at least D times A. But D times A equals E (from Step 4). Therefore F is at least E, which contradicts the assumption that F is less than E.

**Step 11.** Therefore no number less than E is measured by both A and B, and hence E is the least number which A and B measure. This is what was to be found.

**USED:** 7.19, 7.20, 7.33, D7.15, D7.20, D7.5
**Human refs (from References field):** 7.16, 7.17, 7.19, 7.20, 7.21, 7.33, D7.15
**Jaccard:** 0.444 — AI adds ['D7.20', 'D7.5']; Human adds ['7.16', '7.17', '7.21']

## Proposition 7.35
**Statement:** If two numbers measure any number, the least number measured by them will also measure the same.

**Step 1.** Let A and B be two numbers, and let them both measure some number C. Let L be the least number measured by both A and B; such a number exists by Proposition 7.34. We must show that L also measures C.

**Step 2.** Since A measures L and A measures C, and B measures L and B measures C, L is a number measured by both A and B, and C is also measured by both A and B. Since L is the least number measured by both A and B (by 7.34), we have L is not greater than C. For if L were greater than C, then C would be a number measured by both A and B that is less than L, contradicting the minimality of L.

**Step 3.** If L equals C, then L measures C (as any number measures itself, being one times itself), and we are done.

**Step 4.** Suppose L is less than C. Since A measures both C and L, let C = A * n and L = A * m for some numbers n and m, where n > m (by Definition D7.5). Then C - L = A * (n - m), so A measures the remainder C - L. By the same reasoning, since B measures both C and L, B also measures C - L.

**Step 5.** Thus C - L is a positive number measured by both A and B. If C - L is less than L, then C - L is a number measured by both A and B that is less than L, contradicting the fact that L is the least such number (by 7.34). Therefore C - L is not less than L.

**Step 6.** If C - L equals L, then C = 2L, so L measures C, and we are done.

**Step 7.** If C - L is greater than L, we repeat the process: subtract L from C - L to obtain C - 2L. By the same argument as in Step 4, since A measures both C - L and L, A measures C - 2L, and similarly B measures C - 2L.

**Step 8.** We continue subtracting L repeatedly. At each stage, the remainder is measured by both A and B, and by the argument of Step 5, the remainder cannot be less than L (for that would contradict the minimality of L). Since C is finite and each subtraction reduces the remainder by L, this process must eventually yield a remainder equal to L, at which point the next subtraction gives zero. Therefore C is a sum of copies of L, which means L measures C (by Definition D7.5).

**Step 9.** Therefore, if two numbers measure any number, the least number measured by them also measures the same. Q.E.D.

**USED:** 7.34, D7.5
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['7.34', 'D7.5']

## Proposition 7.36
**Statement:** Given three numbers, to find the least number which they measure.

**Step 1.** Let A, B, C be the three given numbers. We must find the least number which they all measure.

**Step 2.** Take A and B, and by Proposition 7.34, find D, the least number which A and B measure. That is, A measures D and B measures D, and D is the least such number.

**Step 3.** Now take D and C, and again by Proposition 7.34, find E, the least number which D and C measure. That is, D measures E and C measures E, and E is the least such number.

**Step 4.** Since A measures D and D measures E, A also measures E. For if D = mA for some number m, and E = nD for some number n, then E = n(mA) = (nm)A, so A measures E. Similarly, since B measures D and D measures E, B also measures E. And C measures E directly by construction. Therefore A, B, and C all measure E.

**Step 5.** We now show that E is the least such number. Suppose, for the sake of contradiction, that there exists some number F less than E such that A, B, and C all measure F.

**Step 6.** Since A measures F and B measures F, and D is the least number measured by both A and B, then by Proposition 7.35, D also measures F.

**Step 7.** Since D measures F and C measures F, and E is the least number measured by both D and C, then by Proposition 7.35, E also measures F.

**Step 8.** But F is less than E. If E measures F, then E is a part of F, meaning F is a multiple of E, so F is at least as great as E. By Definition 7.5, F being a multiple of E means E measures F, requiring F to be no less than E. This contradicts the assumption that F is less than E.

**Step 9.** Therefore no number less than E is measured by all three of A, B, and C. Hence E is the least number which A, B, and C measure. Q.E.D.

**USED:** 7.34, 7.35, D7.5
**Human refs (from References field):** 7.34, 7.35
**Jaccard:** 0.667 — AI adds ['D7.5']

## Proposition 7.37
**Statement:** If a number be measured by any number, the number which is measured will have a part called by the same name as the measuring number.

**Step 1.** Let the number A measure the number B. We must show that B has a part called by the same name as A.

**Step 2.** Since A measures B, by Definition D7.15, A multiplied by some number C produces B. That is, B is the result of adding A to itself as many times as there are units in C, so A measures B according to the units in C.

**Step 3.** Now the unit measures C as many times as there are units in C (by D7.2, since C is a multitude composed of units). And A measures B the same number of times, namely according to the units in C (from Step 2).

**Step 4.** Therefore, by Proposition 7.15 (if a unit measures any number, and another number measures any other number the same number of times, then alternately the unit measures the third number the same number of times that the second measures the fourth), since the unit measures C the same number of times that A measures B, it follows alternately that the unit measures A the same number of times that C measures B.

**Step 5.** But the unit measures A according to the units in A (by D7.2). Therefore C measures B according to the units in A. This means that C, taken as many times as there are units in A, equals B.

**Step 6.** Since C measures B (Step 5), C is a part of B (by D7.3). Moreover, since C measures B exactly as many times as there are units in A, the part C is called by the same name as A: if A is three, then C is a third part of B; if A is five, then C is a fifth part, and so on.

**Step 7.** Therefore, if a number be measured by any number, the number which is measured has a part called by the same name as the measuring number. Q.E.D.

**USED:** 7.15, D7.15, D7.2, D7.3
**Human refs (from References field):** 7.15
**Jaccard:** 0.250 — AI adds ['D7.15', 'D7.2', 'D7.3']

## Proposition 7.38
**Statement:** If a number have any part whatever, it will be measured by a number called by the same name as the part.

**Step 1.** Let the number A have a part, and let the part be called by the same name as the number C. We must show that C measures A.

**Step 2.** Let B be the part of A that is called by the same name as C. Since B is a part of A called by the same name as C, by the definition of parts and their naming (D7.3, D7.15), B is a 1/C-th part of A. This means that the unit measures C the same number of times that B measures A.

**Step 3.** Since B is a 1/C-th part of A, B measures A, and the number of times B measures A equals C. In other words, B multiplied by C produces A, that is, B added to itself as many times as there are units in C yields A (D7.15, D7.3).

**Step 4.** Since B multiplied by C produces A, then by Proposition 7.16, C multiplied by B also produces A. That is, C added to itself as many times as there are units in B yields A.

**Step 5.** Since C multiplied by B produces A, C measures A (D7.3, D7.5). The number of times C measures A is B.

**Step 6.** Therefore, if a number have any part whatever, it will be measured by a number called by the same name as the part. Q.E.D.

**USED:** 7.16, D7.15, D7.3, D7.5
**Human refs (from References field):** 7.15
**Jaccard:** 0.000 — AI adds ['7.16', 'D7.15', 'D7.3', 'D7.5']; Human adds ['7.15']

## Proposition 7.39
**Statement:** To find the number which is the least that will have given parts.

**Step 1.** Let the given parts be a 1/A-th part, a 1/B-th part, and a 1/C-th part (the argument generalizes to any finite number of given parts). We seek the least number that has all these parts.

**Step 2.** By Proposition 7.36, find the least number L that is measured by each of A, B, and C. (For two given parts, apply 7.34 instead; for more than three, iterate using 7.34 and 7.35.)

**Step 3.** Since A measures L, by Proposition 7.37, the number L has a part called by the same name as A, that is, L has a 1/A-th part. Similarly, since B measures L, by 7.37 the number L has a 1/B-th part. And since C measures L, by 7.37 the number L has a 1/C-th part. Therefore L has all the given parts.

**Step 4.** We now show L is the least such number. Suppose for contradiction that some number M less than L also has a 1/A-th part, a 1/B-th part, and a 1/C-th part. By Proposition 7.38, since M has a 1/A-th part, the number A measures M. Likewise, since M has a 1/B-th part, B measures M, and since M has a 1/C-th part, C measures M.

**Step 5.** Thus A, B, and C all measure M. But L is the least number measured by A, B, and C (from Step 2). By Proposition 7.35, since A and B each measure M, the least number measured by A and B also measures M; iterating, L itself must measure M. But L measures M implies L is less than or equal to M (by Definition D7.5 and the nature of measurement), which contradicts M being less than L.

**Step 6.** Therefore no number less than L can have all the given parts, and L is the least number having the given parts, which is what was required to find.

**USED:** 7.34, 7.35, 7.36, 7.37, 7.38, D7.3, D7.5
**Human refs (from References field):** 7.36, 7.37, 7.38
**Jaccard:** 0.429 — AI adds ['7.34', '7.35', 'D7.3', 'D7.5']
