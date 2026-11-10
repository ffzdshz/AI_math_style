# Book 10 of Euclid's Elements — Step-by-Step AI Proofs (Run A)

## Proposition 10.1
**Statement:** Two unequal magnitudes being set out, if from the greater there be subtracted a magnitude greater than its half, and from that which is left a magnitude greater than its half, and if this process be repeated continually, there will be left some magnitude which will be less than the lesser magnitude set out.

**Step 1.** Let A be the greater magnitude and B the lesser. We use the finite-multiple route, directly applying the definition of magnitudes having a ratio: choose a positive integer n such that nB > A. [D5.4]

**Step 2.** Perform n of the prescribed subtractions, unless a remainder less than B has already appeared. Write R₀ = A, and let Sᵢ be the magnitude removed at the ith subtraction and Rᵢ the remainder, so Rᵢ₋₁ = Sᵢ + Rᵢ. Since Sᵢ exceeds half of Rᵢ₋₁, Rᵢ is less than that half; consequently Sᵢ > Rᵢ. Also, each remainder is less than its predecessor, being a part of it. [CN3, CN5]

**Step 3.** Suppose that Rₙ is not less than B. Every preceding remainder Rᵢ is at least Rₙ, and hence, for each i from 1 through n,
Sᵢ > Rᵢ ≥ Rₙ ≥ B.
Thus each of the n removed magnitudes contains a part equal to B together with a positive excess. [CN5]

**Step 4.** Reassembling the removed magnitudes and the final remainder gives
A = S₁ + S₂ + ⋯ + Sₙ + Rₙ.
The n parts equal to B together equal nB, and they form a proper part of A because the removed magnitudes also contain positive excesses. Therefore A > nB, contrary to nB > A from Step 1. Hence Rₙ < B, unless such a remainder occurred earlier. Thus after finitely many prescribed subtractions a magnitude less than the original lesser magnitude is left, as required. [CN2, CN5, D5.4]

**USED:** CN2, CN3, CN5, D5.4
**Human refs (from References field):** D5.4
**Jaccard:** 0.250 — AI adds ['CN2', 'CN3', 'CN5']

## Proposition 10.2
**Statement:** If, when the less of two unequal magnitudes is continually subtracted in turn from the greater, that which is left never measures the one before it, the magnitudes will be incommensurable.

**Step 1.** Let A>B be the two magnitudes satisfying the hypothesis. Suppose, for a contradiction, that they are commensurable, and let E be a common measure. Since E measures B, we have E≤B<A. [D10.1.1, D5.2, CN5]

**Step 2.** Write r₀=A and r₁=B. Collect successive subtractions of the same magnitude into one stage, so that
rᵢ=qᵢrᵢ₊₁+rᵢ₊₂,
where qᵢ is a positive whole number and 0<rᵢ₊₂<rᵢ₊₁. Here qᵢrᵢ₊₁ denotes qᵢ copies of rᵢ₊₁. The hypothesis ensures that these stages continue: an exact subtraction would mean that a remainder measures the magnitude before it, contrary to the hypothesis. [Hypothesis; D5.2]

**Step 3.** E measures every remainder. Indeed, it measures r₀ and r₁. Whenever it measures rᵢ and rᵢ₊₁, both are made up of whole copies of E, as is qᵢrᵢ₊₁. Subtracting those copies from rᵢ leaves rᵢ₊₂ made up of whole copies of E. Repeating this argument proves the assertion at every stage. [D5.2, CN2, CN3]

**Step 4.** Every second remainder is less than half the earlier one. For qᵢ≥1 gives
rᵢ≥rᵢ₊₁+rᵢ₊₂,
and rᵢ₊₁>rᵢ₊₂; hence rᵢ>2rᵢ₊₂. Consequently, passing from rᵢ to rᵢ₊₂ removes more than half of rᵢ. [CN5]

**Step 5.** Choose the exhaustion route of X.1, which applies directly to these magnitudes: consider r₀,r₂,r₄,… . By Step 4, each is obtained from its predecessor by subtracting more than half. Since r₀>E, X.1 therefore guarantees that some remainder r₂ₖ is less than E. [10.1]

**Step 6.** But Step 3 shows that E measures the positive magnitude r₂ₖ. Thus r₂ₖ consists of one or more whole copies of E and cannot be less than E, a contradiction. Therefore A and B have no common measure and are incommensurable. [D5.2, CN5, D10.1.1]

**USED:** 10.1, CN2, CN3, CN5, D10.1.1, D5.2
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['10.1', 'CN2', 'CN3', 'CN5', 'D10.1.1', 'D5.2']

## Proposition 10.3
**Statement:** Given two commensurable magnitudes, to find their greatest common measure.

**Step 1.** Let A and B be the given commensurable magnitudes; thus they have a common measure. If they are equal, either is their greatest common measure. Otherwise let A be the greater. If B measures A, then B is their greatest common measure: it measures both, and no magnitude greater than B can measure B. Hence suppose that B does not measure A. [D10.1.1, D5.2, CN5]

**Step 2.** Use successive subtraction directly, since 10.2 concerns magnitudes themselves and supplies the required termination. Continually subtract the lesser magnitude from the greater, proceeding in turn with the lesser and the remainder. Stop as soon as the lesser of the two current magnitudes measures the greater. This must occur: otherwise the remainders would never measure their preceding magnitudes, and A and B would be incommensurable by 10.2, contrary to the hypothesis. Denote the terminal lesser magnitude by D and the other terminal magnitude by C; thus D measures C. [10.2, D10.1.1]

**Step 3.** The magnitude D measures both terminal magnitudes, C and D. Now reverse the finite sequence of subtractions. At any individual subtraction, a pair X, Y was replaced by X − Y, Y. If D measures X − Y and Y, then each consists of whole copies of D, so their sum X also consists of whole copies of D. Thus D measures both members of the preceding pair. Repeating this backwards shows that D measures both A and B. [D5.2, CN2]

**Step 4.** Let E be any common measure of A and B. Follow the same sequence forwards. Whenever X and Y are both measured by E, subtracting Y from X removes whole copies of E and leaves whole copies of E; hence E measures X − Y as well as Y. Consequently E measures both magnitudes at every stage, and in particular measures the terminal magnitude D. [D5.2, CN3]

**Step 5.** Since every common measure E of A and B measures D, none can be greater than D: D is either equal to E or consists of several copies of E and is greater than one such copy. Since D itself measures A and B, it is their greatest common measure. Therefore the required greatest common measure has been found. [D5.2, CN5]

**USED:** 10.2, CN2, CN3, CN5, D10.1.1, D5.2
**Human refs (from References field):** 10.2
**Jaccard:** 0.167 — AI adds ['CN2', 'CN3', 'CN5', 'D10.1.1', 'D5.2']

## Proposition 10.4
**Statement:** Given three commensurable magnitudes, to find their greatest common measure.

**Step 1.** Let the three given commensurable magnitudes be A, B, and C. There is therefore a magnitude U measuring all three. We use successive subtraction twice, because this route preserves every common measure throughout the construction. [D10.1.1]

**Step 2.** Perform successive subtraction on A and B, stopping when the smaller current magnitude measures the greater. Since A and B are commensurable, the process must terminate: otherwise they would be incommensurable by 10.2. Call the smaller magnitude at termination D. If A and B are equal, take D = A immediately. [10.2]

At every subtraction, any measure of both current magnitudes also measures their difference: removing an integral number of equal copies of that measure leaves an integral number of such copies. Thus every common measure of A and B measures D. Conversely, D measures both magnitudes of the terminal pair; reconstructing the preceding pairs by addition shows that D measures A and B. [D5.2, CN3, CN2]

**Step 3.** In particular, U measures D, and U also measures C. Hence D and C are commensurable. Perform the same successive-subtraction construction on D and C, again taking their common value immediately if they are equal. By 10.2 this construction terminates; denote its terminal measure by E. As in Step 2, subtraction shows that every common measure of D and C measures E, while reconstruction by addition shows that E measures D and C. [D10.1.1, 10.2, D5.2, CN3, CN2]

**Step 4.** Since E measures D, and D measures A and B, replacing each copy of D in A and B by its equal copies of E shows that E measures A and B. It also measures C by construction. Thus E is a common measure of all three given magnitudes. [D5.2, CN2]

**Step 5.** Let H be any common measure of A, B, and C. By Step 2, H measures D. Consequently H measures both D and C, so by Step 3 it measures E. A magnitude measuring E cannot be greater than E: it is either equal to E or one of several equal parts composing E. Therefore no common measure of A, B, and C is greater than E. Hence the constructed magnitude E is their greatest common measure, as required. [D5.2, CN5]

**USED:** 10.2, CN2, CN3, CN5, D10.1.1, D5.2
**Human refs (from References field):** 10.3
**Jaccard:** 0.000 — AI adds ['10.2', 'CN2', 'CN3', 'CN5', 'D10.1.1', 'D5.2']; Human adds ['10.3']

## Proposition 10.5
**Statement:** Commensurable magnitudes have to one another the ratio which a number has to a number.

**Step 1.** Let A and B be commensurable magnitudes. By definition, some magnitude C measures both: let A consist of a copies of C and B of b copies of C. We take this direct common-measure route because the definition supplies all that is needed; a greatest common measure is unnecessary. [D10.1.1]

**Step 2.** Form a number M consisting of 2a units and a number N consisting of 2b units. These are multitudes of units, hence numbers. Using two units for each copy of C ensures that both are numbers even when a or b is one. [D7.2]

**Step 3.** Take arbitrary positive whole-number multiplicities r and s. Then rA consists of ra copies of C, and sB consists of sb copies of C; correspondingly, rM consists of ra pairs of units, and sN consists of sb pairs of units. If ra and sb are equal, the respective wholes are equal by addition of equals. If one count is greater, the corresponding whole contains a part equal to the other whole together with additional copies, and is therefore greater. Thus rA exceeds, equals, or falls short of sB precisely as rM exceeds, equals, or falls short of sN. [CN2, CN5]

**Step 4.** Since this agreement holds for every choice of r and s, the definition of equal ratios gives A:B = M:N. Therefore commensurable magnitudes have to one another the ratio which a number has to a number. [D5.5]

**USED:** CN2, CN5, D10.1.1, D5.5, D7.2
**Human refs (from References field):** 5.22, 5.7, D7.20
**Jaccard:** 0.000 — AI adds ['CN2', 'CN5', 'D10.1.1', 'D5.5', 'D7.2']; Human adds ['5.22', '5.7', 'D7.20']

## Proposition 10.6
**Statement:** If two magnitudes have to one another the ratio which a number has to a number, the magnitudes will be commensurable.

**Step 1.** Let A and B be magnitudes such that A:B = m:n, where m and n are numbers. Regard the numerical terms as finite positive counts of units. We shall construct a common measure by performing corresponding subtractions on the magnitudes and their numerical terms. By the definition of equal ratios, taking single multiples shows that A and B have the same comparison—greater, equal, or less—as m and n. [D7.1, D7.2, D5.5]

**Step 2.** At any stage, suppose the current pairs satisfy X:Y = p:q. If p and q are unequal, interchange both pairs if necessary so that p>q; the equimultiple definition preserves equality of ratios under this interchange and gives X>Y. Then
(X−Y):Y = (p−q):q.
Here we use separando, the form of proportionality naturally suited to subtraction. Replace the two pairs by (X−Y, Y) and (p−q, q), and continue whenever the numerical terms are unequal. [D5.5, 5.17]

**Step 3.** Each subtraction leaves two positive unit-counts and strictly decreases their sum. Since the initial sum contains only finitely many units, the process must stop, and it can stop only when the numerical terms are equal. At that stage let the magnitudes be U and V. Their ratio equals the ratio of two equal numerical terms; taking single multiples in the definition of equal ratios gives U=V. [D7.2, D5.5]

**Step 4.** The magnitude U therefore measures both terminal magnitudes once. Now reverse the finite sequence of subtractions. Each reversed step restores a magnitude by adding the two current magnitudes. If these consist respectively of r and s copies of U, their sum consists of r+s copies of U. Thus U measures both magnitudes at every preceding stage, and consequently measures the original A and B. [CN2, D5.2]

**Step 5.** Magnitudes measured by the same measure are commensurable. Since U measures both A and B, the given magnitudes are commensurable, as required. [D10.1.1]

**USED:** 5.17, CN2, D10.1.1, D5.2, D5.5, D7.1, D7.2
**Human refs (from References field):** 5.11, 5.22, 5.7, 5.9, D7.20
**Jaccard:** 0.000 — AI adds ['5.17', 'CN2', 'D10.1.1', 'D5.2', 'D5.5', 'D7.1', 'D7.2']; Human adds ['5.11', '5.22', '5.7', '5.9', 'D7.20']

## Proposition 10.7
**Statement:** Incommensurable magnitudes have not to one another the ratio which a number has to a number.

**Step 1.** Let A and B be incommensurable magnitudes. By definition, they cannot have any common measure. [D10.1.1]

**Step 2.** Use 10.6 by contraposition: it is the immediately preceding proposition and directly connects a ratio of numbers with commensurability. Suppose, contrary to the assertion, that A:B = m:n for some numbers m and n. Then A and B are commensurable. [10.6]

**Step 3.** Commensurability means that A and B have a common measure, contradicting Step 1. Therefore incommensurable magnitudes have not to one another the ratio which a number has to a number. [D10.1.1]

**USED:** 10.6, D10.1.1
**Human refs (from References field):** 10.6
**Jaccard:** 0.500 — AI adds ['D10.1.1']

## Proposition 10.8
**Statement:** If two magnitudes have not to one another the ratio which a number has to a number, the magnitudes will be incommensurable.

**Step 1.** Let A and B be magnitudes whose ratio is not the ratio of a number to a number. We use the contrapositive of Proposition 10.5, since it directly connects commensurability with such a ratio. If A and B were commensurable, they would have to one another the ratio which a number has to a number, contrary to the hypothesis. Thus A and B are not commensurable. [10.5]

**Step 2.** Magnitudes measured by a common measure are commensurable, and magnitudes which cannot have any common measure are incommensurable. Since A and B are not commensurable, they cannot have any common measure; therefore they are incommensurable, as required. [D10.1.1]

**USED:** 10.5, D10.1.1
**Human refs (from References field):** 10.5
**Jaccard:** 0.500 — AI adds ['D10.1.1']

## Proposition 10.9
**Statement:** The squares on straight lines commensurable in length have to one another the ratio which a square number has to a square number; and squares which have to one another the ratio which a square number has to a square number will also have their sides commensurable in length. But the squares on straight lines incommensurable in length have not to one another the ratio which a square number has to a square number; and squares which have not to one another the ratio which a square number has to a square number will not have their sides commensurable in length either.

**Step 1.** Let A and B be straight lines, and write S(A) and S(B) for the squares on them. Squares are similar, since their angles are equal and their corresponding sides proportional (D1.22, D6.1). Suppose A and B are commensurable in length. By 10.5 there are numbers m and n such that A:B = m:n. By 6.20, S(A):S(B) is the duplicate ratio of A:B. By 8.11, m²:n² is the duplicate ratio of m:n. We use 8.11 directly because the numbers being compared are squares. Equal ratios have equal duplicate ratios, by the definition of duplicate ratio and ex aequali (D5.9, 5.22). Consequently, by 5.11,
S(A):S(B) = m²:n².
Thus squares on lines commensurable in length have the ratio of a square number to a square number.

**Step 2.** Conversely, suppose S(A):S(B) = m²:n², where m and n are numbers. Take a straight line U, and let C and D consist respectively of m and n copies of U. Then C:D = m:n: for any numbers p and q, the comparison of pC with qD is exactly the comparison of pm copies of U with qn copies, and therefore agrees with the comparison of pm with qn (D5.5). Applying the duplicate-ratio argument of Step 1 to C:D = m:n gives
S(C):S(D) = m²:n²
(6.20, 8.11, D5.9, 5.22, 5.11).

**Step 3.** The assumed ratio and Step 2 give S(A):S(B) = S(C):S(D) (5.11). We now use the converse direction of 6.22, which passes directly from proportional similar figures to their corresponding sides. Since these figures are squares, it follows that A:B = C:D. Hence A:B = m:n (5.11), and A and B are commensurable in length by 10.6. This proves the second assertion.

**Step 4.** Suppose A and B are incommensurable in length. If S(A):S(B) were the ratio of a square number to a square number, Steps 2–3 would make A and B commensurable in length. This contradicts their having no common measure (D10.1.1). Therefore their squares do not have the ratio of a square number to a square number.

**Step 5.** Finally, suppose S(A):S(B) is not the ratio of a square number to a square number. If A and B were commensurable in length, Step 1 would give precisely such a ratio, contrary to the supposition. Thus A and B have no common measure and are incommensurable in length (D10.1.1). All four assertions are proved.

**USED:** 10.5, 10.6, 5.11, 5.22, 6.20, 6.22, 8.11, D1.22, D10.1.1, D5.5, D5.9, D6.1
**Human refs (from References field):** 10.5, 10.6, 6.20, 8.11
**Jaccard:** 0.333 — AI adds ['5.11', '5.22', '6.22', 'D1.22', 'D10.1.1', 'D5.5', 'D5.9', 'D6.1']

## Proposition 10.10
**Statement:** To find two straight lines incommensurable, the one in length only, and the other in square also, with an assigned straight line.

**Step 1.** Let AB be the assigned straight line, and write S(x) for the square on a straight line x. Describe the square ABCD on AB, and join AC. Put a = AB and b = AC. Since AB = BC and angle ABC is right, the square on AC equals the two squares on AB and BC; hence S(b) = 2S(a). We choose this diagonal construction because its double-square relation leads directly to the square-ratio criterion. [1.46, P1, D1.22, 1.47]

**Step 2.** The ratio 4:8 cannot be the ratio of a square number to a square number. For 4 is square, whereas 8 is not: it lies strictly between 2·2 and 3·3. If 4:8 were a ratio of square numbers, VIII.24 would imply that 8 was square, a contradiction. [D7.18, 8.24]

**Step 3.** Since S(a):S(b) = 4:8, the squares do not have the ratio of a square number to a square number. Therefore a and b are incommensurable in length by X.9. But S(a) measures both S(a) and S(b), so a and b are commensurable in square. Thus b is incommensurable in length only with the assigned line a. [10.9, D10.1.2]

**Step 4.** Find a mean proportional c between a and b, so that a:c = c:b. Then the square on c equals the rectangle contained by a and b. [6.13, 6.17]

**Step 5.** The square on a and the rectangle contained by a and b have the same height a and respective bases a and b. Consequently, by VI.1 and the equality established in Step 4,
S(a):S(c) = a:b. [6.1]

**Step 6.** Since a and b are incommensurable in length, their ratio is not the ratio of a number to a number. The same is therefore true of S(a):S(c). By X.8 these squares are incommensurable, and hence a and c are incommensurable in square. Here X.7–8 apply directly because the incommensurable ratio a:b is already established. [10.7, 10.8, D10.1.2]

**Step 7.** Moreover, a ratio which is not the ratio of any number to any number cannot be the ratio of a square number to a square number. Thus X.9 also shows that a and c are incommensurable in length. Accordingly, b is incommensurable with the assigned straight line a in length only, while c is incommensurable with it in square also. The two required straight lines have been found. [10.9]

**USED:** 1.46, 1.47, 10.7, 10.8, 10.9, 6.1, 6.13, 6.17, 8.24, D1.22, D10.1.2, D7.18, P1
**Human refs (from References field):** 10.11, 10.6, 10.9, D5.9
**Jaccard:** 0.062 — AI adds ['1.46', '1.47', '10.7', '10.8', '6.1', '6.13', '6.17', '8.24', 'D1.22', 'D10.1.2', 'D7.18', 'P1']; Human adds ['10.11', '10.6', 'D5.9']

## Proposition 10.11
**Statement:** If four magnitudes be proportional, and the first be commensurable with the second, the third will also be commensurable with the fourth; and, if the first be incommensurable with the second, the third will also be incommensurable with the fourth.

**Step 1.** Let A, B, C, D be four magnitudes with A:B = C:D. We take the numerical-ratio route, since the given proportion allows such ratios to transfer directly between the pairs. Suppose first that A is commensurable with B. By 10.5, there are numbers m, n such that A:B = m:n. [10.5]

**Step 2.** Since C:D and m:n are both equal to A:B, they are equal to one another by 5.11. Thus C:D = m:n, and 10.6 implies that C is commensurable with D. [5.11, 10.6]

**Step 3.** Suppose instead that A is incommensurable with B. By 10.7, A:B is not the ratio of any number to any number. [10.7]

**Step 4.** Neither can C:D be the ratio of a number m to a number n: otherwise A:B = C:D and C:D = m:n would give A:B = m:n by 5.11, contrary to Step 3. Therefore, by 10.8, C is incommensurable with D. Both assertions are proved. [5.11, 10.8]

**USED:** 10.5, 10.6, 10.7, 10.8, 5.11
**Human refs (from References field):** 10.5, 10.6, 10.7, 10.8
**Jaccard:** 0.800 — AI adds ['5.11']

## Proposition 10.12
**Statement:** Magnitudes commensurable with the same magnitude are commensurable with one another also.

**Step 1.** Let A and B each be commensurable with the same magnitude C. Choose the direct numerical-ratio route, since it applies immediately to both hypotheses. By 10.5, there are numbers m, n, p, q such that A:C = m:n and C:B = p:q. [10.5]

**Step 2.** Form the numbers P = mp, Q = np, and R = nq. Since m and n multiply the same number p, we have P:Q = m:n. Since n multiplies p and q, we have Q:R = p:q. Thus the two numerical ratios have a common middle term. [7.18, 7.17]

**Step 3.** Ratios equal to the same ratio are equal to one another. Hence A:C = P:Q and C:B = Q:R. [5.11]

**Step 4.** Applying equality of ratios ex aequali to the triples A, C, B and P, Q, R gives A:B = P:R. [5.22]

**Step 5.** Therefore A and B have to one another the ratio of a number to a number, and so are commensurable by the direct criterion 10.6. Consequently, magnitudes commensurable with the same magnitude are commensurable with one another. [10.6]

**USED:** 10.5, 10.6, 5.11, 5.22, 7.17, 7.18
**Human refs (from References field):** 10.5, 10.6, 5.11, 5.22, 8.4
**Jaccard:** 0.571 — AI adds ['7.17', '7.18']; Human adds ['8.4']

## Proposition 10.13
**Statement:** If two magnitudes be commensurable, and the one of them be incommensurable with any magnitude, the remaining one will also be incommensurable with the same.

**Step 1.** Let A and B be commensurable, and let A be incommensurable with C. Suppose, for a contradiction, that B is commensurable with C. Having a common measure is symmetric, so C is then commensurable with B. [D10.1.1]

**Step 2.** A and C are therefore both commensurable with B. Hence A and C are commensurable with one another. We use the common-magnitude criterion directly, since B is already the shared magnitude. [10.12]

**Step 3.** Thus A and C have a common measure, contrary to their assumed incommensurability. Consequently B and C cannot have a common measure and are incommensurable. Therefore the remaining magnitude is also incommensurable with the same magnitude, as required. [D10.1.1]

**USED:** 10.12, D10.1.1
**Human refs (from References field):** 10.12
**Jaccard:** 0.500 — AI adds ['D10.1.1']

## Proposition 10.14
**Statement:** If four straight lines be proportional, and the square on the first be greater than the square on the second by the square on a straight line commensurable with the first, the square on the third will also be greater than the square on the fourth by  the square on a straight line commensurable with the third. And, if the square on the first be greater than the square on the second by the square on a straight line incommensurable with the first, the square on the third will also be greater than the square on the fourth by the square on a straight line in-commensurable with the third.

**Step 1.** Let the four straight lines be a, b, c, d, with a:b = c:d. Write A, B, C, D for their respective squares. Let e be the given straight line whose square E equals the excess of A over B, so A = B + E. Since squares are similar and similarly described figures, A:B = C:D. [6.22]

**Step 2.** Alternately, A:C = B:D. Since A > B, it follows that C > D. [5.16, 5.14]

**Step 3.** Place the smaller square D within C with a common corner and corresponding sides aligned. The remainder is a positive rectilineal figure. Construct a square F equal to this remainder, and let f be its side. Thus C = D + F. [2.14]

**Step 4.** We use the remainder theorem directly, because A:C = B:D compares the whole squares in the same ratio as the squares subtracted. It gives (A − B):(C − D) = A:C, or E:F = A:C. Therefore, alternately, A:E = C:F. [5.19, 5.16]

**Step 5.** Applying the converse theorem for similar and similarly described figures to these squares gives a:e = c:f. This returns directly to a proportion between the straight lines themselves. [6.22]

**Step 6.** If a is commensurable with e, then c is commensurable with f; if a is incommensurable with e, then c is incommensurable with f. In either case, the square on c exceeds the square on d by the square on f, as established in Step 3. Thus the excess square has a side commensurable with c in the first case and incommensurable with c in the second, proving both assertions. [10.11]

**USED:** 10.11, 2.14, 5.14, 5.16, 5.19, 6.22
**Human refs (from References field):** 10.11, 5.17, 5.22, 6.22
**Jaccard:** 0.250 — AI adds ['2.14', '5.14', '5.16', '5.19']; Human adds ['5.17', '5.22']

## Proposition 10.15
**Statement:** If two commensurable magnitudes be added together, the whole will also be commensurable with each of them; and, if the whole be commensurable with one of them, the original magnitudes will also be commensurable.

**Step 1.** Let A and B be the two magnitudes, and let W = A + B. We take the direct common-measure route, since the definition of commensurability supplies exactly what is needed. Suppose first that A and B are commensurable. They therefore have a common measure M; write A = mM and B = nM, where m and n count positive whole numbers of copies of M. [D10.1.1, D5.2]

**Step 2.** Adding these equalities gives W = (m + n)M. Thus M measures W as well as A and B. Consequently W is commensurable with each of A and B. [CN2, D10.1.1]

**Step 3.** Conversely, suppose W is commensurable with A. There is then a common measure N, so W = rN and A = sN for positive whole numbers r and s. Since W is the whole and A is a proper part, W > A; hence r > s. [D10.1.1, D5.2, CN5]

**Step 4.** Subtracting A = sN from W = rN gives B = (r − s)N: removing s copies of N from r copies leaves a positive whole number of copies. Therefore N measures both A and B, so A and B are commensurable. If instead W is commensurable with B, the same argument with A and B interchanged proves the same conclusion. Thus the sum of two commensurable magnitudes is commensurable with each, and commensurability of the sum with either summand implies commensurability of the original magnitudes. [CN3, D10.1.1]

**USED:** CN2, CN3, CN5, D10.1.1, D5.2
**Human refs (from References field):** D10.1.1
**Jaccard:** 0.200 — AI adds ['CN2', 'CN3', 'CN5', 'D5.2']

## Proposition 10.16
**Statement:** If two incommensurable magnitudes be added together, the whole will also be incommensurable with each of them; and, if the whole be incommensurable with one of them, the original magnitudes will also be incommensurable.

**Step 1.** Let A and B be the two magnitudes, and let S = A + B. By Definition D10.1.1, two magnitudes are incommensurable exactly when they have no common measure, that is, when they are not commensurable. We use the immediately preceding Proposition 10.15 by contraposition, since its two assertions supply precisely the required implications. [D10.1.1; 10.15]

**Step 2.** Suppose A and B are incommensurable. If S were commensurable with A, the second assertion of Proposition 10.15 would make A and B commensurable, a contradiction. The same assertion gives the same contradiction if S is assumed commensurable with B. Thus S is incommensurable with each of A and B. [10.15; D10.1.1]

**Step 3.** Conversely, suppose S is incommensurable with one of A and B. If A and B were commensurable, the first assertion of Proposition 10.15 would make S commensurable with each of them, contradicting the hypothesis. Therefore A and B are incommensurable. Both assertions are proved. [10.15; D10.1.1]

**USED:** 10.15, D10.1.1
**Human refs (from References field):** D10.1.1
**Jaccard:** 0.500 — AI adds ['10.15']

## Proposition 10.17
**Statement:** If there be two unequal straight lines, and to the greater there be applied a parallelogram equal to the fourth part of the square on the less and deficient by a square figure, and if it divide it into parts which are commensurable in length, then the square on the greater will be greater than the square on the less by the square on a straight line commensurable with the greater. And, if the square on the greater be greater than the square on the less by the square on a straight line commensurable with  the greater, and if there be applied to the greater a parallelogram equal to the fourth part of the square on the less and deficient by a square figure, it will divide it into parts which are commensurable in length.

**Step 1.** Let the greater straight line have length a and the less length b, so that a > b. Let the given application divide the greater into parts of lengths x and y. Since the deficient figure is a square, the applied parallelogram is a rectangle whose sides are the two parts. Thus, writing xy for this rectangle and t² for the square on a length t,

a = x + y,     4xy = b².
[Definitions D1.22, D2.1]

**Step 2.** We use II.5 directly, because the applied rectangle is precisely the rectangle contained by the two parts of the greater line. First, the parts cannot be equal: if x = y, II.4 gives a² = 4xy = b², contrary to a > b. Here II.4 also shows that the square on a greater positive length is greater than the square on a lesser one.

Interchange the names of the parts if necessary so that x > y, and let d = x − y. Bisect the greater line. The distance between its midpoint and its point of division is d/2. Hence II.5 gives

xy + (d/2)² = (a/2)².

By II.4, the square on twice a length is four times the square on that length. Adding four copies of the preceding equality therefore gives

4xy + d² = a²,

and consequently

a² = b² + d².     (1)
[1.10, 2.5, 2.4, CN2]

**Step 3.** Suppose first that the parts x and y are commensurable in length. Use their common measure directly: let u measure them, so that x consists of m copies of u and y of n copies, where m > n. Then a = x + y consists of m + n copies of u, while d = x − y consists of m − n copies. Thus d is commensurable in length with a. By (1), the square on the greater exceeds the square on the less by the square on this commensurable straight line d. This proves the first assertion. [D10.1.1; Step 2]

**Step 4.** Conversely, suppose that

a² = b² + c²,

where c is commensurable in length with a. For the given deficient application, Step 2 again gives a² = b² + d², where d = x − y > 0. Subtracting b² yields c² = d². Therefore c = d: otherwise II.4 would make the square on the greater of these positive lengths strictly greater. Hence a and d have a common measure u. Write a = mu and d = nu, where m > n are positive integers. [CN3, 2.4, D10.1.1]

**Step 5.** Bisect u, and call its half v. Since a = x + y and d = x − y,

2x = a + d = (m + n)u,
2y = a − d = (m − n)u.

Consequently x = (m + n)v and y = (m − n)v. Thus v measures both parts, so they are commensurable in length. This proves the converse and completes both assertions. [1.10, D10.1.1]

**USED:** 1.10, 2.4, 2.5, CN2, CN3, D1.22, D10.1.1, D2.1
**Human refs (from References field):** 10.12, 10.15, 10.6, 2.5
**Jaccard:** 0.091 — AI adds ['1.10', '2.4', 'CN2', 'CN3', 'D1.22', 'D10.1.1', 'D2.1']; Human adds ['10.12', '10.15', '10.6']

## Proposition 10.18
**Statement:** If there be two unequal straight lines, and to the greater there be applied a parallelogram equal to the fourth part of the square on the less and deficient by a square figure, and if it divide it into parts which are incommensurable, the square on the greater will be greater than the square on the less by the square on a straight line incommensurable with the greater. And, if the square on the greater be greater than the square on the less by the square on a straight line incommensurable with the greater, and if there be applied to the greater a parallelogram equal to the fourth part of the square on the less and deficient by a square figure, it divides it into parts which are incommensurable. Let A, BC be two unequal straight lines, of which BC is the greater, and to BC let there be applied a parallelogram equal to the fourth part of the square on the less, A, and deficient by a square figure.

**Step 1.** Let D be the point of division of BC, with the applied parallelogram on BD and its square defect on DC. Because the defect is a square, the applied figure is the rectangle contained by BD and DC. Thus, writing squares and rectangles as areas,
4(BD·DC) = A².
We use 10.17 by contraposition, since its two directions concern precisely this same application; first we identify the square of the excess. [D1.22, D2.1, 10.17]

**Step 2.** Bisect BC at E. The point D cannot coincide with E: otherwise the preceding area equality and the formula for the square on a doubled line would give
A² = 4BE² = BC²,
contrary to A < BC. Indeed, II.4 shows that the square on a longer line contains the square on the shorter together with positive additional areas, and therefore is greater. Let X be a straight line twice ED; since D differs from E, X is positive. [1.10, 2.4, CN5]

**Step 3.** Since BC is cut equally at E and unequally at D, II.5 gives
BD·DC + ED² = BE².
Taking four copies of these equal areas gives
4(BD·DC) + 4ED² = 4BE².
By II.4, the square on twice a line is four times the square on that line. Substituting the equality from Step 1, X = 2ED, and BC = 2BE, we obtain
A² + X² = BC².
Thus the square on BC exceeds the square on A by the square on X. [2.5, CN2, 2.4]

**Step 4.** Suppose first that BD and DC are incommensurable in length. If X were commensurable with BC, the converse direction of 10.17, applied to the equality in Step 3 and to the given parallelogram, would make BD and DC commensurable in length. This contradicts the supposition. Therefore X is incommensurable with BC, proving the first assertion. [10.17, D10.1.1]

**Step 5.** Conversely, suppose that
BC² = A² + K²,
where K is incommensurable with BC. If the given application divided BC into commensurable parts BD and DC, the forward direction of 10.17 would supply a straight line L commensurable with BC such that
BC² = A² + L².
Subtracting A² gives K² = L². Consequently K = L: if either line were greater, II.4 and the whole–part principle would make its square greater. Hence K would be commensurable with BC, a contradiction. The parts BD and DC are therefore incommensurable in length. This proves the converse and completes both assertions. [10.17, CN3, 2.4, CN5, D10.1.1]

**USED:** 1.10, 10.17, 2.4, 2.5, CN2, CN3, CN5, D1.22, D10.1.1, D2.1
**Human refs (from References field):** 10.13, 10.16, 10.17, 10.6
**Jaccard:** 0.077 — AI adds ['1.10', '2.4', '2.5', 'CN2', 'CN3', 'CN5', 'D1.22', 'D10.1.1', 'D2.1']; Human adds ['10.13', '10.16', '10.6']

## Proposition 10.19
**Statement:** The rectangle contained by rational straight lines commensurable in length is rational.

**Step 1.** Let a and b be rational straight lines commensurable in length, and let R be the rectangle contained by them. Let S be the square on a, and Q the square on the assigned rational straight line. Since a is rational, it is commensurable in square with the assigned straight line; hence S is commensurable with Q. [D10.1.3, D10.1.2]

**Step 2.** Use the direct comparison with the square on the given side a. The rectangle R and the square S have the same height a and bases b and a respectively. Therefore b : a = R : S. [6.1]

**Step 3.** Since b and a are commensurable in length, the proportion in Step 2 implies that R and S are commensurable. Proposition 10.11 is the direct choice here because it transfers commensurability through precisely this proportion. [10.11]

**Step 4.** Both R and Q are commensurable with S, so R is commensurable with Q. An area commensurable with the square on the assigned rational straight line is rational. Therefore the rectangle contained by rational straight lines commensurable in length is rational. [10.12, D10.1.4]

**USED:** 10.11, 10.12, 6.1, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 10.11, 6.1, D10.1.4
**Jaccard:** 0.500 — AI adds ['10.12', 'D10.1.2', 'D10.1.3']

## Proposition 10.20
**Statement:** If a rational area be applied to a rational straight line, it produces as breadth a straight line rational and commensurable in length with the straight line to which it is applied.

**Step 1.** Let A be the given rational area and a the rational straight line to which it is applied. Let b be the resulting breadth, so that A is the rectangle contained by a and b. Let u be the assigned rational straight line, and write S_x for the square on a straight line x. Since a is rational, S_a is commensurable with S_u; since A is rational, A is likewise commensurable with S_u. [D10.1.2, D10.1.3, D10.1.4]

**Step 2.** Therefore S_a and A are commensurable with one another, since both are commensurable with S_u. [10.12]

**Step 3.** The square S_a and the rectangle A can be regarded as having the same height a and bases a and b respectively. Hence S_a : A = a : b. The direct route is to transfer commensurability across this proportion by X.11, without introducing numerical ratios. Since S_a and A are commensurable, a and b are commensurable in length. [6.1, 10.11]

**Step 4.** Likewise, the rectangle A and the square S_b have the same height b and bases a and b respectively. Thus a : b = A : S_b. Since a and b are commensurable, A and S_b are commensurable. [6.1, 10.11]

**Step 5.** Both S_b and S_u are commensurable with A, so they are commensurable with one another. Thus b is commensurable in square with the assigned rational straight line u, and consequently b is rational. Together with Step 3, this proves that the breadth is rational and commensurable in length with the straight line to which the area is applied. [10.12, D10.1.2, D10.1.3]

**USED:** 10.11, 10.12, 6.1, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 10.11, 6.1, D10.1.4
**Jaccard:** 0.500 — AI adds ['10.12', 'D10.1.2', 'D10.1.3']

## Proposition 10.21
**Statement:** The rectangle contained by rational straight lines commensurable in square only is irrational, and the side of the square equal to it is irrational. Let the latter be called medial.

**Step 1.** Let a and b be rational straight lines commensurable in square only, and let R be the rectangle contained by them. Thus a and b are incommensurable in length. Let u be the assigned rational straight line, U the square on u, and Q the square on a. Since a is rational, Q is commensurable with U. [D10.1.2, D10.1.3]

**Step 2.** The square Q and the rectangle R can be taken with the same height a and bases a and b respectively. Therefore, by the theorem on parallelograms of equal height,
Q : R = a : b. [6.1]

**Step 3.** Since a and b are incommensurable in length, the proportion in Step 2 implies that Q and R are incommensurable. The direct proportionality criterion is the natural choice here, since the required proportion is already available and no passage through numerical ratios is needed. [10.11]

**Step 4.** Now U and Q are commensurable, while Q and R are incommensurable. Hence U and R are incommensurable. Therefore R is irrational, being incommensurable with the square on the assigned rational straight line. [10.13, D10.1.4]

**Step 5.** Construct a square equal to R, and let m be its side. Such a square exists by the construction of a square equal to a given rectilineal figure. Since R is irrational, the side of a square equal to it is irrational by definition. Thus m is irrational. Let this straight line be called **medial**. Consequently, both the rectangle contained by the given rational straight lines commensurable in square only and the side of its equal square are irrational, as required. [2.14, D10.1.4]

**USED:** 10.11, 10.13, 2.14, 6.1, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 10.11, 6.1, D10.1.4
**Jaccard:** 0.429 — AI adds ['10.13', '2.14', 'D10.1.2', 'D10.1.3']

## Proposition 10.22
**Statement:** The square on a medial straight line, if applied to a rational straight line, produces as breadth a straight line rational and incommensurable in length with that to which it is applied.

**Step 1.** Let m be a medial straight line, and let its square be applied to a rational straight line a, producing breadth b. Write S(x) for the square on x and R(x,y) for the rectangle contained by x and y. Thus R(a,b) = S(m). By the definition of medial in 10.21, there are rational straight lines u and v, commensurable in square only, such that S(m) = R(u,v); moreover, this area is irrational. We use this defining rectangle because its equality with the applied rectangle gives a proportion directly. [10.21]

**Step 2.** Let r be the assigned rational straight line. Since u, v, and a are rational, S(u), S(v), and S(a) are each commensurable with S(r). Hence S(u) and S(a) are commensurable with one another. [D10.1.2, D10.1.3, 10.12]

**Step 3.** Since R(u,v) = R(a,b), we have u : a = b : v. Because these four lines are already proportional, apply the theorem on similarly described figures directly to their squares, obtaining S(u) : S(a) = S(b) : S(v). [6.16, 6.22]

**Step 4.** Since S(u) is commensurable with S(a), the proportion in Step 3 implies that S(b) is commensurable with S(v). But S(r) is also commensurable with S(v), so S(b) is commensurable with S(r). Therefore b is rational. [10.11, 10.12, D10.1.2, D10.1.3]

**Step 5.** If b were commensurable in length with a, then, since both are rational, R(a,b) would be rational. But R(a,b) = S(m), which is irrational by Step 1. This is impossible, since a rational area is commensurable with S(r), whereas an irrational area is incommensurable with it. Therefore b is incommensurable in length with a. Thus the breadth produced is rational and incommensurable in length with the rational straight line to which the square is applied. [10.19, 10.21, D10.1.4]

**USED:** 10.11, 10.12, 10.19, 10.21, 6.16, 6.22, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 10.11, 10.13, 10.21, 6.14, 6.22, D10.1.4
**Jaccard:** 0.364 — AI adds ['10.12', '10.19', '6.16', 'D10.1.2', 'D10.1.3']; Human adds ['10.13', '6.14']

## Proposition 10.23
**Statement:** A straight line commensurable with a medial straight line is medial.

**Step 1.** Let a be a medial straight line, and let b be commensurable in length with a. Let r be the assigned rational straight line. Construct fourth proportionals u and v so that r:a = a:u and r:b = b:v. Then the rectangle contained by r,u equals the square on a, and the rectangle contained by r,v equals the square on b. We use rectangles on this common base because their areas can be compared directly through their breadths. [D10.1.3, 6.12, 6.17]

**Step 2.** Since a is medial, its square applied to the rational straight line r produces a breadth u which is rational and incommensurable in length with r. Since r is the assigned rational straight line, the squares on u and r are commensurable. [10.22, D10.1.3, D10.1.2]

**Step 3.** Since a and b are commensurable in length, their squares have the ratio of a square number to a square number, and therefore are commensurable. The rectangles with sides r,u and r,v have the same height r; hence, by the direct common-height comparison, the square on a is to the square on b as u is to v. Consequently u and v are commensurable in length. [10.9, 10.6, 6.1, 10.11]

**Step 4.** Since u and v are commensurable in length, their squares likewise have a ratio of square numbers and are commensurable. The squares on v and r are thus both commensurable with the square on u, so they are commensurable with one another. Therefore v is commensurable in square with r and is rational. [10.9, 10.6, 10.12, D10.1.2, D10.1.3]

**Step 5.** Since v is commensurable in length with u, while u is incommensurable in length with r, v is also incommensurable in length with r. Thus r and v are rational straight lines commensurable in square only. The side of the square equal to their rectangle is therefore medial. That square is the square on b, so b is medial. Hence a straight line commensurable with a medial straight line is medial. [10.13, 10.21]

**USED:** 10.11, 10.12, 10.13, 10.21, 10.22, 10.6, 10.9, 6.1, 6.12, 6.17, D10.1.2, D10.1.3
**Human refs (from References field):** 10.11, 10.13, 10.21, 10.22, 6.1, D10.1.3
**Jaccard:** 0.500 — AI adds ['10.12', '10.6', '10.9', '6.12', '6.17', 'D10.1.2']

## Proposition 10.24
**Statement:** The rectangle contained by medial straight lines commensurable in length is medial.

**Step 1.** Let a and b be medial straight lines commensurable in length, and let R be the rectangle contained by them. Construct a square on a straight line c equal to R (2.14). We choose this equal-square route because it reduces the required mediality of the area to the mediality of its square-side (10.21).

**Step 2.** The square on a and the rectangle contained by a and b have the same height a, and their bases are a and b. Consequently, by 6.1,
 a : b = (square on a) : R = (square on a) : (square on c).

**Step 3.** Since a and b are commensurable in length, 10.11, applied directly to this proportion, shows that the squares on a and c are commensurable. Thus a and c are commensurable in square (D10.1.2).

**Step 4.** Since a is medial and c is commensurable with it in square, c is medial by 10.23. Therefore R, being equal to the square on the medial straight line c, is a medial area, in the terminology of 10.21. Hence the rectangle contained by medial straight lines commensurable in length is medial.

**USED:** 10.11, 10.21, 10.23, 2.14, 6.1, D10.1.2
**Human refs (from References field):** 10.11, 10.23, 6.1
**Jaccard:** 0.500 — AI adds ['10.21', '2.14', 'D10.1.2']

## Proposition 10.25
**Statement:** The rectangle contained by medial straight lines commensurable in square only is either rational or medial.

**Step 1.** Let a and b be medial straight lines commensurable in square only, and let r be the assigned rational straight line. Write a² for the square on a and ab for the rectangle contained by a and b. By hypothesis, a² and b² are commensurable. We shall express ab as a rectangle on r and classify its other side. [D10.1.2, D10.1.3]

**Step 2.** Construct fourth proportionals c and d such that r:a = a:c and r:a = b:d. Then rc = a² and rd = ab. Thus the square on a and the required rectangle have both been applied to the same rational straight line r. [6.12, 6.16]

**Step 3.** Since a is medial, applying its square to the rational straight line r produces a rational breadth c. Consequently c² is commensurable with r². [10.22, D10.1.3]

**Step 4.** Rectangles under the same height are proportional to their bases. Hence a²:ab = a:b and rc:rd = c:d. Using the equalities in Step 2 gives a:b = c:d. Therefore the squares on these four proportional straight lines are proportional: a²:b² = c²:d². [6.1, 5.11, 6.22]

**Step 5.** Since a² and b² are commensurable, c² and d² are commensurable. Here we use preservation of commensurability under equal ratios directly, because Step 4 supplies precisely the required proportion. Also c² and r² are commensurable by Step 3; therefore d² and r² are commensurable. Thus d is rational and is commensurable in square with r. [10.11, 10.12, D10.1.2, D10.1.3]

**Step 6.** If d and r are commensurable in length, the rectangle rd contained by these rational straight lines is rational. Since ab = rd, the required rectangle is rational. [10.19]

**Step 7.** If d and r are incommensurable in length, they are commensurable in square only by Step 5. The side of the square equal to the rectangle rd is then medial; hence rd, and therefore ab, is a medial area. The two cases exhaust the possibilities. Thus the rectangle contained by medial straight lines commensurable in square only is either rational or medial. [10.21]

**USED:** 10.11, 10.12, 10.19, 10.21, 10.22, 5.11, 6.1, 6.12, 6.16, 6.22, D10.1.2, D10.1.3
**Human refs (from References field):** 10.11, 10.19, 10.21, 10.22, 5.11, 6.1, 6.17
**Jaccard:** 0.462 — AI adds ['10.12', '6.12', '6.16', '6.22', 'D10.1.2', 'D10.1.3']; Human adds ['6.17']

## Proposition 10.26
**Statement:** A medial area does not exceed a medial area by a rational area.

**Step 1.** Suppose, for a contradiction, that a medial area M exceeds a medial area N by a positive rational area R. Fix the assigned rational straight line r. Use the common-base application route, since Proposition 10.22 directly describes the resulting breadths: apply M and N to r as rectangles, with respective breadths a>b. Then a and b are rational straight lines, each incommensurable in length with r. [D10.1.3, 10.22]

**Step 2.** Place these rectangles with the same base and a common corner, and let d be the excess of a over b. Their difference is the rectangle contained by r and d, and equals R. Since R is rational and r is rational, d is rational and commensurable in length with r. [CN3, 10.20]

**Step 3.** Write u² for the square on a straight line u, and uv for the rectangle contained by u and v. Since a, b, and d are rational, their squares are all commensurable with r². Moreover, a is divided into the segments b and d, so

a² = b² + d² + 2bd.

[D10.1.2, D10.1.3, D10.1.4, 2.4]

**Step 4.** Since a² and b² are each commensurable with r², they are commensurable with one another; hence their positive difference a²−b² is also commensurable with r². Likewise, subtracting d² shows that

(a²−b²)−d² = 2bd

is commensurable with r². These deductions use the transitivity of commensurability and the converse assertion of Proposition 10.15. The area bd measures its double, so bd is commensurable with 2bd and therefore with r². Thus bd is a rational area. [10.12, 10.15, D10.1.1, D10.1.4]

**Step 5.** Use Proposition 10.20 again, since the rational rectangle bd is already applied to the rational straight line d: its breadth b must be commensurable in length with d. But d is commensurable in length with r, so b is commensurable in length with r, contradicting Step 1. Therefore a medial area does not exceed a medial area by a rational area. [10.20, 10.12, 10.22]

**USED:** 10.12, 10.15, 10.20, 10.22, 2.4, CN3, D10.1.1, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 10.11, 10.13, 10.16, 10.20, 10.22, 10.6, 2.4, D10.1.4
**Jaccard:** 0.286 — AI adds ['10.12', '10.15', 'CN3', 'D10.1.1', 'D10.1.2', 'D10.1.3']; Human adds ['10.11', '10.13', '10.16', '10.6']

## Proposition 10.27
**Statement:** To find medial straight lines commensurable in square only which contain a rational rectangle.

**Step 1.** Let a be the assigned rational straight line. By 10.10, construct b incommensurable with a in length only. Thus a and b are commensurable in square only, and b is rational. Throughout, u² denotes the square on u, and uv denotes the rectangle contained by u and v. [10.10; D10.1.2; D10.1.3]

**Step 2.** Construct a third proportional c to a and b, so that a:b = b:c. Then ac = b². [6.11; 6.17] Since b² is a rational area, regard this equality as its application to the rational straight line a. The application theorem directly gives that c is rational and commensurable in length with a. [D10.1.4; 10.20] Therefore c is incommensurable in length with b, since a is incommensurable in length with b. [10.13] Moreover, b² and c² are each commensurable with a², and hence with one another. Thus b and c are also rational straight lines commensurable in square only. [D10.1.3; 10.12; D10.1.2]

**Step 3.** Construct x as a mean proportional between a and b, and y as a mean proportional between b and c. Thus
 a:x = x:b,   b:y = y:c,
and consequently
 x² = ab,   y² = bc.
[6.13; 6.17] We use the direct medial construction: each square equals a rectangle contained by rational straight lines already shown to be commensurable in square only. Therefore both x and y are medial. [10.21]

**Step 4.** Rectangles with the common height b are proportional to their bases, so
 x²:y² = ab:bc = a:c.
[6.1] Since a and c are commensurable in length, x² and y² are commensurable. Thus x and y are commensurable in square. [10.11; D10.1.2]

**Step 5.** Again using rectangles with common height b,
 x²:b² = ab:b² = a:b,
 b²:y² = b²:bc = b:c.
[6.1] Since a:b = b:c, it follows that x²:b² = b²:y². [5.11] Proportional squares have proportional sides; hence x:b = b:y. Consequently xy = b², which is a rational area. The rectangle contained by x and y is therefore rational. [6.22; 6.17; D10.1.4]

**Step 6.** We have a:x = x:b from the construction, and x:b = b:y from Step 5. Applying ex aequali to the three-term sequences a, x, b and x, b, y gives a:b = x:y. [5.22] Since a and b are incommensurable in length, x and y are likewise incommensurable in length. [10.11] Together with Step 4, this shows that x and y are commensurable in square only. They are medial by Step 3 and contain a rational rectangle by Step 5, as required.

**USED:** 10.10, 10.11, 10.12, 10.13, 10.20, 10.21, 5.11, 5.22, 6.1, 6.11, 6.13, 6.17, 6.22, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 10.11, 10.21, 10.23, 5.16, 6.12, 6.13, 6.17
**Jaccard:** 0.211 — AI adds ['10.10', '10.12', '10.13', '10.20', '5.11', '5.22', '6.1', '6.11', '6.22', 'D10.1.2', 'D10.1.3', 'D10.1.4']; Human adds ['10.23', '5.16', '6.12']

## Proposition 10.28
**Statement:** To find medial straight lines commensurable in square only which contain a medial rectangle.

**Step 1.** The ratios 2:1, 3:1, and 3:2 are not ratios of square numbers. Indeed, if m² = kn² for k = 2 or 3, then n measures m by 8.14, which would make k an integer square, an impossibility. If m²:n² = 3:2, then (2m)² = 6n²; the same proposition would make 6 an integer square, also impossible. We choose these ratios so that the square-ratio criterion will determine the required length incommensurabilities directly. [8.14]

**Step 2.** Let u be the assigned rational straight line. Write pq for the rectangle contained by p and q, and p² for the square on p. Construct straight lines b and c such that b² = 2u² and c² = 3u², by constructing squares equal to two and three copies of u². Both b and c are rational, since their squares are commensurable with u². Moreover, each pair among u, b, c is commensurable in square, with square ratios 2:1, 3:1, and 3:2. By Step 1 and 10.9, each pair is incommensurable in length. [2.14, D10.1.2, D10.1.3, 10.9]

**Step 3.** Put t = 3u. Then t is commensurable in length with u, and t² = 9u², the latter equality following by applying the rectangle-ratio theorem twice. Thus t is rational, and t and b are commensurable in square. Since b is incommensurable in length with u, it is also incommensurable in length with t. Now construct x, y, and z so that
x² = ub, y² = tb, z² = bc.
We use the square-equal-to-a-figure construction directly because these three areas are specified. Each defining rectangle has rational sides commensurable in square only; hence x, y, and z are medial. Since z is commensurable in length with itself, its square is medial. Consequently bc = z² is a medial area. [D10.1.1, 6.1, D10.1.2, D10.1.3, 10.13, 2.14, 10.21, 10.24]

**Step 4.** The rectangles tb and ub have the common height b, so
y²:x² = tb:ub = t:u = 3:1.
Therefore x and y are commensurable in square: x² measures both squares. But 3:1 is not a ratio of square numbers, by Step 1, so x and y are incommensurable in length. Thus the medial lines x and y are commensurable in square only. [6.1, D10.1.2, 10.9]

**Step 5.** Since y²:x² = 3:1 = c²:u², the converse assertion for similar figures on proportional straight lines gives y:x = c:u. Applying the rectangle-ratio theorem,
xy:x² = y:x = c:u = bc:bu.
But x² = bu. Hence xy and bc have the same ratio to the same area, and therefore xy = bc. By Step 3, bc is medial. Accordingly, the constructed medial straight lines x and y are commensurable in square only and contain a medial rectangle, as required. [6.22, 6.1, 5.9]

**USED:** 10.13, 10.21, 10.24, 10.9, 2.14, 5.9, 6.1, 6.22, 8.14, D10.1.1, D10.1.2, D10.1.3
**Human refs (from References field):** 10.11, 10.21, 10.23, 5.16, 6.12, 6.13, 6.16, 6.17
**Jaccard:** 0.053 — AI adds ['10.13', '10.24', '10.9', '2.14', '5.9', '6.1', '6.22', '8.14', 'D10.1.1', 'D10.1.2', 'D10.1.3']; Human adds ['10.11', '10.23', '5.16', '6.12', '6.13', '6.16', '6.17']

## Proposition 10.29
**Statement:** To find two rational straight lines commensurable in square only and such that the square on the greater is greater than the square on the less by the square on a straight line commensurable in length with the greater.

**Step 1.** Use four and three equal squares: their difference will be one of those squares. Let a be the assigned rational straight line, and bisect it; call either half c. Thus a = 2c. [D10.1.3, 1.10]

**Step 2.** Describe the square on a and, within one corner, the square on c. Since the two halves of a are equal to c, II.4 gives a² = 4c². The rectilineal figure remaining after removal of the corner square therefore has area 3c². Construct a square equal to this remaining figure, and let b be its side. Then b² = 3c², and consequently a² − b² = c². In particular, a is greater than b: otherwise II.4, applied to the greater line cut at the length of the lesser, would contradict a² > b². [1.46, 2.4, 2.14]

**Step 3.** The area c² measures a² four times and b² three times. Hence a and b are commensurable in square. Since a is the assigned rational straight line, b is rational also. Here commensurability follows directly from the exhibited common measure. [D10.1.2, D10.1.3]

**Step 4.** The ratio a² : b² is 4 : 3. This cannot be the ratio of a square number to a square number: if it were, VIII.24, since 4 is square, would make 3 square also. But 3 is not square, lying strictly between 1·1 and 2·2. Therefore X.9 shows that a and b are incommensurable in length. Together with Step 3, they are commensurable in square only. [D7.18, 8.24, 10.9]

**Step 5.** By construction, c measures a twice, so c is commensurable in length with a. Since a² − b² = c², the square on the greater rational straight line a exceeds the square on the lesser rational straight line b by the square on a straight line commensurable in length with a. Thus a and b satisfy every required condition. [D10.1.1]

**USED:** 1.10, 1.46, 10.9, 2.14, 2.4, 8.24, D10.1.1, D10.1.2, D10.1.3, D7.18
**Human refs (from References field):** 1.47, 10.6, 10.9, 3.31, 5.19, D10.1.4
**Jaccard:** 0.067 — AI adds ['1.10', '1.46', '2.14', '2.4', '8.24', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D7.18']; Human adds ['1.47', '10.6', '3.31', '5.19', 'D10.1.4']

## Proposition 10.30
**Statement:** To find two rational straight lines commensurable in square only and such that the square on the greater is greater is greater than the square on the less by the square on a straight line incommensurable in length with the greater.

**Step 1.** Use the side and diagonal of a square: this makes the excess square equal to the square on the side itself. Let AB be the assigned rational straight line. Construct the square ABCD on AB, and join AC. [D10.1.3, 1.46, P1]

**Step 2.** Since ABCD is a square, AB = BC and angle ABC is right. Hence, by the theorem on right-angled triangles,
AC² = AB² + BC² = 2AB².
Thus AC is greater than AB. Moreover, the square on AB measures both squares, so AC and AB are commensurable in square directly by definition. [D1.22, 1.47, D10.1.2]

**Step 3.** The ratio 2:1 cannot be the ratio of a square number to a square number. For, if it were, there would be a mean proportional number between those square numbers. Since 4:2 is the same ratio, there would consequently be a mean proportional number between 4 and 2. Such a number, being strictly between 2 and 4, would have to be 3. But 4:3 is not equal to 3:2, because 4·2 = 8 whereas 3·3 = 9. This is a contradiction. [8.11, 8.8, 7.19]

**Step 4.** Since AC²:AB² = 2:1, Step 3 and the criterion for commensurability of the sides of squares show that AC and AB are incommensurable in length. Together with Step 2, this proves that they are commensurable in square only. Both are rational straight lines in Euclid’s sense: AB is the assigned rational line, and AC is commensurable with it in square. [10.9, D10.1.2, D10.1.3]

**Step 5.** Subtracting AB² from the equality in Step 2 gives
AC² − AB² = AB².
The straight line producing this excess square is therefore AB itself, which is incommensurable in length with the greater line AC by Step 4. Thus AC and AB are the required two rational straight lines, commensurable in square only, whose squares differ by the square on a straight line incommensurable in length with the greater. [CN3, 10.9]

**USED:** 1.46, 1.47, 10.9, 7.19, 8.11, 8.8, CN3, D1.22, D10.1.2, D10.1.3, P1
**Human refs (from References field):** 1.47, 10.6, 10.9, 3.31, 5.19
**Jaccard:** 0.143 — AI adds ['1.46', '7.19', '8.11', '8.8', 'CN3', 'D1.22', 'D10.1.2', 'D10.1.3', 'P1']; Human adds ['10.6', '3.31', '5.19']

## Proposition 10.31
**Statement:** To find two medial straight lines commensurable in square only, containing a rational rectangle, and such that the square on the greater is greater than the square on the less by the square on a straight line commensurable in length with the greater.

**Step 1.** Write u² for the square on a straight line u, and uv for the rectangle contained by u and v. Take the rational-pair route: by **10.29**, construct rational straight lines a > b, commensurable in square only, such that

a² = b² + h²,

where h is commensurable in length with a. This supplies the required square-difference condition before we pass to medial lines.

**Step 2.** Construct a third proportional c to a and b, so that a:b = b:c (**6.11**). Then ac = b² (**6.17**). Since b is rational, b² is a rational area (**D10.1.3**, **D10.1.4**). Thus applying this rational area to the rational straight line a produces the breadth c; consequently c is rational and commensurable in length with a (**10.20**).

**Step 3.** Since a and b are incommensurable in length, while c and a are commensurable in length, c and b are incommensurable in length (**10.13**). The squares on b and c are each commensurable with the square on the assigned rational straight line, and therefore with one another (**D10.1.3**, **10.12**). Hence b and c are commensurable in square only (**D10.1.2**).

**Step 4.** Construct x as a mean proportional between a and b, and y as a mean proportional between b and c (**6.13**). Thus

a:x = x:b, b:y = y:c,

and therefore x² = ab and y² = bc (**6.17**). Both pairs a, b and b, c consist of rational straight lines commensurable in square only. Accordingly, the sides x and y of the squares equal to their rectangles are medial (**10.21**).

**Step 5.** Rectangles under the same height are proportional to their bases (**6.1**). Hence, using ac = b²,

x²:y² = ab:bc = a:c = a²:ac = a²:b²

(**6.1**, **5.11**). Since a² and b² are commensurable, x² and y² are commensurable (**10.11**). Moreover, proportional squares have proportional sides, so x:y = a:b (**6.22**). Since a and b are incommensurable in length, x and y are likewise incommensurable in length (**10.11**). Thus x and y are commensurable in square only (**D10.1.2**).

**Step 6.** From a:b = x:y, alternation gives a:x = b:y (**5.16**). But a:x = x:b by the construction of x. Therefore x:b = b:y (**5.11**), and consequently xy = b² (**6.17**). The rectangle contained by x and y is therefore rational (**D10.1.4**).

**Step 7.** Apply **10.14** directly: it is the proportional-transfer result naturally suited to the established proportion a:b = x:y. Since a² exceeds b² by h², with h commensurable in length with a, it follows that x² exceeds y² by z² for a straight line z commensurable in length with x.

Thus x is the greater of two medial straight lines x, y commensurable in square only; they contain a rational rectangle, and the square on the greater exceeds the square on the less by the square on a straight line commensurable in length with the greater. This is the required construction.

**USED:** 10.11, 10.12, 10.13, 10.14, 10.20, 10.21, 10.29, 5.11, 5.16, 6.1, 6.11, 6.13, 6.17, 6.22, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 10.11, 10.14, 10.21, 10.23, 10.29, 10.30
**Jaccard:** 0.211 — AI adds ['10.12', '10.13', '10.20', '5.11', '5.16', '6.1', '6.11', '6.13', '6.17', '6.22', 'D10.1.2', 'D10.1.3', 'D10.1.4']; Human adds ['10.23', '10.30']

## Proposition 10.32
**Statement:** To find two medial straight lines commensurable in square only, containing a medial rectangle, and such that the square on the greater is greater than the square on the less by the square on a straight line commensurable with the greater.

**Step 1.** Write xy for the rectangle contained by straight lines x and y, and x² for the square on x. We use the earlier area-to-square construction rather than a mean-proportional construction, because prescribing the square areas will also prescribe their difference. Choose an assigned rational straight line u, and construct r and s such that
r² = 2u², s² = 12u².
These constructions are possible by [2.14]. The lines r and s are rational, and they are commensurable in square with u and with one another, since u² measures all three squares. [D10.1.2, D10.1.3]

**Step 2.** The lines r and u are incommensurable in length, as are s and r. Indeed, their square ratios are respectively 2:1 and 6:1, neither of which is a ratio of square numbers. To verify this numerical obstruction, suppose m² = 2n² or m² = 6n², taking m and n prime to one another by choosing their ratio in least terms. [7.22] The prime 2 must divide m. Substituting m = 2k then forces 2 to divide n as well: in the second case, 2 divides 3n² and therefore divides n. This contradicts their being prime to one another. [7.30] The asserted incommensurabilities now follow from [10.9].

**Step 3.** Construct A, B, and D so that
A² = (4u)r = 4ur, B² = (3u)r = 3ur, D² = ur. [2.14, 2.1]
The lines 4u and 3u are rational and commensurable in length with u. [D10.1.1, D10.1.3] Consequently each is incommensurable in length with r. [10.13] Their squares are respectively 16u² and 9u², while r² = 2u²; thus each is commensurable in square with r. [2.1, D10.1.2] Therefore both A and B, being the sides of squares equal to rectangles contained by rational straight lines commensurable in square only, are medial. [10.21]

**Step 4.** The area ur measures A² four times and B² three times, so A and B are commensurable in square. [D10.1.2] They are not commensurable in length. For if 4:3 were a ratio m²:n², choose m and n prime to one another. [7.22] Then 3m² = 4n², so the prime 3 divides n. Writing n = 3k gives m² = 12k², so 3 also divides m, a contradiction. [7.30] Since A²:B² = 4:3 is therefore not a ratio of square numbers, A and B are incommensurable in length. [10.9]

**Step 5.** The constructed square areas give
A² = B² + D²,
since 4ur = 3ur + ur. [2.1] In particular, A is the greater line. Moreover,
A²:D² = 4:1 = 2²:1²,
so D is commensurable in length with A. [10.9] Thus the required condition on the excess of the squares already holds.

**Step 6.** It remains to identify the rectangle AB. Since s² = (4u)(3u), rectangles of equal height give
A²:s² = (4u)r:(4u)(3u) = r:3u,
and likewise
r²:B² = r²:(3u)r = r:3u. [2.1, 6.1]
Hence A²:s² = r²:B². The squares are similar figures, so
A:s = r:B. [6.22]
Consequently the rectangle contained by the extremes equals that contained by the means:
AB = sr. [6.16]

**Step 7.** By Steps 1–2, s and r are rational straight lines commensurable in square only. Therefore sr is the square on a medial straight line, and hence is a medial area. [10.21] Since AB = sr, the rectangle contained by A and B is medial. Together with Steps 3–5, this proves that A and B are the required two medial straight lines: they are commensurable in square only, contain a medial rectangle, and satisfy A² = B² + D² with D commensurable in length with the greater line A.

**USED:** 10.13, 10.21, 10.9, 2.1, 2.14, 6.1, 6.16, 6.22, 7.22, 7.30, D10.1.1, D10.1.2, D10.1.3
**Human refs (from References field):** 10.11, 10.14, 10.21, 10.23, 10.29, 10.30, 6.16, 6.17, 6.4, 6.8
**Jaccard:** 0.095 — AI adds ['10.13', '10.9', '2.1', '2.14', '6.1', '6.22', '7.22', '7.30', 'D10.1.1', 'D10.1.2', 'D10.1.3']; Human adds ['10.11', '10.14', '10.23', '10.29', '10.30', '6.17', '6.4', '6.8']

## Proposition 10.33
**Statement:** To find two straight lines incommensurable in square which make the sum of the squares on them rational but the rectangle contained by them medial.

**Step 1.** Write p² for the square on a straight line p, and pq for the rectangle contained by p and q. By 10.30, construct rational straight lines a > b, commensurable in square only, such that a² − b² = c², where c is incommensurable in length with a. This construction is chosen because its incommensurable excess permits the converse part of 10.18 to produce an incommensurable division. [10.30]

**Step 2.** Bisect b, and call its half t. Then b = 2t and b² = 4t². Thus t² is the fourth part of b². [1.10, 2.4]

**Step 3.** To a apply a rectangle equal to t² and deficient by a square. This is possible because b < a, so t² is less than the square on half of a. Let the resulting parts of a be x and y; the square defect makes the breadth of the applied rectangle equal to the remaining part, so
x + y = a, and xy = t² = b²/4.
Since a² − b² is the square on a straight line incommensurable in length with a, the converse part of 10.18 shows that x and y are incommensurable in length. [6.28, 10.18]

**Step 4.** Construct squares equal to the rectangles ax and ay, and let their sides be u and v, respectively. Thus
u² = ax, and v² = ay.
The equal-area construction is the direct choice here, since the required conditions concern the squares on the sought lines. [2.14]

**Step 5.** Because x + y = a, the sum of these squares is
u² + v² = ax + ay = a(x + y) = a².
Since a is rational, a² is a rational area. Hence the sum of the squares on u and v is rational. [2.1, D10.1.3, D10.1.4]

**Step 6.** Rectangles having the same height are proportional to their bases; consequently,
u² : v² = ax : ay = x : y.
Since x and y are incommensurable, u² and v² are incommensurable. Therefore u and v are incommensurable in square. [6.1, 10.11, D10.1.2]

**Step 7.** Again, by comparing rectangles under the same height,
u² : a² = ax : a² = x : a,
and
t² : v² = xy : ay = x : a.
Thus u² : a² = t² : v². Since these figures are squares, their sides are proportional: u : a = t : v. Therefore the rectangle uv equals the rectangle at. [6.1, 6.22, 6.16]

**Step 8.** Since b = 2t and b² = 4t², t is commensurable with b both in length and in square. As b is rational and its square is commensurable with a², transitivity of commensurability shows that t is rational and commensurable in square with a. But a is incommensurable in length with b, so it is also incommensurable in length with t. Thus a and t are rational straight lines commensurable in square only, and their rectangle at is medial. Since uv = at, the rectangle contained by u and v is medial. Together with Steps 5 and 6, this proves that u and v are the required straight lines. [D10.1.1, D10.1.2, D10.1.3, 10.12, 10.13, 10.21]

**USED:** 1.10, 10.11, 10.12, 10.13, 10.18, 10.21, 10.30, 2.1, 2.14, 2.4, 6.1, 6.16, 6.22, 6.28, D10.1.1, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 1.47, 10.18, 10.21, 10.23, 10.30, 6.28
**Jaccard:** 0.200 — AI adds ['1.10', '10.11', '10.12', '10.13', '2.1', '2.14', '2.4', '6.1', '6.16', '6.22', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.1.4']; Human adds ['1.47', '10.23']

## Proposition 10.34
**Statement:** To find two straight lines incommensurable in square which make the sum of the squares on them medial but the rectangle contained by them rational.

**Step 1.** Write uv for the rectangle contained by straight lines u,v, and u² for the square on u. By 10.30, construct rational straight lines a>b, commensurable in square only, such that a² exceeds b² by the square on a straight line incommensurable in length with a. This choice supplies exactly the incommensurable-difference condition needed for the deficient-square division below. [10.30]

**Step 2.** Bisect a and b, and put m=b/2. Construct the square on m. Since b<a, this square is less than the square on half of a. Hence, by 6.28, apply to a a rectangle equal to m² and deficient by a square. If p,q are the resulting parts of a, the square defect makes the rectangle’s height equal to the remaining part, so
p+q=a, and pq=m²=b²/4.
The converse assertion of 10.18, applied to a,b and the condition in Step 1, shows that p and q are incommensurable in length. [1.10, 1.46, 6.28, 10.18]

**Step 3.** Construct squares equal respectively to the rectangles bp, bq, and bm, and call their sides x,y,h. Thus
x²=bp, y²=bq, and h²=bm.
These constructions are possible by 2.14. [2.14]

**Step 4.** Rectangles having the same height are proportional to their bases. Therefore
x²:y²=bp:bq=p:q.
Since p and q are incommensurable, 10.11 shows that x² and y² are incommensurable. Consequently x and y are incommensurable in square. [6.1, 10.11, D10.1.2]

**Step 5.** By distributivity of rectangles over the parts of a straight line,
x²+y²=bp+bq=b(p+q)=ba.
But a,b are rational and commensurable in square only. By 10.21, ba is the square on a medial straight line. Thus the sum of the squares on x,y is medial. [2.1, 10.21]

**Step 6.** It remains to identify their rectangle. Since pq=m², 6.17 gives
p:m=m:q.
Using rectangles with common height b, and equality of ratios, we obtain
x²:h²=bp:bm=p:m=m:q=bm:bq=h²:y².
By the converse of 6.22, applied to these squares, x:h=h:y. Hence 6.17 gives
xy=h²=bm. [6.17, 6.1, 5.11, 6.22]

**Step 7.** Since b consists of two copies of m, 2.1 gives b²=2bm. Thus bm is commensurable with b². Because b is rational, b² is commensurable with the square on the assigned rational straight line; by 10.12, bm is also commensurable with that square and is therefore a rational area. Consequently xy=bm is rational. The constructed straight lines x,y are therefore incommensurable in square, their squares have a medial sum, and their contained rectangle is rational, as required. [2.1, D10.1.3, 10.12, D10.1.4]

**USED:** 1.10, 1.46, 10.11, 10.12, 10.18, 10.21, 10.30, 2.1, 2.14, 5.11, 6.1, 6.17, 6.22, 6.28, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 1.47, 10.11, 10.18, 10.31, 10.6, 3.31, 6.28
**Jaccard:** 0.143 — AI adds ['1.10', '1.46', '10.12', '10.21', '10.30', '2.1', '2.14', '5.11', '6.1', '6.17', '6.22', 'D10.1.2', 'D10.1.3', 'D10.1.4']; Human adds ['1.47', '10.31', '10.6', '3.31']

## Proposition 10.35
**Statement:** To find two straight lines incommensurable in square which make the sum of the squares on them medial and the rectangle contained by them medial and moreover incommensurable with the sum of the squares on them.

**Step 1.** We use direct square constructions, arranging that both required medial areas are rectangles contained by rational straight lines commensurable in square only. First observe that none of the ratios 3:1, 2:1, and 6:1 is a ratio of square numbers. Indeed, square numbers have an integer mean proportional. If any of these ratios were a ratio of square numbers, 8.8 would give an integer mean proportional between, respectively, 6 and 2, 4 and 2, or 12 and 2. By 7.19 its square would respectively be 12, 8, or 24; none of these is a square number. [8.8, 7.19]

**Step 2.** Write a² for the square on a straight line a, and ab for the rectangle contained by a and b. Set out a rational straight line r. Since the construction prescribes areas, use 2.14 to construct their square sides: first construct h such that h² = 3r². Thus h > r, and h is rational and commensurable in square with r. But h and r are incommensurable in length, by Step 1 and 10.9. [2.14, D10.1.2, D10.1.3, 10.9]

**Step 3.** By bisection form positive straight lines p and q such that
p = (h + r)/2,  q = (h − r)/2.
Thus p + q = h and p − q = r. Applying 2.5 to the division of h into p and q gives
pq + (r/2)² = (h/2)²,
so pq = r²/2. Construct t such that t² = pq. Consequently r² = 2t² and h² = 6t². Hence t is rational; r and t are commensurable in square only, and h and t are likewise commensurable in square only, by Step 1 and 10.9. [1.10, 2.5, 2.14, D10.1.2, D10.1.3, 10.9]

**Step 4.** Construct straight lines x and y such that x² = rp and y² = rq. The lines p and q are incommensurable in length: a common measure of them would also measure their sum h and their difference r, contradicting Step 2. By 6.1,
x²:y² = rp:rq = p:q.
Therefore 10.11 makes x² and y² incommensurable. Thus x and y are incommensurable in square, as required. [2.14, D10.1.1, 6.1, 10.11, D10.1.2]

**Step 5.** By the distribution of a rectangle over its divided side,
S := x² + y² = rp + rq = r(p + q) = rh.
The lines r and h are rational and commensurable in square only. Hence their rectangle rh, and therefore S, is medial. [2.1, 10.21]

**Step 6.** We next show that the rectangle contained by x and y equals rt. By 6.1,
x²:r² = rp:r² = p:r,
and
t²:y² = pq:rq = p:r.
Thus x²:r² = t²:y². Applying 6.22 to these squares gives x:r = t:y, and 6.16 therefore gives
P := xy = rt.
Since r and t are rational and commensurable in square only, P is medial. [6.1, 6.22, 6.16, 10.21]

**Step 7.** Finally, by 6.1,
S:P = rh:rt = h:t.
The lines h and t are incommensurable in length by Step 3. Hence 10.11 makes S and P incommensurable. We have therefore constructed x and y incommensurable in square, with their sum of squares medial and their contained rectangle medial and incommensurable with that sum, as required. [6.1, 10.11]

**USED:** 1.10, 10.11, 10.21, 10.9, 2.1, 2.14, 2.5, 6.1, 6.16, 6.22, 7.19, 8.8, D10.1.1, D10.1.2, D10.1.3
**Human refs (from References field):** 1.47, 10.11, 10.13, 10.18, 10.32, 3.31
**Jaccard:** 0.050 — AI adds ['1.10', '10.21', '10.9', '2.1', '2.14', '2.5', '6.1', '6.16', '6.22', '7.19', '8.8', 'D10.1.1', 'D10.1.2', 'D10.1.3']; Human adds ['1.47', '10.13', '10.18', '10.32', '3.31']

## Proposition 10.36
**Statement:** If two rational straight lines commensurable in square only be added together, the whole is irrational; and let it be called binomial.

**Step 1.** Let AB and BC be the given rational straight lines, commensurable in square only, placed consecutively on the straight line AC. Let Q be the square on the assigned rational straight line, and write S and T for the squares on AB and BC. Since AB and BC are rational, both S and T are commensurable with Q. [D10.1.3, D10.1.4]

**Step 2.** Since S and T are commensurable with Q, they are commensurable with one another. Therefore their sum U = S + T is commensurable with S; and, since S is commensurable with Q, U is commensurable with Q. Thus U is a rational area. [10.12, 10.15, D10.1.4]

**Step 3.** Take the direct route through the rectangle R contained by AB and BC. Because these rational straight lines are commensurable in square only, R is irrational, hence incommensurable with Q. The area D = 2R is commensurable with R, since R measures both itself and its double. Consequently D is also incommensurable with Q. [10.21, D10.1.4, D10.1.1, 10.13]

**Step 4.** Because U is commensurable with Q whereas D is incommensurable with Q, U and D are incommensurable. Hence U + D is incommensurable with U: otherwise the converse of 10.15 would make U and D commensurable, a contradiction. We reuse 10.15 here because it already governs the addition in Step 2, rather than invoke a separate theorem about sums of incommensurables. [10.13, 10.15]

**Step 5.** By the square-of-a-sum identity, the square on AC equals the squares on AB and BC together with twice their rectangle; that is, it equals U + D. It is therefore incommensurable with U. Since U is commensurable with Q, the square on AC is also incommensurable with Q. Thus AC is irrational. Accordingly, the whole formed by adding the two given rational straight lines commensurable in square only is irrational; let it be called **binomial**. [2.4, 10.13, D10.1.4]

**USED:** 10.12, 10.13, 10.15, 10.21, 2.4, D10.1.1, D10.1.3, D10.1.4
**Human refs (from References field):** 10.11, 10.13, 10.15, 10.16, 10.6, 2.4, D10.1.4
**Jaccard:** 0.364 — AI adds ['10.12', '10.21', 'D10.1.1', 'D10.1.3']; Human adds ['10.11', '10.16', '10.6']

## Proposition 10.37
**Statement:** If two medial straight lines commensurable in square only and containing a rational rectangle be added together, the whole is irrational; and let it be called a first bimedial straight line.

**Step 1.** Let the two given medial straight lines be a and b, and let c be their sum. Fix the assigned rational straight line, and denote its square by Q. Write A and B for the squares on a and b, R for their contained rectangle, and S=A+B. By II.4, the square on c equals S+2R. We choose this direct area-commensurability route because the hypotheses already give commensurability of A and B and rationality of R. [D10.1.4, 2.4]

**Step 2.** Since a and b are commensurable in square, A and B are commensurable. Hence S is commensurable with A. But a is medial, so its square A is an irrational area and therefore incommensurable with Q. Consequently S is also incommensurable with Q. [D10.1.2, 10.15, 10.21, D10.1.4, 10.13]

**Step 3.** By hypothesis R is rational, so R is commensurable with Q. Also R measures both itself and 2R; thus R and 2R are commensurable. It follows that 2R is commensurable with Q. [D10.1.4, D10.1.1, 10.12]

**Step 4.** Since Q and 2R are commensurable, while S is incommensurable with Q, S is incommensurable with 2R. Their sum S+2R is therefore incommensurable with 2R. As 2R is commensurable with Q, this sum is also incommensurable with Q. [10.13, 10.16]

**Step 5.** The square on c equals S+2R, and is therefore incommensurable with the assigned rational square Q. Hence c is irrational. Thus the sum of the two given medial straight lines is irrational; let it be called a **first bimedial straight line**. [2.4, D10.1.4]

**USED:** 10.12, 10.13, 10.15, 10.16, 10.21, 2.4, D10.1.1, D10.1.2, D10.1.4
**Human refs (from References field):** 10.16, 10.36, 2.4, D10.1.4
**Jaccard:** 0.300 — AI adds ['10.12', '10.13', '10.15', '10.21', 'D10.1.1', 'D10.1.2']; Human adds ['10.36']

## Proposition 10.38
**Statement:** If two medial straight lines commensurable in square only and containing a medial rectangle be added together, the whole is irrational; and let it be called a second bimedial straight line.

**Step 1.** Let a and b be medial straight lines commensurable in square only, and suppose that the rectangle ab is medial. Let r be the assigned rational straight line. Apply the areas a², b², and ab to r, obtaining breadths x, y, and z respectively, so that rx = a², ry = b², and rz = ab. Each area is the square on a medial straight line, so x, y, and z are rational by X.22. Here products denote rectangles and squares denote square areas. [D10.1.3, 10.21, 10.22]

**Step 2.** Rectangles under the same height are proportional to their bases. Consequently,
 x:y = a²:b²,
 and
 x:z = a²:ab = a:b.
 Since a² and b² are commensurable, whereas a and b are incommensurable in length, X.11 shows that x and y are commensurable in length, whereas x and z are incommensurable in length. [D10.1.2, 6.1, 10.11]

**Step 3.** Put u = x + y and v = z + z. By X.15, u is commensurable in length with x, and v is commensurable in length with z. We use X.13 directly to preserve the known incommensurability under these replacements: since x and z are incommensurable, u and z are incommensurable; since v and z are commensurable, u and v are therefore incommensurable in length. [10.15, 10.13]

**Step 4.** Length-commensurable straight lines have commensurable squares: X.9 gives their squares a ratio of square numbers, and X.6 therefore gives their commensurability. Thus u² is commensurable with x², and v² with z². Since x and z are rational, their squares are commensurable with r². By X.12, both u² and v² are commensurable with r², so u and v are rational; moreover, their squares are commensurable with one another. Together with Step 3, this says that u and v are rational straight lines commensurable in square only. [10.9, 10.6, 10.12, D10.1.2, D10.1.3]

**Step 5.** Apply X.36: u + v is irrational. This is the direct path chosen because applying the areas to a common rational line has produced precisely the two rational breadths required by X.36. [10.36]

**Step 6.** By the distributive identity for rectangles and the square-of-a-sum identity,
 r(u + v) = rx + ry + rz + rz
 = a² + b² + 2ab
 = (a + b)².
 Thus applying the square on a + b to the rational straight line r produces breadth u + v. [2.1, 2.4]

**Step 7.** If a + b were rational, its square would be a rational area. By X.20, applying that area to r would produce a rational breadth. Step 6 identifies this breadth as u + v, contrary to Step 5. Therefore a + b is irrational. Let this whole be called a **second bimedial straight line**, as required. [D10.1.3, D10.1.4, 10.20]

**USED:** 10.11, 10.12, 10.13, 10.15, 10.20, 10.21, 10.22, 10.36, 10.6, 10.9, 2.1, 2.4, 6.1, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 1.44, 10.11, 10.13, 10.15, 10.20, 10.22, 10.36, 10.6, 2.4, 6.1, D10.1.4
**Jaccard:** 0.588 — AI adds ['10.12', '10.21', '10.9', '2.1', 'D10.1.2', 'D10.1.3']; Human adds ['1.44']

## Proposition 10.39
**Statement:** If two straight lines incommensurable in square which make the sum of the squares on them rational, but the rectangle contained by them medial, be added together, the whole straight line is irrational: and let it be called major.

**Step 1.** Let AB and BC be the given straight lines, incommensurable in square, laid consecutively on AC. Denote the sum of their squares by R, their contained rectangle by M, and the square on AC by T. Thus R is rational and M is medial. We take the direct route through the square on the whole: by 2.4, T = R + 2M. [2.4]

**Step 2.** Let Q be the square on the assigned rational straight line. Since R is rational, R is commensurable with Q. Since M is medial, it is an irrational area and therefore incommensurable with Q. Consequently R and M are incommensurable: apply 10.13 to the commensurable areas Q and R and the area M. [D10.1.4, 10.21, 10.13]

**Step 3.** The areas M and 2M are commensurable, since M itself measures both. The common-measure definition is the direct criterion here. Since M is incommensurable with R, it follows that 2M is also incommensurable with R. [D10.1.1, 10.13]

**Step 4.** Because R and 2M are incommensurable, their sum T is incommensurable with R. But R is commensurable with Q; hence Q is also incommensurable with T. [10.16, 10.13]

**Step 5.** Therefore the square T on AC is irrational, and its side AC is an irrational straight line. Thus the sum of the two given straight lines is irrational; let it be called **major**. [D10.1.4]

**USED:** 10.13, 10.16, 10.21, 2.4, D10.1.1, D10.1.4
**Human refs (from References field):** 10.16, 10.23, 10.33, 10.6, D10.1.4
**Jaccard:** 0.222 — AI adds ['10.13', '10.21', '2.4', 'D10.1.1']; Human adds ['10.23', '10.33', '10.6']

## Proposition 10.40
**Statement:** If two straight lines incommensurable in square which make the sum of the squares on them medial, but the rectangle contained by them rational, be added together, the whole straight line is irrational; and let it be called the side of a rational plus a medial area.

**Step 1.** Let the given straight lines AB and BC, incommensurable in square, be joined in one straight line AC. Write M for the sum of the squares on AB and BC, and R for the rectangle contained by AB and BC. By hypothesis, M is medial and R is rational. By 2.4, the square Q on AC satisfies Q = M + 2R. We take this direct area route, comparing Q with the assigned rational square. [2.4]

**Step 2.** Let U be the square on the assigned rational straight line. Since M is medial, it is an irrational area; hence M is incommensurable with U. Since R is rational, R is commensurable with U. [10.21; D10.1.4]

**Step 3.** A common measure of R and U also measures 2R. Therefore 2R is commensurable with U and is a rational area. Since U and 2R are commensurable, while U and M are incommensurable, 10.13 gives that 2R and M are incommensurable. [D10.1.1; D10.1.4; 10.13]

**Step 4.** Apply 10.16 directly to the incommensurable areas M and 2R: their sum Q is incommensurable with 2R. But 2R is commensurable with U; therefore U is also incommensurable with Q, by 10.13. [10.16; 10.13]

**Step 5.** Thus the square on AC is incommensurable with the assigned rational square, so AC is irrational. Moreover, its square is the sum of the rational area 2R and the medial area M. Let AC be called **the side of a rational plus a medial area**, as required. [D10.1.4]

**USED:** 10.13, 10.16, 10.21, 2.4, D10.1.1, D10.1.4
**Human refs (from References field):** 10.16, 10.34, D10.1.4
**Jaccard:** 0.286 — AI adds ['10.13', '10.21', '2.4', 'D10.1.1']; Human adds ['10.34']

## Proposition 10.41
**Statement:** If two straight lines incommensurable in square which make the sum of the squares on them medial, and the rectangle contained by them medial and also incommensurable with the sum of the squares on them, be added together, the whole straight line is irrational; and let it be called the   side of the sum of two medial areas.

**Step 1.** Let the given straight lines be a and b, and let L be their sum. Write S for the sum of their squares and R for the rectangle contained by them. By hypothesis, S and R are medial areas and are incommensurable with one another. By 2.4, the square on L equals S + 2R. [2.4]

**Step 2.** Choose the assigned rational straight line r. Apply S and R to r as rectangles, and denote their respective breadths by x and y; these applications can be made by applying constituent triangles successively. We choose this common-base route because 10.22 directly converts the given medial areas into rational breadths. Accordingly, x and y are rational straight lines. [D10.1.3, 1.44, 10.22]

**Step 3.** Rectangles of the same height are proportional to their bases, so S : R = x : y. Since S and R are incommensurable, x and y are incommensurable in length. Moreover, y measures both y and 2y, so these two lines are commensurable in length. Therefore x and 2y are incommensurable in length. [6.1, 10.11, D10.1.1, 10.13]

**Step 4.** Since x and y are rational, their squares are commensurable with the square on r. By 2.4, applied to a line divided into two equal parts y, the square on 2y is four times the square on y, and thus is commensurable with it. Commensurability with the same magnitude now shows that the square on 2y is commensurable with the square on r, and also with the square on x. Consequently, 2y is rational, and x and 2y are commensurable in square. Together with Step 3, they are commensurable in square only. [D10.1.3, 2.4, D10.1.1, 10.12, D10.1.2]

**Step 5.** Thus x and 2y are two rational straight lines commensurable in square only. Their sum x + 2y is therefore irrational. [10.36]

**Step 6.** Juxtaposing the rectangle of breadth x and two copies of the rectangle of breadth y gives, on the base r, a rectangle of breadth x + 2y and area S + 2R. By Step 1 this area equals the square on L. If that square were rational, its application to the rational line r would have a rational breadth by 10.20, contrary to Step 5. Hence the square on L is irrational, and its side L is irrational. Therefore the sum of the given straight lines is irrational; let it be called the **side of the sum of two medial areas**. [2.4, 10.20, D10.1.4]

**USED:** 1.44, 10.11, 10.12, 10.13, 10.20, 10.22, 10.36, 2.4, 6.1, D10.1.1, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 10.11, 10.22, 10.35, 10.36, 2.4, 6.1, D10.1.4
**Jaccard:** 0.429 — AI adds ['1.44', '10.12', '10.13', '10.20', 'D10.1.1', 'D10.1.2', 'D10.1.3']; Human adds ['10.35']

## Proposition 10.42
**Statement:** A binomial straight line is divided into its terms at one point only.

**Step 1.** Let the binomial AB be divided into its terms at C, with AC > CB. Suppose it also admits a division into terms at D, with AD > DB; thus the greater term is taken from the same end A in each division. By the definition of a binomial, AC and CB are rational straight lines commensurable in square only, and so are AD and DB. We must prove C = D. [10.36]

**Step 2.** Write U = AC² + CB² and V = AD² + DB². Each of the four squares is commensurable with the square Q on the assigned rational straight line. Consequently U and V are rational areas: commensurability with Q passes to these sums by 10.12 and 10.15. If U and V are unequal, their positive difference is also commensurable with Q, by the converse part of 10.15 and then 10.12. Half that difference is rational as well, since an area and its half are commensurable. [D10.1.3, D10.1.4, 10.12, 10.15, D10.1.1]

**Step 3.** Let R be the rectangle contained by AC and CB, and S the rectangle contained by AD and DB. Both R and S are medial areas, because their sides are rational and commensurable in square only. We compare these rectangles directly: this makes the prohibition against two medial areas differing by a rational area immediately applicable. [10.21, 10.26]

**Step 4.** Applying the square-of-a-divided-line identity to the two divisions gives
AB² = U + 2R = V + 2S.
If R and S were unequal, subtraction would therefore make their positive difference equal to half the positive difference between U and V. By Step 2 this would be a rational area. But a medial area cannot exceed another medial area by a rational area. Hence R = S. [2.4, CN3, 10.26]

**Step 5.** Bisect AB at M. Since AC > CB and AD > DB, both C and D lie between M and B. The identity for a line cut equally and unequally gives
R + MC² = AM²,
S + MD² = AM².
Because R = S, subtraction gives MC² = MD², hence MC = MD; indeed, unequal positive straight lines have unequal squares by 2.4. Since C and D lie on the same side of M, they therefore coincide. Thus the division into the greater and lesser terms is unique: a binomial straight line is divided into its terms at one point only. [1.10, 2.5, CN3, 2.4]

**USED:** 1.10, 10.12, 10.15, 10.21, 10.26, 10.36, 2.4, 2.5, CN3, D10.1.1, D10.1.3, D10.1.4
**Human refs (from References field):** 10.21, 10.36, 2.4
**Jaccard:** 0.250 — AI adds ['1.10', '10.12', '10.15', '10.26', '2.5', 'CN3', 'D10.1.1', 'D10.1.3', 'D10.1.4']

## Proposition 10.43
**Statement:** A first bimedial straight line is divided at one point only.

**Step 1.** Let AB be a first bimedial straight line, divided into its terms at C. Fix the ordering by taking the greater term from A, so AC > CB. Suppose that another point D gives such a division, with AD > DB. By 10.37, each pair consists of medial straight lines commensurable in square only, and each pair contains a rational rectangle. We use the direct medial-area comparison furnished by 10.26.

**Step 2.** We first establish that the sum of the squares on either pair of terms is medial. Write either pair as x, y. Their squares have a common area-measure U, so x² = mU and y² = nU for positive integers m, n. Take a straight line r equal to the m-th part of x, and let e consist of m+n copies of r. Then x and e are commensurable in length, being measured by r. By distributivity of rectangles, x² = m(x·r), whence x·r = U, and therefore x·e = (m+n)U = x²+y². [D10.1.1, D10.1.2, 6.9, 2.1]

**Step 3.** Since x is medial and e is commensurable with it in length, e is medial by 10.23. The rectangle x·e is consequently medial by 10.24. Thus both areas
S_C = AC²+CB² and S_D = AD²+DB²
are medial. [10.23, 10.24]

**Step 4.** Since C and D are distinct, interchange their names if necessary so that their order is A, D, C, B. Put d = CD, and denote the rectangles AC·CB and AD·DB by P_C and P_D respectively. Since DB = d+CB and AC = AD+d, distributivity and subtraction give
P_D−P_C = AD·d−d·CB = d·(AD−CB).
But AD > DB > CB, so this difference is a positive area. Call it Δ. [2.1, CN3, CN5]

**Step 5.** Both P_C and P_D are rational areas, hence are commensurable with the square on the assigned rational straight line. They are therefore commensurable with one another. Since P_D = P_C+Δ, the converse part of 10.15 shows that Δ is commensurable with P_C, and hence with the assigned square. Thus Δ is rational. Its double is also commensurable with that square and is therefore rational. [10.37, D10.1.4, 10.12, 10.15, D10.1.1]

**Step 6.** Applying 2.4 to the two divisions of AB gives
AB² = S_C+2P_C = S_D+2P_D.
Subtracting equal areas yields
S_C−S_D = 2(P_D−P_C) = 2Δ.
Thus one medial area exceeds another medial area by the positive rational area 2Δ, contrary to 10.26. The supposed second division is therefore impossible. Since the defining division exists by 10.37, a first bimedial straight line is divided into its terms at one point only, with the greater term taken from the fixed endpoint. [2.4, CN3, 10.26, 10.37]

**USED:** 10.12, 10.15, 10.23, 10.24, 10.26, 10.37, 2.1, 2.4, 6.9, CN3, CN5, D10.1.1, D10.1.2, D10.1.4
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['10.12', '10.15', '10.23', '10.24', '10.26', '10.37', '2.1', '2.4', '6.9', 'CN3', 'CN5', 'D10.1.1', 'D10.1.2', 'D10.1.4']

## Proposition 10.44
**Statement:** A second bimedial straight line is divided at one point only.

**Step 1.** Let AB be a second bimedial straight line, divided into its terms at C. Write x = AC and y = CB, with x > y. Suppose it also has such a division at D, and write x′ = AD and y′ = DB, with x′ > y′. Throughout, the division into terms is read with the greater term first. By the definition of a second bimedial, each pair consists of medial straight lines commensurable in square only and containing a medial rectangle. Thus x² and y² are commensurable, but x and y are incommensurable in length; likewise for the primed pair. We shall apply their areas to one rational straight line, thereby reducing the question directly to uniqueness of binomial terms. [10.38, D10.1.2]

**Step 2.** Choose a rational straight line r. Apply the areas x², y², and xy to r as rectangles, obtaining breadths u, v, and w, respectively:
r·u = x², r·v = y², r·w = xy.
Such breadths can be constructed by fourth proportionals. Define u′, v′, w′ similarly from x′ and y′. All six breadths are rational: the first two areas in each triple are squares on medial straight lines, and the third is a medial area, hence also equal to a square on a medial straight line. Applying each to a rational straight line gives a rational breadth. [D10.1.3, 6.12, 6.16, 10.21, 10.22]

**Step 3.** Rectangles of the same height are as their bases, so u:v = x²:y². Since x² and y² are commensurable, u and v are commensurable in length. Set U = u + v and V = 2w. Then U is commensurable in length with u, and V with w. Commensurability in length implies commensurability in square: the squares have a ratio of square numbers, and therefore are commensurable. Consequently U and V are rational, by transitivity of commensurability with the square on the assigned rational straight line. The same conclusions hold for U′ = u′ + v′ and V′ = 2w′. [6.1, 10.11, 10.15, 10.9, 10.6, 10.12, D10.1.3]

**Step 4.** Again by the ratios of rectangles, u:w = x²:xy = x:y. Hence u and w are incommensurable in length. Since U is commensurable with u and V with w, U and V are incommensurable in length. Being rational, however, they are commensurable in square. Their sum is therefore a binomial. Moreover, II.7, applied to x cut into y and x − y, gives
x² + y² = 2xy + (x − y)².
Since x > y, this shows U > V. Identically, U′ and V′ are rational straight lines commensurable in square only, and U′ > V′. [6.1, 10.11, 10.13, D10.1.3, 10.12, 10.36, 2.7]

**Step 5.** By II.4,
r·(U + V) = x² + y² + 2xy = AB²,
and likewise r·(U′ + V′) = AB². Equal rectangles on the same height have equal bases, so U + V = U′ + V′. Thus the same straight line has two divisions into binomial terms, with the greater term first. Proposition 10.42 applies directly—the earlier uniqueness result naturally reached by this area application—and gives U = U′ and V = V′. Returning to the rectangles on r, we obtain
x² + y² = x′² + y′², and 2xy = 2x′y′. [2.4, 6.1, 10.42]

**Step 6.** Subtracting the equal doubled rectangles from the equal sums of squares, II.7 gives
(x − y)² = (x′ − y′)².
Both differences are positive, so x − y = x′ − y′; unequal positive straight lines would have unequal squares by II.4. But x + y = AB = x′ + y′. Subtracting the equal differences from these equal sums gives 2y = 2y′, hence y = y′ and then x = x′. Therefore AC = AD, so C and D coincide. Thus a second bimedial straight line is divided into its terms at one point only. [2.7, 2.4, CN3]

**USED:** 10.11, 10.12, 10.13, 10.15, 10.21, 10.22, 10.36, 10.38, 10.42, 10.6, 10.9, 2.4, 2.7, 6.1, 6.12, 6.16, CN3, D10.1.2, D10.1.3
**Human refs (from References field):** 10.11, 10.13, 10.22, 10.36, 10.38, 10.6, 2.4, 6.1
**Jaccard:** 0.421 — AI adds ['10.12', '10.15', '10.21', '10.42', '10.9', '2.7', '6.12', '6.16', 'CN3', 'D10.1.2', 'D10.1.3']

## Proposition 10.45
**Statement:** A major straight line is divided at one and the same point only.

**Step 1.** Let AB be a major straight line, divided into its terms at C. Suppose it also admits such a division at D. In comparing the divisions, place the greater term first, from A; thus AC > CB and AD > DB. Write
S = AC² + CB²,  T = AD² + DB²,
P = AC·CB,  Q = AD·DB,
where squares and products denote areas. By the characterization of a major straight line, S and T are rational areas, while P and Q are medial areas. [10.39]

**Step 2.** Applying the square-of-a-sum identity to the two divisions gives
AB² = S + 2P = T + 2Q.
Thus S + 2P = T + 2Q. [2.4, CN1]

**Step 3.** Suppose P and Q are unequal; interchange the names of the divisions if necessary so that Q > P. Subtraction in the preceding equality gives
S − T = 2(Q − P),
and therefore Q − P = (S − T)/2. This area is rational. Indeed, S and T are each commensurable with the assigned rational square, so they have a common measure. Half that measure measures both S and (S − T)/2. Consequently (S − T)/2 is commensurable with S, hence with the assigned rational square, and is rational. [CN3, D10.1.1, D10.1.4, 10.12]

**Step 4.** But P and Q are medial areas, and a medial area cannot exceed another medial area by a rational area. This contradicts Step 3. Hence P = Q. This is the direct area route: the medial rectangles themselves bring the comparison immediately under 10.26. [10.26]

**Step 5.** Bisect AB at M. Since the greater term starts at A in both divisions, C and D lie on the same side of M. The equal-and-unequal division identity gives
P + MC² = AM²,
Q + MD² = AM².
Since P = Q, subtraction gives MC² = MD². Hence MC = MD: otherwise the square on the greater distance would contain the square on the lesser as a proper part and would be greater. As C and D lie on the same side of M, they therefore coincide. Thus the greater term has one uniquely determined endpoint, and a major straight line is divided at one and the same point only. [1.10, 2.5, CN3, CN5]

**USED:** 1.10, 10.12, 10.26, 10.39, 2.4, 2.5, CN1, CN3, CN5, D10.1.1, D10.1.4
**Human refs (from References field):** 10.26, 10.39
**Jaccard:** 0.182 — AI adds ['1.10', '10.12', '2.4', '2.5', 'CN1', 'CN3', 'CN5', 'D10.1.1', 'D10.1.4']

## Proposition 10.46
**Statement:** The side of a rational plus a medial area is divided at one point only.

**Step 1.** Let AB be a side of a rational plus a medial area, divided at C into its defining terms. By 10.40, AC and CB are incommensurable in square, the sum of their squares is medial, and their rectangle is rational. Suppose D is another division with these properties. In comparing divisions into terms, take the greater term from the same endpoint A, so that AC > CB and AD > DB. Write
S = AC² + CB²,  T = AD² + DB²,
P = AC·CB,  Q = AD·DB.
Thus S and T are medial areas, while P and Q are rational areas. [10.40]

**Step 2.** The areas 2P and 2Q are rational. Indeed, P and Q are commensurable with the square on the assigned rational straight line; each is also commensurable with its double, so their doubles are commensurable with that square. Consequently 2P and 2Q are commensurable with one another. If they are unequal, their positive difference is commensurable with the smaller, by the converse part of 10.15, and hence with the assigned rational square. That difference is therefore rational. [D10.1.1, D10.1.4, 10.12, 10.15]

**Step 3.** Applying 2.4 to the two divisions gives
S + 2P = AB² = T + 2Q.
If 2P > 2Q, subtraction shows that T exceeds S by the rational area 2P − 2Q. If 2Q > 2P, S exceeds T by the rational area 2Q − 2P. Either possibility contradicts 10.26, which says that a medial area cannot exceed a medial area by a rational area. Therefore P = Q. This uses 10.26 directly because the defining square sums are medial and the defining rectangles rational. [2.4, CN1, CN3, 10.26]

**Step 4.** Bisect AB at M. Since the greater term is taken from A in both divisions, C and D lie on the same side of M. By 2.5,
P + MC² = AM²,  Q + MD² = AM².
Since P = Q, subtraction gives MC² = MD², and therefore MC = MD: otherwise the square on the smaller distance would be a proper part of the square on the greater, contrary to their equality. As C and D lie on the same side of M at equal distances from it, they coincide. Thus the defining division is unique: the side of a rational plus a medial area is divided at one point only. [1.10, 2.5, CN3, CN5]

**USED:** 1.10, 10.12, 10.15, 10.26, 10.40, 2.4, 2.5, CN1, CN3, CN5, D10.1.1, D10.1.4
**Human refs (from References field):** 10.26, 10.40
**Jaccard:** 0.167 — AI adds ['1.10', '10.12', '10.15', '2.4', '2.5', 'CN1', 'CN3', 'CN5', 'D10.1.1', 'D10.1.4']

## Proposition 10.47
**Statement:** The side of the sum of two medial areas is divided at one point only.

**Step 1.** Let AB be the side of the sum of two medial areas, divided into its defining terms at C. In comparing divisions into terms, place the greater term first, from the same endpoint A. Write AC = a, CB = b, with a > b. Suppose another defining division at D gives AD = c, DB = d, with c > d. Thus a + b = c + d = AB. Put S = a² + b², P = ab, T = c² + d², and Q = cd. By the defining conditions, S and P are medial and mutually incommensurable, and so are T and Q. [10.41]

**Step 2.** We use the direct reduction to binomial uniqueness: applying medial areas to a rational straight line produces rational breadths, so the naturally applicable uniqueness result is 10.42. Choose the assigned rational straight line r and apply S, P, T, Q to it as rectangles, obtaining respective breadths u, v, w, z. Thus ru = S, rv = P, rw = T, and rz = Q. All four breadths are rational. [10.22]

**Step 3.** The lines 2v and 2z are also rational: their squares are respectively four times the squares on v and z, and hence are commensurable with those squares and therefore with the square on the assigned rational line. Consequently u and 2v are commensurable in square, as are w and 2z. [2.4; D10.1.2; D10.1.3; 10.12]

**Step 4.** Rectangles having the same height are proportional to their breadths. Hence S : P = u : v and T : Q = w : z. Since the respective areas are incommensurable, u and v are incommensurable in length, as are w and z. Since v is commensurable with 2v, and z with 2z, it follows that u and 2v are incommensurable in length, as are w and 2z. Together with Step 3, this shows that u + 2v and w + 2z are binomial straight lines, divided into their terms as indicated. [6.1; 10.11; 10.13; 10.36]

**Step 5.** The square on the whole gives
AB² = S + 2P = T + 2Q.
Applying these equal areas to the same height r therefore gives
u + 2v = w + 2z.
Moreover, applying 2.7 to the greater term a cut into b and a − b, and likewise to c cut into d and c − d, gives
S = 2P + (a − b)²,     T = 2Q + (c − d)².
Thus S > 2P and T > 2Q; consequently u > 2v and w > 2z. The two binomial divisions therefore have their greater terms in the same position. [2.4; 2.7; 6.1; CN5]

**Step 6.** A binomial straight line has only one division into its terms. Applied to the equal wholes in Step 5, this gives u = w and 2v = 2z, hence v = z. The corresponding equal-height rectangles are therefore equal, so S = T and P = Q. [10.42; 6.1]

**Step 7.** Subtracting the equal areas 2P and 2Q from the equal areas S and T, the identities in Step 5 yield
(a − b)² = (c − d)².
Their positive sides are equal, so a − b = c − d; indeed, a greater positive side would have a greater square. Combining this equality with a + b = c + d gives a = c and b = d. Hence AC = AD, and C and D coincide. Therefore the side of the sum of two medial areas is divided into its terms at one point only. [2.7; CN3; 2.4; CN5; CN2]

**USED:** 10.11, 10.12, 10.13, 10.22, 10.36, 10.41, 10.42, 2.4, 2.7, 6.1, CN2, CN3, CN5, D10.1.2, D10.1.3
**Human refs (from References field):** 10.11, 10.22, 10.36, 10.42, 2.4, 6.1
**Jaccard:** 0.400 — AI adds ['10.12', '10.13', '10.41', '2.7', 'CN2', 'CN3', 'CN5', 'D10.1.2', 'D10.1.3']

## Proposition 10.48
**Statement:** To find the first binomial straight line.

**Step 1.** Let R be the assigned rational straight line. Use 10.29 directly, since it supplies the commensurable square-difference required for the first binomial: construct rational straight lines a > b, commensurable in square only, such that a² − b² = c², where c is commensurable in length with a. Here x² denotes the square on x. We shall normalize the greater term to R. [10.29]

**Step 2.** Construct fourth proportionals S and T so that a:b = R:S and a:c = R:T. Alternately, a:R = b:S = c:T. Since a > b, it follows that R > S. [6.12, 5.16, 5.14]

**Step 3.** Since a and b are incommensurable in length, the proportion a:b = R:S shows that R and S are incommensurable in length. But proportional straight lines have proportional squares, so a²:b² = R²:S²; because a² and b² are commensurable, R² and S² are commensurable. Thus R and S are commensurable in square only, and S is rational relative to the assigned rational line R. Likewise, a:c = R:T and the commensurability of a with c show that R and T are commensurable in length. [6.22, 10.11, D10.1.3]

**Step 4.** From a:R = b:S = c:T, the squares satisfy a²:R² = b²:S² = c²:T². Subtracting the corresponding parts b² and S² from the wholes a² and R² gives
(a² − b²):(R² − S²) = a²:R².
Since a² − b² = c², this yields c²:(R² − S²) = c²:T². Magnitudes to which the same magnitude has the same ratio are equal; therefore R² − S² = T². [6.22, 5.19, 5.9]

**Step 5.** Add S to R in one straight line. Since its two terms are rational and commensurable in square only, the whole R + S is a binomial. Its greater term R is the assigned rational straight line itself, and the square on R exceeds the square on S by the square on T, which is commensurable in length with R. Consequently, by the definition, R + S is a **first binomial straight line**, as required. [10.36, D10.2.1]

**USED:** 10.11, 10.29, 10.36, 5.14, 5.16, 5.19, 5.9, 6.12, 6.22, D10.1.3, D10.2.1
**Human refs (from References field):** 10.28, 10.36, 10.6, 10.9, 5.19
**Jaccard:** 0.143 — AI adds ['10.11', '10.29', '5.14', '5.16', '5.9', '6.12', '6.22', 'D10.1.3', 'D10.2.1']; Human adds ['10.28', '10.6', '10.9']

## Proposition 10.49
**Statement:** To find the second binomial straight line.

**Step 1.** Let r be the assigned rational straight line. Use 10.29 directly, since it supplies the required commensurable square-excess; we shall normalize its lesser term to r. Thus find straight lines a > b, commensurable in square only, such that
\[a^2-b^2=c^2,\]
where c is commensurable in length with a. Here and below, x² denotes the square on x. [10.29; D10.1.3]

**Step 2.** Construct fourth proportionals A and C such that
\[b:a=r:A,\qquad b:c=r:C.\]
Alternating these proportions gives
\[a:A=b:r=c:C.\]
Since a > b, the proportion a:A = b:r gives A > r. [6.12; 5.16; 5.11; 5.14]

**Step 3.** Because b and a are incommensurable in length, the proportion b:a = r:A implies that r and A are incommensurable in length. Moreover, proportional straight lines have proportional squares, so
\[b^2:a^2=r^2:A^2.\]
The squares on b and a are commensurable; therefore the squares on r and A are commensurable. Hence A and r are commensurable in square only, and A is rational relative to the assigned rational line r. [10.11; 6.22; D10.1.2; D10.1.3]

**Step 4.** From a:A = c:C, alternation gives a:c = A:C. Since a and c are commensurable in length, A and C are likewise commensurable in length. [5.16; 10.11]

**Step 5.** Applying the theorem on proportional squares to the proportions in Step 2 gives
\[a^2:A^2=b^2:r^2,\qquad a^2:A^2=c^2:C^2.\]
Subtract the parts b² and r² from the corresponding wholes a² and A². The remainders have the same ratio as the wholes; thus, since a² − b² = c²,
\[c^2:(A^2-r^2)=a^2:A^2=c^2:C^2.\]
Magnitudes to which the same magnitude has the same ratio are equal. Consequently,
\[A^2-r^2=C^2.\]
Thus the square on A exceeds the square on r by the square on a straight line commensurable in length with A. [6.22; 5.19; 5.11; 5.9]

**Step 6.** Add A and r end to end, forming the straight line S = A + r. Its terms are rational and commensurable in square only, so S is a binomial. [10.36]

**Step 7.** The greater term is A and the lesser is r. The square-excess condition required in the definition holds by Steps 4–5, and the lesser term is commensurable in length with the assigned rational straight line, being that very line r. Therefore S is a **second binomial straight line**, as required. [D10.1.1; D10.2.1; D10.2.2]

**USED:** 10.11, 10.29, 10.36, 5.11, 5.14, 5.16, 5.19, 5.9, 6.12, 6.22, D10.1.1, D10.1.2, D10.1.3, D10.2.1, D10.2.2
**Human refs (from References field):** 10.36, 10.6, 10.9, 5.19
**Jaccard:** 0.118 — AI adds ['10.11', '10.29', '5.11', '5.14', '5.16', '5.9', '6.12', '6.22', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.2.1', 'D10.2.2']; Human adds ['10.6', '10.9']

## Proposition 10.50
**Statement:** To find the third binomial straight line.

**Step 1.** Let r be the assigned rational straight line, and construct its square S. Form rectangles consisting respectively of eight, six, and two copies of S, and construct squares equal to these rectangles. Let their sides be a, b, and c, so that
 a² = 8S, b² = 6S, c² = 2S.
Here a > b. We choose the direct prescribed-area construction because all the required conditions concern squares. [1.46, 2.14]

**Step 2.** The area S measures the squares on a, b, and r. Thus a and b are each commensurable in square with r, and are therefore rational straight lines; they are also commensurable in square with one another. [D10.1.2, D10.1.3]

**Step 3.** None of the ratios 16:2, 12:2, and 4:3 is the ratio of a square number to a square number. For between two square numbers there is a mean proportional number; and such a mean would also exist between either pair of numbers having their ratio. [8.11, 8.8] Its square would equal the product of that pair, respectively 32, 24, or 12. [7.19] But none of these is a square number: they lie strictly between the consecutive squares 25 and 36, 16 and 25, and 9 and 16, respectively.

**Step 4.** Now
 a²:r² = 8:1 = 16:2,
 b²:r² = 6:1 = 12:2,
 a²:b² = 8:6 = 4:3.
Consequently, a and b are each incommensurable in length with r, and are incommensurable in length with one another. Together with Step 2, this shows that a and b are rational straight lines commensurable in square only. [10.9]

**Step 5.** Moreover,
 a² − b² = 8S − 6S = 2S = c².
Since a²:c² = 8:2 = 16:4, the squares on a and c have the ratio of the square numbers 16 and 4. Hence a and c are commensurable in length. Thus the square on the greater term a exceeds the square on the lesser term b by the square on a straight line commensurable in length with a. [10.9]

**Step 6.** Place a and b consecutively on one straight line. Their sum is a binomial, since they are rational and commensurable in square only. [10.36] Step 5 establishes the square-difference condition governing the first three kinds of binomial, while Step 4 shows that neither term is commensurable in length with the assigned rational straight line r. Therefore a + b is a third binomial straight line. [D10.2.1, D10.2.3]

Thus the third binomial straight line has been found.

**USED:** 1.46, 10.36, 10.9, 2.14, 7.19, 8.11, 8.8, D10.1.2, D10.1.3, D10.2.1, D10.2.3
**Human refs (from References field):** 10.36, 10.6, 10.9, 5.19, 5.22
**Jaccard:** 0.143 — AI adds ['1.46', '2.14', '7.19', '8.11', '8.8', 'D10.1.2', 'D10.1.3', 'D10.2.1', 'D10.2.3']; Human adds ['10.6', '5.19', '5.22']

## Proposition 10.51
**Statement:** To find the fourth binomial straight line.

**Step 1.** Let R be the assigned rational straight line, and write x² for the square on a straight line x. Use 10.30 directly, since it supplies the square-difference condition required for the fourth binomial: construct two rational straight lines a > b, commensurable in square only, such that a² = b² + c², where c is incommensurable in length with a. We shall transfer this pair so that its greater term becomes R. [D10.1.3, 10.30]

**Step 2.** Construct a fourth proportional s to a, b, R, so that a : b = R : s. [6.12]

**Step 3.** The squares on these proportional straight lines are proportional, so a² : b² = R² : s². Since a² and b² are commensurable, R² and s² are commensurable by 10.11. But a and b are incommensurable in length, so the original proportion and the same proposition show that R and s are incommensurable in length. Thus R and s are commensurable in square only. In particular, s is rational relative to the assigned rational line R. [6.22, 10.11, D10.1.2, D10.1.3]

**Step 4.** Apply 10.14 to a : b = R : s. Since the square on a exceeds the square on b by the square on a line incommensurable in length with a, the square on R likewise exceeds the square on s by the square on a line t incommensurable in length with R. Thus R² = s² + t², and R is the greater term. [10.14]

**Step 5.** Add R and s together in one straight line. Because they are rational straight lines commensurable in square only, their sum is a binomial straight line. [10.36]

**Step 6.** Its greater term R is the assigned rational straight line itself, and hence is commensurable in length with that line. Moreover, its square exceeds the square on the lesser term s by the square on t, which is incommensurable in length with R. Therefore R + s is a fourth binomial straight line, as required. [D10.2.4]

**USED:** 10.11, 10.14, 10.30, 10.36, 6.12, 6.22, D10.1.2, D10.1.3, D10.2.4
**Human refs (from References field):** 10.6, 10.9, 5.19
**Jaccard:** 0.000 — AI adds ['10.11', '10.14', '10.30', '10.36', '6.12', '6.22', 'D10.1.2', 'D10.1.3', 'D10.2.4']; Human adds ['10.6', '10.9', '5.19']

## Proposition 10.52
**Statement:** To find the fifth binomial straight line.

**Step 1.** Let r be the assigned rational straight line. Use 10.30 directly, since it supplies precisely the incommensurable square-excess condition required for a fifth binomial. Construct rational straight lines a > b, commensurable in square only, such that
 a² = b² + c²,
where c is incommensurable in length with a. Here and below, x² denotes the square on the straight line x. [D10.1.3, 10.30]

**Step 2.** Normalize the lesser term to the assigned line r. By two applications of the construction of a fourth proportional, construct g and h such that
 b:a = r:g,     a:c = g:h.
Taking inverse ratios in the second proportion also gives c:a = h:g. [6.12, D5.13]

**Step 3.** Squares on proportional straight lines are proportional. Hence
 b²:a² = r²:g²,     c²:a² = h²:g².
Adding the corresponding antecedents gives
 (b²+c²):a² = (r²+h²):g².
But b²+c² = a², so the ratio on the left is a ratio of equality. Consequently r²+h² = g². In particular, g > r, and the excess of the square on g over the square on r is the square on h. [6.22, 5.24, 5.9]

**Step 4.** Since b and a are incommensurable in length and b:a = r:g, the lines r and g are incommensurable in length. Since b² and a² are commensurable and b²:a² = r²:g², their squares r² and g² are commensurable. Thus g and r are commensurable in square only; moreover, g is rational relative to the assigned rational line r. [10.11, D10.1.2, D10.1.3]

**Step 5.** Since a and c are incommensurable in length and a:c = g:h, the lines g and h are likewise incommensurable in length. Therefore the square on the greater term g exceeds the square on the lesser term r by the square on a straight line incommensurable in length with g. [10.11]

**Step 6.** Add g and r on one straight line. Their sum is a binomial, because its terms are rational and commensurable in square only. Its lesser term is r itself, hence is commensurable in length with the assigned rational straight line; and Step 5 establishes the required incommensurable square-excess condition. By the definition, g+r is therefore a fifth binomial straight line. Thus the required straight line has been found. [10.36, D10.2.4, D10.2.5]

**USED:** 10.11, 10.30, 10.36, 5.24, 5.9, 6.12, 6.22, D10.1.2, D10.1.3, D10.2.4, D10.2.5, D5.13
**Human refs (from References field):** 10.36, 10.6, 10.9, 5.19
**Jaccard:** 0.067 — AI adds ['10.11', '10.30', '5.24', '5.9', '6.12', '6.22', 'D10.1.2', 'D10.1.3', 'D10.2.4', 'D10.2.5', 'D5.13']; Human adds ['10.6', '10.9', '5.19']

## Proposition 10.53
**Statement:** To find the sixth binomial straight line.

**Step 1.** Let r be the assigned rational straight line, and write r² for the square on it. Use a direct square-area construction, so that the required excess will be r² itself. Construct the square on r, and form rectangles consisting respectively of three and two copies of this square. Construct squares equal to these rectangles, and call their sides a and b. Thus a² = 3r² and b² = 2r², with a > b. [1.46, 2.14]

**Step 2.** None of the numerical ratios 6:2, 4:2, and 3:2 is a ratio of square numbers. For between two square numbers there is a mean proportional number; consequently, if any of these three ratios were a ratio of square numbers, a mean proportional number would also exist between its displayed terms. The square of that mean would respectively be 12, 8, or 6, whereas none of these is a square number. [8.11, 8.8, 7.19]

**Step 3.** The area r² measures both a² and b². Hence a and b are each commensurable in square with r, and are therefore rational straight lines; they are also commensurable in square with one another. But

a²:r² = 3:1 = 6:2,
b²:r² = 2:1 = 4:2,
a²:b² = 3:2.

By Step 2 and the criterion for commensurability in length, neither a nor b is commensurable in length with r, and a and b are incommensurable in length with one another. Thus a and b are rational straight lines commensurable in square only. [D10.1.2, D10.1.3, 10.9]

**Step 4.** Place a and b consecutively on one straight line. Since they are rational and commensurable in square only, their sum a + b is a binomial straight line. [10.36]

**Step 5.** The square on its greater term exceeds the square on its lesser term by

a² − b² = 3r² − 2r² = r².

The side of this excess square is r, which is incommensurable in length with the greater term a by Step 3. Moreover, neither term is commensurable in length with the assigned rational straight line r. These are precisely the defining conditions of a sixth binomial. Therefore a + b is the required sixth binomial straight line. [D10.2.4, D10.2.6]

**USED:** 1.46, 10.36, 10.9, 2.14, 7.19, 8.11, 8.8, D10.1.2, D10.1.3, D10.2.4, D10.2.6
**Human refs (from References field):** 10.36, 10.6, 10.9, 5.19, 5.22
**Jaccard:** 0.143 — AI adds ['1.46', '2.14', '7.19', '8.11', '8.8', 'D10.1.2', 'D10.1.3', 'D10.2.4', 'D10.2.6']; Human adds ['10.6', '5.19', '5.22']

## Proposition 10.54
**Statement:** If an area be contained by a rational straight line and the first binomial, the âsideâ of the area is the irrational straight line which is called binomial.

**Step 1.** Let r be the rational straight line set out, and let a+b be the given first binomial, where a>b. Here products denote rectangular areas and squares denote square areas. By the definition of a first binomial, a and b are rational and commensurable in square only, a is commensurable in length with r, and a²=b²+c² for some c commensurable in length with a. We shall construct two rational straight lines, commensurable in square only, whose sum has square r(a+b). [D10.2.1, 10.36]

**Step 2.** Bisect b, writing h=b/2. Since b<a, the square h² is less than the square on half of a. Apply to a a rectangle equal to h² and deficient by a square. This divides a into positive parts u and v satisfying
u+v=a, uv=h².
Use X.17 here because its commensurable-excess hypothesis is precisely the distinguishing condition of the first binomial: since a²−b²=c² and c is commensurable with a, the parts u and v are commensurable in length. [1.10, 6.28, 10.17]

**Step 3.** Since u and v are commensurable, their sum a is commensurable with each. Since a is commensurable with r, both u and v are commensurable with r. Rectangles under the same height satisfy
ru:r²=u:r, rv:r²=v:r.
Consequently ru and rv are each commensurable with r², and hence are rational areas. [10.15, 10.12, 6.1, 10.11, D10.1.4]

**Step 4.** Construct squares equal to ru and rv, and call their sides x and y. Thus
x²=ru, y²=rv.
Because these squares are rational, x and y are rational straight lines. Moreover, their squares are commensurable with the same square r², and therefore with one another: x and y are commensurable in square. [2.14, D10.1.3, D10.1.2, 10.12]

**Step 5.** We now identify the rectangle xy. Using uv=h² and rectangles under the same height,
x²:r²=ru:r²=u:r,
h²:y²=uv:rv=u:r.
Thus x²:r²=h²:y². Since squares are similar figures, their sides are proportional: x:r=h:y. Equality of the corresponding rectangles gives xy=rh. As b=2h, it follows that
2xy=rb. [6.1, 5.11, 6.22, 6.16, 2.1]

**Step 6.** The lines a and b are incommensurable in length, whereas a and r are commensurable in length; hence r and b are incommensurable in length. Being rational, they are nevertheless commensurable in square. Their rectangle rb is therefore irrational. If x and y were commensurable in length, their rectangle xy would be rational, since both lines are rational. Its double would also be rational: any common measure of xy and r² measures 2xy as well. This contradicts 2xy=rb. Thus x and y are incommensurable in length and, by Step 4, commensurable in square only. [10.13, 10.12, D10.1.2, 10.21, 10.19, D10.1.1, D10.1.4]

**Step 7.** The square on their sum is
(x+y)²=x²+y²+2xy=ru+rv+rb=r(u+v+b)=r(a+b).
Thus x+y is the side of a square equal to the given area. Since x and y are rational straight lines commensurable in square only, their sum is irrational and is called binomial. Therefore the side of the area contained by the rational straight line and the first binomial is a binomial, as required. [2.4, 2.1, 10.36]

**USED:** 1.10, 10.11, 10.12, 10.13, 10.15, 10.17, 10.19, 10.21, 10.36, 2.1, 2.14, 2.4, 5.11, 6.1, 6.16, 6.22, 6.28, D10.1.1, D10.1.2, D10.1.3, D10.1.4, D10.2.1
**Human refs (from References field):** 10.11, 10.12, 10.13, 10.15, 10.17, 10.19, 10.36, 2.14, 6.1, 6.17, D10.2.1
**Jaccard:** 0.435 — AI adds ['1.10', '10.21', '2.1', '2.4', '5.11', '6.16', '6.22', '6.28', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.1.4']; Human adds ['6.17']

## Proposition 10.55
**Statement:** If an area be contained by a rational straight line and the second binomial, the âsideâ of the area is the irrational straight line which is called a first bimedial.

**Step 1.** Let r be the rational straight line set out, and let a+b, with a>b, be the second binomial. Write products for rectangles and squares for square areas. By the definition of the second binomial, a and b are rational and commensurable in square only, b is commensurable in length with r, and there is a straight line c commensurable in length with a such that a²−b²=c². Consequently a is incommensurable in length with r. [10.36, D10.2.1, D10.2.2, 10.13]

**Step 2.** We use the defining square difference directly to split the greater term. Put
x=(a+c)/2, y=(a−c)/2, and h=b/2.
Since 0<c<a, both x and y are positive, and x+y=a. By II.5 and the square identity II.4,
xy=(a²−c²)/4=b²/4=h².
Moreover, x, y, and a are commensurable in length: if a=md and c=nd for a common measure d and positive integers m>n, then d/2 measures all three. [1.10, 2.5, 2.4, D10.1.1]

**Step 3.** Since x and y are commensurable in length with a, their squares are commensurable with a²; since a is rational, they are therefore commensurable with r². Thus x and y are rational. But each is incommensurable in length with r, because each is commensurable with a, which is incommensurable with r. Construct straight lines u and v such that u²=rx and v²=ry. Each rectangle is contained by rational straight lines commensurable in square only; hence u and v are medial, and their squares are irrational areas. [10.9, 10.6, 10.12, D10.1.3, 10.13, 2.14, 10.21]

**Step 4.** Rectangles under the same height are as their bases, so
u²:v²=rx:ry=x:y.
Since x and y are commensurable in length, u² and v² are commensurable. Thus u and v are commensurable in square. [6.1, 10.11, D10.1.2]

**Step 5.** We next show that uv=rh. Construct a fourth proportional k so that r:u=v:k; then rk=uv. Using rectangles under the same height gives
x:k=rx:rk=u²:uv=u:v,
and
k:y=rk:ry=uv:v²=u:v.
Therefore x:k=k:y, whence k²=xy by VI.17. But xy=h², so k=h, and consequently uv=rh. [6.12, 6.16, 6.1, 5.11, 6.17]

**Step 6.** Since h is half of b and b is commensurable in length with r, h is rational and commensurable in length with r. Hence rh, and therefore uv, is a rational area. To test length-commensurability, reuse the common-height ratio argument already employed in Step 4: if u and v were commensurable in length, then u²:uv=u:v would imply that u² and uv were commensurable. Since uv is rational, u² would then be rational, contrary to Step 3. Thus u and v are commensurable in square only and contain a rational rectangle. [D10.1.1, 10.12, D10.1.3, 10.19, 6.1, 10.11, D10.1.4, 10.21]

**Step 7.** Finally, by the square-on-a-sum identity and the distribution of rectangles,
(u+v)²=u²+v²+2uv=rx+ry+2rh=r(x+y)+rb=r(a+b).
Thus u+v is the side of the given area. It is the sum of two medial straight lines commensurable in square only and containing a rational rectangle; therefore it is irrational and is called a first bimedial straight line. This proves the proposition. [2.4, 2.1, 10.37]

**USED:** 1.10, 10.11, 10.12, 10.13, 10.19, 10.21, 10.36, 10.37, 10.6, 10.9, 2.1, 2.14, 2.4, 2.5, 5.11, 6.1, 6.12, 6.16, 6.17, D10.1.1, D10.1.2, D10.1.3, D10.1.4, D10.2.1, D10.2.2
**Human refs (from References field):** 10.11, 10.12, 10.13, 10.15, 10.17, 10.19, 10.21, 10.37, 6.1, D10.2.2
**Jaccard:** 0.296 — AI adds ['1.10', '10.36', '10.6', '10.9', '2.1', '2.14', '2.4', '2.5', '5.11', '6.12', '6.16', '6.17', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.1.4', 'D10.2.1']; Human adds ['10.15', '10.17']

## Proposition 10.56
**Statement:** If an area be contained by a rational straight line and the third binomial, the âsideâ of the area is the irrational straight line called a second bimedial.

**Step 1.** Let r be the rational straight line set out, and let a+b, with a>b, be the third binomial. Its terms a and b are rational and commensurable in square only. Neither is commensurable in length with r; moreover, a²−b² is the square on a straight line commensurable in length with a. We shall obtain the two medial summands required for a second bimedial. [10.36; D10.2.1; D10.2.3]

**Step 2.** Put t=b/2. Apply to a a rectangle equal to t² and deficient by a square. This is possible because b<a, so t² is less than the square on a/2. Let the resulting parts of a be p and q. Thus
p+q=a,  pq=t²=b²/4.
Use the converse direction of 10.17: its commensurable-excess hypothesis is precisely the defining condition recorded in Step 1. It follows that p and q are commensurable in length. Their sum a is therefore commensurable with each of them. [6.28; 10.17; 10.15]

**Step 3.** The lines p, q and t are rational. To justify this explicitly, equal-height rectangle ratios give
p²:pa=pa:a²=p:a.
Since p and a are commensurable, p² and pa are commensurable, as are pa and a²; hence p² and a² are commensurable. The same argument applies to q and a, and to t and b, since b=2t. Because a and b are rational, transitivity of commensurability shows that p, q and t are rational also. Furthermore, p and q are incommensurable in length with r, since they are commensurable with a; similarly, t is incommensurable in length with r, since it is commensurable with b. [6.1; 10.11; 10.12; D10.1.1; D10.1.3; 10.13]

**Step 4.** Construct square sides x, y and z such that
x²=rp,  y²=rq,  z²=rt.
Each of these rectangles is contained by rational straight lines commensurable in square only. Consequently x, y and z are medial straight lines. Also,
x²:y²=rp:rq=p:q;
therefore x² and y² are commensurable, so x and y are commensurable in square. [2.14; 10.21; 6.1; 10.11; D10.1.2]

**Step 5.** Since pq=t², we have p:t=t:q. Hence
x²:z²=rp:rt=p:t=t:q=rt:rq=z²:y².
The proportionality of these squares implies x:z=z:y. Therefore xy=z²=rt. In particular, the rectangle contained by x and y is medial, being equal to the square on the medial straight line z. [6.17; 6.1; 6.22; 10.21]

**Step 6.** The lines p and t are incommensurable in length: p is commensurable with a, t with b, whereas a and b are incommensurable in length. But equal-height rectangle ratios, together with Step 5, give
x:y=x²:xy=rp:rt=p:t.
Thus x and y are incommensurable in length. Combined with Step 4, this shows that they are commensurable in square only. [10.13; 6.1; 10.11; D10.1.2]

**Step 7.** The square on x+y is
(x+y)²=x²+y²+2xy
=rp+rq+2rt
=r(p+q)+rb
=r(a+b).
Here the square-of-a-sum identity and the distribution of a rectangle over its divided side give the equalities. Thus x+y is the side of the given area. [2.4; 2.1]

**Step 8.** We have shown that x and y are medial straight lines, commensurable in square only, and containing a medial rectangle. Their sum is therefore the irrational straight line called a second bimedial. Since that sum is the side of the given area, the proposition follows. [10.38]

**USED:** 10.11, 10.12, 10.13, 10.15, 10.17, 10.21, 10.36, 10.38, 2.1, 2.14, 2.4, 6.1, 6.17, 6.22, 6.28, D10.1.1, D10.1.2, D10.1.3, D10.2.1, D10.2.3
**Human refs (from References field):** 10.13, 10.21, 10.38, D10.2.3
**Jaccard:** 0.200 — AI adds ['10.11', '10.12', '10.15', '10.17', '10.36', '2.1', '2.14', '2.4', '6.1', '6.17', '6.22', '6.28', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.2.1']

## Proposition 10.57
**Statement:** If an area be contained by a rational straight line and the fourth binomial, the âsideâ of the area is the irrational straight line called major.

**Step 1.** Let r be the rational straight line set out, and let a+b be the fourth binomial, with a>b. Its terms a and b are rational and commensurable in square only. Moreover, a is commensurable in length with r, and a²−b²=d² for a straight line d incommensurable in length with a. Throughout, uv denotes the rectangle contained by u and v. [10.36, D10.2.4]

**Step 2.** Bisect b, calling its half h. Then b²=4h², so h² is commensurable with b² and therefore with r²; hence h is rational. Since a is commensurable in length with r but incommensurable in length with b, r and b are incommensurable in length. Since h is commensurable in length with b, r and h are likewise incommensurable in length. Thus r and h are rational straight lines commensurable in square only, and the rectangle rh is medial. [1.10, 2.4, D10.1.1, D10.1.3, 10.12, 10.13, 10.21]

**Step 3.** Apply to a a rectangle equal to h² and deficient by a square. This construction is possible because h²=(b/2)²<(a/2)². Let the resulting parts of a be p and q; then p+q=a and pq=h²=b²/4. We use the converse direction of 10.18, since the incommensurable excess specified for the fourth binomial is precisely its hypothesis. It follows that p and q are incommensurable in length. [6.28, 10.18]

**Step 4.** Construct straight lines x and y whose squares equal rp and rq respectively. Since rectangles under the same height are as their bases,

x²:y² = rp:rq = p:q.

Therefore x² and y² are incommensurable, because p and q are incommensurable. Thus x and y are incommensurable in square. [2.14, 6.1, 10.11, D10.1.2]

**Step 5.** The sum of these squares is

x²+y² = rp+rq = r(p+q) = ra.

Since r and a are rational and commensurable in length, ra is rational. Hence the sum of the squares on x and y is rational. [2.1, 10.19]

**Step 6.** We next show that xy=rh. By the equal-height rule and pq=h²,

x²:y² = p:q = p²:pq = p²:h².

The converse of the theorem on similar figures therefore gives x:y=p:h. Again by the equal-height rule,

x²:xy = x:y = p:h = rp:rh.

Since x²=rp, magnitudes to which the same magnitude has the same ratio are equal; consequently xy=rh. Thus xy is medial, as established for rh in Step 2. [6.1, 6.22, 5.9]

**Step 7.** The square on the sum x+y is

(x+y)² = x²+y²+2xy = ra+2rh = ra+rb = r(a+b).

Therefore x+y is the side of the given area. [2.4, 2.1]

**Step 8.** The straight lines x and y are incommensurable in square, the sum of their squares is rational, and their rectangle is medial. Their sum is therefore the irrational straight line called major. Since that sum is the side of the area contained by r and the fourth binomial a+b, the required conclusion follows. [10.39]

**USED:** 1.10, 10.11, 10.12, 10.13, 10.18, 10.19, 10.21, 10.36, 10.39, 2.1, 2.14, 2.4, 5.9, 6.1, 6.22, 6.28, D10.1.1, D10.1.2, D10.1.3, D10.2.4
**Human refs (from References field):** 10.11, 10.13, 10.18, 10.19, 10.21, 10.39, 6.1, D10.2.4
**Jaccard:** 0.400 — AI adds ['1.10', '10.12', '10.36', '2.1', '2.14', '2.4', '5.9', '6.22', '6.28', 'D10.1.1', 'D10.1.2', 'D10.1.3']

## Proposition 10.58
**Statement:** If an area be contained by a rational straight line and the fifth binomial, the âsideâ of the area is the irrational straight line called the side of a rational plus a medial area.

**Step 1.** Let r be the rational straight line set out, and write the fifth binomial as a+b, with a>b. Products of straight lines will denote rectangles. The terms a and b are rational and commensurable in square only; b is commensurable in length with r; and a²−b² is the square on a straight line incommensurable in length with a. [10.36, D10.2.4, D10.2.5]

**Step 2.** Bisect b, putting h=b/2. Apply to a a rectangle equal to h² and deficient by a square. This construction is possible because h² is less than the square on half of a. It divides a into positive parts u,v satisfying
u+v=a and uv=h²=b²/4.
We choose this deficient-square construction because 10.18 applies directly to the defining condition in Step 1: u and v are incommensurable in length. [1.10, 6.28, 10.18]

**Step 3.** Construct straight lines x,y whose squares equal the rectangles ru,rv respectively. Thus x²=ru and y²=rv. By the common-height ratio rule,
x²:y²=ru:rv=u:v.
Since u and v are incommensurable, their corresponding squares x² and y² are incommensurable. Hence x and y are incommensurable in square. [2.14, 6.1, 10.11, D10.1.2]

**Step 4.** Since b is commensurable in length with r but incommensurable in length with a, the lines r and a are incommensurable in length. They are nevertheless commensurable in square, since a is rational. Consequently ra is a medial area. Moreover, distributivity of rectangles gives
x²+y²=ru+rv=r(u+v)=ra.
Thus the sum of the squares on x and y is medial. [10.13, D10.1.3, 10.21, 2.1]

**Step 5.** The common-height ratio rule also gives
x²:h²=ru:uv=r:v=r²:rv=r²:y².
Because these squares are proportional, their sides are proportional: x:h=r:y. Therefore the rectangle contained by the extremes equals that contained by the means, so
xy=rh. [6.1, 6.22, 6.16]

**Step 6.** The lines r and h are commensurable in length: half of a common measure of r and b measures both r and h=b/2. Thus h is rational, and the rectangle rh is rational. By Step 5, the rectangle xy is therefore rational. [D10.1.1, D10.1.3, 10.19]

**Step 7.** The square on x+y is
(x+y)²=x²+y²+2xy=ra+2rh=ra+rb=r(a+b).
Hence x+y is the side of the given area. By Steps 3, 4, and 6, its two constituent straight lines are incommensurable in square, the sum of their squares is medial, and their rectangle is rational. Proposition 10.40 therefore declares x+y irrational and calls it the side of a rational plus a medial area. This proves the proposition. [2.4, 2.1, 10.40]

**USED:** 1.10, 10.11, 10.13, 10.18, 10.19, 10.21, 10.36, 10.40, 2.1, 2.14, 2.4, 6.1, 6.16, 6.22, 6.28, D10.1.1, D10.1.2, D10.1.3, D10.2.4, D10.2.5
**Human refs (from References field):** 10.11, 10.12, 10.13, 10.18, 10.19, 10.21, 10.40, 6.1, D10.2.5
**Jaccard:** 0.381 — AI adds ['1.10', '10.36', '2.1', '2.14', '2.4', '6.16', '6.22', '6.28', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.2.4']; Human adds ['10.12']

## Proposition 10.59
**Statement:** If an area be contained by a rational straight line and the sixth binomial, the âsideâ of the area is the irrational straight line called the side of the sum of two medial areas.

**Step 1.** Let r be the given rational straight line, and write the sixth binomial as a+b, where a>b. Throughout, st denotes the rectangle contained by s and t, and s² the square on s. The terms a and b are rational and commensurable in square only [10.36]. By the sixth-binomial definition, neither term is commensurable in length with r, and a²=b²+d² for a straight line d incommensurable in length with a [D10.2.4, D10.2.6].

**Step 2.** Bisect b, putting h=b/2 [1.10]. The line h measures both itself and b, so they are commensurable in length [D10.1.1]; moreover, b²=4h² [2.4]. Thus h is rational, since its square is commensurable with the square on the rational line b [D10.1.3, 10.12]. Since b is incommensurable in length with both r and a, so is h [10.13]. Consequently, r and h, like r and a, are rational straight lines commensurable in square only [D10.1.3, 10.12].

**Step 3.** Apply to a a rectangle equal to h² and deficient by a square. This construction is possible because h²=b²/4<a²/4 [6.28]. It divides a into positive segments u and v satisfying
u+v=a, uv=h²=b²/4.
The converse assertion of 10.18 gives that u and v are incommensurable in length. This is the direct construction to use: its incommensurable square-difference hypothesis is exactly the condition supplied by the sixth-binomial definition [10.18].

**Step 4.** Construct straight lines x and y whose squares equal ru and rv respectively [2.14]. By the proportion of rectangles under the same height,
x²:y²=ru:rv=u:v [6.1].
Since u and v are incommensurable, x² and y² are incommensurable [10.11]; hence x and y are incommensurable in square [D10.1.2]. Also,
x²+y²=ru+rv=r(u+v)=ra [2.1].

**Step 5.** We next determine the rectangle xy. Since uv=h², the same-height proportion gives
x²:y²=u:v=u²:uv=u²:h² [6.1].
Therefore x:y=u:h, by the converse proportion theorem for similar figures, applied to squares [6.22]. Alternating gives x:u=y:h [5.16]. But x²=ru gives x:u=r:x by the rectangle–proportion equivalence [6.16]. Hence y:h=r:x [5.11], and therefore
xy=rh [6.16].

**Step 6.** Since r and a are rational and commensurable in square only, ra is a medial area. Likewise, since r and h are rational and commensurable in square only, rh is medial [10.21]. Furthermore,
ra:rh=a:h [6.1].
As a and h are incommensurable in length, ra and rh are incommensurable areas [10.11]. Thus x²+y² is medial, while xy is medial and incommensurable with x²+y².

**Step 7.** The square on the sum of x and y is
(x+y)²=x²+y²+2xy=ra+2rh=ra+rb=r(a+b),
using b=2h and the square-of-a-sum and rectangle-distribution identities [2.4, 2.1]. Therefore x+y is the side of the given area.

**Step 8.** The lines x and y are incommensurable in square; the sum of their squares is medial; and their rectangle is medial and incommensurable with that sum. Proposition 10.41 therefore applies directly: x+y is irrational and is called the side of the sum of two medial areas. Since its square equals r(a+b), this is precisely the side of the area contained by the rational straight line and the sixth binomial, as required [10.41].

**USED:** 1.10, 10.11, 10.12, 10.13, 10.18, 10.21, 10.36, 10.41, 2.1, 2.14, 2.4, 5.11, 5.16, 6.1, 6.16, 6.22, 6.28, D10.1.1, D10.1.2, D10.1.3, D10.2.4, D10.2.6
**Human refs (from References field):** 10.11, 10.13, 10.21, 10.41, 6.1
**Jaccard:** 0.227 — AI adds ['1.10', '10.12', '10.18', '10.36', '2.1', '2.14', '2.4', '5.11', '5.16', '6.16', '6.22', '6.28', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.2.4', 'D10.2.6']

## Proposition 10.60
**Statement:** The square on the binomial straight line applied to a rational straight line produces as breadth the first binomial.

**Step 1.** Let b be the given binomial and r the rational straight line to which its square is applied. Write b=x+y, where x>y and x,y are rational straight lines commensurable in square only. We follow the square expansion and verify the defining conditions for a first binomial directly. [10.36]

**Step 2.** Apply the areas x², y², and xy to r as rectangles, dividing each into triangles and using 1.44. Denote the respective breadths by u,v,w. Thus
ru=x², rv=y², rw=xy.
Put p=u+v and q=2w. By the square expansion,
b²=x²+y²+2xy=r(p+q).
Consequently the breadth produced by applying b² to r is p+q: rectangles on the same base have the ratio of their breadths. [1.44, 2.4, 6.1]

**Step 3.** Since x and y are rational, their squares are rational areas. Hence u and v are rational and commensurable in length with r. They are therefore commensurable with one another; their sum p is commensurable with each of them, and consequently with r. In particular, p is rational. [D10.1.3, D10.1.4, 10.20, 10.12, 10.15]

**Step 4.** Since x and y are rational and commensurable in square only, xy is the square on a medial straight line. Its application to r therefore produces a breadth w which is rational but incommensurable in length with r. Now q²=4w², so q is also rational. Moreover, q is commensurable in length with w, and hence incommensurable in length with r. Since p is commensurable in length with r, p and q are incommensurable in length. Being rational, they are commensurable in square. Thus p+q is a binomial, with terms p and q. [10.21, 10.22, 2.4, D10.1.3, 10.12, 10.13, 10.36]

**Step 5.** Comparing rectangles of equal height gives
u:w=x²:xy=x:y=xy:y²=w:v.
Therefore u,w,v are proportional, so the rectangle uv equals w². Hence
q²=4w²=4uv. [6.1, 6.17]

**Step 6.** For the square-difference condition, use the difference of the already-constructed commensurable breadths; this gives the required line directly. Since x>y, we have u>v. Set d=u−v. Proposition 2.7 gives
u²+v²=2uv+d²,
while Proposition 2.4 gives
p²=(u+v)²=u²+v²+2uv.
Together with Step 5 these yield
p²=4uv+d²=q²+d².
Thus p>q. Also, since u=v+d and u is commensurable with v, the converse part of 10.15 shows that d is commensurable with v. Since p is likewise commensurable with v, d is commensurable in length with p. [6.1, 2.7, 2.4, 10.15, 10.12]

**Step 7.** The required breadth p+q is therefore a binomial whose greater term p is commensurable in length with the given rational straight line r, and whose greater term's square exceeds the lesser term's square by d², where d is commensurable in length with p. By the definition, p+q is a first binomial. Therefore the square on a binomial straight line, applied to a rational straight line, produces as breadth the first binomial. [D10.2.1]

**USED:** 1.44, 10.12, 10.13, 10.15, 10.20, 10.21, 10.22, 10.36, 2.4, 2.7, 6.1, 6.17, D10.1.3, D10.1.4, D10.2.1
**Human refs (from References field):** 10.11, 10.13, 10.15, 10.17, 10.20, 10.21, 10.22, 10.36, 10.53, 6.1, 6.17, D10.2.1
**Jaccard:** 0.500 — AI adds ['1.44', '10.12', '2.4', '2.7', 'D10.1.3', 'D10.1.4']; Human adds ['10.11', '10.17', '10.53']

## Proposition 10.61
**Statement:** The square on the first bimedial straight line applied to a rational straight line produces as breadth the second binomial.

**Step 1.** Let L be a first bimedial straight line, and let r be the rational straight line to which its square is applied. By 10.37, write L=a+b, where a and b are medial straight lines commensurable in square only, and the rectangle ab is rational. Take a>b. Throughout, products of straight lines denote rectangles and squares denote square areas. [10.37]

**Step 2.** Apply a², b², and ab to r, obtaining breadths x, y, and h respectively, so that
rx=a², ry=b², rh=ab.
These applications are supplied by 1.44, applying the triangular halves of each area and joining the resulting rectangles. Put u=x+y and v=2h. By 2.4,
r(u+v)=a²+b²+2ab=(a+b)²=L².
Thus the breadth whose character must be proved is u+v. [1.44, 2.4]

**Step 3.** By 10.22, x and y are rational and incommensurable in length with r. By 10.20, h is rational and commensurable in length with r. Moreover, rectangles of equal height are as their bases, so
x:y=a²:b².
Since a² and b² are commensurable, x and y are commensurable in length; hence u=x+y is commensurable in length with x. Also v=2h is commensurable in length with h, and therefore with r. [10.22, 10.20, 6.1, 10.11, 10.15, D10.1.1, 10.12]

**Step 4.** By 10.9 and 10.6, straight lines commensurable in length are also commensurable in square. Since u is commensurable in length with the rational line x, and v with the rational line h, both u and v are rational; their squares are therefore commensurable with one another. But u is incommensurable in length with r, because u is commensurable with x whereas x is incommensurable with r. Since v is commensurable with r, u and v are incommensurable in length. Thus u and v are rational straight lines commensurable in square only, and u+v is a binomial. [10.9, 10.6, D10.1.3, 10.12, 10.13, 10.36]

**Step 5.** Applying 2.7 to a cut into b and a−b gives
a²+b²=2ab+(a−b)²>2ab.
Consequently ru>rv, and therefore u>v. Thus v is the lesser term of the binomial. [2.7, 6.1]

**Step 6.** Again using equal-height rectangles,
x:h=rx:rh=a²:ab=a:b,
and
h:y=rh:ry=ab:b²=a:b.
Hence x:h=h:y, and 6.16 gives xy=h². Since v=2h, its square is four times h²; thus
xy=¼v². [6.1, 6.16, 2.4]

**Step 7.** For the square-excess condition, use 10.17 directly: the commensurable partition u=x+y already obtained is precisely the partition required there. Indeed, the rectangle with base x and breadth y, placed along u, is deficient by the square on y, and its area is ¼v². Its two base segments x and y are commensurable in length, and u>v. Therefore 10.17 shows that the square on u exceeds the square on v by the square on a straight line commensurable in length with u. [10.17]

**Step 8.** We have shown that u+v is a binomial, that the square on its greater term u exceeds the square on its lesser term v by the square on a straight line commensurable in length with u, and that its lesser term v is commensurable in length with the rational straight line r. These are exactly the defining conditions for the second binomial. Since r(u+v)=L², the square on the first bimedial straight line, applied to a rational straight line, produces as breadth the second binomial. [D10.2.1, D10.2.2]

**USED:** 1.44, 10.11, 10.12, 10.13, 10.15, 10.17, 10.20, 10.22, 10.36, 10.37, 10.6, 10.9, 2.4, 2.7, 6.1, 6.16, D10.1.1, D10.1.3, D10.2.1, D10.2.2
**Human refs (from References field):** 10.11, 10.13, 10.15, 10.17, 10.20, 10.21, 10.22, 10.23, 10.36, 10.37, 6.1, D10.2.2
**Jaccard:** 0.455 — AI adds ['1.44', '10.12', '10.6', '10.9', '2.4', '2.7', '6.16', 'D10.1.1', 'D10.1.3', 'D10.2.1']; Human adds ['10.21', '10.23']

## Proposition 10.62
**Statement:** The square on the second bimedial straight line applied to a rational straight line produces as breadth the third binomial.

**Step 1.** Let the given second bimedial straight line be a+b, and let r be the rational straight line to which its square is applied. By the characterization of a second bimedial, a and b are medial, commensurable in square only, and contain a medial rectangle ab. Take a>b. We follow the direct route: expand the square and verify the defining conditions on the resulting two breadths. [10.38]

**Step 2.** Construct straight lines p, q, t such that
rp=a², rq=b², rt=ab.
These constructions are possible by fourth proportionals and the equality of the corresponding rectangles. Put x=p+q and y=2t. Then
r(x+y)=a²+b²+2ab=(a+b)².
Thus the breadth produced by applying the given square to r is x+y. [6.12, 6.16, 2.1, 2.4]

**Step 3.** Ratios of rectangles having the same height give
p:q=a²:b²,
and
p:t=a²:ab=a:b=ab:b²=t:q.
Since a² and b² are commensurable, p and q are commensurable in length; since a and b are incommensurable in length, p and t are incommensurable in length. Also p:t=t:q gives pq=t². Moreover, a>b implies p>q. [6.1, 5.11, 10.11, 6.16]

**Step 4.** Since a², b², and ab are medial areas, their application to the rational line r gives rational breadths p, q, t, each incommensurable in length with r. Since p and q are commensurable, x=p+q is commensurable in length with p; likewise y=2t is commensurable in length with t. Consequently neither x nor y is commensurable in length with r. Furthermore, the incommensurability of p with t first gives that x is incommensurable with t, and then that x is incommensurable with y. [10.22, 10.15, 10.13]

**Step 5.** Straight lines commensurable in length have squares whose ratio is that of square numbers, and hence have commensurable squares. Therefore x² is commensurable with p², and y² with t². Since p and t are rational, it follows that x and y are rational and that their squares are commensurable with one another. Together with their incommensurability in length established above, this shows that x and y are rational straight lines commensurable in square only. Their sum x+y is therefore a binomial. [10.9, 10.6, D10.1.3, 10.12, 10.36]

**Step 6.** We use the equal-and-unequal-sections identity because the partition x=p+q is already present. Applied to this partition, it gives
pq+((p−q)/2)²=(x/2)².
Taking four times these areas, and using pq=t² and y=2t, yields
x²=y²+(p−q)².
Thus x>y. Moreover, since p and q are commensurable, the converse part of the addition theorem shows that p−q is commensurable with q; its direct part shows that x=p+q is commensurable with q. Hence p−q is commensurable in length with x. The square on the greater term x therefore exceeds the square on the lesser term y by the square on a straight line commensurable in length with x. [2.5, 2.4, 10.15, 10.12]

**Step 7.** We have shown that x+y is a binomial, that the excess of the square on its greater term over the square on its lesser term is the square on a straight line commensurable in length with the greater, and that neither term is commensurable in length with the rational straight line r. These are precisely the defining conditions of a third binomial. Therefore the square on the second bimedial straight line, applied to a rational straight line, produces as breadth the third binomial. [D10.2.1, D10.2.3]

**USED:** 10.11, 10.12, 10.13, 10.15, 10.22, 10.36, 10.38, 10.6, 10.9, 2.1, 2.4, 2.5, 5.11, 6.1, 6.12, 6.16, D10.1.3, D10.2.1, D10.2.3
**Human refs (from References field):** 10.11, 10.12, 10.13, 10.15, 10.22, 10.23, 10.36, 10.38, 6.1, D10.2.3
**Jaccard:** 0.450 — AI adds ['10.6', '10.9', '2.1', '2.4', '2.5', '5.11', '6.12', '6.16', 'D10.1.3', 'D10.2.1']; Human adds ['10.23']

## Proposition 10.63
**Statement:** The square on the major straight line applied to a rational straight line produces as breadth the fourth binomial.

**Step 1.** Let the given major straight line be divided into its defining terms a and b, with a>b. Thus a² and b² are incommensurable areas, a²+b² is rational, and the rectangle ab is medial. Let r be the rational straight line to which the square on a+b is to be applied. Here products denote rectangles and squares denote square areas. [10.39]

**Step 2.** Apply the areas a², b², and ab to r, obtaining breadths p, q, and w respectively, so that
rp=a², rq=b², rw=ab.
These applications can be made by applying constituent triangles and adjoining the resulting rectangles. Put U=p+q and V=2w. Then
r(U+V)=a²+b²+2ab=(a+b)².
Consequently U+V is the breadth whose character we must establish. [1.44, 2.1, 2.4]

**Step 3.** Since rU=a²+b² is rational, U is rational and commensurable in length with r. Since rw=ab is medial, w is rational and incommensurable in length with r. Now V=2w is commensurable in length with w, and V²=4w². Any common area measure of w² and the assigned rational square therefore also measures V²; hence V is rational. Moreover, V is incommensurable in length with r, because it is commensurable with w. [10.20, 10.22, D10.1.1, 2.4, D10.1.2, D10.1.3, 10.13]

**Step 4.** The squares on U and V are commensurable, since both are commensurable with the assigned rational square. But U and V are incommensurable in length: U is commensurable with r, whereas V is incommensurable with r. Thus U and V are rational straight lines commensurable in square only, and U+V is a binomial. [D10.1.2, D10.1.3, 10.12, 10.13, 10.36]

**Step 5.** By the identity
a²+b²=2ab+(a−b)²,
we have rU>rV, and therefore U>V. Thus U is the greater term of this binomial. Also, rectangles under the same height r give
p:q=a²:b².
Since a² and b² are incommensurable, p and q are incommensurable in length. [2.7, 6.1, 10.11]

**Step 6.** Again using ratios of rectangles under the same height,
p:w=a²:ab=a:b,
and
w:q=ab:b²=a:b.
Hence p:w=w:q, and consequently pq=w². Since V=2w, the rectangle pq is equal to the fourth part of V². [6.1, 5.11, 6.17, 2.4]

**Step 7.** We use the incommensurable-part criterion directly, since the required division U=p+q is already available. On the part p of U construct the rectangle with height q. Its area is pq=V²/4; extending it over the remaining part q adds precisely a square q². It is therefore a parallelogram applied to U and deficient by a square, and it divides U into the incommensurable parts p and q. Since U>V, it follows that U² exceeds V² by the square on a straight line incommensurable in length with U. [2.1, 10.18]

**Step 8.** The breadth U+V is a binomial; its greater term U is commensurable in length with the rational straight line r; and U²−V² is the square on a straight line incommensurable in length with U. By the definition, U+V is therefore the fourth binomial. Since r(U+V)=(a+b)², the square on the major straight line applied to a rational straight line produces as breadth the fourth binomial. [D10.2.4]

**USED:** 1.44, 10.11, 10.12, 10.13, 10.18, 10.20, 10.22, 10.36, 10.39, 2.1, 2.4, 2.7, 5.11, 6.1, 6.17, D10.1.1, D10.1.2, D10.1.3, D10.2.4
**Human refs (from References field):** 10.11, 10.13, 10.18, 10.20, 10.22, 10.36, 10.39, 6.1, D10.2.4
**Jaccard:** 0.474 — AI adds ['1.44', '10.12', '2.1', '2.4', '2.7', '5.11', '6.17', 'D10.1.1', 'D10.1.2', 'D10.1.3']

## Proposition 10.64
**Statement:** The square on the side of a rational plus a medial area applied to a rational straight line produces as breadth the fifth binomial.

**Step 1.** Let s be the side of a rational plus a medial area, and let r be the given rational straight line. Write s=a+b according to its defining division. Thus a and b are incommensurable in square, a²+b² is medial, and ab is rational. In particular, a² and b² are incommensurable areas, and a≠b. Here products denote rectangles and squares denote square areas. [10.40, D10.1.2]

**Step 2.** Construct positive straight lines x, y, and w such that rx=a², ry=b², and rw=ab; fourth proportionals provide these constructions. Put u=x+y and v=2w. Then ru=a²+b² and rv=2ab, so
r(u+v)=a²+b²+2ab=(a+b)²=s².
Consequently, the breadth obtained by applying the square on s to r is u+v. [6.12, 6.16, 2.1, 2.4]

**Step 3.** Since a≠b, Proposition 2.7, applied to the greater of them cut at the length of the lesser, gives a²+b²>2ab. Hence ru>rv, and therefore u>v, since rectangles of the same height are proportional to their bases. [2.7, 6.1]

**Step 4.** Because ru is medial, u is rational and incommensurable in length with r. Since ab is rational, its double 2ab is also rational: it is commensurable with ab and hence with the assigned rational square. Therefore v is rational and commensurable in length with r. It follows that u and v are incommensurable in length. Their squares, however, are commensurable, since both lines are rational. Thus u+v is a binomial, with greater term u and lesser term v. [10.22, D10.1.1, D10.1.4, 10.12, 10.20, 10.13, D10.1.3, 10.36]

**Step 5.** The equal-height rectangles rx and ry give x:y=a²:b². Since a² and b² are incommensurable, x and y are incommensurable in length. Moreover, comparison of equal-height rectangles gives
x:w=a²:ab=a:b,
and
w:y=ab:b²=a:b.
Hence x:w=w:y, and therefore xy=w²=v²/4. [6.1, 10.11, 6.17]

**Step 6.** Since u=x+y, the rectangle xy is an area applied to u deficient by the square on y: indeed, uy=xy+y². Its area is one quarter of the square on v, and it divides u into the incommensurable parts x and y. We use the direct incommensurable-part criterion of Proposition 10.18, since the defining squares have supplied precisely this partition. As u>v, that proposition shows that u² exceeds v² by the square on a straight line incommensurable in length with u. [2.1, 10.18]

**Step 7.** Thus u+v is a binomial whose greater term’s square exceeds the lesser term’s square by the square on a line incommensurable in length with the greater term, while its lesser term v is commensurable in length with the given rational line r. By the definition, u+v is the fifth binomial. Since r(u+v)=s², the square on the side of a rational plus a medial area, applied to a rational straight line, produces as breadth the fifth binomial. [D10.2.4, D10.2.5]

**USED:** 10.11, 10.12, 10.13, 10.18, 10.20, 10.22, 10.36, 10.40, 2.1, 2.4, 2.7, 6.1, 6.12, 6.16, 6.17, D10.1.1, D10.1.2, D10.1.3, D10.1.4, D10.2.4, D10.2.5
**Human refs (from References field):** 10.13, 10.18, 10.20, 10.22, 10.36, 10.40
**Jaccard:** 0.286 — AI adds ['10.11', '10.12', '2.1', '2.4', '2.7', '6.1', '6.12', '6.16', '6.17', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.1.4', 'D10.2.4', 'D10.2.5']

## Proposition 10.65
**Statement:** The square on the side of the sum of two medial areas applied to a rational straight line produces as breadth the sixth binomial.

**Step 1.** Let L be a side of the sum of two medial areas. Take its defining division L=a+b, with a>b. Thus a² and b² are incommensurable areas, while S=a²+b² and P=ab are medial areas incommensurable with one another. Here squares and products denote their corresponding areas. We shall apply these constituent areas separately. [10.41, D10.1.2]

**Step 2.** Let r be the given rational straight line. Construct breadths x,y,w such that rx=a², ry=b², and rw=ab; fourth proportionals provide these constructions. Put u=x+y and v=2w. Then ru=S and rv=2P. Since L²=S+2P, the rectangle r(u+v) equals L². Consequently, the breadth obtained by applying L² to r is u+v. [6.12, 6.16, 2.1, 2.4, 6.1]

**Step 3.** Since S and P are medial, their applications to r show that u and w are rational and each is incommensurable in length with r. Now v=2w, so v is commensurable in length with w, and v²=4w². Thus v² is commensurable with w² and hence with the square on the assigned rational line; therefore v is rational. Moreover, because w is incommensurable in length with r, so is v. Thus both u and v are rational, but neither is commensurable in length with r. [10.22, 2.4, D10.1.1, D10.1.3, 10.12, 10.13]

**Step 4.** Rectangles of the same height give u:w=S:P. Since S and P are incommensurable, u and w are incommensurable in length. As v is commensurable with w, u and v are likewise incommensurable in length. But their squares are commensurable, since both lines are rational. Hence u and v are rational straight lines commensurable in square only, and u+v is a binomial. [6.1, 10.11, 10.13, D10.1.3, 10.12, 10.36]

**Step 5.** Similarly, x:y=a²:b², so x and y are incommensurable in length. Furthermore, comparison of rectangles under the same height gives
x:w=a²:ab=a:b,
and
w:y=ab:b²=a:b.
Therefore x:w=w:y, whence xy=w². Since v=2w, this rectangle xy equals one fourth of v². [6.1, 10.11, 5.11, 6.16, 2.4]

**Step 6.** By the identity a²+b²=2ab+(a−b)², we have S>2P and consequently u>v. On the straight line u=x+y, the rectangle xy is an application deficient by the square on y. It equals one fourth of the square on v and divides u into the incommensurable parts x,y. Proposition 10.18 is therefore the direct criterion: its incommensurable-division hypothesis has just been established. It follows that u² exceeds v² by the square on a straight line incommensurable in length with u. [2.7, 6.1, 2.1, 10.18]

**Step 7.** Thus the binomial u+v has greater term u whose square exceeds the square on its lesser term v by the square on a line incommensurable with u; and neither term is commensurable in length with the given rational line r. These are precisely the conditions defining the sixth binomial. Since u+v is the breadth obtained by applying L² to r, the square on the side of the sum of two medial areas, applied to a rational straight line, produces as breadth the sixth binomial. [D10.2.4, D10.2.6]

**USED:** 10.11, 10.12, 10.13, 10.18, 10.22, 10.36, 10.41, 2.1, 2.4, 2.7, 5.11, 6.1, 6.12, 6.16, D10.1.1, D10.1.2, D10.1.3, D10.2.4, D10.2.6
**Human refs (from References field):** 10.11, 10.22, 10.36, 10.41, 6.1
**Jaccard:** 0.263 — AI adds ['10.12', '10.13', '10.18', '2.1', '2.4', '2.7', '5.11', '6.12', '6.16', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.2.4', 'D10.2.6']

## Proposition 10.66
**Statement:** A straight line commensurable in length with a binomial straight line is itself also binomial and the same in order.

**Step 1.** Let B be a binomial straight line, and let L be commensurable in length with B. Fix the rational straight line r relative to which its order is specified. Write B = a + b, where a > b and a, b are rational straight lines commensurable in square only. We use proportional division to transfer the defining properties of these terms to L. [10.36]

**Step 2.** Cut L similarly to B, obtaining L = c + d with a:b = c:d, where c is the greater term. Alternating and then taking the sums of antecedents and consequents gives

a:c = b:d = (a+b):(c+d) = B:L.

Since B and L are commensurable in length, a and c are commensurable in length, as are b and d. [6.10, 5.16, 5.12, 10.11]

**Step 3.** Because a and c are commensurable in length, their squares have the ratio of a square number to a square number and consequently are commensurable. Likewise, the squares on b and d are commensurable. Since a and b are rational, their squares are each commensurable with the square on r. Transitivity of commensurability therefore shows that the squares on c and d are each commensurable with the square on r, and also with one another. Thus c and d are rational straight lines commensurable in square. [10.9, 10.6, 10.12, D10.1.2, D10.1.3]

**Step 4.** Since a:b = c:d and a, b are incommensurable in length, c, d are likewise incommensurable in length. Hence c and d are rational straight lines commensurable in square only, so their sum L is binomial. [10.11, 10.36]

**Step 5.** To preserve the square-excess condition determining the order, apply 10.14 directly: it already treats both possible cases. Since a:b = c:d, if the square on a exceeds the square on b by the square on a straight line commensurable in length with a, then the square on c exceeds the square on d by the square on a straight line commensurable in length with c. If instead the former excess is the square on a straight line incommensurable in length with a, the latter excess is likewise the square on a straight line incommensurable in length with c. Thus this distinction is preserved. [10.14]

**Step 6.** The relation of each term to r is also preserved. Since a and c are commensurable in length, if a is commensurable in length with r, so is c; if a is incommensurable in length with r, so is c. The same argument applies to b and d. Consequently, the greater term, the lesser term, or neither term is commensurable in length with r for L exactly as for B. [10.12, 10.13]

**Step 7.** When the square-excess line is commensurable with the greater term, the three respective possibilities in Step 6 define the first, second, and third binomials. When it is incommensurable with the greater term, they define the fourth, fifth, and sixth binomials. Steps 5 and 6 preserve both defining distinctions. Therefore L is binomial and has the same order as B, as required. [D10.2.1, D10.2.2, D10.2.3, D10.2.4, D10.2.5, D10.2.6]

**USED:** 10.11, 10.12, 10.13, 10.14, 10.36, 10.6, 10.9, 5.12, 5.16, 6.10, D10.1.2, D10.1.3, D10.2.1, D10.2.2, D10.2.3, D10.2.4, D10.2.5, D10.2.6
**Human refs (from References field):** 10.11, 10.12, 10.13, 10.14, 10.36, 5.11, 5.16, 5.19, 6.12, D10.2.1, D10.2.2, D10.2.3, D10.2.4, D10.2.5, D10.2.6
**Jaccard:** 0.571 — AI adds ['10.6', '10.9', '5.12', '6.10', 'D10.1.2', 'D10.1.3']; Human adds ['5.11', '5.19', '6.12']

## Proposition 10.67
**Statement:** A straight line commensurable in length with a bimedial straight line is itself also bimedial and the same in order.

**Step 1.** Let L be bimedial, and let M be commensurable in length with L. We take the direct route of transferring the defining two-part decomposition. Write L = a + b, where a and b are medial and commensurable in square only. The rectangle ab is rational if L is first bimedial, and medial if L is second bimedial. Here xy denotes the rectangle contained by x and y, and x² denotes the square on x. [10.37, 10.38]

**Step 2.** Cut M similarly to L, obtaining M = c + d with a:b = c:d. Alternately, a:c = b:d; and the ratio of the sums is the same ratio. Hence
L:M = a:c = b:d.
Since L and M are commensurable in length, a and c are commensurable in length, as are b and d. [6.10, 5.16, 5.12, 10.11]

**Step 3.** Since c and d are respectively commensurable in length with the medial lines a and b, both c and d are medial. Moreover, a:b = c:d and a, b are incommensurable in length, so c, d are incommensurable in length. By proportionality of similarly described squares,
a²:b² = c²:d².
The first two squares are commensurable, so the latter two are commensurable also. Thus c and d are medial straight lines commensurable in square only. [10.23, 10.11, 6.22, D10.1.2]

**Step 4.** The rectangles ab and cb have the common height b, while cb and cd have the common height c. Therefore
ab:cb = a:c, and cb:cd = b:d.
The corresponding pairs of lengths are commensurable by Step 2, so ab is commensurable with cb, and cb with cd. Consequently ab and cd are commensurable areas. [6.1, 10.11, 10.12]

**Step 5.** Suppose L is first bimedial. Then ab is rational, hence commensurable with the square on the assigned rational straight line. Since cd is commensurable with ab, it too is commensurable with that square and therefore rational. Thus M = c + d is the sum of two medial straight lines commensurable in square only and containing a rational rectangle. It is therefore first bimedial. [D10.1.4, 10.12, 10.37]

**Step 6.** Suppose instead that L is second bimedial. Then ab is medial and therefore irrational. The rectangle cd cannot be rational: otherwise its commensurability with ab would make ab commensurable with the assigned rational square, contrary to its irrationality. Now use the rational-or-medial alternative of 10.25, which applies directly to the two parts established in Step 3. It says that cd is either rational or medial; rationality having been excluded, cd is medial. Hence M = c + d is second bimedial. In either case, M is bimedial and of the same order as L. [10.21, D10.1.4, 10.12, 10.25, 10.38]

**USED:** 10.11, 10.12, 10.21, 10.23, 10.25, 10.37, 10.38, 5.12, 5.16, 6.1, 6.10, 6.22, D10.1.2, D10.1.4
**Human refs (from References field):** 10.11, 10.23, 10.37, 10.38, 5.11, 5.16, 5.19
**Jaccard:** 0.312 — AI adds ['10.12', '10.21', '10.25', '5.12', '6.1', '6.10', '6.22', 'D10.1.2', 'D10.1.4']; Human adds ['5.11', '5.19']

## Proposition 10.68
**Statement:** A straight line commensurable with a major straight line is itself also major.

**Step 1.** Let a be a major straight line, and let b be commensurable in length with a. Choose a rational straight line r. Construct x and y as third proportionals to r, a and to r, b respectively, so that r:a = a:x and r:b = b:y. Then the rectangles rx and ry equal the squares on a and b respectively. Here products denote rectangular areas and squares denote square areas. [6.11, 6.17]

**Step 2.** Use the fourth-binomial breadth route, since it applies directly to the square on the given major line. The square on a, applied to the rational straight line r, has breadth x; therefore x is a fourth binomial. [10.63]

**Step 3.** Since a and b are commensurable in length, their squares have the ratio of a square number to a square number. The rectangles rx and ry have the same height r, so their ratio equals x:y. Thus
x:y = rx:ry = a²:b²
is a ratio of numbers. Consequently x and y are commensurable in length. [10.9, 6.1, 10.6]

**Step 4.** A straight line commensurable in length with a binomial is itself binomial and of the same order. Since x is a fourth binomial, y is also a fourth binomial. [10.66]

**Step 5.** The rectangle ry is therefore contained by a rational straight line and a fourth binomial. Its square-side is consequently major. But ry equals the square on b, so b is that square-side and is major. Hence a straight line commensurable with a major straight line is itself also major. [10.57]

**USED:** 10.57, 10.6, 10.63, 10.66, 10.9, 6.1, 6.11, 6.17
**Human refs (from References field):** 10.11, 10.23, 10.39, 5.11, 5.16, 5.18, 6.20
**Jaccard:** 0.000 — AI adds ['10.57', '10.6', '10.63', '10.66', '10.9', '6.1', '6.11', '6.17']; Human adds ['10.11', '10.23', '10.39', '5.11', '5.16', '5.18', '6.20']

## Proposition 10.69
**Statement:** A straight line commensurable with the side of a rational plus a medial area is itself also the side of a rational plus a medial area.

**Step 1.** Let x be the side of a rational plus a medial area, and let y be commensurable in length with x. Choose a rational straight line r. By VI.12, construct straight lines a and b such that r:x = x:a and r:y = y:b. Then, by VI.17, the rectangles contained by r,a and by r,b equal the squares on x and y respectively; write these equalities as ra = x² and rb = y². [6.12, 6.17]

**Step 2.** Since the square on x, applied to the rational straight line r, has breadth a, X.64 shows that a is a fifth binomial. We choose this fixed-rational-base route because it converts the claim directly into preservation of binomial order. [10.64]

**Step 3.** Since x and y are commensurable in length, their squares have the ratio of a square number to a square number, by X.9. The rectangles ra and rb have the same height r, so VI.1 gives a:b = ra:rb = x²:y². Thus a and b have the ratio of a number to a number, and are therefore commensurable in length by X.6. [10.9, 6.1, 10.6]

**Step 4.** A straight line commensurable in length with a binomial is itself binomial and of the same order. Since a is a fifth binomial, b is consequently a fifth binomial. [10.66]

**Step 5.** The square on y equals the rectangle contained by the rational straight line r and the fifth binomial b. By X.58, the side of this area, namely y, is the side of a rational plus a medial area. Hence a straight line commensurable with the side of a rational plus a medial area is itself also the side of a rational plus a medial area. [10.58]

**USED:** 10.58, 10.6, 10.64, 10.66, 10.9, 6.1, 6.12, 6.17
**Human refs (from References field):** 10.40
**Jaccard:** 0.000 — AI adds ['10.58', '10.6', '10.64', '10.66', '10.9', '6.1', '6.12', '6.17']; Human adds ['10.40']

## Proposition 10.70
**Statement:** A straight line commensurable with the side of the sum of two medial areas is the side of the sum of two medial areas.

**Step 1.** Let a be the side of the sum of two medial areas, and let b be a straight line commensurable in length with a. Choose a rational straight line r. Construct fourth proportionals u and v such that r:a = a:u and r:b = b:v. Then the rectangles contained by r,u and by r,v equal the squares on a and b respectively. [6.12, 6.16]

**Step 2.** Since the square on a, applied to the rational straight line r, has breadth u, u is a sixth binomial. We choose this application route because it identifies the required binomial order directly. [10.65]

**Step 3.** Since a and b are commensurable in length, their squares have the ratio of a square number to a square number. Consequently, the squares on a and b are commensurable areas. [10.9, 10.6]

**Step 4.** The rectangles contained by r,u and by r,v have the same height r, so their ratio is u:v. Thus the square on a is to the square on b as u is to v. Since these squares are commensurable, u and v are commensurable in length. [6.1, 10.11]

**Step 5.** A straight line commensurable in length with a binomial is itself binomial and of the same order. Therefore v, being commensurable with the sixth binomial u, is also a sixth binomial. [10.66]

**Step 6.** The square on b is the rectangle contained by the rational straight line r and the sixth binomial v. The side of such an area is the side of the sum of two medial areas. Hence b is the side of the sum of two medial areas, as required. [10.59]

**USED:** 10.11, 10.59, 10.6, 10.65, 10.66, 10.9, 6.1, 6.12, 6.16
**Human refs (from References field):** 10.41
**Jaccard:** 0.000 — AI adds ['10.11', '10.59', '10.6', '10.65', '10.66', '10.9', '6.1', '6.12', '6.16']; Human adds ['10.41']

## Proposition 10.71
**Statement:** If a rational and a medial area be added together, four irrational straight lines arise, namely a binomial or a first bimedial or a major or a side of a rational plus a medial area.

**Step 1.** Let R be a rational area and M a medial area, relative to the assigned rational straight line a. We use the direct common-base route, since the application theorems immediately determine the two breadths. Apply R and M to a as rectangles, obtaining breadths r and m respectively. Such applications can be made by triangulating the figures and adjoining the rectangles supplied by 1.44. By 10.20, r is rational and commensurable in length with a; by 10.22, m is rational and incommensurable in length with a. Thus, writing products for rectangular areas, R = ar and M = am. [1.44, 10.20, 10.22]

**Step 2.** Since r and m are rational, their squares are each commensurable with the square on a, and hence with one another. But r and m are incommensurable in length, because r is commensurable with a whereas m is incommensurable with a. They are therefore rational straight lines commensurable in square only, so r + m is a binomial. In particular, r and m are unequal. [D10.1.3, 10.12, 10.13, 10.36]

**Step 3.** By 2.1, the rectangle contained by a and r + m equals ar + am, that is, R + M. Construct its square-side s by 2.14. Let g be the greater of r and m, and h the lesser; also construct d so that the square on d equals the difference of their squares. Thus s² = a(r + m) and g² = h² + d². There are four cases, according as r is the greater or lesser term and d is commensurable or incommensurable in length with g. [2.1, 2.14]

**Step 4.** Suppose r > m and d is commensurable in length with r. The greater term r is commensurable in length with the assigned rational line a, and its square exceeds the square on m by the square on a line commensurable with r. Hence r + m is a first binomial. Since s² is the rectangle contained by a and this first binomial, s is an irrational straight line called a binomial. [D10.2.1, 10.54]

**Step 5.** Suppose m > r and d is commensurable in length with m. The square on the greater term exceeds that on the lesser by the square on a line commensurable with the greater, while the lesser term r is commensurable in length with a. Hence r + m is a second binomial. Therefore s is an irrational straight line called a first bimedial. [D10.2.1, D10.2.2, 10.55]

**Step 6.** Suppose r > m and d is incommensurable in length with r. The greater term r is commensurable in length with a, but its square exceeds the square on m by the square on a line incommensurable with r. Hence r + m is a fourth binomial. Therefore s is an irrational straight line called major. [D10.2.4, 10.57]

**Step 7.** Suppose m > r and d is incommensurable in length with m. The square on the greater term exceeds that on the lesser by the square on a line incommensurable with the greater, while the lesser term r is commensurable in length with a. Hence r + m is a fifth binomial. Therefore s is the irrational straight line called the side of a rational plus a medial area. [D10.2.4, D10.2.5, 10.58]

These four cases exhaust the possibilities. Consequently, adding a rational and a medial area gives an area whose square-side is a binomial, a first bimedial, a major, or a side of a rational plus a medial area, as required.

**USED:** 1.44, 10.12, 10.13, 10.20, 10.22, 10.36, 10.54, 10.55, 10.57, 10.58, 2.1, 2.14, D10.1.3, D10.2.1, D10.2.2, D10.2.4, D10.2.5
**Human refs (from References field):** 10.11, 10.20, 10.22, 10.36, 10.54, 10.55, 10.57, 10.58, 6.1, D10.2.1, D10.2.2, D10.2.4, D10.2.5
**Jaccard:** 0.579 — AI adds ['1.44', '10.12', '10.13', '2.1', '2.14', 'D10.1.3']; Human adds ['10.11', '6.1']

## Proposition 10.72
**Statement:** If two medial areas incommensurable with one another be added together, the remaining two irrational straight lines arise, namely either a second bimedial or a side of the sum of two medial areas.

**Step 1.** Let M and N be the given medial areas, incommensurable with one another, and let r be the assigned rational straight line. Apply M and N to r as rectangles, obtaining breadths a and b respectively. Thus M = rect(r,a) and N = rect(r,b). By 10.22, both a and b are rational, and each is incommensurable in length with r. [10.22]

**Step 2.** The two rectangles have the same height r, so M:N = a:b. Since M and N are incommensurable, a and b are incommensurable in length. But, being rational, their squares are each commensurable with the square on r, and therefore are commensurable with one another. Hence a and b are rational straight lines commensurable in square only, and a+b is a binomial. [6.1, 10.11, D10.1.3, 10.12, 10.36]

**Step 3.** By addition of the rectangles,
M+N = rect(r,a+b).
Let s be the side of the square equal to this area. Since a and b are unequal, interchange their names if necessary so that a>b, and construct d whose square equals the difference between the squares on a and b. Thus a² = b²+d². We classify the binomial breadth a+b and then use the area-to-side results, since these apply directly to the rectangle just obtained. [2.1, 2.14]

**Step 4.** Suppose d is commensurable in length with a. The square on the greater term a then exceeds the square on the lesser term b by the square on a straight line commensurable in length with a. Moreover, neither term is commensurable in length with r, by Step 1. Consequently a+b is a third binomial. Since M+N is contained by the rational straight line r and this third binomial, its square-side s is an irrational straight line called a second bimedial. [D10.2.1, D10.2.3, 10.56]

**Step 5.** Suppose instead that d is incommensurable in length with a. The square on the greater term then exceeds the square on the lesser by the square on a straight line incommensurable in length with the greater. Since neither term is commensurable in length with r, a+b is a sixth binomial. The square-side s of the area contained by r and this sixth binomial is therefore the irrational straight line called the side of the sum of two medial areas. [D10.2.4, D10.2.6, 10.59]

**Step 6.** These two cases exhaust the possibilities. Therefore the side of the square equal to the sum of two incommensurable medial areas is either a second bimedial or a side of the sum of two medial areas, as required. [10.56, 10.59]

**USED:** 10.11, 10.12, 10.22, 10.36, 10.56, 10.59, 2.1, 2.14, 6.1, D10.1.3, D10.2.1, D10.2.3, D10.2.4, D10.2.6
**Human refs (from References field):** 10.11, 10.22, 10.36, 10.56, 10.59, 6.1, D10.2.3, D10.2.6
**Jaccard:** 0.571 — AI adds ['10.12', '2.1', '2.14', 'D10.1.3', 'D10.2.1', 'D10.2.4']

## Proposition 10.73
**Statement:** If from a rational straight line there be subtracted a rational straight line commensurable with the whole in square only, the remainder is irrational; and let it be called   an apotome.

**Step 1.** Let the rational straight line AB have the rational straight line AC subtracted from it, where AC is commensurable with AB in square only, and let CB be the remainder. Let K be the square on the assigned rational straight line. The squares on AB and AC are commensurable with each other and with K. [D10.1.2, D10.1.3, D10.1.4]

**Step 2.** Use the square identity for subtraction, since it directly connects the remainder with the rectangle contained by the two given lines. Write S for the sum of the squares on AB and AC, R for the rectangle contained by AB and AC, and T for the square on CB. Then
S = 2R + T.
[2.7]

**Step 3.** Since the squares on AB and AC are commensurable, their sum S is commensurable with the square on AB. Since that square is also commensurable with K, S is commensurable with K. [10.15, 10.12]

**Step 4.** The rectangle R is irrational, because its sides AB and AC are rational and commensurable in square only. Thus R is incommensurable with K. Moreover, R and 2R are commensurable, R itself measuring both. Consequently 2R is also incommensurable with K. [10.21, D10.1.4, D10.1.1, 10.13]

**Step 5.** Suppose that T were commensurable with K. Then S and T would be commensurable, since both would be commensurable with K. But S = 2R + T; therefore, by the converse part of 10.15, its two parts 2R and T would be commensurable. Since T is commensurable with K, 2R would consequently be commensurable with K, contrary to Step 4. Hence T is incommensurable with K. [10.12, 10.15]

**Step 6.** The square on CB is therefore incommensurable with the square on the assigned rational straight line, so CB is irrational. Let this remainder be called an **apotome**, as required. [D10.1.4]

**USED:** 10.12, 10.13, 10.15, 10.21, 2.7, D10.1.1, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 10.11, 10.13, 10.15, 10.16, 10.6, 2.7, D10.1.4
**Jaccard:** 0.333 — AI adds ['10.12', '10.21', 'D10.1.1', 'D10.1.2', 'D10.1.3']; Human adds ['10.11', '10.16', '10.6']

## Proposition 10.74
**Statement:** If from a medial straight line there be subtracted a medial straight line which is commensurable with the whole in square only, and which contains with the whole a rational rectangle, the remainder is irrational. And let it be called a first apotome of a medial straight line.

**Step 1.** Let a be the whole medial straight line, b the medial straight line subtracted, and c = a − b the remainder. By hypothesis, a and b are commensurable in square only, and the rectangle R contained by a and b is rational. Thus their squares a² and b² are commensurable. Let Q be the square on the assigned rational straight line. [D10.1.2, D10.1.4]

**Step 2.** Since a is medial, its square a² is an irrational area and therefore is incommensurable with Q. Put P = a² + b². Since a² and b² are commensurable, P is commensurable with a²; consequently P is incommensurable with Q. [10.21, D10.1.4, 10.15, 10.13]

**Step 3.** Put T = 2R. Since R is rational, R and Q have a common measure. The same measure measures T, so T is commensurable with Q. Since P is incommensurable with Q, it is also incommensurable with T. [D10.1.4, D10.1.1, 10.13]

**Step 4.** Use II.7, the direct square identity for the given subtraction: the squares on the whole a and the subtracted segment b together equal twice their rectangle together with the square on the remainder c. Hence P = T + c². Since the whole P is incommensurable with T, the remaining area c² is incommensurable with T. [2.7, 10.16]

**Step 5.** Since T is commensurable with Q but incommensurable with c², Q is also incommensurable with c². Therefore the square on c is irrational, and its side c is irrational. Thus the remainder is irrational; let it be called a **first apotome of a medial straight line**. [10.13, D10.1.4]

**USED:** 10.13, 10.15, 10.16, 10.21, 2.7, D10.1.1, D10.1.2, D10.1.4
**Human refs (from References field):** 10.16, 2.7, D10.1.4
**Jaccard:** 0.375 — AI adds ['10.13', '10.15', '10.21', 'D10.1.1', 'D10.1.2']

## Proposition 10.75
**Statement:** If from a medial straight line there be subtracted a medial straight line which is commensurable with the whole in square only, and which contains with the whole a medial rectangle, the remainder is irrational; and let it be called a second apotome of a medial straight line.

**Step 1.** Let AB be the whole medial straight line, AC the subtracted medial straight line, and CB the remainder, with C between A and B. Write a = AB, b = AC, and c = CB; squares and products below denote areas. By hypothesis, a² and b² are commensurable, and M = ab is medial [D10.1.2]. Put S = a² + b². By II.7,
S = 2M + c².
We use half this identity so that the given medial rectangle M itself enters the final argument: putting H = S/2 gives
H = M + c²/2. [2.7]

**Step 2.** Since a² and b² are commensurable, their sum S is commensurable with a² [10.15]. Also H and S are commensurable, since H measures S twice [D10.1.1]. Consequently H is commensurable with a² [10.12].

**Step 3.** Form a rectangle of area H with one side a, and denote its other side by d. This construction is available by taking a triangular half of each of the squares a² and b², applying each triangle to the side a at a right angle, and combining the two resulting breadths [1.34, 1.44]. The rectangle H and the square a² have the same height a, so
H : a² = d : a. [6.1]
Since H and a² are commensurable, d and a are commensurable in length [10.11].

**Step 4.** Because a is medial and d is commensurable with it in length, d is medial [10.23]. Hence H, the rectangle contained by the medial straight lines a and d, which are commensurable in length, is medial [10.24].

**Step 5.** Suppose that c² were rational. Then it would be commensurable with the square on the assigned rational straight line [D10.1.4]. Since c²/2 is commensurable with c², it too would be commensurable with that assigned square and therefore rational [D10.1.1, 10.12, D10.1.4]. But Step 1 shows that the medial area H exceeds the medial area M by the positive area c²/2. A medial area cannot exceed a medial area by a rational area [10.26]. Thus c² is irrational, and its side c = CB is irrational [D10.1.4]. Therefore the remainder is irrational; let it be called a **second apotome of a medial straight line**.

**USED:** 1.34, 1.44, 10.11, 10.12, 10.15, 10.23, 10.24, 10.26, 2.7, 6.1, D10.1.1, D10.1.2, D10.1.4
**Human refs (from References field):** 10.11, 10.13, 10.15, 10.20, 10.22, 10.23, 10.28, 10.6, 10.73, 2.7, 6.1
**Jaccard:** 0.263 — AI adds ['1.34', '1.44', '10.12', '10.24', '10.26', 'D10.1.1', 'D10.1.2', 'D10.1.4']; Human adds ['10.13', '10.20', '10.22', '10.28', '10.6', '10.73']

## Proposition 10.76
**Statement:** If from a straight line there be subtracted a straight line which is incommensurable in square with the whole and which with the whole makes the squares on them added together rational, but the rectangle contained by them medial, the remainder is irrational; and let it be called minor.

**Step 1.** Let AB be the whole straight line, BC the straight line subtracted, and AC the remainder, with C between A and B. By hypothesis, AB and BC are incommensurable in square, the area S = AB² + BC² is rational, and the rectangle M = AB·BC is medial. Let Q be the square on the assigned rational straight line. Then S is commensurable with Q, while M, being medial, is irrational and therefore incommensurable with Q. [10.21, D10.1.4]

**Step 2.** We take the direct route through the square of the remainder, since this relates exactly the two areas specified in the hypotheses. By the identity for a straight line cut into two segments,
AB² + BC² = 2(AB·BC) + AC².
Thus, writing D = AC², we have S = 2M + D. [2.7]

**Step 3.** The areas M and 2M are commensurable, since M measures both. Since M is incommensurable with Q, it follows that 2M is also incommensurable with Q. [D10.1.1, 10.13]

**Step 4.** Since S and Q are commensurable, and Q is incommensurable with 2M, S is incommensurable with 2M. [10.13]

**Step 5.** Now S = 2M + D. Since this whole is incommensurable with its part 2M, the two parts 2M and D are incommensurable. Consequently their sum S is also incommensurable with D. These are respectively the second and first assertions of the same proposition. [10.16]

**Step 6.** Since Q is commensurable with S, whereas S is incommensurable with D, Q is incommensurable with D. Hence D = AC² is an irrational area, and its side AC is an irrational straight line. Therefore the remainder is irrational; let it be called **minor**. [10.13, D10.1.4]

**USED:** 10.13, 10.16, 10.21, 2.7, D10.1.1, D10.1.4
**Human refs (from References field):** 10.16, 10.33, 2.7
**Jaccard:** 0.286 — AI adds ['10.13', '10.21', 'D10.1.1', 'D10.1.4']; Human adds ['10.33']

## Proposition 10.77
**Statement:** If from a straight line there be subtracted a straight line which is incommensurable in square with the whole, and which with the whole makes the sum of the squares on them medial, but twice the rectangle contained by them rational, the remainder is irrational: and let it be called that which produces with a rational area a medial whole.

**Step 1.** Let AB be the whole straight line, AC the subtracted straight line, and CB the remainder. By hypothesis, AB and AC are incommensurable in square, the sum M of their squares is medial, and twice their rectangle, R, is rational. Write Q for the square on CB. Applying 2.7 directly to the given subtraction gives
M = R + Q.
[2.7]

**Step 2.** Let U be the square on the assigned rational straight line. Since R is rational, R is commensurable with U. Since M is medial, it is irrational, and therefore incommensurable with U. Consequently M is incommensurable with R: this follows from 10.13 applied to the commensurable areas U and R. [D10.1.4, 10.21, 10.13]

**Step 3.** Use the whole-and-part clause of 10.16, which applies immediately to the identity M = R + Q: since the whole M is incommensurable with its part R, the original parts R and Q are incommensurable with one another. [10.16]

**Step 4.** Since R and U are commensurable, while R and Q are incommensurable, 10.13 shows that U and Q are incommensurable. Thus Q is an irrational area, and its side CB is an irrational straight line. Moreover, by Step 1, its square Q together with the rational area R makes the medial whole M. Therefore the remainder is irrational; and let it be called **that which produces with a rational area a medial whole**. [10.13, D10.1.4, 2.7]

**USED:** 10.13, 10.16, 10.21, 2.7, D10.1.4
**Human refs (from References field):** 10.16, 10.34, 2.7
**Jaccard:** 0.333 — AI adds ['10.13', '10.21', 'D10.1.4']; Human adds ['10.34']

## Proposition 10.78
**Statement:** If from a straight line there be subtracted a straight line which is incommensurable in square with the whole and which with the whole makes the sum of the squares on them medial, twice the rectangle contained by them medial, and further the squares on them incommensurable with twice the rectangle contained by them, the remainder is irrational; and let it be called that which produces with a medial area a medial whole.

**Step 1.** Let AB be the whole straight line, and let AC be subtracted from it, leaving CB, with C between A and B. By hypothesis, AB and AC are incommensurable in square, and the areas
M = AB² + AC² and N = 2(AB·AC)
are medial and incommensurable with one another. By II.7,
AB² + AC² = 2(AB·AC) + CB².
Thus M exceeds N by precisely the square on CB. [2.7]

**Step 2.** Take the direct medial-area difference route, since both M and N are already medial by hypothesis. A medial area does not exceed a medial area by a rational area. Consequently, their difference, the square on CB, cannot be rational. [10.26]

**Step 3.** By the definition of irrational areas and their sides, the square on CB is therefore irrational, and its side CB is irrational. Hence the remainder is irrational; under the stated hypotheses, let it be called **that which produces with a medial area a medial whole**. Indeed, its square together with the medial area N equals the medial whole M. [D10.1.4]

**USED:** 10.26, 2.7, D10.1.4
**Human refs (from References field):** 10.11, 10.20, 10.22, 10.35, 10.73, 2.7, 6.1
**Jaccard:** 0.111 — AI adds ['10.26', 'D10.1.4']; Human adds ['10.11', '10.20', '10.22', '10.35', '10.73', '6.1']

## Proposition 10.79
**Statement:** To an apotome only one rational straight line can be annexed which is commensurable with the whole in square only.

**Step 1.** Let x be an apotome. By its defining construction, x = a − b, where a and b are rational straight lines commensurable in square only. Thus b is one annex of the required kind. Write u² for the square on u and uv for the rectangle contained by u and v. [10.73]

**Step 2.** Suppose that another rational straight line d, different from b, can be annexed to x, and put c = x + d. By hypothesis, c and d are commensurable in square only. Since d is rational, transitivity of commensurability between their squares shows that c is rational also. Interchanging the two representations if necessary, take d > b; then c > a. Consequently the rectangle cd is greater than ab: with corresponding sides placed along the same rays from a common corner, ab is a proper part of cd. [D10.1.2, D10.1.3, 10.12, CN5]

**Step 3.** The pairs a, b and c, d each consist of rational straight lines commensurable in square only. Therefore ab and cd are medial areas, being equal to squares on medial straight lines. This leads directly to the medial-area obstruction used below. [10.21]

**Step 4.** Apply the square-and-rectangle identity to a = x + b and c = x + d. It gives

a² + b² = x² + 2ab,

c² + d² = x² + 2cd.

Subtracting and cancelling the common square x², we obtain

(c² + d²) − (a² + b²) = 2(cd − ab).

The area on the right is positive by Step 2. [2.7, CN3]

**Step 5.** Since a, b, c, d are rational straight lines, their squares are rational areas. By transitivity of commensurability and the proposition concerning commensurable wholes and parts, the two sums a² + b² and c² + d², and their positive difference, are commensurable with the square on the assigned rational straight line. Hence 2(cd − ab) is rational. Its half cd − ab is commensurable with it—the half itself measures both—and is therefore rational as well. [D10.1.1, D10.1.3, D10.1.4, 10.12, 10.15]

**Step 6.** Thus the medial area cd exceeds the medial area ab by the rational area cd − ab. This contradicts the directly applicable proposition that a medial area does not exceed a medial area by a rational area. Therefore no second annex d exists. Together with the existence established in Step 1, this proves that to an apotome only one rational straight line can be annexed which is commensurable with the whole in square only. [10.26]

**USED:** 10.12, 10.15, 10.21, 10.26, 10.73, 2.7, CN3, CN5, D10.1.1, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 10.21, 10.26, 10.73, 2.7
**Jaccard:** 0.333 — AI adds ['10.12', '10.15', 'CN3', 'CN5', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.1.4']

## Proposition 10.80
**Statement:** To a first apotome of a medial straight line only one medial straight line can be annexed which is commensurable with the whole in square only and which contains with the whole a rational rectangle.

**Step 1.** Let a be a first apotome of a medial straight line. By 10.74, there are medial straight lines x and y such that a = x − y, the lines x and y are commensurable in square only, and the rectangle xy is rational. Suppose that another medial straight line v can be annexed with the required properties, giving a whole u: thus a = u − v, u and v are commensurable in square only, and uv is rational. Since v is medial, u is medial also, by 10.23. If the annexes differ, interchange the two representations if necessary so that y > v. Then x = a + y > a + v = u, and consequently xy > uv: the greater rectangle contains a rectangle equal to the lesser as a proper part. [10.74, 10.23, CN5]

**Step 2.** Put S = x² + y² and T = u² + v², where squares and products denote areas. Since x² and y² are commensurable, S is commensurable with x² by 10.15. Construct a square equal to S by 2.14. Its side is therefore commensurable in square with x, by D10.1.2, and is medial by 10.23. Thus S is a medial area. The same argument, using u² and v², shows that T is a medial area. [10.15, 2.14, D10.1.2, 10.23]

**Step 3.** Write P = xy and Q = uv, and let D = P − Q, which is positive by Step 1. Both P and Q are rational areas, hence commensurable with the square on the assigned rational straight line. They are consequently commensurable with one another by 10.12. Since P = Q + D, the converse part of 10.15 makes D commensurable with Q. By 10.12, D is therefore commensurable with the assigned rational square and is rational. Moreover, 2D is commensurable with D by 10.15, so 2D is likewise rational. [D10.1.4, 10.12, 10.15]

**Step 4.** Apply 2.7, the identity directly adapted to a whole and a subtracted segment. Because x − y = a and u − v = a, it gives
S = a² + 2P,     T = a² + 2Q.
Subtracting the common parts yields
S − T = 2(P − Q) = 2D.
Thus the medial area S exceeds the medial area T by the positive rational area 2D. [2.7, CN3]

**Step 5.** This is impossible by 10.26: a medial area does not exceed a medial area by a rational area. This direct medial-area obstruction rules out unequal annexes. Hence y = v, and the annex is unique. Its existence is supplied by the defining construction in 10.74. Therefore to a first apotome of a medial straight line only one medial straight line can be annexed which is commensurable with the whole in square only and contains with the whole a rational rectangle. [10.26, 10.74]

**USED:** 10.12, 10.15, 10.23, 10.26, 10.74, 2.14, 2.7, CN3, CN5, D10.1.2, D10.1.4
**Human refs (from References field):** 10.15, 10.23, 10.26, 10.74, 2.7
**Jaccard:** 0.455 — AI adds ['10.12', '2.14', 'CN3', 'CN5', 'D10.1.2', 'D10.1.4']

## Proposition 10.81
**Statement:** To a second apotome of a medial straight line only one medial straight line can be annexed which is commensurable with the whole in square only and which contains with the whole a medial rectangle.

**Step 1.** Let x be the given second apotome of a medial straight line. By 10.75, write x = a − b, where a and b are medial, commensurable in square only, and contain a medial rectangle. Suppose also x = c − d, with c and d satisfying the same conditions. We shall reduce these two annexations to annexations of one ordinary apotome, where the earlier uniqueness theorem applies naturally. In what follows, (u,v) denotes either (a,b) or (c,d). Write u² for a square and uv for a rectangle. [10.75]

**Step 2.** Fix one rational straight line r. Apply the areas u², v², and uv to r, obtaining breadths p, q, and t respectively; thus rp = u², rq = v², and rt = uv. Each breadth is rational by 10.22: for the third application, uv is the square on a medial straight line because it is a medial area. [10.22]

**Step 3.** Since u² and v² are commensurable, their breadths p and q are commensurable in length: rectangles of equal height have the ratio of their bases, and proportional magnitudes preserve commensurability. Put P = p + q and Q = 2t. Then P is commensurable in length with p, and Q with t. [6.1, 10.11, 10.15]

**Step 4.** The lines P and Q are rational. Indeed, length-commensurable lines have squares in the ratio of square numbers, so their squares are commensurable. Consequently P² is commensurable with p², and Q² with t². Since p and t are rational, transitivity makes P² and Q² commensurable with the assigned rational square. It also follows that P and Q are commensurable in square with one another. [10.9, 10.6, 10.12, D10.1.3]

**Step 5.** Nevertheless, P and Q are incommensurable in length. For equal-height rectangles give
p : t = u² : uv = u : v.
Since u and v are incommensurable in length, so are p and t. As P is commensurable with p and Q with t, applying 10.13 twice shows that P and Q are incommensurable in length. [6.1, 10.11, 10.13]

**Step 6.** Distributivity of rectangles and the identity in 2.7 give
rP = u² + v² = 2uv + (u − v)² = rQ + x².
Thus P > Q, and the breadth w obtained by applying x² to r is precisely P − Q. By Steps 4–5, P and Q are rational and commensurable in square only. Therefore w is an ordinary apotome. The same w results from either original annexation, since x and r are fixed. [2.1, 2.7, 10.73]

**Step 7.** For each original pair, Q is a rational annex to w, and its whole P is commensurable with it in square only. By 10.79 this annex Q is unique. Hence the values of Q obtained from (a,b) and (c,d) are equal. Since rQ = 2uv, it follows that ab = cd. [10.79]

**Step 8.** If b and d were unequal, interchange their names if necessary so that d > b. Since a = x + b and c = x + d, we would also have c > a. The rectangle cd would then strictly exceed ab, contrary to Step 7. Thus d = b, and consequently c = a. The annex supplied by the definition exists and is unique: only one medial straight line can be annexed with the required square-commensurability and medial rectangle. [2.1, CN5, 10.75]

**USED:** 10.11, 10.12, 10.13, 10.15, 10.22, 10.6, 10.73, 10.75, 10.79, 10.9, 2.1, 2.7, 6.1, CN5, D10.1.3
**Human refs (from References field):** 10.11, 10.13, 10.15, 10.22, 10.23, 10.6, 10.73, 10.75, 10.79, 2.7, 6.1
**Jaccard:** 0.625 — AI adds ['10.12', '10.9', '2.1', 'CN5', 'D10.1.3']; Human adds ['10.23']

## Proposition 10.82
**Statement:** To a minor straight line only one straight line can be annexed which is incommensurable in square with the whole and which makes, with the whole, the sum of the squares on them rational but twice the rectangle contained by them medial.

**Step 1.** Let x be the given minor straight line. Write u² for the square on u and uv for the rectangle contained by u and v. By the characterization of a minor, there is an annex b such that x+b and b are incommensurable in square, (x+b)²+b² is rational, and P=(x+b)b is medial. [10.76]

**Step 2.** The area 2P is also medial. Indeed, let m be the medial side of a square equal to P. The lines m and 2m are commensurable in length, being both measured by m; hence 2m is medial. Their rectangle is therefore medial, and that rectangle equals 2m²=2P. Thus at least one annex has all the required properties. [D10.1.1, 10.23, 10.24]

**Step 3.** Suppose that two distinct annexes b and c have the required properties. Interchange their names if necessary so that c>b. Put
R_b=(x+b)²+b²,  M_b=2(x+b)b,
R_c=(x+c)²+c²,  M_c=2(x+c)c.
By hypothesis, R_b and R_c are rational, while M_b and M_c are medial. Since c>b and x+c>x+b, each square in R_c is greater than the corresponding square in R_b. Consequently R_c>R_b. [CN5]

**Step 4.** We use the square-of-the-remainder identity directly, because the remainder x is the same for both annexes. Applied to the whole x+b and its segments x,b, and then to x+c and its segments x,c, it gives
R_b=x²+M_b,  R_c=x²+M_c.
Subtracting yields
R_c−R_b=M_c−M_b>0. [2.7, CN3]

**Step 5.** Let Q be the square on the assigned rational straight line. Since R_b and R_c are rational, both are commensurable with Q, and hence with one another. In the decomposition R_c=R_b+(R_c−R_b), the whole is commensurable with the first part; therefore the two parts are commensurable. Thus R_c−R_b is commensurable with R_b and consequently with Q. The positive difference R_c−R_b is therefore rational. [D10.1.4, 10.12, 10.15]

**Step 6.** By Step 4, the medial area M_c exceeds the medial area M_b by this rational area. But a medial area does not exceed a medial area by a rational area. This contradiction excludes distinct annexes. Together with Step 2, it proves that to a minor straight line exactly one straight line can be annexed which is incommensurable in square with the whole and makes the sum of their squares rational but twice their rectangle medial. [10.26]

**USED:** 10.12, 10.15, 10.23, 10.24, 10.26, 10.76, 2.7, CN3, CN5, D10.1.1, D10.1.4
**Human refs (from References field):** 10.26, 10.76
**Jaccard:** 0.182 — AI adds ['10.12', '10.15', '10.23', '10.24', '2.7', 'CN3', 'CN5', 'D10.1.1', 'D10.1.4']

## Proposition 10.83
**Statement:** To a straight line which produces with a rational area a medial whole only one straight line can be annexed which is incommensurable in square with the whole straight line and which with the whole straight line makes the sum of the squares on them medial, but twice the rectangle contained by them rational.

**Step 1.** Let a be a straight line which produces with a rational area a medial whole. By the designation in 10.77, it has an annex b such that b is incommensurable in square with a+b, the area S_b=(a+b)²+b² is medial, and the area R_b=2(a+b)b is rational. Suppose that a different annex c has the same properties, and put S_c=(a+c)²+c² and R_c=2(a+c)c. Interchanging the names if necessary, let b>c. Here squares and products denote the corresponding square and rectangular areas. [10.77]

**Step 2.** We compare the medial sums directly: the natural identity is 2.7, since it expresses each sum as the square on the same remainder a plus its rational double rectangle. Applied to the wholes a+b and a+c, it gives
S_b=a²+R_b,
S_c=a²+R_c. [2.7]

**Step 3.** Since b>c and a+b>a+c, the square on each of the former lines exceeds the square on the corresponding latter line, as follows from 2.4 applied to the greater line cut at the length of the lesser. Hence S_b>S_c. Subtracting the equal expressions in Step 2 gives
D:=S_b−S_c=R_b−R_c>0. [2.4, CN3]

**Step 4.** Both R_b and R_c are rational areas, so each is commensurable with the square Q on the assigned rational straight line. Consequently R_b and R_c are commensurable with one another. Since R_b=R_c+D, the converse part of 10.15 shows that D is commensurable with R_c. Since R_c is commensurable with Q, so is D. Therefore D is a rational area. [D10.1.4, 10.12, 10.15]

**Step 5.** Thus the medial area S_b exceeds the medial area S_c by the positive rational area D. This is impossible, for a medial area does not exceed a medial area by a rational area. Therefore two distinct qualifying annexes cannot exist. Since an annex with the stated properties exists by the designation of the given straight line, exactly one can be annexed, as required. [10.26, 10.77]

**USED:** 10.12, 10.15, 10.26, 10.77, 2.4, 2.7, CN3, D10.1.4
**Human refs (from References field):** 10.26, 10.77
**Jaccard:** 0.250 — AI adds ['10.12', '10.15', '2.4', '2.7', 'CN3', 'D10.1.4']

## Proposition 10.84
**Statement:** To a straight line which produces with a medial area a medial whole only one straight line can be annexed which is incommensurable in square with the whole straight line and which with the whole straight line makes the sum of the squares on them medial and twice the rectangle contained by them both medial and also incommensurable with the sum of the squares on them.

**Step 1.** Let d be a straight line which produces with a medial area a medial whole. By X.78, it has an annex b such that the whole a = d + b is incommensurable in square with b, while S = a² + b² and T = 2ab are medial areas incommensurable with one another. Suppose another annex b′ has the same properties, and put a′ = d + b′, S′ = a′² + b′², and T′ = 2a′b′. Here products denote rectangular areas and squares denote square areas. We shall prove b = b′. [10.78]

**Step 2.** II.7 applies directly to each whole and its annex, giving
S = T + d² and S′ = T′ + d².
Thus S > T and S′ > T′, and both differences equal the same square d². [2.7]

**Step 3.** Use rational breadths to reduce the question directly to uniqueness of an annex to an apotome. Fix a rational straight line r, and apply S, T, S′, T′ to r as rectangles, obtaining respective breadths p, q, p′, q′. Thus
rp = S, rq = T, rp′ = S′, rq′ = T′.
The applications can be made by successive applications of I.44. Since all four areas are medial, X.22 shows that all four breadths are rational straight lines. [1.44, 10.22]

**Step 4.** The squares on p and q are each commensurable with the square on the assigned rational straight line; hence they are commensurable with one another. Thus p and q are commensurable in square. The same holds for p′ and q′. On the other hand, VI.1 gives p:q = S:T and p′:q′ = S′:T′. Since the areas in each pair are incommensurable, X.11 shows that the corresponding breadths are incommensurable in length. Consequently, p and q, and likewise p′ and q′, are commensurable in square only. [D10.1.3, D10.1.2, 10.12, 6.1, 10.11]

**Step 5.** Since S > T and S′ > T′, we have p > q and p′ > q′. By subtraction and the distributivity of rectangles,
r(p − q) = S − T = d² = S′ − T′ = r(p′ − q′).
Equal rectangles on the same height have equal breadths, so p − q = p′ − q′. Call this common remainder h. Since h is obtained by subtracting from a rational straight line another rational straight line commensurable with it in square only, h is an apotome. [6.1, 2.1, CN3, 10.73]

**Step 6.** Both q and q′ are therefore rational annexes to the same apotome h, each commensurable in square only with its corresponding whole, p or p′. By the uniqueness of the annex to an apotome, q = q′. Hence T = rq = rq′ = T′, and therefore ab = a′b′. [10.79]

**Step 7.** If b > b′, then a = d + b > d + b′ = a′. The rectangle ab would consequently strictly contain a rectangle equal to a′b′ and would be greater than it, contrary to their equality. The assumption b′ > b gives the same contradiction. Therefore b = b′. An admissible annex exists by Step 1, and any other is equal to it. Thus exactly one straight line with all the stated properties can be annexed to d. [CN5, 10.78]

**USED:** 1.44, 10.11, 10.12, 10.22, 10.73, 10.78, 10.79, 2.1, 2.7, 6.1, CN3, CN5, D10.1.2, D10.1.3
**Human refs (from References field):** 10.11, 10.22, 10.73, 10.78, 10.79, 2.7, 6.1
**Jaccard:** 0.500 — AI adds ['1.44', '10.12', '2.1', 'CN3', 'CN5', 'D10.1.2', 'D10.1.3']

## Proposition 10.85
**Statement:** To find the first apotome.

**Step 1.** Let r be the rational straight line set out. Construct a first binomial straight line, and denote its greater term by a and its lesser term by b. We use the first-binomial construction because it already supplies the conditions required of the whole and annex of a first apotome. [10.48]

**Step 2.** By the meaning of binomial, a and b are rational straight lines commensurable in square only. Since this binomial is first, a is commensurable in length with r, and there is a straight line c, commensurable in length with a, such that the square on a equals the squares on b and c together. [10.36, D10.2.1]

**Step 3.** Take AB equal to a and cut off AC equal to b, leaving CB. This is possible since a is greater than b. Since a rational straight line AC, commensurable with AB in square only, has been subtracted from the rational straight line AB, the remainder CB is an apotome. Its whole is AB and its annex is AC. [1.3, 10.73]

**Step 4.** The square on the whole AB exceeds the square on its annex AC by the square on c, which is commensurable in length with AB; moreover, AB is commensurable in length with the rational straight line r set out. Thus CB satisfies the definition of a first apotome. Therefore a first apotome has been found. [D10.3.1]

**USED:** 1.3, 10.36, 10.48, 10.73, D10.2.1, D10.3.1
**Human refs (from References field):** 10.6, 10.73, 10.9, 5.19, D10.3.1
**Jaccard:** 0.222 — AI adds ['1.3', '10.36', '10.48', 'D10.2.1']; Human adds ['10.6', '10.9', '5.19']

## Proposition 10.86
**Statement:** To find the second apotome.

**Step 1.** Let r be the rational straight line set out. Construct a second binomial by 10.49, and let its greater and lesser terms be a and b. We choose this construction because its terms already have the square-difference and commensurability properties required for a second apotome. By the definition of a binomial in 10.36, a and b are rational straight lines commensurable in square only. [10.49, 10.36]

**Step 2.** Since the constructed binomial is second, b is commensurable in length with r, and the square on a exceeds the square on b by the square on a straight line c commensurable in length with a. These are precisely the conditions in the definitions of the first group of binomials and of its second species. [D10.2.1, D10.2.2]

**Step 3.** Since a is greater than b, cut off from a a straight line equal to b, and call the remainder x. Because the whole a and the subtracted straight line b are rational and commensurable in square only, x is an apotome. Its whole is a and its annex is b. [1.3, 10.73]

**Step 4.** The annex b is commensurable in length with the rational straight line r, and the square on the whole a exceeds that on the annex b by the square on c, which is commensurable in length with a. Therefore, by the definition of the second apotome, x is a second apotome. Thus the required second apotome has been found. [D10.3.2]

**USED:** 1.3, 10.36, 10.49, 10.73, D10.2.1, D10.2.2, D10.3.2
**Human refs (from References field):** 10.6, 10.73, 10.9, 5.19, D10.3.2
**Jaccard:** 0.200 — AI adds ['1.3', '10.36', '10.49', 'D10.2.1', 'D10.2.2']; Human adds ['10.6', '10.9', '5.19']

## Proposition 10.87
**Statement:** To find the third apotome.

**Step 1.** Let r be the rational straight line set out. By 10.50, construct a third binomial relative to r, and let its greater and lesser terms be a and b. We choose this earlier construction because its defining conditions provide exactly the terms needed here, with subtraction replacing addition. [10.50]

**Step 2.** Since these are the terms of a binomial, a and b are rational straight lines commensurable in square only. Since the binomial is third, neither a nor b is commensurable in length with r; moreover, the square on a exceeds the square on b by the square on a straight line c commensurable in length with a. These are the common square-difference condition and the distinguishing condition for a third binomial. [10.36, D10.2.1, D10.2.3]

**Step 3.** From a cut off a straight line equal to b, and call the remainder x. This is possible since a is greater than b. Because a and b are rational and commensurable in square only, x is an apotome. Its whole straight line is a, and its annex is b, since adjoining b to x restores a. [1.3, 10.73]

**Step 4.** Neither the whole a nor the annex b is commensurable in length with r, and the square on the whole exceeds the square on the annex by the square on c, which is commensurable in length with the whole. Therefore, by the definition, x is a third apotome. Thus the third apotome has been found. [D10.3.3]

**USED:** 1.3, 10.36, 10.50, 10.73, D10.2.1, D10.2.3, D10.3.3
**Human refs (from References field):** 10.6, 10.73, 10.9, 5.19, 5.22, D10.3.3
**Jaccard:** 0.182 — AI adds ['1.3', '10.36', '10.50', 'D10.2.1', 'D10.2.3']; Human adds ['10.6', '10.9', '5.19', '5.22']

## Proposition 10.88
**Statement:** To find the fourth apotome.

**Step 1.** Construct a fourth binomial by 10.51. Let its greater and lesser terms be a and b, and let r be the rational straight line set out in that construction. By the meaning of binomial, a and b are rational straight lines commensurable in square only (10.36). We use this earlier construction because its terms already satisfy the conditions needed for a fourth apotome.

**Step 2.** By the definition of a fourth binomial, a is commensurable in length with r, and the square on a exceeds the square on b by the square on a straight line c incommensurable in length with a. Thus a² − b² = c² (D10.2.4).

**Step 3.** Since a > b, cut off from a a straight line equal to b, leaving x (1.3). Since a and b are rational and commensurable in square only, their difference x is an apotome (10.73).

**Step 4.** The annex of x is b, and the whole obtained by annexing b is a. The whole a is commensurable in length with r, while its square exceeds the square on the annex b by the square on c, which is incommensurable in length with a. Therefore x is a fourth apotome (D10.3.4). Hence the required fourth apotome has been found.

**USED:** 1.3, 10.36, 10.51, 10.73, D10.2.4, D10.3.4
**Human refs (from References field):** 10.6, 10.73, 10.9, 5.19, D10.3.4
**Jaccard:** 0.222 — AI adds ['1.3', '10.36', '10.51', 'D10.2.4']; Human adds ['10.6', '10.9', '5.19']

## Proposition 10.89
**Statement:** To find the fifth apotome.

**Step 1.** Set out a rational straight line r. By 10.52 construct a fifth binomial relative to r, and denote its greater term by a and its lesser term by b. We use this construction because its terms already satisfy the relations required of the whole and annex of a fifth apotome. By the meaning of binomial, a and b are rational straight lines commensurable in square only. [10.52, 10.36]

**Step 2.** By the definition of a fifth binomial, b is commensurable in length with r, and the square on a exceeds the square on b by the square on a straight line d incommensurable in length with a. Thus a² = b² + d². [D10.2.4, D10.2.5]

**Step 3.** Let AB be the greater term a. Cut off BC equal to b, with C between A and B. Since AB and BC are rational and commensurable in square only, the remainder AC is an apotome, with whole AB and annex BC. [1.3, 10.73]

**Step 4.** The square on the whole AB exceeds the square on the annex BC by the square on d, which is incommensurable in length with AB; moreover, the annex BC is commensurable in length with the rational straight line r set out. These are precisely the defining conditions of a fifth apotome. Therefore AC is the required fifth apotome. [D10.3.4, D10.3.5]

**USED:** 1.3, 10.36, 10.52, 10.73, D10.2.4, D10.2.5, D10.3.4, D10.3.5
**Human refs (from References field):** 10.6, 10.73, 10.9, 5.19, D10.3.5
**Jaccard:** 0.182 — AI adds ['1.3', '10.36', '10.52', 'D10.2.4', 'D10.2.5', 'D10.3.4']; Human adds ['10.6', '10.9', '5.19']

## Proposition 10.90
**Statement:** To find the sixth apotome.

**Step 1.** Fix the rational straight line U used as reference. By 10.53 construct a sixth binomial, and let A and B be its greater and lesser terms. We use this construction directly because its terms already satisfy the conditions needed for a sixth apotome. [10.53]

**Step 2.** Since A + B is binomial, A and B are rational straight lines commensurable in square only. Since it is a sixth binomial, neither A nor B is commensurable in length with U, and the square on A exceeds the square on B by the square on a straight line C incommensurable in length with A. Thus A² = B² + C². [10.36; D10.2.4; D10.2.6]

**Step 3.** From A cut off a straight line equal to B, and call the remainder R. Because a rational straight line has been subtracted from a rational straight line commensurable with it in square only, R is an apotome. Its whole is A and its annex is B, since R + B = A. [1.3; 10.73]

**Step 4.** The square on this whole A exceeds the square on its annex B by the square on C, which is incommensurable in length with A; moreover, neither the whole nor the annex is commensurable in length with U. These are precisely the defining conditions of a sixth apotome. Therefore R is the required sixth apotome. [D10.3.4; D10.3.6]

**USED:** 1.3, 10.36, 10.53, 10.73, D10.2.4, D10.2.6, D10.3.4, D10.3.6
**Human refs (from References field):** 10.6, 10.73, 10.9, 5.19, 5.22, D10.3.6
**Jaccard:** 0.167 — AI adds ['1.3', '10.36', '10.53', 'D10.2.4', 'D10.2.6', 'D10.3.4']; Human adds ['10.6', '10.9', '5.19', '5.22']

## Proposition 10.91
**Statement:** If an area be contained by a rational straight line and a first apotome, the âsideâ of the area is an apotome.

**Step 1.** Let a be the given rational straight line, and write the first apotome as b−c, where b is its whole and c its annex. Thus b>c; b and c are rational and commensurable in square only. By the definition of a first apotome, b is commensurable in length with a, and there is a straight line d, commensurable in length with b, such that b²−c²=d². Here products denote rectangles and squares denote square areas. [10.73, D10.3.1]

**Step 2.** Put h=c/2. Since c<b, the square h² is less than the square on half of b. Apply to b a rectangle equal to h² and deficient by a square. This divides b into positive parts u,v satisfying
u+v=b,  uv=h²=c²/4.
The parts are unequal, since equality would give c=b; label them so that u>v. We use the commensurable-division direction of X.17: the condition b²−c²=d², with d commensurable with b, is exactly its hypothesis. Hence u and v are commensurable in length. Each is therefore commensurable with their sum b, and consequently with a. [6.28, 10.17, 10.15, 10.12]

**Step 3.** Since u and v are commensurable in length with the rational line a, they are rational, and the rectangles au and av are rational. Construct straight lines x,y such that
x²=au,  y²=av.
Then x>y. Their squares are rational areas, so x and y are rational straight lines. Moreover, their squares, being commensurable with the same rational square, are commensurable with one another; thus x and y are commensurable in square. [D10.1.3, 10.19, 2.14, 6.1, D10.1.4, 10.12, D10.1.2]

**Step 4.** We show that 2xy=ac. By the ratios of rectangles of equal height,
x²:y²=au:av=u:v=u²:uv=u²:h².
The converse proportionality theorem for similar figures therefore gives x:y=u:h, and alternation gives u:x=h:y. On the other hand, x²=au gives u:x=x:a. Consequently x:a=h:y, whence xy=ah. Since c=2h, it follows that 2xy=ac. [6.1, 6.22, 5.16, 6.17, 5.11, 6.16, 2.1]

**Step 5.** Because a is commensurable in length with b, while b is incommensurable in length with c, a and c are incommensurable in length. They are both rational; hence the rectangle ac is irrational. If x and y were commensurable in length, their rectangle xy would be rational. Its double would also be rational: xy and 2xy have a common measure, so commensurability with the rational reference square passes from xy to 2xy. This contradicts 2xy=ac. Thus x and y are incommensurable in length. [10.13, 10.21, 10.19, D10.1.1, 10.12, D10.1.4]

**Step 6.** We have shown that x and y are rational straight lines commensurable in square only, with x>y. Their difference x−y is therefore an apotome. [10.73]

**Step 7.** Finally, the square identity for a difference, together with rectangle decomposition, gives
(x−y)²=x²+y²−2xy
=au+av−ac
=a(u+v)−ac
=ab−ac
=a(b−c).
Thus the square on the apotome x−y equals the area contained by the given rational straight line and the first apotome. Therefore the side of that area is an apotome, as required. [2.7, 2.1, CN3]

**USED:** 10.12, 10.13, 10.15, 10.17, 10.19, 10.21, 10.73, 2.1, 2.14, 2.7, 5.11, 5.16, 6.1, 6.16, 6.17, 6.22, 6.28, CN3, D10.1.1, D10.1.2, D10.1.3, D10.1.4, D10.3.1
**Human refs (from References field):** 10.11, 10.12, 10.13, 10.15, 10.17, 10.19, 10.21, 10.53, 10.73, 5.11, 6.1, 6.17, 6.26, D10.3.1
**Jaccard:** 0.423 — AI adds ['2.1', '2.14', '2.7', '5.16', '6.16', '6.22', '6.28', 'CN3', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.1.4']; Human adds ['10.11', '10.53', '6.26']

## Proposition 10.92
**Statement:** If an area be contained by a rational straight line and a second apotome, the âsideâ of the area is a first apotome of a medial straight line.

**Step 1.** Let r be the given rational straight line, and write the second apotome as a − b, where a > b. By the definition of an apotome, a and b are rational and commensurable in square only. Since this is a second apotome, b is commensurable in length with r, and a² − b² = c² for a straight line c commensurable in length with a. [10.73; D10.3.2]

**Step 2.** We use the deficient-square division: its commensurable-parts criterion is precisely the square-difference condition just obtained. Apply to a a rectangle equal to b²/4 and deficient by a square. This is possible because b < a. Thus a is divided into positive parts d and e satisfying d + e = a and de = b²/4. The parts are unequal, since equality would imply b = a; label them so that d > e. By the commensurable-parts direction of 10.17, d and e are commensurable in length. Their sum a is therefore commensurable in length with each of them. [6.28; 10.17; 10.15]

**Step 3.** Since d and e are commensurable in length with the rational line a, their squares are commensurable with a², by 10.9 and 10.6. Transitivity and the definition of rational straight lines therefore make d and e rational. Moreover, b is commensurable with r but incommensurable in length with a, so a is incommensurable in length with r. Since d and e are each commensurable with a, each is likewise incommensurable in length with r. Consequently r and each of d and e are rational straight lines commensurable in square only. [10.9; 10.6; 10.12; D10.1.3; 10.13]

**Step 4.** Construct squares with sides x and y equal respectively to the rectangles rd and re, so that x² = rd and y² = re. Because d > e, we have x > y. Each rectangle is contained by rational straight lines commensurable in square only; hence x and y are medial straight lines. [2.14; 10.21]

**Step 5.** Rectangles under the same height are proportional to their bases, so x² : y² = rd : re = d : e. Since d and e are commensurable, x² and y² are commensurable. Thus x and y are commensurable in square. [6.1; 10.11; D10.1.2]

**Step 6.** From x² = rd, y² = re, and de = b²/4, multiplication gives (xy)² = r²b²/4. All the lengths are positive, so xy = r(b/2). Since b and r have a common measure, half that measure measures both b/2 and r. These two lines are therefore commensurable in length and rational, and their rectangle—and hence xy—is rational. [D10.1.1; 10.19]

**Step 7.** If x and y were commensurable in length, their rectangle would be medial, because both lines are medial. But a medial area is irrational, whereas xy has just been shown rational. Thus x and y are incommensurable in length; together with Step 5, this says that they are commensurable in square only. [10.24; 10.21]

**Step 8.** The square-difference identity gives
(x − y)² = x² + y² − 2xy = r(d + e) − rb = r(a − b).
Thus x − y is the side of the given area. It is the remainder after subtracting from the medial line x a medial line y commensurable with it in square only and containing with it a rational rectangle. By 10.74, this remainder is a first apotome of a medial straight line. Therefore the side of an area contained by a rational straight line and a second apotome is a first apotome of a medial straight line. [2.7; 10.74]

**USED:** 10.11, 10.12, 10.13, 10.15, 10.17, 10.19, 10.21, 10.24, 10.6, 10.73, 10.74, 10.9, 2.14, 2.7, 6.1, 6.28, D10.1.1, D10.1.2, D10.1.3, D10.3.2
**Human refs (from References field):** 10.11, 10.13, 10.15, 10.17, 10.19, 10.21, 10.73, 10.74, 5.11, 6.1, 6.17, 6.26, D10.3.2
**Jaccard:** 0.435 — AI adds ['10.12', '10.24', '10.6', '10.9', '2.14', '2.7', '6.28', 'D10.1.1', 'D10.1.2', 'D10.1.3']; Human adds ['5.11', '6.17', '6.26']

## Proposition 10.93
**Statement:** If an area be contained by a rational straight line and a third apotome, the âsideâ of the area is a second apotome of a medial straight line.

**Step 1.** Let r be the given rational straight line, and write the third apotome as b−c, where b>c. Products below denote rectangular areas. By the definition of an apotome, b and c are rational and commensurable in square only. By the definition of a third apotome, neither is commensurable in length with r, and there is a straight line d, commensurable in length with b, such that b²−c²=d². Thus 0<d<b. [10.73, D10.3.3]

**Step 2.** Use this commensurable square-difference to split b directly. Put
u=(b+d)/2, v=(b−d)/2, and w=c/2.
Then u>v>0 and u+v=b. If e measures both b and d, then e/2 measures b, u, and v; hence u and v are commensurable in length with b and with one another. Also w is commensurable in length with c. Applying II.5 to the equal and unequal divisions of b gives
uv+(d/2)²=(b/2)²,
so uv=c²/4=w². [D10.1.1, 2.5]

**Step 3.** Since u and v are commensurable in length with b, their squares are commensurable with b²; similarly, w² is commensurable with c². This follows from the square-number ratios in X.9 and the commensurability criterion X.6. As b and c are rational, transitivity of commensurability shows that u, v, and w are rational. Since b and c are each incommensurable in length with r, so are u, v, and w. Moreover, u and w are incommensurable in length: apply X.13 first to b and u, using the incommensurability of b with c, and then to c and w. [10.9, 10.6, 10.12, D10.1.3, 10.13]

**Step 4.** Construct squares equal to the rectangles ru and rv, and call their sides x and y respectively. This is the direct area-to-side construction of II.14. Thus
x²=ru, y²=rv,
and x>y. Because r and each of u and v are rational and commensurable in square only, x and y are medial straight lines. [2.14, 10.21]

**Step 5.** Rectangles under the same height are as their bases, so
x²:y²=ru:rv=u:v.
Since u and v are commensurable in length, x² and y² are commensurable areas. Thus x and y are commensurable in square. Also, because w²=uv,
u²:w²=u²:uv=u:v=x²:y².
The converse of VI.22, applied to these squares, therefore gives x:y=u:w. Since u and w are incommensurable in length, X.11 shows that x and y are incommensurable in length. Consequently they are commensurable in square only. [6.1, 10.11, 6.22]

**Step 6.** Again using rectangles under the same height,
x²:xy=x:y=u:w=ru:rw=x²:rw.
Areas to which the same area has the same ratio are equal; hence xy=rw. But r and w are rational and commensurable in square only, so rw is a medial area. Thus x and y contain a medial rectangle. [6.1, 5.9, 10.21]

**Step 7.** By addition of rectangles,
x²+y²=r(u+v)=rb,
while 2xy=2rw=rc. Applying II.7 to x=y+(x−y) therefore yields
(x−y)²=x²+y²−2xy=rb−rc=r(b−c).
Thus the positive straight line x−y is the side of the given area. It is obtained by subtracting from the medial straight line x the medial straight line y, which is commensurable with x in square only and contains with x a medial rectangle. By X.75, x−y is a second apotome of a medial straight line. Therefore the side of an area contained by a rational straight line and a third apotome is a second apotome of a medial straight line. [2.1, 2.7, 10.75]

**USED:** 10.11, 10.12, 10.13, 10.21, 10.6, 10.73, 10.75, 10.9, 2.1, 2.14, 2.5, 2.7, 5.9, 6.1, 6.22, D10.1.1, D10.1.3, D10.3.3
**Human refs (from References field):** 10.11, 10.13, 10.15, 10.17, 10.21, 10.75, 5.11, 6.1, 6.17, 6.26, D10.3.3
**Jaccard:** 0.261 — AI adds ['10.12', '10.6', '10.73', '10.9', '2.1', '2.14', '2.5', '2.7', '5.9', '6.22', 'D10.1.1', 'D10.1.3']; Human adds ['10.15', '10.17', '5.11', '6.17', '6.26']

## Proposition 10.94
**Statement:** If an area be contained by a rational straight line and a fourth apotome, the âsideâ of the area is minor.

**Step 1.** Let r be the given rational straight line, and let the fourth apotome be a−b, with a>b. Write products for rectangular areas and squares for square areas. The straight lines a and b are rational and commensurable in square only; moreover, a is commensurable in length with r, and a²−b² is the square on a straight line incommensurable in length with a. [10.73, D10.3.4]

**Step 2.** Bisect b, putting h=b/2; thus h²=b²/4. Apply to a a rectangle equal to h² and deficient by a square. This construction is possible because b<a, so h² is less than the square on half of a. Denote the resulting parts of a by u and v, so that
u+v=a, uv=h².
By 10.18, u and v are incommensurable in length. This is the appropriate division theorem because the definition of a fourth apotome gives precisely its incommensurable-square-difference hypothesis. Label the parts so that u>v. [1.10, 6.1, 6.28, 10.18]

**Step 3.** Construct straight lines x and y whose squares equal the rectangles ru and rv respectively:
x²=ru, y²=rv.
Then x>y. Rectangles of the same height are proportional to their bases, so x²:y²=u:v. Since u and v are incommensurable, their proportional magnitudes x² and y² are also incommensurable. Thus x and y are incommensurable in square. [2.14, 6.1, 10.11, D10.1.2]

**Step 4.** We claim that xy=rh. Indeed, using uv=h² and rectangles of equal height,
x²:y²=u:v=u²:h².
Proportional squares have proportional sides, whence x:y=u:h. Therefore
x²:xy=x:y=u:h=ru:rh=x²:rh.
Magnitudes to which the same magnitude has the same ratio are equal; hence xy=rh. [6.1, 6.22, 5.9]

**Step 5.** The sum of the squares is
x²+y²=ru+rv=r(u+v)=ra.
Since r and a are rational and commensurable in length, ra is rational. Consequently x²+y² is rational. [2.1, 10.19]

**Step 6.** Since h² is one fourth of b² and b is rational, h is rational also: its square is commensurable with the square on b, and hence with the assigned rational square. Thus r and h are commensurable in square. But b is incommensurable in length with a, whereas a is commensurable in length with r; therefore b is incommensurable in length with r. Since h is commensurable in length with b, h too is incommensurable in length with r. The rectangle rh is consequently medial, being contained by rational straight lines commensurable in square only. By Step 4, xy is therefore medial. [6.1, D10.1.3, 10.12, 10.13, 10.21]

**Step 7.** The square on the difference x−y satisfies
(x−y)²=x²+y²−2xy=ra−2rh=r(a−b),
because 2h=b. Hence x−y is the side of the given area contained by r and the fourth apotome a−b. [2.7, 2.1]

**Step 8.** The straight line y is incommensurable in square with the whole x; the sum x²+y² is rational; and the rectangle xy is medial. Therefore, by 10.76, the remainder x−y is minor. Thus the side of an area contained by a rational straight line and a fourth apotome is minor. [10.76]

**USED:** 1.10, 10.11, 10.12, 10.13, 10.18, 10.19, 10.21, 10.73, 10.76, 2.1, 2.14, 2.7, 5.9, 6.1, 6.22, 6.28, D10.1.2, D10.1.3, D10.3.4
**Human refs (from References field):** 10.11, 10.18, 10.19, 10.21, 10.76, 5.11, 6.1, 6.17, 6.26, D10.3.4
**Jaccard:** 0.318 — AI adds ['1.10', '10.12', '10.13', '10.73', '2.1', '2.14', '2.7', '5.9', '6.22', '6.28', 'D10.1.2', 'D10.1.3']; Human adds ['5.11', '6.17', '6.26']

## Proposition 10.95
**Statement:** If an area be contained by a rational straight line and a fifth apotome, the âsideâ of the area is a straight line which produces with a rational area a medial whole.

**Step 1.** Let r be the given rational straight line, and let the fifth apotome be a−b, where a>b. Write uv for the rectangle contained by two straight lines u,v, and u² for the square on u. By the definition of an apotome and the definition of its fifth kind, a and b are rational and commensurable in square only; b is commensurable in length with r; and a²−b² is the square on a straight line incommensurable in length with a. [10.73, D10.3.4, D10.3.5]

**Step 2.** Since b and r are commensurable in length, whereas a and b are incommensurable in length, a and r are incommensurable in length. They are nevertheless commensurable in square, since a is rational relative to the rational straight line r set out. Consequently ra is a medial area. On the other hand, rb is rational, since r and b are rational and commensurable in length. [10.13, D10.1.3, 10.21, 10.19]

**Step 3.** Bisect b, calling its half h. Apply to a a rectangle equal to h² and deficient by a square. This construction is permitted because b<a, so h² is less than the square on half of a. It divides a into positive parts p,q satisfying
p+q=a and pq=h²=b²/4.
Label them so that p>q; equality would imply a=b. We use the converse direction of the incommensurable-excess criterion directly: since a²−b² has a side incommensurable with a, this division makes p and q incommensurable in length. [1.10, 6.28, 10.18]

**Step 4.** Construct squares equal to rp and rq, and let their sides be x and y respectively. Thus x²=rp and y²=rq, with x>y. Rectangles of the same height are proportional to their bases, so
x²:y²=p:q.
Since p and q are incommensurable, x² and y² are incommensurable. Hence x and y are incommensurable in square. [2.14, 6.1, 10.11, D10.1.2]

**Step 5.** Adding the two rectangles gives
x²+y²=rp+rq=r(p+q)=ra.
Thus the sum of the squares on x and y is medial, by Step 2. [2.1]

**Step 6.** We next identify twice their rectangle. By proportionality of rectangles of equal height,
x²:r²=rp:r²=p:r,
and
h²:y²=pq:rq=p:r.
Therefore x²:r²=h²:y². Since these are squares, their sides are proportional: x:r=h:y. The rectangle of the extremes consequently equals that of the means, so xy=rh. Since b consists of two copies of h, it follows that
2xy=2rh=rb,
which is rational by Step 2. [6.1, 6.22, 6.16, 2.1]

**Step 7.** Put z=x−y. The square identity for a line and its two parts gives
z²=x²+y²−2xy=ra−rb=r(a−b).
Thus z is the side of the given area. Moreover, x and y are incommensurable in square, the sum of their squares is medial, and twice their rectangle is rational. Proposition 10.77 therefore says precisely that their difference z is a straight line which produces with a rational area a medial whole. Hence the side of the area contained by r and the fifth apotome a−b has the required character. [2.7, 2.1, 10.77]

**USED:** 1.10, 10.11, 10.13, 10.18, 10.19, 10.21, 10.73, 10.77, 2.1, 2.14, 2.7, 6.1, 6.16, 6.22, 6.28, D10.1.2, D10.1.3, D10.3.4, D10.3.5
**Human refs (from References field):** 10.18, 10.19, 10.21, 10.77, 6.26, D10.3.5
**Jaccard:** 0.250 — AI adds ['1.10', '10.11', '10.13', '10.73', '2.1', '2.14', '2.7', '6.1', '6.16', '6.22', '6.28', 'D10.1.2', 'D10.1.3', 'D10.3.4']; Human adds ['6.26']

## Proposition 10.96
**Statement:** If an area be contained by a rational straight line and a sixth apotome, the âsideâ of the area is a straight line which produces with a medial area a medial whole.

**Step 1.** Let r be the given rational straight line, taken as the rational straight line set out, and write the sixth apotome as a−b, where a>b>0. Here a and b are rational and commensurable in square only; neither is commensurable in length with r; and a²−b² is the square on a straight line incommensurable in length with a. We write xy for the rectangle contained by straight lines x and y. [10.73; D10.3.4; D10.3.5; D10.3.6]

**Step 2.** Put h=b/2. Since h²<(a/2)², apply to a a rectangle equal to h² and deficient by a square. This divides a into positive segments x and y satisfying x+y=a and xy=h². By the incommensurable alternative of X.18, x and y are incommensurable in length. Label them so that x>y. This deficient-square construction is the direct route because X.18 matches exactly the excess-square condition defining the sixth apotome. [6.28; 10.18]

**Step 3.** Construct straight lines u and v whose squares equal rx and ry respectively. Thus u>v. Rectangles of equal height are proportional to their bases, so u²:v²=x:y. Since x and y are incommensurable, their corresponding squares u² and v² are incommensurable; consequently u and v are incommensurable in square. Also, by distributing the rectangle over the division x+y=a,

u²+v²=rx+ry=ra.

[2.14; 6.1; 10.11; D10.1.2; 2.1]

**Step 4.** We next show that 2uv=rb. Since h²=xy, the equal-height rectangle relation gives

x²:h²=x²:xy=x:y=u²:v².

Proportional squares have proportional sides, so u:v=x:h. Moreover, u²=rx gives r:u=u:x. Combining these last two proportions ex aequali gives r:v=u:h, and therefore rh=uv. Since b=2h, it follows that rb=2uv. [6.1; 6.22; 6.17; 5.22; 6.16; 2.1]

**Step 5.** Each of a and b is rational but incommensurable in length with r, and hence each is commensurable with r in square only. Therefore ra and rb are medial areas. Furthermore, ra:rb=a:b; since a and b are incommensurable in length, ra and rb are incommensurable areas. By Steps 3 and 4, the sum u²+v² and twice the rectangle uv are thus medial and incommensurable with one another. [D10.1.3; 10.21; 6.1; 10.11]

**Step 6.** Subtract v from u. The square on the remainder satisfies

(u−v)²=u²+v²−2uv=ra−rb=r(a−b).

Thus u−v is the side of the given area contained by the rational straight line r and the sixth apotome a−b. [2.7; 2.1]

**Step 7.** The lines u and v are incommensurable in square, their squares together form a medial area, and twice their rectangle is a medial area incommensurable with that sum. Consequently, by X.78, their difference u−v is a straight line which produces with a medial area a medial whole. Since this difference is the side of the given area, the proposition is proved. [10.78]

**USED:** 10.11, 10.18, 10.21, 10.73, 10.78, 2.1, 2.14, 2.7, 5.22, 6.1, 6.16, 6.17, 6.22, 6.28, D10.1.2, D10.1.3, D10.3.4, D10.3.5, D10.3.6
**Human refs (from References field):** 10.11, 10.18, 10.21, 10.78, 6.1, 6.26, D10.3.6
**Jaccard:** 0.300 — AI adds ['10.73', '2.1', '2.14', '2.7', '5.22', '6.16', '6.17', '6.22', '6.28', 'D10.1.2', 'D10.1.3', 'D10.3.4', 'D10.3.5']; Human adds ['6.26']

## Proposition 10.97
**Statement:** The square on an apotome applied to a rational straight line produces as breadth a first apotome.

**Step 1.** Let x be the given apotome and r the given rational straight line. Write x=a−b, where a>b and a,b are rational straight lines commensurable in square only, as in the definition of an apotome. Products below denote rectangular areas, and squares denote square areas. [10.73]

**Step 2.** Apply the areas a², b², and ab to r, obtaining breadths u,v,w respectively, so that
ru=a², rv=b², rw=ab.
These applications can be made by applying the constituent triangles successively. Put p=u+v; then rp=a²+b². The areas a² and b² are rational, and their sum is rational: their commensurability with the rational square, together with the sum property of commensurable magnitudes, establishes this. Therefore u,v,p are rational and commensurable in length with r. In particular, u and v are commensurable in length. [1.44, 2.1, D10.1.3, D10.1.4, 10.12, 10.15, 10.20]

**Step 3.** Since a and b are rational and commensurable in square only, ab is the square on a medial straight line. Its application to r therefore gives w rational but incommensurable in length with r. Put q=2w. The square q² equals 4w², so q is rational. Also q is incommensurable in length with r: if a length measured q and r, half that length would measure w and r, which is impossible. Since p is commensurable in length with r, p and q are incommensurable in length. Their squares, however, are commensurable, since both are commensurable with the rational square. Thus p and q are rational straight lines commensurable in square only. [10.21, 10.22, 2.4, D10.1.1, D10.1.2, D10.1.3, D10.1.4, 10.12, 10.13]

**Step 4.** Applying the square identity to a=b+x gives
a²+b²=2ab+x².
Consequently rp=rq+x², and hence p>q and
r(p−q)=x².
Thus the breadth produced by applying the square on x to r is p−q. By Step 3, this difference is an apotome, with whole p and annex q. [2.7, 2.1, 10.73]

**Step 5.** Rectangles under the same height are proportional to their bases. Therefore
u:w=ru:rw=a²:ab=a:b,
and
w:v=rw:rv=ab:b²=a:b.
Hence u:w=w:v, and the rectangle uv equals w². Since q=2w, it follows that uv is one fourth of q². [6.1, 6.17, 2.4]

**Step 6.** As p=u+v, the rectangle uv is an area applied to p deficient by the square on v: indeed, pv=uv+v². Its division of p is into the commensurable parts u and v established in Step 2. We use the commensurable-division criterion here because the applications of the component squares have already supplied exactly its required division. Since p>q and uv is one fourth of q², that criterion gives
p²=q²+d²
for a straight line d commensurable in length with p. [2.1, 10.17]

**Step 7.** The breadth p−q is an apotome; its whole p is commensurable in length with the rational straight line r; and the square on its whole exceeds the square on its annex by the square on a straight line commensurable in length with the whole. These are precisely the defining conditions of a first apotome. Therefore the square on an apotome, applied to a rational straight line, produces as breadth a first apotome. [D10.3.1]

**USED:** 1.44, 10.12, 10.13, 10.15, 10.17, 10.20, 10.21, 10.22, 10.73, 2.1, 2.4, 2.7, 6.1, 6.17, D10.1.1, D10.1.2, D10.1.3, D10.1.4, D10.3.1
**Human refs (from References field):** 10.11, 10.17, 10.20, 10.22, 10.73, 2.7, 6.1, 6.17, D10.3.1
**Jaccard:** 0.400 — AI adds ['1.44', '10.12', '10.13', '10.15', '10.21', '2.1', '2.4', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.1.4']; Human adds ['10.11']

## Proposition 10.98
**Statement:** The square on a first apotome of a medial straight line applied to a rational straight line produces as breadth a second apotome.

**Step 1.** Let a be the given first apotome of a medial straight line, and let r be the rational straight line to which its square is to be applied. By the defining description, write a = u − v, where u > v are medial straight lines commensurable in square only, and the rectangle uv is rational. We proceed directly from these defining areas. [10.74]

**Step 2.** Apply the squares on u and v, and the rectangle uv, to r, obtaining breadths p, q, and t respectively. Thus rp = u², rq = v², and rt = uv. Since u is medial, p is rational and incommensurable in length with r. Since uv is rational, t is rational and commensurable in length with r. [10.22, 10.20]

**Step 3.** Rectangles of the same height are proportional to their bases, so p:q = u²:v². Therefore p and q are commensurable in length. Put P = p + q and B = 2t. Then P is commensurable in length with p, and B with t. Commensurable lengths have commensurable squares: their squares have a square-number ratio, hence a number ratio. Consequently, because p and t are rational, P and B are rational also. Moreover, B is commensurable in length with r. [6.1, 10.11, 10.15, 10.9, 10.6, 10.12, D10.1.3]

**Step 4.** By the identity for the square on a remainder,

rP = u² + v² = 2uv + (u − v)² = rB + a².

Thus P > B, and r(P − B) = a². Hence P − B is precisely the breadth produced by applying the square on a to r. [2.7]

**Step 5.** Since P is commensurable in length with p, whereas p is incommensurable in length with r, P is incommensurable in length with r. Since B is commensurable in length with r, P and B are incommensurable in length. But both are rational, so their squares are commensurable. Therefore P − B is an apotome, with whole P and annex B. [10.13, D10.1.3, 10.12, 10.73]

**Step 6.** Again by ratios of rectangles of equal height,

p:t = u:v = t:q.

Hence pq = t² = B²/4. The rectangle pq is an application to P = p + q deficient by the square on q, and it divides P into the commensurable parts p and q. We therefore use the commensurable-division criterion, which applies directly to this construction: the square on P exceeds the square on B by the square on a straight line commensurable in length with P. [6.1, 6.17, 10.17]

**Step 7.** The apotome P − B has its annex B commensurable in length with the rational straight line r, and the square on its whole P exceeds the square on its annex by the square on a straight line commensurable with P. It is therefore a second apotome. Since r(P − B) = a², the square on a first apotome of a medial straight line, applied to a rational straight line, produces as breadth a second apotome. [D10.3.2]

**USED:** 10.11, 10.12, 10.13, 10.15, 10.17, 10.20, 10.22, 10.6, 10.73, 10.74, 10.9, 2.7, 6.1, 6.17, D10.1.3, D10.3.2
**Human refs (from References field):** 10.11, 10.15, 10.17, 10.20, 10.22, 10.23, 10.73, 10.74, 2.7, 5.11, 6.1, 6.17, D10.3.2
**Jaccard:** 0.611 — AI adds ['10.12', '10.13', '10.6', '10.9', 'D10.1.3']; Human adds ['10.23', '5.11']

## Proposition 10.99
**Statement:** The square on a second apotome of a medial straight line applied to a rational straight line produces as breadth a third apotome.

**Step 1.** Let x be the given second apotome of a medial straight line, and let r be the rational straight line to which its square is applied. By the defining property, write x = a − b, where a > b are medial straight lines commensurable in square only, and the rectangle ab is medial. Products below denote rectangular areas. [10.75]

**Step 2.** Apply the areas a², b², and ab to r, obtaining breadths u, v, and w respectively, so that
ru = a², rv = b², rw = ab.
These applications can be constructed by applying the triangular halves of the respective areas and adjoining the resulting rectangles. Since each area is the square on a medial straight line, each of u, v, and w is rational and incommensurable in length with r. [1.44, 10.22]

**Step 3.** Ratios of rectangles under the same height give
u : v = a² : b²,
and
u : w = a : b = w : v.
Since a² and b² are commensurable, u and v are commensurable in length. Since a and b are incommensurable in length, u and w are incommensurable in length. [6.1, 10.11]

**Step 4.** Put c = u + v and d = 2w. Since u and v are commensurable, c is commensurable in length with u; also d is commensurable in length with w. Consequently c and d are each incommensurable in length with r. Moreover, u and w being incommensurable, replacing u by the commensurable line c and then w by the commensurable line d shows that c and d are incommensurable in length with one another. [10.15, 10.13]

**Step 5.** Commensurability in length gives commensurability in square: the corresponding squares have the ratio of square numbers and hence are commensurable. Thus c² is commensurable with u², and d² with w². Since u and w are rational, transitivity of commensurability shows that c and d are rational and commensurable in square with one another. Together with Step 4, they are therefore commensurable in square only. [10.9, 10.6, 10.12, D10.1.3]

**Step 6.** The square identity for a line cut into the segments a − b and b gives
a² + b² = 2ab + (a − b)².
But rc = a² + b² and rd = 2ab. Hence c > d and
r(c − d) = (a − b)² = x².
Thus the breadth produced by applying x² to r is c − d. Since c and d are rational and commensurable in square only, this breadth is an apotome, with whole c and annex d. [2.7, 6.1, 10.73]

**Step 7.** From u : w = w : v, the rectangle uv equals w², which is one fourth of d². The division c = u + v therefore exhibits a rectangle uv applied to c and deficient by the square on v; its two parts u and v are commensurable in length. We use the commensurable-division criterion directly, since precisely its required division is already available. It follows that c² exceeds d² by the square on a straight line commensurable in length with c. [6.17, 10.17]

**Step 8.** The breadth c − d is an apotome; neither its whole c nor its annex d is commensurable in length with the rational straight line r; and the square on its whole exceeds the square on its annex by the square on a straight line commensurable with the whole. It is therefore a third apotome. Hence the square on a second apotome of a medial straight line, applied to a rational straight line, produces as breadth a third apotome. [D10.3.3]

**USED:** 1.44, 10.11, 10.12, 10.13, 10.15, 10.17, 10.22, 10.6, 10.73, 10.75, 10.9, 2.7, 6.1, 6.17, D10.1.3, D10.3.3
**Human refs (from References field):** 10.11, 10.13, 10.15, 10.17, 10.22, 10.23, 10.73, 10.75, 2.7, 5.11, 6.1, D10.3.3
**Jaccard:** 0.556 — AI adds ['1.44', '10.12', '10.6', '10.9', '6.17', 'D10.1.3']; Human adds ['10.23', '5.11']

## Proposition 10.100
**Statement:** The square on a minor straight line applied to a rational straight line produces as breadth a fourth apotome.

**Step 1.** Let x be a minor straight line and r the rational straight line to which its square is to be applied. We use the defining decomposition of the minor and classify the resulting breadth directly. By 10.76, write x = a − b, where a > b, the squares a² and b² are incommensurable, their sum is rational, and the rectangle ab is medial. Here products denote rectangular areas. [10.76; D10.1.2]

**Step 2.** Apply a², b², and ab to r, obtaining breadths p, q, and t respectively, so that rp = a², rq = b², and rt = ab. These applications can be made by applying the triangular halves of the respective areas successively. Put u = p + q and v = 2t. By addition of rectangles and the square identity for a = b + x,
ru = a² + b² = 2ab + x² = rv + x².
Consequently u > v and r(u − v) = x²: the required breadth is u − v. [1.44; 2.1; 2.7]

**Step 3.** Since ru = a² + b² is rational, u is rational and commensurable in length with r. Since rt = ab is medial, t is rational but incommensurable in length with r. Moreover, v = 2t is rational: its square is four times t², so any area measuring both t² and the assigned rational square also measures v². Since v is commensurable in length with t, it remains incommensurable in length with r. [10.20; 10.22; 2.1; D10.1.2; D10.1.3; 10.13]

**Step 4.** The rational straight lines u and v are commensurable in square, because their squares are commensurable with the same assigned rational square. They are incommensurable in length: u is commensurable with r, whereas v is incommensurable with r. Thus u − v is an apotome, with whole u and annex v. [D10.1.3; 10.12; 10.13; 10.73]

**Step 5.** Rectangles of the same height are proportional to their bases. Hence
p : q = rp : rq = a² : b².
Since a² and b² are incommensurable, p and q are incommensurable in length. Similarly,
p : t = a² : ab = a : b,
and
t : q = ab : b² = a : b.
Therefore p : t = t : q, and the rectangle pq equals t², which is one quarter of v². [6.1; 10.11; 6.17]

**Step 6.** The rectangle pq is applied to u = p + q deficient by the square q²: the full rectangle of base u and height q consists of pq together with q². It therefore gives an application to u equal to one quarter of v², deficient by a square, and dividing u into the incommensurable parts p and q. We use the forward direction of 10.18, since this incommensurable division is already established. It follows that u² exceeds v² by the square on a straight line incommensurable in length with u. [2.1; 10.18]

**Step 7.** The apotome u − v has its whole u commensurable in length with the rational straight line r, while u² exceeds the square on its annex v by the square on a straight line incommensurable with u. It is therefore a fourth apotome. Since r(u − v) = x², the square on the minor straight line, applied to the rational straight line, produces as breadth a fourth apotome. [D10.3.4]

**USED:** 1.44, 10.11, 10.12, 10.13, 10.18, 10.20, 10.22, 10.73, 10.76, 2.1, 2.7, 6.1, 6.17, D10.1.2, D10.1.3, D10.3.4
**Human refs (from References field):** 10.11, 10.18, 10.20, 10.22, 10.73, 10.76, 2.7, 5.11, 6.1, 6.17, D10.3.4
**Jaccard:** 0.588 — AI adds ['1.44', '10.12', '10.13', '2.1', 'D10.1.2', 'D10.1.3']; Human adds ['5.11']

## Proposition 10.101
**Statement:** The square on the straight line which produces with a rational area a medial whole, if applied to a rational straight line, produces as breadth a fifth apotome.

**Step 1.** Let x be the given straight line, and let r be the rational straight line to which its square is applied. By the characterization in 10.77, write x = a − b, where a > b, the squares a² and b² are incommensurable, their sum a² + b² is medial, and twice the rectangle ab is rational. Products below denote rectangular areas. [10.77]

**Step 2.** Apply the areas a², b², and ab to r, obtaining respective breadths u, v, and w, so that ru = a², rv = b², and rw = ab. These applications can be made by applying the constituent triangles of each area and adjoining the resulting rectangles. Put U = u + v and V = 2w. Thus rU = a² + b² and rV = 2ab. By 2.7,

rU = rV + x².

Consequently U > V, and the rectangle r(U − V) equals x². Hence the breadth in question is U − V. [1.44, 2.1, 2.7, 6.1]

**Step 3.** Since rU is medial and r is rational, U is rational and incommensurable in length with r. Since rV is rational, V is rational and commensurable in length with r. [10.22, 10.20]

**Step 4.** The rational straight lines U and V have squares commensurable with the square on the assigned rational straight line, and therefore their squares are commensurable with one another. But U and V are incommensurable in length: V is commensurable with r, whereas U is incommensurable with r. Thus U and V are rational straight lines commensurable in square only, so U − V is an apotome, with whole U and annex V. [D10.1.3, 10.12, 10.13, 10.73]

**Step 5.** The rectangles ru and rv have the same height, so

u : v = a² : b².

Since a² and b² are incommensurable, u and v are incommensurable in length. Thus the division U = u + v is into incommensurable parts. [6.1, 10.11]

**Step 6.** Again, by comparing rectangles of equal height,

u : w = a² : ab = a : b,

w : v = ab : b² = a : b.

Therefore u : w = w : v, and the rectangle uv equals w². Since V = 2w, the square w² is the fourth part of V². Consequently uv = V²/4. [6.1, 5.11, 6.17, 2.4]

**Step 7.** The rectangle uv, placed along the part u of U with height v, is an application to U deficient by the square on v: indeed, Uv = uv + v². It equals the fourth part of the square on V and divides U into the incommensurable parts u and v. We therefore use the deficient-square criterion of 10.18 directly, since this division supplies precisely its hypotheses. As U > V, the square on U exceeds the square on V by the square on a straight line incommensurable in length with U. [2.1, 10.18]

**Step 8.** The apotome U − V thus has its whole-square exceeding its annex-square by the square on a straight line incommensurable with the whole, while its annex V is commensurable in length with the rational straight line r. By the definition, it is a fifth apotome. Since U − V is the breadth obtained by applying x² to r, the required conclusion follows. [D10.3.4, D10.3.5]

**USED:** 1.44, 10.11, 10.12, 10.13, 10.18, 10.20, 10.22, 10.73, 10.77, 2.1, 2.4, 2.7, 5.11, 6.1, 6.17, D10.1.3, D10.3.4, D10.3.5
**Human refs (from References field):** 10.11, 10.18, 10.20, 10.22, 10.73, 10.77, 2.7, 6.1, D10.3.5
**Jaccard:** 0.500 — AI adds ['1.44', '10.12', '10.13', '2.1', '2.4', '5.11', '6.17', 'D10.1.3', 'D10.3.4']

## Proposition 10.102
**Statement:** The square on the straight line which produces with a medial area a medial whole, if applied to a rational straight line, produces as breadth a sixth apotome.

**Step 1.** Let x be the given straight line. By the defining description in 10.78, write x = a − b, where a > b, the squares a² and b² are incommensurable, and the areas
S = a² + b²,   T = 2ab
are medial and incommensurable with one another. Here and below, products denote rectangles and squares denote square areas. [10.78, D10.1.2]

**Step 2.** Let r be the rational straight line to which x² is to be applied, and take r as the rational straight line set out. Apply S and T to r, obtaining rectangular breadths h and k, so that
rh = S,   rk = T.
These applications can be made by applying triangular pieces and adjoining the resulting rectangles. By 2.7,
S − T = (a − b)² = x² > 0.
Thus h > k, and, by addition and subtraction of rectangles on the same base,
r(h − k) = x².
Consequently the breadth whose kind must be determined is h − k. [1.44, 2.1, 2.7, 6.1]

**Step 3.** Since S and T are medial areas, 10.22 shows that h and k are rational straight lines, each incommensurable in length with r. Moreover, rectangles under the same height are proportional to their bases, so
h : k = S : T.
Therefore h and k are incommensurable in length, by 10.11. Their squares, however, are commensurable: both lines are rational, so their squares are commensurable with the square on the assigned rational line, and hence with one another. Thus h and k are commensurable in square only, and h − k is an apotome, with whole h and annex k. [10.22, 6.1, 10.11, D10.1.3, 10.12, 10.73]

**Step 4.** Apply a², b², and ab separately to the same line r, obtaining breadths p, q, and m:
rp = a²,   rq = b²,   rm = ab.
By addition of rectangles on r,
p + q = h,   2m = k.
Also, by 6.1,
p : q = a² : b².
Since a² and b² are incommensurable, p and q are incommensurable in length. [1.44, 2.1, 6.1, 10.11]

**Step 5.** Again using rectangles under the same height gives
p : m = a² : ab = a : b,
and
m : q = ab : b² = a : b.
Hence p, m, q are proportional. By 6.17,
pq = m² = ¼k².
Thus the rectangle contained by p and q equals the fourth part of the square on k. [6.1, 6.17]

**Step 6.** Divide h into its parts p and q. The rectangle of base p and height q, applied to h = p + q, is deficient by the square of side q. By Step 5 its area is ¼k², and by Step 4 the division is into incommensurable parts. We therefore use the forward direction of 10.18: it applies directly to this deficient-square rectangle and gives precisely the excess-square condition needed here. It follows that h² exceeds k² by the square on a straight line incommensurable in length with h. [2.1, 10.18]

**Step 7.** The breadth h − k is an apotome; its whole h and annex k are both incommensurable in length with the rational straight line r set out; and h² exceeds k² by the square on a straight line incommensurable with h. These are exactly the conditions for a sixth apotome. Therefore the square on the straight line which produces with a medial area a medial whole, when applied to a rational straight line, produces as breadth a sixth apotome. [D10.3.4, D10.3.6]

**USED:** 1.44, 10.11, 10.12, 10.18, 10.22, 10.73, 10.78, 2.1, 2.7, 6.1, 6.17, D10.1.2, D10.1.3, D10.3.4, D10.3.6
**Human refs (from References field):** 10.11, 10.18, 10.22, 10.73, 10.78, 2.7, 6.1, D10.3.6
**Jaccard:** 0.533 — AI adds ['1.44', '10.12', '2.1', '6.17', 'D10.1.2', 'D10.1.3', 'D10.3.4']

## Proposition 10.103
**Statement:** A straight line commensurable in length with an apotome is an apotome and the same in order.

**Step 1.** Let a be an apotome, and let b be commensurable in length with a. Write a = u − v, where u > v and u, v are rational straight lines commensurable in square only. We take the direct route of transferring this defining whole and annex proportionally. [10.73]

**Step 2.** Construct a fourth proportional v′ such that a : b = v : v′, and put u′ = b + v′. Since u = a + v, taking the sums of the antecedents and consequents gives
u : u′ = a : b = v : v′.
Alternately, u : v = u′ : v′. Also b = u′ − v′. [6.12, 5.12, 5.16]

**Step 3.** Since a and b are commensurable in length, the equal ratios show that u and u′ are commensurable in length, as are v and v′. Consequently u² and u′² are commensurable, and v² and v′² are commensurable: their ratios are ratios of square numbers, and hence ratios of numbers. [10.11, 10.9, 10.6]

**Step 4.** Fix the rational straight line r relative to which the orders are designated. Since u and v are rational, their squares are commensurable with r². Step 3 and transitivity of commensurability therefore show that u′² and v′² are also commensurable with r². Thus u′ and v′ are rational and commensurable in square. But u and v are incommensurable in length, so u : v = u′ : v′ implies that u′ and v′ are likewise incommensurable in length. Hence b = u′ − v′ is an apotome. [D10.1.2, D10.1.3, 10.12, 10.11, 10.73]

**Step 5.** Because u and u′ are commensurable in length, they have the same commensurability status in length with r: if u is commensurable with r, so is u′; if u is incommensurable with r, so is u′. The same reasoning applies to v and v′. Thus the whole is commensurable with r in one decomposition exactly when it is in the other, and likewise for the annex. [10.12, 10.13]

**Step 6.** Apply 10.14 to u : v = u′ : v′. If u² exceeds v² by the square on a straight line commensurable in length with u, then u′² exceeds v′² by the square on a straight line commensurable in length with u′. If the former excess-side is incommensurable with u, the latter is incommensurable with u′. Thus the other distinction determining the order is also preserved. [10.14]

**Step 7.** When the excess-side is commensurable with the whole, the first, second, and third orders are distinguished according as the whole, the annex, or neither is commensurable in length with r. When the excess-side is incommensurable with the whole, the same three alternatives distinguish the fourth, fifth, and sixth orders. Steps 5 and 6 preserve every one of these defining conditions. Therefore b is an apotome of the same order as a. [D10.3.1, D10.3.2, D10.3.3, D10.3.4, D10.3.5, D10.3.6]

**USED:** 10.11, 10.12, 10.13, 10.14, 10.6, 10.73, 10.9, 5.12, 5.16, 6.12, D10.1.2, D10.1.3, D10.3.1, D10.3.2, D10.3.3, D10.3.4, D10.3.5, D10.3.6
**Human refs (from References field):** 10.11, 10.12, 10.13, 10.14, 10.73, 5.12, 5.16, 6.12
**Jaccard:** 0.444 — AI adds ['10.6', '10.9', 'D10.1.2', 'D10.1.3', 'D10.3.1', 'D10.3.2', 'D10.3.3', 'D10.3.4', 'D10.3.5', 'D10.3.6']

## Proposition 10.104
**Statement:** A straight line commensurable with an apotome of a medial straight line is an apotome of a medial straight line and the same in order.

**Step 1.** Let s be an apotome of a medial straight line, and let t be commensurable in length with s. Write s = a − b, where a and b are medial straight lines, a > b, and a and b are commensurable in square only. The rectangle ab is rational if s is a first apotome of a medial straight line, and medial if s is a second. We transport this defining subtraction directly, since the character of its rectangle distinguishes the two orders. Here u² denotes the square on u, and uv the rectangle contained by u and v. [10.74, 10.75]

**Step 2.** Construct a fourth proportional d such that s:b = t:d, and put c = t + d. By componendo, a:b = c:d. Taking these proportions alternately gives

a:c = b:d = s:t.

Moreover, t = c − d. [6.12, 5.18, 5.16]

**Step 3.** Since s and t are commensurable in length, the proportions in Step 2 imply that a and c, and likewise b and d, are commensurable in length. Since a and b are medial, c and d are also medial. [10.11, 10.23]

**Step 4.** Since a:b = c:d and a and b are incommensurable in length, c and d are incommensurable in length. The similar-polygon theorem, applied directly to squares, also gives a²:b² = c²:d². Since a² and b² are commensurable, c² and d² are commensurable. Thus c and d are commensurable in square only. [10.11, 6.20, D10.1.2]

**Step 5.** Consider the intermediate rectangle ad. Rectangles under the same height are as their bases, so

ab:ad = b:d, and ad:cd = a:c.

The pairs b,d and a,c are commensurable in length. Hence ab and ad are commensurable areas, as are ad and cd. Therefore ab and cd are commensurable with one another. [6.1, 10.11, 10.12]

**Step 6.** Because c and d are medial and commensurable in square only, cd is either rational or medial. If ab is rational, its commensurability with cd makes cd rational: both are commensurable with the square on the assigned rational straight line. If ab is medial, it is irrational; cd cannot then be rational, since their commensurability would make ab rational as well. Consequently, in this case cd is medial. Thus cd has the same character—rational or medial—as ab. [10.25, D10.1.4, 10.12, 10.21]

**Step 7.** We have expressed t = c − d as the difference of medial straight lines commensurable in square only. When s is a first apotome of a medial straight line, cd is rational, so t is also a first apotome of a medial straight line. When s is a second, cd is medial, so t is also a second. Therefore a straight line commensurable with an apotome of a medial straight line is an apotome of a medial straight line and the same in order. [10.74, 10.75]

**USED:** 10.11, 10.12, 10.21, 10.23, 10.25, 10.74, 10.75, 5.16, 5.18, 6.1, 6.12, 6.20, D10.1.2, D10.1.4
**Human refs (from References field):** 10.11, 10.13, 10.23, 10.74, 10.75, 5.12, 5.16, 6.12, D10.1.4
**Jaccard:** 0.438 — AI adds ['10.12', '10.21', '10.25', '5.18', '6.1', '6.20', 'D10.1.2']; Human adds ['10.13', '5.12']

## Proposition 10.105
**Statement:** A straight line commensurable with a minor straight line is minor.

**Step 1.** Let a be a minor straight line, and let b be commensurable in length with a. Choose a rational straight line r. By VI.12 construct straight lines u and v such that r:a = a:u and r:b = b:v. Then, by VI.17, the rectangles contained by r,u and r,v equal the squares on a and b respectively. Thus both squares have been applied to the same rational straight line r. [6.12, 6.17]

**Step 2.** We use square application because it takes the given minor directly to an apotome of specified order. Since a is minor, the breadth u obtained by applying its square to the rational straight line r is a fourth apotome. [10.100]

**Step 3.** Since a and b are commensurable in length, their squares have the ratio of a square number to a square number. Consequently, the squares on a and b are commensurable as areas. [10.9, 10.6]

**Step 4.** The two rectangles have the same height r, so they are to one another as their bases u and v. Hence
(square on a):(square on b) = u:v.
Since the first two magnitudes are commensurable, u and v are commensurable in length. [6.1, 10.11]

**Step 5.** A straight line commensurable in length with an apotome is an apotome of the same order. Therefore, since u is a fourth apotome, v is also a fourth apotome. [10.103]

**Step 6.** The square on b equals the rectangle contained by the rational straight line r and the fourth apotome v. The side of such an area is minor; therefore b is minor. Thus a straight line commensurable with a minor straight line is minor. [10.94]

**USED:** 10.100, 10.103, 10.11, 10.6, 10.9, 10.94, 6.1, 6.12, 6.17
**Human refs (from References field):** 10.11, 10.13, 10.23, 10.76, 5.12, 5.16, 5.18, 6.22, D10.1.4
**Jaccard:** 0.059 — AI adds ['10.100', '10.103', '10.6', '10.9', '10.94', '6.1', '6.12', '6.17']; Human adds ['10.13', '10.23', '10.76', '5.12', '5.16', '5.18', '6.22', 'D10.1.4']

## Proposition 10.106
**Statement:** A straight line commensurable with that which produces with a rational area a medial whole is a straight line which produces with a rational area a medial whole.

**Step 1.** Let A be a straight line which produces with a rational area a medial whole, and let B be commensurable in length with A. Choose a rational straight line R. Construct C and D so that R:A = A:C and R:B = B:D, respectively (6.11). Then the rectangles contained by R,C and by R,D equal the squares on A and B, respectively (6.17). Thus these rectangles are applications of the two squares to the same rational straight line.

**Step 2.** Since the square on A has been applied to the rational straight line R, its breadth C is a fifth apotome (10.101). We use this fifth-apotome route because it is supplied directly by the hypothesis through application of the square.

**Step 3.** Because A and B are commensurable in length, their squares have the ratio of a square number to a square number (10.9). The rectangles contained by R,C and R,D have the same height R; hence their ratio is C:D (6.1). By their equalities with the respective squares from Step 1, C:D is therefore the ratio of a square number to a square number. Consequently C and D are commensurable in length (10.6).

**Step 4.** A straight line commensurable in length with an apotome is an apotome of the same order (10.103). Since C is a fifth apotome, D is therefore also a fifth apotome.

**Step 5.** The rectangle contained by the rational straight line R and the fifth apotome D has, by 10.95, a side which produces with a rational area a medial whole. That rectangle equals the square on B by Step 1, so its side is B. Therefore B is a straight line which produces with a rational area a medial whole, as required.

**USED:** 10.101, 10.103, 10.6, 10.9, 10.95, 6.1, 6.11, 6.17
**Human refs (from References field):** 10.77
**Jaccard:** 0.000 — AI adds ['10.101', '10.103', '10.6', '10.9', '10.95', '6.1', '6.11', '6.17']; Human adds ['10.77']

## Proposition 10.107
**Statement:** A straight line commensurable with that which produces with a medial area a medial whole is itself also a straight line which produces with a medial area a medial whole.

**Step 1.** Let a be a straight line which produces with a medial area a medial whole, and let b be commensurable in length with a. Choose a rational straight line r. Apply the squares on a and b to r as rectangles, and denote their respective breadths by x and y. Thus rect(r,x) = square(a) and rect(r,y) = square(b). These applications are obtained by applying the two triangular halves of each square and adjoining the resulting rectangles. [1.44]

**Step 2.** By 10.102, x is a sixth apotome. We choose the sixth-apotome route because this proposition applies directly to the given kind of line a. [10.102]

**Step 3.** Since a and b are commensurable in length, their squares have to one another the ratio of a square number to a square number. The applied rectangles have the same height r, so their ratio is the ratio of their breadths. Consequently,

x : y = rect(r,x) : rect(r,y) = square(a) : square(b).

Thus x and y have the ratio of a number to a number and are therefore commensurable in length. [10.9, 6.1, 10.6]

**Step 4.** A straight line commensurable in length with an apotome is an apotome of the same order. Since x is a sixth apotome, y is also a sixth apotome. [10.103]

**Step 5.** The rectangle contained by the rational straight line r and the sixth apotome y has, by 10.96, a side which produces with a medial area a medial whole. But this rectangle equals the square on b, so b is its side. Therefore b is itself a straight line which produces with a medial area a medial whole, as required. [10.96]

**USED:** 1.44, 10.102, 10.103, 10.6, 10.9, 10.96, 6.1
**Human refs (from References field):** 10.78
**Jaccard:** 0.000 — AI adds ['1.44', '10.102', '10.103', '10.6', '10.9', '10.96', '6.1']; Human adds ['10.78']

## Proposition 10.108
**Statement:** If from a rational area a medial area be subtracted, the âsideâ of the remaining area becomes one of two irrational straight lines, either an apotome or a minor straight line.

**Step 1.** Let R be the given rational area and M the medial area subtracted from it, with R > M. Set out the assigned rational straight line r, and apply the two areas to r as rectangles, with respective breadths a and b. Such applications can be made by applying triangular pieces using 1.44. Thus R = ra and M = rb. By 10.20, a is rational and commensurable in length with r; by 10.22, b is rational and incommensurable in length with r. [1.44, 10.20, 10.22]

**Step 2.** Since the rectangles have the same height r and R > M, we have a > b. Both a and b are rational, so their squares are commensurable with the square on the assigned rational line and therefore with one another. But a and b are incommensurable in length: a is commensurable with r, whereas b is not. Consequently a and b are commensurable in square only, and c = a − b is an apotome, with whole a and annex b. [6.1, D10.1.3, D10.1.2, 10.12, 10.13, 10.73]

**Step 3.** By the division of a rectangle, the remaining area is R − M = r(a − b) = rc. Construct a straight line d whose square equals the excess of the square on a over the square on b. We classify c directly according as d is commensurable or incommensurable in length with a; this reaches the applicable area-to-side propositions directly. [2.1, 2.14]

**Step 4.** If d is commensurable in length with a, then c is a first apotome: its whole a is commensurable in length with the rational straight line r, and a² − b² = d². Since the remaining area is contained by r and this first apotome, its side is an apotome. [D10.3.1, 10.91]

**Step 5.** If d is incommensurable in length with a, then c is a fourth apotome, because its whole a is still commensurable in length with r. Since the remaining area is contained by r and this fourth apotome, its side is a minor straight line. [D10.3.4, 10.94]

**Step 6.** These two cases exhaust the possibilities. An apotome and a minor straight line are both irrational. Therefore, if a medial area is subtracted from a rational area, the side of the remaining area is one of the two stated irrational straight lines: either an apotome or a minor straight line. [10.73, 10.76]

**USED:** 1.44, 10.12, 10.13, 10.20, 10.22, 10.73, 10.76, 10.91, 10.94, 2.1, 2.14, 6.1, D10.1.2, D10.1.3, D10.3.1, D10.3.4
**Human refs (from References field):** 10.13, 10.20, 10.22, 10.73, 10.91, 10.94, D10.3.1, D10.3.4
**Jaccard:** 0.500 — AI adds ['1.44', '10.12', '10.76', '2.1', '2.14', '6.1', 'D10.1.2', 'D10.1.3']

## Proposition 10.109
**Statement:** If from a medial area a rational area be subtracted, there arise two other irrational straight lines, either a first apotome of a medial straight line or a straight line which produces with a rational area a medial whole.

**Step 1.** Let M be the medial area and R the rational area subtracted from it, with M > R. Set out the assigned rational straight line r. Apply both areas to r as rectangles, obtaining breadths a and b respectively, so that M = ra and R = rb. Such applications can be made by applying the triangles composing each area successively to the same base [1.44]. By 10.22, a is rational but incommensurable in length with r; by 10.20, b is rational and commensurable in length with r. Since M > R, we have a > b [10.22, 10.20].

**Step 2.** Since a and b are rational, their squares are each commensurable with the square on r, and hence with one another [D10.1.3, 10.12]. But a and b are incommensurable in length: b is commensurable with r, whereas a is incommensurable with r [10.13]. Thus they are commensurable in square only. Consequently c = a − b is an apotome, with whole a and annex b [10.73].

**Step 3.** Subtracting the rectangle rb from the rectangle ra leaves the rectangle rc; hence M − R = rc [CN3]. Let s be the side of a square equal to this remaining area. Also construct d such that d² = a² − b² [2.14]. The direct route is now to classify c by its annex b, which is commensurable in length with the assigned rational line r, and then apply the corresponding rectangle-to-side theorem.

**Step 4.** Suppose first that d is commensurable in length with a. The square on the whole a then exceeds the square on the annex b by the square on a line commensurable with the whole. Since the annex b is commensurable in length with r, c is a second apotome [D10.3.2]. The remaining area is therefore contained by the rational line r and a second apotome. Its side s is consequently a first apotome of a medial straight line [10.92].

**Step 5.** Suppose instead that d is incommensurable in length with a. The square on the whole then exceeds the square on the annex by the square on a line incommensurable with the whole; since the annex is commensurable in length with r, c is a fifth apotome [D10.3.4, D10.3.5]. The remaining area is therefore contained by the rational line r and a fifth apotome. Its side s is consequently a straight line which produces with a rational area a medial whole [10.95].

**Step 6.** The two cases exhaust the possibilities. A first apotome of a medial straight line is irrational [10.74], and a straight line which produces with a rational area a medial whole is likewise irrational [10.77]. Therefore, when a rational area is subtracted from a medial area, the side of the remaining area is one of the two stated irrational straight lines: either a first apotome of a medial straight line or a straight line which produces with a rational area a medial whole. This proves the proposition.

**USED:** 1.44, 10.12, 10.13, 10.20, 10.22, 10.73, 10.74, 10.77, 10.92, 10.95, 2.14, CN3, D10.1.3, D10.3.2, D10.3.4, D10.3.5
**Human refs (from References field):** 10.13, 10.73, 10.92, 10.95, D10.3.2, D10.3.5
**Jaccard:** 0.375 — AI adds ['1.44', '10.12', '10.20', '10.22', '10.74', '10.77', '2.14', 'CN3', 'D10.1.3', 'D10.3.4']

## Proposition 10.110
**Statement:** If from a medial area there be subtracted a medial area incommensurable with the whole, the two remaining irrational straight lines arise, either a second apotome of a medial straight line or a straight line which produces with a medial area a medial whole.

**Step 1.** Let M be the whole medial area and N the medial area subtracted, where M>N and M,N are incommensurable. Choose an assigned rational straight line r, and apply M and N to it as rectangles, with breadths x and y respectively. These applications can be made by applying their triangular parts at right angles and adjoining the resulting rectangles [1.44; 2.1]. By 10.22, both x and y are rational and incommensurable in length with r. We use this common-base application because it leads directly to the classifications of the sides of areas.

**Step 2.** The rectangles have the same height r, so M:N=x:y [6.1]. Consequently x>y, and x,y are incommensurable in length [10.11]. Since both are rational, their squares are commensurable with the square on the assigned rational line, and hence with one another [D10.1.3; 10.12]. Thus x and y are commensurable in square only. Their difference a=x−y is therefore an apotome, with whole x and annex y [10.73].

**Step 3.** By partitioning the rectangle with sides r,x at breadth y, the remaining area M−N is exactly the rectangle with sides r,a [2.1; CN3]. Construct a straight line d whose square equals the excess of the square on x over the square on y [2.14]. There are now two exhaustive cases: d is commensurable in length with x, or it is not.

**Step 4.** Suppose d is commensurable in length with x. Neither the whole x nor the annex y is commensurable in length with r, and the square on x exceeds the square on y by the square on d. Hence a is a third apotome [D10.3.3]. Since M−N is contained by the rational straight line r and this third apotome, its square-side is a second apotome of a medial straight line [10.93], which is irrational [10.75].

**Step 5.** Suppose instead that d is incommensurable in length with x. The square on the whole then exceeds the square on the annex by the square on a straight line incommensurable with the whole; and neither whole nor annex is commensurable in length with r. Hence a is a sixth apotome [D10.3.4; D10.3.6]. Since M−N is contained by r and this sixth apotome, its square-side is a straight line which produces with a medial area a medial whole [10.96], which is irrational [10.78].

Thus, in every case, the side of the remaining area is either a second apotome of a medial straight line or a straight line which produces with a medial area a medial whole, as required.

**USED:** 1.44, 10.11, 10.12, 10.22, 10.73, 10.75, 10.78, 10.93, 10.96, 2.1, 2.14, 6.1, CN3, D10.1.3, D10.3.3, D10.3.4, D10.3.6
**Human refs (from References field):** 10.11, 10.22, 10.73, 10.93, 10.96, 6.1, D10.3.3, D10.3.6
**Jaccard:** 0.471 — AI adds ['1.44', '10.12', '10.75', '10.78', '2.1', '2.14', 'CN3', 'D10.1.3', 'D10.3.4']

## Proposition 10.111
**Statement:** The apotome is not the same with the binomial straight line.

**Step 1.** Suppose that a straight line L is both an apotome and a binomial. Use the common-square application route, which reduces the question to the first species. Apply the square on L to the assigned rational straight line e, and call the resulting breadth B. Since L is binomial, B is a first binomial; since L is an apotome, the same B is a first apotome. [10.60, 10.97]

**Step 2.** Accordingly, write B = p + q = r − s. Here p and q are rational straight lines commensurable in square only, with p the greater; r and s are likewise rational straight lines commensurable in square only, with r the whole and s the annex. Because these are the first species relative to e, both p and r are commensurable in length with e. [10.36, 10.73, D10.2.1, D10.3.1]

**Step 3.** The equality gives r = p + q + s. Set h = r − p, so that h = q + s > q. Since p and r are commensurable in length with e, they are commensurable with one another. Since r = p + h is commensurable with p, h is also commensurable with p, and hence with e. Thus h is rational. [10.12, 10.15, D10.1.3]

**Step 4.** The straight lines h and q are incommensurable in length: otherwise, since h is commensurable with p, q would also be commensurable with p, contrary to their being commensurable in square only. Nevertheless, h and q are both rational, so their squares are commensurable with the square on e and therefore with one another. Hence h and q are commensurable in square only. [10.12, D10.1.3]

**Step 5.** Subtracting q from h therefore leaves an irrational straight line, by the proposition defining the apotome. But h − q = s, and s is rational by Step 2. This is a contradiction. Consequently, an apotome cannot be the same straight line as a binomial. [10.73]

**USED:** 10.12, 10.15, 10.36, 10.60, 10.73, 10.97, D10.1.3, D10.2.1, D10.3.1
**Human refs (from References field):** 10.12, 10.13, 10.15, 10.60, 10.73, 10.97, D10.2.1, D10.3.1
**Jaccard:** 0.700 — AI adds ['10.36', 'D10.1.3']; Human adds ['10.13']

## Proposition 10.112
**Statement:** The square on a rational straight line applied to the binomial straight line produces as breadth an apotome the terms of which are commensurable with the terms of the binomial and moreover in the same ratio; and further the apotome so arising will have the same order as the binomial straight line.

**Step 1.** Let the given binomial be a+b, where a>b, and let r be the rational straight line whose square is to be applied to it. Fix the same assigned rational straight line u throughout. By the definition of a binomial, a and b are rational and commensurable in square only. Thus a², b², and r² are commensurable with u². We take the direct difference-of-squares route, scaling the difference a−b to obtain the required breadth. [10.36; D10.1.3; D10.1.4]

**Step 2.** Put Δ=a²−b². Since a² and b² are commensurable, the converse part of 10.15, applied to a²=b²+Δ, shows that Δ is commensurable with b². Consequently Δ is commensurable with u² and with r². It is therefore a positive rational area, and there are positive integers m,n such that r²:Δ=m:n. [10.12; 10.15; D10.1.4; 10.5]

**Step 3.** Construct c and d by taking m copies of an nth part of a and b respectively; the prescribed parts can be obtained by 6.9. Then c>d and
c:a=d:b=m:n.
Hence c is commensurable in length with a, and d with b. Alternating the proportion also gives c:d=a:b, which is the required equality of the ratios of corresponding terms. [6.9; 10.6; 5.16]

**Step 4.** Since c is commensurable in length with a, their squares have the ratio of a square number to a square number and are therefore commensurable. Likewise d² is commensurable with b². Thus c² and d² are each commensurable with u², so c and d are rational and commensurable in square. But a and b are incommensurable in length, and a:b=c:d; therefore c and d are also incommensurable in length. It follows that c−d is an apotome, with whole c and annex d. [10.9; 10.6; 10.12; D10.1.3; 10.11; 10.73]

**Step 5.** Use 2.5 for the difference-of-squares rectangle: a+b and a−b are the unequal parts of a line whose equal halves are a. It gives
(a+b)(a−b)=a²−b²=Δ,
where products denote rectangles. Also, subtracting corresponding parts in c:a=d:b gives
(c−d):(a−b)=m:n.
The rectangles with common height a+b consequently satisfy
(a+b)(c−d):Δ=m:n=r²:Δ.
Having the same ratio to Δ, these areas are equal. Thus (a+b)(c−d)=r², and c−d is precisely the breadth produced by applying the square on r to the binomial. [2.5; 5.19; 6.1; 5.9]

**Step 6.** We now check the order. Because c is commensurable in length with a, c is commensurable in length with u if and only if a is; similarly, d is commensurable in length with u if and only if b is. Furthermore, since a:b=c:d, 10.14 preserves the other defining distinction: the square on the greater term exceeds that on the lesser by the square on a line commensurable with the greater term in both pairs, or by the square on a line incommensurable with the greater term in both pairs. [10.12; 10.14]

**Step 7.** The definitions of the six orders therefore agree for the binomial a+b and the apotome c−d:
• When the square-excess side is commensurable with the greater term, the order is first, second, or third according as the greater term, the lesser term, or neither term is commensurable in length with u. These alternatives are preserved by Step 6. [D10.2.1; D10.2.2; D10.2.3; D10.3.1; D10.3.2; D10.3.3]
• When the square-excess side is incommensurable with the greater term, the same three alternatives give the fourth, fifth, or sixth order, respectively, and are likewise preserved. [D10.2.4; D10.2.5; D10.2.6; D10.3.4; D10.3.5; D10.3.6]
Thus the breadth is an apotome of the same order as the binomial; its terms are respectively commensurable in length with the binomial’s terms and are in the same ratio. This proves the proposition.

**USED:** 10.11, 10.12, 10.14, 10.15, 10.36, 10.5, 10.6, 10.73, 10.9, 2.5, 5.16, 5.19, 5.9, 6.1, 6.9, D10.1.3, D10.1.4, D10.2.1, D10.2.2, D10.2.3, D10.2.4, D10.2.5, D10.2.6, D10.3.1, D10.3.2, D10.3.3, D10.3.4, D10.3.5, D10.3.6
**Human refs (from References field):** 10.11, 10.12, 10.14, 10.15, 10.20, 10.36, 10.73, 5.11, 5.12, 5.14, 5.16, 5.17, 6.16, 6.22, D5.9
**Jaccard:** 0.189 — AI adds ['10.5', '10.6', '10.9', '2.5', '5.19', '5.9', '6.1', '6.9', 'D10.1.3', 'D10.1.4', 'D10.2.1', 'D10.2.2', 'D10.2.3', 'D10.2.4', 'D10.2.5', 'D10.2.6', 'D10.3.1', 'D10.3.2', 'D10.3.3', 'D10.3.4', 'D10.3.5', 'D10.3.6']; Human adds ['10.20', '5.11', '5.12', '5.14', '5.17', '6.16', '6.22', 'D5.9']

## Proposition 10.113
**Statement:** The square on a rational straight line, if applied to an apotome, produces as, breadth the binomial straight line the terms of which are commensurable with the terms of the apotome and in the same ratio; and further the binomial so arising has the same order as the apotome.

**Step 1.** Let r be the given rational straight line, A the given apotome, and X the breadth obtained by applying the square on r to A. Thus the rectangle A·X equals r². Write A = u − v, where u > v are rational straight lines commensurable in square only [10.73]. Set S = u + v; then S is binomial [10.36]. We use this conjugate sum to establish that X is binomial, and then apply the preceding proposition in its stated direction to obtain the term and order assertions.

**Step 2.** Let T be the rectangle A·S. Apply II.5 to a straight line of length 2u, bisected into lengths u and cut unequally into lengths u − v and u + v. It gives
T + v² = u².
Thus T is the excess of the square on u over the square on v [2.5].

**Step 3.** Since u and v are commensurable in square, u² and v² are commensurable [D10.1.2]. Consequently, from u² = T + v², the converse assertion of X.15 shows that T and v² are commensurable [10.15]. Moreover, because v and r are rational, their squares are each commensurable with the square on the assigned rational straight line, and hence are commensurable with one another [D10.1.3, D10.1.2, 10.12]. Therefore T and r² are commensurable [10.12].

**Step 4.** The rectangles A·X and A·S have the same height A. Hence
r² : T = (A·X) : (A·S) = X : S
[6.1]. Since r² and T are commensurable, X and S are commensurable in length [10.11].

**Step 5.** Since S is binomial and X is commensurable with it in length, X is itself binomial [10.66].

**Step 6.** Now apply the square on r to the binomial X. Its breadth is A, since X·A = r². Proposition X.112 therefore says that this apotome has terms respectively commensurable with the terms of X and in the same ratio, and that its order is the same as that of X [10.112]. The apotome terms obtained are precisely u and v: only one rational annex commensurable in square only with the whole can belong to A [10.79]. Thus, writing the corresponding binomial terms as c and d, we have c commensurable in length with u, d commensurable in length with v, and c : d = u : v. Also, X and A have the same order. Therefore the square on a rational straight line, applied to an apotome, produces exactly the binomial breadth asserted.

**USED:** 10.11, 10.112, 10.12, 10.15, 10.36, 10.66, 10.73, 10.79, 2.5, 6.1, D10.1.2, D10.1.3
**Human refs (from References field):** 10.11, 10.12, 10.14, 10.15, 10.20, 10.36, 10.73, 5.11, 5.14, 5.16, 5.19, 6.16, D10.1.3, D5.9
**Jaccard:** 0.300 — AI adds ['10.112', '10.66', '10.79', '2.5', '6.1', 'D10.1.2']; Human adds ['10.14', '10.20', '5.11', '5.14', '5.16', '5.19', '6.16', 'D5.9']

## Proposition 10.114
**Statement:** If an area be contained by an apotome and the binomial straight line the terms of which are commensurable with the terms of the apotome and in the same ratio, the âsideâ of the area is rational.

**Step 1.** Let the given apotome be A = a − b and the given binomial be B = c + d, with corresponding greater terms a and c. By hypothesis, a and c are commensurable in length, b and d are commensurable in length, and a:b = c:d. Let R be the rectangle contained by A and B. Choose the assigned rational straight line r. [D10.1.3]

**Step 2.** Apply the square on r to A. By 10.113 its breadth is a binomial C = e + f, whose terms e and f are respectively commensurable in length with a and b, and satisfy e:f = a:b. Thus the rectangle contained by A and C equals the square on r. This is the direct comparison route: 10.113 is chosen because the fixed factor is an apotome. [10.113]

**Step 3.** Since c:d and e:f both equal a:b, we have c:d = e:f. Alternating gives c:e = d:f; therefore, by adding antecedents and consequents,
(c + d):(e + f) = c:e,
that is, B:C = c:e. [5.11, 5.16, 5.12]

**Step 4.** Both c and e are commensurable in length with a, so they are commensurable with one another. Since B:C = c:e, B and C are consequently commensurable in length. [10.12, 10.11]

**Step 5.** The rectangles contained by A, B and by A, C have the same height A. Hence their ratio is B:C. The second rectangle equals the square on r, so R has to the square on r the ratio B:C. Since B and C are commensurable, R and the square on r are commensurable areas. [6.1, 10.11]

**Step 6.** Construct a square equal to R, and let its side be s. The square on s is commensurable with the square on the assigned rational straight line r; thus s is commensurable in square with r and is therefore rational. Consequently the “side” of the area contained by the given apotome and binomial is rational, as required. [2.14, D10.1.2, D10.1.3]

**USED:** 10.11, 10.113, 10.12, 2.14, 5.11, 5.12, 5.16, 6.1, D10.1.2, D10.1.3
**Human refs (from References field):** 10.11, 10.112, 10.12, 5.19, 6.1
**Jaccard:** 0.250 — AI adds ['10.113', '2.14', '5.11', '5.12', '5.16', 'D10.1.2', 'D10.1.3']; Human adds ['10.112', '5.19']

## Proposition 10.115
**Statement:** From a medial straight line there arise irrational straight lines infinite in number, and none of them is the same as any of the preceding.

**Step 1.** Fix a rational straight line \(u\), and let \(x_0\) be the given medial straight line. For a straight line \(z\), write \(T(z)\) for the breadth obtained by applying its square to \(u\); thus \(u\,T(z)=z^2\). We choose successive mean proportionals, because square-application reverses this construction directly. Given \(x_n\), construct \(x_{n+1}\) as a mean proportional between \(u\) and \(x_n\). Then
\[
x_{n+1}^{\,2}=u x_n,\qquad T(x_{n+1})=x_n.
\]
This construction can be repeated after every finite number of steps. [6.13, 6.17]

**Step 2.** Every \(x_n\) is irrational. The initial line \(x_0\) is irrational because it is medial. If \(x_{n+1}\) were rational, its square would be a rational area; applying that area to the rational line \(u\) would produce a rational breadth. But that breadth is \(x_n\). Thus the irrationality of \(x_n\) implies that of \(x_{n+1}\), and the assertion follows successively from \(x_0\). Moreover, \(T(x_0)\) is rational, since the square on a medial line applied to a rational line produces a rational breadth. [10.21, D10.1.3, D10.1.4, 10.20, 10.22]

**Step 3.** None of \(x_1,x_2,\ldots\) is medial. Indeed, if \(x_n\) were medial, where \(n\geq1\), then \(T(x_n)\) would be rational. Yet \(T(x_n)=x_{n-1}\), which is irrational by Step 2. [10.22]

**Step 4.** Consider the six previously established additive kinds: the binomial, the first and second bimedials, the major, the side of a rational plus a medial area, and the side of the sum of two medial areas. Applying the square of any one of these to \(u\) produces a binomial. Applying the square of a binomial to \(u\) again produces a binomial. Consequently, every positive iterate of \(T\) on a line of any of these six kinds is a binomial and therefore irrational. [10.60, 10.61, 10.62, 10.63, 10.64, 10.65; 10.36]

**Step 5.** Likewise, consider the six subtractive kinds: the apotome, the first and second apotomes of a medial line, the minor, the line which produces with a rational area a medial whole, and the line which produces with a medial area a medial whole. Applying their squares to \(u\) produces apotomes; applying the square of an apotome to \(u\) again produces an apotome. Thus every positive iterate of \(T\) on a line of any of these six kinds is an apotome and therefore irrational. [10.97, 10.98, 10.99, 10.100, 10.101, 10.102; 10.73]

**Step 6.** For every \(n\geq1\), reversing the successive constructions gives
\[
T^n(x_n)=x_0,\qquad T^{n+1}(x_n)=T(x_0),
\]
where the last line is rational. Hence \(x_n\) cannot belong to any of the twelve kinds in Steps 4–5, since all their positive iterates remain irrational. By Step 3 it is not medial either. Each constructed line is therefore different in kind from all thirteen previously established irrational kinds. [6.17, 10.22; the square-application results invoked in Steps 4–5]

**Step 7.** The constructed lines are also distinct from one another. If \(x_i=x_j\) with \(0\leq i<j\), applying \(T\) exactly \(i\) times would give \(x_0=x_{j-i}\). This is impossible: \(x_0\) is medial, whereas \(x_{j-i}\), whose index is positive, is not medial. Equivalently, the first rational iterate of \(x_n\) occurs exactly after \(n+1\) square-applications. Since a further mean proportional can always be constructed, the process supplies irrational straight lines without end, none equal to an earlier one and none of the previously established kinds. Therefore, from a medial straight line there arise irrational straight lines infinite in number, and none is the same as any of the preceding. [6.13, 6.17, 10.22]

**USED:** 10.100, 10.101, 10.102, 10.20, 10.21, 10.22, 10.36, 10.60, 10.61, 10.62, 10.63, 10.64, 10.65, 10.73, 10.97, 10.98, 10.99, 6.13, 6.17, D10.1.3, D10.1.4
**Human refs (from References field):** 10.20, D10.1.4
**Jaccard:** 0.095 — AI adds ['10.100', '10.101', '10.102', '10.21', '10.22', '10.36', '10.60', '10.61', '10.62', '10.63', '10.64', '10.65', '10.73', '10.97', '10.98', '10.99', '6.13', '6.17', 'D10.1.3']
