# Book 5 of Euclid's Elements — Step-by-Step AI Proofs (Run A)

## Proposition 5.1
**Statement:** If a magnitude be the same multiple of a magnitude that a part subtracted is of a part subtracted, the remainder will also be the same multiple of the remainder that the whole is of the whole.

**Step 1.** Let A and B be the whole magnitudes, and let C and D be the respective parts subtracted. Suppose A is the same multiple of B that C is of D. By the definition of a multiple, A consists of some number n of parts each equal to B, while C consists of the same number n of parts each equal to D. We use these equal constituent parts directly, without invoking a theorem about ratios. [D5.2]

**Step 2.** In each of the n parts of A equal to B, take away a part equal to D; this is possible since D is a part of B. Each remainder is equal to the remainder B − D, because equal magnitudes have been subtracted from equal magnitudes. Thus there are n remaining parts, each equal to B − D. [CN3]

**Step 3.** The parts taken away together equal C: both consist of n parts each equal to D, and repeated addition of equals gives equal wholes. Consequently, subtracting their total from A leaves a magnitude equal to A − C. But what remains after these removals is precisely the collection of the n remaining parts from Step 2. Hence A − C consists of n parts each equal to B − D. [CN2, CN3]

**Step 4.** Therefore B − D measures A − C exactly n times. By the definition of a multiple, A − C is the same multiple of B − D that A is of B, as required. [D5.2]

**USED:** CN2, CN3, D5.2
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['CN2', 'CN3', 'D5.2']

## Proposition 5.2
**Statement:** If a first magnitude be the same multiple of a second that a third is of a fourth, and a fifth also be the same multiple of the second that a sixth is of the fourth, the sum of the first and fifth will also be the same multiple of the second that the sum of the third and sixth is of the fourth.

**Step 1.** Denote the first through sixth magnitudes by A, B, C, D, E, F, respectively. Choose the direct route of counting measuring parts, since the hypotheses concern multiples rather than general ratios. By the definition of a multiple, A consists of some number m of parts each equal to B, while C consists of the same number m of parts each equal to D. Likewise, E consists of some number n of parts each equal to B, and F consists of the same number n of parts each equal to D. The numbers m and n need not be equal. [D5.2]

**Step 2.** Add the expressions for A and E as sums of their measuring parts. Since equals added to equals give equal wholes, A + E equals the sum of the m parts equal to B followed by the n parts equal to B: altogether m + n such parts. In precisely the same way, C + F equals the sum of m + n parts each equal to D. [CN2]

**Step 3.** Thus B measures A + E exactly as many times as D measures C + F. By the definition of a multiple, the sum of the first and fifth is therefore the same multiple of the second as the sum of the third and sixth is of the fourth, as required. [D5.2]

**USED:** CN2, D5.2
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['CN2', 'D5.2']

## Proposition 5.3
**Statement:** If a first magnitude be the same multiple of a second that a third is of a fourth, and if equimultiples be taken of the first and third, then also ex aequali the magnitudes taken will be equimultiples respectively, the one of the second and the other of the fourth.

**Step 1.** Let A be the same multiple of B that C is of D, and let E and F be equimultiples of A and C respectively. By the meaning of multiple, E consists of some number n of copies of A, and F consists of the same number n of copies of C. Thus it suffices to show that these two sums are equimultiples of B and D. [D5.2]

**Step 2.** We use successive addition, since Proposition 5.2 directly preserves the required relation. The first pair of summands, A and C, are equimultiples of B and D by hypothesis. Whenever the sums of the first k copies are equimultiples of B and D, adding one further A to the first sum and one further C to the second gives sums that are again equimultiples of B and D: this is precisely Proposition 5.2, applied to the two partial sums and the additional pair A, C. [5.2]

**Step 3.** Continuing through all n pairs of summands, the resulting sums E and F are therefore equimultiples of B and D respectively. Hence, ex aequali, the magnitudes taken are the same multiple of the second and fourth magnitudes, as required. [5.2, D5.2]

**USED:** 5.2, D5.2
**Human refs (from References field):** 5.2
**Jaccard:** 0.500 — AI adds ['D5.2']

## Proposition 5.4
**Statement:** If a first magnitude have to a second the same ratio as a third to a fourth, any equimultiples whatever of the first and third will also have the same ratio to any equimultiples whatever of the second and fourth respectively, taken in corresponding order.

**Step 1.** Let A have to B the same ratio as C has to D. Let E and G be any equimultiples of A and C, and let F and H be any equimultiples of B and D, respectively. We shall prove that E has to F the same ratio as G has to H. We choose the direct defining test for equality of ratios, since it concerns precisely such arbitrary equimultiples. [D5.5]

**Step 2.** Take any equimultiples K and M of E and G, and any equimultiples L and N of F and H, respectively. Since E and G are equimultiples of A and C, Proposition 5.3 shows that K and M are equimultiples of A and C. Likewise, L and N are equimultiples of B and D. [5.3]

**Step 3.** Since A has to B the same ratio as C has to D, these equimultiples satisfy the defining condition: K and M alike exceed, are alike equal to, or alike fall short of L and N, respectively. Thus the comparison of K with L agrees with that of M with N. [D5.5]

**Step 4.** The equimultiples K, M and L, N were arbitrary. Therefore E has to F the same ratio as G has to H. Since E, G and F, H were themselves any equimultiples of the original magnitudes in corresponding order, the proposition follows. [D5.5]

**USED:** 5.3, D5.5
**Human refs (from References field):** 5.3, D5.5
**Jaccard:** 1.000 — Perfect match.

## Proposition 5.5
**Statement:** If a magnitude be the same multiple of a magnitude that a part subtracted is of a part subtracted, the remainder will also be the same multiple of the remainder that the whole is of the whole.

**Step 1.** Let A and B be the whole magnitudes, and let C and D be the respective parts subtracted. Suppose A is the same multiple of B that C is of D. By the definition of a multiple, there is a common number n of copies such that A consists of n copies of B and C consists of n copies of D. We use these equal parts directly, followed by cancellation. [D5.2]

**Step 2.** Write R = A − C and S = B − D, so that B consists of D together with S. In each of the n copies of B making up A, distinguish the corresponding copy of D and the remaining copy of S. Adding these decompositions, the n copies of D together equal C, while the remaining pieces together equal a magnitude T consisting of n copies of S. Thus A = C + T. This follows by repeated addition of equals. [D5.2, CN2]

**Step 3.** Subtract C from the equal magnitudes A and C + T. The remainders are equal; hence R = A − C = T. [CN3]

**Step 4.** Since T consists of n copies of S, the equality R = T shows that R is n times S. Therefore A − C is the same multiple of B − D that A is of B: the remainder is the same multiple of the remainder that the whole is of the whole. [D5.2]

**USED:** CN2, CN3, D5.2
**Human refs (from References field):** 5.1
**Jaccard:** 0.000 — AI adds ['CN2', 'CN3', 'D5.2']; Human adds ['5.1']

## Proposition 5.6
**Statement:** If two magnitudes be equimultiples of two magnitudes, and any magnitudes subtracted from them be equimultiples of the same, the remainders also are either equal to the same or equimultiples of them.

**Step 1.** Let X and Y be equimultiples of A and B respectively, and let U and V, subtracted from X and Y, also be equimultiples of A and B respectively. Write R and S for the remainders. We use repeated measurement directly, since it is the defining property of a multiple: X consists of m copies of A and Y of m copies of B, while U consists of n copies of A and V of n copies of B. [D5.2]

**Step 2.** Since U and V are parts removed with remainders left, each is less than its respective whole. Thus n is less than m: n copies cannot exhaust or exceed the m copies constituting the whole. Removing the first n copies from each of the two lists therefore leaves the same positive number k of copies in each. [D5.2, CN5]

**Step 3.** The first n copies of A together equal U. Subtracting these from the m-copy representation of X leaves an aggregate equal to R, by subtraction of equals from equals. Hence R equals the remaining k copies of A. In precisely the same way, S equals the remaining k copies of B. [D5.2, CN3]

**Step 4.** If k is one, R equals A and S equals B. If k is greater than one, A measures R exactly k times and B measures S exactly k times; consequently R and S are equimultiples of A and B. Thus the remainders are either equal to the original magnitudes respectively or equimultiples of them, as required. [D5.2]

**USED:** CN3, CN5, D5.2
**Human refs (from References field):** 5.2
**Jaccard:** 0.000 — AI adds ['CN3', 'CN5', 'D5.2']; Human adds ['5.2']

## Proposition 5.7
**Statement:** Equal magnitudes have to the same the same ratio, as also has the same to equal magnitudes.

**Step 1.** Let A and B be equal magnitudes, and let C be a magnitude with which their ratios are considered. We use the definition of equal ratios directly for both assertions, checking arbitrary equimultiples rather than invoking a theorem about ratios. [D5.5]

**Step 2.** Let m and n be any positive whole numbers. Repeated addition of equals to equals gives mA = mB and nA = nB: each multiple consists of the indicated number of copies of its magnitude. [D5.2, CN2]

**Step 3.** Compare mA and mB with nC. Since mA = mB, they alike exceed nC, alike equal nC, or alike fall short of nC; in particular, equality of either with nC entails equality of the other with nC. As m and n were arbitrary, the definition of equal ratios gives A:C = B:C. Thus equal magnitudes have to the same magnitude the same ratio. [CN1, D5.5]

**Step 4.** Now compare mC with nA and nB. Since nA = nB, mC alike exceeds both, equals both, or falls short of both; again, equality with either entails equality with the other. Since m and n were arbitrary, the same definition gives C:A = C:B. Thus the same magnitude also has the same ratio to equal magnitudes, completing both assertions. [CN1, D5.5]

**USED:** CN1, CN2, D5.2, D5.5
**Human refs (from References field):** D5.5
**Jaccard:** 0.250 — AI adds ['CN1', 'CN2', 'D5.2']

## Proposition 5.8
**Statement:** Of unequal magnitudes, the greater has to the same a greater ratio than the less has; and the same has to the less a greater ratio than it has to the greater.

**Step 1.** Let A and B be the unequal magnitudes, with A greater than B, and let C be the common magnitude in the ratios under consideration. Write A = B + D, where D is the positive excess. We use the definition of greater ratio directly: a single strict comparison between suitable multiples will establish both assertions. Write kX for k copies of a magnitude X. [CN5, D5.2, D5.7]

**Step 2.** Choose a positive integer n such that nD > C; such a multiple exists by the criterion for magnitudes to have a ratio. Repeated addition of A = B + D gives nA = nB + nD. Since nD > C, it follows that
nA = nB + nD > nB + C.
[D5.4, D5.2, CN2, CN5]

**Step 3.** Multiples of C eventually exceed nB. In a finite succession ending with such a multiple, let mC be the first multiple exceeding nB. Thus nB < mC. If m > 1, the preceding multiple satisfies (m − 1)C ≤ nB, and adding C gives mC ≤ nB + C. If m = 1, the same upper bound holds because C is a part of nB + C. Consequently, by Step 2,
nB < mC ≤ nB + C < nA,
and hence nB < mC < nA. [D5.4, D5.2, CN2, CN5]

**Step 4.** For the ratios A:C and B:C, take the equimultiples nA and nB of the antecedents, and the equal multiples mC and mC of the consequents. Then nA exceeds mC, whereas nB does not exceed mC. Therefore A has to C a greater ratio than B has to C. [D5.7]

**Step 5.** For the ratios C:B and C:A, take the equal multiples mC and mC of the antecedents, and the equimultiples nB and nA of the consequents. Then mC exceeds nB, whereas mC does not exceed nA. Therefore C has to B a greater ratio than C has to A. Thus the greater magnitude has to the same a greater ratio than the less has, and the same has to the less a greater ratio than it has to the greater. [D5.7]

**USED:** CN2, CN5, D5.2, D5.4, D5.7
**Human refs (from References field):** 5.1, D5.4, D5.7
**Jaccard:** 0.333 — AI adds ['CN2', 'CN5', 'D5.2']; Human adds ['5.1']

## Proposition 5.9
**Statement:** Magnitudes which have the same ratio to the same are equal to one another; and magnitudes to which the same has the same ratio are equal.

**Step 1.** Use Proposition 5.8 directly, since its two clauses address the two possible positions of the common magnitude. Equality of ratios excludes a greater ratio in either direction: Definition D5.5 requires every corresponding pair of equimultiples to agree in whether they exceed, equal, or fall short, whereas Definition D5.7 requires equimultiples for which one comparison exceeds and the other does not. These conditions are incompatible. [5.8, D5.5, D5.7]

**Step 2.** Let A and B have the same ratio to C. If A were greater than B, then A would have to C a greater ratio than B has to C, by the first clause of Proposition 5.8, contradicting their having the same ratio by Step 1. If B were greater than A, the same clause would give the opposite strict inequality of ratios, again a contradiction. Thus A = B. [5.8, D5.5, D5.7]

**Step 3.** Let C have the same ratio to A as to B. If A were greater than B, then C would have to B a greater ratio than it has to A, by the second clause of Proposition 5.8, contradicting the hypothesis by Step 1. If B were greater than A, that clause would instead make the ratio of C to A greater than that of C to B, likewise impossible. Thus A = B. Therefore magnitudes which have the same ratio to the same are equal, and magnitudes to which the same has the same ratio are equal. [5.8, D5.5, D5.7]

**USED:** 5.8, D5.5, D5.7
**Human refs (from References field):** 5.8
**Jaccard:** 0.333 — AI adds ['D5.5', 'D5.7']

## Proposition 5.10
**Statement:** Of magnitudes which have a ratio to the same, that which has a greater ratio is greater; and that to which the same has a greater ratio is less.

**Step 1.** Let A have to C a greater ratio than B has to C. We first exclude equality, then the opposite inequality: propositions 5.7 and 5.8 naturally apply because they give ratio comparisons from magnitude comparisons. If A = B, then A:C = B:C by 5.7, contrary to the hypothesis. Thus A is not equal to B. [5.7]

**Step 2.** If A were less than B, then B, being greater, would have to C a greater ratio than A has to C, by 5.8. This contradicts the given strict comparison. Therefore A is neither equal to nor less than B, and hence A is greater than B. [5.8]

**Step 3.** Now let C have to A a greater ratio than it has to B. If A = B, then C:A = C:B by the second assertion of 5.7, contrary to the hypothesis. Thus A is not equal to B. [5.7]

**Step 4.** If A were greater than B, then C would have to the lesser magnitude B a greater ratio than it has to A, by the second assertion of 5.8. This contradicts the given strict comparison. Therefore A is neither equal to nor greater than B, and hence A is less than B. Thus, of magnitudes having a ratio to the same magnitude, that which has the greater ratio is greater; and that to which the same magnitude has the greater ratio is less. [5.8]

**USED:** 5.7, 5.8
**Human refs (from References field):** 5.7, 5.8
**Jaccard:** 1.000 — Perfect match.

## Proposition 5.11
**Statement:** Ratios which are the same with the same ratio are also the same with one another.

**Step 1.** Let A:B and C:D each be the same ratio as E:F. We use the equimultiple criterion directly, since both hypotheses involve the same comparison ratio. Take arbitrary positive integers m and n, forming the equimultiples mA, mC, mE and nB, nD, nF. [D5.5]

**Step 2.** Since A:B is the same ratio as E:F, mA and nB have the same comparison—greater than, equal to, or less than—as mE and nF. Likewise, since C:D is the same ratio as E:F, mC and nD have the same comparison as mE and nF. Thus, if mE exceeds nF, both mA exceeds nB and mC exceeds nD; if mE equals nF, both corresponding pairs are equal; and if mE falls short of nF, both corresponding pairs fall short. [D5.5]

**Step 3.** Consequently, mA and mC alike exceed, are alike equal to, or alike fall short of nB and nD respectively. Since m and n were arbitrary, the definition of sameness of ratios gives A:B the same ratio as C:D. Therefore ratios which are the same with the same ratio are also the same with one another. [D5.5]

**USED:** D5.5
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['D5.5']

## Proposition 5.12
**Statement:** If any number of magnitudes be proportional, as one of the antecedents is to one of the consequents, so will all the antecedents be to all the consequents.

**Step 1.** Let the given proportional pairs be A₁, B₁; …; Aₖ, Bₖ, and put S = A₁ + ⋯ + Aₖ and T = B₁ + ⋯ + Bₖ. The antecedents are magnitudes that can be added together, and likewise the consequents. Fix any index j. By the meaning of proportionality, Aᵢ : Bᵢ = Aⱼ : Bⱼ for every i. We take the direct route through the defining equimultiple test for equality of ratios. [D5.6, D5.5]

**Step 2.** Take any positive integers m and n. Form Xᵢ = mAᵢ and Yᵢ = nBᵢ for every i. Since a multiple consists of repeated copies of its magnitude, collecting the m copies of each antecedent, and similarly the n copies of each consequent, gives
X₁ + ⋯ + Xₖ = mS,
Y₁ + ⋯ + Yₖ = nT.
These equalities follow by repeated addition of equal magnitudes. [D5.2, CN2]

**Step 3.** Since Aᵢ : Bᵢ = Aⱼ : Bⱼ, the equimultiple test says that Xᵢ and Yᵢ have the same comparison as mAⱼ and nBⱼ. Thus, if mAⱼ exceeds nBⱼ, every Xᵢ exceeds Yᵢ; if they are equal, every Xᵢ equals Yᵢ; and if mAⱼ falls short of nBⱼ, every Xᵢ falls short of Yᵢ. [D5.5]

**Step 4.** These comparisons persist upon taking the sums. In the equality case, repeated addition of equals gives mS = nT. In the greater case, write each Xᵢ as Yᵢ together with its positive excess Eᵢ. Then mS is nT together with E₁ + ⋯ + Eₖ, and therefore mS > nT, since the whole is greater than the part. In the lesser case, reversing the roles gives mS < nT. Consequently, mAⱼ and nBⱼ alike exceed, equal, or fall short of one another exactly as mS and nT do. [CN2, CN5]

**Step 5.** The integers m and n were arbitrary. Hence the defining equimultiple test gives Aⱼ : Bⱼ = S : T. Since j was any chosen corresponding pair, as any one antecedent is to its consequent, so are all the antecedents taken together to all the consequents taken together. This is the required conclusion. [D5.5]

**USED:** CN2, CN5, D5.2, D5.5, D5.6
**Human refs (from References field):** 5.1, D5.5
**Jaccard:** 0.167 — AI adds ['CN2', 'CN5', 'D5.2', 'D5.6']; Human adds ['5.1']

## Proposition 5.13
**Statement:** If a first magnitude have to a second the same ratio as a third to a fourth, and the third have to the fourth a greater ratio than a fifth has to a sixth, the first will also have to the second a greater ratio than the fifth to the sixth.

**Step 1.** Let A, B, C, D, E, F be the six magnitudes, with A:B = C:D and C:D greater than E:F. We use the definitions directly, transferring the equimultiples that witness the greater ratio. By D5.7, there are positive integers m and n such that mC exceeds nD, while mE does not exceed nF. [D5.7]

**Step 2.** Take also the multiples mA and nB. Since A:B = C:D, the equimultiples mA, mC must alike exceed, equal, or fall short of nB, nD respectively. As mC exceeds nD, mA therefore exceeds nB. [D5.5]

**Step 3.** Thus the equimultiples mA, mE of A, E and the equimultiples nB, nF of B, F satisfy: mA exceeds nB, but mE does not exceed nF. By the definition of a greater ratio, A:B is greater than E:F, as required. [D5.7]

**USED:** D5.5, D5.7
**Human refs (from References field):** D5.5, D5.7
**Jaccard:** 1.000 — Perfect match.

## Proposition 5.14
**Statement:** If a first magnitude have to a second the same ratio as a third has to a fourth, and the first be greater than the third, the second will also be greater than the fourth; if equal, equal; and if less, less.

**Step 1.** Let A, B, C, D be the first, second, third, and fourth magnitudes, with A:B = C:D. We use comparisons with a common term, since these apply directly to the given magnitude comparisons. First suppose A > C. Comparing their ratios to B gives A:B > C:B. [5.8]

**Step 2.** Since C:D = A:B and A:B > C:B, we have C:D > C:B. With the common antecedent C, the greater ratio has the smaller consequent; hence D < B, or B > D. [5.13, 5.10]

**Step 3.** Next suppose A = C. Equal magnitudes have the same ratio to B, so A:B = C:B. Together with A:B = C:D, this gives C:B = C:D. [5.7, 5.11]

**Step 4.** Magnitudes to which the same magnitude has the same ratio are equal. Applying this to C:B = C:D gives B = D. [5.9]

**Step 5.** Finally suppose A < C. Since C > A, comparison with the common consequent D gives C:D > A:D. Since A:B = C:D, it follows that A:B > A:D. [5.8, 5.13]

**Step 6.** With the common antecedent A, the greater ratio has the smaller consequent; hence B < D. Thus, whenever A:B = C:D, the second magnitude is greater than, equal to, or less than the fourth according as the first is greater than, equal to, or less than the third. [5.10]

**USED:** 5.10, 5.11, 5.13, 5.7, 5.8, 5.9
**Human refs (from References field):** 5.10, 5.13, 5.8
**Jaccard:** 0.500 — AI adds ['5.11', '5.7', '5.9']

## Proposition 5.15
**Statement:** Parts have the same ratio as the same multiples of them taken in corresponding order.

**Step 1.** Let C and D be the same multiples of magnitudes A and B, respectively. By the definition of a multiple, write C = A₁ + ⋯ + Aₙ and D = B₁ + ⋯ + Bₙ, where every Aᵢ equals A and every Bᵢ equals B, with the same number of terms in both sums. [D5.2]

**Step 2.** For every index i, equal magnitudes have the same ratio to the same magnitude, so Aᵢ:Bᵢ = A:Bᵢ. Likewise, the same magnitude has the same ratio to equal magnitudes, so A:B = A:Bᵢ. Since ratios which are the same with the same ratio are the same with one another, Aᵢ:Bᵢ = A:B. Thus all the corresponding pairs are proportional. [5.7, 5.11]

**Step 3.** We apply 5.12 directly: it is the natural route because the prescribed multiples are sums of these proportional pairs. The ratio of one antecedent to its consequent therefore equals the ratio of all the antecedents together to all the consequents together:
A₁:B₁ = (A₁ + ⋯ + Aₙ):(B₁ + ⋯ + Bₙ) = C:D.
Together with Step 2, this gives A:B = C:D. Hence parts have the same ratio as the same multiples of them taken in corresponding order. [5.12, 5.11]

**USED:** 5.11, 5.12, 5.7, D5.2
**Human refs (from References field):** 5.12, 5.7
**Jaccard:** 0.500 — AI adds ['5.11', 'D5.2']

## Proposition 5.16
**Statement:** If four magnitudes be proportional, they will also be proportional alternately.

**Step 1.** Let A, B, C, D be proportional, so that A:B = C:D. We must prove A:C = B:D, which is the alternate proportion. [D5.6, D5.12]

**Step 2.** Take arbitrary positive whole numbers m and n, forming equimultiples mA, mB of A, B and equimultiples nC, nD of C, D. Use 5.15 directly, since each individual ratio has both its terms multiplied by the same number. Thus
A:B = mA:mB and C:D = nC:nD. [5.15]

**Step 3.** Combining these equalities with the hypothesis A:B = C:D, ratios which are the same with the same ratio give
mA:mB = nC:nD. [5.11]

**Step 4.** Apply 5.14 to these four multiples. If mA is greater than nC, then mB is greater than nD; if mA equals nC, then mB equals nD; and if mA is less than nC, then mB is less than nD. Thus mA and mB alike exceed, equal, or fall short of nC and nD respectively. [5.14]

**Step 5.** Here mA and mB are arbitrary equimultiples of the first and third magnitudes in the order A, C, B, D, while nC and nD are arbitrary equimultiples of the second and fourth. Step 4 therefore establishes precisely the defining condition for A:C = B:D. Hence the four magnitudes are proportional alternately. [D5.5, D5.6, D5.12]

**USED:** 5.11, 5.14, 5.15, D5.12, D5.5, D5.6
**Human refs (from References field):** 5.11, 5.14, 5.15, D5.5
**Jaccard:** 0.667 — AI adds ['D5.12', 'D5.6']

## Proposition 5.17
**Statement:** If magnitudes be proportional componendo, they will also be proportional separando.

**Step 1.** Write the given proportion componendo as
(A+B):B = (C+D):D.
By the definitions of composition and separation, we must prove A:B = C:D. We take the direct route through the defining equimultiple test. [D5.14, D5.15, D5.5]

**Step 2.** Let m and n be arbitrary positive integers. Put
E=m(A+B), F=m(C+D),
P=mB, Q=mD, R=nB, S=nD.
The remainder-of-multiples rule gives
E−P=mA and F−Q=mC.
Here we use 5.1, the first applicable remainder-of-multiples result in the table. [5.1]

**Step 3.** By addition of corresponding multiples, P+R and Q+S are respectively the (m+n)-fold multiples of B and D. Since E and F are the m-fold multiples of A+B and C+D, the given proportion implies that E and F alike exceed, equal, or fall short of P+R and Q+S, respectively. [5.2, D5.5]

**Step 4.** Remove P from both magnitudes in the first comparison, and Q from both magnitudes in the second. Each comparison retains its character: equal magnitudes leave equal remainders; in an unequal comparison the positive excess remains, so the greater remainder is still greater than the lesser. Consequently, E−P and F−Q alike exceed, equal, or fall short of R and S, respectively. Thus mA and mC alike exceed, equal, or fall short of nB and nD, respectively. [CN3, CN5; Step 2]

**Step 5.** Since m and n were arbitrary, the defining equimultiple test gives A:B = C:D. Therefore the magnitudes are proportional separando, as required. [D5.5, D5.6, D5.15]

**USED:** 5.1, 5.2, CN3, CN5, D5.14, D5.15, D5.5, D5.6
**Human refs (from References field):** 5.1, 5.2
**Jaccard:** 0.250 — AI adds ['CN3', 'CN5', 'D5.14', 'D5.15', 'D5.5', 'D5.6']

## Proposition 5.18
**Statement:** If magnitudes be proportional separando, they will also be proportional componendo.

**Step 1.** Let X=A+B and Y=C+D, with all the parts positive, and suppose A:B=C:D. This is the hypothesis obtained by separating the ratios X:B and Y:D; the required conclusion by composition is X:B=Y:D. We use the defining equimultiple criterion directly, without introducing alternate ratios. [D5.15, D5.14, D5.5]

**Step 2.** Choose arbitrary positive integers m and n, writing mM for m copies of a magnitude M. Each copy of X contains B, so mB can be subtracted from mX; similarly mD can be subtracted from mY. Proposition 5.1, the earliest applicable table entry for the remainder-of-multiples identity, gives
mX−mB=mA and mY−mD=mC.
Thus mX=mA+mB and mY=mC+mD. [D5.2, 5.1]

**Step 3.** If n≤m, then nB≤mB<mX and nD≤mD<mY: the additional copies and the positive remainders make the respective wholes greater than their parts. Hence mX and mY both exceed nB and nD respectively. [D5.2, CN5]

**Step 4.** If n>m, put k=n−m, a positive integer. Grouping the copies gives nB=mB+kB and nD=mD+kD. Since A:B=C:D, the definition of equal ratios says that mA and mC alike exceed, are alike equal to, or alike fall short of kB and kD respectively. [D5.2, D5.5]

**Step 5.** Add mB to both magnitudes in the first comparison, and mD to both in the second. Equality is preserved by addition of equals; a strict inequality is preserved because its positive excess remains a part of the larger whole. Using the identities above, it follows that mX and mY alike exceed, are alike equal to, or alike fall short of nB and nD respectively. [CN2, CN5]

**Step 6.** Thus, for every choice of m and n, the equimultiples mX and mY have matching relations to nB and nD. Therefore X:B=Y:D by the definition of equal ratios. Equivalently, (A+B):B=(C+D):D. Hence magnitudes proportional separando are also proportional componendo. [D5.5, D5.14, D5.15]

**USED:** 5.1, CN2, CN5, D5.14, D5.15, D5.2, D5.5
**Human refs (from References field):** 5.11, 5.14, 5.17
**Jaccard:** 0.000 — AI adds ['5.1', 'CN2', 'CN5', 'D5.14', 'D5.15', 'D5.2', 'D5.5']; Human adds ['5.11', '5.14', '5.17']

## Proposition 5.19
**Statement:** If, as a whole is to a whole, so is a part subtracted to a part subtracted, the remainder will also be to the remainder as whole to whole.

**Step 1.** Let the wholes be A and B, the parts subtracted be C and D, and the respective remainders be R and S. Thus A = R + C and B = S + D, and by hypothesis A:B = C:D. By alternation, A:C = B:D. We choose alternation first because it puts each whole in relation to its own subtracted part, allowing separation directly. [5.16, D5.12]

**Step 2.** The proportion just obtained is (R + C):C = (S + D):D. By separation, taking the excess of each antecedent over its consequent, R:C = S:D. [5.17, D5.15]

**Step 3.** Alternating this proportion gives R:S = C:D. [5.16, D5.12]

**Step 4.** By hypothesis A:B = C:D, and Step 3 gives R:S = C:D. Ratios which are the same with the same ratio are the same with one another; hence R:S = A:B. Therefore the remainder is to the remainder as the whole is to the whole. [5.11]

**USED:** 5.11, 5.16, 5.17, D5.12, D5.15
**Human refs (from References field):** 5.11, 5.16, 5.17
**Jaccard:** 0.600 — AI adds ['D5.12', 'D5.15']

## Proposition 5.20
**Statement:** If there be three magnitudes, and others equal to them in multitude, which taken two and two are in the same ratio, and if ex aequali the first be greater than the third, the fourth will also be greater than the sixth; if equal, equal; and, if less, less.

**Step 1.** Let the two triples be A, B, C and D, E, F, with A:B = D:E and B:C = E:F. We use common-consequent ratio comparisons, since these apply directly to the extreme terms without requiring ratios between the two triples. First, C:B = F:E: for arbitrary positive integers m,n, the comparisons of nB with mC and of nE with mF agree; reversing both comparisons shows that those of mC with nB and of mF with nE agree. This is precisely the definition of equality of the inverse ratios. [D5.5]

**Step 2.** Suppose A > C. Then A:B > C:B. [5.8] Hence there are positive integers m,n such that mA > nB while mC does not exceed nB. [D5.7] Since A:B = D:E and C:B = F:E, these same comparisons give mD > nE while mF does not exceed nE. [D5.5] Thus D:E > F:E, and consequently D > F. [D5.7, 5.10]

**Step 3.** Suppose A = C. Then A:B = C:B. [5.7] Combining this with A:B = D:E and C:B = F:E gives D:E = F:E. [5.11] Magnitudes having the same ratio to the same magnitude are equal; therefore D = F. [5.9]

**Step 4.** Suppose A < C. Then C:B > A:B. [5.8] There are therefore positive integers m,n such that mC > nB while mA does not exceed nB. [D5.7] The equalities C:B = F:E and A:B = D:E give mF > nE while mD does not exceed nE. [D5.5] Hence F:E > D:E, so F > D, or D < F. [D5.7, 5.10] Thus, ex aequali, according as the first magnitude is greater than, equal to, or less than the third, the fourth is greater than, equal to, or less than the sixth, as required.

**USED:** 5.10, 5.11, 5.7, 5.8, 5.9, D5.5, D5.7
**Human refs (from References field):** 5.10, 5.13, 5.8
**Jaccard:** 0.250 — AI adds ['5.11', '5.7', '5.9', 'D5.5', 'D5.7']; Human adds ['5.13']

## Proposition 5.21
**Statement:** If there be three magnitudes, and others equal to them in multitude, which taken two and two together are in the same ratio, and the proportion of them be perturbed, then, if ex aequali the first magnitude is greater than the third, the fourth will also be greater than the sixth; if equal, equal; and if less, less.

**Step 1.** Let the two triples be A, B, C and D, E, F. The perturbed proportion means that A:B = E:F and B:C = D:E. We must compare A with C and D with F, the extreme terms left after removing the intermediates. We choose the common-antecedent ratios B:C and B:A, since their comparisons can be transferred directly through the given proportions by the defining equimultiple tests. [D5.18, D5.17]

**Step 2.** From A:B = E:F we obtain B:A = F:E directly from the definition of equal ratios. Indeed, for arbitrary positive integers m and n, the comparisons of nA with mB and of nE with mF agree. Reversing both comparisons shows that the comparisons of mB with nA and of mF with nE agree. This is precisely B:A = F:E. [D5.5]

**Step 3.** Suppose A > C. Since the same magnitude has a greater ratio to the less, B:C > B:A. Hence there are equimultiples satisfying mB > nC but mB ≤ nA. By B:C = D:E, the first comparison gives mD > nE; by B:A = F:E, the second gives mF ≤ nE. Thus D:E > F:E by the definition of a greater ratio. Magnitudes having ratios to the same magnitude are ordered as their ratios; therefore D > F. [5.8, D5.7, D5.5, 5.10]

**Step 4.** Suppose A = C. The same magnitude has the same ratio to equal magnitudes, so B:C = B:A. Combining this with B:C = D:E and B:A = F:E gives D:E = F:E, since ratios equal to the same ratio are equal to one another. Magnitudes having the same ratio to the same magnitude are equal; hence D = F. [5.7, 5.11, 5.9]

**Step 5.** Suppose A < C. Then B:A > B:C. Consequently there are equimultiples satisfying mB > nA but mB ≤ nC. The proportions B:A = F:E and B:C = D:E give respectively mF > nE and mD ≤ nE. Therefore F:E > D:E, and hence F > D, or D < F. Thus, ex aequali, if the first magnitude is greater than the third, the fourth is greater than the sixth; if equal, equal; and if less, less. [5.8, D5.7, D5.5, 5.10]

**USED:** 5.10, 5.11, 5.7, 5.8, 5.9, D5.17, D5.18, D5.5, D5.7
**Human refs (from References field):** 5.10, 5.13, 5.8
**Jaccard:** 0.200 — AI adds ['5.11', '5.7', '5.9', 'D5.17', 'D5.18', 'D5.5', 'D5.7']; Human adds ['5.13']

## Proposition 5.22
**Statement:** If there be any number of magnitudes whatever, and others equal to them in multitude, which taken two and two together are in the same ratio, they will also be in the same ratio ex aequali.

**Step 1.** Let A₁,…,Aᵣ and B₁,…,Bᵣ be two lists of magnitudes, with r ≥ 2, such that Aᵢ:Aᵢ₊₁ = Bᵢ:Bᵢ₊₁ for every i < r. We must show A₁:Aᵣ = B₁:Bᵣ, which is the meaning of proportion ex aequali. We use the order-preserving comparison theorem 5.20, since the successive ratios occur in corresponding order. [D5.17; 5.20]

**Step 2.** First consider three magnitudes A,B,C and three others D,E,F satisfying A:B = D:E and B:C = E:F. Take arbitrary positive integral multipliers m,n. By the theorem on equimultiples of proportional magnitudes,
(mA):(mB) = (mD):(mE),
and
(mB):(nC) = (mE):(nF).
Thus the triples mA,mB,nC and mD,mE,nF satisfy the successive-ratio hypotheses of the comparison theorem. [5.4]

**Step 3.** Apply that theorem to these triples. If mA is greater than nC, then mD is greater than nF; if mA equals nC, then mD equals nF; and if mA is less than nC, then mD is less than nF. [5.20]

**Step 4.** Since m and n were arbitrary, any equimultiples of A and D alike exceed, equal, or fall short of any equimultiples of C and F, respectively. Therefore A:C = D:F by the definition of equality of ratios. This establishes the required result for three magnitudes in each list. [D5.5]

**Step 5.** Return to the original lists. For k = 2, A₁:Aₖ = B₁:Bₖ is a hypothesis. Whenever this equality has been obtained for some k < r, combine it with the given equality Aₖ:Aₖ₊₁ = Bₖ:Bₖ₊₁. Applying the three-magnitude argument of Steps 2–4 to A₁,Aₖ,Aₖ₊₁ and B₁,Bₖ,Bₖ₊₁ gives A₁:Aₖ₊₁ = B₁:Bₖ₊₁. Repeating this finite process yields A₁:Aᵣ = B₁:Bᵣ. [Steps 2–4, using 5.4, 5.20 and D5.5]

**Step 6.** Hence, upon removing all intermediate terms, the first magnitude has to the last in one list the same ratio as the first has to the last in the other. The magnitudes are therefore in the same ratio ex aequali, as required. [D5.17]

**USED:** 5.20, 5.4, D5.17, D5.5
**Human refs (from References field):** 5.20, 5.4, D5.5
**Jaccard:** 0.750 — AI adds ['D5.17']

## Proposition 5.23
**Statement:** If there be three magnitudes, and others equal to them in multitude, which taken two and two together are in the same ratio, and the proportion of them be perturbed, they will also be in the same ratio ex aequali.

**Step 1.** Let the two triples be A, B, C and D, E, F, with A:B = E:F and B:C = D:E. This is the given perturbed proportion. We must prove A:C = D:F, the proportion ex aequali. [D5.18, D5.17]

**Step 2.** Let m and n be arbitrary positive integers. Take G = mA, H = mB, K = mD, and L = nC, M = nE, N = nF. To establish A:C = D:F by the definition of equal ratios, it suffices to show that G and L have the same comparison as K and N for every such choice. [D5.5]

**Step 3.** Parts have the same ratio as their corresponding equimultiples; hence G:H = A:B and M:N = E:F. Since A:B = E:F by hypothesis, it follows that G:H = M:N. [5.15, 5.11]

**Step 4.** From B:C = D:E, taking m-fold multiples of the antecedents and n-fold multiples of the consequents gives H:L = K:M. [5.4]

**Step 5.** Thus the triples G, H, L and K, M, N satisfy G:H = M:N and H:L = K:M. We use the perturbed-comparison proposition directly, since it matches this order without rearrangement. It gives: if G > L, then K > N; if G = L, then K = N; and if G < L, then K < N. [5.21]

**Step 6.** Therefore arbitrary equimultiples G and K of A and D alike exceed, are alike equal to, or alike fall short of the arbitrary equimultiples L and N of C and F, respectively. By the definition of equal ratios, A:C = D:F. Hence the original triples are in the same ratio ex aequali, as required. [D5.5, D5.17]

**USED:** 5.11, 5.15, 5.21, 5.4, D5.17, D5.18, D5.5
**Human refs (from References field):** 5.11, 5.15, 5.16, 5.21
**Jaccard:** 0.375 — AI adds ['5.4', 'D5.17', 'D5.18', 'D5.5']; Human adds ['5.16']

## Proposition 5.24
**Statement:** If a first magnitude have to a second the same ratio as a third has to a fourth, and also a fifth have to the second the same ratio as a sixth to the fourth, the first and fifth added together will have to the second the same ratio as the third and sixth have to the fourth.

**Step 1.** Let the six magnitudes be A, B, C, D, E, F, with A:B = C:D and E:B = F:D. The latter equality also gives B:E = D:F directly by D5.5: for arbitrary positive integers m and n, the comparisons of nE with mB and of nF with mD agree; reversing both comparisons shows that the comparisons of mB with nE and of mD with nF agree.

**Step 2.** Choose ex aequali as the first combination, since B and D now serve as intermediate terms. Apply 5.22 to the triples A, B, E and C, D, F. From A:B = C:D and B:E = D:F, obtain A:E = C:F.

**Step 3.** Since A and C are respectively the excesses of A+E over E and C+F over F, this last equality is the separated proportion for A+E, E, C+F, F (D5.15). By 5.18, the corresponding composed proportion holds; that is, (A+E):E = (C+F):F (D5.14).

**Step 4.** Apply 5.22 again, now to the triples A+E, E, B and C+F, F, D. The equality from Step 3 and the given equality E:B = F:D yield (A+E):B = (C+F):D. Thus the first and fifth added together have to the second the same ratio as the third and sixth added together have to the fourth, as required.

**USED:** 5.18, 5.22, D5.14, D5.15, D5.5
**Human refs (from References field):** 5.18, 5.22
**Jaccard:** 0.400 — AI adds ['D5.14', 'D5.15', 'D5.5']

## Proposition 5.25
**Statement:** If four magnitudes be proportional, the greatest and the least are greater than the remaining two.

**Step 1.** Write the given proportion as A:B = C:D, with A the greatest magnitude. This arrangement is possible by exchanging the two ratios and, if necessary, inverting both; simultaneous inversion preserves proportionality by the equimultiple definition (D5.5). Since A>B, that definition, with unit multiples, gives C>D. Since A>C, Proposition 5.14 gives B>D. Thus D is the least magnitude.

**Step 2.** Let X be the excess of A over B, and Y the excess of C over D, so that A=B+X and C=D+Y. Choose separation as the direct route, because these excesses determine the difference between the required sums. By Proposition 5.17,
X:B = Y:D.

**Step 3.** Since B>D, the three cases of Proposition 5.14 force X>Y: if X=Y, that proposition would give B=D, and if X<Y, it would give B<D. Both are excluded. Therefore X=Y+H for some positive excess H. (5.14)

**Step 4.** Substituting these equal magnitudes and adding equals gives
A+D = B+X+D = B+Y+H+D = B+C+H. (CN2)
Consequently A+D is greater than B+C, since the whole is greater than the part (CN5). Thus the greatest and the least together are greater than the remaining two.

**USED:** 5.14, 5.17, CN2, CN5, D5.5
**Human refs (from References field):** 5.19
**Jaccard:** 0.000 — AI adds ['5.14', '5.17', 'CN2', 'CN5', 'D5.5']; Human adds ['5.19']
