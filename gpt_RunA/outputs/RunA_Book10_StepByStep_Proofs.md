# Book 10 of Euclid's Elements — Step-by-Step AI Proofs (Run A)

## Proposition 10.1
**Statement:** Two unequal magnitudes being set out, if from the greater there be subtracted a magnitude greater than its half, and from that which is left a magnitude greater than its half, and if this process be repeated continually, there will be left some magnitude which will be less than the lesser magnitude set out.

**Step 1.** Let A be the greater magnitude and B the lesser. By D5.4, choose a finite multiple nB of B such that nB > A. We use the finite-multiple route: compare this multiple with the total removed, rather than introduce an auxiliary sequence of bisections. [D5.4]

**Step 2.** Put R₀ = A. For each successive subtraction, let Sᵢ be the magnitude removed and Rᵢ the remainder, so that Rᵢ₋₁ = Sᵢ + Rᵢ. We claim that Sᵢ > Rᵢ. Indeed, let Hᵢ be half of Rᵢ₋₁. By the hypothesis, Sᵢ = Hᵢ + Eᵢ for some positive excess Eᵢ. Hence Hᵢ + Hᵢ = Hᵢ + Eᵢ + Rᵢ. Subtracting Hᵢ gives Hᵢ = Eᵢ + Rᵢ. Therefore Sᵢ > Hᵢ > Rᵢ, since each whole is greater than its part. [Hypothesis; CN3; CN5]

**Step 3.** Suppose, for contradiction, that none of the first n remainders is less than B. Then Rᵢ ≥ B for every i from 1 through n. Consequently Sᵢ > B for each of these subtractions. [Step 2]

**Step 4.** Write Sᵢ = B + Fᵢ, where each Fᵢ is positive. Adding these equalities gives
S₁ + ⋯ + Sₙ = nB + (F₁ + ⋯ + Fₙ).
Thus S₁ + ⋯ + Sₙ > nB. But the successive decompositions in Step 2 give
A = S₁ + ⋯ + Sₙ + Rₙ,
so A > S₁ + ⋯ + Sₙ. Therefore A > nB. [Step 2; CN2; CN5]

**Step 5.** This contradicts nB > A from Step 1. Hence at least one of the first n remainders is less than B. Thus, after finitely many of the prescribed subtractions, there is left a magnitude less than the lesser magnitude originally set out. [Steps 1–4]

**USED:** CN2, CN3, CN5, D5.4
**Human refs (from References field):** D5.4
**Jaccard:** 0.250 — AI adds ['CN2', 'CN3', 'CN5']

## Proposition 10.2
**Statement:** If, when the less of two unequal magnitudes is continually subtracted in turn from the greater, that which is left never measures the one before it, the magnitudes will be incommensurable.

**Step 1.** Let A>B be the two magnitudes satisfying the stated subtraction hypothesis. Suppose, for a contradiction, that they are commensurable. Then some positive magnitude E measures both A and B. We take the direct magnitude route, applying 10.1 to alternate remainders. [D10.1.1]

**Step 2.** If E measures two magnitudes X>Y, each consists of a finite number of copies of E. Subtracting Y from X cancels the corresponding copies, so the positive remainder also consists of copies of E. Thus E measures every positive remainder in the prescribed process. In particular, every such remainder is at least E, and E≤B<A. [D5.2; CN3; CN5]

**Step 3.** Group consecutive subtractions of the same lesser magnitude into one turn. Each turn is finite: by Step 2, the magnitude being diminished contains finitely many copies of E, and each subtraction removes at least one copy. Write R₀=A, R₁=B, and let R₂,R₃,… be the successive remainders at the ends of these turns. The hypothesis excludes exact measurement at any turn, so the process continues with positive remainders satisfying
Rᵢ=qᵢRᵢ₊₁+Rᵢ₊₂, where qᵢ≥1 and 0<Rᵢ₊₂<Rᵢ₊₁.
Here qᵢRᵢ₊₁ denotes the copies of Rᵢ₊₁ removed during that turn. [Hypothesis; Step 2; D5.2]

**Step 4.** In each such equality, the removed magnitude qᵢRᵢ₊₁ is at least Rᵢ₊₁ and therefore greater than the remainder Rᵢ₊₂. Consequently Rᵢ>2Rᵢ₊₂: the passage from Rᵢ to Rᵢ₊₂ removes more than half of Rᵢ. Hence the sequence R₀,R₂,R₄,… is obtained by repeatedly subtracting more than half of the current magnitude. [Step 3; CN2; CN5]

**Step 5.** Set out the unequal magnitudes A and E. Since A>E, and the sequence A=R₀,R₂,R₄,… repeatedly removes more than half of what remains, 10.1 gives a remainder R₂ₖ<E after finitely many such passages. [Steps 2 and 4; 10.1]

**Step 6.** But Step 2 shows that E measures R₂ₖ, so R₂ₖ must contain at least one copy of E and cannot be less than E. This contradicts Step 5. Therefore A and B have no common measure and are incommensurable. [D5.2; CN5; D10.1.1]

**USED:** 10.1, CN2, CN3, CN5, D10.1.1, D5.2
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['10.1', 'CN2', 'CN3', 'CN5', 'D10.1.1', 'D5.2']

## Proposition 10.3
**Statement:** Given two commensurable magnitudes, to find their greatest common measure.

**Step 1.** Let A and B be the given commensurable magnitudes, labelled so that A is not less than B. If B measures A, including the case A = B, then B is their greatest common measure: it measures both, and no magnitude greater than B can measure B. Hence suppose that B does not measure A. [D5.2; CN5]

**Step 2.** Starting with A and B, continually subtract the lesser magnitude from the greater, retaining the lesser and the positive remainder as the next pair. Stop as soon as the lesser of the current pair measures the greater. This process must stop: otherwise the successive remainders would never measure their predecessors, and A and B would be incommensurable by 10.2, contrary to the hypothesis and D10.1.1. Denote the terminal pair by H and G, where G measures H. **Path choice:** use 10.2 directly, since its subtraction criterion applies to the given magnitudes without any reduction to numbers. [10.2; D10.1.1]

**Step 3.** The magnitude G measures both members of the terminal pair. Now reverse the subtractions. At any subtraction, if the former pair was X, Y with X > Y, the new pair was Y, X − Y, possibly reordered. If G measures both members of the new pair, then each consists of whole copies of G; adding them shows that G also measures X = Y + (X − Y). Thus G measures both members of the former pair. Repeating this argument backwards through the finite process proves that G measures A and B. [D5.2; CN2]

**Step 4.** Let M be any common measure of A and B. At each subtraction, if M measures X and Y, then X and Y consist of whole copies of M. Subtracting the copies constituting Y from those constituting X leaves whole copies of M constituting X − Y. Therefore M measures both members of the next pair. Following the finite process forwards, M consequently measures G. [D5.2; CN3]

**Step 5.** Since every common measure M of A and B measures G, it is either equal to G or less than G: one copy gives equality, while several copies make G greater than any one of them. No common measure can therefore exceed G. Together with Step 3, this proves that the constructed magnitude G is the greatest common measure of A and B, as required. [D5.2; CN5]

**USED:** 10.2, CN2, CN3, CN5, D10.1.1, D5.2
**Human refs (from References field):** 10.2
**Jaccard:** 0.167 — AI adds ['CN2', 'CN3', 'CN5', 'D10.1.1', 'D5.2']

## Proposition 10.4
**Statement:** Given three commensurable magnitudes, to find their greatest common measure.

**Step 1.** Let the three given commensurable magnitudes be A, B, and C. There exists a magnitude H measuring all three [D10.1.1]. Our path is to reduce the problem to the two-magnitude construction [10.3], using successive subtraction on the first pair to keep track of its common measures.

**Step 2.** Starting with A and B, proceed as follows. If they are equal, put D = A. If the lesser measures the greater, put D equal to the lesser. Otherwise subtract the lesser from the greater and continue with the lesser and the remainder, stopping when one measures the other. This process must terminate: otherwise A and B would be incommensurable, contrary to their having the common measure H [10.2, D10.1.1]. Let D be the lesser magnitude in the terminal pair.

**Step 3.** Every common measure of A and B measures D. Indeed, whenever a magnitude K measures two unequal magnitudes X and Y, their difference is also a multiple of K: subtracting the copies of K constituting the lesser from those constituting the greater leaves whole copies of K [D5.2, CN3]. Thus any common measure of the initial pair measures both members of every successive pair, and consequently measures D. In particular, H measures D; since H also measures C, the magnitudes D and C are commensurable [D10.1.1].

**Step 4.** Moreover, D measures A and B. It measures both members of the terminal pair. At each preceding subtraction, the former greater magnitude is the sum of the former lesser magnitude and the remainder. If D measures these two, it measures their sum, by joining their copies of D [D5.2, CN2]. Reversing the finite sequence therefore shows that D measures both original magnitudes. The cases where the process stopped immediately have the same conclusion directly [D5.2].

**Step 5.** Find E, the greatest common measure of D and C [10.3]. Since E measures D, and D measures A and B, replacing each copy of D in A and B by its constituent copies of E shows that E measures A and B [D5.2, CN2]. It also measures C by its construction. Hence E is a common measure of all three given magnitudes.

**Step 6.** Let K be any common measure of A, B, and C. By Step 3, K measures D. Therefore K is a common measure of D and C, and cannot be greater than their greatest common measure E [10.3]. Since E itself measures A, B, and C, it is their greatest common measure. Thus the required magnitude has been found.

**USED:** 10.2, 10.3, CN2, CN3, D10.1.1, D5.2
**Human refs (from References field):** 10.3
**Jaccard:** 0.167 — AI adds ['10.2', 'CN2', 'CN3', 'D10.1.1', 'D5.2']

## Proposition 10.5
**Statement:** Commensurable magnitudes have to one another the ratio which a number has to a number.

**Step 1.** Let A and B be commensurable magnitudes. By D10.1.1, some magnitude C measures both. Thus A consists of k copies of C and B of l copies of C, where k and l are positive repetition counts, possibly one (D5.2). **Path choice:** use this common measure directly; no greatest-common-measure construction is needed.

**Step 2.** Let T be the number consisting of two units. Form M from k copies of T and N from l copies of T. Both M and N are numbers composed of units, even if either repetition count is one (D7.1, D7.2).

**Step 3.** Take arbitrary positive repetition counts r and s. Then rA and rM are equimultiples of A and M, while sB and sN are equimultiples of B and N. By repeated addition, rA consists of rk copies of C and sB of sl copies of C; correspondingly, rM consists of rk copies of T and sN of sl copies of T. Here rk means the total count in r groups of k copies, and similarly for sl (D5.2, D7.2, CN2).

**Step 4.** If rk equals sl, the corresponding sums are equal, so rA = sB and rM = sN (CN2). If rk exceeds sl, rA contains a part equal to sB together with additional copies of C, and rM contains a part equal to sN together with additional copies of T; hence rA > sB and rM > sN (CN2, CN5). If rk falls short of sl, the same argument with the wholes and parts reversed gives rA < sB and rM < sN (CN2, CN5).

**Step 5.** Therefore, for every choice of these equimultiples, rA and rM alike exceed, equal, or fall short of sB and sN respectively. By D5.5, A:B = M:N. Since M and N are numbers, commensurable magnitudes have to one another the ratio which a number has to a number.

**USED:** CN2, CN5, D10.1.1, D5.2, D5.5, D7.1, D7.2
**Human refs (from References field):** 5.22, 5.7, D7.20
**Jaccard:** 0.000 — AI adds ['CN2', 'CN5', 'D10.1.1', 'D5.2', 'D5.5', 'D7.1', 'D7.2']; Human adds ['5.22', '5.7', 'D7.20']

## Proposition 10.6
**Statement:** If two magnitudes have to one another the ratio which a number has to a number, the magnitudes will be commensurable.

**Step 1.** Let the magnitudes A and B satisfy A:B = m:n, where m and n are numbers, as hypothesized. Regard the numerical terms as finite counts of units; a term arising later may itself be a single unit (D7.1, D7.2). We shall construct a magnitude measuring both A and B, which proves commensurability by D10.1.1.

**Step 2.** Suppose a current pair of magnitudes X,Y and its corresponding numerical pair p,q satisfy X:Y = p:q. Taking single copies in D5.5 shows that X and Y have the same order of size as p and q. Reversing both pairs when necessary also preserves the proportion, directly by D5.5. Thus, whenever the numerical terms are unequal, we may arrange them so that p>q and correspondingly X>Y.

**Step 3.** Replace these pairs by X−Y,Y and p−q,q. Separation of the proportion gives
(X−Y):Y = (p−q):q (5.17).
Both new terms in each pair remain positive. Path choice: separation is the directly applicable ratio operation because it preserves the correspondence after subtracting the lesser term from the greater.

**Step 4.** Repeat Steps 2–3 whenever the numerical terms are unequal. At every subtraction the combined count of units in the numerical pair decreases by the positive count q, while both remaining counts stay positive (D7.1, D7.2, CN5). The initial combined count is finite, so such subtractions cannot continue indefinitely. Since a further subtraction is possible whenever the terms are unequal, the process must reach equal numerical terms.

**Step 5.** Let U,V be the magnitudes corresponding to the terminal numerical pair d,d. The preserved proportion is U:V = d:d. Taking single copies in D5.5 gives U=V. Denote this positive common magnitude by E; the terminal magnitudes are therefore each one copy of E.

**Step 6.** Reverse the finite sequence of subtractions. At any stage, if X−Y consists of r copies of E and Y consists of s copies of E, then adding these equalities shows that X consists of r+s copies of E (CN2). Consequently, being measured by E is preserved at every reversed step (D5.2); any interchange of the two terms plainly leaves this unchanged. Hence the original magnitudes A and B are both measured by E. They are therefore commensurable (D10.1.1), as required.

**USED:** 5.17, CN2, CN5, D10.1.1, D5.2, D5.5, D7.1, D7.2
**Human refs (from References field):** 5.11, 5.22, 5.7, 5.9, D7.20
**Jaccard:** 0.000 — AI adds ['5.17', 'CN2', 'CN5', 'D10.1.1', 'D5.2', 'D5.5', 'D7.1', 'D7.2']; Human adds ['5.11', '5.22', '5.7', '5.9', 'D7.20']

## Proposition 10.7
**Statement:** Incommensurable magnitudes have not to one another the ratio which a number has to a number.

**Step 1.** Let A and B be incommensurable magnitudes. Then no magnitude measures both A and B. [D10.1.1]

**Step 2.** Suppose, for contradiction, that A has to B the ratio which some number m has to some number n. Then A and B are commensurable. We apply 10.6 directly because its hypothesis is precisely the assumed equality of ratios. [10.6]

**Step 3.** Since A and B are commensurable, they have a common measure, contrary to Step 1. Therefore no such numbers m and n exist: incommensurable magnitudes have not to one another the ratio which a number has to a number. [D10.1.1; Step 1]

**USED:** 10.6, D10.1.1
**Human refs (from References field):** 10.6
**Jaccard:** 0.500 — AI adds ['D10.1.1']

## Proposition 10.8
**Statement:** If two magnitudes have not to one another the ratio which a number has to a number, the magnitudes will be incommensurable.

**Step 1.** Let A and B be magnitudes such that A has not to B the ratio which a number has to a number. [Hypothesis.]

**Step 2.** Suppose, for a contradiction, that A and B have a common measure. They are then commensurable. [D10.1.1.]

**Step 3.** Since A and B are commensurable, A has to B the ratio which a number has to a number. [10.5.] This is the direct path: 10.5 applies immediately to the commensurability in Step 2.

**Step 4.** The conclusion of Step 3 contradicts the hypothesis in Step 1. Therefore A and B cannot have any common measure and hence are incommensurable, as required. [D10.1.1.]

**USED:** 10.5, D10.1.1
**Human refs (from References field):** 10.5
**Jaccard:** 0.500 — AI adds ['D10.1.1']

## Proposition 10.9
**Statement:** The squares on straight lines commensurable in length have to one another the ratio which a square number has to a square number; and squares which have to one another the ratio which a square number has to a square number will also have their sides commensurable in length. But the squares on straight lines incommensurable in length have not to one another the ratio which a square number has to a square number; and squares which have not to one another the ratio which a square number has to a square number will not have their sides commensurable in length either.

**Step 1.** For any straight line x, write Q(x) for the square constructed on it [1.46]. All such squares are similar: their angles are equal right angles, and their corresponding sides are proportional because each square is equilateral [D1.22, P4, D6.1].

**Step 2.** Suppose that x:y = m:n, where m and n are numbers. Write m² and n² for the square numbers produced by multiplying each number by itself [D7.18]. By 6.20, Q(x):Q(y) is the duplicate ratio of x:y; this theorem applies directly because the figures are similar polygons. By 8.11, m²:n² is the duplicate ratio of m:n. These duplicate ratios are equal: by D5.9, each is the ratio of the extremes of a three-term continued proportion, and 5.22 equates those extreme ratios when the corresponding adjacent ratios are equal. Consequently,
Q(x):Q(y) = m²:n².

**Step 3.** Let a and b be commensurable in length. They therefore have the ratio of a number to a number; say a:b = m:n [10.5]. Applying Step 2 gives Q(a):Q(b) = m²:n². Thus squares on straight lines commensurable in length have the ratio of a square number to a square number.

**Step 4.** Conversely, suppose that Q(a):Q(b) = m²:n², where m and n are the sides of the given square numbers [D7.18]. Choose a straight line u, and, by laying off successive copies of it, construct c consisting of m copies and d consisting of n copies [P2, P3]. Then c:d = m:n by D5.5: any equimultiples of c and d are compared exactly as the corresponding multiples of their numbers of copies, m and n.

**Step 5.** By Step 2, Q(c):Q(d) = m²:n². Combining this with the hypothesis gives Q(a):Q(b) = Q(c):Q(d) [5.11]. For this reverse passage from square figures to their sides, use the converse direction of 6.22: since the similar figures on the four straight lines are proportional, their corresponding sides are proportional. Hence a:b = c:d. Together with Step 4, this gives a:b = m:n [5.11]. Therefore a and b are commensurable in length [10.6]. This proves the second assertion.

**Step 6.** Now let a and b be incommensurable in length. If Q(a):Q(b) were the ratio of a square number to a square number, Steps 4–5 would make a and b commensurable, contrary to their having no common measure [D10.1.1]. Thus squares on straight lines incommensurable in length do not have the ratio of a square number to a square number.

**Step 7.** Finally, suppose that Q(a):Q(b) is not the ratio of any square number to any square number. If a and b were commensurable in length, Step 3 would give precisely such a ratio, a contradiction. Hence their sides are incommensurable in length [D10.1.1]. All four assertions follow.

**USED:** 1.46, 10.5, 10.6, 5.11, 5.22, 6.20, 6.22, 8.11, D1.22, D10.1.1, D5.5, D5.9, D6.1, D7.18, P2, P3, P4
**Human refs (from References field):** 10.5, 10.6, 6.20, 8.11
**Jaccard:** 0.235 — AI adds ['1.46', '5.11', '5.22', '6.22', 'D1.22', 'D10.1.1', 'D5.5', 'D5.9', 'D6.1', 'D7.18', 'P2', 'P3', 'P4']

## Proposition 10.10
**Statement:** To find two straight lines incommensurable, the one in length only, and the other in square also, with an assigned straight line.

**Step 1.** Choose the numerical ratio 2:3 because its consecutive terms give a direct obstruction to its being a ratio of square numbers. Indeed, if two square numbers had this ratio, there would be a mean proportional number between them [8.11], and therefore also a mean proportional number between 2 and 3 [8.8]. Such a number would necessarily be strictly between 2 and 3 [D7.20], which is impossible because numbers are multitudes of units [D7.2]. Thus 2:3 is not the ratio of any square number to any square number.

**Step 2.** Let a be the assigned straight line. Bisect it, and call either half h [1.10]. Produce a beyond one endpoint and, using a circle centred at that endpoint with radius the adjacent half, append another segment equal to h [P2, P3]. Call the resulting whole d. Then a consists of two copies of h and d of three [CN2], so a:d = 2:3 [D5.5].

**Step 3.** Construct a mean proportional b between a and d, and then a mean proportional c between a and b [6.13]. Thus

a:b = b:d, and a:c = c:b.

**Step 4.** Write Q(x) for the square on a straight line x, and R(x,y) for the rectangle contained by x and y [D1.22, D2.1]. The proportions in Step 3 give

Q(b) = R(a,d), and Q(c) = R(a,b) [6.17].

Since Q(a) = R(a,a), comparison of rectangles having the same altitude a gives

Q(a):Q(b) = a:d = 2:3,

Q(a):Q(c) = a:b [6.1, 5.11].

**Step 5.** The squares Q(a) and Q(b) have the numerical ratio 2:3, so they are commensurable [10.6]. Hence a and b are commensurable in square [D10.1.2]. But Step 1 shows that their squares do not have the ratio of a square number to a square number; therefore a and b are incommensurable in length [10.9]. Thus b is incommensurable with a in length only.

**Step 6.** Since a and b are incommensurable in length, a:b is not the ratio of any number to any number [10.7]. By Step 4, the same is true of Q(a):Q(c). Therefore Q(a) and Q(c) are incommensurable [10.8], and consequently a and c are incommensurable in square [D10.1.2].

**Step 7.** Moreover, because Q(a):Q(c) is not any numerical ratio, it is in particular not the ratio of a square number to a square number. Thus a and c are also incommensurable in length [10.9]. The constructed straight lines b and c therefore satisfy the requirements: b is incommensurable with the assigned line a in length only, and c is incommensurable with it in square also.

**USED:** 1.10, 10.6, 10.7, 10.8, 10.9, 5.11, 6.1, 6.13, 6.17, 8.11, 8.8, CN2, D1.22, D10.1.2, D2.1, D5.5, D7.2, D7.20, P2, P3
**Human refs (from References field):** 10.11, 10.6, 10.9, D5.9
**Jaccard:** 0.091 — AI adds ['1.10', '10.7', '10.8', '5.11', '6.1', '6.13', '6.17', '8.11', '8.8', 'CN2', 'D1.22', 'D10.1.2', 'D2.1', 'D5.5', 'D7.2', 'D7.20', 'P2', 'P3']; Human adds ['10.11', 'D5.9']

## Proposition 10.11
**Statement:** If four magnitudes be proportional, and the first be commensurable with the second, the third will also be commensurable with the fourth; and, if the first be incommensurable with the second, the third will also be incommensurable with the fourth.

**Step 1.** Let the four magnitudes A, B, C, D be proportional, so that A:B = C:D. [D5.6]

**Step 2.** Suppose first that A is commensurable with B. Then there are numbers m, n such that A:B = m:n. [10.5] The chosen route begins with 10.5 because commensurability is the given hypothesis, and this proposition expresses it through a numerical ratio.

**Step 3.** Since C:D and m:n have the same ratio as A:B, we have C:D = m:n. [5.11] Therefore C is commensurable with D. [10.6] This proves the first assertion.

**Step 4.** Now suppose that A is incommensurable with B. We reuse the same numerical-ratio criterion by contradiction, rather than introduce a separate criterion. Suppose, contrary to the required conclusion, that C is commensurable with D. Then there are numbers p, q such that C:D = p:q. [10.5]

**Step 5.** Together with A:B = C:D, this gives A:B = p:q. [5.11] Hence A is commensurable with B. [10.6] This contradicts their assumed incommensurability, which excludes any common measure. Consequently C and D cannot have a common measure and are incommensurable. [D10.1.1] Thus both assertions are proved.

**USED:** 10.5, 10.6, 5.11, D10.1.1, D5.6
**Human refs (from References field):** 10.5, 10.6, 10.7, 10.8
**Jaccard:** 0.286 — AI adds ['5.11', 'D10.1.1', 'D5.6']; Human adds ['10.7', '10.8']

## Proposition 10.12
**Statement:** Magnitudes commensurable with the same magnitude are commensurable with one another also.

**Step 1.** Let A and B each be commensurable with the same magnitude C. By 10.5, there are numbers m, n, p, q such that A:C = m:n and C:B = p:q. We choose the numerical-ratio route, arranging a common middle number in order to combine these proportions.

**Step 2.** Let X and Y be the numbers produced when m and n, respectively, multiply p; and let Z be the number produced when n multiplies q. Since m and n multiply the same number p, we have X:Y = m:n by 7.18. Since n multiplies p and q, we have Y:Z = p:q by 7.17.

**Step 3.** The ratios A:C and X:Y are each equal to m:n, and the ratios C:B and Y:Z are each equal to p:q. Therefore A:C = X:Y and C:B = Y:Z, by 5.11.

**Step 4.** Apply 5.22, ex aequali, to the three magnitudes A, C, B and the three numbers X, Y, Z. It follows that A:B = X:Z.

**Step 5.** Since A and B have the ratio of the number X to the number Z, they are commensurable by 10.6. This criterion applies directly to the numerical ratio just obtained. Thus magnitudes commensurable with the same magnitude are commensurable with one another.

**USED:** 10.5, 10.6, 5.11, 5.22, 7.17, 7.18
**Human refs (from References field):** 10.5, 10.6, 5.11, 5.22, 8.4
**Jaccard:** 0.571 — AI adds ['7.17', '7.18']; Human adds ['8.4']

## Proposition 10.13
**Statement:** If two magnitudes be commensurable, and the one of them be incommensurable with any magnitude, the remaining one will also be incommensurable with the same.

**Step 1.** Let A and B be commensurable, and let A be incommensurable with C. Thus A and C have no common measure. We must prove that B and C are incommensurable. (Hypotheses; D10.1.1.)

**Step 2.** Choose contradiction using 10.12, since it applies directly to magnitudes commensurable with the same magnitude. Suppose B and C are commensurable. Then C is commensurable with B, because a common measure measures both magnitudes regardless of their order. (D10.1.1.)

**Step 3.** A is commensurable with B by hypothesis, and C is commensurable with B by Step 2. Therefore A and C are commensurable with one another. (10.12.)

**Step 4.** Consequently A and C have a common measure, contradicting Step 1. Hence B and C cannot have a common measure and are therefore incommensurable, as required. (D10.1.1.)

**USED:** 10.12, D10.1.1
**Human refs (from References field):** 10.12
**Jaccard:** 0.500 — AI adds ['D10.1.1']

## Proposition 10.14
**Statement:** If four straight lines be proportional, and the square on the first be greater than the square on the second by the square on a straight line commensurable with the first, the square on the third will also be greater than the square on the fourth by  the square on a straight line commensurable with the third. And, if the square on the first be greater than the square on the second by the square on a straight line incommensurable with the first, the square on the third will also be greater than the square on the fourth by the square on a straight line in-commensurable with the third.

**Step 1.** Let the four straight lines be a, b, c, d, with a:b = c:d. Denote the square on a straight line x by S(x), constructing the squares as necessary by 1.46. Let e be the straight line given in the hypothesis, so that S(a) = S(b) + S(e).

**Step 2.** Since a:b = c:d, the squares on these lines are proportional: S(a):S(b) = S(c):S(d) [6.22]. Since S(a) is greater than S(b) by hypothesis, S(c) is greater than S(d) [5.14].

**Step 3.** Construct a square equal to the positive rectilineal excess of S(c) over S(d), and let its side be f [2.14]. Thus S(c) = S(d) + S(f).

**Step 4.** Alternating the proportion in Step 2 gives S(a):S(c) = S(b):S(d) [5.16]. Consequently, the whole areas have the same ratio as the areas taken away. Their remainders therefore have that same ratio: S(a):S(c) = S(e):S(f) [5.19]. Alternating again gives S(a):S(e) = S(c):S(f) [5.16].

**Step 5.** By the converse of 6.22, the sides of these proportional squares are proportional: a:e = c:f. This is the direct path: the proportion already obtained between squares yields the required proportion between straight lines, without introducing ratios of square numbers.

**Step 6.** If e is commensurable with a, then, from a:e = c:f, the straight line f is commensurable with c [10.11]. Together with S(c) = S(d) + S(f) from Step 3, this proves the first assertion.

**Step 7.** If e is incommensurable with a, then the same proportion a:e = c:f shows that f is incommensurable with c [10.11]. Again S(c) = S(d) + S(f), so the square on c exceeds the square on d by the square on a straight line incommensurable with c. This proves the second assertion and completes the proof.

**USED:** 1.46, 10.11, 2.14, 5.14, 5.16, 5.19, 6.22
**Human refs (from References field):** 10.11, 5.17, 5.22, 6.22
**Jaccard:** 0.222 — AI adds ['1.46', '2.14', '5.14', '5.16', '5.19']; Human adds ['5.17', '5.22']

## Proposition 10.15
**Statement:** If two commensurable magnitudes be added together, the whole will also be commensurable with each of them; and, if the whole be commensurable with one of them, the original magnitudes will also be commensurable.

**Step 1.** Let W be the whole formed by adding the magnitudes A and B. First suppose that A and B are commensurable. By D10.1.1, some magnitude U measures both A and B. We use this defining common measure directly, since no greatest-common-measure construction is needed.

**Step 2.** Since U measures A and B, each consists of a finite collection of complete copies of U (D5.2). Adding these two collections gives a collection of complete copies of U equal to W (CN2). Hence U also measures W (D5.2).

**Step 3.** Thus U is a common measure of W and A, and also of W and B. Therefore W is commensurable with each of A and B (D10.1.1).

**Step 4.** Conversely, suppose W is commensurable with one of its summands, which we may call A. There is then a magnitude V measuring both W and A (D10.1.1), so both consist of finite collections of complete copies of V (D5.2). Since W is greater than its part A, the collection constituting W contains more copies than the collection constituting A (CN5).

**Step 5.** From the copies constituting W remove as many copies as constitute A. The remaining complete copies of V equal the remaining magnitude B, since equal magnitudes have been subtracted from equal magnitudes (CN3). Consequently V measures B as well as A (D5.2), and A and B are commensurable (D10.1.1). Therefore the sum of two commensurable magnitudes is commensurable with each, and commensurability of the whole with either summand implies commensurability of the two summands.

**USED:** CN2, CN3, CN5, D10.1.1, D5.2
**Human refs (from References field):** D10.1.1
**Jaccard:** 0.200 — AI adds ['CN2', 'CN3', 'CN5', 'D5.2']

## Proposition 10.16
**Statement:** If two incommensurable magnitudes be added together, the whole will also be incommensurable with each of them; and, if the whole be incommensurable with one of them, the original magnitudes will also be incommensurable.

**Step 1.** Let A and B be the two magnitudes, and let S = A + B. We use the two assertions of 10.15 by contradiction: this is the direct route because that proposition concerns precisely the commensurability of a sum and its summands. Commensurability means having a common measure, and incommensurability means having none (D10.1.1).

**Step 2.** Suppose A and B are incommensurable. Let C be either A or B. If S were commensurable with C, then, by the second assertion of 10.15, the original magnitudes A and B would be commensurable. This contradicts their having no common measure (D10.1.1). Therefore S is incommensurable with C. Since C was either summand, S is incommensurable with each of A and B.

**Step 3.** Conversely, suppose S is incommensurable with one of the summands, denoted by C. If A and B were commensurable, then, by the first assertion of 10.15, S would be commensurable with each of them, hence with C. This contradicts the assumed incommensurability of S and C (D10.1.1). Thus A and B are incommensurable. Both assertions are proved.

**USED:** 10.15, D10.1.1
**Human refs (from References field):** D10.1.1
**Jaccard:** 0.500 — AI adds ['10.15']

## Proposition 10.17
**Statement:** If there be two unequal straight lines, and to the greater there be applied a parallelogram equal to the fourth part of the square on the less and deficient by a square figure, and if it divide it into parts which are commensurable in length, then the square on the greater will be greater than the square on the less by the square on a straight line commensurable with the greater. And, if the square on the greater be greater than the square on the less by the square on a straight line commensurable with  the greater, and if there be applied to the greater a parallelogram equal to the fourth part of the square on the less and deficient by a square figure, it will divide it into parts which are commensurable in length.

**Step 1.** Let the greater straight line have length a and the less length b, so that a>b. Write Q(t) for the square on a length t and R(s,t) for the rectangle contained by lengths s and t. Suppose the given application divides a into two parts x and y. Since the deficiency is a square, the applied parallelogram is the rectangle contained by these two parts. Consequently,
 a=x+y, 4R(x,y)=Q(b).
[D1.22, D2.1; hypothesis; CN2]

**Step 2.** The two parts are unequal. Indeed, cut off from a a length equal to b. Proposition 2.4 expresses Q(a) as Q(b) together with positive areas, so Q(a)>Q(b). But if x=y, the same proposition gives Q(a)=4Q(x)=4R(x,y)=Q(b), a contradiction. Denote the greater part by p and the less by q; thus a=p+q and p>q. [1.3, 2.4, CN5, D1.22, CN2; Step 1]

**Step 3.** Cut off from p a length equal to q, and call the remaining length d; thus p=q+d. We use 2.8 directly because it supplies exactly four times the applied rectangle, without requiring an auxiliary midpoint construction. Applied to p cut into q and d, it gives
 Q(p+q)=4R(p,q)+Q(d).
Since p+q=a and 4R(p,q)=Q(b), we therefore have
 Q(a)=Q(b)+Q(d). (∗)
[1.3, 2.8, CN1, CN2; Step 1]

**Step 4.** First suppose that the parts p and q are commensurable in length. There is then a straight-line measure u which measures both. Adding their collections of copies of u shows that u measures p+q=a; subtracting the collection constituting q from that constituting p shows that u measures p−q=d. Hence a and d are commensurable in length. Equation (∗) therefore proves that the square on the greater original line exceeds the square on the less by the square on a straight line commensurable with the greater. [D10.1.1, CN2, CN3; Step 3]

**Step 5.** Conversely, suppose that
 Q(a)=Q(b)+Q(c),
where c is commensurable in length with a, and consider any application of the stated kind. Its two parts determine d as above, and equation (∗) holds. Subtracting Q(b) from the two expressions for Q(a) gives Q(c)=Q(d). Therefore c=d: otherwise, by 2.4 and CN5, the greater of these two lengths would have the greater square. Thus a and d are commensurable in length. [CN3, 2.4, CN5, D10.1.1; Step 3]

**Step 6.** Let u be a common measure of a and d, and bisect u into two equal lengths v. Since u measures both a and d, subtraction shows that u measures a−d. But
 a−d=(p+q)−(p−q)=2q.
Thus 2q consists of a whole number of copies of u, and q consists of the same number of copies of v. Hence v measures q. It also measures a, since each copy of u consists of two copies of v; consequently it measures a−q=p. The two parts p and q therefore have the common measure v and are commensurable in length. This proves the converse and completes both directions. [D10.1.1, 1.10, CN2, CN3; Steps 3–5]

**USED:** 1.10, 1.3, 2.4, 2.8, CN1, CN2, CN3, CN5, D1.22, D10.1.1, D2.1
**Human refs (from References field):** 10.12, 10.15, 10.6, 2.5
**Jaccard:** 0.000 — AI adds ['1.10', '1.3', '2.4', '2.8', 'CN1', 'CN2', 'CN3', 'CN5', 'D1.22', 'D10.1.1', 'D2.1']; Human adds ['10.12', '10.15', '10.6', '2.5']

## Proposition 10.18
**Statement:** If there be two unequal straight lines, and to the greater there be applied a parallelogram equal to the fourth part of the square on the less and deficient by a square figure, and if it divide it into parts which are incommensurable, the square on the greater will be greater than the square on the less by the square on a straight line incommensurable with the greater. And, if the square on the greater be greater than the square on the less by the square on a straight line incommensurable with the greater, and if there be applied to the greater a parallelogram equal to the fourth part of the square on the less and deficient by a square figure, it divides it into parts which are incommensurable. Let A, BC be two unequal straight lines, of which BC is the greater, and to BC let there be applied a parallelogram equal to the fourth part of the square on the less, A, and deficient by a square figure.

**Step 1.** Let D be the point at which the given applied parallelogram divides BC, so that the parts are BD and DC. Write Q(X) for the area of the square on a straight line X. We use the two implications of 10.17 by contradiction: this is the direct route because that proposition concerns exactly the same application of area and supplies the commensurable alternative. [10.17]

**Step 2.** Since BC is greater than A, cut off BF equal to A from BC. [1.3] By 2.4, Q(BC) equals Q(BF), together with Q(FC) and twice the rectangle contained by BF and FC. Consequently Q(BC) is greater than Q(A). [2.4, CN5] Place the smaller square at a corner within the larger; their difference is a rectilineal area. Construct a square equal to this remainder, and call its side E. Thus
Q(BC) = Q(A) + Q(E). [2.14]

**Step 3.** First suppose that BD and DC are incommensurable in length. If E were commensurable with BC, the converse implication of 10.17, applied to the equality in Step 2 and to the given parallelogram, would make BD and DC commensurable in length. This contradicts the hypothesis. Therefore E is incommensurable with BC, and the equality in Step 2 proves the first assertion. [10.17, D10.1.1]

**Step 4.** Conversely, suppose that
Q(BC) = Q(A) + Q(T),
where T is incommensurable in length with BC. Suppose, for a contradiction, that the given application divides BC into parts BD and DC which are commensurable in length. The forward implication of 10.17 then supplies a straight line U commensurable with BC such that
Q(BC) = Q(A) + Q(U). [10.17]
The two sums are equal to the same area; subtracting their common area Q(A) therefore gives Q(T) = Q(U). [CN1, CN3]

**Step 5.** The straight lines T and U must be equal. For, if they were unequal, cutting from the greater a length equal to the less and applying 2.4 would express the square on the greater as the square on the less together with positive additional areas, contrary to Q(T) = Q(U). [1.3, 2.4, CN5] Since U is commensurable with BC, a common measure of U and BC would consequently measure T also. This contradicts the assumed incommensurability of T and BC. Hence BD and DC are incommensurable in length, proving the converse and completing both assertions. [D10.1.1]

**USED:** 1.3, 10.17, 2.14, 2.4, CN1, CN3, CN5, D10.1.1
**Human refs (from References field):** 10.13, 10.16, 10.17, 10.6
**Jaccard:** 0.091 — AI adds ['1.3', '2.14', '2.4', 'CN1', 'CN3', 'CN5', 'D10.1.1']; Human adds ['10.13', '10.16', '10.6']

## Proposition 10.19
**Statement:** The rectangle contained by rational straight lines commensurable in length is rational.

**Step 1.** Let a and b be rational straight lines commensurable in length, and let R be the rectangle contained by them (D2.1). Let u be the assigned rational straight line (D10.1.3). Describe the square Q on a and the square U on u (1.46).

**Step 2.** Compare R directly with Q: this is the natural path because they have the same height a, with respective bases b and a. Parallelograms of the same height are to one another as their bases; therefore a:b = Q:R (6.1).

**Step 3.** Since a and b are commensurable in length, the proportion in Step 2 implies that Q and R are commensurable (10.11). This directly transfers the given commensurability to the areas, without introducing numerical ratios.

**Step 4.** Since a is rational, it is commensurable in square with the assigned straight line u (D10.1.3). Hence their squares Q and U are commensurable (D10.1.2).

**Step 5.** Thus R and U are each commensurable with Q, so they are commensurable with one another (10.12). An area commensurable with the square U on the assigned rational straight line is rational (D10.1.4). Therefore the rectangle contained by rational straight lines commensurable in length is rational.

**USED:** 1.46, 10.11, 10.12, 6.1, D10.1.2, D10.1.3, D10.1.4, D2.1
**Human refs (from References field):** 10.11, 6.1, D10.1.4
**Jaccard:** 0.375 — AI adds ['1.46', '10.12', 'D10.1.2', 'D10.1.3', 'D2.1']

## Proposition 10.20
**Statement:** If a rational area be applied to a rational straight line, it produces as breadth a straight line rational and commensurable in length with the straight line to which it is applied.

**Step 1.** Let u be the assigned rational straight line, a the given rational straight line, and R the given rational area. Suppose R is applied to a with breadth b; thus R is the rectangle contained by a and b (D2.1). Construct the squares U, S, and T on u, a, and b respectively (1.46).

**Step 2.** Since a is rational, its square S is commensurable with U (D10.1.2, D10.1.3). Since R is rational, R is likewise commensurable with U (D10.1.4). Therefore S and R are commensurable with one another (10.12).

**Step 3.** Regard S and R as parallelograms of equal height a, with bases a and b respectively. Then S : R = a : b (6.1). Consequently a and b are commensurable in length (10.11). This is the direct path: the equal-height proportion makes the commensurability-transfer principle immediately applicable, without introducing numerical ratios.

**Step 4.** Regard R and T as parallelograms of equal height b, with bases a and b respectively. Then R : T = a : b (6.1). Since a and b are commensurable in length, the same transfer principle shows that R and T are commensurable (10.11).

**Step 5.** Both T and U are commensurable with R, by Steps 4 and 2. Hence T and U are commensurable with one another (10.12). Thus b is commensurable in square with the assigned rational straight line u, and is therefore rational (D10.1.2, D10.1.3). Together with Step 3, this proves that the breadth b is rational and commensurable in length with the straight line a to which the rational area was applied.

**USED:** 1.46, 10.11, 10.12, 6.1, D10.1.2, D10.1.3, D10.1.4, D2.1
**Human refs (from References field):** 10.11, 6.1, D10.1.4
**Jaccard:** 0.375 — AI adds ['1.46', '10.12', 'D10.1.2', 'D10.1.3', 'D2.1']

## Proposition 10.21
**Statement:** The rectangle contained by rational straight lines commensurable in square only is irrational, and the side of the square equal to it is irrational. Let the latter be called medial.

**Step 1.** Let a and b be rational straight lines commensurable in square only. Thus their squares have a common area-measure, but a and b have no common length-measure [D10.1.1, D10.1.2]. Let R be the rectangle contained by a and b [D2.1].

**Step 2.** Use 10.20 directly, since R is already an area applied to the rational straight line a, with breadth b. If R were rational, its breadth b would be commensurable in length with a [10.20]. This contradicts Step 1. Therefore R is not rational.

**Step 3.** A rational area is one commensurable with the square on the assigned rational straight line, whereas an area incommensurable with that square is irrational. Since R is not rational, it is therefore irrational [D10.1.4].

**Step 4.** Construct a square equal to R, and let c be its side [2.14]. By the definition of an irrational straight line producing an irrational area, the side of a square equal to the irrational area R is irrational [D10.1.4]. Hence both the rectangle contained by a and b and the side c of the square equal to it are irrational. Let this side c be called medial.

**USED:** 10.20, 2.14, D10.1.1, D10.1.2, D10.1.4, D2.1
**Human refs (from References field):** 10.11, 6.1, D10.1.4
**Jaccard:** 0.125 — AI adds ['10.20', '2.14', 'D10.1.1', 'D10.1.2', 'D2.1']; Human adds ['10.11', '6.1']

## Proposition 10.22
**Statement:** The square on a medial straight line, if applied to a rational straight line, produces as breadth a straight line rational and incommensurable in length with that to which it is applied.

**Step 1.** Write Q(x) for the square on a straight line x, and R(x,y) for the rectangle contained by x and y. Let m be medial, let r be rational, and let s be the breadth obtained by applying Q(m) to r, so that R(r,s) = Q(m) (D2.1). By the meaning of medial in 10.21, there are rational straight lines a and b, commensurable in square only, such that Q(m) = R(a,b); moreover, this area is irrational (10.21).

**Step 2.** The rectangles R(a,b) and R(r,s) are equal (CN1). Therefore a:r = s:b (6.16), and consequently
Q(a):Q(r) = Q(s):Q(b) (6.22).
We use 6.22 here because the four proportional straight lines have already been obtained, and it gives the required proportion of their squares directly.

**Step 3.** Let u be the assigned rational straight line. Since a, r, and b are rational, Q(a), Q(r), and Q(b) are each commensurable with Q(u) (D10.1.2, D10.1.3). Hence Q(a) and Q(r) are commensurable with one another (10.12).

**Step 4.** Applying 10.11 to the proportion in Step 2, the commensurability of Q(a) with Q(r) implies that Q(s) is commensurable with Q(b). Since Q(b) is commensurable with Q(u), Q(s) is also commensurable with Q(u) (10.12). Thus s is commensurable in square with the assigned rational straight line and is therefore rational (D10.1.2, D10.1.3).

**Step 5.** To establish incommensurability in length, use 10.19, which now applies directly if the two rational sides r and s are assumed commensurable in length. Under that assumption, R(r,s) would be a rational area (10.19). But R(r,s) = R(a,b), and the latter area is irrational (Step 1; 10.21), contradicting the distinction between rational and irrational areas (D10.1.4). Therefore s is incommensurable in length with r. Together with Step 4, this proves that the breadth is rational and incommensurable in length with the rational straight line to which the square on the medial straight line is applied.

**USED:** 10.11, 10.12, 10.19, 10.21, 6.16, 6.22, CN1, D10.1.2, D10.1.3, D10.1.4, D2.1
**Human refs (from References field):** 10.11, 10.13, 10.21, 6.14, 6.22, D10.1.4
**Jaccard:** 0.308 — AI adds ['10.12', '10.19', '6.16', 'CN1', 'D10.1.2', 'D10.1.3', 'D2.1']; Human adds ['10.13', '6.14']

## Proposition 10.23
**Statement:** A straight line commensurable with a medial straight line is medial.

**Step 1.** Let m be a medial straight line and n a straight line commensurable with it. Write Q(x) for the square on a straight line x. Then Q(m) and Q(n) are commensurable: if the given commensurability is in square, this is its definition; if it is in length, their squares have the ratio of a square number to a square number and hence are commensurable. [D10.1.2, 10.9, 10.6]

**Step 2.** By the definition of medial in 10.21, there are rational straight lines r and s, commensurable in square only, such that Q(m) equals the rectangle contained by r and s. We choose the direct route of keeping r fixed in this defining rectangle, so that a ratio of areas becomes a ratio of the remaining sides. [10.21]

**Step 3.** Construct a third proportional t to r and n, so that r:n = n:t. The rectangle contained by r and t therefore equals Q(n). [6.11, 6.17]

**Step 4.** Regard the rectangles contained by r,s and by r,t as having the same height r. Their areas are consequently in the ratio s:t; thus Q(m):Q(n) = s:t. Since Q(m) and Q(n) are commensurable by Step 1, s and t are commensurable in length. [6.1, 10.11]

**Step 5.** Since s and t are commensurable in length, Q(s) and Q(t) have the ratio of a square number to a square number and hence are commensurable. Let u be the assigned rational straight line. Since s is rational, Q(s) is commensurable with Q(u). Therefore Q(t) is commensurable with Q(u), and t is rational. [10.9, 10.6, D10.1.3, 10.12]

**Step 6.** The squares Q(r) and Q(s) are commensurable by Step 2, while Q(t) and Q(s) are commensurable by Step 5. Hence Q(r) and Q(t) are commensurable, so r and t are commensurable in square. But s is incommensurable in length with r, and t is commensurable in length with s; therefore t is incommensurable in length with r. Thus r and t are rational straight lines commensurable in square only. [10.12, D10.1.2, 10.13]

**Step 7.** By Step 3, Q(n) equals the rectangle contained by r and t. Since these are rational straight lines commensurable in square only, the side of the square equal to their rectangle is medial. That side is n. Therefore a straight line commensurable with a medial straight line is medial. [10.21]

**USED:** 10.11, 10.12, 10.13, 10.21, 10.6, 10.9, 6.1, 6.11, 6.17, D10.1.2, D10.1.3
**Human refs (from References field):** 10.11, 10.13, 10.21, 10.22, 6.1, D10.1.3
**Jaccard:** 0.417 — AI adds ['10.12', '10.6', '10.9', '6.11', '6.17', 'D10.1.2']; Human adds ['10.22']

## Proposition 10.24
**Statement:** The rectangle contained by medial straight lines commensurable in length is medial.

**Step 1.** Let a and b be medial straight lines commensurable in length. Write [x,y] for the area of the rectangle contained by x and y, and x² for the square on x. Let r be the assigned rational straight line. We must prove that [a,b] is medial. [D2.1, D10.1.3]

**Step 2.** Path choice: apply a² and [a,b] to the same rational straight line, so that 10.22 leads directly toward the characterization in 10.21. Construct fourth proportionals u and v such that r:a = a:u and r:a = b:v. Then [r,u] = a² and [r,v] = [a,b], since in proportional straight lines the rectangle contained by the extremes equals that contained by the means. [6.12, 6.16]

**Step 3.** Since a is medial and its square has been applied to the rational straight line r with breadth u, the straight line u is rational and incommensurable in length with r. Consequently u² is commensurable with r². [10.22, D10.1.3]

**Step 4.** Rectangles of the same height are proportional to their bases. Thus u:v = [r,u]:[r,v], while a:b = a²:[a,b]. By the equalities in Step 2, these give u:v = a:b. Since a and b are commensurable in length, u and v are commensurable in length. Here 10.11 is the natural direct transfer theorem for the proportion, rather than passing through numerical ratios. [6.1, 5.11, 10.11]

**Step 5.** Because u and v are commensurable in length, u² and v² have the ratio of a square number to a square number, and hence are commensurable. But u² is also commensurable with r² by Step 3. Therefore v² is commensurable with r², so v is rational and commensurable in square with r. [10.9, 10.6, 10.12, D10.1.2, D10.1.3]

**Step 6.** The straight lines u and v are commensurable in length, whereas u and r are incommensurable in length. Therefore v and r are also incommensurable in length. Together with Step 5, this shows that r and v are rational straight lines commensurable in square only. [10.13, D10.1.2]

**Step 7.** The side of a square equal to the rectangle contained by rational straight lines commensurable in square only is medial. Hence [r,v] is a medial area. Since [r,v] = [a,b] by Step 2, the rectangle contained by the given medial straight lines a and b is medial, as required. [10.21]

**USED:** 10.11, 10.12, 10.13, 10.21, 10.22, 10.6, 10.9, 5.11, 6.1, 6.12, 6.16, D10.1.2, D10.1.3, D2.1
**Human refs (from References field):** 10.11, 10.23, 6.1
**Jaccard:** 0.133 — AI adds ['10.12', '10.13', '10.21', '10.22', '10.6', '10.9', '5.11', '6.12', '6.16', 'D10.1.2', 'D10.1.3', 'D2.1']; Human adds ['10.23']

## Proposition 10.25
**Statement:** The rectangle contained by medial straight lines commensurable in square only is either rational or medial.

**Step 1.** Let a and b be the given medial straight lines, commensurable in square only, and let u be the assigned rational straight line. Write S(t) for the square on t and R(s,t) for the rectangle contained by s and t. Thus S(a) and S(b) are commensurable. We shall express R(a,b) as a rectangle with rational sides. [D2.1, D10.1.2, D10.1.3]

**Step 2.** Construct a third proportional x to u and a, so that u:a = a:x. Then R(u,x) = S(a). This is the square on the medial straight line a applied to the rational straight line u; consequently its breadth x is rational. In particular, S(x) is commensurable with S(u). [6.11, 6.17, 10.22, D10.1.2, D10.1.3]

**Step 3.** Construct a fourth proportional y to a, b, and x, so that a:b = x:y. The squares on these proportional straight lines are proportional, giving S(a):S(b) = S(x):S(y). The direct application to squares is the chosen route, since it immediately matches the given square-commensurability. [6.12, 6.22]

**Step 4.** Since S(a) and S(b) are commensurable, the proportion in Step 3 implies that S(x) and S(y) are commensurable. But S(x) is also commensurable with S(u), by Step 2. Therefore S(y) is commensurable with S(u), and y is rational. [10.11, 10.12, D10.1.2, D10.1.3]

**Step 5.** Rectangles with the same height are to one another as their bases. Hence
S(a):R(a,b) = a:b,
and
R(u,x):R(u,y) = x:y.
Combining these equalities with Step 3 gives S(a):R(a,b) = R(u,x):R(u,y). Since S(a) = R(u,x), the same magnitude has the same ratio to R(a,b) and R(u,y); therefore R(a,b) = R(u,y). [6.1, 5.11, 5.9]

**Step 6.** If u and y are commensurable in length, their rectangle R(u,y) is rational, since both sides are rational. Thus the equal rectangle R(a,b) is rational. [10.19; Step 5]

**Step 7.** If u and y are incommensurable in length, they are nevertheless commensurable in square by Step 4. They are therefore rational straight lines commensurable in square only. By 10.21, the side of a square equal to R(u,y) is medial; that is, R(u,y) is a medial area. Thus R(a,b) is medial by Step 5. The two cases exhaust the possibilities, so the rectangle contained by the given medial straight lines is either rational or medial. [D10.1.1, D10.1.2, 10.21]

**USED:** 10.11, 10.12, 10.19, 10.21, 10.22, 5.11, 5.9, 6.1, 6.11, 6.12, 6.17, 6.22, D10.1.1, D10.1.2, D10.1.3, D2.1
**Human refs (from References field):** 10.11, 10.19, 10.21, 10.22, 5.11, 6.1, 6.17
**Jaccard:** 0.438 — AI adds ['10.12', '5.9', '6.11', '6.12', '6.22', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D2.1']

## Proposition 10.26
**Statement:** A medial area does not exceed a medial area by a rational area.

**Step 1.** Suppose, to the contrary, that medial areas M and N satisfy M = N + R, where R is a positive rational area. Let r be the assigned rational straight line, and let U be its square. Thus rational areas are precisely those commensurable with U. [D10.1.3, D10.1.4]

**Step 2.** Apply N and R as adjacent rectangles with the same side r, and call their respective breadths y and z. Such applications are obtained by dividing the figures into triangles and applying those triangles successively in a right angle. Put x = y + z. The combined rectangle contained by r and x equals N + R, hence M. The chosen route is application to a common rational line, because it makes the breadth criteria directly applicable. [P1, 1.44, 2.1, CN2]

**Step 3.** Since the rectangles contained by r and x, and by r and y, are medial, x and y are rational straight lines, each incommensurable in length with r. Since the rectangle contained by r and z is rational, z is rational and commensurable in length with r. [10.22, 10.20]

**Step 4.** Write x², y², and z² for the squares on these straight lines. Since x, y, and z are rational, all three squares are commensurable with U. [D10.1.2, D10.1.3]

**Step 5.** The areas y² and z² are commensurable with one another, since both are commensurable with U. Their sum S = y² + z² is therefore commensurable with y², and consequently with U. Since x² is also commensurable with U, x² and S are commensurable. [10.12, 10.15]

**Step 6.** Let T be the rectangle contained by y and z. Because x = y + z, the square on x equals the squares on y and z together with twice their rectangle; thus x² = S + 2T. Since this whole x² is commensurable with its part S, the converse part of 10.15 shows that S and 2T are commensurable. Hence 2T is commensurable with U. [2.4, 10.15, 10.12]

**Step 7.** The area T itself measures both T and 2T, so these areas are commensurable. Since 2T is commensurable with U, T is commensurable with U and is therefore rational. [D10.1.1, 10.12, D10.1.4]

**Step 8.** Apply this rational rectangle T to its rational side z; its breadth is y. Proposition 10.20 is the direct, earlier applicable criterion here: it gives that y is commensurable in length with z, without requiring a separate classification of the rectangle. But z is commensurable in length with r, so y is commensurable in length with r, contrary to Step 3. Therefore a medial area cannot exceed a medial area by a rational area. [10.20, 10.12, 10.22]

**USED:** 1.44, 10.12, 10.15, 10.20, 10.22, 2.1, 2.4, CN2, D10.1.1, D10.1.2, D10.1.3, D10.1.4, P1
**Human refs (from References field):** 10.11, 10.13, 10.16, 10.20, 10.22, 10.6, 2.4, D10.1.4
**Jaccard:** 0.235 — AI adds ['1.44', '10.12', '10.15', '2.1', 'CN2', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'P1']; Human adds ['10.11', '10.13', '10.16', '10.6']

## Proposition 10.27
**Statement:** To find medial straight lines commensurable in square only which contain a rational rectangle.

**Step 1.** Write a² for the square on a straight line a, and ab for the rectangle contained by straight lines a and b (D2.1). Let r be the assigned rational straight line. By 10.10, construct s commensurable in square only with r. Thus s is rational, its square is commensurable with r², and s is incommensurable in length with r (D10.1.2, D10.1.3).

**Step 2.** Construct a third proportional t to s and r, so that s:r = r:t (6.11). Then st = r² (6.17). The area r² is rational (D10.1.4); therefore, when it is applied to the rational straight line s, its breadth t is rational and commensurable in length with s (10.20). Since s is incommensurable in length with r, so is t (10.13). But t, being rational, is commensurable in square with the assigned line r. Consequently r and t are commensurable in square only (D10.1.2, D10.1.3).

**Step 3.** Construct a mean proportional x between r and s, and a mean proportional y between r and t (6.13). Then x² = rs and y² = rt (6.17). Both x and y are medial by 10.21, since each is the side of a square equal to the rectangle contained by rational straight lines commensurable in square only. This is the chosen construction: mean proportionals establish mediality directly.

**Step 4.** Rectangles with the same height are proportional to their bases (6.1), so
x²:y² = rs:rt = s:t.
Since s and t are commensurable in length, x² and y² are commensurable as areas (10.11). Hence x and y are commensurable in square (D10.1.2).

**Step 5.** Again, using r² = st and 6.1,
s²:r² = s²:st = s:t.
Together with Step 4, this gives x²:y² = s²:r² (5.11). The converse of 6.22 therefore gives x:y = s:r. This is the natural conversion here because the established proportion already concerns squares. Since s and r are incommensurable in length, x and y are also incommensurable in length (10.11). Combined with Step 4, they are commensurable in square only (D10.1.2).

**Step 6.** Finally, the established area equalities and 6.1 give
x²:r² = rs:st = r:t,
and
r²:y² = st:rt = s:r.
But r:t = s:r by construction. Therefore x²:r² = r²:y² (5.11). Applying the converse of 6.22 to these squares yields x:r = r:y, and hence xy = r² (6.17). The rectangle xy is thus rational (D10.1.4). Accordingly, the constructed medial straight lines x and y are commensurable in square only and contain a rational rectangle, as required.

**USED:** 10.10, 10.11, 10.13, 10.20, 10.21, 5.11, 6.1, 6.11, 6.13, 6.17, 6.22, D10.1.2, D10.1.3, D10.1.4, D2.1
**Human refs (from References field):** 10.11, 10.21, 10.23, 5.16, 6.12, 6.13, 6.17
**Jaccard:** 0.222 — AI adds ['10.10', '10.13', '10.20', '5.11', '6.1', '6.11', '6.22', 'D10.1.2', 'D10.1.3', 'D10.1.4', 'D2.1']; Human adds ['10.23', '5.16', '6.12']

## Proposition 10.28
**Statement:** To find medial straight lines commensurable in square only which contain a medial rectangle.

**Step 1.** The ratios 2:3, 4:5, and 5:6 are not ratios of square numbers. For if any were a ratio of square numbers, there would be a mean proportional number between those square numbers [8.11], and hence a mean proportional number between the corresponding consecutive numbers [8.8]. Such a mean must lie strictly between its unequal extremes [D7.20], but no number lies strictly between consecutive numbers [D7.2].

**Step 2.** Let r be the assigned rational straight line [D10.1.3]. By repeatedly laying off r along a straight line, construct a = 2r, b = 3r, and c = 5r [P2, P3]. Construct p as a mean proportional between r and c, and q as a mean proportional between a and b [6.13]. Here and below, u² denotes the square on u, and uv the rectangle contained by u and v [D2.1]. Thus
p² = rc,   q² = ab [6.17],
and, by repeated distribution of rectangles,
a² = 4r²,   b² = 9r²,   p² = 5r²,   q² = 6r² [2.1].
Path choice: mean proportionals are used because their defining proportions immediately supply the rectangle equalities needed in the construction [6.17].

**Step 3.** The lines a and b are commensurable in length with r, since r measures both; consequently they are rational [D10.1.1, D10.1.3]. The lines p and q are also rational, since their squares are measured by r² [D10.1.2, D10.1.3]. Moreover, each of the pairs a,p; b,p; and p,q is commensurable in square, since r² measures all four squares [D10.1.2].

**Step 4.** From Step 2,
a²:p² = 4:5,   p²:q² = 5:6 [D5.5].
Neither ratio is a ratio of square numbers, by Step 1. Therefore a and p are incommensurable in length, as are p and q [10.9]. Since a and b are commensurable in length, the incommensurability of a with p also implies that b and p are incommensurable in length [10.13]. Thus a,p; b,p; and p,q are each pairs of rational straight lines commensurable in square only [D10.1.2].

**Step 5.** Construct x as a mean proportional between a and p, and y as a mean proportional between b and p [6.13]. Then
x² = ap,   y² = bp [6.17].
Because a,p and b,p are pairs of rational straight lines commensurable in square only, the sides of squares equal to their rectangles are medial. Hence both x and y are medial [10.21].

**Step 6.** Rectangles having the same height are as their bases, so
x²:y² = ap:bp = a:b = 2:3 [6.1, D5.5].
Their squares are therefore commensurable [10.6], and x and y are commensurable in square [D10.1.2]. But 2:3 is not a ratio of square numbers, by Step 1; hence x and y are incommensurable in length [10.9]. They are consequently commensurable in square only.

**Step 7.** Using the rectangle equalities from Steps 2 and 5, and comparing rectangles of equal height, we have
x²:p² = ap:p² = a:p,
and
q²:y² = ab:bp = a:p [6.1].
Therefore x²:p² = q²:y² [5.11]. Since proportional squares have proportional sides,
x:p = q:y [6.22].
It follows that the rectangle contained by the extremes equals that contained by the means:
xy = pq [6.16].

**Step 8.** The lines p and q are rational and commensurable in square only, by Steps 3–4. Accordingly, the side of a square equal to pq is medial; that is, pq is a medial area [10.21]. Since xy = pq, the rectangle contained by x and y is medial. This identifies the required area directly, without a rational-or-medial case distinction. Thus x and y are medial straight lines, commensurable in square only, which contain a medial rectangle, as required.

**USED:** 10.13, 10.21, 10.6, 10.9, 2.1, 5.11, 6.1, 6.13, 6.16, 6.17, 6.22, 8.11, 8.8, D10.1.1, D10.1.2, D10.1.3, D2.1, D5.5, D7.2, D7.20, P2, P3
**Human refs (from References field):** 10.11, 10.21, 10.23, 5.16, 6.12, 6.13, 6.16, 6.17
**Jaccard:** 0.154 — AI adds ['10.13', '10.6', '10.9', '2.1', '5.11', '6.1', '6.22', '8.11', '8.8', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D2.1', 'D5.5', 'D7.2', 'D7.20', 'P2', 'P3']; Human adds ['10.11', '10.23', '5.16', '6.12']

## Proposition 10.29
**Statement:** To find two rational straight lines commensurable in square only and such that the square on the greater is greater than the square on the less by the square on a straight line commensurable in length with the greater.

**Step 1.** Let AB be the assigned rational straight line (D10.1.3). Choose an equilateral-triangle construction, so that an altitude will give the required difference of squares. Construct the equilateral triangle ABC on AB (1.1), bisect AB at D (1.10), and join CD (P1). Write Q(XY) for the square on a straight line XY.

**Step 2.** The triangles ADC and BDC have AD = DB, AC = BC, and CD common. Therefore their angles ADC and BDC are equal (1.8). These are adjacent angles on the straight line AB, so both are right angles (D1.10).

**Step 3.** Since AB is divided into equal parts at D, the square-of-a-sum identity gives Q(AB) = 4Q(AD) (2.4). Since triangle ADC is right-angled and AC = AB, we also have Q(AB) = Q(CD) + Q(AD) (1.47). Subtracting Q(AD) gives Q(CD) = 3Q(AD) (CN3). Consequently Q(AB) : Q(CD) = 4 : 3 (D5.5).

**Step 4.** The ratio 4 : 3 cannot be the ratio of a square number to a square number. For, between any two square numbers there is a mean proportional number (8.11). If their ratio were 4 : 3, a mean proportional number N would therefore also exist between 4 and 3 (8.8). Thus 4 : N = N : 3, which forces 3 < N < 4 (D7.20). But no number, being a multitude of units, lies strictly between the consecutive numbers 3 and 4 (D7.2). This is impossible.

**Step 5.** Apply the square-ratio criterion, which is directly suited to the ratio obtained in Step 3: since Q(AB) : Q(CD) is not the ratio of a square number to a square number, AB and CD are incommensurable in length (10.9). On the other hand, Q(AD) measures their squares four times and three times respectively, so AB and CD are commensurable in square (D10.1.2). They are therefore commensurable in square only.

**Step 6.** AB is the assigned rational straight line, and CD is commensurable with it in square only. Hence both AB and CD are rational straight lines (D10.1.3). Furthermore, AD measures AB twice, so AD is commensurable in length with AB (D10.1.1).

**Step 7.** Step 3 gives Q(AB) = Q(CD) + Q(AD); hence Q(AB) is greater than Q(CD) (CN5). Thus AB is greater than CD, since a greater straight line has a greater square by 2.4. The square on AB therefore exceeds the square on CD by Q(AD), the square on a straight line commensurable in length with AB by Step 6. Accordingly AB and CD are the two required rational straight lines, commensurable in square only, with the stipulated excess. ∎

**USED:** 1.1, 1.10, 1.47, 1.8, 10.9, 2.4, 8.11, 8.8, CN3, CN5, D1.10, D10.1.1, D10.1.2, D10.1.3, D5.5, D7.2, D7.20, P1
**Human refs (from References field):** 1.47, 10.6, 10.9, 3.31, 5.19, D10.1.4
**Jaccard:** 0.091 — AI adds ['1.1', '1.10', '1.8', '2.4', '8.11', '8.8', 'CN3', 'CN5', 'D1.10', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D5.5', 'D7.2', 'D7.20', 'P1']; Human adds ['10.6', '3.31', '5.19', 'D10.1.4']

## Proposition 10.30
**Statement:** To find two rational straight lines commensurable in square only and such that the square on the greater is greater is greater than the square on the less by the square on a straight line incommensurable in length with the greater.

**Step 1.** Let AB be the assigned rational straight line (D10.1.3). Construct the square ABCD on AB and join AC (1.46; P1). We choose the side and diagonal of a square because the excess of their squares will itself be the square on the side, making the two required incommensurability assertions identical. Write Q for the area of ABCD. Since ABCD is a square, AB = BC and angle ABC is right (D1.22).

**Step 2.** By the right-triangle theorem, the square on AC equals the squares on AB and BC together, and therefore equals 2Q (1.47). Thus Q measures both the square on AB and the square on AC, so AB and AC are commensurable in square (D10.1.2). Also, each remaining angle of triangle ABC is less than its right angle (1.17); hence AC > AB, since the greater angle subtends the greater side (1.19).

**Step 3.** We use the square-ratio criterion (10.9), since the construction has immediately determined the ratio of the squares. Suppose that AC and AB were commensurable in length. Their squares would then have the ratio of a square number to a square number (10.9). Denote these square numbers by m² and n², where m and n are their numerical sides (D7.18). Since the square on AC is twice Q, this proportion gives m² = 2n² (D5.5).

**Step 4.** Consequently n² measures m², so n measures m (8.14). The equality m² = 2n² implies m > n; therefore, as m is a multiple of n, m is at least twice n. By multiplication as repeated addition and the definition of a square number, m² is then at least four times n², contradicting m² = 2n² (D7.15; D7.18). Hence AC and AB are incommensurable in length. Together with Step 2, this proves that they are commensurable in square only (D10.1.2).

**Step 5.** AB is rational by its choice, and AC is rational because its square is commensurable with the square on the assigned rational line AB (D10.1.3). Subtracting Q from the equality established in Step 2, the square on AC exceeds the square on AB by Q, which is the square on AB itself (CN3). But AB is incommensurable in length with AC by Step 4. Thus AC and AB are the required rational straight lines, commensurable in square only, whose greater square exceeds the lesser by the square on a straight line incommensurable in length with the greater.

**USED:** 1.17, 1.19, 1.46, 1.47, 10.9, 8.14, CN3, D1.22, D10.1.2, D10.1.3, D5.5, D7.15, D7.18, P1
**Human refs (from References field):** 1.47, 10.6, 10.9, 3.31, 5.19
**Jaccard:** 0.118 — AI adds ['1.17', '1.19', '1.46', '8.14', 'CN3', 'D1.22', 'D10.1.2', 'D10.1.3', 'D5.5', 'D7.15', 'D7.18', 'P1']; Human adds ['10.6', '3.31', '5.19']

## Proposition 10.31
**Statement:** To find two medial straight lines commensurable in square only, containing a rational rectangle, and such that the square on the greater is greater than the square on the less by the square on a straight line commensurable in length with the greater.

**Step 1.** Write x² for the square on a straight line x, and xy for the rectangle contained by x and y. By 10.29, construct rational straight lines a > b, commensurable in square only, such that a² = b² + d², where d is commensurable in length with a. Path choice: preserve the ratio a:b while constructing medial lines, so that the required square-difference condition can be transferred by 10.14.

**Step 2.** Construct a third proportional c to a and b, so that a:b = b:c (6.11). Then ac = b² (6.17). Since b is rational, b² is a rational area (D10.1.3, D10.1.4). Thus the rational area b², applied to the rational straight line a, has breadth c; consequently c is rational and commensurable in length with a (10.20).

**Step 3.** Since c is commensurable in length with a, while b is incommensurable in length with a, c and b are incommensurable in length (10.13). Since b and c are rational, their squares are each commensurable with the square on the assigned rational straight line, and therefore are commensurable with one another (D10.1.3, 10.12). Hence b and c are commensurable in square only (D10.1.2).

**Step 4.** Construct a mean proportional m between a and b, and a mean proportional n between b and c (6.13). Thus a:m = m:b and b:n = n:c, whence m² = ab and n² = bc (6.17). Each of the pairs a,b and b,c consists of rational straight lines commensurable in square only. Therefore m and n are both medial straight lines (10.21).

**Step 5.** Rectangles having the same height are to one another as their bases (6.1). Using the equalities established above gives
m²:n² = ab:bc = a:c = a²:ac = a²:b² (6.1, CN1).
Consequently m:n = a:b, by the converse part of 6.22 applied to the squares. Since a > b, it follows that m > n (5.14).

**Step 6.** The squares a² and b² are commensurable, so the proportional squares m² and n² are commensurable (10.11). But a and b are incommensurable in length, so the proportional straight lines m and n are incommensurable in length (10.11). Thus m and n are commensurable in square only (D10.1.2).

**Step 7.** From a:b = m:n, alternation gives a:m = b:n (5.16). Since a:m = m:b by the construction of m, it follows that m:b = b:n (5.11). Therefore mn = b² (6.17). As b² is rational, the rectangle contained by m and n is rational (D10.1.4).

**Step 8.** Apply 10.14 to the proportional straight lines a,b,m,n. Since a² exceeds b² by the square on a straight line commensurable in length with a, m² exceeds n² by the square on a straight line t commensurable in length with m. Thus the constructed medial straight lines m > n are commensurable in square only, contain a rational rectangle, and satisfy m² = n² + t² with t commensurable in length with m, as required.

**USED:** 10.11, 10.12, 10.13, 10.14, 10.20, 10.21, 10.29, 5.11, 5.14, 5.16, 6.1, 6.11, 6.13, 6.17, 6.22, CN1, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 10.11, 10.14, 10.21, 10.23, 10.29, 10.30
**Jaccard:** 0.190 — AI adds ['10.12', '10.13', '10.20', '5.11', '5.14', '5.16', '6.1', '6.11', '6.13', '6.17', '6.22', 'CN1', 'D10.1.2', 'D10.1.3', 'D10.1.4']; Human adds ['10.23', '10.30']

## Proposition 10.32
**Statement:** To find two medial straight lines commensurable in square only, containing a medial rectangle, and such that the square on the greater is greater than the square on the less by the square on a straight line commensurable with the greater.

**Step 1.** By 10.28, construct two medial straight lines a and b, commensurable in square only, whose rectangle R is medial; name the greater a. Thus a > b. **Construction choice:** begin with 10.28 because it already supplies the required medial rectangle, and impose the square-difference condition by a commensurable alteration of one side.

**Step 2.** Construct a third proportional c to a and b, so that a:b = b:c [6.11]. Then ac = b² [6.17]. Since a > b, the same proportion gives b > c [5.14], and therefore a > c. Rectangles with the same height are proportional to their bases, so

a:c = a²:ac = a²:b² [6.1].

The squares a² and b² are commensurable by Step 1. Hence a and c are commensurable in length, by direct transfer along this proportion [10.11].

**Step 3.** Adjoin a segment equal to c to a, forming a straight line of length a+c [P2, 1.3], and bisect the whole [1.10]. Let d be its half, and let e be the distance between its midpoint and the division separating a from c. Since a > c,

d = (a+c)/2,    e = (a−c)/2 > 0.

Take a common measure h of a and c. The half of h measures a, d, and e: if a consists of m copies of h and c of n copies, these three lines consist respectively of 2m, m+n, and m−n copies of h/2. Thus d is commensurable in length with both a and e [1.10, D10.1.1].

**Step 4.** Apply 2.5 to the segment of length a+c, divided equally at its midpoint and unequally into a and c. It gives

ac + e² = d².

Since ac = b² by Step 2, we obtain

d² = b² + e².

Consequently d² > b² and d > b [CN5, 6.20]. Moreover, d is medial, since it is commensurable in length with the medial line a [10.23]. The excess square e² already has a side commensurable in length with d, by Step 3.

**Step 5.** Because d and a are commensurable in length, their squares have the ratio of a square number to a square number [10.9], and therefore are commensurable [10.6]. Since a² and b² are also commensurable, d² and b² are commensurable [10.12]. Thus d and b are commensurable in square [D10.1.2]. They are not commensurable in length: otherwise their commensurability, together with that of d and a, would make a and b commensurable in length [10.12], contrary to Step 1. Hence d and b are commensurable in square only.

**Step 6.** Let S be the rectangle contained by d and b. Since R is the rectangle contained by a and b,

S:R = d:a [6.1].

As d and a are commensurable in length, S and R are commensurable areas [10.11]. The medial area R is irrational, and hence incommensurable with the square on the assigned rational straight line [10.21, D10.1.4]. Therefore S is likewise incommensurable with that square [10.13], so S is not rational [D10.1.4]. But d and b are medial straight lines commensurable in square only; their rectangle is consequently either rational or medial [10.25]. The rational alternative being excluded, S is medial.

**Step 7.** The constructed straight lines d and b are therefore medial and commensurable in square only; they contain a medial rectangle, and the square on the greater d exceeds the square on b by e², where e is commensurable in length with d [Steps 3–6]. These are the required straight lines.

**USED:** 1.10, 1.3, 10.11, 10.12, 10.13, 10.21, 10.23, 10.25, 10.28, 10.6, 10.9, 2.5, 5.14, 6.1, 6.11, 6.17, 6.20, CN5, D10.1.1, D10.1.2, D10.1.4, P2
**Human refs (from References field):** 10.11, 10.14, 10.21, 10.23, 10.29, 10.30, 6.16, 6.17, 6.4, 6.8
**Jaccard:** 0.143 — AI adds ['1.10', '1.3', '10.12', '10.13', '10.25', '10.28', '10.6', '10.9', '2.5', '5.14', '6.1', '6.11', '6.20', 'CN5', 'D10.1.1', 'D10.1.2', 'D10.1.4', 'P2']; Human adds ['10.14', '10.29', '10.30', '6.16', '6.4', '6.8']

## Proposition 10.33
**Statement:** To find two straight lines incommensurable in square which make the sum of the squares on them rational but the rectangle contained by them medial.

**Step 1.** Write u² for the square on a straight line u, and uv for the rectangle contained by u and v. By 10.30, construct rational straight lines a>b, commensurable in square only, such that

a²=b²+c²,

where c is incommensurable in length with a. This construction is chosen because its incommensurable square-difference supplies exactly what the sum-and-difference construction below requires. Since c²<a², we have c<a (CN5, 6.20).

**Step 2.** Extend a segment AC=a beyond C, and mark B so that CB=a; on CB mark D so that CD=c (P2, 1.3). Put p=AD and q=DB. Thus p=a+c, q=a−c, and p+q=2a. The line AB is cut equally at C and unequally at D, so 2.5 gives

pq+c²=a².

Comparing this with a²=b²+c² and subtracting c² gives pq=b² (CN3).

**Step 3.** The lines p and q are incommensurable in length. For suppose they were commensurable. Their sum p+q=2a would then be commensurable with p (10.15). Since a measures both a and 2a, those two lines are commensurable (D10.1.1); hence p would be commensurable with a (10.12). But p=a+c, so the converse part of 10.15 would make a and c commensurable, contrary to Step 1. Therefore p and q are incommensurable.

**Step 4.** Construct a mean proportional x between a and p, and a mean proportional y between a and q (6.13). By 6.17,

x²=ap, y²=aq.

These are the two straight lines to be found.

**Step 5.** By the distributive identity for rectangles (2.1),

x²+y²=ap+aq=a(p+q)=2a².

Because a is rational, a² is commensurable with the square on the assigned rational straight line (D10.1.3). Any common area measuring those two squares also measures 2a² (D10.1.1). Therefore x²+y² is a rational area (D10.1.4).

**Step 6.** Rectangles with the same height are proportional to their bases (6.1), so

x²:y²=ap:aq=p:q.

Since p and q are incommensurable, x² and y² are incommensurable by 10.11. Thus x and y are incommensurable in square (D10.1.2).

**Step 7.** Using the identities from Steps 2 and 4 and comparing rectangles of equal height (6.1), we have

x²:a²=ap:a²=p:a,

and

b²:y²=pq:aq=p:a.

Consequently x²:a²=b²:y² (5.11). Squares are similar figures, so the converse part of 6.22 gives x:a=b:y. Hence the rectangle contained by the extremes equals that contained by the means:

xy=ab (6.16).

**Step 8.** The lines a and b are rational and commensurable in square only. Therefore the square equal to their rectangle has a medial side, so ab is a medial area (10.21). By Step 7, xy is medial also. Thus x and y are incommensurable in square, the sum of their squares is rational, and the rectangle contained by them is medial, as required.

**USED:** 1.3, 10.11, 10.12, 10.15, 10.21, 10.30, 2.1, 2.5, 5.11, 6.1, 6.13, 6.16, 6.17, 6.20, 6.22, CN3, CN5, D10.1.1, D10.1.2, D10.1.3, D10.1.4, P2
**Human refs (from References field):** 1.47, 10.18, 10.21, 10.23, 10.30, 6.28
**Jaccard:** 0.077 — AI adds ['1.3', '10.11', '10.12', '10.15', '2.1', '2.5', '5.11', '6.1', '6.13', '6.16', '6.17', '6.20', '6.22', 'CN3', 'CN5', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.1.4', 'P2']; Human adds ['1.47', '10.18', '10.23', '6.28']

## Proposition 10.34
**Statement:** To find two straight lines incommensurable in square which make the sum of the squares on them medial but the rectangle contained by them rational.

**Step 1.** Write u² for the square on a straight line u, and uv for the rectangle contained by u and v. By 10.30, construct rational straight lines a > b, commensurable in square only, such that a² = b² + c², where c is incommensurable in length with a. In particular, a² > b² (CN5). This construction is chosen because its incommensurable remainder supplies exactly the hypothesis needed for 10.18, while a and b already contain a medial rectangle.

**Step 2.** Bisect b, and denote its half by h (1.10). Then b² = 4h² (2.4). Apply to a a rectangle equal to h² and deficient by a square, using 6.28; this is possible because h² = b²/4 < a²/4. Let the resulting parts of a be p and q. Since the deficiency is a square, the applied rectangle has sides p and q, so
p + q = a and pq = h² = b²/4.

**Step 3.** Since a² exceeds b² by c², and c is incommensurable in length with a, the converse assertion of 10.18 shows that the parts p and q are incommensurable in length.

**Step 4.** Construct x as a mean proportional between p and b (6.13), and construct y as a fourth proportional to x, b, h (6.12). Thus
p:x = x:b = h:y.
Consequently,
x² = bp (6.17), and xy = bh (6.16).

**Step 5.** We also have y² = bq. Indeed, pq = h² gives p:h = h:q (6.17). Alternating p:x = h:y gives p:h = x:y (5.16), and hence x:y = h:q (5.11). Alternating this last proportion and x:b = h:y gives, respectively,
x:h = y:q and x:h = b:y (5.16).
Therefore b:y = y:q (5.11), and so y² = bq (6.17).

**Step 6.** Adding the equalities for the squares and using p + q = a gives
x² + y² = bp + bq = b(p + q) = ba
(CN2; 2.1). Because a and b are rational and commensurable in square only, their rectangle ba is equal to the square on a medial straight line (10.21). Thus the sum of the squares on x and y is medial.

**Step 7.** Since b = h + h, we have b² = bh + bh (2.1). Therefore xy = bh is half of b². The square b² is rational because b is rational (D10.1.3; D10.1.4). Moreover, bh measures b² twice, so these areas are commensurable (D10.1.1). Hence bh is commensurable with the assigned rational square (10.12), and is therefore rational (D10.1.4). Thus the rectangle xy is rational.

**Step 8.** Rectangles with the same height are proportional to their bases, so
x²:y² = bp:bq = p:q (6.1).
Since p and q are incommensurable, 10.11 transfers their incommensurability directly to the squares x² and y². Therefore x and y are incommensurable in square (D10.1.2). The constructed straight lines x and y consequently have all three required properties: they are incommensurable in square, the sum of their squares is medial, and their rectangle is rational.

**USED:** 1.10, 10.11, 10.12, 10.18, 10.21, 10.30, 2.1, 2.4, 5.11, 5.16, 6.1, 6.12, 6.13, 6.16, 6.17, 6.28, CN2, CN5, D10.1.1, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 1.47, 10.11, 10.18, 10.31, 10.6, 3.31, 6.28
**Jaccard:** 0.115 — AI adds ['1.10', '10.12', '10.21', '10.30', '2.1', '2.4', '5.11', '5.16', '6.1', '6.12', '6.13', '6.16', '6.17', 'CN2', 'CN5', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.1.4']; Human adds ['1.47', '10.31', '10.6', '3.31']

## Proposition 10.35
**Statement:** To find two straight lines incommensurable in square which make the sum of the squares on them medial and the rectangle contained by them medial and moreover incommensurable with the sum of the squares on them.

**Step 1.** We use a sum-and-difference construction: the sum of the required squares will be medial, while their difference will be rational, making their incommensurability in square immediate from a common-measure argument. First observe that none of the ratios 2:1, 3:1, and 6:1 is a ratio of square numbers. Indeed, suppose m²:n² = k:1 for one of these values of k, and cancel the greatest common divisor of m and n [7.2]. Then m² = kn² [7.19]. For k = 2 or 3, the corresponding prime divides m, and substitution shows that it also divides n. For k = 6, the prime 3 divides m; writing m = 3r gives 3r² = 2n², so 3 also divides n. These conclusions follow from the prime-divisor property [7.30; D7.11] and contradict the cancellation of their common divisor.

**Step 2.** Let e be the assigned rational straight line [D10.1.3]. Construct its square, and construct straight lines f and t such that
f² = 3e² and t² = e²/2.
Here and below, a squared letter denotes the square on that straight line, and a product denotes the rectangle contained by its factors. The required squares can be constructed equal to three copies of the square on e and to its half [1.46, 1.10, 2.14].

**Step 3.** The squares on e, f, and t have the common area-measure e²/2. Thus these lines are rational and pairwise commensurable in square [D10.1.2, D10.1.3]. But
f²:e² = 3:1, e²:t² = 2:1, and f²:t² = 6:1.
By Step 1 and 10.9, each corresponding pair of straight lines is incommensurable in length. In particular, e and f, and also e and t, are rational straight lines commensurable in square only.

**Step 4.** Since f² > e², we have f > e [6.20]. Take AB = f and bisect it at C. Bisect e, and cut off CD = e/2 along CB, with D between C and B [1.10, 1.3]. Put a = AD and b = DB. Thus a and b are positive, and
a + b = f, a − b = e.

**Step 5.** Apply 2.5 to AB, cut equally at C and unequally at D. It gives
ab + (e/2)² = (f/2)².
Since squares on half-lengths are fourth parts of the original squares [6.20], subtraction yields
ab = (f² − e²)/4 = e²/2 = t²
[CN3].

**Step 6.** Construct x as a mean proportional between e and a, and y as a mean proportional between e and b [6.13]. Thus
e:x = x:a and e:y = y:b,
and consequently
x² = ea and y² = eb
[6.17]. These x and y will be the required straight lines.

**Step 7.** By distributing the rectangles over the sum and difference of their bases [2.1; CN3],
S := x² + y² = e(a + b) = ef,
and
x² − y² = e(a − b) = e².
Since e and f are rational straight lines commensurable in square only, ef is a medial area [10.21]. Moreover, it is irrational, hence incommensurable with the rational square e² [10.21; D10.1.4]. Thus S is medial and incommensurable with e².

**Step 8.** We next establish the rectangle contained by x and y. Since x² = ea, y² = eb, and t² = ab, rectangles of equal altitude give
x²:a² = ea:a² = e:a,
and
y²:t² = eb:ab = e:a
[6.1]. Therefore the squares on x, a, y, t are proportional, and their sides are proportional [6.22]:
x:a = y:t.
But e:x = x:a by Step 6, so e:x = y:t [CN1]. Consequently,
P := xy = et
[6.16]. Since e and t are rational straight lines commensurable in square only, P is medial [10.21].

**Step 9.** The two areas just obtained satisfy
S:P = ef:et = f:t
[6.1]. Since f and t are incommensurable in length by Step 3, S and P are incommensurable [10.11].

**Step 10.** Finally, suppose that x² and y² had a common area-measure. That measure would also measure their sum and their difference [D10.1.1], which by Step 7 are S and e². This contradicts their established incommensurability. Therefore x and y are incommensurable in square [D10.1.2]. Their squares have the medial sum S, their contained rectangle P is medial, and P is incommensurable with S. Hence x and y satisfy every requirement.

**USED:** 1.10, 1.3, 1.46, 10.11, 10.21, 10.9, 2.1, 2.14, 2.5, 6.1, 6.13, 6.16, 6.17, 6.20, 6.22, 7.19, 7.2, 7.30, CN1, CN3, D10.1.1, D10.1.2, D10.1.3, D10.1.4, D7.11
**Human refs (from References field):** 1.47, 10.11, 10.13, 10.18, 10.32, 3.31
**Jaccard:** 0.033 — AI adds ['1.10', '1.3', '1.46', '10.21', '10.9', '2.1', '2.14', '2.5', '6.1', '6.13', '6.16', '6.17', '6.20', '6.22', '7.19', '7.2', '7.30', 'CN1', 'CN3', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.1.4', 'D7.11']; Human adds ['1.47', '10.13', '10.18', '10.32', '3.31']

## Proposition 10.36
**Statement:** If two rational straight lines commensurable in square only be added together, the whole is irrational; and let it be called binomial.

**Step 1.** Let AB and BC be the given rational straight lines, commensurable in square only, and let AC be their whole. Let Q be the square on the assigned rational straight line, and denote the squares on AB and BC by X and Y respectively. Then X and Y are commensurable, and X is commensurable with Q. [D10.1.2, D10.1.3]

**Step 2.** Put S = X + Y. Since X and Y are commensurable, S is commensurable with X; since X is also commensurable with Q, S is commensurable with Q. Thus S is a rational area. [10.15, 10.12, D10.1.4]

**Step 3.** Let R be the rectangle contained by AB and BC. We use 10.21 directly, since its hypotheses are exactly those given: R is irrational, and therefore incommensurable with Q. [10.21, D10.1.4]

**Step 4.** The areas R and 2R are commensurable, since R measures both. Consequently, because R is incommensurable with Q, 2R is also incommensurable with Q. [D10.1.1, 10.13]

**Step 5.** Since S and Q are commensurable while 2R is incommensurable with Q, S and 2R are incommensurable. The direct sum clause of 10.16 therefore gives that S + 2R is incommensurable with S. Since S is commensurable with Q, it follows that S + 2R is incommensurable with Q. [10.13, 10.16, 10.13]

**Step 6.** By 2.4, the square on AC equals the squares on AB and BC together with twice their rectangle; that is, it equals S + 2R. Hence the square on AC is incommensurable with Q, so AC is irrational. Thus the whole formed by adding the two given straight lines is irrational; let it be called binomial. [2.4, D10.1.4]

**USED:** 10.12, 10.13, 10.15, 10.16, 10.21, 2.4, D10.1.1, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 10.11, 10.13, 10.15, 10.16, 10.6, 2.4, D10.1.4
**Jaccard:** 0.417 — AI adds ['10.12', '10.21', 'D10.1.1', 'D10.1.2', 'D10.1.3']; Human adds ['10.11', '10.6']

## Proposition 10.37
**Statement:** If two medial straight lines commensurable in square only and containing a rational rectangle be added together, the whole is irrational; and let it be called a first bimedial straight line.

**Step 1.** Let a and b be the given medial straight lines, commensurable in square only, and let c = a + b. Write A and B for their squares, R for the rectangle contained by a and b, and U for the square on the assigned rational straight line. By the hypotheses, A and B are commensurable (D10.1.2), and R is commensurable with U because R is rational (D10.1.4).

**Step 2.** We take the direct route through areas, since the given commensurability of the squares immediately permits the use of 10.15. Put S = A + B. Then S is commensurable with A (10.15). Since a is medial, A is an irrational area (10.21), and therefore A is incommensurable with U (D10.1.4). Consequently S is incommensurable with U (10.13).

**Step 3.** Put T = R + R. A common measure of R and U also measures T, since T consists of two copies of R. Thus T is commensurable with U (D10.1.1). Since U is incommensurable with S, it follows that T is also incommensurable with S (10.13).

**Step 4.** The square on the sum of two straight lines equals their two squares together with twice their contained rectangle. Hence the square on c equals S + T (2.4). Since S and T are incommensurable, their sum, and therefore the square on c, is incommensurable with T (10.16).

**Step 5.** But T is commensurable with U by Step 3. Therefore U is incommensurable with the square on c (10.13). The square on c is consequently irrational, and its side c is irrational (D10.1.4).

**Step 6.** Thus the sum of the two given medial straight lines is irrational, as established in Step 5. Let this sum be called a first bimedial straight line.

**USED:** 10.13, 10.15, 10.16, 10.21, 2.4, D10.1.1, D10.1.2, D10.1.4
**Human refs (from References field):** 10.16, 10.36, 2.4, D10.1.4
**Jaccard:** 0.333 — AI adds ['10.13', '10.15', '10.21', 'D10.1.1', 'D10.1.2']; Human adds ['10.36']

## Proposition 10.38
**Statement:** If two medial straight lines commensurable in square only and containing a medial rectangle be added together, the whole is irrational; and let it be called a second bimedial straight line.

**Step 1.** Let a and b be the given medial straight lines, and let r be the assigned rational straight line. Write a² and b² for their squares, and ab for the rectangle they contain. By hypothesis, a² and b² are commensurable, whereas a and b are incommensurable in length; moreover, ab is a medial area, that is, an area equal to a square on a medial straight line. We must prove that a+b is irrational. [D10.1.2, D10.1.3]

**Step 2.** Construct straight lines x, y, z such that rx=a², ry=b², and rz=ab. These constructions are obtained by taking fourth proportionals and using the equality of the rectangles contained by the extremes and the means. [6.12, 6.16] Thus x, y, z are the breadths obtained by applying these three areas to r. Each area is a square on a medial straight line, or equal to such a square; therefore x, y, z are rational. [10.22]

**Step 3.** Rectangles of equal altitude are proportional to their bases. Hence a²:ab=a:b, so a² and ab are incommensurable, because a and b are incommensurable in length. [6.1, 10.11] Again, the rectangles applied to r give x:y=a²:b² and x:z=a²:ab. Consequently x and y are commensurable in length, while x and z are incommensurable in length. [6.1, 10.11]

**Step 4.** Put u=x+y and v=z+z. Since x and y are commensurable, u is commensurable with x; likewise v is commensurable with z. [10.15] Since x is incommensurable with z, u is incommensurable with z; and since v is commensurable with z, v is incommensurable with u. Thus u and v are incommensurable in length. [10.13, applied twice]

**Step 5.** Since u is commensurable in length with x, their squares have the ratio of a square number to a square number and are therefore commensurable. The same holds for the squares on v and z. [10.9, 10.6] Since x and z are rational, x² and z² are each commensurable with r². It follows that u² and v² are each commensurable with r², and consequently with one another. Thus u and v are rational straight lines commensurable in square only. [D10.1.2, D10.1.3, 10.12]

**Step 6.** Path choice: the breadths now satisfy exactly the hypotheses of the earlier binomial proposition, so apply that result directly. Their sum w=u+v is irrational. [10.36]

**Step 7.** By distribution of a rectangle over the parts of its base,
 rw=rx+ry+rz+rz=a²+b²+2ab. [2.1]
But a²+b²+2ab is the square on a+b. Hence rw=(a+b)². [2.4]

**Step 8.** Suppose a+b were rational. Its square would then be a rational area. [D10.1.2, D10.1.3, D10.1.4] Applied to the rational straight line r, that area would produce a rational breadth. [10.20] By Step 7 this breadth is w, contradicting Step 6. Therefore a+b is irrational; let it be called a **second bimedial straight line**.

**USED:** 10.11, 10.12, 10.13, 10.15, 10.20, 10.22, 10.36, 10.6, 10.9, 2.1, 2.4, 6.1, 6.12, 6.16, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 1.44, 10.11, 10.13, 10.15, 10.20, 10.22, 10.36, 10.6, 2.4, 6.1, D10.1.4
**Jaccard:** 0.556 — AI adds ['10.12', '10.9', '2.1', '6.12', '6.16', 'D10.1.2', 'D10.1.3']; Human adds ['1.44']

## Proposition 10.39
**Statement:** If two straight lines incommensurable in square which make the sum of the squares on them rational, but the rectangle contained by them medial, be added together, the whole straight line is irrational: and let it be called major.

**Step 1.** Let a and b be the given straight lines, incommensurable in square, and let c be their sum. Denote the sum of their squares by S and their contained rectangle by M. Thus S is rational and M is medial, by hypothesis. Let U be the square on the assigned rational straight line. Since S is rational, S is commensurable with U. [D10.1.4]

**Step 2.** A medial area is irrational, so M is incommensurable with U. Since S is commensurable with U, M is also incommensurable with S. [10.21, D10.1.4, 10.13]

**Step 3.** The areas M and 2M are commensurable, since M measures both. Therefore, because M is incommensurable with S, the area 2M is likewise incommensurable with S. [D10.1.1, 10.13]

**Step 4.** The square on the whole straight line c equals the squares on its two parts together with twice their contained rectangle. Hence the square on c equals S + 2M. [2.4]

**Step 5.** Since S and 2M are incommensurable, their sum is incommensurable with S. Consequently the square on c is incommensurable with S. Here the direct incommensurable-sum criterion is the natural choice, because the two area summands have already been shown incommensurable. [10.16]

**Step 6.** But S is commensurable with U; therefore the square on c, being incommensurable with S, is incommensurable with U. Thus the square on c is irrational, and its side c is irrational. Accordingly, the whole straight line a + b is irrational; let it be called major. [10.13, D10.1.4]

**USED:** 10.13, 10.16, 10.21, 2.4, D10.1.1, D10.1.4
**Human refs (from References field):** 10.16, 10.23, 10.33, 10.6, D10.1.4
**Jaccard:** 0.222 — AI adds ['10.13', '10.21', '2.4', 'D10.1.1']; Human adds ['10.23', '10.33', '10.6']

## Proposition 10.40
**Statement:** If two straight lines incommensurable in square which make the sum of the squares on them medial, but the rectangle contained by them rational, be added together, the whole straight line is irrational; and let it be called the side of a rational plus a medial area.

**Step 1.** Let the given straight lines be a and b, incommensurable in square, and let c be their sum. Write M for the sum of the squares on a and b, and R for the rectangle contained by a and b. By hypothesis, M is medial and R is rational. By 2.4, the square on c equals M + 2R. We take the direct area route, using this decomposition of the square.

**Step 2.** Let Q be the square on the assigned rational straight line. Since R is rational, R and Q have a common area-measure (D10.1.4, D10.1.1). That same measure measures 2R, since 2R consists of two copies of R. Thus 2R is commensurable with Q and is therefore a rational area (D10.1.1, D10.1.4).

**Step 3.** Since M is medial, it is irrational by 10.21, and hence is incommensurable with Q (D10.1.4). But Q and 2R are commensurable by Step 2. Therefore M and 2R are incommensurable (10.13).

**Step 4.** The sum theorem for incommensurable magnitudes applies immediately: M + 2R is incommensurable with 2R (10.16). Since 2R is commensurable with Q, it follows that M + 2R is also incommensurable with Q (10.13).

**Step 5.** The square on c equals M + 2R by Step 1, so it is incommensurable with Q. Consequently c is irrational (D10.1.4). Moreover, its square is the sum of the rational area 2R and the medial area M. Let c therefore be called the **side of a rational plus a medial area**, as required.

**USED:** 10.13, 10.16, 10.21, 2.4, D10.1.1, D10.1.4
**Human refs (from References field):** 10.16, 10.34, D10.1.4
**Jaccard:** 0.286 — AI adds ['10.13', '10.21', '2.4', 'D10.1.1']; Human adds ['10.34']

## Proposition 10.41
**Statement:** If two straight lines incommensurable in square which make the sum of the squares on them medial, and the rectangle contained by them medial and also incommensurable with the sum of the squares on them, be added together, the whole straight line is irrational; and let it be called the   side of the sum of two medial areas.

**Step 1.** Let the given straight lines be a and b, and let their sum be c. Write S for the sum of their squares and R for the rectangle contained by them. By hypothesis, S and R are medial areas and are incommensurable with one another. The square on the whole satisfies c² = S + 2R [2.4].

**Step 2.** Apply S and R to the assigned rational straight line r as rectangles, and denote their respective breadths by u and v. Such applications can be made by applying their constituent triangles to r in a right angle and adding the resulting rectangles [1.44, CN2]. Thus the rectangles contained by r, u and by r, v equal S and R respectively. Since both areas are medial, u and v are rational straight lines [10.22].

**Step 3.** The squares on u and v are therefore commensurable with the square on r [D10.1.2, D10.1.3]. The square on 2v is four times the square on v [2.4], so these two squares are commensurable [D10.1.1]. Consequently, the square on 2v is commensurable both with the square on r and with the square on u [10.12]. Hence 2v is rational, and u and 2v are commensurable in square [D10.1.2, D10.1.3].

**Step 4.** Rectangles of the same height are to one another as their bases; therefore S : R = u : v [6.1]. Since S and R are incommensurable, u and v are incommensurable in length [10.11]. But v and 2v are commensurable, since v measures both [D10.1.1]. Thus u and 2v are incommensurable in length [10.13].

**Step 5.** The straight lines u and 2v are therefore rational and commensurable in square only. Their sum u + 2v is irrational [10.36]. This is the direct path: applying the medial areas to a common rational line has produced exactly the hypotheses of the earlier binomial theorem.

**Step 6.** The rectangle contained by r and u + 2v equals the rectangle contained by r and u together with twice the rectangle contained by r and v; hence it equals S + 2R, which is c² [2.1, Step 1]. If c² were a rational area, its application to the rational straight line r would produce a rational breadth [10.20]. Its breadth, however, is u + 2v, which is irrational by Step 5. Therefore c² is irrational, and its side c is irrational [D10.1.4]. Thus the sum of the given straight lines is irrational; let it be called the side of the sum of two medial areas.

**USED:** 1.44, 10.11, 10.12, 10.13, 10.20, 10.22, 10.36, 2.1, 2.4, 6.1, CN2, D10.1.1, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 10.11, 10.22, 10.35, 10.36, 2.4, 6.1, D10.1.4
**Jaccard:** 0.375 — AI adds ['1.44', '10.12', '10.13', '10.20', '2.1', 'CN2', 'D10.1.1', 'D10.1.2', 'D10.1.3']; Human adds ['10.35']

## Proposition 10.42
**Statement:** A binomial straight line is divided into its terms at one point only.

**Step 1.** We prove uniqueness of the greater and lesser terms, measuring the greater term from a fixed endpoint A; interchanging their order does not constitute a different pair of terms. Let AB be binomial. Suppose that C and D give two distinct divisions into its terms, with AC > CB and AD > DB. In each pair the straight lines are rational and commensurable in square only (10.36). Interchanging the names C and D if necessary, let their order be A, C, D, B. Then AC > CB > DB (CN5).

**Step 2.** Write Q(x) for the square on x and R(x,y) for the rectangle contained by x and y (D2.1). Put
M = R(AC,CB),   N = R(AD,DB).
By 10.21, both M and N are medial areas: each equals the square on a medial straight line. The direct route is therefore to use 10.26, which forbids a rational difference between unequal medial areas.

**Step 3.** Since CB = CD + DB and AD = AC + CD, distribution of the rectangles gives
M = R(AC,CD) + R(AC,DB),
N = R(AC,DB) + R(CD,DB)
(2.1). Subtracting the common rectangle and applying 2.1 once more yields
M − N = R(CD,AC − DB)
(CN3). Both sides of this last rectangle are positive, since C and D are distinct and AC > DB. Consequently M > N (CN5).

**Step 4.** Put
U = Q(AC) + Q(CB),   V = Q(AD) + Q(DB).
The four squares are rational areas, because their sides are rational straight lines (D10.1.3, D10.1.4). Areas commensurable with the assigned rational square are commensurable with one another (10.12); their sum is commensurable with either summand (10.15), and hence with the assigned square (10.12). Thus U and V are rational areas.

**Step 5.** Applying 2.4 to the two divisions of AB gives
Q(AB) = U + 2M = V + 2N
(CN1). Subtraction therefore gives
V − U = 2(M − N) > 0
(CN3; Step 3). In particular, V > U.

**Step 6.** Because U and V are rational, they are commensurable (10.12, D10.1.4). Applying the converse part of 10.15 to V = U + (V − U), the difference V − U is commensurable with U, and therefore with the assigned rational square (10.12). Hence V − U is rational (D10.1.4). Its half is rational as well: if an area h measures both V − U and the assigned square, then h/2 measures both (V − U)/2 and that same square (D10.1.1, D10.1.4). By Step 5, this half is M − N.

**Step 7.** Thus the medial area M exceeds the medial area N by the rational area M − N, contrary to 10.26. The supposed distinct divisions are therefore impossible. The greater and lesser terms of a binomial are uniquely determined; with the greater term measured from the fixed endpoint, their dividing point is unique. Therefore a binomial straight line is divided into its terms at one point only.

**USED:** 10.12, 10.15, 10.21, 10.26, 10.36, 2.1, 2.4, CN1, CN3, CN5, D10.1.1, D10.1.3, D10.1.4, D2.1
**Human refs (from References field):** 10.21, 10.36, 2.4
**Jaccard:** 0.214 — AI adds ['10.12', '10.15', '10.26', '2.1', 'CN1', 'CN3', 'CN5', 'D10.1.1', 'D10.1.3', 'D10.1.4', 'D2.1']

## Proposition 10.43
**Statement:** A first bimedial straight line is divided at one point only.

**Step 1.** Let AB be a first bimedial straight line, divided into its terms at C. Suppose that it also admits such a division at D. In comparing divisions into terms, take the greater term from the same endpoint A, so that AC > CB and AD > DB. By 10.37, each pair consists of medial straight lines commensurable in square only and containing a rational rectangle. Thus the squares within each pair are commensurable areas. [10.37, D10.1.2]

**Step 2.** We first establish that the sum of the squares for either division is medial. Write x, y for the terms of either pair, and construct their third proportional z, so that x : y = y : z. Then the rectangle xz equals the square on y. Consequently, by the ratio of rectangles having the same height,

x² : y² = x² : xz = x : z.

Since x² and y² are commensurable, x and z are commensurable in length. [6.11, 6.17, 6.1, 10.11]

**Step 3.** The sum x + z is therefore commensurable in length with x. Since x is medial, x + z is medial also. The rectangle contained by x and x + z is consequently medial; but this rectangle equals x² + xz, hence x² + y². Thus the sum of the squares belonging to each proposed division is medial. [10.15, 10.23, 10.24, 2.1, 6.17]

**Step 4.** Denote these medial sums by

M = AC² + CB²,    N = AD² + DB²,

and denote the rational rectangles by

R = AC·CB,    S = AD·DB.

Applying the square-of-a-sum identity to the two divisions of AB gives

M + 2R = AB² = N + 2S.

[Step 3, 10.37, 2.4, CN1]

**Step 5.** We use the direct area route: 10.26 forbids precisely a rational excess between the two medial areas just obtained. Suppose R and S are unequal, and interchange the names of the divisions if necessary so that S > R. Since R and S are rational areas, they are commensurable with the assigned rational square and hence with one another. By the converse assertion of 10.15, their positive difference E = S − R is commensurable with R; it is therefore rational. Its double 2E is likewise rational. Substituting S = R + E into Step 4 and cancelling 2R gives

M = N + 2E.

This makes one medial area exceed another by a rational area, contrary to 10.26. Therefore R = S. [D10.1.4, 10.12, 10.15, CN2, CN3, 10.26]

**Step 6.** Suppose now that C and D are distinct. Interchanging their names if necessary, their order is A, D, C, B. By distributivity of rectangles,

AC·CB = AD·CB + DC·CB,

AD·DB = AD·CB + AD·DC.

The left-hand rectangles are equal by Step 5. Subtracting the common rectangle AD·CB therefore yields

DC·CB = AD·DC.

But AD > DB > CB. With the same positive side DC, the rectangle contained by AD and DC is greater than the rectangle contained by CB and DC: the latter is congruent to a proper part of the former. This contradicts their equality. [2.1, CN3, CN5]

**Step 7.** Hence C and D cannot be distinct. The defining division exists by 10.37 and, by Step 6, admits no second point. Therefore a first bimedial straight line is divided into its terms at one point only. [10.37, Step 6]

**USED:** 10.11, 10.12, 10.15, 10.23, 10.24, 10.26, 10.37, 2.1, 2.4, 6.1, 6.11, 6.17, CN1, CN2, CN3, CN5, D10.1.2, D10.1.4
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['10.11', '10.12', '10.15', '10.23', '10.24', '10.26', '10.37', '2.1', '2.4', '6.1', '6.11', '6.17', 'CN1', 'CN2', 'CN3', 'CN5', 'D10.1.2', 'D10.1.4']

## Proposition 10.44
**Statement:** A second bimedial straight line is divided at one point only.

**Step 1.** Let L be a second bimedial straight line, and let L=a+b be its division into terms, with a>b. Suppose that L=c+d is another division of the same kind, with c>d. In comparing division points, take the greater term from the same endpoint. By 10.38, each pair consists of medial straight lines commensurable in square only, and each pair contains a medial rectangle. Thus a² and b² are commensurable, but a and b are incommensurable in length; the corresponding assertions hold for c and d. [10.38, D10.1.2]

**Step 2.** Fix the assigned rational straight line r. Let (p,q) denote either (a,b) or (c,d). Construct breadths u,v,w such that
ru=p²,  rv=q²,  rw=pq,
where products denote rectangular areas. These breadths can be constructed as fourth proportionals. Since p and q are medial and their rectangle pq is medial, applying these three medial areas to r gives rational breadths u,v,w. [6.12, 6.16, 10.22]

**Step 3.** The rectangles ru and rv have the ratio u:v. Since p² and q² are commensurable, u and v are commensurable in length. Put x=u+v and y=2w. Then x is commensurable in length with u, and y with w. Their respective squares are therefore commensurable; consequently, because u and w are rational, x and y are rational also. Moreover,
rx=p²+q²,  ry=2pq.
[6.1, 10.11, 10.15, D10.1.1, 10.9, 10.6, 10.12, D10.1.3, 2.1]

**Step 4.** Since p²:pq=p:q, and p and q are incommensurable in length, the areas p² and pq are incommensurable. But p²+q² is commensurable with p², while 2pq is commensurable with pq. Applying 10.13 twice, p²+q² and 2pq are incommensurable. Their applications to the common base r therefore have incommensurable breadths x and y. Since x and y are rational, their squares are commensurable with the square on r and hence with one another. Thus x and y are rational straight lines commensurable in square only, so x+y is a binomial. [6.1, 10.11, 10.15, D10.1.1, 10.13, D10.1.3, 10.12, 10.36]

**Step 5.** The square identity for the sum p+q gives
r(x+y)=p²+q²+2pq=(p+q)²=L².
Also,
p²+q²=2pq+(p−q)².
Since p>q, the last square is positive; hence rx>ry, and therefore x>y. Thus x is the greater term of the auxiliary binomial. [2.1, 2.4, 2.7, CN5, 6.1, D5.5]

**Step 6.** Apply Steps 2–5 to both proposed divisions, obtaining binomial terms x,y from a,b and x′,y′ from c,d. Their sums are equal, because
r(x+y)=L²=r(x′+y′),
and rectangles on the same base have the ratio of their breadths. Moreover, x>y and x′>y′. We now use 10.42: binomial uniqueness is the earlier uniqueness result naturally reached by applying our areas to a rational line. It gives x=x′ and y=y′. In particular,
a²+b²=rx=rx′=c²+d².
[6.1, D5.5, 10.42, CN1]

**Step 7.** Suppose a≠c, and interchange the names of the two divisions if necessary so that a>c. Set h=a−c. Since a+b=c+d, subtraction gives d=b+h. Thus h>0 and c>d>b, so c−b>0. Expanding the squares gives
a²=c²+2ch+h²,
d²=b²+2bh+h².
Consequently,
a²+b²=c²+d²+2h(c−b)>c²+d²,
contrary to Step 6. Therefore a=c. [CN3, 2.4, 2.1, CN2, CN5]

**Step 8.** Subtracting a=c from the equal wholes a+b=c+d gives b=d. The defining terms therefore coincide, and so does their division point. Such a division exists by the definition of a second bimedial straight line in 10.38; hence a second bimedial straight line is divided at one point only. [CN3, 10.38]

**USED:** 10.11, 10.12, 10.13, 10.15, 10.22, 10.36, 10.38, 10.42, 10.6, 10.9, 2.1, 2.4, 2.7, 6.1, 6.12, 6.16, CN1, CN2, CN3, CN5, D10.1.1, D10.1.2, D10.1.3, D5.5
**Human refs (from References field):** 10.11, 10.13, 10.22, 10.36, 10.38, 10.6, 2.4, 6.1
**Jaccard:** 0.333 — AI adds ['10.12', '10.15', '10.42', '10.9', '2.1', '2.7', '6.12', '6.16', 'CN1', 'CN2', 'CN3', 'CN5', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D5.5']

## Proposition 10.45
**Statement:** A major straight line is divided at one and the same point only.

**Step 1.** Let AB be a major straight line, divided into its defining terms at C. Fix A as the endpoint from which the greater term is measured, so AC > CB. Suppose that D is another dividing point into terms of the same kind, with AD > DB. Write S_C = AC² + CB² and S_D = AD² + DB², and let M_C and M_D denote the rectangles AC·CB and AD·DB. By 10.39, S_C and S_D are rational areas, while M_C and M_D are medial areas. The direct path is to compare these medial rectangles and apply the prohibition in 10.26 against their differing by a rational area. [10.39, 10.26]

**Step 2.** Bisect AB at O. Since the greater term is measured from A in both divisions, C and D lie between O and B. If they are distinct, interchange their names if necessary so that their order is O, D, C, B. The equal-and-unequal division identity gives
M_C + OC² = OB² = M_D + OD².
Here 2.5 is the natural cut-line identity because it directly compares the rectangles through their distances from the midpoint. Since OC = OD + DC, the square-expansion identity shows that OC² > OD². Consequently M_D > M_C. [1.10, 2.5, 2.4, CN3, CN5]

**Step 3.** Expanding the square on the whole line at each dividing point gives
AB² = S_C + 2M_C = S_D + 2M_D.
Subtracting equal areas and collecting the remainders therefore yields
S_C − S_D = 2(M_D − M_C) > 0.
Put Δ = S_C − S_D and δ = M_D − M_C; thus Δ = 2δ. [2.4, CN2, CN3]

**Step 4.** Let R be the square on the assigned rational straight line. Since S_C and S_D are rational, each is commensurable with R, and hence they are commensurable with one another. Since S_C = S_D + Δ, the converse assertion of 10.15 makes Δ commensurable with S_D. Therefore Δ is commensurable with R and is a rational area. [D10.1.4, 10.12, 10.15]

**Step 5.** Because Δ = 2δ, the area δ measures both itself and Δ; thus δ and Δ are commensurable. As Δ is commensurable with R, so is δ. Hence δ is rational. But δ = M_D − M_C is positive, and both M_D and M_C are medial. This contradicts 10.26: a medial area does not exceed a medial area by a rational area. [D10.1.1, 10.12, D10.1.4, 10.26]

**Step 6.** The supposition that C and D are distinct is therefore impossible. Thus, with the greater term measured from the fixed endpoint, the defining division of a major straight line is at one and the same point only. [Steps 1–5]

**USED:** 1.10, 10.12, 10.15, 10.26, 10.39, 2.4, 2.5, CN2, CN3, CN5, D10.1.1, D10.1.4
**Human refs (from References field):** 10.26, 10.39
**Jaccard:** 0.167 — AI adds ['1.10', '10.12', '10.15', '2.4', '2.5', 'CN2', 'CN3', 'CN5', 'D10.1.1', 'D10.1.4']

## Proposition 10.46
**Statement:** The side of a rational plus a medial area is divided at one point only.

**Step 1.** Let AB be the side of a rational plus a medial area, divided into its terms at C. By 10.40, AC and CB are incommensurable in square, the area S_C = AC² + CB² is medial, and the rectangle R_C = AC·CB is rational. Compare divisions with the greater term adjacent to A; merely interchanging the two terms is not a new decomposition. Thus AC > CB. Suppose there is another such division at D, with AD > DB. Then S_D = AD² + DB² is medial and R_D = AD·DB is rational, again by 10.40. The direct route is to show that these two medial areas would differ by a rational area, contrary to 10.26.

**Step 2.** Interchanging the names C and D if necessary, suppose the points occur in the order A, D, C, B. Since DB > CB and AD > DB, we have AD > CB (CN5). By distributing rectangles using 2.1,
R_D = AD·CB + AD·CD,
R_C = AD·CB + CB·CD.
Consequently,
R_D = R_C + CD·(AD − CB)
(2.1, CN2, CN3). The additional rectangle is positive, so R_D > R_C (CN5). Denote their positive difference by E.

**Step 3.** Let Q be the square on the assigned rational straight line. Since R_C and R_D are rational, both are commensurable with Q (D10.1.4), and therefore with one another (10.12). Since R_D = R_C + E, the converse part of 10.15 shows that E is commensurable with R_C. Hence E is commensurable with Q (10.12), and is rational (D10.1.4). Moreover, E measures 2E, so E and 2E are commensurable (D10.1.1). Thus 2E is likewise commensurable with Q and is rational (10.12, D10.1.4).

**Step 4.** Applying 2.4 to the two divisions of AB gives
AB² = S_C + 2R_C,
AB² = S_D + 2R_D.
These expressions are equal (CN1). Substituting R_D = R_C + E and subtracting the common area 2R_C gives
S_C = S_D + 2E
(CN2, CN3).

**Step 5.** Thus the medial area S_C exceeds the medial area S_D by the positive rational area 2E. This is impossible by 10.26. Therefore no second division into the defining terms exists. Since the division at C exists by 10.40, the side of a rational plus a medial area is divided at one point only.

**USED:** 10.12, 10.15, 10.26, 10.40, 2.1, 2.4, CN1, CN2, CN3, CN5, D10.1.1, D10.1.4
**Human refs (from References field):** 10.26, 10.40
**Jaccard:** 0.167 — AI adds ['10.12', '10.15', '2.1', '2.4', 'CN1', 'CN2', 'CN3', 'CN5', 'D10.1.1', 'D10.1.4']

## Proposition 10.47
**Statement:** The side of the sum of two medial areas is divided at one point only.

**Step 1.** Let AB be the side of the sum of two medial areas, divided into its defining terms at C. Fix their order by placing the greater term next to A, so AC > CB. Suppose that D is another defining division with AD > DB. Put
S = AC² + CB², P = AC·CB,
S′ = AD² + DB², P′ = AD·DB.
By 10.41, S and P are medial areas incommensurable with one another, and likewise S′ and P′. The squares on the two terms of each division are incommensurable, so those terms are unequal. [10.41; D10.1.2]

**Step 2.** Path choice: apply the medial areas to a rational straight line, thereby reducing the question to binomial uniqueness, 10.42—the first uniqueness theorem naturally applicable to the resulting rational breadths. Choose the assigned rational straight line r, and apply S, P, S′, P′ to it as rectangles with respective breadths u, v, u′, v′. Thus
r·u = S, r·v = P, r·u′ = S′, r·v′ = P′.
Each application can be constructed by taking the third proportional to r and the medial side of the corresponding area; the rectangle contained by the extremes then equals the square on that medial side. All four breadths are rational by 10.22. [D10.1.3; 6.11; 6.17; 10.22]

**Step 3.** Rectangles on the same base are proportional to their breadths, so S:P = u:v and S′:P′ = u′:v′. Consequently u and v are incommensurable in length, as are u′ and v′. Since v measures both v and 2v, these latter two lengths are commensurable; hence u and 2v are incommensurable. Similarly u′ and 2v′ are incommensurable. [6.1; 10.11; D10.1.1; 10.13]

**Step 4.** By 2.4, the square on 2v is four times the square on v, and similarly for v′. These squares are therefore commensurable with the squares on v and v′ respectively. Since v and v′ are rational, transitivity of commensurability shows that 2v and 2v′ are rational also. Moreover, any two rational straight lines are commensurable in square, since their squares are commensurable with the assigned rational square. Thus u and 2v, and likewise u′ and 2v′, are rational straight lines commensurable in square only. Accordingly u + 2v and u′ + 2v′ are binomials. [2.4; D10.1.1; D10.1.2; D10.1.3; 10.12; 10.36]

**Step 5.** Applying 2.4 to the two divisions of AB gives
AB² = S + 2P = S′ + 2P′.
By distributivity of rectangles, the rectangles on base r with breadths u + 2v and u′ + 2v′ therefore have equal areas. Their breadths are consequently equal:
u + 2v = u′ + 2v′.
Thus these are two decompositions of the same binomial. [2.4; 2.1; 6.1; 5.9]

**Step 6.** By 2.7,
S = 2P + (AC − CB)²,
S′ = 2P′ + (AD − DB)².
The differences of the terms are positive, so S > 2P and S′ > 2P′. On the common base r, these inequalities imply u > 2v and u′ > 2v′: otherwise the corresponding rectangles could not have those inequalities. Both binomial decompositions therefore have their greater terms first. By uniqueness of the division of a binomial, u = u′ and 2v = 2v′. In particular, the corresponding rectangles give 2P = 2P′. [2.7; 2.1; CN5; 10.42; 6.1]

**Step 7.** Suppose C and D are distinct. Interchanging their names if necessary, their order is A, C, D, B. Put e = CD. Distributivity gives
P = AC·DB + AC·e,
P′ = AC·DB + DB·e.
But AC > CB > DB, so AC·e is greater than DB·e: it contains that rectangle together with the positive rectangle e·(AC − DB). Hence P consists of P′ together with a positive area, and therefore 2P > 2P′, contrary to Step 6. Thus C = D. Consequently the side of the sum of two medial areas is divided into its defining terms at one point only. [2.1; CN5]

**USED:** 10.11, 10.12, 10.13, 10.22, 10.36, 10.41, 10.42, 2.1, 2.4, 2.7, 5.9, 6.1, 6.11, 6.17, CN5, D10.1.1, D10.1.2, D10.1.3
**Human refs (from References field):** 10.11, 10.22, 10.36, 10.42, 2.4, 6.1
**Jaccard:** 0.333 — AI adds ['10.12', '10.13', '10.41', '2.1', '2.7', '5.9', '6.11', '6.17', 'CN5', 'D10.1.1', 'D10.1.2', 'D10.1.3']

## Proposition 10.48
**Statement:** To find the first binomial straight line.

**Step 1.** Let AB be the assigned rational straight line, and write r for its length. By 10.29, construct two rational straight lines u > v, commensurable in square only, such that the square on u exceeds the square on v by the square on a straight line commensurable in length with u. The direct path is to use this construction, which already supplies the required square-excess condition, and then normalize its greater term to AB. [D10.1.3, 10.29]

**Step 2.** Construct a fourth proportional b to u, v, r, so that u:v = r:b. Since u > v, equality of these ratios implies r > b. [6.12, D5.5]

**Step 3.** Since u and v are incommensurable in length, the proportion u:v = r:b implies that r and b are also incommensurable in length. [10.11]

**Step 4.** The squares on four proportional straight lines are proportional; hence the square on u is to the square on v as the square on r is to the square on b. The first two squares are commensurable, so the latter two squares are commensurable also. Consequently r and b are commensurable in square; and b is rational because its square is commensurable with the square on the assigned rational line r. Together with Step 3, this shows that r and b are rational straight lines commensurable in square only. [6.22, 10.11, D10.1.2, D10.1.3]

**Step 5.** Apply 10.14 to u:v = r:b and the square-excess condition in Step 1. The square on r therefore exceeds the square on b by the square on a straight line t commensurable in length with r. [10.14]

**Step 6.** Produce AB beyond B, and mark C on the produced part so that BC = b. Since AB and BC are rational and commensurable in square only, their sum AC is a binomial straight line, divided into its terms at B. [P2, P3, 10.36]

**Step 7.** Its greater term is AB, by Step 2. This term is the assigned rational straight line itself and is therefore commensurable in length with it. By Step 5, the square on AB exceeds the square on BC by the square on a straight line commensurable in length with AB. Thus AC satisfies the definition of a first binomial straight line. A first binomial straight line has therefore been found. [D10.1.1, D10.2.1]

**USED:** 10.11, 10.14, 10.29, 10.36, 6.12, 6.22, D10.1.1, D10.1.2, D10.1.3, D10.2.1, D5.5, P2, P3
**Human refs (from References field):** 10.28, 10.36, 10.6, 10.9, 5.19
**Jaccard:** 0.059 — AI adds ['10.11', '10.14', '10.29', '6.12', '6.22', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.2.1', 'D5.5', 'P2', 'P3']; Human adds ['10.28', '10.6', '10.9', '5.19']

## Proposition 10.49
**Statement:** To find the second binomial straight line.

**Step 1.** Let r be the assigned rational straight line [D10.1.3]. By 10.29 construct two rational straight lines a > b, commensurable in square only, such that a² = b² + c² for a straight line c commensurable in length with a. Here squares denote the corresponding square areas. **Path choice:** use 10.29 directly because it supplies precisely the required square-difference condition; then scale the pair so that its lesser term equals r.

**Step 2.** Construct the fourth proportional x to b, a, r, so that b:a = r:x [6.12]. Taking inverse ratios gives a:b = x:r [D5.13]. Since a > b, it follows that x > r [5.14].

**Step 3.** The lines a and b are incommensurable in length. Therefore, from a:b = x:r, the lines x and r are also incommensurable in length [10.11].

**Step 4.** Squares similarly described on proportional straight lines are proportional; hence a²:b² = x²:r² [6.22]. Since a² and b² are commensurable, x² and r² are commensurable [10.11]. Thus x and r are commensurable in square, and, by Step 3, in square only [D10.1.2]. In particular, x is rational because its square is commensurable with the square on the assigned rational line r [D10.1.3].

**Step 5.** Since a:b = x:r, and a² exceeds b² by the square on a line commensurable in length with a, the square x² likewise exceeds r² by the square on a straight line y commensurable in length with x [10.14]. Thus x² = r² + y², with x and y commensurable in length.

**Step 6.** Produce a straight line of length x and cut off on its extension a straight line equal to r; call the whole s [P2, 1.3]. Its two terms x and r are rational and commensurable in square only, so s is a binomial straight line [10.36].

**Step 7.** The greater term of s is x and the lesser is r. Its lesser term is therefore commensurable in length with the assigned rational line, being that very line [D10.1.1]. Moreover, by Step 5, the square on the greater term exceeds the square on the lesser by the square on a line commensurable in length with the greater. These are the common square-difference condition and the lesser-term criterion defining a second binomial [D10.2.1, D10.2.2]. Therefore s is the required second binomial straight line.

**USED:** 1.3, 10.11, 10.14, 10.29, 10.36, 5.14, 6.12, 6.22, D10.1.1, D10.1.2, D10.1.3, D10.2.1, D10.2.2, D5.13, P2
**Human refs (from References field):** 10.36, 10.6, 10.9, 5.19
**Jaccard:** 0.056 — AI adds ['1.3', '10.11', '10.14', '10.29', '5.14', '6.12', '6.22', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.2.1', 'D10.2.2', 'D5.13', 'P2']; Human adds ['10.6', '10.9', '5.19']

## Proposition 10.50
**Statement:** To find the third binomial straight line.

**Step 1.** Let r be the assigned rational straight line, and write x² for the square on a straight line x (D10.1.3). We use a direct mean-proportional construction, so that the required difference of squares is built into the terms. By producing straight lines and cutting off equal copies, construct u = 2r and v = 3r (P2, 1.3).

**Step 2.** Construct c as a mean proportional between r and u, and b as a mean proportional between u and v (6.13). The square on each mean proportional equals the rectangle contained by its extremes (6.17). Therefore, by distributing these rectangles into squares on r,
c² = 2r² and b² = 6r² (2.1).

**Step 3.** Construct a = 2c (P2, 1.3). The square on the sum of two equal straight lines is four times the square on either; hence a² = 4c² = 8r² (2.4). Thus r² measures both a² and b². Consequently a and b are commensurable in square with r and with one another, and both are rational straight lines (D10.1.2, D10.1.3).

**Step 4.** The number 4 is a square number, whereas 32, 24, and 3 are not (D7.18). By 8.24, if a square number has to another number the ratio of a square number to a square number, that other number must also be square. Therefore none of the ratios 4:32, 4:24, and 4:3 is a ratio of square numbers. This criterion applies directly to the square ratios obtained from our construction:
r²:a² = 4:32, r²:b² = 4:24, and a²:b² = 4:3.

**Step 5.** Since none of these square ratios is a ratio of square numbers, 10.9 shows that a is incommensurable in length with r, b is incommensurable in length with r, and a is incommensurable in length with b. Together with Step 3, this proves that a and b are rational straight lines commensurable in square only (D10.1.2).

**Step 6.** Subtracting the constructed squares gives
a² − b² = 8r² − 6r² = 2r² = c² (CN3).
Thus a is the greater term: a line no greater than b cannot have a square greater than b² (2.4, CN5). Moreover, since a = 2c, the straight line c measures both a and itself; hence c is commensurable in length with a (D10.1.1).

**Step 7.** Produce a and cut off a straight line equal to b consecutively with it, forming the single straight line a + b (P2, 1.3). Because its terms are rational and commensurable in square only, a + b is a binomial straight line (10.36).

**Step 8.** The square on the greater term a exceeds the square on the lesser term b by the square on c, which is commensurable in length with a; and neither term is commensurable in length with the assigned rational straight line r. These are precisely the defining conditions of a third binomial (D10.2.1, D10.2.3). Therefore a + b is the required third binomial straight line.

**USED:** 1.3, 10.36, 10.9, 2.1, 2.4, 6.13, 6.17, 8.24, CN3, CN5, D10.1.1, D10.1.2, D10.1.3, D10.2.1, D10.2.3, D7.18, P2
**Human refs (from References field):** 10.36, 10.6, 10.9, 5.19, 5.22
**Jaccard:** 0.100 — AI adds ['1.3', '2.1', '2.4', '6.13', '6.17', '8.24', 'CN3', 'CN5', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.2.1', 'D10.2.3', 'D7.18', 'P2']; Human adds ['10.6', '5.19', '5.22']

## Proposition 10.51
**Statement:** To find the fourth binomial straight line.

**Step 1.** Let AB be the assigned rational straight line [D10.1.3]. Write s² for the square on a straight line s. By 10.30, construct rational straight lines a > b, commensurable in square only, such that a² exceeds b² by c², where c is incommensurable in length with a. This is the direct starting construction because it supplies precisely the square-difference condition required for a fourth binomial; we shall transfer its greater term to AB.

**Step 2.** Construct a fourth proportional x such that a:AB = b:x [6.12]. Since a > b, AB > x [5.14]. Alternating the proportion gives a:b = AB:x [5.16].

**Step 3.** Since a and b are incommensurable in length, the proportion a:b = AB:x implies that AB and x are likewise incommensurable in length [10.11].

**Step 4.** Applying 6.22 directly to the squares on the proportional straight lines gives a²:b² = AB²:x². The squares a² and b² are commensurable, so AB² and x² are commensurable [10.11]. Thus AB and x are commensurable in square and, by Step 3, in square only [D10.1.2]. Consequently x is rational relative to the assigned straight line AB [D10.1.3].

**Step 5.** Since a:b = AB:x and a² exceeds b² by the square on a straight line incommensurable in length with a, 10.14 shows that AB² exceeds x² by the square on a straight line incommensurable in length with AB.

**Step 6.** Produce AB beyond B and cut off BC equal to x [P2, 1.3]. The straight lines AB and BC are rational and commensurable in square only, so their sum AC is a binomial straight line [10.36]. Its greater term is AB, by Step 2.

**Step 7.** The greater term AB is commensurable in length with the assigned rational straight line, being that very line [D10.1.1]. By Step 5, its square exceeds the square on the lesser term BC by the square on a straight line incommensurable in length with AB. Therefore AC is a fourth binomial straight line [D10.2.4]. Thus the required straight line has been found.

**USED:** 1.3, 10.11, 10.14, 10.30, 10.36, 5.14, 5.16, 6.12, 6.22, D10.1.1, D10.1.2, D10.1.3, D10.2.4, P2
**Human refs (from References field):** 10.6, 10.9, 5.19
**Jaccard:** 0.000 — AI adds ['1.3', '10.11', '10.14', '10.30', '10.36', '5.14', '5.16', '6.12', '6.22', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.2.4', 'P2']; Human adds ['10.6', '10.9', '5.19']

## Proposition 10.52
**Statement:** To find the fifth binomial straight line.

**Step 1.** Let r be the assigned rational straight line, and write s² for the square on any straight line s (D10.1.3). By 10.30, construct two rational straight lines a > b, commensurable in square only, such that a² exceeds b² by the square on a straight line incommensurable in length with a. We choose 10.30 directly because it supplies the required square-difference condition; we shall scale its lesser term to r.

**Step 2.** Construct a fourth proportional x such that b:a = r:x (6.12). Alternating gives b:r = a:x (5.16). Since b < a, it follows that r < x (5.14). Reading the alternated proportion as a:x = b:r and alternating again gives a:b = x:r (5.16).

**Step 3.** From a:b = x:r, the squares satisfy a²:b² = x²:r² (6.22). Since a² and b² are commensurable, x² and r² are commensurable by 10.11. Thus x and r are commensurable in square (D10.1.2), and x is rational relative to r (D10.1.3). Moreover, since a and b are incommensurable in length, the proportion a:b = x:r gives that x and r are incommensurable in length, again by 10.11. Consequently x and r are rational straight lines commensurable in square only.

**Step 4.** Apply 10.14 to a:b = x:r. Because a² exceeds b² by the square on a straight line incommensurable in length with a, x² exceeds r² by the square on a straight line k incommensurable in length with x. Thus x² = r² + k², with k incommensurable in length with the greater term x (10.14).

**Step 5.** Produce the segment x and lay off on its continuation a segment equal to r, obtaining the straight line L = x + r (P2, 1.3). Since its two terms are rational and commensurable in square only, L is a binomial straight line (10.36).

**Step 6.** The lesser term of L is r, which is commensurable in length with the assigned rational straight line, being that line itself (D10.1.1). By Step 4, the square on its greater term exceeds the square on its lesser term by the square on a straight line incommensurable in length with the greater term. Therefore L is a fifth binomial straight line (D10.2.5). The required straight line has been found.

**USED:** 1.3, 10.11, 10.14, 10.30, 10.36, 5.14, 5.16, 6.12, 6.22, D10.1.1, D10.1.2, D10.1.3, D10.2.5, P2
**Human refs (from References field):** 10.36, 10.6, 10.9, 5.19
**Jaccard:** 0.059 — AI adds ['1.3', '10.11', '10.14', '10.30', '5.14', '5.16', '6.12', '6.22', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.2.5', 'P2']; Human adds ['10.6', '10.9', '5.19']

## Proposition 10.53
**Statement:** To find the sixth binomial straight line.

**Step 1.** Let r be the assigned rational straight line, and write S for the square on r [D10.1.3]. Path choice: construct two terms whose squares are respectively 3S and 2S, so that their square-excess is S itself. Produce a straight line and cut off successive copies of r, obtaining the lengths 2r and 3r [P2, 1.3].

**Step 2.** Construct a mean proportional a between r and 3r, and a mean proportional b between r and 2r [6.13]. The square on a mean proportional equals the rectangle contained by the extremes; hence, distributing these rectangles into copies of S, we obtain
 a² = r·(3r) = 3S,     b² = r·(2r) = 2S
[6.17, 2.1].

**Step 3.** None of the numerical ratios 6:2, 4:2, and 3:2 is a ratio of square numbers. Indeed, between two square numbers there is a mean proportional number [8.11]; consequently, if any of these three ratios were a ratio of square numbers, there would also be a mean proportional number between its displayed terms [8.8]. The square of that mean would respectively equal 12, 8, or 6 [7.19]. But 2² < 6 < 8 < 3² and 3² < 12 < 4², so none of these three numbers is a square number [D7.18].

**Step 4.** Since S measures both a² and b², the lines a and b are commensurable in square with r and with one another. Thus both are rational straight lines [D10.1.2, D10.1.3]. Moreover, their square-area ratios are
 a²:r² = 6:2,     b²:r² = 4:2,     a²:b² = 3:2
[D5.5]. Apply 10.9 directly, since these are precisely square-area ratios: by Step 3, a is incommensurable in length with r, b is incommensurable in length with r, and a is incommensurable in length with b [10.9]. Therefore a and b are rational straight lines commensurable in square only.

**Step 5.** The square 3S is greater than 2S, and therefore a is greater than b: a square on a shorter or equal side could not exceed the square on the other side [CN5]. Subtracting b² = 2S from a² = 3S gives
 a² − b² = S = r²
[CN3]. Thus the square on the greater term exceeds the square on the lesser by the square on r, which is incommensurable in length with the greater term a, as established by 10.9 in Step 4.

**Step 6.** Place a and b consecutively on one straight line, and call their whole L [P2, 1.3]. Since they are rational and commensurable in square only, L is a binomial straight line [10.36].

**Step 7.** Neither term of L is commensurable in length with the assigned rational line r, and the square on its greater term exceeds that on its lesser by the square on a line incommensurable in length with the greater. Consequently L is a sixth binomial straight line [D10.2.6]. The required straight line has therefore been found.

**USED:** 1.3, 10.36, 10.9, 2.1, 6.13, 6.17, 7.19, 8.11, 8.8, CN3, CN5, D10.1.2, D10.1.3, D10.2.6, D5.5, D7.18, P2
**Human refs (from References field):** 10.36, 10.6, 10.9, 5.19, 5.22
**Jaccard:** 0.100 — AI adds ['1.3', '2.1', '6.13', '6.17', '7.19', '8.11', '8.8', 'CN3', 'CN5', 'D10.1.2', 'D10.1.3', 'D10.2.6', 'D5.5', 'D7.18', 'P2']; Human adds ['10.6', '5.19', '5.22']

## Proposition 10.54
**Statement:** If an area be contained by a rational straight line and the first binomial, the âsideâ of the area is the irrational straight line which is called binomial.

**Step 1.** Let r be the rational straight line set out, and let a+b be the first binomial relative to it, with a>b. Write pq for the rectangle contained by p and q, and p² for the square on p. By the meaning of binomial in 10.36 and by D10.2.1, a and b are rational and commensurable in square only; moreover, a is commensurable in length with r, and a²=b²+c² for some straight line c commensurable in length with a. We must identify the side of r(a+b). [10.36, D10.2.1]

**Step 2.** Bisect b, and call its half t. Thus b=2t and t² is one fourth of b². Apply to a a rectangle equal to t² and deficient by a square. This construction is possible because b<a, so t² is less than the square on half of a. Denote the resulting parts of a by u and v; then u+v=a and uv=t². [1.10, 2.4, 6.28]

**Step 3.** Since a² exceeds b² by the square on a line commensurable in length with a, the converse direction of 10.17 shows that u and v are commensurable in length. This is the direct path supplied by the defining square-excess condition of a first binomial. Each of u and v is therefore commensurable with u+v=a, and consequently with r. [10.17, 10.15, 10.12]

**Step 4.** Construct straight lines x and y such that x²=ru and y²=rv. Since u and v are commensurable in length with the rational line r, they are rational; hence ru and rv are rational areas. Their square sides x and y are therefore rational. Furthermore, their squares are commensurable, since both are commensurable with the assigned rational square. Thus x and y are commensurable in square. [2.14, D10.1.3, 10.19, D10.1.4, 10.12, D10.1.2]

**Step 5.** The lines u and t are incommensurable in length. For t is commensurable with b, since b=2t. If u were commensurable with t, then, because a is commensurable with u, repeated application of 10.12 would make a commensurable with b, contrary to Step 1. [D10.1.1, 10.12]

**Step 6.** Rectangles of equal height are proportional to their bases. Therefore, using uv=t²,

x²:y² = ru:rv = u:v = u²:uv = u²:t².

The converse of 6.22, applied to squares, now gives x:y=u:t. Since u and t are incommensurable in length, so are x and y. Together with Step 4, this proves that x and y are rational straight lines commensurable in square only. [6.1, 5.11, 6.22, 10.11]

**Step 7.** Again by the ratios of rectangles of equal height,

x²:xy = x:y = u:t = ru:rt.

But x²=ru. Consequently the equal antecedents have the same ratio to xy and rt, so xy=rt. [6.1, 5.11, 5.9]

**Step 8.** The square on x+y is therefore

(x+y)² = x²+y²+2xy
= ru+rv+2rt
= r(u+v)+r(2t)
= ra+rb
= r(a+b).

Here the square of a sum is expanded by 2.4, rectangles are distributed by 2.1, and the established equalities are added. Thus x+y is a side of the given area. [2.4, 2.1, CN2]

**Step 9.** Since x and y are rational and commensurable in square only, 10.36 states that their sum x+y is irrational and is called binomial. By Step 8, this sum is precisely the side of the area contained by r and the first binomial a+b. Hence the side of the given area is the irrational straight line called binomial. [10.36]

**USED:** 1.10, 10.11, 10.12, 10.15, 10.17, 10.19, 10.36, 2.1, 2.14, 2.4, 5.11, 5.9, 6.1, 6.22, 6.28, CN2, D10.1.1, D10.1.2, D10.1.3, D10.1.4, D10.2.1
**Human refs (from References field):** 10.11, 10.12, 10.13, 10.15, 10.17, 10.19, 10.36, 2.14, 6.1, 6.17, D10.2.1
**Jaccard:** 0.391 — AI adds ['1.10', '2.1', '2.4', '5.11', '5.9', '6.22', '6.28', 'CN2', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.1.4']; Human adds ['10.13', '6.17']

## Proposition 10.55
**Statement:** If an area be contained by a rational straight line and the second binomial, the âsideâ of the area is the irrational straight line which is called a first bimedial.

**Step 1.** Let r be the given rational straight line, and let a+b be the second binomial, with a>b. Write pq for the rectangle contained by p and q, and p² for the square on p [D2.1]. The terms a and b are rational and commensurable in square only; b is commensurable in length with r; and a² exceeds b² by the square on a straight line commensurable in length with a [10.36, D10.2.1, D10.2.2].

**Step 2.** Bisect b, calling its half h [1.10]. Then h² is the fourth part of b² [2.4]. Since b<a, this area is smaller than the square on half of a [6.1]. Apply to a a rectangle equal to h² and deficient by a square [6.28]. Thus a is divided into positive parts x and y satisfying
x+y=a, xy=h².
By the converse direction of 10.17, x and y are commensurable in length. This is the direct splitting route: the commensurable square-difference in the definition supplies exactly the hypothesis of 10.17.

**Step 3.** Since x and y are commensurable, each is commensurable in length with their sum a [10.15]. Also h is commensurable in length with b, since b=2h [D10.1.1]. Therefore x² and y² are commensurable with a², and h² with b²: length-commensurability gives a ratio of square numbers between the squares, and hence commensurability of those squares [10.9, 10.6]. As a and b are rational, it follows that x, y, and h are rational [10.12, D10.1.3]. Moreover, h and r are commensurable in length, since both are commensurable with b [10.12].

**Step 4.** Because a is incommensurable in length with b, while b is commensurable in length with r, a is incommensurable in length with r [10.13]. Since x and y are each commensurable in length with a, each is likewise incommensurable in length with r [10.13]. But x, y, and r are rational, so each of x and y is commensurable in square only with r [D10.1.3, 10.12]. Construct straight lines u and v such that
u²=rx, v²=ry
[2.14]. Both u and v are medial, because each is the side of a rectangle contained by rational straight lines commensurable in square only [10.21].

**Step 5.** Rectangles with the same altitude are proportional to their bases; hence
u²:v²=rx:ry=x:y
[6.1]. Since x and y are commensurable, u² and v² are commensurable [10.11]. Thus u and v are commensurable in square [D10.1.2].

**Step 6.** Since xy=h², the same rectangle-ratio theorem gives
x²:h²=x²:xy=x:y
[6.1]. Comparing this with Step 5 gives u²:v²=x²:h² [5.11]. Consequently,
u:v=x:h
[6.22]. Here the converse of 6.22 is the natural choice because the equality obtained is already an equality of ratios of squares. Now x is commensurable in length with a, and h with b, whereas a and b are incommensurable in length. Therefore x and h are incommensurable in length [10.13]. The displayed proportion implies that u and v are incommensurable in length [10.11]. Together with Step 5, this shows that they are commensurable in square only.

**Step 7.** From u²=rx we have r:u=u:x [6.17]. Alternating the proportion u:v=x:h gives u:x=v:h [5.16]. Hence r:u=v:h [5.11], and therefore
uv=rh
[6.16]. The straight lines r and h are rational and commensurable in length by Step 3, so rh, and therefore uv, is a rational rectangle [10.19].

**Step 8.** The square on the sum of u and v is
(u+v)²=u²+v²+2uv
[2.4]. Substituting the established equalities and distributing rectangles gives
(u+v)²=rx+ry+2rh=r(x+y+2h)=r(a+b)
[CN2, 2.1]. Thus u+v is a side of a square equal to the given area.

**Step 9.** The straight lines u and v are medial, are commensurable in square only, and contain a rational rectangle. Their sum u+v is therefore irrational and is called a first bimedial [10.37]. Since its square equals the area contained by r and the second binomial a+b, the side of that area is a first bimedial, as required.

**USED:** 1.10, 10.11, 10.12, 10.13, 10.15, 10.17, 10.19, 10.21, 10.36, 10.37, 10.6, 10.9, 2.1, 2.14, 2.4, 5.11, 5.16, 6.1, 6.16, 6.17, 6.22, 6.28, CN2, D10.1.1, D10.1.2, D10.1.3, D10.2.1, D10.2.2, D2.1
**Human refs (from References field):** 10.11, 10.12, 10.13, 10.15, 10.17, 10.19, 10.21, 10.37, 6.1, D10.2.2
**Jaccard:** 0.345 — AI adds ['1.10', '10.36', '10.6', '10.9', '2.1', '2.14', '2.4', '5.11', '5.16', '6.16', '6.17', '6.22', '6.28', 'CN2', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.2.1', 'D2.1']

## Proposition 10.56
**Statement:** If an area be contained by a rational straight line and the third binomial, the âsideâ of the area is the irrational straight line called a second bimedial.

**Step 1.** Let r be the rational straight line set out, and let a+b be the third binomial, with a>b. Write xy for the rectangle contained by straight lines x,y, and x² for the square on x. By the definition of binomial, a and b are rational and commensurable in square only (10.36). By the definition of a third binomial, neither a nor b is commensurable in length with r, and there is a straight line c commensurable in length with a such that a²=b²+c² (D10.2.1, D10.2.3).

**Step 2.** Bisect b, putting t=b/2; thus t² is the fourth part of b² (1.10, 2.4). Apply to a a rectangle equal to t² and deficient by a square. This is possible because b<a, so the prescribed area is less than the square on half of a (6.28). Let the resulting parts of a be p and q. Then p+q=a and pq=t². Since c is commensurable in length with a, the converse direction of 10.17 gives that p and q are commensurable in length. This is the appropriate path because the defining excess-square side is commensurable with the greater term.

**Step 3.** Since p and q are commensurable, their sum a is commensurable in length with each of them (10.15). Also t is commensurable in length with b, since t measures b twice (D10.1.1). A line commensurable in length with a rational line is rational: their squares have the ratio of square numbers (10.9), hence are commensurable (10.6), and commensurability with the assigned rational square follows by 10.12 and D10.1.3. Consequently p, q, and t are rational.

**Step 4.** Because a is incommensurable in length with r, so are p and q; because b is incommensurable in length with r, so is t (10.13). Moreover, p and t are incommensurable in length. For if they were commensurable, then, using the commensurability of a with p and of t with b, two applications of 10.12 would make a and b commensurable in length, contrary to Step 1.

**Step 5.** Construct straight lines u and v such that u²=rp and v²=rq (2.14). Since r,p,q,t are rational, their squares are commensurable with one another (D10.1.3, 10.12). Together with Step 4, this shows that each of the pairs r,p; r,q; and r,t is commensurable in square only. Therefore u and v are medial straight lines, and rt is a medial area (10.21).

**Step 6.** Rectangles with the same height are proportional to their bases, so u²:v²=rp:rq=p:q (6.1). Since p and q are commensurable, u² and v² are commensurable (10.11); hence u and v are commensurable in square (D10.1.2). Furthermore, because pq=t², we have p²:t²=p²:pq=p:q (6.1). Thus u²:v²=p²:t² (5.11), and proportional squares have proportional sides, giving u:v=p:t (6.22). Since p and t are incommensurable in length, u and v are likewise incommensurable in length (10.11). Thus u and v are medial straight lines commensurable in square only.

**Step 7.** Using the proportion just obtained and rectangles with a common height gives u²:uv=u:v=p:t=rp:rt (6.1, 5.11). But u²=rp. Therefore the equal antecedent has the same ratio to uv and rt, and consequently uv=rt (5.9). The rectangle contained by u and v is therefore medial, by Step 5.

**Step 8.** The square on their sum satisfies
(u+v)²=u²+v²+2uv=rp+rq+2rt=r(p+q)+r(2t)=ra+rb=r(a+b),
by 2.4, 2.1, CN2, and CN1, using p+q=a and 2t=b. Hence u+v is the side of the given area. Since u and v are medial straight lines commensurable in square only and contain a medial rectangle, their sum is irrational and is called a second bimedial (10.38). Therefore the side of the area contained by the rational straight line and the third binomial is a second bimedial.

**USED:** 1.10, 10.11, 10.12, 10.13, 10.15, 10.17, 10.21, 10.36, 10.38, 10.6, 10.9, 2.1, 2.14, 2.4, 5.11, 5.9, 6.1, 6.22, 6.28, CN1, CN2, D10.1.1, D10.1.2, D10.1.3, D10.2.1, D10.2.3
**Human refs (from References field):** 10.13, 10.21, 10.38, D10.2.3
**Jaccard:** 0.154 — AI adds ['1.10', '10.11', '10.12', '10.15', '10.17', '10.36', '10.6', '10.9', '2.1', '2.14', '2.4', '5.11', '5.9', '6.1', '6.22', '6.28', 'CN1', 'CN2', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.2.1']

## Proposition 10.57
**Statement:** If an area be contained by a rational straight line and the fourth binomial, the âsideâ of the area is the irrational straight line called major.

**Step 1.** Let r be the given rational straight line, and let a+b be the fourth binomial relative to r, with a>b. Throughout, pq denotes the rectangle contained by p and q, and p² denotes the square on p. The terms a and b are rational and commensurable in square only; moreover, a is commensurable in length with r, and a²=b²+d² for a straight line d incommensurable in length with a. [10.36, D10.2.4]

**Step 2.** Bisect b and r, putting h=b/2 and k=r/2. [1.10] Apply to a a rectangle equal to h² and deficient by a square; this is possible because h² is less than the square on half of a. [6.28] If u and v are the resulting parts of a, then
u+v=a, and uv=h²=b²/4.
Since the excess of a² over b² is the square on a line incommensurable in length with a, the parts u and v are incommensurable in length. [10.18] This square-deficient division is the direct route: the incommensurable-excess clause of 10.18 matches exactly the defining condition of the fourth binomial.

**Step 3.** Construct straight lines x and y such that x²=ru and y²=rv. [2.14] Then
x²+y²=ru+rv=r(u+v)=ra. [2.1]
Since r and a are rational and commensurable in length, ra is rational. Thus the sum of the squares on x and y is rational. [10.19]

**Step 4.** Rectangles with the same height are proportional to their bases, so
x²:y²=ru:rv=u:v. [6.1]
But u and v are incommensurable. Therefore x² and y² are incommensurable, and consequently x and y are incommensurable in square. [10.11, D10.1.2]

**Step 5.** We next identify the rectangle xy. Since x²=ru, y²=rv, and h²=uv, proportionality of rectangles gives
x²:u²=ru:u²=r:u=rv:uv=y²:h². [6.1, 5.11]
The converse of the theorem on proportional similar figures therefore gives x:u=y:h; it applies directly here because the compared figures are squares. [6.22] Also, x²=ru gives r:x=x:u. [6.17] Hence r:x=y:h, and therefore
xy=rh. [5.11, 6.16]

**Step 6.** The half k of r is rational and commensurable in length with r. [D10.1.1, D10.1.3] Since a is commensurable in length with r, it is also commensurable in length with k. [10.12] But a and b are incommensurable in length; hence k and b are incommensurable in length. [10.13] Being rational, k and b are commensurable in square, so they are commensurable in square only. [D10.1.3, 10.12] Their rectangle kb is therefore medial. [10.21] Now r=2k and b=2h, whence
rh=2kh=kb. [2.1]
Together with Step 5, this proves that xy is medial. [CN1]

**Step 7.** The straight lines x and y are thus incommensurable in square, the sum x²+y² is rational, and their rectangle xy is medial. These are precisely the hypotheses of 10.39. Consequently x+y is irrational and is the straight line called major. [10.39]

**Step 8.** Finally, the square on their sum is
(x+y)²=x²+y²+2xy=ra+2rh=ra+rb=r(a+b). [2.4, 2.1, CN1, CN2]
Thus the square on the major straight line x+y equals the given area contained by r and the fourth binomial a+b. Accordingly, the side of that area is the irrational straight line called major. [D10.1.4]

**USED:** 1.10, 10.11, 10.12, 10.13, 10.18, 10.19, 10.21, 10.36, 10.39, 2.1, 2.14, 2.4, 5.11, 6.1, 6.16, 6.17, 6.22, 6.28, CN1, CN2, D10.1.1, D10.1.2, D10.1.3, D10.1.4, D10.2.4
**Human refs (from References field):** 10.11, 10.13, 10.18, 10.19, 10.21, 10.39, 6.1, D10.2.4
**Jaccard:** 0.320 — AI adds ['1.10', '10.12', '10.36', '2.1', '2.14', '2.4', '5.11', '6.16', '6.17', '6.22', '6.28', 'CN1', 'CN2', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.1.4']

## Proposition 10.58
**Statement:** If an area be contained by a rational straight line and the fifth binomial, the âsideâ of the area is the irrational straight line called the side of a rational plus a medial area.

**Step 1.** Let r be the given rational straight line, and let a+b be the fifth binomial, with a>b. Products below denote rectangular areas, and t² denotes the square on t. The terms a and b are rational and commensurable in square only (10.36). By the definition of the fifth binomial, b is commensurable in length with r, while a² exceeds b² by the square on a straight line incommensurable in length with a (D10.2.4, D10.2.5).

**Step 2.** Bisect b, and denote its half by h (1.10). Thus h² is the fourth part of b² (2.4). Since b<a, this area is less than the square on half of a (2.4). Apply to a a rectangle equal to h² and deficient by a square, as permitted by 6.28. If x and y are the resulting parts of a, then
x+y=a,  xy=h².

**Step 3.** The parts x and y are incommensurable in length, by 10.18. We use its incommensurable-division clause directly: the applied rectangle equals the fourth part of b², and the defining excess-square side is incommensurable with a.

**Step 4.** Construct u as a mean proportional between r and x, and v as a mean proportional between r and y (6.13). Then
r:u=u:x,  r:v=v:y,
and consequently u²=rx and v²=ry (6.17). Rectangles of the same altitude are proportional to their bases, so
u²:v²=rx:ry=x:y (6.1).
Since x and y are incommensurable, u² and v² are incommensurable (10.11). Therefore u and v are incommensurable in square (D10.1.2).

**Step 5.** Since a is incommensurable in length with b, whereas b is commensurable in length with r, a is incommensurable in length with r (10.13). The rational lines a and r are nevertheless commensurable in square, since their squares are commensurable with the assigned rational square (D10.1.3, 10.12). Hence ar is a medial area (10.21). Moreover,
u²+v²=rx+ry=r(x+y)=ra
by Step 4 and distributivity of rectangles (CN2, 2.1). Thus the sum of the squares on u and v is medial.

**Step 6.** We next show that uv=rh. Since xy=h², rectangles of equal altitude give
x²:h²=x²:xy=x:y (6.1).
Together with Step 4, this yields u²:v²=x²:h² (5.11). Applying the converse of 6.22 to these squares gives u:v=x:h; alternately, u:x=v:h (5.16). But r:u=u:x by the construction of u. Therefore r:u=v:h (5.11), and hence
uv=rh (6.16).

**Step 7.** The rectangle rb is rational, because r and b are rational and commensurable in length (10.19). Since b consists of two copies of h, rb consists of two copies of rh (2.1). Thus rh is commensurable with rb, having rh itself as a common measure (D10.1.1). It follows that rh is rational, since rb is commensurable with the assigned rational square (10.12, D10.1.4). By Step 6, the rectangle uv is therefore rational.

**Step 8.** By the square-of-a-sum identity and the established equalities,
(u+v)²=u²+v²+2uv=ra+2rh=ra+rb=r(a+b)
(2.4, 2.1, CN1, CN2). Thus u+v is the side of the given area (D10.1.4). The lines u and v are incommensurable in square, the sum of their squares is medial, and their rectangle is rational. These are exactly the hypotheses of 10.40, which therefore supplies the direct classification: u+v is irrational and is called the side of a rational plus a medial area. Hence the side of the area contained by the rational straight line and the fifth binomial has the required name and nature.

**USED:** 1.10, 10.11, 10.12, 10.13, 10.18, 10.19, 10.21, 10.36, 10.40, 2.1, 2.4, 5.11, 5.16, 6.1, 6.13, 6.16, 6.17, 6.22, 6.28, CN1, CN2, D10.1.1, D10.1.2, D10.1.3, D10.1.4, D10.2.4, D10.2.5
**Human refs (from References field):** 10.11, 10.12, 10.13, 10.18, 10.19, 10.21, 10.40, 6.1, D10.2.5
**Jaccard:** 0.333 — AI adds ['1.10', '10.36', '2.1', '2.4', '5.11', '5.16', '6.13', '6.16', '6.17', '6.22', '6.28', 'CN1', 'CN2', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.1.4', 'D10.2.4']

## Proposition 10.59
**Statement:** If an area be contained by a rational straight line and the sixth binomial, the âsideâ of the area is the irrational straight line called the side of the sum of two medial areas.

**Step 1.** Write xy for the rectangle contained by straight lines x and y, and x² for the square on x [D2.1]. Let the given area be r(a+b), where r is the given rational straight line and a>b are the terms of the sixth binomial. Thus a and b are rational and commensurable in square only; neither is commensurable in length with r. Moreover, a²=b²+d² for a straight line d incommensurable in length with a [10.36, D10.2.4, D10.2.6].

**Step 2.** Bisect b, and call its half h [1.10]. The lines b and h are commensurable in length [D10.1.1], and b²=4h² [2.4]. Consequently h² is commensurable with b²; since b is rational, h is also rational [D10.1.1, 10.12, D10.1.3]. Since b is incommensurable in length with both r and a, its commensurable half h is likewise incommensurable in length with both r and a [10.13].

**Step 3.** Apply to a a rectangle equal to h², deficient by a square. This construction is possible because h² is the fourth part of b² and b<a [6.28]. Let the resulting parts of a be m and n. Then
m+n=a, and mn=h²=¼b².
The sixth-binomial condition from Step 1 gives precisely the excess-square hypothesis of 10.18; we therefore use its incommensurable case directly. It follows that m and n are incommensurable in length [10.18].

**Step 4.** Construct square-sides u and v such that
u²=rm, and v²=rn [2.14].
Rectangles with the same height are proportional to their bases, so u²:v²=m:n [6.1]. Since m and n are incommensurable, u² and v² are incommensurable [10.11]. Thus u and v are incommensurable in square [D10.1.2]. Also,
u²+v²=rm+rn=r(m+n)=ra [2.1].

**Step 5.** We next show that uv=rh. Using the equalities already obtained and comparing rectangles with a common height gives
v²:h²=rn:mn=r:m=rm:m²=u²:m² [6.1, 5.11].
The converse of 6.22 applies directly to these proportional squares and yields v:h=u:m [6.22]. But u²=rm gives r:u=u:m [6.17]. Hence r:u=v:h [5.11], and therefore rh=uv [6.16].

**Step 6.** Since r and a are rational and incommensurable in length, ra is a medial area [10.21]. Since r and h are likewise rational and incommensurable in length, rh is also a medial area [10.21]. Furthermore,
ra:rh=a:h [6.1].
The lines a and h are incommensurable in length by Step 2, so the areas ra and rh are incommensurable [10.11]. By Steps 4 and 5, therefore, the sum u²+v² is medial, while the rectangle uv is medial and incommensurable with that sum.

**Step 7.** The square on u+v is
(u+v)²=u²+v²+2uv [2.4].
Substituting the equalities from Steps 4 and 5, and using b=2h, gives
(u+v)²=ra+2rh=ra+rb=r(a+b) [2.1, CN2, CN1].
Thus u+v is the side of a square equal to the given area.

**Step 8.** The straight lines u and v are incommensurable in square; the sum of their squares is medial; and their rectangle is medial and incommensurable with that sum. Therefore their sum u+v is irrational and is called the side of the sum of two medial areas [10.41]. By Step 7, this is the side of the area contained by the given rational straight line and the sixth binomial, as required.

**USED:** 1.10, 10.11, 10.12, 10.13, 10.18, 10.21, 10.36, 10.41, 2.1, 2.14, 2.4, 5.11, 6.1, 6.16, 6.17, 6.22, 6.28, CN1, CN2, D10.1.1, D10.1.2, D10.1.3, D10.2.4, D10.2.6, D2.1
**Human refs (from References field):** 10.11, 10.13, 10.21, 10.41, 6.1
**Jaccard:** 0.200 — AI adds ['1.10', '10.12', '10.18', '10.36', '2.1', '2.14', '2.4', '5.11', '6.16', '6.17', '6.22', '6.28', 'CN1', 'CN2', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.2.4', 'D10.2.6', 'D2.1']

## Proposition 10.60
**Statement:** The square on the binomial straight line applied to a rational straight line produces as breadth the first binomial.

**Step 1.** Let the given binomial be a+b, where a>b and a,b are rational straight lines commensurable in square only [10.36]. Let r be the rational straight line to which its square is to be applied. Write pq for the rectangle contained by p,q, and p² for the square on p.

**Step 2.** Construct straight lines u,v,w such that
ru=a², rv=b², rw=ab.
These are obtained by constructing fourth proportionals and using the equality of the rectangles contained by the extremes and the means [6.12, 6.16]. Put X=u+v and Y=2w.

**Step 3.** The areas a² and b² are rational and commensurable [D10.1.2, D10.1.3, D10.1.4]. Their sum is therefore rational: it is commensurable with a², and hence with the assigned rational square [10.15, 10.12, D10.1.4]. Since rX=ru+rv=a²+b² [2.1], application of these rational areas to r shows that u,v,X are rational and commensurable in length with r [10.20]. In particular, u and v are commensurable in length [10.12].

**Step 4.** Since a,b are rational and commensurable in square only, ab is equal to the square on a medial straight line [10.21]. Consequently, its application to r produces w rational but incommensurable in length with r [10.22]. Now Y=2w, so Y and w are commensurable in length [D10.1.1], while Y²=4w² [2.4]. Thus Y² is commensurable with w², and Y is rational [D10.1.1, 10.12, D10.1.3]. Moreover, Y is incommensurable in length with r [10.13].

**Step 5.** Because X and Y are rational, their squares are commensurable [D10.1.3, 10.12, D10.1.2]. But X is commensurable in length with r, whereas Y is not; hence X and Y are incommensurable in length [10.13]. Therefore X+Y is a binomial, with terms X and Y [10.36].

**Step 6.** By the addition of rectangles and the square-of-a-sum identity,
r(X+Y)=ru+rv+2rw=a²+b²+2ab=(a+b)² [2.1, 2.4].
Thus X+Y is the breadth obtained by applying the given square to r.

**Step 7.** Rectangles of equal height are proportional to their bases. Using the equalities of Step 2 gives
u:w=a²:ab=a:b,
and
w:v=ab:b²=a:b [6.1].
Hence u:w=w:v [5.11], and therefore uv=w² [6.16].

**Step 8.** Since a>b, the square on the remaining segment a−b is positive, and
a²+b²=2ab+(a−b)²>2ab [2.7, CN5].
Thus rX>rY. Rectangles on the same height r are proportional to their breadths, so X>Y [6.1, 5.14].

**Step 9.** Apply the rectangle uv to X=u+v, taking u along X and v as its perpendicular breadth. It is deficient by the square v², since vX=uv+v² [2.1]. Its area is w², which is one-fourth of Y² by Steps 4 and 7. The resulting division of X is into u and v, already proved commensurable in length. The commensurable-cut criterion is therefore the direct choice here: since X>Y, it shows that X² exceeds Y² by the square on a straight line commensurable in length with X [10.17].

**Step 10.** The breadth X+Y is consequently a binomial whose greater term X is commensurable in length with the rational straight line r, and whose greater term's square exceeds the lesser term's square by the square on a straight line commensurable in length with the greater. It is therefore a first binomial [D10.2.1]. By Step 6, this is exactly the breadth produced by applying the square on the given binomial to r. Hence the proposition is proved.

**USED:** 10.12, 10.13, 10.15, 10.17, 10.20, 10.21, 10.22, 10.36, 2.1, 2.4, 2.7, 5.11, 5.14, 6.1, 6.12, 6.16, CN5, D10.1.1, D10.1.2, D10.1.3, D10.1.4, D10.2.1
**Human refs (from References field):** 10.11, 10.13, 10.15, 10.17, 10.20, 10.21, 10.22, 10.36, 10.53, 6.1, 6.17, D10.2.1
**Jaccard:** 0.360 — AI adds ['10.12', '2.1', '2.4', '2.7', '5.11', '5.14', '6.12', '6.16', 'CN5', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.1.4']; Human adds ['10.11', '10.53', '6.17']

## Proposition 10.61
**Statement:** The square on the first bimedial straight line applied to a rational straight line produces as breadth the second binomial.

**Step 1.** Let L be a first bimedial straight line, and let r be the rational straight line to which its square is applied. Write L = a + b, where a > b. By 10.37, a and b are medial straight lines commensurable in square only, and the rectangle ab is rational. Here xy denotes the rectangle contained by x and y, and x² denotes the square on x (D2.1). We use the direct decomposition of L², because its component areas supply the prospective binomial terms.

**Step 2.** Construct fourth proportionals p, q, t such that r:a = a:p, r:b = b:q, and r:a = b:t (6.12). Consequently,
 rp = a², rq = b², rt = ab
by 6.16. Put U = p + q and V = t + t. By 2.4, 2.1, and CN2,
 L² = a² + b² + 2ab = r(p + q + 2t) = r(U + V).
Thus U + V is the breadth of an application of L² to r.

**Step 3.** Since a and b are medial, p and q are rational and each is incommensurable in length with r (10.22). Since ab is rational, t is rational and commensurable in length with r (10.20). Moreover, rectangles on the same base have the ratio of their breadths, so p:q = a²:b² (6.1). The squares a² and b² are commensurable (D10.1.2); hence p and q are commensurable in length (10.11).

**Step 4.** Since p and q are commensurable, U = p + q is commensurable in length with p (10.15). Therefore U is rational: by 10.9 and 10.6, U² and p² are commensurable, and rationality follows from 10.12 and D10.1.3. Also, V = 2t is commensurable in length with t, since t measures V (D10.1.1). The same argument using 10.9, 10.6, 10.12, and D10.1.3 shows that V is rational. Since t is commensurable in length with r, so is V (10.12).

**Step 5.** Because U is commensurable in length with p, while p is incommensurable in length with r, U is incommensurable in length with r (10.13). Since V is commensurable in length with r, U and V are incommensurable in length (10.13). Being rational, however, their squares are commensurable with the square on the assigned rational straight line and therefore with one another (D10.1.3, 10.12, D10.1.2). Thus U and V are rational straight lines commensurable in square only, and U + V is a binomial (10.36).

**Step 6.** Using the rectangles constructed in Step 2 and the ratios of rectangles with a common side, we obtain
 p:t = a²:ab = a:b,
 t:q = ab:b² = a:b
(6.1). Hence p:t = t:q (5.11). The rectangle criterion already used in Step 2 now gives
 pq = t²
(6.16).

**Step 7.** Since a > b, we have a² > b² (2.4, CN5); therefore p > q by their proportion in Step 3 (5.14). Let w = p − q. Applying 2.7 to p divided into q and w gives
 p² + q² = 2pq + w².
Also, 2.4 gives U² = p² + q² + 2pq and V² = 4t². Combining these equalities with pq = t² yields
 U² = w² + 4pq = w² + V²
(CN2, CN3). Since w is positive, U² > V², and hence U > V (CN5, 2.4).

**Step 8.** Since p = q + w and p is commensurable in length with q, the converse part of 10.15 shows that w is commensurable in length with q. Also, U = p + q is commensurable in length with q (10.15). Therefore w is commensurable in length with U (10.12).

**Step 9.** The breadth U + V is thus a binomial whose greater term U has its square exceeding the square on its lesser term V by w², where w is commensurable in length with U. Furthermore, the lesser term V is commensurable in length with the rational straight line r. These are precisely the defining conditions of a second binomial (D10.2.2). Therefore the square on a first bimedial straight line, applied to a rational straight line, produces as breadth the second binomial.

**USED:** 10.11, 10.12, 10.13, 10.15, 10.20, 10.22, 10.36, 10.37, 10.6, 10.9, 2.1, 2.4, 2.7, 5.11, 5.14, 6.1, 6.12, 6.16, CN2, CN3, CN5, D10.1.1, D10.1.2, D10.1.3, D10.2.2, D2.1
**Human refs (from References field):** 10.11, 10.13, 10.15, 10.17, 10.20, 10.21, 10.22, 10.23, 10.36, 10.37, 6.1, D10.2.2
**Jaccard:** 0.310 — AI adds ['10.12', '10.6', '10.9', '2.1', '2.4', '2.7', '5.11', '5.14', '6.12', '6.16', 'CN2', 'CN3', 'CN5', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D2.1']; Human adds ['10.17', '10.21', '10.23']

## Proposition 10.62
**Statement:** The square on the second bimedial straight line applied to a rational straight line produces as breadth the third binomial.

**Step 1.** Let s be a second bimedial straight line, and let r be the rational straight line to which its square is to be applied. By 10.38, write s=a+b, where a>b are medial straight lines commensurable in square only, and the rectangle ab is medial—that is, equal to a square on a medial straight line. Throughout, u² denotes the square on u and uv the rectangle contained by u and v. [10.38]

**Step 2.** Construct breadths x, y, z such that
rx=a², ry=b², rz=ab.
These constructions are possible by taking fourth proportionals and using the equality of the rectangles contained by the extremes and the means. Since each of the three applied areas is a square on a medial straight line, x, y, z are rational and each is incommensurable in length with r. [6.12, 6.16, 10.22]

**Step 3.** Rectangles of the same height are proportional to their bases. Consequently,
x:y=a²:b²,
x:z=a²:ab=a:b,
z:y=ab:b²=a:b.
Since a and b are commensurable in square, x and y are commensurable in length. Since a and b are incommensurable in length, x and z are incommensurable in length. Also x>y, because a²>b². [6.1, D10.1.2, 10.11]

**Step 4.** Put p=x+y and q=2z. Because x and y are commensurable, p is commensurable in length with x; and q is commensurable in length with z, since z measures q twice. Lines commensurable in length have commensurable squares: their squares have a numerical ratio by 10.9 and hence are commensurable by 10.6. Therefore p and q are rational, since their squares are respectively commensurable with the squares on the rational lines x and z, and thus with the assigned rational square. [10.15, D10.1.1, 10.9, 10.6, 10.12, D10.1.3]

**Step 5.** Since p is commensurable in length with x, while x is incommensurable in length with r, p is incommensurable in length with r. Likewise, q is incommensurable in length with r. Moreover, x and z are incommensurable in length; hence p and z are incommensurable in length, and, because q and z are commensurable in length, p and q are incommensurable in length. [10.13]

**Step 6.** The proportion already obtained, x:z=z:y, gives xy=z² by 6.16. Since q=2z, the square on q is four times the square on z; hence
q²=4xy.
Because x and y are unequal parts of p, 2.5 shows that xy is less than one-quarter of p². Thus q²<p², and therefore p>q. [6.16, 2.4, 2.5]

**Step 7.** Use the commensurable-partition criterion 10.17: it is the natural direct choice because the required partition is already supplied by x and y. Indeed, the rectangle xy, applied to p=x+y with height y, is deficient by the square y². Its area is one-quarter of q², and it divides p into the commensurable lengths x and y. Therefore the square on p exceeds the square on q by the square on a straight line commensurable in length with p. [10.17]

**Step 8.** By distribution of rectangles and the square-of-a-sum identity,
r(p+q)=rx+ry+2rz=a²+b²+2ab=(a+b)²=s².
Thus p+q is precisely the breadth produced when the square on s is applied to r; equality of rectangles on the same base gives equality of their breadths. [2.1, 2.4, 6.1]

**Step 9.** The rational lines p and q are commensurable in square, since their squares are each commensurable with the assigned rational square; but they are incommensurable in length by Step 5. Hence p+q is a binomial. Its greater term is p; the square on p exceeds that on q by the square on a line commensurable in length with p; and neither p nor q is commensurable in length with r. Therefore p+q is the third binomial relative to r. Accordingly, the square on the second bimedial straight line, applied to a rational straight line, produces as breadth the third binomial. [10.12, D10.1.3, D10.1.2, 10.36, D10.2.1, D10.2.3]

**USED:** 10.11, 10.12, 10.13, 10.15, 10.17, 10.22, 10.36, 10.38, 10.6, 10.9, 2.1, 2.4, 2.5, 6.1, 6.12, 6.16, D10.1.1, D10.1.2, D10.1.3, D10.2.1, D10.2.3
**Human refs (from References field):** 10.11, 10.12, 10.13, 10.15, 10.22, 10.23, 10.36, 10.38, 6.1, D10.2.3
**Jaccard:** 0.409 — AI adds ['10.17', '10.6', '10.9', '2.1', '2.4', '2.5', '6.12', '6.16', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.2.1']; Human adds ['10.23']

## Proposition 10.63
**Statement:** The square on the major straight line applied to a rational straight line produces as breadth the fourth binomial.

**Step 1.** Let L be a major straight line and r the rational straight line to which its square is to be applied. Write uv for the rectangle contained by u and v, and u² for the square on u. By the characterization of a major straight line, L = a + b, where a² and b² are incommensurable, a² + b² is rational, and ab is medial. Since a and b are unequal, name them so that a > b. (10.39; D10.1.2)

**Step 2.** Construct straight lines p, q, t such that rp = a², rq = b², and rt = ab; these constructions follow by taking fourth proportionals and using the equality of the rectangles contained by the extremes and means. (6.12; 6.16) Set x = p + q and y = 2t. Then rx = a² + b² and ry = 2ab, so r(x + y) = a² + b² + 2ab = (a + b)² = L². Thus x + y is the breadth produced by applying the square on L to r. (2.1; 2.4)

**Step 3.** Since rx = a² + b² is a rational area applied to the rational straight line r, its breadth x is rational and commensurable in length with r. (10.20)

**Step 4.** Since rt = ab is medial, its application to r produces a rational breadth t incommensurable in length with r. (10.22) Now y = 2t is commensurable in length with t, since t measures both. (D10.1.1) Also y² = 4t²; any common area-measure of t² and the assigned rational square therefore measures y² as well. Hence y is rational. (2.4; D10.1.1; D10.1.3; D10.1.4) Since t and y are commensurable, while t is incommensurable with r, y is incommensurable in length with r. (10.13)

**Step 5.** Because x is commensurable in length with r and y is incommensurable in length with r, x and y are incommensurable in length. (10.13) Since both are rational, their squares are commensurable with the assigned rational square and therefore with one another. Thus x and y are commensurable in square only, and x + y is a binomial. (D10.1.3; 10.12; D10.1.2; 10.36)

**Step 6.** Because a > b, we have a² + b² = 2ab + (a − b)² > 2ab. (2.7; CN5) Consequently rx > ry. Rectangles with the same altitude are proportional to their bases, so x > y. Thus x is the greater term of this binomial. (6.1; 5.14)

**Step 7.** The rectangles rp and rq have the same altitude, and therefore p:q = rp:rq = a²:b². Since a² and b² are incommensurable, p and q are incommensurable in length. (6.1; 10.11)

**Step 8.** Again, comparison of rectangles with a common altitude gives p:t = a²:ab = a:b and t:q = ab:b² = a:b. Hence p:t = t:q, and therefore pq = t². (6.1; 5.11; 6.16) Since y = 2t, its square is four times t². Thus pq is one-fourth of y². (2.4)

**Step 9.** Apply the rectangle pq to x = p + q, taking p as its applied base and q as its height. The deficiency on the remaining segment q is precisely the square q². This rectangle equals one-fourth of y², and it divides x into the incommensurable parts p and q. Since x > y, 10.18 gives that x² exceeds y² by the square on a straight line incommensurable in length with x. This is the direct path: the original incommensurable squares have supplied exactly the incommensurable parts required by 10.18. (10.18)

**Step 10.** Therefore x + y is a binomial whose greater term x is commensurable in length with the given rational straight line r, while x² exceeds y² by the square on a straight line incommensurable in length with x. By definition, x + y is a fourth binomial. Since it is the breadth produced by applying L² to r, the proposition follows. (D10.2.4)

**USED:** 10.11, 10.12, 10.13, 10.18, 10.20, 10.22, 10.36, 10.39, 2.1, 2.4, 2.7, 5.11, 5.14, 6.1, 6.12, 6.16, CN5, D10.1.1, D10.1.2, D10.1.3, D10.1.4, D10.2.4
**Human refs (from References field):** 10.11, 10.13, 10.18, 10.20, 10.22, 10.36, 10.39, 6.1, D10.2.4
**Jaccard:** 0.409 — AI adds ['10.12', '2.1', '2.4', '2.7', '5.11', '5.14', '6.12', '6.16', 'CN5', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.1.4']

## Proposition 10.64
**Statement:** The square on the side of a rational plus a medial area applied to a rational straight line produces as breadth the fifth binomial.

**Step 1.** Let s be the given side of a rational plus a medial area, and let r be the rational straight line to which its square is applied. By the naming clause of 10.40, write s = a + b, with a > b, where a² and b² are incommensurable, a² + b² is medial, and the rectangle ab is rational. Here xy denotes the rectangle contained by x and y (D2.1). We take the direct decomposition route: the incommensurability of a² and b² will supply the incommensurable division required by 10.18.

**Step 2.** Construct u, v, and h as fourth proportionals so that r:a = a:u, r:b = b:v, and r:a = b:h (6.12). Then ru = a², rv = b², and rh = ab (6.16). Put p = u + v and q = h + h. By distributivity of rectangles and the square-of-a-sum identity,
r(p + q) = ru + rv + 2rh = a² + b² + 2ab = (a + b)²
(2.1, 2.4). Thus p + q is the breadth obtained by applying the given square to r.

**Step 3.** The rectangle rp equals the medial area a² + b², so p is rational and incommensurable in length with r (10.22). Also rq = 2ab is rational: a common measure of ab and the assigned rational square also measures 2ab and that square (D10.1.1, D10.1.4). Therefore q is rational and commensurable in length with r (10.20).

**Step 4.** Since p and q are rational, their squares are each commensurable with the assigned rational square, and hence with one another (D10.1.3, 10.12). Thus p and q are commensurable in square (D10.1.2). But q is commensurable in length with r, whereas p is not; consequently p and q are incommensurable in length (10.13). Their sum p + q is therefore a binomial (10.36).

**Step 5.** Since a > b, the square on a − b is positive, and
rp = a² + b² = 2ab + (a − b)² = rq + (a − b)²
(2.7). Hence rp exceeds rq. Rectangles with the same positive altitude increase with their bases, by 2.1 and CN5; therefore p > q.

**Step 6.** Rectangles of the same altitude are proportional to their bases (6.1), so
u:v = ru:rv = a²:b².
Since a² and b² are incommensurable, u and v are incommensurable in length (10.11). Again, using common altitudes,
u:h = a²:ab = a:b,
and
h:v = ab:b² = a:b
(6.1). Hence u:h = h:v (5.11). Using again the rectangle–proportion equivalence already invoked in Step 2, we obtain uv = h² (6.16). Since q = h + h, the square on q is four times the square on h (2.4). Thus uv is one-fourth of q².

**Step 7.** Because p = u + v, the rectangle uv, applied along the portion u of p with height v, falls short of the rectangle on the whole of p by the square v² (2.1). It is therefore an application to p of one-fourth of q², deficient by a square, and it divides p into the incommensurable parts u and v. Since p > q, 10.18 applies: p² exceeds q² by the square on a straight line incommensurable in length with p.

**Step 8.** We have shown that p + q is a binomial, that p is its greater term, that its lesser term q is commensurable in length with the rational straight line r set out, and that p² exceeds q² by the square on a straight line incommensurable in length with p. These are precisely the defining conditions of a fifth binomial (D10.2.4, D10.2.5). Therefore the square on the side of a rational plus a medial area, applied to a rational straight line, produces as breadth the fifth binomial.

**USED:** 10.11, 10.12, 10.13, 10.18, 10.20, 10.22, 10.36, 10.40, 2.1, 2.4, 2.7, 5.11, 6.1, 6.12, 6.16, CN5, D10.1.1, D10.1.2, D10.1.3, D10.1.4, D10.2.4, D10.2.5, D2.1
**Human refs (from References field):** 10.13, 10.18, 10.20, 10.22, 10.36, 10.40
**Jaccard:** 0.261 — AI adds ['10.11', '10.12', '2.1', '2.4', '2.7', '5.11', '6.1', '6.12', '6.16', 'CN5', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.1.4', 'D10.2.4', 'D10.2.5', 'D2.1']

## Proposition 10.65
**Statement:** The square on the side of the sum of two medial areas applied to a rational straight line produces as breadth the sixth binomial.

**Step 1.** Let s be the given side of the sum of two medial areas, and let r be the given rational straight line. Write s=a+b according to 10.41, and put M=a²+b² and N=ab, where products denote rectangular areas. Thus a² and b² are incommensurable, while M and N are medial areas incommensurable with one another. [10.41, D10.1.2]

**Step 2.** Using fourth proportionals, take straight lines u,v,w such that ru=a², rv=b², and rw=ab. [6.12, 6.16] Put p=u+v and q=2w. Distributing rectangles gives rp=M and rq=2N. Moreover, s²=M+2N, so r(p+q)=s². Therefore p+q is the breadth produced by applying the square on s to r. [2.1, 2.4]

**Step 3.** Since M and N are medial areas, their application to r shows that p and w are rational and each is incommensurable in length with r. [10.22] Since q=2w, q is commensurable in length with w. [D10.1.1] Also q²=4w²; hence any common measure of w² and the square on the assigned rational straight line also measures q². Thus q is rational. [2.4, D10.1.2, D10.1.3] Since w is incommensurable in length with r, so is q. [10.13]

**Step 4.** Rectangles of the same altitude have the ratio of their bases, so p:w=M:N. [6.1] Since M and N are incommensurable, p and w are incommensurable in length. [10.11] Since q is commensurable in length with w, p and q are incommensurable in length. [10.13] But p and q are rational, so their squares are commensurable with the same assigned rational square, and therefore with one another. [D10.1.3, 10.12] Consequently p and q are rational straight lines commensurable in square only, and p+q is a binomial. [10.36]

**Step 5.** The lines a and b are unequal, since their squares are incommensurable. [D10.1.1] Interchanging their names if necessary, take a>b. Then a²+b²=2ab+(a−b)², whence M>2N. [2.7, CN5] Since p:q=M:2N, it follows that p>q. Thus p is the greater term of the binomial. [6.1, D5.5]

**Step 6.** The applications of a² and b² to the same line r give u:v=a²:b². [6.1] Since a² and b² are incommensurable, u and v are incommensurable in length. [10.11]

**Step 7.** Again, comparison of rectangles with equal altitudes gives u:w=a²:ab=a:b and w:v=ab:b²=a:b. [6.1] Hence u:w=w:v, and therefore uv=w². [5.11, 6.17] Since q²=4w², the rectangle uv equals the fourth part of the square on q. [2.4]

**Step 8.** Because p=u+v, the rectangle uv is an application to p deficient by the square on v: indeed, pv=uv+v². [2.1] Its dividing parts u and v are incommensurable in length by Step 6. The direct path is therefore to use the incommensurable-division criterion 10.18. Applied to the greater line p and the lesser q, it proves that the square on p exceeds the square on q by the square on a straight line incommensurable in length with p. [10.18]

**Step 9.** Thus p+q is a binomial whose greater term is p; neither term is commensurable in length with r; and the square on the greater term exceeds that on the lesser by the square on a straight line incommensurable in length with the greater. By definition, p+q is a sixth binomial. [D10.2.6] Since r(p+q)=s² by Step 2, the square on the side of the sum of two medial areas, applied to a rational straight line, produces as breadth the sixth binomial.

**USED:** 10.11, 10.12, 10.13, 10.18, 10.22, 10.36, 10.41, 2.1, 2.4, 2.7, 5.11, 6.1, 6.12, 6.16, 6.17, CN5, D10.1.1, D10.1.2, D10.1.3, D10.2.6, D5.5
**Human refs (from References field):** 10.11, 10.22, 10.36, 10.41, 6.1
**Jaccard:** 0.238 — AI adds ['10.12', '10.13', '10.18', '2.1', '2.4', '2.7', '5.11', '6.12', '6.16', '6.17', 'CN5', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.2.6', 'D5.5']

## Proposition 10.66
**Statement:** A straight line commensurable in length with a binomial straight line is itself also binomial and the same in order.

**Step 1.** Let L be a binomial straight line, and let M be commensurable in length with L. Fix the assigned rational straight line r relative to which the order is determined. Write L = a + b, where a > b and a, b are rational straight lines commensurable in square only [10.36; D10.1.3]. Throughout, x² denotes the square on a straight line x.

**Step 2.** We take the direct route of transferring the two terms proportionally. Divide M into c + d in the same ratio as L is divided into a + b, so that a:b = c:d [6.10]. By alternation and the proposition on sums of antecedents and consequents,

a:c = b:d = (a + b):(c + d) = L:M [5.16; 5.12].

Since a > b, the proportion a:c = b:d gives c > d [5.14].

**Step 3.** Since L and M are commensurable in length, the proportions in Step 2 show that a and c are commensurable in length, and likewise b and d [10.11]. Moreover, since a and b are incommensurable in length and a:b = c:d, c and d are incommensurable in length [10.11].

**Step 4.** Because a and c are commensurable in length, a²:c² is the ratio of a square number to a square number; hence a² and c² are commensurable areas [10.9; 10.6]. Similarly, b² and d² are commensurable. Since a and b are rational, a² and b² are each commensurable with r² [D10.1.3; D10.1.2]. Therefore c² and d² are each commensurable with r² [10.12], and consequently c and d are rational straight lines [D10.1.3].

**Step 5.** Since c² and d² are commensurable with the same area r², they are commensurable with one another [10.12]. Thus c and d are commensurable in square, but, by Step 3, not in length [D10.1.2]. They are therefore rational straight lines commensurable in square only, so their sum M is binomial [10.36].

**Step 6.** The length-commensurability of each term with the assigned line r is preserved. Indeed, a and c are commensurable in length; therefore, if a is commensurable in length with r, so is c [10.12], while if a is incommensurable in length with r, so is c [10.13]. The same argument applies to b and d. Hence the alternatives that the greater term, the lesser term, or neither term is commensurable in length with r are the same for L and M [10.12; 10.13].

**Step 7.** For the square-excess condition, apply 10.14 directly to a:b = c:d; this is the natural choice because it transfers exactly the condition appearing in the definitions of the orders. If a² exceeds b² by the square on a straight line commensurable in length with a, then c² exceeds d² by the square on a straight line commensurable in length with c. If instead the former excess-square side is incommensurable in length with a, then the latter is incommensurable in length with c [10.14].

**Step 8.** When the excess-square side is commensurable in length with the greater term, the greater-term, lesser-term, and neither-term alternatives of Step 6 define respectively the first, second, and third binomials [D10.2.1; D10.2.2; D10.2.3]. When the excess-square side is incommensurable in length with the greater term, those same alternatives define respectively the fourth, fifth, and sixth binomials [D10.2.4; D10.2.5; D10.2.6]. Steps 6 and 7 preserve both defining conditions. Therefore M is itself binomial and has the same order as L.

**USED:** 10.11, 10.12, 10.13, 10.14, 10.36, 10.6, 10.9, 5.12, 5.14, 5.16, 6.10, D10.1.2, D10.1.3, D10.2.1, D10.2.2, D10.2.3, D10.2.4, D10.2.5, D10.2.6
**Human refs (from References field):** 10.11, 10.12, 10.13, 10.14, 10.36, 5.11, 5.16, 5.19, 6.12, D10.2.1, D10.2.2, D10.2.3, D10.2.4, D10.2.5, D10.2.6
**Jaccard:** 0.545 — AI adds ['10.6', '10.9', '5.12', '5.14', '6.10', 'D10.1.2', 'D10.1.3']; Human adds ['5.11', '5.19', '6.12']

## Proposition 10.67
**Statement:** A straight line commensurable in length with a bimedial straight line is itself also bimedial and the same in order.

**Step 1.** Let L be a bimedial straight line, and let M be commensurable in length with L. We choose the square-to-binomial route, since it brings the question directly under the preceding order-preservation theorem, 10.66. Fix a rational straight line r. Construct x and y so that r:L = L:x and r:M = M:y [6.12]. Then the rectangles contained by r,x and r,y equal the squares on L and M respectively [6.17]. Write these equalities as rx = L² and ry = M².

**Step 2.** Since L and M are commensurable in length, L²:M² is the ratio of a square number to a square number [10.9]. Consequently L² and M² are commensurable areas [10.6].

**Step 3.** Rectangles with the same height are to one another as their bases [6.1]. Therefore, using the equalities from Step 1,
L²:M² = rx:ry = x:y.
Since L² and M² are commensurable, x and y are commensurable in length [10.11].

**Step 4.** Suppose first that L is a first bimedial. Its square, applied to the rational straight line r, produces a second binomial as breadth; hence x is a second binomial [10.61]. Since y is commensurable in length with x, y is likewise a second binomial [10.66]. The side of the rectangle contained by the rational line r and the second binomial y is a first bimedial [10.55]. But that rectangle equals M², so its side is M. Thus M is a first bimedial, of the same order as L.

**Step 5.** Suppose instead that L is a second bimedial. Its square, applied to r, produces a third binomial as breadth; hence x is a third binomial [10.62]. By Step 3 and 10.66, y is likewise a third binomial. The side of the rectangle contained by r and y is therefore a second bimedial [10.56]. Since this rectangle equals M², that side is M. Thus M is a second bimedial, again of the same order as L. In either case, a straight line commensurable in length with a bimedial straight line is itself bimedial and the same in order.

**USED:** 10.11, 10.55, 10.56, 10.6, 10.61, 10.62, 10.66, 10.9, 6.1, 6.12, 6.17
**Human refs (from References field):** 10.11, 10.23, 10.37, 10.38, 5.11, 5.16, 5.19
**Jaccard:** 0.059 — AI adds ['10.55', '10.56', '10.6', '10.61', '10.62', '10.66', '10.9', '6.1', '6.12', '6.17']; Human adds ['10.23', '10.37', '10.38', '5.11', '5.16', '5.19']

## Proposition 10.68
**Statement:** A straight line commensurable with a major straight line is itself also major.

**Step 1.** Let A be a major straight line, and let B be commensurable in length with A. By 10.9, the squares A² and B² have the ratio of a square number to a square number. Therefore A² and B² are commensurable areas, by 10.6.

**Step 2.** Let r be the assigned rational straight line (D10.1.3). Construct fourth proportionals x and y such that r:A = A:x and r:B = B:y (6.12). Consequently, the rectangle contained by r and x equals A², and the rectangle contained by r and y equals B² (6.17).

**Step 3.** Since A is major, its square applied to the rational straight line r produces a fourth binomial as breadth (10.63). Thus x is a fourth binomial relative to r. Path choice: applying the square immediately reaches this fourth-binomial characterization, so we transfer its order rather than reconstruct the major's defining terms.

**Step 4.** Rectangles with the same altitude are to one another as their bases (6.1). Hence, using the equalities in Step 2, A²:B² = x:y. Since A² and B² are commensurable by Step 1, x and y are commensurable in length (10.11).

**Step 5.** A straight line commensurable in length with a binomial is itself binomial and of the same order (10.66). Since x is a fourth binomial, y is therefore also a fourth binomial relative to r.

**Step 6.** The side of an area contained by a rational straight line and a fourth binomial is major (10.57). Apply this to the rectangle contained by r and y. By Step 2 this rectangle equals B², so B is its square-side and is therefore major. Thus a straight line commensurable with a major straight line is itself also major.

**USED:** 10.11, 10.57, 10.6, 10.63, 10.66, 10.9, 6.1, 6.12, 6.17, D10.1.3
**Human refs (from References field):** 10.11, 10.23, 10.39, 5.11, 5.16, 5.18, 6.20
**Jaccard:** 0.062 — AI adds ['10.57', '10.6', '10.63', '10.66', '10.9', '6.1', '6.12', '6.17', 'D10.1.3']; Human adds ['10.23', '10.39', '5.11', '5.16', '5.18', '6.20']

## Proposition 10.69
**Statement:** A straight line commensurable with the side of a rational plus a medial area is itself also the side of a rational plus a medial area.

**Step 1.** Let x be the side of a rational plus a medial area, and let y be a straight line commensurable in length with x. Let r be the assigned rational straight line (D10.1.3). We shall prove that y is also the side of a rational plus a medial area.

**Step 2.** Construct fourth proportionals u and v such that r:x = x:u and r:y = y:v (6.12). Consequently, the rectangle contained by r and u equals the square on x, and the rectangle contained by r and v equals the square on y (6.17).

**Step 3.** The square on x, applied to the rational straight line r, therefore produces u as breadth. Since x is the side of a rational plus a medial area, u is a fifth binomial (10.64). This application route is chosen because 10.64 directly identifies the binomial order needed for the conclusion.

**Step 4.** Since x and y are commensurable in length, their squares have the ratio of a square number to a square number (10.9). Hence the squares on x and y are commensurable areas (10.6).

**Step 5.** The rectangles contained by r, u and by r, v have the same height r. Thus, by their equalities with the respective squares from Step 2,
(square on x):(square on y) = u:v (6.1).
Since these squares are commensurable, u and v are commensurable in length (10.11).

**Step 6.** A straight line commensurable in length with a binomial is itself a binomial of the same order; therefore v is a fifth binomial (10.66). The rectangle contained by the rational straight line r and the fifth binomial v consequently has as its square-side the side of a rational plus a medial area (10.58). But this rectangle equals the square on y by Step 2. Therefore y is itself the side of a rational plus a medial area, as required.

**USED:** 10.11, 10.58, 10.6, 10.64, 10.66, 10.9, 6.1, 6.12, 6.17, D10.1.3
**Human refs (from References field):** 10.40
**Jaccard:** 0.000 — AI adds ['10.11', '10.58', '10.6', '10.64', '10.66', '10.9', '6.1', '6.12', '6.17', 'D10.1.3']; Human adds ['10.40']

## Proposition 10.70
**Statement:** A straight line commensurable with the side of the sum of two medial areas is the side of the sum of two medial areas.

**Step 1.** Let a be the side of the sum of two medial areas, and let b be commensurable in length with a. By 10.9, the squares on a and b have the ratio of a square number to a square number; consequently, these squares are commensurable by 10.6.

**Step 2.** Let r be the assigned rational straight line (D10.1.3). Construct fourth proportionals x and y such that r:a = a:x and r:b = b:y (6.12). By 6.17, the rectangle contained by r and x equals the square on a, and the rectangle contained by r and y equals the square on b. Thus these rectangles apply the two squares to the same rational straight line r.

**Step 3.** Since a is the side of the sum of two medial areas, the breadth x is a sixth binomial by 10.65. Our path is through this sixth-binomial representation: it is supplied directly by 10.65 and avoids reconstructing the constituent summands.

**Step 4.** Rectangles having the same height are to one another as their bases (6.1). Taking r as their common height, we therefore have
(square on a):(square on b) = x:y.
The squares are commensurable by Step 1, so x and y are commensurable in length by 10.11.

**Step 5.** A straight line commensurable in length with a binomial is itself binomial and of the same order (10.66). Since x is a sixth binomial, y is therefore also a sixth binomial.

**Step 6.** The rectangle contained by the rational straight line r and the sixth binomial y has as its square-side the side of the sum of two medial areas (10.59). By Step 2, that rectangle equals the square on b, so b is precisely such a side. Hence a straight line commensurable with the side of the sum of two medial areas is itself the side of the sum of two medial areas.

**USED:** 10.11, 10.59, 10.6, 10.65, 10.66, 10.9, 6.1, 6.12, 6.17, D10.1.3
**Human refs (from References field):** 10.41
**Jaccard:** 0.000 — AI adds ['10.11', '10.59', '10.6', '10.65', '10.66', '10.9', '6.1', '6.12', '6.17', 'D10.1.3']; Human adds ['10.41']

## Proposition 10.71
**Statement:** If a rational and a medial area be added together, four irrational straight lines arise, namely a binomial or a first bimedial or a major or a side of a rational plus a medial area.

**Step 1.** Let R be a rational area, M a medial area, and r the assigned rational straight line. Construct squares a² = R, b² = M, and s² = R + M [2.14]. Construct fourth proportionals x and y such that r:a = a:x and r:b = b:y [6.12]. Then the rectangles rx and ry equal R and M respectively [6.17], and therefore r(x + y) = R + M = s² [2.1]. Here products denote rectangular areas. The direct route is to classify the breadth x + y and then use the earlier area-to-side propositions.

**Step 2.** Since the rational area R is applied to the rational straight line r, its breadth x is rational and commensurable in length with r [10.20]. Since the medial area M is applied to r, its breadth y is rational but incommensurable in length with r [10.22]. The squares on x and y are each commensurable with the square on r, and hence with one another [D10.1.2, D10.1.3, 10.12]. But x and y cannot be commensurable in length: otherwise, since x is commensurable in length with r, y would also be commensurable in length with r [10.12]. Thus x and y are rational straight lines commensurable in square only, so x + y is a binomial [10.36].

**Step 3.** In particular, x and y are unequal. Let g be the greater and h the lesser, and construct d such that d² = g² − h² [2.14]. Either d is commensurable in length with g or it is incommensurable with g [D10.1.1]. Together with the alternatives x > y and y > x, this gives the following four exhaustive cases.

**Step 4.** Suppose x > y and d is commensurable in length with x. The greater term x is commensurable in length with r, and x² exceeds y² by the square on a straight line commensurable in length with x. Thus x + y is a first binomial [D10.2.1]. Since s² is the rectangle contained by r and this first binomial, s is the irrational straight line called binomial [10.54].

**Step 5.** Suppose y > x and d is commensurable in length with y. The lesser term x is commensurable in length with r, and y² exceeds x² by the square on a straight line commensurable in length with y. Thus x + y is a second binomial [D10.2.2]. Consequently, the side s of the rectangle contained by r and x + y is the irrational straight line called a first bimedial [10.55].

**Step 6.** Suppose x > y and d is incommensurable in length with x. The greater term x is commensurable in length with r, but x² exceeds y² by the square on a straight line incommensurable in length with x. Thus x + y is a fourth binomial [D10.2.4]. Consequently, s is the irrational straight line called major [10.57].

**Step 7.** Suppose y > x and d is incommensurable in length with y. The lesser term x is commensurable in length with r, but y² exceeds x² by the square on a straight line incommensurable in length with y. Thus x + y is a fifth binomial [D10.2.5]. Consequently, s is the irrational straight line called the side of a rational plus a medial area [10.58].

**Step 8.** Each of these four alternatives can actually occur. First, second, fourth, and fifth binomials can be constructed [10.48, 10.49, 10.51, 10.52]. Relative to the assigned rational straight line r, each has one rational term commensurable in length with r and another rational term incommensurable in length with r [10.36, D10.2.1, D10.2.2, D10.2.4, D10.2.5]. The rectangle contained by r and the former term is rational [10.19]; the rectangle contained by r and the latter is medial [10.21]. Their sum is the rectangle contained by r and the whole binomial [2.1], whose side has the corresponding type established in Steps 4–7. Therefore adding a rational and a medial area gives exactly the four asserted possibilities for the side of the equal square: a binomial, a first bimedial, a major, or a side of a rational plus a medial area.

**USED:** 10.12, 10.19, 10.20, 10.21, 10.22, 10.36, 10.48, 10.49, 10.51, 10.52, 10.54, 10.55, 10.57, 10.58, 2.1, 2.14, 6.12, 6.17, D10.1.1, D10.1.2, D10.1.3, D10.2.1, D10.2.2, D10.2.4, D10.2.5
**Human refs (from References field):** 10.11, 10.20, 10.22, 10.36, 10.54, 10.55, 10.57, 10.58, 6.1, D10.2.1, D10.2.2, D10.2.4, D10.2.5
**Jaccard:** 0.407 — AI adds ['10.12', '10.19', '10.21', '10.48', '10.49', '10.51', '10.52', '2.1', '2.14', '6.12', '6.17', 'D10.1.1', 'D10.1.2', 'D10.1.3']; Human adds ['10.11', '6.1']

## Proposition 10.72
**Statement:** If two medial areas incommensurable with one another be added together, the remaining two irrational straight lines arise, namely either a second bimedial or a side of the sum of two medial areas.

**Step 1.** Let M and N be the given medial areas, incommensurable with one another, and let r be the assigned rational straight line [D10.1.3]. Apply M and N to r, obtaining rectangular breadths a and b, respectively. Thus M = ra and N = rb, where products denote rectangular areas. By 10.22, both a and b are rational, and each is incommensurable in length with r.

**Step 2.** The rectangles ra and rb have the same height r, so M : N = a : b [6.1]. Since M and N are incommensurable, a and b are incommensurable in length [10.11].

**Step 3.** Since a and b are rational, their squares are each commensurable with the square on r [D10.1.3, D10.1.2]. Their squares are therefore commensurable with one another [10.12]. Consequently a and b are rational straight lines commensurable in square only, and their sum a + b is a binomial [10.36]. Neither term is commensurable in length with r, by Step 1.

**Step 4.** The rectangle contained by r and a + b equals the sum of the rectangles ra and rb, and hence equals M + N [2.1]. Construct a square equal to this area, and let its side be s [2.14]. The direct path is therefore to classify the binomial breadth a + b and use the corresponding area-to-side proposition, since the given sum is already expressed as a rectangle with rational side r.

**Step 5.** Since a and b are incommensurable in length, they are unequal; name them so that a > b. Construct a straight line d whose square equals the excess of the square on a over the square on b [2.14]. Thus a² = b² + d². Either d is commensurable in length with a, or it is incommensurable in length with a [D10.1.1].

**Step 6.** Suppose first that d is commensurable in length with a. The square on the greater term a therefore exceeds the square on the lesser term b by the square on a straight line commensurable in length with a. Since neither term is commensurable in length with r, the binomial a + b is a third binomial relative to r [D10.2.3]. The side s of the area contained by r and this third binomial is consequently the irrational straight line called a second bimedial [10.56].

**Step 7.** Suppose instead that d is incommensurable in length with a. Since neither a nor b is commensurable in length with r, the binomial a + b is now a sixth binomial relative to r [D10.2.6]. The side s of the area contained by r and this sixth binomial is consequently the irrational straight line called the side of the sum of two medial areas [10.59]. These cases exhaust the alternatives in Step 5. Therefore the side of the sum of the two given incommensurable medial areas is either a second bimedial or a side of the sum of two medial areas, as required.

**USED:** 10.11, 10.12, 10.22, 10.36, 10.56, 10.59, 2.1, 2.14, 6.1, D10.1.1, D10.1.2, D10.1.3, D10.2.3, D10.2.6
**Human refs (from References field):** 10.11, 10.22, 10.36, 10.56, 10.59, 6.1, D10.2.3, D10.2.6
**Jaccard:** 0.571 — AI adds ['10.12', '2.1', '2.14', 'D10.1.1', 'D10.1.2', 'D10.1.3']

## Proposition 10.73
**Statement:** If from a rational straight line there be subtracted a rational straight line commensurable with the whole in square only, the remainder is irrational; and let it be called   an apotome.

**Step 1.** Let AB be the rational whole, and let AC be the rational straight line subtracted, with C between A and B. Thus CB is the remainder. By hypothesis, AB and AC are commensurable in square but incommensurable in length (D10.1.1, D10.1.2). Let R be the assigned rational straight line relative to which rationality is understood (D10.1.3).

**Step 2.** The parts AC and CB are incommensurable in length. For if they were commensurable in length, their sum AB would be commensurable in length with AC by 10.15, contrary to the hypothesis. Here we choose the earlier commensurable-sum criterion because it applies directly to the decomposition AB = AC + CB.

**Step 3.** Suppose, for a contradiction, that CB is rational. Since AC is also rational, the squares on AC and CB are each commensurable with the square on R (D10.1.3). Therefore these two squares are commensurable with one another by 10.12. Hence AC and CB are commensurable in square (D10.1.2), and, by Step 2, in square only.

**Step 4.** We now use the earlier addition theorem 10.36: the sum of the rational straight lines AC and CB, commensurable in square only, is irrational. But their sum is AB, which is rational by hypothesis. This contradiction proves that CB is irrational (D10.1.3). Let this remainder be called an **apotome**.

**USED:** 10.12, 10.15, 10.36, D10.1.1, D10.1.2, D10.1.3
**Human refs (from References field):** 10.11, 10.13, 10.15, 10.16, 10.6, 2.7, D10.1.4
**Jaccard:** 0.083 — AI adds ['10.12', '10.36', 'D10.1.1', 'D10.1.2', 'D10.1.3']; Human adds ['10.11', '10.13', '10.16', '10.6', '2.7', 'D10.1.4']

## Proposition 10.74
**Statement:** If from a medial straight line there be subtracted a medial straight line which is commensurable with the whole in square only, and which contains with the whole a rational rectangle, the remainder is irrational. And let it be called a first apotome of a medial straight line.

**Step 1.** Let AB be the given medial straight line, and let the medial straight line BC be subtracted from it, leaving AC. Thus AB and BC are commensurable in square only, and their rectangle is rational. Let U be the square on the assigned rational straight line, and write X = AB², Y = BC², Z = AC², and R for the rectangle contained by AB and BC. Then X and Y are commensurable (D10.1.2). Since AB is medial, X is irrational and therefore incommensurable with U; meanwhile, R is commensurable with U because it is rational (10.21; D10.1.4).

**Step 2.** Put S = X + Y. Since X and Y are commensurable, S is commensurable with X (10.15). But X is incommensurable with U, so S is also incommensurable with U (10.13).

**Step 3.** Put T = 2R. The area R measures both R and T, so T is commensurable with R (D10.1.1). Since R is commensurable with U, T is commensurable with U (10.12).

**Step 4.** We choose the direct area route: the square-of-a-difference identity applies immediately to the given subtraction, without requiring an auxiliary construction. By 2.7, the squares on AB and BC together equal twice their rectangle together with the square on AC. Hence S = T + Z.

**Step 5.** Since T is commensurable with U while S is incommensurable with U, S is incommensurable with T (10.13). Applying the converse assertion of 10.16 to S = T + Z, we conclude that Z and T are incommensurable. Since T is commensurable with U, it follows that Z is incommensurable with U (10.13).

**Step 6.** Thus the square on AC is irrational, and consequently AC itself is irrational (D10.1.4). Therefore the remainder is irrational; let it be called a first apotome of a medial straight line.

**USED:** 10.12, 10.13, 10.15, 10.16, 10.21, 2.7, D10.1.1, D10.1.2, D10.1.4
**Human refs (from References field):** 10.16, 2.7, D10.1.4
**Jaccard:** 0.333 — AI adds ['10.12', '10.13', '10.15', '10.21', 'D10.1.1', 'D10.1.2']

## Proposition 10.75
**Statement:** If from a medial straight line there be subtracted a medial straight line which is commensurable with the whole in square only, and which contains with the whole a medial rectangle, the remainder is irrational; and let it be called a second apotome of a medial straight line.

**Step 1.** Let a be the whole medial straight line, b the medial straight line subtracted, and c the remainder, so that a=b+c and c is positive. Denote their squares by a², b², and c², and the rectangle contained by a and b by R. By hypothesis, R is medial and a² is commensurable with b² (D10.1.2). We use the direct area-difference route: express c² as the excess of one medial area over another, then apply 10.26.

**Step 2.** Put S=a²+b². Since a² and b² are commensurable, S is commensurable with a² (10.15). Construct a square equal to S, and let its side be s (2.14). Thus s is commensurable in square with the medial straight line a (D10.1.2), and is therefore medial (10.23). Consequently, S is a medial area.

**Step 3.** Construct squares equal to R and 2R, with sides r and t respectively (2.14). Since R is medial, r is medial. Moreover, R itself measures both R and 2R, so these areas are commensurable (D10.1.1). Hence t and r are commensurable in square (D10.1.2), and t is medial by 10.23. Therefore 2R is also a medial area.

**Step 4.** Since a is cut into the segments b and c, the square on a together with the square on b equals twice the rectangle contained by a and b together with the square on c (2.7). Thus S=2R+c². In particular, S exceeds 2R by the positive area c² (CN5).

**Step 5.** A medial area does not exceed a medial area by a rational area (10.26). Since S and 2R are medial, their difference c² cannot be rational. Therefore its side c is irrational (D10.1.4). Hence the remainder is irrational; as stipulated, let it be called a second apotome of a medial straight line.

**USED:** 10.15, 10.23, 10.26, 2.14, 2.7, CN5, D10.1.1, D10.1.2, D10.1.4
**Human refs (from References field):** 10.11, 10.13, 10.15, 10.20, 10.22, 10.23, 10.28, 10.6, 10.73, 2.7, 6.1
**Jaccard:** 0.176 — AI adds ['10.26', '2.14', 'CN5', 'D10.1.1', 'D10.1.2', 'D10.1.4']; Human adds ['10.11', '10.13', '10.20', '10.22', '10.28', '10.6', '10.73', '6.1']

## Proposition 10.76
**Statement:** If from a straight line there be subtracted a straight line which is incommensurable in square with the whole and which with the whole makes the squares on them added together rational, but the rectangle contained by them medial, the remainder is irrational; and let it be called minor.

**Step 1.** Let BC be subtracted from AB, leaving AC, under the stated hypotheses. Write S for the sum of the squares on AB and BC, M for the rectangle contained by AB and BC, and T for the square on AC. Let U be the square on the assigned rational straight line. Since S is rational by hypothesis, S is commensurable with U. [D10.1.4]

**Step 2.** By the square-of-a-difference identity,
S = 2M + T.
Thus the question reduces directly to the commensurability of these areas, without any auxiliary construction. [2.7]

**Step 3.** Since M is medial, it is irrational and therefore incommensurable with U. [10.21; D10.1.4] Moreover, M and 2M are commensurable, since M measures both. [D10.1.1] Consequently 2M is also incommensurable with U. [10.13]

**Step 4.** Since S is commensurable with U, whereas 2M is incommensurable with U, S is incommensurable with 2M. [10.13] We now use 10.16, since the known incommensurability is between a whole and one of its parts: from S = 2M + T, its converse gives that 2M and T are incommensurable; its forward implication then gives that S and T are incommensurable. [10.16]

**Step 5.** But S and U are commensurable. Therefore, since T is incommensurable with S, it is also incommensurable with U. [10.13] The square T on AC is consequently irrational, and so its side AC is irrational. [D10.1.4] Hence the remainder is irrational; let it be called **minor**.

**USED:** 10.13, 10.16, 10.21, 2.7, D10.1.1, D10.1.4
**Human refs (from References field):** 10.16, 10.33, 2.7
**Jaccard:** 0.286 — AI adds ['10.13', '10.21', 'D10.1.1', 'D10.1.4']; Human adds ['10.33']

## Proposition 10.77
**Statement:** If from a straight line there be subtracted a straight line which is incommensurable in square with the whole, and which with the whole makes the sum of the squares on them medial, but twice the rectangle contained by them rational, the remainder is irrational: and let it be called that which produces with a rational area a medial whole.

**Step 1.** Let AB be the whole straight line, BC the subtracted part, and AC the remainder, with C between A and B. Write M for the sum of the squares on AB and BC, and R for twice the rectangle contained by AB and BC. By hypothesis, AB and BC are incommensurable in square, M is medial, and R is rational. Let U be the square on the assigned rational straight line. [Hypotheses; D10.1.4]

**Step 2.** By 2.7, the squares on AB and BC together equal twice the rectangle contained by AB and BC together with the square on AC. Thus
M = R + AC².
We choose 2.7 directly because it identifies the square on the remainder without auxiliary constructions. [2.7]

**Step 3.** A medial area is irrational, so M is incommensurable with U. Since R is rational, R is commensurable with U. Therefore M is incommensurable with R: for magnitudes commensurable with one another are incommensurable with the same magnitude whenever either is. [10.21; D10.1.4; 10.13]

**Step 4.** Since R and the square on AC together make M, and M is incommensurable with R, the converse assertion of 10.16 shows that the square on AC is incommensurable with R. [2.7; 10.16]

**Step 5.** But R is commensurable with U. Hence the square on AC is also incommensurable with U, and consequently AC is irrational. Moreover, its square together with the rational area R makes the medial whole M. Therefore the remainder AC is irrational, and let it be called **that which produces with a rational area a medial whole**. [10.13; D10.1.4; Step 2]

**USED:** 10.13, 10.16, 10.21, 2.7, D10.1.4
**Human refs (from References field):** 10.16, 10.34, 2.7
**Jaccard:** 0.333 — AI adds ['10.13', '10.21', 'D10.1.4']; Human adds ['10.34']

## Proposition 10.78
**Statement:** If from a straight line there be subtracted a straight line which is incommensurable in square with the whole and which with the whole makes the sum of the squares on them medial, twice the rectangle contained by them medial, and further the squares on them incommensurable with twice the rectangle contained by them, the remainder is irrational; and let it be called that which produces with a medial area a medial whole.

**Step 1.** Let AB be the whole straight line, BC the subtracted straight line, and AC the remainder, with C between A and B, satisfying the stated hypotheses. Denote the sum of the squares on AB and BC by S, and twice the rectangle contained by AB and BC by T. By hypothesis, S and T are medial areas. By 2.7,
S = T + (the square on AC).
Consequently, S exceeds T by the square on AC, and S > T (CN5).

**Step 2.** We take the direct area-difference route: 10.26 applies immediately to the two medial areas S and T. By that proposition, a medial area cannot exceed a medial area by a rational area. Therefore their difference, which is the square on AC by Step 1, is not rational (10.26).

**Step 3.** The square on AC is therefore irrational, and its side AC is irrational (D10.1.4). Moreover, Step 1 shows that the square on AC, together with the medial area T, makes the medial whole S (2.7). Thus the remainder is irrational; let it be called **that which produces with a medial area a medial whole**.

**USED:** 10.26, 2.7, CN5, D10.1.4
**Human refs (from References field):** 10.11, 10.20, 10.22, 10.35, 10.73, 2.7, 6.1
**Jaccard:** 0.100 — AI adds ['10.26', 'CN5', 'D10.1.4']; Human adds ['10.11', '10.20', '10.22', '10.35', '10.73', '6.1']

## Proposition 10.79
**Statement:** To an apotome only one rational straight line can be annexed which is commensurable with the whole in square only.

**Step 1.** Let x be the given apotome. By 10.73, there are rational straight lines a > b, commensurable in square only, such that x = a − b. Thus b is an admissible annex. Write t² for the square on a straight line t, and uv for the rectangle contained by u and v. Path choice: compare the medial rectangles arising from two proposed annexes; the square identities will make their difference rational, directly invoking 10.26.

**Step 2.** Suppose that a different rational straight line d can also be annexed, and put c = x + d. By hypothesis, c and d are commensurable in square only. Let R be the square on the assigned rational straight line. Since d is rational, d² is commensurable with R; since c² is commensurable with d², it is also commensurable with R. Consequently c is rational. We therefore have two representations x = a − b = c − d, each formed from rational straight lines commensurable in square only. [D10.1.2, D10.1.3, 10.12]

**Step 3.** Interchanging the two representations if necessary, suppose b > d, and write b = d + h, where h > 0. Since a = x + b and c = x + d, we have a = c + h. Distributing the rectangles gives ab = cb + hb = cd + ch + hb, so ab > cd. Let E = ab − cd, a positive area. Moreover, ab and cd are both medial areas, because their respective sides are rational and commensurable in square only. [CN2, 2.1, CN5, 10.21]

**Step 4.** Put U = a² + b² and V = c² + d². Each of the four squares is commensurable with R. Hence a² and b² are commensurable with one another, and their sum U is commensurable with each and therefore with R. The same reasoning applies to V. Thus U and V are rational areas and are commensurable with one another. [D10.1.3, 10.12, 10.15, D10.1.4]

**Step 5.** Applying 2.7 to the subtractions a − b = x and c − d = x gives
U = x² + 2ab,
V = x² + 2cd.
Since ab = cd + E, substitution and subtraction of the common area x² + 2cd yield U = V + 2E. [2.7, CN2, CN3]

**Step 6.** Because U and V are commensurable and U = V + 2E, the converse part of 10.15 shows that V and 2E are commensurable. Since V is commensurable with R, so is 2E. Also E measures 2E twice, so E and 2E are commensurable. It follows that E is commensurable with R and is therefore rational. [10.15, 10.12, D10.1.1, D10.1.4]

**Step 7.** Thus the medial area ab exceeds the medial area cd by the positive rational area E. This contradicts 10.26. Therefore no annex different from b can have the required properties. Since b already provides such an annex, to an apotome only one rational straight line can be annexed which is commensurable with the whole in square only. [10.26, 10.73]

**USED:** 10.12, 10.15, 10.21, 10.26, 10.73, 2.1, 2.7, CN2, CN3, CN5, D10.1.1, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 10.21, 10.26, 10.73, 2.7
**Jaccard:** 0.286 — AI adds ['10.12', '10.15', '2.1', 'CN2', 'CN3', 'CN5', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.1.4']

## Proposition 10.80
**Statement:** To a first apotome of a medial straight line only one medial straight line can be annexed which is commensurable with the whole in square only and which contains with the whole a rational rectangle.

**Step 1.** Let h be a first apotome of a medial straight line. At least one annex of the required kind exists by the defining description in 10.74. Suppose that there are two distinct medial annexes b and d, and write a = h + b and c = h + d for the corresponding wholes. Thus a and b are commensurable in square only, as are c and d, while the rectangles ab and cd are rational. Interchanging the two annexes if necessary, take d > b; then c > a (CN2, CN5). Here xy denotes the rectangle contained by x and y, and x² the square on x.

**Step 2.** By 6.12, construct straight lines e and f such that b:a = a:e and d:c = c:f. Then be = a² and df = c² (6.17). Since the respective wholes and annexes are commensurable in square, b² is commensurable with be, and d² with df (D10.1.2).

**Step 3.** Rectangles of equal height are proportional to their bases, so b²:be = b:e and d²:df = d:f (6.1). Therefore b is commensurable in length with e, and d with f (10.11). Hence b + e is commensurable in length with b, and d + f with d (10.15). Since b and d are medial, b + e and d + f are also medial (10.23).

**Step 4.** Consequently the rectangles b(b + e) and d(d + f) are medial: each is contained by medial straight lines commensurable in length (10.24). But, by 2.1 and the equalities in Step 2,
M := b(b + e) = b² + a²,
N := d(d + f) = d² + c².
Thus both M and N are medial areas.

**Step 5.** Apply 2.7 directly to each whole and its annex; this is the direct route because it expresses each medial area as the same square plus twice a rational rectangle. Since a − b = c − d = h, it gives
M = h² + 2ab,
N = h² + 2cd.
Moreover, c > a and d > b, so the squares making up N are respectively greater than those making up M; hence N > M (CN5, CN2). Subtracting the displayed equalities therefore gives the positive excess
N − M = 2cd − 2ab (CN3).

**Step 6.** Let Q be the square on the assigned rational straight line. Since ab and cd are rational areas, each is commensurable with Q, and so is each of their doubles (D10.1.1, D10.1.4). Thus 2ab and 2cd are commensurable with one another (10.12). From 2cd = 2ab + (N − M), it follows that N − M is commensurable with 2ab (10.15), and therefore with Q (10.12). Hence N − M is a rational area (D10.1.4).

**Step 7.** We have obtained a medial area N exceeding a medial area M by a rational area, contrary to 10.26. Thus two distinct annexes satisfying the stated conditions cannot exist. Since an annex of the required kind exists by 10.74, exactly one medial straight line can be annexed which is commensurable with the whole in square only and contains with it a rational rectangle.

**USED:** 10.11, 10.12, 10.15, 10.23, 10.24, 10.26, 10.74, 2.1, 2.7, 6.1, 6.12, 6.17, CN2, CN3, CN5, D10.1.1, D10.1.2, D10.1.4
**Human refs (from References field):** 10.15, 10.23, 10.26, 10.74, 2.7
**Jaccard:** 0.278 — AI adds ['10.11', '10.12', '10.24', '2.1', '6.1', '6.12', '6.17', 'CN2', 'CN3', 'CN5', 'D10.1.1', 'D10.1.2', 'D10.1.4']

## Proposition 10.81
**Statement:** To a second apotome of a medial straight line only one medial straight line can be annexed which is commensurable with the whole in square only and which contains with the whole a medial rectangle.

**Step 1.** Let a be a second apotome of a medial straight line. By 10.75, there is an annex b₁ such that, putting c₁ = a + b₁, the lines c₁ and b₁ are medial and commensurable in square only, and c₁b₁ is a medial rectangle. Suppose b₂ is another annex having the required properties, and put c₂ = a + b₂. Thus, for i = 1, 2, bᵢ is medial, cᵢ and bᵢ are commensurable in square only, and cᵢbᵢ is medial. We choose the direct route through 10.79: applying a² to a rational line will produce an ordinary apotome with two proposed rational annexes.

**Step 2.** Let r be the assigned rational straight line (D10.1.3). Products below denote rectangular areas. By constructing fourth proportionals and using 6.16, obtain positive breadths t, pᵢ, qᵢ, and wᵢ satisfying
rt = a²,   rpᵢ = bᵢ²,   rqᵢ = cᵢ²,   rwᵢ = cᵢbᵢ
(6.12, 6.16). Put Xᵢ = pᵢ + qᵢ and Yᵢ = 2wᵢ.

**Step 3.** A medial area is equal to the square on a medial straight line, according to the terminology introduced in 10.21. Consequently, applying 10.22 to bᵢ² and to the medial rectangle cᵢbᵢ shows that pᵢ and wᵢ are rational. Since bᵢ and cᵢ are commensurable in square, their squares are commensurable (D10.1.2). Rectangles on the same base have the ratio of their breadths; hence pᵢ and qᵢ are commensurable in length (6.1, 10.11). Therefore Xᵢ is commensurable in length with pᵢ (10.15). Also Yᵢ is commensurable in length with wᵢ, since wᵢ measures its double (D10.1.1).

**Step 4.** By 10.9 and 10.6, the length-commensurabilities just obtained imply that Xᵢ² is commensurable with pᵢ² and Yᵢ² with wᵢ². Since pᵢ and wᵢ are rational, their squares are commensurable with r² (D10.1.3). Thus Xᵢ² and Yᵢ² are each commensurable with r², and also with one another (10.12). Accordingly, Xᵢ and Yᵢ are rational and commensurable in square (D10.1.3, D10.1.2).

**Step 5.** By the ratios of rectangles on a common base,
pᵢ : wᵢ = bᵢ² : cᵢbᵢ = bᵢ : cᵢ
(6.1). But bᵢ and cᵢ are incommensurable in length, so pᵢ and wᵢ are incommensurable in length (10.11). Since Xᵢ is commensurable with pᵢ and Yᵢ with wᵢ, two applications of 10.13 show that Xᵢ and Yᵢ are incommensurable in length. Together with Step 4, this proves that they are commensurable in square only.

**Step 6.** Since cᵢ = a + bᵢ, proposition 2.7 gives
cᵢ² + bᵢ² = 2cᵢbᵢ + a².
Expressing these areas as rectangles on r gives rXᵢ = r(Yᵢ + t), by 2.1. Hence Xᵢ = Yᵢ + t, by 6.1. Therefore t = Xᵢ − Yᵢ. By Steps 4–5 and 10.73, t is an ordinary apotome, and each Yᵢ is a rational annex commensurable with its whole Xᵢ in square only.

**Step 7.** Proposition 10.79 now applies directly: an ordinary apotome has only one such rational annex. Thus Y₁ = Y₂. The rectangles on r with these equal breadths coincide and are equal (CN4). Since rYᵢ = 2cᵢbᵢ by 2.1, it follows that
2c₁b₁ = 2c₂b₂.

**Step 8.** If b₁ and b₂ were unequal, interchange their labels if necessary so that b₁ > b₂. Then c₁ = a + b₁ > a + b₂ = c₂. The rectangle c₁b₁ therefore contains a rectangle equal to c₂b₂ as a proper part, so c₁b₁ > c₂b₂; doubling preserves this strict inequality (CN5, 2.1). This contradicts Step 7. Hence b₁ = b₂. Since an annex exists by Step 1, exactly one medial straight line can be annexed with the stated properties. ∎

**USED:** 10.11, 10.12, 10.13, 10.15, 10.21, 10.22, 10.6, 10.73, 10.75, 10.79, 10.9, 2.1, 2.7, 6.1, 6.12, 6.16, CN4, CN5, D10.1.1, D10.1.2, D10.1.3
**Human refs (from References field):** 10.11, 10.13, 10.15, 10.22, 10.23, 10.6, 10.73, 10.75, 10.79, 2.7, 6.1
**Jaccard:** 0.455 — AI adds ['10.12', '10.21', '10.9', '2.1', '6.12', '6.16', 'CN4', 'CN5', 'D10.1.1', 'D10.1.2', 'D10.1.3']; Human adds ['10.23']

## Proposition 10.82
**Statement:** To a minor straight line only one straight line can be annexed which is incommensurable in square with the whole and which makes, with the whole, the sum of the squares on them rational but twice the rectangle contained by them medial.

**Step 1.** Let x be the given minor straight line. By the defining characterization in 10.76, there are straight lines a>b such that a=x+b, the lines a and b are incommensurable in square, a²+b² is rational, and ab is medial. Here t² denotes the square on t, and st denotes the rectangle contained by s and t. [10.76]

**Step 2.** The area 2ab is also medial. Indeed, let m be the medial straight line whose square equals the medial area ab. [10.21] The lines m and 2m are commensurable in length, since m measures both; therefore 2m is medial. [D10.1.1, 10.23] Consequently, the rectangle contained by m and 2m is medial. [10.24] This rectangle equals twice m², and hence equals 2ab. [2.1, CN2, CN1] Thus b is an annex satisfying all the required conditions.

**Step 3.** Suppose that two distinct annexes satisfy these conditions. Relabel their representations as a=x+b and c=x+d, with d>b. Writing d=b+h, where h>0, gives c=a+h. [CN2] Set
R=a²+b², S=c²+d², M=2ab, and N=2cd.
By hypothesis, R and S are rational, while M and N are medial. Since c>a and d>b, expansion of the squares by 2.4 shows that S contains R together with positive additional areas. Hence S>R. [2.4, CN5] Let Δ=S−R.

**Step 4.** The positive area Δ is rational. To see this explicitly, let Q be the square on the assigned rational straight line. Both R and S are commensurable with Q, and hence with one another. [D10.1.4, 10.12] Since S=R+Δ and S is commensurable with R, the converse part of 10.15 makes Δ commensurable with R. [10.15] Therefore Δ is commensurable with Q, and so is rational. [10.12, D10.1.4]

**Step 5.** Applying 2.7 to a=x+b and c=x+d gives
R=x²+M and S=x²+N. [2.7]
Substitute these equalities into S=R+Δ and subtract the common area x². The result is
N=M+Δ. [CN2, CN3]
This is the direct area-comparison route: 2.7 identifies the difference of the rational square-sums with the difference of the medial double rectangles, bringing precisely 10.26 into application.

**Step 6.** Thus the medial area N exceeds the medial area M by the positive rational area Δ. This is impossible, since a medial area does not exceed a medial area by a rational area. [10.26] Therefore two distinct qualifying annexes cannot exist. Together with the existence established in Steps 1–2, this proves that to the given minor straight line exactly one straight line can be annexed satisfying all the stated conditions.

**USED:** 10.12, 10.15, 10.21, 10.23, 10.24, 10.26, 10.76, 2.1, 2.4, 2.7, CN1, CN2, CN3, CN5, D10.1.1, D10.1.4
**Human refs (from References field):** 10.26, 10.76
**Jaccard:** 0.125 — AI adds ['10.12', '10.15', '10.21', '10.23', '10.24', '2.1', '2.4', '2.7', 'CN1', 'CN2', 'CN3', 'CN5', 'D10.1.1', 'D10.1.4']

## Proposition 10.83
**Statement:** To a straight line which produces with a rational area a medial whole only one straight line can be annexed which is incommensurable in square with the whole straight line and which with the whole straight line makes the sum of the squares on them medial, but twice the rectangle contained by them rational.

**Step 1.** Let a be the given straight line. By the denomination introduced in 10.77, there is an annex b such that the whole x = a + b is incommensurable in square with b, while M = x² + b² is medial and R = 2xb is rational. Here u² denotes the square on u, and uv the rectangle contained by u and v. It remains to prove uniqueness. [10.77]

**Step 2.** Suppose that a distinct annex c also satisfies the required conditions. Put y = a + c, N = y² + c², and T = 2yc; thus N is medial and T rational. Interchanging the two annexes if necessary, suppose c > b. Then y > x. The square on a straight line exceeds the square on any proper part, by the square-of-a-sum identity; consequently y² > x² and c² > b², and therefore N > M. [2.4, CN2, CN5]

**Step 3.** Applying 2.7 to the whole x cut into a and b, and to the whole y cut into a and c, gives
M = a² + R,
N = a² + T.
Hence T > R and N − M = T − R. We use the direct medial-area comparison of 10.26, since these identities make the difference of the two medial areas equal to the difference of two rational areas. [2.7, CN3]

**Step 4.** Let Q be the square on the assigned rational straight line. Since R and T are rational, both are commensurable with Q, and thus with one another. Since T = R + (T − R) is commensurable with R, the converse assertion of 10.15 shows that T − R is commensurable with R. Therefore T − R is commensurable with Q and is a rational area. [D10.1.4, 10.12, 10.15]

**Step 5.** Thus the medial area N exceeds the medial area M by the positive rational area T − R. This contradicts 10.26. No distinct second annex can therefore exist. Together with the annex supplied by the given denomination, this proves that exactly one straight line can be annexed which is incommensurable in square with the whole and makes the sum of their squares medial but twice their rectangle rational. [10.26, 10.77]

**USED:** 10.12, 10.15, 10.26, 10.77, 2.4, 2.7, CN2, CN3, CN5, D10.1.4
**Human refs (from References field):** 10.26, 10.77
**Jaccard:** 0.200 — AI adds ['10.12', '10.15', '2.4', '2.7', 'CN2', 'CN3', 'CN5', 'D10.1.4']

## Proposition 10.84
**Statement:** To a straight line which produces with a medial area a medial whole only one straight line can be annexed which is incommensurable in square with the whole straight line and which with the whole straight line makes the sum of the squares on them medial and twice the rectangle contained by them both medial and also incommensurable with the sum of the squares on them.

**Step 1.** Let x be the given straight line. By its characterization in 10.78, an annex v exists such that, writing u = x + v, the lines u and v are incommensurable in square, while S = u² + v² and T = 2uv are medial areas incommensurable with one another. Suppose another annex v′ has the required properties, and put u′ = x + v′, S′ = u′² + v′², and T′ = 2u′v′. Thus S′ and T′ are also medial and incommensurable with one another. Here products denote rectangular areas and squares denote squares on straight lines. [10.78]

**Step 2.** Applying 2.7 to u = x + v and to u′ = x + v′ gives
S = x² + T and S′ = x² + T′.
Consequently S > T and S′ > T′. [2.7, CN5]

**Step 3.** Path choice: apply the medial areas to a rational straight line. Their breadths will be rational by 10.22, making the earlier uniqueness theorem for an apotome, 10.79, directly applicable. Let r be the assigned rational straight line, and apply x², S, T, S′, and T′ to r as rectangles, with respective breadths h, a, b, a′, and b′. Thus
rh = x², ra = S, rb = T, ra′ = S′, and rb′ = T′.
These applications can be made by applying the constituent triangles successively and adding their breadths. Since S, T, S′, and T′ are medial, a, b, a′, and b′ are rational straight lines. [1.44, 2.1, 10.22]

**Step 4.** The identities in Step 2 now give
ra = rh + rb = r(h + b), and ra′ = rh + rb′ = r(h + b′).
Rectangles on the same base have equal areas only when their breadths are equal: otherwise the rectangle with greater breadth contains the other together with a positive remainder. Hence a = h + b and a′ = h + b′. In particular, h = a − b = a′ − b′. [2.1, CN5]

**Step 5.** Since a and b are rational, their squares are each commensurable with the square on r. Therefore their squares are commensurable with one another, so a and b are commensurable in square. The same argument applies to a′ and b′. [D10.1.3, 10.12, D10.1.2]

**Step 6.** Rectangles of equal height are proportional to their bases; consequently
S : T = a : b and S′ : T′ = a′ : b′.
Since S and T are incommensurable, a and b are incommensurable in length; likewise a′ and b′ are incommensurable in length. Together with Step 5, this shows that each pair consists of rational straight lines commensurable in square only. [6.1, 10.11]

**Step 7.** Since h = a − b, where a and b are rational and commensurable in square only, h is an apotome. Both b and b′ are rational annexes to this same apotome, each commensurable with its corresponding whole, a or a′, in square only. The uniqueness of such an annex therefore gives b = b′. [10.73, 10.79]

**Step 8.** The rectangles rb and rb′ consequently coincide, so T = T′, that is, 2uv = 2u′v′. If v′ > v, then u′ = x + v′ > x + v = u. Splitting the rectangle u′v′ along lengths u and v exhibits uv together with positive additional rectangles; hence 2u′v′ > 2uv, a contradiction. The supposition v > v′ gives the same contradiction with the pairs interchanged. Thus v = v′. Since an annex exists by Step 1, exactly one straight line with all the stated properties can be annexed to x. [CN4, 2.1, CN5]

**USED:** 1.44, 10.11, 10.12, 10.22, 10.73, 10.78, 10.79, 2.1, 2.7, 6.1, CN4, CN5, D10.1.2, D10.1.3
**Human refs (from References field):** 10.11, 10.22, 10.73, 10.78, 10.79, 2.7, 6.1
**Jaccard:** 0.500 — AI adds ['1.44', '10.12', '2.1', 'CN4', 'CN5', 'D10.1.2', 'D10.1.3']

## Proposition 10.85
**Statement:** To find the first apotome.

**Step 1.** Let r be the assigned rational straight line. By 10.48 construct a first binomial relative to r, and denote its greater term by a and its lesser term by b. We choose this construction because its terms already possess the required commensurability and square-difference properties; only subtraction remains. [10.48; D10.2.1]

**Step 2.** By the definition of a binomial introduced in 10.36, a and b are rational straight lines commensurable in square only. Since their sum is a first binomial, a is commensurable in length with r, and there is a straight line c commensurable in length with a such that the square on a equals the squares on b and c together. [10.36; D10.2.1]

**Step 3.** Since a is greater than b, cut from a a segment equal to b, and call the remaining segment x. This construction is possible by 1.3. The remainder x is an apotome, because a and the subtracted segment b are rational and commensurable in square only. Its annex is b and its whole is a. [1.3; 10.73]

**Step 4.** The square on the whole a exceeds the square on the annex b by the square on c, which is commensurable in length with a; moreover, a is commensurable in length with the assigned rational straight line r. Thus x satisfies precisely the definition of a first apotome. Therefore the required first apotome has been found. [D10.3.1]

**USED:** 1.3, 10.36, 10.48, 10.73, D10.2.1, D10.3.1
**Human refs (from References field):** 10.6, 10.73, 10.9, 5.19, D10.3.1
**Jaccard:** 0.222 — AI adds ['1.3', '10.36', '10.48', 'D10.2.1']; Human adds ['10.6', '10.9', '5.19']

## Proposition 10.86
**Statement:** To find the second apotome.

**Step 1.** Let r be the assigned rational straight line. Construct a second binomial relative to r, and let its greater and lesser terms be a and b respectively [10.49]. We choose this route because the second binomial already supplies the required pair of terms; we shall subtract them instead of adding them.

**Step 2.** By the definition of a binomial, a and b are rational straight lines commensurable in square only [10.36]. Since their sum is a second binomial, b is commensurable in length with r, and the square on a exceeds the square on b by the square on a straight line c commensurable in length with a [D10.2.1, D10.2.2].

**Step 3.** Since a is greater than b, cut off from a a straight line equal to b, and call the remainder d [1.3]. Thus d is obtained by subtracting from the rational straight line a the rational straight line b, which is commensurable with a in square only. Therefore d is an apotome, with whole a and annex b [10.73].

**Step 4.** The annex b is commensurable in length with the assigned rational straight line r, and the square on the whole a exceeds the square on the annex b by the square on c, which is commensurable in length with a. Hence d is a second apotome [D10.3.2]. Thus the second apotome has been found.

**USED:** 1.3, 10.36, 10.49, 10.73, D10.2.1, D10.2.2, D10.3.2
**Human refs (from References field):** 10.6, 10.73, 10.9, 5.19, D10.3.2
**Jaccard:** 0.200 — AI adds ['1.3', '10.36', '10.49', 'D10.2.1', 'D10.2.2']; Human adds ['10.6', '10.9', '5.19']

## Proposition 10.87
**Statement:** To find the third apotome.

**Step 1.** Let r be the assigned rational straight line. By 10.50 construct a third binomial relative to r, and denote its greater and lesser terms by a and b. We choose this construction because its terms already satisfy the required conditions; subtraction instead of addition will produce the desired apotome. [10.50]

**Step 2.** As the terms of a binomial, a and b are rational straight lines commensurable in square only. Since their sum is a third binomial, neither a nor b is commensurable in length with r. Moreover, the square on a exceeds the square on b by the square on a straight line c commensurable in length with a. [10.36; D10.2.1; D10.2.3]

**Step 3.** Since a is greater than b, cut off from a a segment equal to b, and call the remainder x. Because a and b are rational and commensurable in square only, x is an apotome. Its whole is a and its annex is b. [1.3; 10.73]

**Step 4.** Neither the whole a nor the annex b is commensurable in length with the assigned rational straight line r, and the square on the whole exceeds the square on the annex by the square on c, which is commensurable in length with the whole. Therefore x is a third apotome. Thus the required third apotome has been found. [D10.3.3]

**USED:** 1.3, 10.36, 10.50, 10.73, D10.2.1, D10.2.3, D10.3.3
**Human refs (from References field):** 10.6, 10.73, 10.9, 5.19, 5.22, D10.3.3
**Jaccard:** 0.182 — AI adds ['1.3', '10.36', '10.50', 'D10.2.1', 'D10.2.3']; Human adds ['10.6', '10.9', '5.19', '5.22']

## Proposition 10.88
**Statement:** To find the fourth apotome.

**Step 1.** Let r be the assigned rational straight line. Construct a fourth binomial by 10.51, and denote its greater term by a and its lesser term by b. This construction is the direct choice because its terms already satisfy the required conditions on the whole and annex, without rescaling. [10.51]

**Step 2.** By the definition of binomial, a and b are rational straight lines commensurable in square only. Since their sum is a fourth binomial, a is commensurable in length with r, and the square on a exceeds the square on b by the square on a straight line d incommensurable in length with a. [10.36, D10.2.4]

**Step 3.** Denote the greater term a by AB. From its end B cut off BC equal to b, with C between A and B. Since the rational straight line BC is commensurable with the rational whole AB in square only, the remainder AC is an apotome, whose whole is AB and whose annex is BC. [1.3, 10.73]

**Step 4.** The whole AB is commensurable in length with r, while its square exceeds the square on the annex BC by the square on d, which is incommensurable in length with AB. Therefore AC is a fourth apotome. Thus the required fourth apotome has been found. [D10.3.4]

**USED:** 1.3, 10.36, 10.51, 10.73, D10.2.4, D10.3.4
**Human refs (from References field):** 10.6, 10.73, 10.9, 5.19, D10.3.4
**Jaccard:** 0.222 — AI adds ['1.3', '10.36', '10.51', 'D10.2.4']; Human adds ['10.6', '10.9', '5.19']

## Proposition 10.89
**Statement:** To find the fifth apotome.

**Step 1.** Let r be the assigned rational straight line. Construct a fifth binomial by 10.52, and denote its greater term by AB and its lesser term by b. Construction choice: use this construction because its terms already possess exactly the square-difference and commensurability properties needed for a fifth apotome. As terms of a binomial, AB and b are rational straight lines commensurable in square only (10.36).

**Step 2.** By the defining conditions of a fifth binomial, b is commensurable in length with r, and the square on AB exceeds the square on b by the square on a straight line d incommensurable in length with AB. Thus AB² = b² + d² (D10.2.4, D10.2.5).

**Step 3.** From AB cut off BC equal to b, leaving AC (1.3). Since the rational straight line BC is commensurable with the rational whole AB in square only, the remainder AC is an apotome, with whole AB and annex BC (10.73).

**Step 4.** The annex BC is commensurable in length with the assigned rational straight line r. Moreover, by Step 2, the square on the whole AB exceeds the square on the annex BC by the square on d, which is incommensurable in length with AB. Therefore AC is a fifth apotome by D10.3.4 and D10.3.5. Thus the fifth apotome has been found.

**USED:** 1.3, 10.36, 10.52, 10.73, D10.2.4, D10.2.5, D10.3.4, D10.3.5
**Human refs (from References field):** 10.6, 10.73, 10.9, 5.19, D10.3.5
**Jaccard:** 0.182 — AI adds ['1.3', '10.36', '10.52', 'D10.2.4', 'D10.2.5', 'D10.3.4']; Human adds ['10.6', '10.9', '5.19']

## Proposition 10.90
**Statement:** To find the sixth apotome.

**Step 1.** Let r be the assigned rational straight line. Construct a sixth binomial relative to r, and let its greater and lesser terms be u and v, respectively [10.53]. We choose this construction because its terms already have the required properties; we shall subtract the lesser instead of adding it.

**Step 2.** By the definition of a binomial, u and v are rational straight lines commensurable in square only [10.36]. Since the binomial is sixth, neither u nor v is commensurable in length with r, and the square on u exceeds the square on v by the square on a straight line d incommensurable in length with u [D10.2.4, D10.2.6].

**Step 3.** From u cut off a straight line equal to v, and call the remainder w [1.3]. Since a rational straight line has been subtracted from a rational straight line commensurable with it in square only, w is an apotome [10.73]. Its whole is u and its annex is v.

**Step 4.** The square on the whole u exceeds the square on the annex v by the square on d, which is incommensurable in length with u; moreover, neither the whole nor the annex is commensurable in length with the assigned rational straight line r. Therefore w is a sixth apotome [D10.3.4, D10.3.6]. Thus the required sixth apotome has been found.

**USED:** 1.3, 10.36, 10.53, 10.73, D10.2.4, D10.2.6, D10.3.4, D10.3.6
**Human refs (from References field):** 10.6, 10.73, 10.9, 5.19, 5.22, D10.3.6
**Jaccard:** 0.167 — AI adds ['1.3', '10.36', '10.53', 'D10.2.4', 'D10.2.6', 'D10.3.4']; Human adds ['10.6', '10.9', '5.19', '5.22']

## Proposition 10.91
**Statement:** If an area be contained by a rational straight line and a first apotome, the âsideâ of the area is an apotome.

**Step 1.** Let r be the given rational straight line, and write the first apotome as a−b, where a is its whole and b its annex. Products below denote rectangles, and t² denotes the square on t. By the meaning of apotome, a and b are rational and commensurable in square only [10.73]. By the definition of a first apotome, a is commensurable in length with r, and a²−b²=c² for a straight line c commensurable in length with a [D10.3.1].

**Step 2.** Bisect b, calling its half h [1.10]. Since b<a, the square h² is smaller than the square on half a. Apply to a a rectangle equal to h² and deficient by a square [6.28]. Its division of a gives positive parts x,y satisfying x+y=a and xy=h². The parts are unequal: if x=y, then h=x=y, whence b=2h=x+y=a, a contradiction. Label them so that x>y. We use this deficient-square construction because 10.17 applies directly to the commensurable square-difference specified in Step 1.

**Step 3.** Since xy is the fourth part of b² and a²−b² is the square on a line commensurable with a, the parts x,y are commensurable in length [10.17]. Each is therefore commensurable with their sum a [10.15], and hence with r [10.12].

**Step 4.** Construct straight lines u,v whose squares equal the rectangles rx,ry respectively [2.14]. Thus u²=rx and v²=ry, with u>v since x>y [6.1]. Moreover,
 u²:r²=x:r and v²:r²=y:r [6.1].
Consequently, each of u²,v² is commensurable with r² [10.11]. Since r is rational, u and v are rational [10.12, D10.1.3]; and their squares are commensurable with one another [10.12, D10.1.2].

**Step 5.** The rectangle ratios give
 u²:v²=rx:ry=x:y=x²:(xy)=x²:h² [6.1, 5.11].
Since the squares on u,v,x,h are proportional, their sides are proportional [6.22]. Therefore u:v=x:h.

**Step 6.** From u²=rx, we have r:u=u:x [6.17]. From u:v=x:h, alternation gives u:x=v:h [5.16]. Hence r:u=v:h [5.11], and therefore uv=rh [6.16]. Since b consists of two copies of h, it follows that 2uv=rb [2.1].

**Step 7.** The straight lines u,v are incommensurable in length. For, if they were commensurable, the proportion u:v=x:h would make x,h commensurable [10.11]. But x is commensurable with a by Step 3, while h is commensurable with b because b=2h [D10.1.1]. Repeated application of 10.12 would then make a,b commensurable in length, contrary to Step 1. Thus u,v are rational straight lines commensurable in square only.

**Step 8.** Subtract v from u, leaving w [1.3]. By 2.7,
 w²+2uv=u²+v².
But u²+v²=rx+ry=r(x+y)=ra [CN2, 2.1], and 2uv=rb by Step 6. Subtracting equal areas therefore gives
 w²=ra−rb=r(a−b) [CN3, 2.1].

**Step 9.** Since w is obtained by subtracting from the rational straight line u the rational straight line v, commensurable with u in square only, w is an apotome [10.73]. Its square equals the given rectangle r(a−b), so w is the side of that area [D10.1.4]. Therefore the side of an area contained by a rational straight line and a first apotome is an apotome.

**USED:** 1.10, 1.3, 10.11, 10.12, 10.15, 10.17, 10.73, 2.1, 2.14, 2.7, 5.11, 5.16, 6.1, 6.16, 6.17, 6.22, 6.28, CN2, CN3, D10.1.1, D10.1.2, D10.1.3, D10.1.4, D10.3.1
**Human refs (from References field):** 10.11, 10.12, 10.13, 10.15, 10.17, 10.19, 10.21, 10.53, 10.73, 5.11, 6.1, 6.17, 6.26, D10.3.1
**Jaccard:** 0.310 — AI adds ['1.10', '1.3', '2.1', '2.14', '2.7', '5.16', '6.16', '6.22', '6.28', 'CN2', 'CN3', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.1.4']; Human adds ['10.13', '10.19', '10.21', '10.53', '6.26']

## Proposition 10.92
**Statement:** If an area be contained by a rational straight line and a second apotome, the âsideâ of the area is a first apotome of a medial straight line.

**Step 1.** Write uv for the rectangle contained by straight lines u and v, and u² for the square on u. Let r be the given rational straight line, and let the second apotome, relative to r, be a−b, where a>b. By the definition of a second apotome and the description of an apotome, a and b are rational and commensurable in square only, b is commensurable in length with r, and a²−b²=d² for a straight line d commensurable in length with a. The given area is r(a−b). [D10.3.2, 10.73]

**Step 2.** Bisect b, calling its half c; thus c² is the fourth part of b². Apply to a a rectangle equal to c² and deficient by a square. This construction is possible because b<a, so c² is less than the square on half of a. Denote the resulting parts of a by p>q. Then p+q=a and pq=c². We choose this construction because the converse in 10.17 applies directly to the defining condition a²−b²=d²: it gives that p and q are commensurable in length. Consequently, each is commensurable in length with their sum a. [1.10, 2.4, 6.28, 10.17, 10.15]

**Step 3.** Straight lines commensurable in length are also commensurable in square: their squares have the ratio of square numbers, and magnitudes having a numerical ratio are commensurable. Therefore, since p and q are commensurable in length with the rational line a, they are rational. Likewise c, being half of the rational line b, is rational. Moreover, c is commensurable in length with b, and hence with r. [10.9, 10.6, 10.12, D10.1.3, D10.1.1]

**Step 4.** Since a is incommensurable in length with b, while b is commensurable in length with r, a is incommensurable in length with r. Since p and q are each commensurable in length with a, each is likewise incommensurable in length with r. But p, q, and r are rational, so p and r, and also q and r, are commensurable in square only. Construct square sides x and y such that x²=rp and y²=rq; take x>y, since p>q. By 10.21, both x and y are medial straight lines. [10.13, D10.1.3, 10.12, 2.14, 6.1, 10.21]

**Step 5.** The rectangles rp and rq have the same altitude, so x²:y²=p:q. Since p and q are commensurable in length, x² and y² are commensurable areas. Thus x and y are commensurable in square. [6.1, 10.11, D10.1.2]

**Step 6.** Using pq=c² and the defining squares of x and y, the equal-altitude rectangle proportions give
x²:c²=rp:pq=r:q
and
r²:y²=r²:rq=r:q.
Hence x²:c²=r²:y². By the converse of 6.22, applied to squares, x:c=r:y; therefore xy=rc. Since r and c are rational and commensurable in length, rc, and consequently xy, is a rational area. [6.1, 5.11, 6.22, 6.16, 10.19]

**Step 7.** If x and y were commensurable in length, their rectangle would be medial by 10.24, since both lines are medial. A medial area is irrational, whereas Step 6 establishes that xy is rational. This is impossible. Hence x and y are incommensurable in length and, by Step 5, commensurable in square only. [10.24, 10.21, D10.1.4]

**Step 8.** Since p+q=a and 2c=b, distribution of rectangles gives
x²+y²=rp+rq=ra,
and
2xy=2rc=rb.
By 2.7, x²+y²=2xy+(x−y)². Subtracting equal areas therefore yields
(x−y)²=ra−rb=r(a−b).
Thus x−y is the side of the given area. [2.1, 2.7, CN3]

**Step 9.** We have obtained x−y by subtracting from the medial straight line x a medial straight line y which is commensurable with x in square only and contains with x a rational rectangle. Therefore 10.74 identifies x−y as a first apotome of a medial straight line. By Step 8, this is the side of the area contained by r and the given second apotome, as required. [10.74]

**USED:** 1.10, 10.11, 10.12, 10.13, 10.15, 10.17, 10.19, 10.21, 10.24, 10.6, 10.73, 10.74, 10.9, 2.1, 2.14, 2.4, 2.7, 5.11, 6.1, 6.16, 6.22, 6.28, CN3, D10.1.1, D10.1.2, D10.1.3, D10.1.4, D10.3.2
**Human refs (from References field):** 10.11, 10.13, 10.15, 10.17, 10.19, 10.21, 10.73, 10.74, 5.11, 6.1, 6.17, 6.26, D10.3.2
**Jaccard:** 0.367 — AI adds ['1.10', '10.12', '10.24', '10.6', '10.9', '2.1', '2.14', '2.4', '2.7', '6.16', '6.22', '6.28', 'CN3', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.1.4']; Human adds ['6.17', '6.26']

## Proposition 10.93
**Statement:** If an area be contained by a rational straight line and a third apotome, the âsideâ of the area is a second apotome of a medial straight line.

**Step 1.** Let r be the given rational straight line, and write the third apotome as a−b, where a is its whole and b its annex. Products of straight lines below denote rectangles, and squares denote the corresponding square areas. By 10.73, a and b are rational and commensurable in square only. By D10.3.3, neither is commensurable in length with r, and a²−b²=c² for some straight line c commensurable in length with a.

**Step 2.** Let d be half of b (1.10), so that d² is the fourth part of b² (2.4). Apply to a a rectangle equal to d² and deficient by a square; this is possible by 6.28 because b<a. Let u and v be the resulting segments, with u>v. Thus u+v=a and uv=d². We use 10.17 directly here because its square-difference hypothesis is precisely the condition supplied in Step 1: it follows that u and v are commensurable in length. Consequently each is commensurable in length with a=u+v (10.15).

**Step 3.** Since d measures b twice, d is commensurable in length with b (D10.1.1). The commensurabilities of u and v with a, and of d with b, imply that u, v, and d are rational: their squares are commensurable with the respective rational squares by 10.9 and 10.6, and hence with the assigned rational square by 10.12 and D10.1.3. Moreover, u and v are incommensurable in length with r because a is, and d is incommensurable in length with r because b is (10.13). Thus each of u, v, and d is commensurable in square only with r. Finally, u is incommensurable in length with b, and therefore with d, by applying 10.13 first to u and a, and then to b and d.

**Step 4.** Construct straight lines x and y such that x²=ru and y²=rv (2.14). Since u>v, we have x²>y² and therefore x>y (2.1, 2.4, CN5). The pairs r,u and r,v consist of rational straight lines commensurable in square only, so x and y are medial straight lines (10.21).

**Step 5.** By 6.1,

x²:y² = ru:rv = u:v.

Since u and v are commensurable, x² and y² are commensurable (10.11). Also, because d²=uv, 6.1 gives

u²:d² = u²:uv = u:v.

Hence x²:y²=u²:d² (5.11), and consequently x:y=u:d by the converse in 6.22, applied to squares. Since u and d are incommensurable in length, x and y are incommensurable in length (10.11). Therefore x and y are commensurable in square only (D10.1.2).

**Step 6.** Using 6.1 and the proportion just obtained, we have

x²:xy = x:y = u:d = ru:rd = x²:rd.

The equality of these ratios follows by 5.11. Thus xy=rd, since magnitudes to which the same magnitude has the same ratio are equal (5.9). By Step 3, r and d are rational and commensurable in square only; therefore rd, and hence xy, is a medial area (10.21).

**Step 7.** We have exhibited medial straight lines x>y which are commensurable in square only and contain a medial rectangle. Therefore x−y is a second apotome of a medial straight line (10.75).

**Step 8.** By 2.7,

(x−y)²+2xy = x²+y².

But x²+y²=ru+rv=r(u+v)=ra, and 2xy=2rd=rb because b=2d (2.1). Subtracting equal areas therefore gives

(x−y)² = ra−rb = r(a−b)

(CN3, 2.1). Thus x−y is the side of the given area (D10.1.4). By Step 7, that side is a second apotome of a medial straight line, as required.

**USED:** 1.10, 10.11, 10.12, 10.13, 10.15, 10.17, 10.21, 10.6, 10.73, 10.75, 10.9, 2.1, 2.14, 2.4, 2.7, 5.11, 5.9, 6.1, 6.22, 6.28, CN3, CN5, D10.1.1, D10.1.2, D10.1.3, D10.1.4, D10.3.3
**Human refs (from References field):** 10.11, 10.13, 10.15, 10.17, 10.21, 10.75, 5.11, 6.1, 6.17, 6.26, D10.3.3
**Jaccard:** 0.310 — AI adds ['1.10', '10.12', '10.6', '10.73', '10.9', '2.1', '2.14', '2.4', '2.7', '5.9', '6.22', '6.28', 'CN3', 'CN5', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.1.4']; Human adds ['6.17', '6.26']

## Proposition 10.94
**Statement:** If an area be contained by a rational straight line and a fourth apotome, the âsideâ of the area is minor.

**Step 1.** Let r be the rational straight line set out, and write the fourth apotome as b − c, where b is the whole and c the annex. Write uv for the rectangle contained by u and v, and u² for the square on u. By 10.73 and D10.3.4, b and c are rational and commensurable in square only, b is commensurable in length with r, and b² exceeds c² by the square on a straight line incommensurable in length with b.

**Step 2.** Bisect c, and put h = c/2 [1.10]. Then h is commensurable in length with c [D10.1.1], and h² = c²/4 [2.4]. Consequently h² is commensurable with the assigned rational square, so h is rational [D10.1.1, 10.12, D10.1.3]. Since r is commensurable in length with b, whereas c is incommensurable in length with b, r and c are incommensurable in length; since h is commensurable with c, r and h are likewise incommensurable in length [10.13]. Being rational, r and h are commensurable in square [10.12, D10.1.3]. Thus the rectangle rh is medial [10.21].

**Step 3.** Since c < b, h² is less than the square on half of b. Apply to b a rectangle equal to h² and deficient by a square [6.28]. Its division of b gives segments m and n such that m + n = b and mn = h² = c²/4. By 10.18, m and n are incommensurable in length. This is the direct applicable route because the square-excess condition in Step 1 is precisely the incommensurable condition of 10.18. The segments are therefore unequal; name them so that m > n.

**Step 4.** Construct square sides x, y, z such that x² = rm, y² = rn, and z² = rh [2.14]. We have x > y. Rectangles with the same height have the ratio of their bases, so x² : y² = m : n [6.1]. Since m and n are incommensurable, x² and y² are incommensurable [10.11]. Hence x and y are incommensurable in square [D10.1.2].

**Step 5.** By distribution of rectangles,
x² + y² = rm + rn = r(m + n) = rb [2.1].
Since r and b are rational and commensurable in length, rb is rational [10.19]. Thus the sum of the squares on x and y is rational.

**Step 6.** From mn = h² we obtain m : h = h : n [6.17]. Therefore
x² : z² = m : h = h : n = z² : y² [6.1, 5.11].
The proportionality of these squares gives x : z = z : y [6.22]. Hence xy = z² = rh [6.17]. By Step 2, the rectangle xy is therefore medial [10.21].

**Step 7.** The lines x and y are incommensurable in square, their squares together form a rational area, and their rectangle is medial. Therefore their difference x − y is minor [10.76].

**Step 8.** Finally, 2.7 gives x² + y² = 2xy + (x − y)². Substituting the equalities already proved and subtracting equal areas yields
(x − y)² = rb − 2rh = rb − rc = r(b − c),
since 2h = c [2.1, CN3]. Thus x − y is the side of the area contained by r and the given fourth apotome [D10.1.4]. By Step 7 this side is minor, as required.

**USED:** 1.10, 10.11, 10.12, 10.13, 10.18, 10.19, 10.21, 10.73, 10.76, 2.1, 2.14, 2.4, 2.7, 5.11, 6.1, 6.17, 6.22, 6.28, CN3, D10.1.1, D10.1.2, D10.1.3, D10.1.4, D10.3.4
**Human refs (from References field):** 10.11, 10.18, 10.19, 10.21, 10.76, 5.11, 6.1, 6.17, 6.26, D10.3.4
**Jaccard:** 0.360 — AI adds ['1.10', '10.12', '10.13', '10.73', '2.1', '2.14', '2.4', '2.7', '6.22', '6.28', 'CN3', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.1.4']; Human adds ['6.26']

## Proposition 10.95
**Statement:** If an area be contained by a rational straight line and a fifth apotome, the âsideâ of the area is a straight line which produces with a rational area a medial whole.

**Step 1.** Write uv for the rectangle contained by straight lines u and v, and u² for the square on u. Let r be the given rational straight line and let a−b be the fifth apotome, with whole a and annex b. Thus a>b are rational straight lines commensurable in square only; b is commensurable in length with r; and a²−b² is the square on a straight line incommensurable in length with a. [10.73; D10.3.5]

**Step 2.** We use the sum a+b, because the same defining conditions immediately make it a fifth binomial. Indeed, it is binomial by 10.36 and fifth by D10.2.5. Therefore the side of r(a+b) is a straight line called the side of a rational plus a medial area. [10.58] By the designation introduced in 10.40, write this side as x+y, choosing x>y, where x² and y² are incommensurable, their sum S=x²+y² is medial, and xy is rational. Thus (x+y)²=r(a+b). [10.40]

**Step 3.** Since a and r are rational, their squares are commensurable. [D10.1.3; 10.12] But b is commensurable in length with r and incommensurable in length with a; hence a and r are incommensurable in length. [10.13] Consequently M=ra is medial. [10.21] Also R=rb is rational, since r and b are rational and commensurable in length. [10.19]

**Step 4.** Put T=2xy. Since xy is rational, its double T is also rational: the double is commensurable with xy, and hence with the assigned rational square. [10.15; 10.12; D10.1.4] Expanding the equality from Step 2 gives
S+T=(x+y)²=r(a+b)=M+R.
[2.4; 2.1]

**Step 5.** We claim that S=M and T=R. If S and M were unequal, the greater would exceed the lesser by the positive difference of R and T, by cancellation in S+T=M+R. [CN3] That difference would be rational: R and T are commensurable with the assigned rational square and therefore with one another; their difference is commensurable with either, and consequently with the assigned square. [D10.1.4; 10.12; 10.15] But S and M are medial, and a medial area cannot exceed a medial area by a rational area. [10.26] Hence S=M, and cancellation then gives T=R. [CN3]

**Step 6.** The square on the difference x−y satisfies
(x−y)²+2xy=x²+y².
[2.7] Substituting the equalities established in Step 5 and subtracting equal areas yields
(x−y)²=M−R=ra−rb=r(a−b).
[CN3; 2.1] Thus x−y is the side of the given area.

**Step 7.** The straight lines x and y are incommensurable in square, the sum of their squares is medial, and twice their rectangle is rational, as established in Steps 2 and 4. Therefore their difference x−y is precisely a straight line which produces with a rational area a medial whole. [10.77] Hence the side of an area contained by a rational straight line and a fifth apotome has the required designation.

**USED:** 10.12, 10.13, 10.15, 10.19, 10.21, 10.26, 10.36, 10.40, 10.58, 10.73, 10.77, 2.1, 2.4, 2.7, CN3, D10.1.3, D10.1.4, D10.2.5, D10.3.5
**Human refs (from References field):** 10.18, 10.19, 10.21, 10.77, 6.26, D10.3.5
**Jaccard:** 0.190 — AI adds ['10.12', '10.13', '10.15', '10.26', '10.36', '10.40', '10.58', '10.73', '2.1', '2.4', '2.7', 'CN3', 'D10.1.3', 'D10.1.4', 'D10.2.5']; Human adds ['10.18', '6.26']

## Proposition 10.96
**Statement:** If an area be contained by a rational straight line and a sixth apotome, the âsideâ of the area is a straight line which produces with a medial area a medial whole.

**Step 1.** Let r be the given rational straight line, and write the sixth apotome as a−b, where a is its whole and b its annex. Write uv for the rectangle contained by u and v, and u² for the square on u. By 10.73, a and b are rational and commensurable in square only. By the definition of a sixth apotome, neither a nor b is commensurable in length with r, and a² exceeds b² by the square on a straight line incommensurable in length with a. [10.73; D10.3.4; D10.3.6]

**Step 2.** Since r, a, and b are rational, their squares are commensurable with one another. Thus r is commensurable in square only with each of a and b, so the rectangles ra and rb are medial areas. Moreover, ra:rb = a:b; therefore ra and rb are incommensurable, because a and b are incommensurable in length. [D10.1.3; 10.12; 10.21; 6.1; 10.11]

**Step 3.** Bisect b, and denote its half by h. Apply to a a rectangle equal to h² and deficient by a square. This construction is possible because b<a, so h² is less than the square on half of a. Let c and d be the resulting parts of a; then c+d=a and cd=h²=b²/4. The incommensurable clause of 10.18 shows that c and d are incommensurable in length. In particular they are unequal; name the greater c. The path choice here is to use 10.18 directly, since its incommensurable hypothesis is exactly the sixth-apotome condition established in Step 1. [1.10; 6.28; 10.18]

**Step 4.** Construct straight lines x and y such that x²=rc and y²=rd, with x>y since c>d. Rectangles of equal height give x²:y²=c:d. Hence the squares on x and y are incommensurable, and x and y are therefore incommensurable in square. [2.14; 6.1; 10.11; D10.1.2]

**Step 5.** We show that twice the rectangle xy equals rb. Since h²=cd, equal-height rectangles give
c²:h² = c²:cd = c:d = x²:y².
The converse direction of 6.22, applied to these squares, therefore gives x:y=c:h. Consequently,
x²:xy = x:y = c:h = rc:rh.
As x²=rc, magnitudes having the same ratio to these equal antecedents are equal; thus xy=rh. Adding equals to equals, and using b=h+h, yields 2xy=2rh=rb. [6.1; 5.11; 6.22; 5.9; CN2; 2.1]

**Step 6.** Since c+d=a, distribution of the rectangle gives
x²+y² = rc+rd = ra.
Also, 2.7 gives (x−y)²+2xy=x²+y². Substituting the preceding equality and 2xy=rb, and subtracting equal areas, we obtain
(x−y)² = ra−rb = r(a−b).
Thus x−y is the side of a square equal to the given area. [2.1; 2.7; CN3]

**Step 7.** By Step 4, x and y are incommensurable in square. By Steps 2, 5, and 6, the sum x²+y² is the medial area ra, twice their rectangle is the medial area rb, and these two areas are incommensurable. Therefore 10.78 applies to the subtraction of y from x: the remainder x−y is the irrational straight line called that which produces with a medial area a medial whole. Since its square equals the given rectangle by Step 6, the required side has precisely this character. [10.78]

**USED:** 1.10, 10.11, 10.12, 10.18, 10.21, 10.73, 10.78, 2.1, 2.14, 2.7, 5.11, 5.9, 6.1, 6.22, 6.28, CN2, CN3, D10.1.2, D10.1.3, D10.3.4, D10.3.6
**Human refs (from References field):** 10.11, 10.18, 10.21, 10.78, 6.1, 6.26, D10.3.6
**Jaccard:** 0.273 — AI adds ['1.10', '10.12', '10.73', '2.1', '2.14', '2.7', '5.11', '5.9', '6.22', '6.28', 'CN2', 'CN3', 'D10.1.2', 'D10.1.3', 'D10.3.4']; Human adds ['6.26']

## Proposition 10.97
**Statement:** The square on an apotome applied to a rational straight line produces as breadth a first apotome.

**Step 1.** Let d be the given apotome. By the characterization in 10.73, write d = x − y, where x > y and x, y are rational straight lines commensurable in square only. Let r be the rational straight line to which the square on d is applied, and let t be the resulting breadth, so that rt = d². Throughout, a product of straight lines denotes their rectangle (D2.1).

**Step 2.** Construct straight lines p, q, h such that
rp = x², rq = y², rh = xy
by taking fourth proportionals (6.12, 6.16). The squares x² and y² are rational areas; their sum is also rational, since each is commensurable with the assigned rational square (D10.1.3, D10.1.4, 10.12, 10.15). Therefore 10.20 shows that p and q are rational and each is commensurable in length with r. In particular, p and q are commensurable in length with one another (10.12). Put u = p + q. By 2.1, ru = x² + y²; hence 10.20 also shows that u is rational and commensurable in length with r.

**Step 3.** Rectangles of the same height have the ratio of their bases (6.1), so
p : h = x² : xy = x : y,
and
h : q = xy : y² = x : y.
Thus p : h = h : q (5.11), and consequently pq = h² (6.16). Since p and q are rational and commensurable in length, their rectangle, and therefore h², is rational (10.19). Set v = 2h. By 2.4,
v² = 4h² = 4pq.
A magnitude and its fourfold are commensurable, so v² is rational as well (D10.1.1, 10.12, D10.1.4). Consequently v is a rational straight line (D10.1.2, D10.1.3).

**Step 4.** Since x and y are incommensurable in length and p : h = x : y, the straight lines p and h are incommensurable in length (10.11). But u is commensurable in length with p, since both are commensurable with r (10.12), and v is commensurable in length with h, being its double (D10.1.1). Applying 10.13 successively therefore shows that u and v are incommensurable in length. Their squares are nevertheless commensurable, since both straight lines are rational (D10.1.2, D10.1.3, 10.12). Thus u and v are rational straight lines commensurable in square only.

**Step 5.** By 2.7,
x² + y² = 2xy + (x − y)².
The defining area equalities and 2.1 therefore give
ru = rv + rt = r(v + t).
By 6.1, u = v + t. Hence u > v (CN5), and t = u − v. Since u and v are rational and commensurable in square only, t is an apotome whose whole is u and whose annex is v (10.73).

**Step 6.** Use the commensurable-parts criterion of 10.17: it is the direct route here because the required parts p and q have already been obtained. Indeed, u = p + q, and the rectangle pq applied along the part p of u, with breadth q, is deficient by the square q², since uq = pq + q² (2.1). By Step 3, this rectangle equals one fourth of v². Its division of u is into the commensurable lengths p and q, and u > v by Step 5. Therefore 10.17 gives a straight line w commensurable in length with u such that
u² = v² + w².

**Step 7.** The breadth t is an apotome with whole u and annex v; the whole u is commensurable in length with the rational straight line r; and the square on u exceeds the square on v by the square on w, which is commensurable in length with u. These are exactly the conditions of D10.3.1. Therefore t is a first apotome. Thus the square on an apotome, applied to a rational straight line, produces as breadth a first apotome.

**USED:** 10.11, 10.12, 10.13, 10.15, 10.17, 10.19, 10.20, 10.73, 2.1, 2.4, 2.7, 5.11, 6.1, 6.12, 6.16, CN5, D10.1.1, D10.1.2, D10.1.3, D10.1.4, D10.3.1, D2.1
**Human refs (from References field):** 10.11, 10.17, 10.20, 10.22, 10.73, 2.7, 6.1, 6.17, D10.3.1
**Jaccard:** 0.292 — AI adds ['10.12', '10.13', '10.15', '10.19', '2.1', '2.4', '5.11', '6.12', '6.16', 'CN5', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.1.4', 'D2.1']; Human adds ['10.22', '6.17']

## Proposition 10.98
**Statement:** The square on a first apotome of a medial straight line applied to a rational straight line produces as breadth a second apotome.

**Step 1.** Let x be a first apotome of a medial straight line, and let r be the rational straight line to which its square is to be applied. By 10.74, write x = a − b, where a > b are medial straight lines commensurable in square only, and the rectangle ab is rational. Throughout, pq denotes the rectangle contained by p and q, and p² denotes the square on p. [10.74, D2.1]

**Step 2.** Construct straight lines u, v, w such that
ru = a²,  rv = b²,  rw = ab.
These constructions are possible by taking fourth proportionals and using the equality of the rectangles contained by the extremes and the means. Since a and b are medial, u and v are rational and incommensurable in length with r. Since ab is rational, w is rational and commensurable in length with r. Put U = u + v and V = 2w. [6.12, 6.16, 10.22, 10.20]

**Step 3.** Rectangles with the same base are proportional to their breadths, so
u : v = a² : b².
The squares a² and b² are commensurable; therefore u and v are commensurable in length. Their sum U is consequently commensurable in length with u, and hence incommensurable in length with r. On the other hand, V = 2w is commensurable in length with r: any common measure of w and r also measures 2w. It follows that U and V are incommensurable in length. [6.1, 10.11, 10.15, 10.13, D10.1.1]

**Step 4.** Again using ratios of rectangles with a common altitude,
u : w = a² : ab = a : b,
and
w : v = ab : b² = a : b.
Thus u, w, v are continuously proportional, and uv = w². The square-of-a-sum identity now gives
U² = u² + v² + 2w²,
V² = 4w² = 4uv.
In particular, uv is the fourth part of V². [6.1, 6.17, 2.4]

**Step 5.** Since u, v, w are rational straight lines, their squares are rational areas. Sums and integral multiples of these areas remain commensurable with the assigned rational square: this follows from commensurability with the same magnitude and commensurability of a sum with its commensurable summands. Hence the expressions for U² and V² in Step 4 are rational areas. Therefore U and V are rational straight lines, and their squares are commensurable. Together with Step 3, this proves that U and V are commensurable in square only. [D10.1.3, D10.1.4, 10.12, 10.15, D10.1.2]

**Step 6.** Because x = a − b, the square-and-rectangle identity gives
a² + b² = 2ab + x².
By the applications in Step 2 and distributivity of rectangles, this becomes
rU = rV + x².
Thus U > V, and subtraction yields
r(U − V) = x².
Consequently, the breadth obtained by applying x² to r is precisely U − V. [2.7, 2.1, CN5, CN3, 6.1]

**Step 7.** Use the commensurable-cut direction of 10.17, since the required division is already available. Indeed, divide U into u and v. The rectangle with base u and breadth v is deficient from the rectangle with base U and breadth v by the square on v. Its area is uv, which by Step 4 equals the fourth part of V². Since U > V and the parts u, v are commensurable in length, 10.17 shows that
U² = V² + d²
for a straight line d commensurable in length with U. [2.1, 10.17]

**Step 8.** The rational straight lines U and V are commensurable in square only, so U − V is an apotome, with whole U and annex V. Its annex V is commensurable in length with the given rational straight line r, while U² exceeds V² by the square on a straight line commensurable in length with U. Therefore U − V is a second apotome. By Step 6 it is exactly the required breadth. Thus the square on a first apotome of a medial straight line, applied to a rational straight line, produces as breadth a second apotome. [10.73, D10.3.2]

**USED:** 10.11, 10.12, 10.13, 10.15, 10.17, 10.20, 10.22, 10.73, 10.74, 2.1, 2.4, 2.7, 6.1, 6.12, 6.16, 6.17, CN3, CN5, D10.1.1, D10.1.2, D10.1.3, D10.1.4, D10.3.2, D2.1
**Human refs (from References field):** 10.11, 10.15, 10.17, 10.20, 10.22, 10.23, 10.73, 10.74, 2.7, 5.11, 6.1, 6.17, D10.3.2
**Jaccard:** 0.423 — AI adds ['10.12', '10.13', '2.1', '2.4', '6.12', '6.16', 'CN3', 'CN5', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.1.4', 'D2.1']; Human adds ['10.23', '5.11']

## Proposition 10.99
**Statement:** The square on a second apotome of a medial straight line applied to a rational straight line produces as breadth a third apotome.

**Step 1.** Let r be the rational straight line to which the square is applied. By the characterization in 10.75, write the given second apotome of a medial straight line as a−b, where a>b, both a and b are medial, they are commensurable in square only, and the rectangle ab is medial. We shall construct directly the whole and annex of the required breadth. Here uv denotes the rectangle contained by u and v, and u² denotes the square on u. [10.75]

**Step 2.** Construct straight lines x, y, z such that
rx=a²,   ry=b²,   rz=ab.
These constructions are possible by taking fourth proportionals and using the equality of the rectangles contained by the extremes and means. Since each applied area is medial, x, y, and z are rational and each is incommensurable in length with r. [6.12, 6.16, 10.22]

**Step 3.** Rectangles having the same height are proportional to their bases. Consequently,
x:y=a²:b²,   x:z=a:b,   z:y=a:b.
Since a² and b² are commensurable, x and y are commensurable in length. Since a and b are incommensurable in length, x and z are incommensurable in length. Moreover, x:z=z:y, so xy=z². [6.1, 5.11, D10.1.2, 10.11, 6.16]

**Step 4.** Put U=x+y and V=2z. Since x and y are commensurable in length, U is commensurable in length with x; and V is commensurable in length with z, which measures it twice. Thus U² is commensurable with x², and V² with z²: indeed, squares on length-commensurable lines have a ratio of square numbers and hence are commensurable. As x and z are rational, it follows that U and V are rational. [10.15, D10.1.1, 10.9, 10.6, 10.12, D10.1.3]

**Step 5.** Because U is commensurable in length with x, while x is incommensurable in length with r, U is incommensurable in length with r. Likewise, V is incommensurable in length with r. Also, x is incommensurable in length with z; transferring this first from x to U and then from z to V shows that U and V are incommensurable in length. Being rational, however, U and V are commensurable in square. Thus they are commensurable in square only, and neither is commensurable in length with r. [10.13, 10.12, D10.1.3, D10.1.2]

**Step 6.** By addition of rectangles,
rU=a²+b²,   rV=2ab.
But a²+b²=(a−b)²+2ab. Hence rU>rV, and therefore U>V. Subtracting the equal rectangles gives
r(U−V)=(a−b)².
Thus U−V is precisely the breadth produced by applying the square on the given line to r. [2.1, 2.7, CN5, 6.1, CN3]

**Step 7.** The division U=x+y supplies directly the deficient-rectangle criterion of 10.17: the rectangle xy, applied along the part x of U with breadth y, is deficient by the square on y. Its area is z², which is one fourth of V² because V=2z. Since the parts x and y are commensurable in length, 10.17 shows that
U²=V²+h²
for a straight line h commensurable in length with U. This criterion is the direct choice here because its required commensurable division has already been exhibited. [2.4, 10.17]

**Step 8.** Since U and V are rational and commensurable in square only, U−V is an apotome, with whole U and annex V. Neither its whole nor its annex is commensurable in length with the rational straight line r; and the square on its whole exceeds that on its annex by the square on h, which is commensurable in length with the whole. Therefore U−V is a third apotome. By Step 6 it is the required breadth. Hence the square on a second apotome of a medial straight line, applied to a rational straight line, produces as breadth a third apotome. [10.73, D10.3.3]

**USED:** 10.11, 10.12, 10.13, 10.15, 10.17, 10.22, 10.6, 10.73, 10.75, 10.9, 2.1, 2.4, 2.7, 5.11, 6.1, 6.12, 6.16, CN3, CN5, D10.1.1, D10.1.2, D10.1.3, D10.3.3
**Human refs (from References field):** 10.11, 10.13, 10.15, 10.17, 10.22, 10.23, 10.73, 10.75, 2.7, 5.11, 6.1, D10.3.3
**Jaccard:** 0.458 — AI adds ['10.12', '10.6', '10.9', '2.1', '2.4', '6.12', '6.16', 'CN3', 'CN5', 'D10.1.1', 'D10.1.2', 'D10.1.3']; Human adds ['10.23']

## Proposition 10.100
**Statement:** The square on a minor straight line applied to a rational straight line produces as breadth a fourth apotome.

**Step 1.** Let m be the given minor straight line and r the given rational straight line. Write x² for the square on x and xy for the rectangle contained by x and y. By the characterization of a minor, there are straight lines a > b such that m = a − b, the squares a² and b² are incommensurable, a² + b² is rational, and ab is medial (10.76). Consequently a + b is major (10.39). Our path is to apply 10.63 to this associated major, obtaining the square-excess condition required for a fourth apotome.

**Step 2.** Construct positive straight lines U and h such that
rU = a² + b² and rh = ab.
These applications are obtainable by fourth proportionals (6.12, 6.16), adding the breadths of the applications of a² and b² for the first equality (2.1). Since a² + b² is rational, U is rational and commensurable in length with r (10.20). Since ab is medial, h is rational and incommensurable in length with r (10.22).

**Step 3.** Put V = 2h. Then rV = 2ab (2.1). Also V² = 4h² (2.4), so V is rational: any area measuring both h² and the square on the assigned rational straight line also measures V² (D10.1.1, D10.1.3). Since h measures V, these two straight lines are commensurable in length; therefore V, like h, is incommensurable in length with r (D10.1.1, 10.13).

**Step 4.** By 2.7,
a² + b² = (a − b)² + 2ab.
Thus rU = m² + rV, and rU is greater than rV (CN5). Rectangles with the same height are proportional to their bases, so U > V (6.1, 5.14). Subtracting rV and using the distributivity of rectangles gives
r(U − V) = m²
(CN3, 2.1). Hence U − V is the breadth produced by applying the square on m to r.

**Step 5.** Since U and V are rational, their squares are commensurable with the square on the assigned rational straight line, and therefore with one another (D10.1.3, 10.12). But U is commensurable in length with r, whereas V is incommensurable in length with r; hence U and V are incommensurable in length (10.13). They are therefore rational straight lines commensurable in square only. It follows that U + V is binomial (10.36), and, since U > V, U − V is an apotome whose whole is U and whose annex is V (10.73).

**Step 6.** By 2.4 and 2.1,
(a + b)² = a² + b² + 2ab = rU + rV = r(U + V).
Thus U + V is the breadth obtained by applying the square on the major straight line a + b to r. It is consequently a fourth binomial (10.63).

**Step 7.** A binomial has only one division into its terms (10.42). Therefore the greater and lesser terms of this fourth binomial are precisely U and V, identified in Step 5. By the definition of a fourth binomial, U² exceeds V² by the square on a straight line incommensurable in length with U (D10.2.4).

**Step 8.** The apotome U − V thus has its whole U commensurable in length with r, while U² exceeds the square on its annex V by the square on a straight line incommensurable in length with U. It is therefore a fourth apotome (D10.3.4). By Step 4, it is exactly the breadth produced by applying the square on the given minor straight line to the given rational straight line. This proves the proposition.

**USED:** 10.12, 10.13, 10.20, 10.22, 10.36, 10.39, 10.42, 10.63, 10.73, 10.76, 2.1, 2.4, 2.7, 5.14, 6.1, 6.12, 6.16, CN3, CN5, D10.1.1, D10.1.3, D10.2.4, D10.3.4
**Human refs (from References field):** 10.11, 10.18, 10.20, 10.22, 10.73, 10.76, 2.7, 5.11, 6.1, 6.17, D10.3.4
**Jaccard:** 0.259 — AI adds ['10.12', '10.13', '10.36', '10.39', '10.42', '10.63', '2.1', '2.4', '5.14', '6.12', '6.16', 'CN3', 'CN5', 'D10.1.1', 'D10.1.3', 'D10.2.4']; Human adds ['10.11', '10.18', '5.11', '6.17']

## Proposition 10.101
**Statement:** The square on the straight line which produces with a rational area a medial whole, if applied to a rational straight line, produces as breadth a fifth apotome.

**Step 1.** Let c be the given straight line, and let r be the rational straight line to which its square is applied. By the designation in 10.77, write c = a − b, where a > b, the squares a² and b² are incommensurable, M = a² + b² is medial, and R = 2ab is rational. Here products denote rectangular areas. By 2.7, M = R + c²; hence M > R (CN5).

**Step 2.** Construct fourth proportionals p, q, h such that r:a = a:p, r:b = b:q, and r:a = b:h (6.12). Then rp = a², rq = b², and rh = ab (6.16). Put w = p + q and t = 2h. Thus rw = M and rt = R (2.1). Since M > R, the equal-base rectangles give w > t; subtracting them gives r(w − t) = c². Consequently w − t is the breadth in question (2.1, CN3, CN5).

**Step 3.** Since M is medial, its application to the rational straight line r gives w rational and incommensurable in length with r (10.22). Since R is rational, its application to r gives t rational and commensurable in length with r (10.20).

**Step 4.** The squares on w and t are each commensurable with the fixed rational square, and therefore with one another (D10.1.3, 10.12). Thus w and t are commensurable in square (D10.1.2). But t is commensurable in length with r, whereas w is not; hence w and t are incommensurable in length (10.13). Therefore w − t is an apotome, with whole w and annex t (10.73).

**Step 5.** The rectangles rp and rq have the same height, so p:q = rp:rq = a²:b² (6.1). Since a² and b² are incommensurable, p and q are incommensurable in length (10.11).

**Step 6.** Again using ratios of rectangles of equal height,

p:h = a²:ab = a:b = ab:b² = h:q

(6.1, 5.11). Reusing the rectangle criterion already employed in Step 2, we obtain pq = h² (6.16). Since t = 2h, we have t² = 4h² (2.4), and therefore pq is the fourth part of t².

**Step 7.** Since w = p + q, the rectangle contained by p and q is applied to w deficient by the square on q: indeed, wq = pq + q² (2.1). Its area is the fourth part of t², and it divides w into the incommensurable parts p and q. The direct path is therefore the incommensurable-cut criterion 10.18. Since w > t, that proposition shows that w² exceeds t² by the square on a straight line incommensurable in length with w.

**Step 8.** We have an apotome w − t whose annex t is commensurable in length with the rational straight line r, while the square on its whole w exceeds the square on its annex by the square on a straight line incommensurable in length with w. By D10.3.5, it is a fifth apotome. Since r(w − t) = c², the square on the given straight line, applied to r, produces as breadth a fifth apotome, as required.

**USED:** 10.11, 10.12, 10.13, 10.18, 10.20, 10.22, 10.73, 10.77, 2.1, 2.4, 2.7, 5.11, 6.1, 6.12, 6.16, CN3, CN5, D10.1.2, D10.1.3, D10.3.5
**Human refs (from References field):** 10.11, 10.18, 10.20, 10.22, 10.73, 10.77, 2.7, 6.1, D10.3.5
**Jaccard:** 0.450 — AI adds ['10.12', '10.13', '2.1', '2.4', '5.11', '6.12', '6.16', 'CN3', 'CN5', 'D10.1.2', 'D10.1.3']

## Proposition 10.102
**Statement:** The square on the straight line which produces with a medial area a medial whole, if applied to a rational straight line, produces as breadth a sixth apotome.

**Step 1.** Let x be the given straight line and r the rational straight line to which its square is to be applied. Write s² for the square on s and st for the rectangle contained by s and t. By 10.78, write x = a − b, where a > b, the squares a² and b² are incommensurable, and the areas M = a² + b² and N = 2ab are medial and incommensurable with one another. [10.78, D10.1.2]

**Step 2.** Apply a², b², and ab to r as rectangles, obtaining respective breadths p, q, and h; these applications may be made by successive applications of 1.44 to triangular pieces of the areas. Thus rp = a², rq = b², and rh = ab. Put u = p + q and v = 2h. By addition of rectangles on the same base, ru = M and rv = N. [1.44, 2.1]

**Step 3.** By 2.7, a² + b² = 2ab + (a − b)², so M = N + x². Consequently M > N, and therefore u > v, since rectangles on the same base are proportional to their breadths. Subtracting rv = N from ru = M now gives r(u − v) = x². Thus the breadth whose classification is required is u − v. [2.7, 6.1, 2.1, CN3]

**Step 4.** Since M and N are medial areas applied to the rational straight line r, both u and v are rational and incommensurable in length with r. Their squares are therefore commensurable with one another. Moreover, M:N = u:v; hence the incommensurability of M and N implies that u and v are incommensurable in length. Thus u and v are rational straight lines commensurable in square only, and u − v is an apotome, with whole u and annex v. [10.22, D10.1.3, 10.12, 6.1, 10.11, 10.73]

**Step 5.** Similarly, p:q = a²:b². Since a² and b² are incommensurable, p and q are incommensurable in length. Also, comparison of rectangles with a common side gives
p:h = a²:ab = a:b = ab:b² = h:q.
Therefore p, h, q are proportional, and the rectangle pq equals h². Since v = 2h, this rectangle equals the fourth part of v². [6.1, 10.11, 6.17, 2.4]

**Step 6.** The rectangle with sides p and q is an application to u = p + q deficient by the square on q: completing it to the rectangle uq adds precisely q². It therefore applies the fourth part of v² to u, deficient by a square, and divides u into the incommensurable parts p and q. We use 10.18 directly because this incommensurable division is already established. It follows that u² exceeds v² by the square on a straight line incommensurable in length with u. [2.1, 10.18]

**Step 7.** The apotome u − v has whole u and annex v, neither commensurable in length with the rational straight line r; moreover, the square on its whole exceeds the square on its annex by the square on a straight line incommensurable in length with the whole. Hence u − v is a sixth apotome. Since r(u − v) = x² by Step 3, the square on the given straight line, applied to r, produces a sixth apotome as breadth, as required. [D10.3.6]

**USED:** 1.44, 10.11, 10.12, 10.18, 10.22, 10.73, 10.78, 2.1, 2.4, 2.7, 6.1, 6.17, CN3, D10.1.2, D10.1.3, D10.3.6
**Human refs (from References field):** 10.11, 10.18, 10.22, 10.73, 10.78, 2.7, 6.1, D10.3.6
**Jaccard:** 0.500 — AI adds ['1.44', '10.12', '2.1', '2.4', '6.17', 'CN3', 'D10.1.2', 'D10.1.3']

## Proposition 10.103
**Statement:** A straight line commensurable in length with an apotome is an apotome and the same in order.

**Step 1.** Fix the assigned rational straight line r. Let x be an apotome and let y be commensurable in length with x. By the meaning of apotome in 10.73, write x = u − v, where u > v and u, v are rational straight lines commensurable in square only. We use proportional rescaling of these defining terms, so that the conditions determining the order can be transferred directly. [D10.1.3, 10.73]

**Step 2.** Construct a fourth proportional v′ such that x:y = v:v′, and put u′ = y + v′. Since u = x + v, the proposition on sums of proportional magnitudes gives
u:u′ = (x + v):(y + v′) = x:y = v:v′.
Thus y = u′ − v′. [6.12, 5.12]

**Step 3.** Since x and y are commensurable in length, the proportions in Step 2 imply that u and u′ are commensurable in length, and likewise v and v′. Moreover, alternation gives u:v = u′:v′. Since u and v are incommensurable in length, u′ and v′ are also incommensurable in length. [10.11, 5.16]

**Step 4.** The length-commensurabilities of u with u′ and v with v′ imply that their respective squares have ratios of square numbers, and hence are commensurable areas. Because u and v are rational, their squares are commensurable with the square on r. Consequently, the squares on u′ and v′ are also commensurable with the square on r, and therefore with one another. Thus u′ and v′ are rational straight lines commensurable in square. [10.9, 10.6, 10.12, D10.1.2, D10.1.3]

**Step 5.** By Steps 3–4, u′ and v′ are rational straight lines commensurable in square only. Since u′ = y + v′, subtracting v′ from u′ leaves y. Therefore y is an apotome. [10.73]

**Step 6.** Since u and u′ are commensurable in length, commensurability of u with r implies commensurability of u′ with r, while incommensurability of u with r implies incommensurability of u′ with r. The same assertions hold for v and v′. Hence the status of each defining term relative to r is preserved: the whole, the annex, or neither is commensurable in length with r, exactly as before. [10.12, 10.13]

**Step 7.** Apply 10.14 directly to u:v = u′:v′; this proposition preserves precisely the square-difference condition used to distinguish the orders. If the square on u exceeds the square on v by the square on a straight line commensurable in length with u, then the square on u′ exceeds the square on v′ by the square on a straight line commensurable in length with u′. If the former difference-square has its side incommensurable in length with u, then the latter has its side incommensurable in length with u′. [10.14]

**Step 8.** If x is a first, second, or third apotome, Step 7 preserves the commensurable difference-square condition, and Step 6 preserves, respectively, commensurability with r of the whole, the annex, or neither. Thus y is respectively a first, second, or third apotome. If x is a fourth, fifth, or sixth apotome, Step 7 preserves the incommensurable difference-square condition, and Step 6 preserves the same respective term-status; thus y is respectively a fourth, fifth, or sixth apotome. Therefore a straight line commensurable in length with an apotome is an apotome and the same in order. [D10.3.1, D10.3.2, D10.3.3, D10.3.4, D10.3.5, D10.3.6]

**USED:** 10.11, 10.12, 10.13, 10.14, 10.6, 10.73, 10.9, 5.12, 5.16, 6.12, D10.1.2, D10.1.3, D10.3.1, D10.3.2, D10.3.3, D10.3.4, D10.3.5, D10.3.6
**Human refs (from References field):** 10.11, 10.12, 10.13, 10.14, 10.73, 5.12, 5.16, 6.12
**Jaccard:** 0.444 — AI adds ['10.6', '10.9', 'D10.1.2', 'D10.1.3', 'D10.3.1', 'D10.3.2', 'D10.3.3', 'D10.3.4', 'D10.3.5', 'D10.3.6']

## Proposition 10.104
**Statement:** A straight line commensurable with an apotome of a medial straight line is an apotome of a medial straight line and the same in order.

**Step 1.** Let a be an apotome of a medial straight line, and let b be a straight line commensurable in length with a. Fix a rational straight line r. Write a² and b² for the areas of the squares on a and b. [D10.1.3]

**Step 2.** Since a and b are commensurable in length, a² has to b² the ratio of a square number to a square number. Consequently a² and b² are commensurable areas. [10.9, 10.6]

**Step 3.** Construct fourth proportionals c and d such that r:a = a:c and r:b = b:d. Then the rectangle contained by r and c equals a², and the rectangle contained by r and d equals b². Thus c and d are the breadths obtained by applying these squares to r. [6.12, 6.17]

**Step 4.** The two rectangles have the same altitude r, so their areas are proportional to their breadths: a²:b² = c:d. Since a² and b² are commensurable, c and d are commensurable in length. Here 6.1 applies directly because the altitude is common. [6.1, 10.11]

**Step 5.** If a is a first apotome of a medial straight line, c is a second apotome; if a is a second apotome of a medial straight line, c is a third apotome. [10.98, 10.99] The chosen route is through these ordinary apotomes, whose order can be transferred directly by 10.103.

**Step 6.** Since d is commensurable in length with c, d is an apotome of the same order as c. Therefore d is a second apotome when a is a first apotome of a medial straight line, and a third apotome when a is a second apotome of a medial straight line. [10.103]

**Step 7.** The square on b equals the rectangle contained by the rational straight line r and d. If d is a second apotome, the side of this area, b, is a first apotome of a medial straight line. If d is a third apotome, b is a second apotome of a medial straight line. [10.92, 10.93] Hence b is an apotome of a medial straight line and is of the same order as a, as required.

**USED:** 10.103, 10.11, 10.6, 10.9, 10.92, 10.93, 10.98, 10.99, 6.1, 6.12, 6.17, D10.1.3
**Human refs (from References field):** 10.11, 10.13, 10.23, 10.74, 10.75, 5.12, 5.16, 6.12, D10.1.4
**Jaccard:** 0.105 — AI adds ['10.103', '10.6', '10.9', '10.92', '10.93', '10.98', '10.99', '6.1', '6.17', 'D10.1.3']; Human adds ['10.13', '10.23', '10.74', '10.75', '5.12', '5.16', 'D10.1.4']

## Proposition 10.105
**Statement:** A straight line commensurable with a minor straight line is minor.

**Step 1.** Let x be a minor straight line, and let y be commensurable in length with x. Choose a rational straight line r [D10.1.3]. We use the common-base rectangle route, because 10.100 directly associates the square on a minor with a fourth apotome.

**Step 2.** Construct straight lines a and b such that r:x = x:a and r:y = y:b [6.12]. Then the rectangle contained by r and a equals the square on x, and the rectangle contained by r and b equals the square on y [6.16]. Thus a and b are the breadths obtained by applying these squares to the same rational straight line r.

**Step 3.** Since x is minor, the breadth a is a fourth apotome [10.100].

**Step 4.** Since x and y are commensurable in length, their squares have the ratio of a square number to a square number [10.9]. Consequently, the squares on x and y are commensurable areas [10.6].

**Step 5.** Rectangles having the same height r are to one another as their bases a and b [6.1]. Using the area equalities from Step 2, therefore, the square on x is to the square on y as a is to b. Since those squares are commensurable, a and b are commensurable in length [10.11].

**Step 6.** A straight line commensurable in length with an apotome is an apotome of the same order [10.103]. Since a is a fourth apotome, b is likewise a fourth apotome.

**Step 7.** The rectangle contained by the rational straight line r and the fourth apotome b has a minor straight line as its square-side [10.94]. By Step 2, y is precisely that square-side. Hence y is minor, as required.

**USED:** 10.100, 10.103, 10.11, 10.6, 10.9, 10.94, 6.1, 6.12, 6.16, D10.1.3
**Human refs (from References field):** 10.11, 10.13, 10.23, 10.76, 5.12, 5.16, 5.18, 6.22, D10.1.4
**Jaccard:** 0.056 — AI adds ['10.100', '10.103', '10.6', '10.9', '10.94', '6.1', '6.12', '6.16', 'D10.1.3']; Human adds ['10.13', '10.23', '10.76', '5.12', '5.16', '5.18', '6.22', 'D10.1.4']

## Proposition 10.106
**Statement:** A straight line commensurable with that which produces with a rational area a medial whole is a straight line which produces with a rational area a medial whole.

**Step 1.** Let a be a straight line which produces with a rational area a medial whole, and let b be commensurable in length with a. Fix the assigned rational straight line r [D10.1.3]. We use the square-application route: it directly converts the given kind into a fifth apotome, whose order is preserved under commensurability [10.101, 10.103].

**Step 2.** Construct x and y as third proportionals to r, a and to r, b respectively, so that r:a = a:x and r:b = b:y [6.11]. Consequently, the rectangle contained by r, x equals the square on a, and the rectangle contained by r, y equals the square on b [6.17]. Thus these rectangles are applications of the two squares to the same rational straight line r. By 10.101, x is a fifth apotome, with respect to r.

**Step 3.** Since a and b are commensurable in length, their squares have the ratio of a square number to a square number [10.9]. Therefore the squares on a and b are commensurable areas [10.6].

**Step 4.** The rectangles contained by r, x and by r, y have the same height r; hence they are to one another as x is to y [6.1]. Using their equalities with the respective squares from Step 2, we obtain (square on a):(square on b) = x:y. Since the first two areas are commensurable, x and y are commensurable in length [10.11].

**Step 5.** Since x is a fifth apotome and y is commensurable in length with x, y is also an apotome of the same order; therefore y is a fifth apotome with respect to r [10.103].

**Step 6.** The square on b equals the rectangle contained by the rational straight line r and the fifth apotome y. The side of such an area is a straight line which produces with a rational area a medial whole [10.95]. Therefore b is a straight line which produces with a rational area a medial whole, as required.

**USED:** 10.101, 10.103, 10.11, 10.6, 10.9, 10.95, 6.1, 6.11, 6.17, D10.1.3
**Human refs (from References field):** 10.77
**Jaccard:** 0.000 — AI adds ['10.101', '10.103', '10.11', '10.6', '10.9', '10.95', '6.1', '6.11', '6.17', 'D10.1.3']; Human adds ['10.77']

## Proposition 10.107
**Statement:** A straight line commensurable with that which produces with a medial area a medial whole is itself also a straight line which produces with a medial area a medial whole.

**Step 1.** Let A be a straight line which produces with a medial area a medial whole, and let B be commensurable in length with A. Choose a rational straight line r [D10.1.3]. We use the sixth-apotome route, since application of the square on A to a rational straight line directly gives this classification [10.102].

**Step 2.** Construct third proportionals u and v such that r:A = A:u and r:B = B:v [6.11]. Consequently, the rectangle contained by r and u equals the square on A, and the rectangle contained by r and v equals the square on B [6.17]. Thus u and v are the respective breadths obtained by applying these squares to r.

**Step 3.** Since A produces with a medial area a medial whole, application of its square to the rational straight line r produces a sixth apotome as breadth. Therefore u is a sixth apotome [10.102].

**Step 4.** Since A and B are commensurable in length, their squares have the ratio of a square number to a square number [10.9]. Hence their squares are commensurable areas [10.6].

**Step 5.** The rectangles contained by r,u and r,v have the same altitude r, so their areas are in the ratio u:v [6.1]. By their equalities with the respective squares in Step 2, the square on A is to the square on B as u is to v. Since those squares are commensurable, u and v are commensurable in length [10.11].

**Step 6.** A straight line commensurable in length with an apotome is an apotome of the same order; therefore v, being commensurable with the sixth apotome u, is itself a sixth apotome [10.103]. The side of the area contained by the rational straight line r and the sixth apotome v is a straight line which produces with a medial area a medial whole [10.96]. That area equals the square on B by Step 2, so B is its side. Therefore B also produces with a medial area a medial whole, as required.

**USED:** 10.102, 10.103, 10.11, 10.6, 10.9, 10.96, 6.1, 6.11, 6.17, D10.1.3
**Human refs (from References field):** 10.78
**Jaccard:** 0.000 — AI adds ['10.102', '10.103', '10.11', '10.6', '10.9', '10.96', '6.1', '6.11', '6.17', 'D10.1.3']; Human adds ['10.78']

## Proposition 10.108
**Statement:** If from a rational area a medial area be subtracted, the âsideâ of the remaining area becomes one of two irrational straight lines, either an apotome or a minor straight line.

**Step 1.** Let R be the given rational area and M the medial area subtracted from it, with M < R. Fix the assigned rational straight line r. Apply both areas to r, obtaining breadths a and b, so that R = ra and M = rb. These applications can be constructed by first making equal rectangles, then giving them the prescribed side r by a fourth proportional [1.45, 6.12, 6.16]. We choose this common-base route because it directly determines the kind of apotome bounding the remaining rectangle.

**Step 2.** Since R is rational, a is rational and commensurable in length with r [10.20]. Since M is medial, b is rational and incommensurable in length with r [10.22]. The squares on a and b are therefore both commensurable with the square on r, and hence with one another [D10.1.3, 10.12]. But a and b cannot be commensurable in length: otherwise their commensurability, together with that of a and r, would make b commensurable in length with r [10.12]. Thus a and b are rational straight lines commensurable in square only [D10.1.2].

**Step 3.** The rectangles ra and rb have the same base, so R > M implies a > b [6.1]. Put c = a − b. By 10.73, c is an apotome, whose whole is a and whose annex is b. Moreover, ra = rb + rc, so the remaining area R − M equals rc [2.1, CN3].

**Step 4.** Construct a straight line d whose square equals the excess of the square on a over the square on b [2.14]. Thus a² = b² + d². The lines d and a are either commensurable or incommensurable in length [D10.1.1]. These are the only alternatives that need to be considered, because the whole a is already commensurable in length with the rational line r.

**Step 5.** If d is commensurable in length with a, then c is a first apotome relative to r: its whole a is commensurable in length with r, and the excess of the square on its whole over the square on its annex is the square on a line commensurable in length with its whole [D10.3.1]. Consequently, the side of the area rc, and therefore of R − M, is an apotome [10.91].

**Step 6.** If d is incommensurable in length with a, then c is a fourth apotome relative to r, since its whole a is commensurable in length with r but the side of the difference of the squares is incommensurable in length with a [D10.3.4]. Consequently, the side of the area rc, and therefore of R − M, is a minor straight line [10.94].

**Step 7.** The two cases exhaust the alternatives [D10.1.1]. An apotome and a minor straight line are both irrational [10.73, 10.76]. Hence, if a medial area is subtracted from a rational area, the side of the remaining area is one of these two irrational straight lines: either an apotome or a minor straight line.

**USED:** 1.45, 10.12, 10.20, 10.22, 10.73, 10.76, 10.91, 10.94, 2.1, 2.14, 6.1, 6.12, 6.16, CN3, D10.1.1, D10.1.2, D10.1.3, D10.3.1, D10.3.4
**Human refs (from References field):** 10.13, 10.20, 10.22, 10.73, 10.91, 10.94, D10.3.1, D10.3.4
**Jaccard:** 0.350 — AI adds ['1.45', '10.12', '10.76', '2.1', '2.14', '6.1', '6.12', '6.16', 'CN3', 'D10.1.1', 'D10.1.2', 'D10.1.3']; Human adds ['10.13']

## Proposition 10.109
**Statement:** If from a medial area a rational area be subtracted, there arise two other irrational straight lines, either a first apotome of a medial straight line or a straight line which produces with a rational area a medial whole.

**Step 1.** Let M be the given medial area and R the rational area subtracted, with M > R. Let r be the assigned rational straight line. Apply M and R to r as rectangles, using 1.44 successively on triangular pieces if necessary, and call their respective breadths a and b. Thus M = ra and R = rb, where products denote rectangular areas. By 10.22, a is rational and incommensurable in length with r. By 10.20, b is rational and commensurable in length with r.

**Step 2.** Since a and b are rational, their squares are each commensurable with the square on r (D10.1.3), and therefore are commensurable with one another (10.12). Thus a and b are commensurable in square (D10.1.2). But b is commensurable in length with r, whereas a is incommensurable in length with r; consequently a and b are incommensurable in length (10.13). They are therefore commensurable in square only.

**Step 3.** The rectangles M and R have the same base r, so their breadths have the same ratio as their areas (6.1). Since M > R, we have a > b. Set d = a − b. By Step 2 and 10.73, d is an apotome, with whole a and annex b. Moreover, ra = rb + rd (2.1); hence M − R = rd (CN3). Construct the side s of a square equal to this remaining area (2.14).

**Step 4.** Construct a straight line c whose square equals the excess of the square on a over the square on b, so that a² − b² = c² (2.14). The direct path is to classify the apotome d using its annex b, already known to be commensurable in length with r. We distinguish whether c is commensurable or incommensurable in length with a; these alternatives are exhaustive (D10.1.1).

**Step 5.** If c is commensurable in length with a, then the square on the whole a exceeds the square on the annex b by the square on a straight line commensurable with a, while b is commensurable in length with r. Thus d is a second apotome (D10.3.2). Since s² = rd and r is rational, 10.92 shows that s is a first apotome of a medial straight line, which is irrational by 10.74.

**Step 6.** If c is incommensurable in length with a, the same whole and annex instead satisfy the definition of a fifth apotome (D10.3.5). Since s² = rd and r is rational, 10.95 shows that s is a straight line which produces with a rational area a medial whole, which is irrational by 10.77. Therefore the side of the area remaining when a rational area is subtracted from a medial area is either a first apotome of a medial straight line or a straight line which produces with a rational area a medial whole, as required.

**USED:** 1.44, 10.12, 10.13, 10.20, 10.22, 10.73, 10.74, 10.77, 10.92, 10.95, 2.1, 2.14, 6.1, CN3, D10.1.1, D10.1.2, D10.1.3, D10.3.2, D10.3.5
**Human refs (from References field):** 10.13, 10.73, 10.92, 10.95, D10.3.2, D10.3.5
**Jaccard:** 0.316 — AI adds ['1.44', '10.12', '10.20', '10.22', '10.74', '10.77', '2.1', '2.14', '6.1', 'CN3', 'D10.1.1', 'D10.1.2', 'D10.1.3']

## Proposition 10.110
**Statement:** If from a medial area there be subtracted a medial area incommensurable with the whole, the two remaining irrational straight lines arise, either a second apotome of a medial straight line or a straight line which produces with a medial area a medial whole.

**Step 1.** Let M be the given medial area and N the smaller medial area subtracted from it, with M and N incommensurable. Let r be the assigned rational straight line. By repeated applications of 1.44, apply M and N as rectangles to the same base r, and call their respective breadths a and b. Then M:N = a:b by 6.1. Consequently a>b, and a and b are incommensurable in length by 10.11.

**Step 2.** Since both applied areas are medial, 10.22 shows that a and b are rational straight lines, each incommensurable in length with r. Their squares are therefore each commensurable with the square on r (D10.1.3), and hence commensurable with one another (10.12). Thus a and b are commensurable in square only (D10.1.2 and Step 1).

**Step 3.** Put x=a−b. Since x is the remainder after subtracting from a rational straight line another rational straight line commensurable with it in square only, x is an apotome (10.73). Moreover, the rectangle contained by r and a equals the sum of the rectangles contained by r and b and by r and x (2.1). Therefore the rectangle contained by r and x equals M−N (CN3).

**Step 4.** Construct a straight line s whose square equals M−N, and a straight line d whose square equals the excess of the square on a over the square on b (2.14). We classify x directly by the apotome definitions, since Step 3 has already expressed the remaining area as a rectangle on a rational straight line. The exhaustive distinction is whether d is commensurable or incommensurable in length with a (D10.1.1).

**Step 5.** Suppose first that d is commensurable in length with a. The square on the whole a exceeds the square on the annex b by the square on d, and neither a nor b is commensurable in length with r. Hence x is a third apotome relative to r (D10.3.3). The side of the rectangle contained by a rational straight line and a third apotome is a second apotome of a medial straight line (10.93). Thus s is a second apotome of a medial straight line.

**Step 6.** Suppose instead that d is incommensurable in length with a. Since neither the whole a nor the annex b is commensurable in length with r, x is now a sixth apotome (D10.3.6). The side of the rectangle contained by a rational straight line and a sixth apotome is a straight line which produces with a medial area a medial whole (10.96). Thus s is a straight line of that kind.

**Step 7.** These two cases exhaust the possibilities. Therefore the side of the remaining area M−N is irrational and is either a second apotome of a medial straight line or a straight line which produces with a medial area a medial whole, as asserted (10.93, 10.96).

**USED:** 1.44, 10.11, 10.12, 10.22, 10.73, 10.93, 10.96, 2.1, 2.14, 6.1, CN3, D10.1.1, D10.1.2, D10.1.3, D10.3.3, D10.3.6
**Human refs (from References field):** 10.11, 10.22, 10.73, 10.93, 10.96, 6.1, D10.3.3, D10.3.6
**Jaccard:** 0.500 — AI adds ['1.44', '10.12', '2.1', '2.14', 'CN3', 'D10.1.1', 'D10.1.2', 'D10.1.3']

## Proposition 10.111
**Statement:** The apotome is not the same with the binomial straight line.

**Step 1.** Suppose that a straight line x is both an apotome and a binomial. Apply its square to the assigned rational straight line r, and call the resulting breadth y. By 10.60, y is a first binomial; by 10.97, it is a first apotome. We choose this square-application route because the distinguished terms of these first kinds are commensurable in length with the same rational line.

**Step 2.** Since y is a first binomial, write y = a + b, where a and b are rational straight lines commensurable in square only, and a is commensurable in length with r (10.36, D10.2.1). Since y is also a first apotome, write y = c − d, where c and d are rational straight lines commensurable in square only, and c is commensurable in length with r (10.73, D10.3.1).

**Step 3.** Adding d to the equality a + b = c − d gives c = a + b + d (CN2). Thus c > a (CN5). Put e = c − a; subtracting a gives e = b + d (CN3). Since a and c are each commensurable in length with r, they are commensurable in length with one another (10.12). Since c = a + e is commensurable with a, the converse part of 10.15 makes e commensurable with a. Consequently e is commensurable in length with r (10.12), and is therefore rational (D10.1.3).

**Step 4.** Because b and d are rational, their squares are each commensurable with the square on r, and hence with one another (D10.1.3, 10.12). Thus b and d are commensurable in square (D10.1.2). If they were incommensurable in length, their sum b + d = e would be irrational by 10.36, contradicting Step 3. Here 10.36 is the direct criterion to use because the expression under consideration is a sum of two rational straight lines. Therefore b and d are commensurable in length.

**Step 5.** By 10.15, their sum e = b + d is commensurable in length with b. But e is also commensurable in length with a, by Step 3. Hence a and b are commensurable in length with one another (10.12), contradicting their being commensurable in square only in Step 2. The supposition is therefore impossible: an apotome is not the same as a binomial straight line.

**USED:** 10.12, 10.15, 10.36, 10.60, 10.73, 10.97, CN2, CN3, CN5, D10.1.2, D10.1.3, D10.2.1, D10.3.1
**Human refs (from References field):** 10.12, 10.13, 10.15, 10.60, 10.73, 10.97, D10.2.1, D10.3.1
**Jaccard:** 0.500 — AI adds ['10.36', 'CN2', 'CN3', 'CN5', 'D10.1.2', 'D10.1.3']; Human adds ['10.13']

## Proposition 10.112
**Statement:** The square on a rational straight line applied to the binomial straight line produces as breadth an apotome the terms of which are commensurable with the terms of the binomial and moreover in the same ratio; and further the apotome so arising will have the same order as the binomial straight line.

**Step 1.** Let e be the assigned rational straight line, r the rational straight line whose square is applied, and B = a + b the given binomial, where a > b. Its terms a and b are rational and commensurable in square only (10.36). Let x be the breadth produced by the application, so that Bx = r². Here pq denotes the rectangle contained by p and q, and p² denotes the square on p (D2.1).

**Step 2.** Put c = a − b and Δ = Bc. We take the direct conjugate route: 2.5 supplies the required product identity by applying it to a straight line of length 2a, bisected into a, a and cut unequally into a + b, a − b. It gives
Δ + b² = a².
Since a² and b² are commensurable, 10.15, applied to this sum, shows that Δ and b² are commensurable. Moreover, b² and r² are each commensurable with e², since b and r are rational (D10.1.2, D10.1.3). Therefore Δ is rational and is commensurable with r² (10.12, D10.1.4).

**Step 3.** The rectangles Bc and Bx have the common side B. Consequently,
Δ : r² = Bc : Bx = c : x
by 6.1. Since Δ and r² are commensurable, c and x are commensurable in length (10.11).

**Step 4.** Construct a fourth proportional u such that
c : x = a : u
(6.12). Since a > c (CN5), it follows that u > x (5.14). Put v = u − x. In the proportion a : u = c : x, subtract the corresponding parts c and x from the wholes a and u. Since a − c = b and u − x = v, 5.19 gives
b : v = a : u.
Thus
c : x = a : u = b : v,
and, by alternation,
a : b = u : v
(5.16).

**Step 5.** Since c and x are commensurable in length, the proportions just obtained show that a and u, and likewise b and v, are commensurable in length (10.11). Their corresponding squares are therefore commensurable: 10.9 gives a ratio of square numbers between each pair of squares, and 10.6 gives their commensurability. Since a² and b² are commensurable with e², so also are u² and v² (10.12). Hence u and v are rational (D10.1.3), and they are commensurable with one another in square (10.12, D10.1.2).

**Step 6.** The original terms a and b are incommensurable in length. Since a : b = u : v, the lines u and v are likewise incommensurable in length (10.11). Therefore u and v are rational straight lines commensurable in square only. As x = u − v, 10.73 shows that x is an apotome, with whole u and annex v. Its corresponding terms are commensurable in length with a and b, and satisfy u : v = a : b, as required.

**Step 7.** It remains to determine the order. The proportional terms already obtained make 10.14 the direct applicable theorem. Applied to a : b = u : v, it shows that the square-difference condition is preserved: if a² exceeds b² by the square on a line commensurable in length with a, then u² exceeds v² by the square on a line commensurable in length with u; and the incommensurable alternative is preserved as well.

The other defining conditions are also preserved. Because a and u are commensurable in length, if a is commensurable in length with e, then u is so (10.12); if a is incommensurable in length with e, then u is so (10.13). The same reasoning applies to b and v. Thus the greater term, the lesser term, or neither term is commensurable in length with e in exactly the same cases for the binomial and the apotome.

**Step 8.** The order now follows directly from the definitions:
• When the square-difference side is commensurable with the greater term, commensurability with e of the greater term, the lesser term, or neither gives respectively the first, second, or third binomial and the first, second, or third apotome (D10.2.1, D10.3.1; D10.2.2, D10.3.2; D10.2.3, D10.3.3).
• When the square-difference side is incommensurable with the greater term, those same three cases give respectively the fourth, fifth, or sixth binomial and the fourth, fifth, or sixth apotome (D10.2.4, D10.3.4; D10.2.5, D10.3.5; D10.2.6, D10.3.6).

Consequently, the square on the rational straight line, applied to the binomial, produces an apotome whose corresponding terms are commensurable in length with the binomial’s terms and are in the same ratio, and whose order is the same as that of the binomial. This proves the proposition.

**USED:** 10.11, 10.12, 10.13, 10.14, 10.15, 10.36, 10.6, 10.73, 10.9, 2.5, 5.14, 5.16, 5.19, 6.1, 6.12, CN5, D10.1.2, D10.1.3, D10.1.4, D10.2.1, D10.2.2, D10.2.3, D10.2.4, D10.2.5, D10.2.6, D10.3.1, D10.3.2, D10.3.3, D10.3.4, D10.3.5, D10.3.6, D2.1
**Human refs (from References field):** 10.11, 10.12, 10.14, 10.15, 10.20, 10.36, 10.73, 5.11, 5.12, 5.14, 5.16, 5.17, 6.16, 6.22, D5.9
**Jaccard:** 0.205 — AI adds ['10.13', '10.6', '10.9', '2.5', '5.19', '6.1', '6.12', 'CN5', 'D10.1.2', 'D10.1.3', 'D10.1.4', 'D10.2.1', 'D10.2.2', 'D10.2.3', 'D10.2.4', 'D10.2.5', 'D10.2.6', 'D10.3.1', 'D10.3.2', 'D10.3.3', 'D10.3.4', 'D10.3.5', 'D10.3.6', 'D2.1']; Human adds ['10.20', '5.11', '5.12', '5.17', '6.16', '6.22', 'D5.9']

## Proposition 10.113
**Statement:** The square on a rational straight line, if applied to an apotome, produces as, breadth the binomial straight line the terms of which are commensurable with the terms of the apotome and in the same ratio; and further the binomial so arising has the same order as the apotome.

**Step 1.** Write R(u,v) for the rectangle contained by straight lines u,v, and u² for the square on u. Let r be the given rational straight line, t the given apotome, and x the breadth obtained by applying r² to t; thus R(t,x)=r². Write t=a−b, where a>b are rational straight lines commensurable in square only. Set c=a+b; then c is binomial. [D2.1; 10.73; 10.36]

**Step 2.** By 2.5,
R(t,c)+b²=R(a−b,a+b)+b²=a².
Here 2.5 is the natural choice: a+b and a−b are the unequal parts of a straight line whose equal halves are a,a. Since a² and b² are commensurable, 10.15, applied to the whole a² and its part b², shows that R(t,c) is commensurable with b². Moreover, because b and r are rational, their squares are each commensurable with the square on the assigned rational straight line, and therefore with one another. Hence R(t,c) is commensurable with r². [2.5; D10.1.2; D10.1.3; 10.15; 10.12]

**Step 3.** The rectangles R(t,x) and R(t,c), having the same height t, satisfy
R(t,x):R(t,c)=x:c.
Their areas are commensurable by Step 2 and R(t,x)=r². Therefore x and c are commensurable in length, and, since c is binomial, x is also binomial. The chosen route is now to apply the preceding reciprocal theorem to x, rather than to establish the six orders separately. [6.1; 10.11; 10.66]

**Step 4.** Let u>v be the binomial terms of x. Regard the same rectangle R(t,x)=r² as the square on r applied to the binomial x, with breadth t. By 10.112, this breadth is an apotome whose whole and annex are commensurable in length respectively with u and v, whose terms have the ratio u:v, and whose order is the same as that of x. Its whole and annex must be precisely a and b: by 10.79, only one rational annex commensurable in square only with the resulting whole can be annexed to the apotome t. Consequently u is commensurable in length with a, v with b, and u:v=a:b; moreover, x has the same order as t. Thus the square on the rational straight line, applied to the given apotome, produces the required binomial breadth. [D2.1; 10.112; 10.79]

**USED:** 10.11, 10.112, 10.12, 10.15, 10.36, 10.66, 10.73, 10.79, 2.5, 6.1, D10.1.2, D10.1.3, D2.1
**Human refs (from References field):** 10.11, 10.12, 10.14, 10.15, 10.20, 10.36, 10.73, 5.11, 5.14, 5.16, 5.19, 6.16, D10.1.3, D5.9
**Jaccard:** 0.286 — AI adds ['10.112', '10.66', '10.79', '2.5', '6.1', 'D10.1.2', 'D2.1']; Human adds ['10.14', '10.20', '5.11', '5.14', '5.16', '5.19', '6.16', 'D5.9']

## Proposition 10.114
**Statement:** If an area be contained by an apotome and the binomial straight line the terms of which are commensurable with the terms of the apotome and in the same ratio, the âsideâ of the area is rational.

**Step 1.** Let the given apotome be a − b, with a > b, and let the given binomial be c + d, where corresponding terms satisfy a : b = c : d, and a is commensurable in length with c, while b is commensurable in length with d. The four terms are rational straight lines by the meanings of apotome and binomial in 10.73 and 10.36. Write R(x,y) for the rectangle contained by x and y, and let S = R(a − b,c + d) be the given area (D2.1).

**Step 2.** We take the direct route of cancelling equal cross-rectangles, without distinguishing the six orders of apotomes. Since the hypothesis already supplies four proportional straight lines, 6.16 applies immediately and gives R(a,d) = R(b,c). Denote this common area by T.

**Step 3.** Put X = R(a,c) and Y = R(b,d). Splitting the rectangles along their component lengths gives
S + T + Y = R(a,c + d) = X + T
by 2.1: indeed, R(b,c + d) = T + Y, while R(a,c + d) = S + R(b,c + d). Subtracting the equal area T from both sides yields S + Y = X (CN3).

**Step 4.** Since a and c are rational and commensurable in length, X is rational; similarly, Y is rational (10.19). Let Q be the square on the assigned rational straight line. By D10.1.4, X and Y are each commensurable with Q, and therefore X and Y are commensurable with one another (10.12).

**Step 5.** Since X = S + Y and X is commensurable with Y, the converse part of 10.15 shows that S is commensurable with Y. Since Y is also commensurable with Q, it follows that S is commensurable with Q (10.12).

**Step 6.** Construct a square equal to S, and let its side be s (2.14). Its square is commensurable with Q by Step 5. Thus s is commensurable in square with the assigned rational straight line (D10.1.2), and consequently s is rational (D10.1.3). Therefore the side of the given area is rational, as required.

**USED:** 10.12, 10.15, 10.19, 10.36, 10.73, 2.1, 2.14, 6.16, CN3, D10.1.2, D10.1.3, D10.1.4, D2.1
**Human refs (from References field):** 10.11, 10.112, 10.12, 5.19, 6.1
**Jaccard:** 0.059 — AI adds ['10.15', '10.19', '10.36', '10.73', '2.1', '2.14', '6.16', 'CN3', 'D10.1.2', 'D10.1.3', 'D10.1.4', 'D2.1']; Human adds ['10.11', '10.112', '5.19', '6.1']

## Proposition 10.115
**Statement:** From a medial straight line there arise irrational straight lines infinite in number, and none of them is the same as any of the preceding.

**Step 1.** Let r be the assigned rational straight line, and let x₀ be the given medial straight line. Write x² for the square on x and xy for the rectangle contained by x and y. Construct a third proportional b to r and x₀, so that r:x₀ = x₀:b [6.11]. Then x₀² = rb [6.17]. Since x₀ is medial, it is irrational, whereas the breadth b obtained by applying its square to r is rational [10.21, 10.22].

**Step 2.** The line x₀ is neither binomial nor apotome. For, if it were binomial, applying its square to r would produce a first binomial as breadth [10.60]; this breadth would be irrational [10.36], contrary to the rationality of b. If x₀ were an apotome, the same application would produce a first apotome [10.97], again irrational [10.73]. Both conclusions contradict Step 1 and the distinction between rational and irrational lines [D10.1.3].

**Step 3.** Construct successively x₁, x₂, x₃, and so on, taking xₙ to be a mean proportional between r and xₙ₋₁ [6.13]. Thus, at every stage,

r:xₙ = xₙ:xₙ₋₁, and xₙ² = rxₙ₋₁ [6.17].

Path choice: the mean-proportional construction is used directly because it makes the preceding line exactly the breadth obtained by applying each new square to the same rational line r.

**Step 4.** Every xₙ is irrational. Indeed, suppose xₙ₋₁ is irrational. Rectangles of the same height are proportional to their bases, so Step 3 gives

xₙ²:r² = xₙ₋₁:r [6.1].

The lines xₙ₋₁ and r are incommensurable in length, since xₙ₋₁ is irrational [D10.1.3]. Hence the squares xₙ² and r² are incommensurable [10.11]. Therefore xₙ is incommensurable in square with the assigned rational line and is irrational [D10.1.2, D10.1.3]. Starting with the irrational line x₀ from Step 1, this proves the assertion at every stage.

**Step 5.** No xₙ with n ≥ 1 is medial. Otherwise, applying its square to r would give a rational breadth [10.22]. But that breadth is xₙ₋₁ by Step 3, and xₙ₋₁ is irrational by Step 4. This is impossible [D10.1.3].

**Step 6.** None of the new lines belongs to any of the twelve previously established additive or subtractive irrational kinds. To prove this successively, suppose that xₙ₋₁ is neither binomial nor apotome; Step 2 supplies the initial case.

If xₙ were binomial, first bimedial, second bimedial, major, the side of a rational plus a medial area, or the side of the sum of two medial areas, then applying its square to r would produce, respectively, a first, second, third, fourth, fifth, or sixth binomial [10.60, 10.61, 10.62, 10.63, 10.64, 10.65]. Since the breadth is xₙ₋₁, this would make xₙ₋₁ binomial, contrary to the supposition.

Likewise, if xₙ were an apotome, a first apotome of a medial straight line, a second apotome of a medial straight line, minor, that which produces with a rational area a medial whole, or that which produces with a medial area a medial whole, the breadth would be, respectively, a first, second, third, fourth, fifth, or sixth apotome [10.97, 10.98, 10.99, 10.100, 10.101, 10.102]. This would make xₙ₋₁ an apotome, again a contradiction.

In particular, xₙ is itself neither binomial nor apotome, so the argument continues to the next stage. Thus all twelve kinds are excluded for every n ≥ 1.

**Step 7.** The constructed lines are also distinct from one another and from x₀. Since x₀ is irrational, x₀ ≠ r [D10.1.3]. A mean proportional between unequal extremes lies strictly between them: otherwise, in r:xₙ = xₙ:xₙ₋₁, the comparison of r with xₙ would differ from the comparison of xₙ with xₙ₋₁, contradicting the definition of equal ratios with the first multiples taken [D5.5]. Consequently, if x₀ > r, then

x₀ > x₁ > x₂ > ⋯ > r;

and if x₀ < r, all these inequalities are reversed. No new line therefore equals any earlier line.

**Step 8.** The mean-proportional construction can be repeated beyond any prescribed finite number of stages [6.13]. Every resulting line is irrational by Step 4; none repeats an earlier line by Step 7; and none is medial or any of the twelve preceding irrational kinds by Steps 5–6. Therefore, from a medial straight line there arise irrational straight lines infinite in number, and none of them is the same as any of the preceding.

**USED:** 10.100, 10.101, 10.102, 10.11, 10.21, 10.22, 10.36, 10.60, 10.61, 10.62, 10.63, 10.64, 10.65, 10.73, 10.97, 10.98, 10.99, 6.1, 6.11, 6.13, 6.17, D10.1.2, D10.1.3, D5.5
**Human refs (from References field):** 10.20, D10.1.4
**Jaccard:** 0.000 — AI adds ['10.100', '10.101', '10.102', '10.11', '10.21', '10.22', '10.36', '10.60', '10.61', '10.62', '10.63', '10.64', '10.65', '10.73', '10.97', '10.98', '10.99', '6.1', '6.11', '6.13', '6.17', 'D10.1.2', 'D10.1.3', 'D5.5']; Human adds ['10.20', 'D10.1.4']
