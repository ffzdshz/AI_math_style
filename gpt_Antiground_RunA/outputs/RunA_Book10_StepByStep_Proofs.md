# Book 10 of Euclid's Elements — Step-by-Step AI Proofs (Run A)

## Proposition 10.1
**Statement:** Two unequal magnitudes being set out, if from the greater there be subtracted a magnitude greater than its half, and from that which is left a magnitude greater than its half, and if this process be repeated continually, there will be left some magnitude which will be less than the lesser magnitude set out.

**Step 1.** Let A be the greater magnitude and B the lesser. We use a finite-multiple comparison: choose a finite positive integer n such that nB > A, where nB denotes the sum of n copies of B. Such a multiple exists by D5.4. [D5.4]

**Step 2.** Write R₀ = A. For each prescribed subtraction, let Sᵢ be the magnitude removed and Rᵢ the remainder, so Rᵢ₋₁ = Sᵢ + Rᵢ. Let Hᵢ be half of Rᵢ₋₁. By hypothesis, Sᵢ = Hᵢ + Eᵢ for some positive excess Eᵢ. Thus Hᵢ + Hᵢ = Hᵢ + Eᵢ + Rᵢ; subtracting Hᵢ gives Hᵢ = Eᵢ + Rᵢ. Consequently Sᵢ > Hᵢ > Rᵢ: each removed magnitude exceeds the remainder it leaves. [Hypothesis; CN3, CN5]

**Step 3.** Consider the remainder Rₙ after n subtractions, and suppose that Rₙ ≥ B. Each remainder is a proper part of its predecessor, so Rᵢ ≥ Rₙ ≥ B for every i from 1 to n. By Step 2, therefore, Sᵢ > Rᵢ ≥ B for every such i. [CN5; Step 2]

**Step 4.** Since each Sᵢ exceeds B, write Sᵢ = B + Fᵢ with Fᵢ positive. Adding these equalities gives
S₁ + ⋯ + Sₙ = nB + (F₁ + ⋯ + Fₙ) > nB.
Thus the total magnitude removed exceeds nB. [CN2, CN5]

**Step 5.** The successive decompositions in Step 2 give A = S₁ + ⋯ + Sₙ + Rₙ. Hence A > S₁ + ⋯ + Sₙ > nB, contrary to nB > A from Step 1. The supposition Rₙ ≥ B is therefore impossible, and Rₙ < B. Thus after finitely many of the prescribed subtractions there is left a magnitude less than the lesser magnitude originally set out. [CN2, CN5; Steps 1, 4]

**USED:** CN2, CN3, CN5, D5.4
**Human refs (from References field):** D5.4
**Jaccard:** 0.250 — AI adds ['CN2', 'CN3', 'CN5']

## Proposition 10.2
**Statement:** If, when the less of two unequal magnitudes is continually subtracted in turn from the greater, that which is left never measures the one before it, the magnitudes will be incommensurable.

**Step 1.** Let A > B be the given magnitudes. Suppose, contrary to the conclusion, that they are commensurable. Then some magnitude E measures both A and B [D10.1.1]. We use 10.1 directly on alternate remainders; this keeps the argument entirely about magnitudes.

**Step 2.** Record the remainders at successive turns of the subtraction process as r₀ = A, r₁ = B, r₂, r₃, …. Thus, for each i ≥ 1,
 rᵢ₋₁ = qᵢrᵢ + rᵢ₊₁, with 0 < rᵢ₊₁ < rᵢ,
where qᵢrᵢ denotes a positive whole multiple of rᵢ [D5.2]. Each block of subtractions is finite, since a sufficiently large multiple of the magnitude being subtracted exceeds the magnitude from which it is subtracted [D5.4]. Exact exhaustion would mean that the lesser magnitude measures its predecessor, contrary to the hypothesis. Hence these positive remainders continue indefinitely [hypothesis].

**Step 3.** The magnitude E measures every remainder. Indeed, it measures r₀ and r₁. Whenever it measures rᵢ₋₁ and rᵢ, the multiple qᵢrᵢ consists of whole copies of E, by repeated addition [D5.2; CN2]. Subtracting those copies from the whole copies constituting rᵢ₋₁ leaves whole copies of E constituting rᵢ₊₁ [CN3]. Since this remainder is positive, E measures it [D5.2]. Repeating this argument establishes the assertion throughout the process.

**Step 4.** At every turn, the removed magnitude qᵢrᵢ is at least rᵢ, and rᵢ > rᵢ₊₁. Thus the removed magnitude is greater than the remainder [CN5; Step 2]. Consequently, in
 rᵢ₋₁ = qᵢrᵢ + rᵢ₊₁,
the removed magnitude is greater than half the whole, and the remainder is less than half the whole [CN2; CN3]. In particular, the sequence r₀, r₂, r₄, … is obtained by repeatedly subtracting more than half of the magnitude currently remaining.

**Step 5.** Since E measures B, we have E ≤ B < A [D5.2; CN5]. Apply 10.1 to the unequal magnitudes A and E and to the successive removals producing r₂, r₄, …. By Step 4, each removal exceeds half the current magnitude. Therefore some positive remainder r₂ₖ is less than E [10.1].

**Step 6.** But E measures r₂ₖ by Step 3. A positive magnitude composed of whole copies of E is either equal to E or greater than E; it cannot be less than E [D5.2; CN5]. This contradicts Step 5. Therefore A and B have no common measure and are incommensurable [D10.1.1].

**USED:** 10.1, CN2, CN3, CN5, D10.1.1, D5.2, D5.4
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['10.1', 'CN2', 'CN3', 'CN5', 'D10.1.1', 'D5.2', 'D5.4']

## Proposition 10.3
**Statement:** Given two commensurable magnitudes, to find their greatest common measure.

**Step 1.** Let A and B be the given commensurable magnitudes, ordered so that A ≥ B. They therefore admit a common measure [D10.1.1]. If B measures A, return B: it measures both magnitudes, and no measure of B can exceed B, since B consists of one or more copies of that measure [D5.2, CN5]. This includes the case A = B. Hence suppose A > B and B does not measure A.

**Step 2.** Repeatedly subtract the smaller magnitude from the greater, replacing the pair X > Y by Y and X − Y and reordering as necessary. Stop as soon as the smaller magnitude measures the greater. We choose this direct subtraction route because 10.2 supplies precisely the required termination criterion for magnitudes [10.2].

**Step 3.** The process must terminate. Otherwise the successive subtraction would never yield a remainder measuring its predecessor, and A and B would be incommensurable [10.2], contrary to their having a common measure [D10.1.1]. Denote the terminal pair by U and D, where D measures U.

**Step 4.** The magnitude D measures both original magnitudes. Indeed, it measures both members U and D of the terminal pair. At any preceding subtraction, the pair X, Y was replaced by Y, X − Y. If D measures Y and X − Y, then each consists of whole copies of D; adding those copies shows that D measures X = Y + (X − Y) [D5.2, CN2]. Applying this argument backwards through the finite sequence shows that D measures A and B.

**Step 5.** Let E be any common measure of A and B. At each subtraction, if E measures X and Y, then X and Y consist of whole copies of E. Subtracting the copies constituting Y from those constituting X leaves whole copies of E constituting X − Y; thus E measures the new pair Y, X − Y [D5.2, CN3]. Applying this argument forwards through the sequence shows that E measures D.

**Step 6.** Since E measures D, either D consists of one copy of E, so E = D, or E is a proper part of D, so E < D [D5.2, CN5]. Therefore every common measure of A and B is no greater than D. By Step 4, D itself is a common measure. Hence the last smaller magnitude D obtained by the terminating subtraction process is the greatest common measure of A and B, as required.

**USED:** 10.2, CN2, CN3, CN5, D10.1.1, D5.2
**Human refs (from References field):** 10.2
**Jaccard:** 0.167 — AI adds ['CN2', 'CN3', 'CN5', 'D10.1.1', 'D5.2']

## Proposition 10.4
**Statement:** Given three commensurable magnitudes, to find their greatest common measure.

**Step 1.** Let A, B, C be the three given commensurable magnitudes, and let U be a measure common to them [D10.1.1]. By 10.3, construct the greatest common measure D of A and B, using successive subtraction. Path choice: use the two-magnitude construction successively, since it applies directly to magnitudes without translating the problem into arithmetic [10.3].

**Step 2.** Track any common measure T of A and B through this construction. Whenever two magnitudes are integral multiples of T, subtracting the smaller from the larger leaves an integral multiple of T: cancel their equal constituent copies of T [D5.2, CN3]. Consequently T measures every remainder in the successive-subtraction construction of 10.3, and therefore measures its final output D. If one input already measures the other, the output is that input, which T also measures. Thus every common measure of A and B measures D [10.3, D5.2, CN3].

**Step 3.** In particular, U measures D by Step 2. Since U also measures C, the magnitudes D and C are commensurable [D10.1.1].

**Step 4.** Apply 10.3 to D and C, and construct their greatest common measure E. If D already measures C, this application simply returns E = D; otherwise use the successive-subtraction construction [10.3].

**Step 5.** Since E measures D, while D measures A and B, both A and B consist of finitely many copies of E: replace each constituent copy of D by its constituent copies of E [D5.2, CN2]. Also E measures C by its construction in Step 4 [10.3]. Hence E is a common measure of A, B, C [D10.1.1].

**Step 6.** Let H be any common measure of A, B, C. Since H measures A and B, Step 2 shows that H measures D. Thus H measures both D and C. Applying the same remainder-preservation argument of Step 2 to the construction in Step 4 shows that H measures E [10.3, D5.2, CN3]. A measure of E cannot exceed E: either it equals E or it is one of several equal parts composing E [D5.2, CN5]. Therefore no common measure of A, B, C exceeds E. Together with Step 5, this proves that the constructed E is their greatest common measure, as required.

**USED:** 10.3, CN2, CN3, CN5, D10.1.1, D5.2
**Human refs (from References field):** 10.3
**Jaccard:** 0.167 — AI adds ['CN2', 'CN3', 'CN5', 'D10.1.1', 'D5.2']

## Proposition 10.5
**Statement:** Commensurable magnitudes have to one another the ratio which a number has to a number.

**Step 1.** Let A and B be commensurable magnitudes. By D10.1.1, some magnitude E measures both. Thus A consists of m copies of E and B of n copies of E, where m and n are positive counts, possibly one (D5.2). Our path is to use this arbitrary common measure: no greatest common measure is needed.

**Step 2.** Let T be the number consisting of two units. Form M from m copies of T and N from n copies of T. By D7.2, M and N are numbers; each contains at least two units, even if one of the counts is one.

**Step 3.** We have E:E = T:T. Indeed, for any positive counts r and s, rE and sE are equal when r = s, by repeated addition of equals (CN2). When r > s, sE is a proper part of rE, so rE > sE (CN5); the reverse inequality holds when r < s. Exactly the same comparisons hold between rT and sT. Consequently the corresponding equimultiples agree in being greater, equal, or less, and the asserted equality of ratios follows from D5.5.

**Step 4.** Apply 5.4 to E:E = T:T, taking m copies of the first and third terms and n copies of the second and fourth terms. This matching-equimultiples form makes 5.4 the direct choice. It gives mE:nE = mT:nT, that is, A:B = M:N. If a count is one, its corresponding terms simply remain unchanged. Since M and N are numbers by Step 2, the commensurable magnitudes A and B have to one another the ratio which a number has to a number.

**USED:** 5.4, CN2, CN5, D10.1.1, D5.2, D5.5, D7.2
**Human refs (from References field):** 5.22, 5.7, D7.20
**Jaccard:** 0.000 — AI adds ['5.4', 'CN2', 'CN5', 'D10.1.1', 'D5.2', 'D5.5', 'D7.2']; Human adds ['5.22', '5.7', 'D7.20']

## Proposition 10.6
**Statement:** If two magnitudes have to one another the ratio which a number has to a number, the magnitudes will be commensurable.

**Step 1.** Let the magnitudes A and B satisfy A:B = m:n, where m and n are numbers, hence finite multitudes of units (D7.2). Path choice: transfer successive subtractions of the numerical counts to the magnitudes by separation of a proportion (5.17); the terminal pair will provide a common measure.

**Step 2.** Suppose the current proportion is X:Y = r:s, where r and s are positive integral counts, possibly a single unit. By D5.5, taking both multipliers to be one, X exceeds, equals, or falls short of Y according as r exceeds, equals, or falls short of s. If r>s, separation gives
(X−Y):Y = (r−s):s
by 5.17. This proposition applies directly because we subtract the consequent from the antecedent. If s>r, first interchange X with Y and r with s: the inverse ratios remain equal by D5.5. Then perform the same subtraction.

**Step 3.** Starting with A:B = m:n, repeat Step 2 whenever the two numerical counts are unequal. Each subtraction leaves both counts positive and decreases their combined number of units by at least one. Since the initial counts contain only finitely many units, this process must terminate; it can terminate only with equal counts, say d and d (D7.2). Throughout, the corresponding magnitude ratio remains equal to the numerical ratio by 5.17 and D5.5.

**Step 4.** Let X and Y be the terminal magnitudes. Then X:Y = d:d. Applying D5.5 with both multipliers equal to one gives X=Y. Denote their common magnitude by E.

**Step 5.** Reverse the finite sequence. The magnitude E measures both terminal magnitudes, each once. An interchange does not affect this fact. Undoing a subtraction restores the former larger magnitude as the sum of the two current magnitudes. If those magnitudes consist of p copies and q copies of E, their sum consists of p+q copies of E, so E measures that sum as well (CN2; D5.2). Consequently, reversing every operation shows that E measures both original magnitudes A and B.

**Step 6.** Since A and B are measured by the same magnitude E, they are commensurable by D10.1.1. Therefore magnitudes having to one another the ratio which a number has to a number are commensurable.

**USED:** 5.17, CN2, D10.1.1, D5.2, D5.5, D7.2
**Human refs (from References field):** 5.11, 5.22, 5.7, 5.9, D7.20
**Jaccard:** 0.000 — AI adds ['5.17', 'CN2', 'D10.1.1', 'D5.2', 'D5.5', 'D7.2']; Human adds ['5.11', '5.22', '5.7', '5.9', 'D7.20']

## Proposition 10.7
**Statement:** Incommensurable magnitudes have not to one another the ratio which a number has to a number.

**Step 1.** Let A and B be incommensurable magnitudes. They therefore cannot have any common measure [D10.1.1].

**Step 2.** Suppose, for contradiction, that A:B = m:n for some numbers m and n. Then A and B are commensurable [10.6]. This is the direct contrapositive route: 10.6 applies exactly to the supposed numerical ratio.

**Step 3.** Being commensurable, A and B have a common measure, contrary to Step 1 [D10.1.1]. Hence no such numbers m and n exist. Therefore incommensurable magnitudes have not to one another the ratio which a number has to a number.

**USED:** 10.6, D10.1.1
**Human refs (from References field):** 10.6
**Jaccard:** 0.500 — AI adds ['D10.1.1']

## Proposition 10.8
**Statement:** If two magnitudes have not to one another the ratio which a number has to a number, the magnitudes will be incommensurable.

**Step 1.** Let A and B be magnitudes such that A:B is not the ratio of any number to any number. (Hypothesis.) We use 10.5 by contradiction, since it directly gives a numerical ratio from commensurability.

**Step 2.** Suppose, for contradiction, that A and B have a common measure. Then A and B are commensurable. (D10.1.1.)

**Step 3.** Since A and B are commensurable, they have to one another the ratio which a number has to a number. (10.5.) This contradicts the hypothesis in Step 1.

**Step 4.** Therefore A and B cannot have any common measure, and hence they are incommensurable, as required. (Step 3; D10.1.1.)

**USED:** 10.5, D10.1.1
**Human refs (from References field):** 10.5
**Jaccard:** 0.500 — AI adds ['D10.1.1']

## Proposition 10.9
**Statement:** The squares on straight lines commensurable in length have to one another the ratio which a square number has to a square number; and squares which have to one another the ratio which a square number has to a square number will also have their sides commensurable in length. But the squares on straight lines incommensurable in length have not to one another the ratio which a square number has to a square number; and squares which have not to one another the ratio which a square number has to a square number will not have their sides commensurable in length either.

**Step 1.** Let a and b be straight lines, and write Q(a) and Q(b) for their squares. Any two squares are similar: their corresponding angles are equal right angles, and their corresponding sides are proportional because each square is equilateral [D1.22, P4, D6.1].

**Step 2.** Suppose first that a and b are commensurable in length. By 10.5 there are numbers m and n such that a:b = m:n [10.5].

**Step 3.** The ratio Q(a):Q(b) is the duplicate ratio of a:b [6.20]. Also, the square numbers m² and n² have the duplicate ratio of their sides m and n [8.11]. Equal ratios have equal duplicate ratios: this follows by applying 5.22 to the three-term proportions defining duplication [D5.9, 5.22]. Consequently,
Q(a):Q(b) = m²:n².
This proves the first assertion. The direct route is 6.20, since the squares themselves are similar polygons; no subdivision into triangles is needed.

**Step 4.** Conversely, suppose that Q(a):Q(b) = m²:n² for some square numbers m² and n² with sides m and n. Choose a straight line u, and form straight lines c and d consisting respectively of m and n copies of u. Then c:d = m:n: in the comparison of any equimultiples, the lengths are ordered exactly as their numbers of copies of u [D5.5]. Moreover, u measures both c and d, so they are commensurable in length [D10.1.1].

**Step 5.** Applying the duplicate-ratio argument of Step 3 to c:d = m:n gives Q(c):Q(d) = m²:n² [6.20, 8.11, D5.9, 5.22]. Together with the hypothesis, this yields
Q(a):Q(b) = Q(c):Q(d)
[5.11].

**Step 6.** The four squares are similar and similarly described on their respective sides. Therefore the converse of 6.22, applied to the proportion in Step 5, gives a:b = c:d [6.22]. Since c:d = m:n, it follows that a:b = m:n [5.11]. Hence a and b are commensurable in length [10.6]. This proves the second assertion. Here 6.22 is the direct converse tool, because it recovers the proportion of the sides from the proportion of their similar figures.

**Step 7.** Now suppose that a and b are incommensurable in length. If Q(a):Q(b) were the ratio of a square number to a square number, Steps 4–6 would make a and b commensurable in length, contrary to their having no common measure [D10.1.1]. Thus their squares cannot have the ratio of a square number to a square number.

**Step 8.** Finally, suppose that Q(a):Q(b) is not the ratio of a square number to a square number. If a and b were commensurable in length, Steps 2–3 would give precisely such a ratio, a contradiction. Hence their sides are incommensurable in length [D10.1.1]. All four assertions are proved.

**USED:** 10.5, 10.6, 5.11, 5.22, 6.20, 6.22, 8.11, D1.22, D10.1.1, D5.5, D5.9, D6.1, P4
**Human refs (from References field):** 10.5, 10.6, 6.20, 8.11
**Jaccard:** 0.308 — AI adds ['5.11', '5.22', '6.22', 'D1.22', 'D10.1.1', 'D5.5', 'D5.9', 'D6.1', 'P4']

## Proposition 10.10
**Statement:** To find two straight lines incommensurable, the one in length only, and the other in square also, with an assigned straight line.

**Step 1.** Choose the numerical ratio 3:2. This is not the ratio of a square number to a square number. For, between two square numbers there is a mean proportional number [8.11]; if their ratio were 3:2, a mean proportional number would therefore also exist between 3 and 2 [8.8]. Such a number would lie strictly between 2 and 3, whereas no multitude of units lies between these consecutive numbers [D7.2]. This choice allows us to use established propositions about square numbers directly.

**Step 2.** Let a be the assigned straight line, and write S(t) for the square on a straight line t. Cut off one third of a, and let d be the remaining straight line [6.9]. Thus a consists of three equal parts and d of two of those parts, so a:d = 3:2 [D5.5].

**Step 3.** Construct a mean proportional x between a and d, so that a:x = x:d [6.13]. The square S(x) consequently equals the rectangle contained by a and d [6.17]. Comparing that rectangle with S(a), with a as their common altitude, gives
S(a):S(x) = a:d = 3:2 [6.1].

**Step 4.** Since S(a):S(x) is a ratio of numbers, these squares are commensurable [10.6]; hence a and x are commensurable in square [D10.1.2]. But, by Step 1, their squares do not have the ratio of a square number to a square number. Therefore a and x are incommensurable in length [10.9]. Thus x satisfies the first requirement: it is incommensurable with a in length only.

**Step 5.** Construct a mean proportional y between a and x, so that a:y = y:x [6.13]. Then S(y) equals the rectangle contained by a and x [6.17]. Comparing this rectangle with S(a), again using their common altitude a, gives
S(a):S(y) = a:x [6.1].

**Step 6.** Since a and x are incommensurable in length, a:x is not the ratio of a number to a number [10.7]. Consequently S(a):S(y) is not such a ratio either. Applying 10.8 directly to these square areas, S(a) and S(y) are incommensurable; hence a and y are incommensurable in square [D10.1.2]. Their squares in particular cannot have the ratio of a square number to a square number, so a and y are also incommensurable in length [10.9]. Therefore the constructed straight lines x and y are the required lines: x is incommensurable with the assigned line in length only, and y in square also.

**USED:** 10.6, 10.7, 10.8, 10.9, 6.1, 6.13, 6.17, 6.9, 8.11, 8.8, D10.1.2, D5.5, D7.2
**Human refs (from References field):** 10.11, 10.6, 10.9, D5.9
**Jaccard:** 0.133 — AI adds ['10.7', '10.8', '6.1', '6.13', '6.17', '6.9', '8.11', '8.8', 'D10.1.2', 'D5.5', 'D7.2']; Human adds ['10.11', 'D5.9']

## Proposition 10.11
**Statement:** If four magnitudes be proportional, and the first be commensurable with the second, the third will also be commensurable with the fourth; and, if the first be incommensurable with the second, the third will also be incommensurable with the fourth.

**Step 1.** Let A, B, C, D be proportional magnitudes, so that A:B = C:D [D5.6]. Path choice: use 10.5 followed by 10.6, since commensurability directly supplies a ratio of numbers; reuse this criterion by contradiction for the second assertion.

**Step 2.** Suppose A is commensurable with B. Then there are numbers m and n such that A:B = m:n [10.5].

**Step 3.** Since C:D and m:n have the same ratio as A:B, we have C:D = m:n [5.11]. Therefore C is commensurable with D [10.6]. This proves the first assertion.

**Step 4.** Now suppose A is incommensurable with B. Assume, for contradiction, that C is commensurable with D. There are then numbers p and q such that C:D = p:q [10.5]. Since A:B = C:D, it follows that A:B = p:q [5.11].

**Step 5.** Consequently A and B are commensurable [10.6], contrary to their having no common measure [D10.1.1]. Thus C and D cannot have a common measure and are incommensurable [D10.1.1]. Together with Step 3, this proves both assertions.

**USED:** 10.5, 10.6, 5.11, D10.1.1, D5.6
**Human refs (from References field):** 10.5, 10.6, 10.7, 10.8
**Jaccard:** 0.286 — AI adds ['5.11', 'D10.1.1', 'D5.6']; Human adds ['10.7', '10.8']

## Proposition 10.12
**Statement:** Magnitudes commensurable with the same magnitude are commensurable with one another also.

**Step 1.** Let A and B each be commensurable with C. Commensurability is symmetric, since a common measure measures both magnitudes (D10.1.1). Thus A and C, and C and B, are commensurable. By 10.5, there are numbers m, n, p, q such that A:C = m:n and C:B = p:q. We choose the numerical-ratio route because 10.5 applies immediately to both hypotheses.

**Step 2.** Form the numbers r = mp, s = np, and t = nq by multiplication (D7.15). Since m and n multiply the same number p, the resulting products have the ratio of their multipliers: r:s = m:n (7.18). This form of the multiplication theorem applies directly to the products defining r and s.

**Step 3.** Since the same number n multiplies p and q, the resulting products have the ratio of the numbers multiplied: s:t = p:q (7.17). Combining these numerical proportions with Step 1 gives A:C = r:s and C:B = s:t, because ratios equal to the same ratio are equal to one another (5.11).

**Step 4.** Apply 5.22, ex aequali, to the corresponding triples A, C, B and r, s, t. The proportions in Step 3 yield A:B = r:t.

**Step 5.** Therefore A and B have to one another the ratio of a number to a number. The direct numerical-ratio criterion, 10.6, now shows that A and B are commensurable. Hence magnitudes commensurable with the same magnitude are commensurable with one another.

**USED:** 10.5, 10.6, 5.11, 5.22, 7.17, 7.18, D10.1.1, D7.15
**Human refs (from References field):** 10.5, 10.6, 5.11, 5.22, 8.4
**Jaccard:** 0.444 — AI adds ['7.17', '7.18', 'D10.1.1', 'D7.15']; Human adds ['8.4']

## Proposition 10.13
**Statement:** If two magnitudes be commensurable, and the one of them be incommensurable with any magnitude, the remaining one will also be incommensurable with the same.

**Step 1.** Let A and B be commensurable magnitudes, and let A be incommensurable with C. Thus A and C have no common measure. [Hypotheses; D10.1.1]

**Step 2.** We use contradiction with 10.12, the direct route because it applies to magnitudes commensurable with the same magnitude. Suppose that B and C are commensurable. Then C is commensurable with B also, since a common measure measures both magnitudes irrespective of their order. [D10.1.1]

**Step 3.** A is commensurable with B by hypothesis, and C is commensurable with B by Step 2. Therefore A and C are commensurable, since magnitudes commensurable with the same magnitude are commensurable with one another. [10.12]

**Step 4.** Consequently A and C have a common measure, contradicting Step 1. Hence B and C cannot have a common measure and are therefore incommensurable, as required. [D10.1.1]

**USED:** 10.12, D10.1.1
**Human refs (from References field):** 10.12
**Jaccard:** 0.500 — AI adds ['D10.1.1']

## Proposition 10.14
**Statement:** If four straight lines be proportional, and the square on the first be greater than the square on the second by the square on a straight line commensurable with the first, the square on the third will also be greater than the square on the fourth by  the square on a straight line commensurable with the third. And, if the square on the first be greater than the square on the second by the square on a straight line incommensurable with the first, the square on the third will also be greater than the square on the fourth by the square on a straight line in-commensurable with the third.

**Step 1.** Let the four straight lines be a, b, c, d, with a:b = c:d. Write S(x) for the square on a straight line x, and let e be the straight line in the hypothesis, so that S(a) = S(b) + S(e). Construct a fourth proportional f to a, e, c; thus a:e = c:f [6.12]. Path choice: construct the prospective excess-side by proportion, allowing both commensurability cases to be treated directly without introducing numerical ratios.

**Step 2.** Alternating the given and constructed proportions gives a:c = b:d and a:c = e:f [5.16]. Squares are similar figures, so the squares on these proportional straight lines are proportional [6.22]. Therefore
S(a):S(c) = S(b):S(d),
and
S(a):S(c) = S(e):S(f).
Consequently S(b):S(d) = S(e):S(f) [5.11].

**Step 3.** Since these last two ratios are equal, the sum of their antecedents has to the sum of their consequents that same ratio [5.12]. Hence, using the equal ratios from Step 2 [5.11],
(S(b) + S(e)):(S(d) + S(f)) = S(a):S(c).
But S(b) + S(e) = S(a) by hypothesis. Thus S(a) has the same ratio to S(d) + S(f) as it has to S(c). Magnitudes to which the same magnitude has the same ratio are equal [5.9]; therefore
S(c) = S(d) + S(f).
In particular, S(c) is greater than S(d), and its excess is the square on f [CN5].

**Step 4.** If e is commensurable with a, apply 10.11 to the constructed proportion a:e = c:f. It follows that c is commensurable with f. Together with Step 3, this proves that the square on the third straight line exceeds the square on the fourth by the square on a straight line commensurable with the third [10.11].

**Step 5.** If instead e is incommensurable with a, the incommensurable case of 10.11, applied to the same proportion a:e = c:f, shows that c is incommensurable with f. Step 3 again gives S(c) = S(d) + S(f), so the excess is now the square on a straight line incommensurable with the third [10.11]. Both assertions are proved.

**USED:** 10.11, 5.11, 5.12, 5.16, 5.9, 6.12, 6.22, CN5
**Human refs (from References field):** 10.11, 5.17, 5.22, 6.22
**Jaccard:** 0.200 — AI adds ['5.11', '5.12', '5.16', '5.9', '6.12', 'CN5']; Human adds ['5.17', '5.22']

## Proposition 10.15
**Statement:** If two commensurable magnitudes be added together, the whole will also be commensurable with each of them; and, if the whole be commensurable with one of them, the original magnitudes will also be commensurable.

**Step 1.** Let the two magnitudes be A and B, and let W = A + B. First suppose that A and B are commensurable. There is therefore a magnitude E measuring both [D10.1.1]. Path choice: use this common measure directly; finding a greatest common measure is unnecessary.

**Step 2.** Since E measures A and B, write A = mE and B = nE, where m and n count the respective finite repetitions of E [D5.2]. Adding these equalities gives W = (m + n)E [CN2]. Thus E also measures W [D5.2]. Consequently W and A have the common measure E, as do W and B; hence W is commensurable with each of A and B [D10.1.1].

**Step 3.** Conversely, suppose that W is commensurable with one of the original magnitudes, which we may call A. Choose a common measure F of W and A [D10.1.1], and write W = rF and A = sF, where r and s count repetitions of F [D5.2]. Since W is the whole and A a proper part, W > A [CN5]; therefore r > s.

**Step 4.** Subtract A = sF from W = rF. The remainder B is equal to the remaining r − s copies of F [CN3]. Thus F measures B as well as A [D5.2], so A and B are commensurable [D10.1.1]. The naming of the parts was arbitrary, so this applies whichever part is commensurable with the whole. Both assertions are proved.

**USED:** CN2, CN3, CN5, D10.1.1, D5.2
**Human refs (from References field):** D10.1.1
**Jaccard:** 0.200 — AI adds ['CN2', 'CN3', 'CN5', 'D5.2']

## Proposition 10.16
**Statement:** If two incommensurable magnitudes be added together, the whole will also be incommensurable with each of them; and, if the whole be incommensurable with one of them, the original magnitudes will also be incommensurable.

**Step 1.** Let A and B be the two magnitudes, and let S = A + B be their whole. We use the two clauses of 10.15 by contradiction, choosing that proposition because it directly concerns commensurability of the same whole and parts. By D10.1.1, incommensurable magnitudes are precisely those having no common measure.

**Step 2.** Suppose A and B are incommensurable. If S were commensurable with either A or B, the second clause of 10.15 would imply that A and B are commensurable, contrary to the hypothesis. Therefore S is not commensurable with either part, and hence is incommensurable with each of them. [10.15; D10.1.1]

**Step 3.** Conversely, suppose S is incommensurable with one of A and B. If A and B were commensurable, the first clause of 10.15 would make S commensurable with each of them, including the part with which it is assumed incommensurable. This is a contradiction. Therefore A and B are incommensurable. Both assertions are proved. [10.15; D10.1.1]

**USED:** 10.15, D10.1.1
**Human refs (from References field):** D10.1.1
**Jaccard:** 0.500 — AI adds ['10.15']

## Proposition 10.17
**Statement:** If there be two unequal straight lines, and to the greater there be applied a parallelogram equal to the fourth part of the square on the less and deficient by a square figure, and if it divide it into parts which are commensurable in length, then the square on the greater will be greater than the square on the less by the square on a straight line commensurable with the greater. And, if the square on the greater be greater than the square on the less by the square on a straight line commensurable with  the greater, and if there be applied to the greater a parallelogram equal to the fourth part of the square on the less and deficient by a square figure, it will divide it into parts which are commensurable in length.

**Step 1.** Let the greater straight line have length a and the less length b, and let the given application divide a into positive parts x and y. Write S(t) for the square on t and R(s,t) for the rectangle contained by s and t. Since the deficient figure is a square, the applied parallelogram is rectangular: its base is one of the parts and its height equals the other. Consequently,
 a = x + y, and 4R(x,y) = S(b).
[Hypothesis; D1.22, D2.1.]

**Step 2.** The parts x and y are unequal. For if x = y, then 2.4 gives S(a) = 4S(x) = 4R(x,y) = S(b). But a > b implies S(a) > S(b), since 2.4 expresses the square on the greater line as the square on the less together with further positive areas. This is a contradiction. Name the greater part x, and cut from it a length equal to y; let the positive remainder be d. Thus x = y + d. [2.4, CN5, 1.3.]

**Step 3.** Apply 2.8 to the line x, divided into y and d. It gives
 S(x + y) = 4R(x,y) + S(d).
Hence, using Step 1,
 S(a) = S(b) + S(d).
The path choice is direct: 2.8 supplies precisely the required excess square, namely the square on the difference of the two parts, without a midpoint construction. [2.8, CN1.]

**Step 4.** First suppose that x and y are commensurable in length. Since a = x + y, the whole a is commensurable with y. Since x = d + y and x is commensurable with y, the remainder d is also commensurable with y. Both assertions follow directly from the sum-and-remainder clauses of 10.15. Therefore a and d are commensurable with one another by 10.12. Together with Step 3, this proves that the square on the greater line exceeds the square on the less by the square on a line commensurable in length with the greater. [10.15, 10.12.]

**Step 5.** Conversely, suppose that
 S(a) = S(b) + S(c),
where c is commensurable in length with a. Comparing this equality with Step 3 and subtracting S(b), we obtain S(c) = S(d). Hence c = d: unequal positive lines have unequal squares, as follows from 2.4 and CN5. Thus a and d are commensurable in length. [Hypothesis; CN1, CN3, 2.4, CN5.]

**Step 6.** From a = x + y and x = d + y, we have a = d + 2y. Since this whole is commensurable with its part d, the converse clause of 10.15 shows that d and 2y are commensurable. Also, 2y and y are commensurable, since y measures both. Therefore d and y are commensurable by 10.12. [10.15, D10.1.1, 10.12.]

**Step 7.** Finally, x = d + y. Since d and y are commensurable, their whole x is commensurable with y by 10.15. Thus the applied parallelogram divides the greater line into parts commensurable in length. This proves the converse and completes both directions. [10.15.]

**USED:** 1.3, 10.12, 10.15, 2.4, 2.8, CN1, CN3, CN5, D1.22, D10.1.1, D2.1
**Human refs (from References field):** 10.12, 10.15, 10.6, 2.5
**Jaccard:** 0.154 — AI adds ['1.3', '2.4', '2.8', 'CN1', 'CN3', 'CN5', 'D1.22', 'D10.1.1', 'D2.1']; Human adds ['10.6', '2.5']

## Proposition 10.18
**Statement:** If there be two unequal straight lines, and to the greater there be applied a parallelogram equal to the fourth part of the square on the less and deficient by a square figure, and if it divide it into parts which are incommensurable, the square on the greater will be greater than the square on the less by the square on a straight line incommensurable with the greater. And, if the square on the greater be greater than the square on the less by the square on a straight line incommensurable with the greater, and if there be applied to the greater a parallelogram equal to the fourth part of the square on the less and deficient by a square figure, it divides it into parts which are incommensurable. Let A, BC be two unequal straight lines, of which BC is the greater, and to BC let there be applied a parallelogram equal to the fourth part of the square on the less, A, and deficient by a square figure.

**Step 1.** Let D be the point at which the given parallelogram, applied to BC and deficient by a square, divides BC. Its area is one fourth of the square on A, and BC is greater than A. Write sq(X) for the square on a straight line X. **Path choice:** use the two implications of 10.17 by contradiction, since that proposition concerns exactly the same application of area and the complementary case of commensurable parts. [10.17]

**Step 2.** We first establish the comparison needed below. If one straight line is greater than another, cut off from the greater a segment equal to the less. The square on the greater equals the square on the less, together with the square on the remaining segment and twice the rectangle contained by the less and that remaining segment. It is therefore greater than the square on the less. Consequently, equal squares have equal sides: otherwise the square on the greater side would be greater. [1.3, 2.4, CN5]

**Step 3.** Since BC is greater than A, the decomposition in Step 2 leaves a positive rectilineal remainder after the square on A is removed from the square on BC. Construct a square equal to this remainder, and call its side H. Thus
sq(BC) = sq(A) + sq(H).
The excess is therefore the square on an actual straight line H. [Step 2; 2.14, CN2]

**Step 4.** First suppose that BD and DC are incommensurable. If H were commensurable with BC, the identity in Step 3 and the converse implication of 10.17 would imply that the given parallelogram divides BC into commensurable parts. This contradicts the assumption about BD and DC. Hence H is incommensurable with BC. Together with Step 3, this proves the first assertion. [10.17, D10.1.1]

**Step 5.** Conversely, suppose that
sq(BC) = sq(A) + sq(K),
where K is incommensurable with BC. If BD and DC were commensurable, the forward implication of 10.17 would give a straight line L commensurable with BC such that
sq(BC) = sq(A) + sq(L).
Equating these expressions and subtracting sq(A), we obtain sq(K) = sq(L). Hence K = L by Step 2. Any common measure of L and BC would therefore also measure K and BC, contradicting the stipulated incommensurability of K and BC. Thus BD and DC are incommensurable, proving the converse and completing both assertions. [10.17, CN1, CN3, Step 2, D10.1.1]

**USED:** 1.3, 10.17, 2.14, 2.4, CN1, CN2, CN3, CN5, D10.1.1
**Human refs (from References field):** 10.13, 10.16, 10.17, 10.6
**Jaccard:** 0.083 — AI adds ['1.3', '2.14', '2.4', 'CN1', 'CN2', 'CN3', 'CN5', 'D10.1.1']; Human adds ['10.13', '10.16', '10.6']

## Proposition 10.19
**Statement:** The rectangle contained by rational straight lines commensurable in length is rational.

**Step 1.** Let a and b be rational straight lines commensurable in length, and let R be the rectangle contained by them. Let u be the assigned rational straight line, and denote the squares on a and u by S_a and S_u respectively. [D2.1, D10.1.3]

**Step 2.** Since a is rational, it is commensurable in square with u. Therefore S_a and S_u are commensurable areas. [D10.1.3, D10.1.2]

**Step 3.** Compare R with S_a. These are parallelograms with the same height a and respective bases b and a; hence b : a = R : S_a. This equal-height comparison is the direct path because it brings the given ratio of lengths into a proportion with the required areas. [6.1]

**Step 4.** Since b and a are commensurable in length, the proportion in Step 3 implies that R and S_a are commensurable. We apply the commensurability-transfer proposition directly, rather than introducing numerical ratios. [10.11]

**Step 5.** Both R and S_u are commensurable with S_a, so R and S_u are commensurable with one another. [10.12] An area commensurable with the square on the assigned rational straight line is rational. Thus R is rational: the rectangle contained by rational straight lines commensurable in length is rational. [D10.1.4]

**USED:** 10.11, 10.12, 6.1, D10.1.2, D10.1.3, D10.1.4, D2.1
**Human refs (from References field):** 10.11, 6.1, D10.1.4
**Jaccard:** 0.429 — AI adds ['10.12', 'D10.1.2', 'D10.1.3', 'D2.1']

## Proposition 10.20
**Statement:** If a rational area be applied to a rational straight line, it produces as breadth a straight line rational and commensurable in length with the straight line to which it is applied.

**Step 1.** Let the rational area be applied as a rectangle R contained by the given rational straight line a and its breadth b (D2.1). Let u be the assigned rational straight line relative to which rationality is understood (D10.1.3). Construct the squares S, Q, and T on u, a, and b respectively (1.46).

**Step 2.** Since a is rational, it is commensurable in square with u; hence Q is commensurable with S (D10.1.3, D10.1.2). Since R is a rational area, R is also commensurable with S (D10.1.4). Therefore Q and R are commensurable with one another (10.12).

**Step 3.** Regard Q and R as parallelograms having the same height a and bases a and b respectively. Then Q : R = a : b (6.1). Since Q and R are commensurable, a and b are commensurable in length (10.11). This is the direct path: 10.11 transfers commensurability along the proportion immediately, without introducing ratios of numbers.

**Step 4.** Now regard R and T as parallelograms having the same height b and bases a and b respectively. Thus R : T = a : b (6.1). Since a and b are commensurable in length, this proportion implies that R and T are commensurable (10.11).

**Step 5.** Both T and S are commensurable with R, so T and S are commensurable with one another (10.12). Consequently b and u are commensurable in square (D10.1.2), and b is therefore rational (D10.1.3). Together with Step 3, this proves that the breadth is rational and commensurable in length with the straight line to which the area is applied.

**USED:** 1.46, 10.11, 10.12, 6.1, D10.1.2, D10.1.3, D10.1.4, D2.1
**Human refs (from References field):** 10.11, 6.1, D10.1.4
**Jaccard:** 0.375 — AI adds ['1.46', '10.12', 'D10.1.2', 'D10.1.3', 'D2.1']

## Proposition 10.21
**Statement:** The rectangle contained by rational straight lines commensurable in square only is irrational, and the side of the square equal to it is irrational. Let the latter be called medial.

**Step 1.** Let a and b be rational straight lines commensurable in square only; thus their squares are commensurable, but a and b are incommensurable in length [D10.1.1, D10.1.2]. Let R be the rectangle contained by a and b. This rectangle is already applied to a with breadth b [D2.1].

**Step 2.** Use 10.20 directly, since R is already applied to a rational straight line; no auxiliary ratio construction is needed. Suppose R were rational. Then its breadth b would be commensurable in length with a [10.20], contradicting Step 1. Therefore R is not rational.

**Step 3.** By D10.1.4, rational areas are precisely those commensurable with the square on the assigned rational straight line. Since R is not rational, it is incommensurable with that square and is therefore irrational [D10.1.4].

**Step 4.** Construct a square equal to R, and let m be its side [2.14]. The straight line on which a square equal to an irrational rectilineal area is described is itself irrational [D10.1.4]. Hence m is irrational. Let this straight line be called medial. Thus both the given rectangle and the side of the square equal to it are irrational, as required.

**USED:** 10.20, 2.14, D10.1.1, D10.1.2, D10.1.4, D2.1
**Human refs (from References field):** 10.11, 6.1, D10.1.4
**Jaccard:** 0.125 — AI adds ['10.20', '2.14', 'D10.1.1', 'D10.1.2', 'D2.1']; Human adds ['10.11', '6.1']

## Proposition 10.22
**Statement:** The square on a medial straight line, if applied to a rational straight line, produces as breadth a straight line rational and incommensurable in length with that to which it is applied.

**Step 1.** Let m be a medial straight line, and let its square be applied to a rational straight line a, producing breadth b. Write S(x) for the square on x and R(x,y) for the rectangle contained by x and y. Thus R(a,b) = S(m). By the meaning of medial in 10.21, there are rational straight lines u and v, commensurable in square only, such that S(m) = R(u,v); moreover, this area is irrational. Hence R(a,b) = R(u,v). [10.21, CN1]

**Step 2.** Equality of these rectangles gives a:u = v:b. Therefore S(a):S(u) = S(v):S(b). We use the theorem on proportional similar figures directly, applied to squares, because the required rationality is determined by commensurability in square; no passage through numerical ratios is needed. [6.16, 6.22]

**Step 3.** Let r be the assigned rational straight line. Since a and u are rational, S(a) and S(u) are each commensurable with S(r). Consequently S(a) and S(u) are commensurable with one another. [D10.1.2, D10.1.3, 10.12]

**Step 4.** From the proportion in Step 2 and the commensurability established in Step 3, S(v) and S(b) are commensurable. Since v is rational, S(v) is also commensurable with S(r). Thus S(b) and S(r) are commensurable, so b is rational. [10.11, D10.1.2, D10.1.3, 10.12]

**Step 5.** Suppose that b were commensurable in length with a. Since both are rational, their rectangle R(a,b) would then be rational. But this rectangle equals the irrational area S(m), as established in Step 1. This is impossible, since a rational area is commensurable with S(r), whereas an irrational area is incommensurable with it. Therefore b is incommensurable in length with a. Together with Step 4, this proves that the breadth is rational and incommensurable in length with the rational straight line to which the square was applied. [10.19, 10.21, D10.1.4]

**USED:** 10.11, 10.12, 10.19, 10.21, 6.16, 6.22, CN1, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 10.11, 10.13, 10.21, 6.14, 6.22, D10.1.4
**Jaccard:** 0.333 — AI adds ['10.12', '10.19', '6.16', 'CN1', 'D10.1.2', 'D10.1.3']; Human adds ['10.13', '6.14']

## Proposition 10.23
**Statement:** A straight line commensurable with a medial straight line is medial.

**Step 1.** Let a be a medial straight line and b a straight line commensurable with a. Write S_x for the square on a straight line x. The areas S_a and S_b are commensurable: if the given commensurability is in length, 10.9 makes their ratio that of two square numbers, so 10.6 applies; if it is in square, this is exactly D10.1.2.

**Step 2.** Choose the assigned rational straight line r (D10.1.3). Construct third proportionals u and v such that r:a = a:u and r:b = b:v (6.11). Then the rectangles contained by r,u and by r,v equal S_a and S_b respectively (6.17). Our chosen route is to use 10.22, since a is already known to be medial, and compare these rectangles on the same rational base.

**Step 3.** The rectangle contained by r,u is the square on the medial line a applied to the rational line r. Consequently its breadth u is rational and incommensurable in length with r (10.22).

**Step 4.** Rectangles of the same height r are to one another as their bases u and v. Hence S_a:S_b = u:v (6.1). Since S_a and S_b are commensurable by Step 1, u and v are commensurable in length (10.11).

**Step 5.** Because u and v are commensurable in length, S_u:S_v is the ratio of two square numbers (10.9), and therefore S_u and S_v are commensurable (10.6). Since u is rational, S_u is also commensurable with S_r (D10.1.3, D10.1.2). Thus S_v and S_r are commensurable, being commensurable with the same area S_u (10.12). Accordingly v is rational and commensurable in square with r (D10.1.3, D10.1.2).

**Step 6.** The lines u and v are commensurable in length, whereas u and r are incommensurable in length. Therefore v and r are incommensurable in length (10.13). Together with Step 5, this says that the rational lines r and v are commensurable in square only (D10.1.2).

**Step 7.** The side of a square equal to the rectangle contained by rational straight lines commensurable in square only is medial (10.21). The rectangle contained by r,v equals S_b by Step 2. Hence b is medial. Therefore a straight line commensurable with a medial straight line is medial.

**USED:** 10.11, 10.12, 10.13, 10.21, 10.22, 10.6, 10.9, 6.1, 6.11, 6.17, D10.1.2, D10.1.3
**Human refs (from References field):** 10.11, 10.13, 10.21, 10.22, 6.1, D10.1.3
**Jaccard:** 0.500 — AI adds ['10.12', '10.6', '10.9', '6.11', '6.17', 'D10.1.2']

## Proposition 10.24
**Statement:** The rectangle contained by medial straight lines commensurable in length is medial.

**Step 1.** Let a and b be medial straight lines commensurable in length, and let R be the rectangle contained by them [hypothesis; D2.1]. Let r be the assigned rational straight line [D10.1.3]. Path choice: express R as a rectangle contained by rational straight lines commensurable in square only, so that the characterization in 10.21 applies.

**Step 2.** Construct a fourth proportional c such that r:a = a:c [6.12]. Then the rectangle contained by r and c equals the square on a [6.16]. Since a is medial and r is rational, c is rational and incommensurable in length with r [10.22].

**Step 3.** Construct a fourth proportional d such that a:b = c:d [6.12]. Since a and b are commensurable in length, c and d are commensurable in length [10.11]. We use 10.11 directly because the required proportion is already available.

**Step 4.** From r:a = a:c and a:b = c:d, it follows ex aequali that r:b = a:d [5.22]. Consequently, the rectangle contained by r and d equals the rectangle contained by a and b, namely R [6.16].

**Step 5.** Since c and d are commensurable in length, their squares have the ratio of a square number to a square number [10.9], and therefore their squares are commensurable [10.6]. Since c is rational, its square is also commensurable with the square on the assigned rational line r [D10.1.3; D10.1.2]. Thus the squares on d and r, being commensurable with the square on c, are commensurable with one another [10.12]. Hence d is rational and commensurable in square with r [D10.1.2; D10.1.3].

**Step 6.** But c and d are commensurable in length, while c is incommensurable in length with r. Therefore d is also incommensurable in length with r [10.13]. Together with Step 5, this shows that r and d are rational straight lines commensurable in square only.

**Step 7.** The rectangle contained by r and d therefore has a medial straight line as the side of its equal square [10.21]. This rectangle equals R by Step 4. Thus R is a medial area: the rectangle contained by the medial straight lines a and b commensurable in length is medial.

**USED:** 10.11, 10.12, 10.13, 10.21, 10.22, 10.6, 10.9, 5.22, 6.12, 6.16, D10.1.2, D10.1.3, D2.1
**Human refs (from References field):** 10.11, 10.23, 6.1
**Jaccard:** 0.067 — AI adds ['10.12', '10.13', '10.21', '10.22', '10.6', '10.9', '5.22', '6.12', '6.16', 'D10.1.2', 'D10.1.3', 'D2.1']; Human adds ['10.23', '6.1']

## Proposition 10.25
**Statement:** The rectangle contained by medial straight lines commensurable in square only is either rational or medial.

**Step 1.** Let a and b be medial straight lines commensurable in square only, and let r be the assigned rational straight line. Write Q(x) for the square on x and R(x,y) for the rectangle contained by x and y. By hypothesis, Q(a) and Q(b) are commensurable [D10.1.2]; r is rational [D10.1.3].

**Step 2.** Construct fourth proportionals c and d such that
r:a = a:c and r:a = b:d [6.12].
Consequently,
R(r,c) = Q(a) and R(r,d) = R(a,b) [6.16].

**Step 3.** The first equality exhibits the square on the medial straight line a as applied to the rational straight line r, with breadth c. The direct result for precisely this situation is 10.22; hence c is rational [10.22].

**Step 4.** The proportions in Step 2 give a:c = b:d [5.11], and therefore, by alternation, a:b = c:d [5.16]. Applying the theorem on similar figures described on proportional straight lines to their squares gives
Q(a):Q(b) = Q(c):Q(d) [6.22].

**Step 5.** Since Q(a) and Q(b) are commensurable, the proportion just obtained directly implies that Q(c) and Q(d) are commensurable [10.11]. Since c is rational, Q(c) is also commensurable with Q(r) [D10.1.3, D10.1.2]. Thus Q(d) and Q(r), being commensurable with the same area Q(c), are commensurable with one another [10.12]. Therefore d is rational [D10.1.3].

**Step 6.** Split according to whether r and d are commensurable in length [D10.1.1]. If they are, then R(r,d), being contained by rational straight lines commensurable in length, is rational [10.19]. By Step 2, R(a,b) is therefore rational.

**Step 7.** Otherwise, r and d are incommensurable in length but commensurable in square by Step 5 [D10.1.2]. They are consequently rational straight lines commensurable in square only. The side of a square equal to R(r,d) is then medial [10.21]; that is, R(r,d) is a medial area. By Step 2, R(a,b) is therefore medial. Hence the rectangle contained by the given medial straight lines commensurable in square only is either rational or medial.

**USED:** 10.11, 10.12, 10.19, 10.21, 10.22, 5.11, 5.16, 6.12, 6.16, 6.22, D10.1.1, D10.1.2, D10.1.3
**Human refs (from References field):** 10.11, 10.19, 10.21, 10.22, 5.11, 6.1, 6.17
**Jaccard:** 0.333 — AI adds ['10.12', '5.16', '6.12', '6.16', '6.22', 'D10.1.1', 'D10.1.2', 'D10.1.3']; Human adds ['6.1', '6.17']

## Proposition 10.26
**Statement:** A medial area does not exceed a medial area by a rational area.

**Step 1.** Suppose, for a contradiction, that two medial areas M = s² and N = t², with s and t medial straight lines, satisfy M = N + R, where R is a rational area. Let r be the assigned rational straight line. Construct third proportionals x and y so that r:s = s:x and r:t = t:y (6.11). Then the rectangles contained by r, x and by r, y equal M and N respectively (6.17). We choose this common-rational-base route because it allows 10.22 to apply directly to both medial areas.

**Step 2.** Since each medial area has been applied to the rational straight line r, both x and y are rational straight lines, and each is incommensurable in length with r (10.22).

**Step 3.** Since M > N, their breadths satisfy x > y, by rectangular dissection and the fact that the whole exceeds its part (2.1, CN5). Write x = y + d. The rectangle contained by r and x is the sum of the rectangles contained by r, y and by r, d (2.1). Subtracting the rectangle equal to N therefore shows that the rectangle contained by r and d equals R (CN3). Since R and r are rational, d is rational and commensurable in length with r (10.20).

**Step 4.** Let Q be the square on r. Since x, y, and d are rational straight lines, their squares are each commensurable with Q (D10.1.3, D10.1.2). Consequently these squares are also commensurable with one another (10.12).

**Step 5.** Put S = y² + d², and let K be the rectangle contained by y and d. Since y² and d² are commensurable, S is commensurable with y² (10.15), and hence with Q and x² (10.12). But x = y + d, so the square identity gives x² = S + 2K (2.4). Since this whole x² is commensurable with its part S, its two parts S and 2K are commensurable (10.15). Thus 2K is commensurable with Q (10.12).

**Step 6.** The area K is commensurable with 2K, since K measures both (D10.1.1). Therefore K is commensurable with Q (10.12), and is consequently a rational area (D10.1.4).

**Step 7.** Apply this rational rectangle K to its rational side d. Its breadth y must be commensurable in length with d (10.20). Since d is commensurable in length with r, y is likewise commensurable in length with r (10.12). This contradicts Step 2, which established its incommensurability with r (10.22). Therefore a medial area does not exceed a medial area by a rational area.

**USED:** 10.12, 10.15, 10.20, 10.22, 2.1, 2.4, 6.11, 6.17, CN3, CN5, D10.1.1, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 10.11, 10.13, 10.16, 10.20, 10.22, 10.6, 2.4, D10.1.4
**Jaccard:** 0.222 — AI adds ['10.12', '10.15', '2.1', '6.11', '6.17', 'CN3', 'CN5', 'D10.1.1', 'D10.1.2', 'D10.1.3']; Human adds ['10.11', '10.13', '10.16', '10.6']

## Proposition 10.27
**Statement:** To find medial straight lines commensurable in square only which contain a rational rectangle.

**Step 1.** Let a be the assigned rational straight line. By 10.10, construct b commensurable in square only with a. Then b is rational (D10.1.3). Throughout, write u² for the square on u and uv for the rectangle contained by u and v.

**Step 2.** Construct the third proportional c to a and b, so that a:b = b:c (6.11). Consequently ac = b² (6.17). Since b² is commensurable with a², it is a rational area (D10.1.4). Thus the rational area b², applied to the rational straight line a, has breadth c; therefore c is rational and commensurable in length with a (10.20).

**Step 3.** Since c is commensurable in length with a, while a is incommensurable in length with b, c is incommensurable in length with b (10.13). Moreover, since b and c are rational, their squares are each commensurable with a² (D10.1.3), and hence are commensurable with one another (10.12). Therefore b and c are commensurable in square only (D10.1.2).

**Step 4.** Construct a mean proportional x between a and b, and a mean proportional y between b and c (6.13). Then x² = ab and y² = bc (6.17). Each of the pairs a,b and b,c consists of rational straight lines commensurable in square only; hence x and y are medial (10.21). This mean-proportional construction is the direct path: it supplies exactly the rectangle equalities to which 10.21 applies.

**Step 5.** Rectangles of equal height are proportional to their bases (6.1). Using the equalities in Steps 2 and 4, and joining equal ratios by 5.11, we obtain
x²:y² = ab:bc = a:c = a²:ac = a²:b².
Since a² and b² are commensurable, x² and y² are commensurable (10.11). Furthermore, the converse of 6.22, applied to these proportional squares, gives x:y = a:b. Since a and b are incommensurable in length, x and y are also incommensurable in length (10.11). Thus x and y are commensurable in square only (D10.1.2).

**Step 6.** Again by 6.1 and 5.11, using a:b = b:c, we have
x²:b² = ab:b² = a:b = b:c = b²:bc = b²:y².
The converse of 6.22 therefore gives x:b = b:y. Hence xy = b² (6.17), which is a rational area (D10.1.4). Thus the constructed straight lines x and y are medial, are commensurable in square only, and contain a rational rectangle, as required.

**USED:** 10.10, 10.11, 10.12, 10.13, 10.20, 10.21, 5.11, 6.1, 6.11, 6.13, 6.17, 6.22, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 10.11, 10.21, 10.23, 5.16, 6.12, 6.13, 6.17
**Jaccard:** 0.222 — AI adds ['10.10', '10.12', '10.13', '10.20', '5.11', '6.1', '6.11', '6.22', 'D10.1.2', 'D10.1.3', 'D10.1.4']; Human adds ['10.23', '5.16', '6.12']

## Proposition 10.28
**Statement:** To find medial straight lines commensurable in square only which contain a medial rectangle.

**Step 1.** For the numerical choices below, observe that none of the ratios 2:1, 3:1, and 3:2 is a ratio of square numbers. Indeed, if a square number is an integral multiple of another square number, its side is an integral multiple of the other side; consequently that multiplier must itself be a square [8.14, D7.18]. This excludes the multipliers 2, 3, and 6. Moreover, if m²:n² = 3:2, then (2m)²:n² = 6:1, which is likewise impossible.

**Step 2.** Let u be the assigned rational straight line. By extending it and successively marking off equal lengths, construct s = 2u and t = 3u [P2, P3]. Construct v as a mean proportional between u and s, and w as a mean proportional between u and t [6.13]. Writing a² for the square on a and ab for the rectangle contained by a and b, we have
v² = us = 2u²,   w² = ut = 3u²,
by the property of a mean proportional and the ratios of rectangles with equal heights [6.17, 6.1]. Also t² = 9u² [6.1]. Thus u, t, v, and w are rational straight lines, since their squares are commensurable with u² [D10.1.2, D10.1.3].

**Step 3.** The pairs u, v and v, w are commensurable in square, since their squares have u² as a common measure [D10.1.2]. But v²:u² = 2:1 and w²:v² = 3:2; hence Step 1 and 10.9 show that both pairs are incommensurable in length. Furthermore, t is commensurable in length with u, which measures it three times [D10.1.1]. Since u is incommensurable in length with v, so is t [10.13]. The squares t² and v² also have u² as a common measure. Therefore t and v, too, are commensurable in square only [D10.1.2].

**Step 4.** Construct x as a mean proportional between u and v, and y as a mean proportional between t and v [6.13]. Then
x² = uv,   y² = tv [6.17].
Both rectangles are contained by rational straight lines commensurable in square only, as established in Step 3. Their equal-square sides x and y are therefore medial [10.21]. This common-side construction is chosen because it makes the ratio of the new squares immediately accessible.

**Step 5.** The rectangles tv and uv have the same height, so
y²:x² = tv:uv = t:u = 3:1 [6.1].
Thus x² measures y² three times, and x and y are commensurable in square [D10.1.2]. Since 3:1 is not a ratio of square numbers, they are incommensurable in length [Step 1; 10.9]. Hence x and y are commensurable in square only.

**Step 6.** We also have w²:u² = 3:1. Therefore
y²:x² = w²:u² [5.11].
Applying the converse of the theorem on proportional similar rectilineal figures to these four squares gives
y:x = w:u [6.22].

**Step 7.** Let R be the rectangle contained by x and y, and T the rectangle contained by v and w. Comparing rectangles with equal heights gives
R:x² = y:x,   T:uv = w:u [6.1].
Since x² = uv and y:x = w:u, these yield R:x² = T:x² [5.11]. Consequently R = T [5.9]. But v and w are rational and commensurable in square only; therefore the square equal to T has a medial side [10.21]. Thus T, and hence R, is a medial area. This identifies the rectangle directly, without a rational-or-medial case distinction. We have therefore found medial straight lines x and y, commensurable in square only, which contain a medial rectangle, as required.

**USED:** 10.13, 10.21, 10.9, 5.11, 5.9, 6.1, 6.13, 6.17, 6.22, 8.14, D10.1.1, D10.1.2, D10.1.3, D7.18, P2, P3
**Human refs (from References field):** 10.11, 10.21, 10.23, 5.16, 6.12, 6.13, 6.16, 6.17
**Jaccard:** 0.143 — AI adds ['10.13', '10.9', '5.11', '5.9', '6.1', '6.22', '8.14', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D7.18', 'P2', 'P3']; Human adds ['10.11', '10.23', '5.16', '6.12', '6.16']

## Proposition 10.29
**Statement:** To find two rational straight lines commensurable in square only and such that the square on the greater is greater than the square on the less by the square on a straight line commensurable in length with the greater.

**Step 1.** Write S(x) for the square on a straight line x, and R(x,y) for the rectangle contained by x and y. We use the numerical pattern 4 = 3 + 1 so that the required excess square will be exhibited directly. Let AB be the assigned rational straight line. Bisect AB at C, and bisect CB at D [1.10]. Put a = AB, c = AC, t = DB, and d = AD. Then c = 2t, d = 3t, and a = 4t = 2c [CN2]. Thus c is commensurable in length with a, since c measures a twice [D10.1.1].

**Step 2.** Construct a mean proportional b between a and d, so that a:b = b:d [6.13]. Consequently,
S(b) = R(a,d) [6.17].

**Step 3.** Since a:c = c:t = 2:1, we also have R(a,t) = S(c) [6.17]. Rectangles of the same height are proportional to their bases [6.1]. Therefore, because d = 3t and a = 4t,
S(b) = R(a,d) = 3R(a,t) = 3S(c),
and
S(a) = R(a,a) = 4R(a,t) = 4S(c).

**Step 4.** The displayed common measure S(c) measures S(a) four times and S(b) three times. Thus a and b are commensurable in square [D10.1.2], and S(a):S(b) = 4:3 [D5.5]. Here the explicit common measure allows us to use the definition directly. Since a is the assigned rational straight line and b is commensurable in square with it, both a and b are rational [D10.1.3].

**Step 5.** Four is a square number, whereas three is not: 2 multiplied by 2 makes 4, and any number, being a multitude of units, has at least two units and therefore has square at least 4 [D7.2, D7.15, D7.18]. If 4:3 were the ratio of a square number to a square number, then, because its antecedent 4 is square, its consequent 3 would also be square [8.24], a contradiction. Hence S(a):S(b) is not the ratio of a square number to a square number. The direct square-ratio criterion now shows that a and b are incommensurable in length [10.9]. Together with Step 4, this proves that they are commensurable in square only.

**Step 6.** Since S(a) = 4S(c) and S(b) = 3S(c), the former square is greater than the latter [CN5]; hence a is greater than b, since squares have the duplicate ratio of their sides [6.20]. Subtracting gives
S(a) − S(b) = S(c) [CN3].
By Step 1, c is commensurable in length with the greater line a. Thus a and b are the required two rational straight lines, commensurable in square only, whose squares differ by the square on a straight line commensurable in length with the greater.

**USED:** 1.10, 10.9, 6.1, 6.13, 6.17, 6.20, 8.24, CN2, CN3, CN5, D10.1.1, D10.1.2, D10.1.3, D5.5, D7.15, D7.18, D7.2
**Human refs (from References field):** 1.47, 10.6, 10.9, 3.31, 5.19, D10.1.4
**Jaccard:** 0.045 — AI adds ['1.10', '6.1', '6.13', '6.17', '6.20', '8.24', 'CN2', 'CN3', 'CN5', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D5.5', 'D7.15', 'D7.18', 'D7.2']; Human adds ['1.47', '10.6', '3.31', '5.19', 'D10.1.4']

## Proposition 10.30
**Statement:** To find two rational straight lines commensurable in square only and such that the square on the greater is greater is greater than the square on the less by the square on a straight line incommensurable in length with the greater.

**Step 1.** Let AB be the assigned rational straight line (D10.1.3). Construct the square ABCD on AB and join AC (1.46, P1). We choose this construction because the square on its diagonal will exceed the square on its side by that same side-square.

**Step 2.** Write r = AB and d = AC. Since ABCD is a square, BC = AB and angle ABC is right (D1.22). Therefore, by 1.47,

d² = r² + r².

The other angles of triangle ABC are less than a right angle (1.32), so the side AC opposite the right angle is greater than AB (1.19). Thus d > r.

**Step 3.** The area r² measures both r² and d², measuring the latter twice. Hence d and r are commensurable in square (D10.1.2). Since r is the assigned rational straight line, d is also rational (D10.1.3).

**Step 4.** No square number can be double another square number. Indeed, suppose m² = 2n². Then n² measures m², so n measures m (8.14). Since m > n, m must be at least twice n; consequently m² is at least four times n², by the definition of multiplication (D7.15), contradicting m² = 2n². Thus a double ratio cannot be the ratio of two square numbers (D7.20).

Now d² is double r² by Step 2. Therefore d² and r² do not have the ratio of a square number to a square number. Applying 10.9—the direct criterion naturally reached from this known square-ratio—we conclude that d and r are incommensurable in length. Together with Step 3, this shows that they are commensurable in square only.

**Step 5.** Subtracting r² from the equality in Step 2 gives

d² − r² = r² (CN3).

The straight line producing this excess square is r itself, which is incommensurable in length with the greater line d by Step 4. Hence AC and AB are the required two rational straight lines, commensurable in square only, whose square-difference is the square on a straight line incommensurable in length with the greater.

**USED:** 1.19, 1.32, 1.46, 1.47, 10.9, 8.14, CN3, D1.22, D10.1.2, D10.1.3, D7.15, D7.20, P1
**Human refs (from References field):** 1.47, 10.6, 10.9, 3.31, 5.19
**Jaccard:** 0.125 — AI adds ['1.19', '1.32', '1.46', '8.14', 'CN3', 'D1.22', 'D10.1.2', 'D10.1.3', 'D7.15', 'D7.20', 'P1']; Human adds ['10.6', '3.31', '5.19']

## Proposition 10.31
**Statement:** To find two medial straight lines commensurable in square only, containing a rational rectangle, and such that the square on the greater is greater than the square on the less by the square on a straight line commensurable in length with the greater.

**Step 1.** Write u² for the square on a straight line u, and uv for the rectangle contained by u and v. By 10.29, construct rational straight lines a > b, commensurable in square only, such that a² = b² + c², where c is commensurable in length with a. Our path is to preserve this pair’s ratio: 10.14 will then transfer the required square-difference property.

**Step 2.** Construct a third proportional d to a and b, so that a:b = b:d (6.11). Then ad = b² (6.17). Since b is rational, b² is a rational area (D10.1.3, D10.1.4). Thus the rectangle ad is a rational area applied to the rational straight line a; consequently d is rational and commensurable in length with a (10.20). Since a is incommensurable in length with b, so is d (10.13). Moreover, the squares on b and d are each commensurable with the assigned rational square, and therefore with one another (D10.1.3, D10.1.4, 10.12). Hence b and d are commensurable in square only (D10.1.2).

**Step 3.** Construct x as a mean proportional between a and b, and y as a mean proportional between b and d (6.13). Thus x² = ab and y² = bd (6.17). Both pairs a, b and b, d consist of rational straight lines commensurable in square only. Therefore x and y are medial straight lines (10.21).

**Step 4.** Rectangles with the same height are in the ratio of their bases (6.1). Using the equalities already established, we obtain
x²:y² = ab:bd = a:d = a²:ad = a²:b².
The equality of these ratios follows by 5.11. Since proportional squares have proportional sides, x:y = a:b (6.22).

**Step 5.** The squares a² and b² are commensurable. The proportion a²:b² = x²:y² therefore makes x² and y² commensurable (10.11). But a and b are incommensurable in length, so the proportion a:b = x:y makes x and y incommensurable in length (10.11). Thus x and y are commensurable in square only (D10.1.2).

**Step 6.** Again by the ratios of rectangles with equal heights, and by a:b = b:d,
x²:b² = ab:ad = b:d = a:b = ad:bd = b²:y²
(6.1, 5.11). Applying 6.22 to these proportional squares gives x:b = b:y. Consequently xy = b² (6.17). Since b² is rational, the rectangle contained by x and y is rational (D10.1.4).

**Step 7.** Finally, a:b = x:y, while a² exceeds b² by c², whose side c is commensurable in length with a. Therefore, by 10.14, x² exceeds y² by the square on a straight line z commensurable in length with x. Thus the greater straight line x and the less y are medial, commensurable in square only, contain a rational rectangle, and satisfy x² = y² + z² with z commensurable in length with x, as required.

**USED:** 10.11, 10.12, 10.13, 10.14, 10.20, 10.21, 10.29, 5.11, 6.1, 6.11, 6.13, 6.17, 6.22, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 10.11, 10.14, 10.21, 10.23, 10.29, 10.30
**Jaccard:** 0.222 — AI adds ['10.12', '10.13', '10.20', '5.11', '6.1', '6.11', '6.13', '6.17', '6.22', 'D10.1.2', 'D10.1.3', 'D10.1.4']; Human adds ['10.23', '10.30']

## Proposition 10.32
**Statement:** To find two medial straight lines commensurable in square only, containing a medial rectangle, and such that the square on the greater is greater than the square on the less by the square on a straight line commensurable with the greater.

**Step 1.** Fix the assigned rational straight line, relative to which all rationality is understood (D10.1.3). Write st for the rectangle contained by s,t, and s² for the square on s. By 10.29, construct rational straight lines a>b, commensurable in square only, such that a²=b²+h² for a straight line h commensurable in length with a. Our path is to preserve this ratio and transfer its square-excess property; an auxiliary construction will ensure that the resulting rectangle is medial.

**Step 2.** By 10.28, construct medial straight lines p,q, commensurable in square only, whose rectangle pq is medial. Construct their mean proportional w by 6.13. Then w²=pq by 6.17, so w is medial, being the square-side of that medial area.

**Step 3.** Construct third proportionals c,d satisfying a:p=p:c and a:w=w:d (6.11). Thus ac=p² and ad=w²=pq (6.17). These equalities apply the squares on the medial lines p,w to the rational line a. Consequently c and d are rational and each is incommensurable in length with a (10.22). Moreover, by 6.1,
 c:d=ac:ad=p²:pq=p:q.
Since p,q are incommensurable in length, so are c,d (10.11).

**Step 4.** At least one of c,d is incommensurable in length with b: otherwise both would be commensurable with b and hence with each other, contrary to Step 3 (10.12). Choose such a line and call it t. Thus t is rational and is incommensurable in length with both a and b.

**Step 5.** Construct the third proportional e to a,b, so that a:b=b:e (6.11). Then ae=b² (6.17). Since b is rational, b² is a rational area (D10.1.3, D10.1.4). Applied to the rational line a, this area therefore produces a rational breadth e commensurable in length with a (10.20). Since t is incommensurable in length with a, it is also incommensurable in length with e (10.13).

**Step 6.** The rational lines a,b,e,t are all commensurable in square with the assigned rational line, and therefore with one another (D10.1.3, D10.1.2, 10.12). Construct mean proportionals x between a,t and y between e,t (6.13). Then
 x²=at,     y²=et
by 6.17. The pairs a,t and e,t are rational and commensurable in square only, by Steps 4–5. Hence x and y are medial (10.21).

**Step 7.** By 6.1 and the equalities already established,
 x²:y²=at:et=a:e=a²:ae=a²:b².
Consequently x:y=a:b, and likewise y:x=b:a, by the converse of 6.22 applied to squares. Thus x>y (5.14). The squares x²,y² are commensurable because a²,b² are commensurable; the lines x,y are incommensurable in length because a,b are incommensurable in length (10.11). Therefore x,y are commensurable in square only (D10.1.2).

**Step 8.** Using 6.1 and Step 7,
 xy:x²=y:x=b:a=bt:at.
Since x²=at, the areas xy and bt have the same ratio to the same area and are therefore equal (5.9). But b,t are rational and commensurable in square only, by Steps 4 and 6. Hence bt, and therefore xy, is a medial rectangle (10.21).

**Step 9.** We have a:b=x:y, while a² exceeds b² by h² with h commensurable in length with a. Therefore 10.14 gives a straight line z commensurable in length with x such that x²=y²+z². Thus x and y are medial straight lines commensurable in square only, containing a medial rectangle, and the square on the greater exceeds the square on the less by the square on a straight line commensurable with the greater, as required.

**USED:** 10.11, 10.12, 10.13, 10.14, 10.20, 10.21, 10.22, 10.28, 10.29, 5.14, 5.9, 6.1, 6.11, 6.13, 6.17, 6.22, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 10.11, 10.14, 10.21, 10.23, 10.29, 10.30, 6.16, 6.17, 6.4, 6.8
**Jaccard:** 0.208 — AI adds ['10.12', '10.13', '10.20', '10.22', '10.28', '5.14', '5.9', '6.1', '6.11', '6.13', '6.22', 'D10.1.2', 'D10.1.3', 'D10.1.4']; Human adds ['10.23', '10.30', '6.16', '6.4', '6.8']

## Proposition 10.33
**Statement:** To find two straight lines incommensurable in square which make the sum of the squares on them rational but the rectangle contained by them medial.

**Step 1.** Fix the assigned rational straight line. By 10.30, construct two rational straight lines a > b, commensurable in square only, such that a² = b² + d², where d is incommensurable in length with a. Here s² denotes the square on s, and st denotes the rectangle contained by s and t. This starting construction supplies precisely the incommensurable excess-square side required by 10.18. [D10.1.3, 10.30]

**Step 2.** Bisect b, calling its half h; thus h² is the fourth part of b². [1.10, 6.20] Let AB be the straight line a. Apply to AB a rectangle equal to h² and deficient by a square, obtaining a point C between A and B such that AC·CB = h². This construction is possible because b < a, so h² is less than the square on half AB. [6.20, 6.28] Since a² exceeds b² by d², and d is incommensurable in length with a, the resulting segments AC and CB are incommensurable in length. [10.18]

**Step 3.** Bisect AB at O and describe the circle with centre O and radius OA. At C erect a perpendicular to AB, meeting one semicircle at D, and join AD and BD. [1.10, P3, 1.11, P1] The angle ADB is right. [3.31] The perpendicular DC is a mean proportional between AC and CB; hence DC² = AC·CB = h², and therefore DC = h. [6.8, 6.17, CN1, 6.20]

**Step 4.** The same right-triangle proportionalities give
AD² = AB·AC and BD² = AB·CB. [6.8, 6.17]
The rectangles on the right have the common height AB, so
AD² : BD² = AC : CB. [6.1]
Since AC and CB are incommensurable, 10.11 directly transfers their incommensurability to the square areas AD² and BD². Thus AD and BD are incommensurable in square. [10.11, D10.1.2]

**Step 5.** Since ADB is a right-angled triangle,
AD² + BD² = AB² = a². [1.47]
The line a is rational, so its square is a rational area. Consequently the sum of the squares on AD and BD is rational. [D10.1.3, D10.1.4]

**Step 6.** The relations b = 2h and b² = 4h² show that b and h are commensurable both in length and in square. [D10.1.1, D10.1.2] Since a² is commensurable with b², it is also commensurable with h²; moreover, h² is commensurable with the square on the assigned rational line. Thus h is rational. [10.12, D10.1.3] But a is incommensurable in length with b, and b is commensurable in length with h; therefore a is incommensurable in length with h. [10.13] Hence a and h are rational straight lines commensurable in square only. By 10.21, the side of a square equal to their rectangle ah is medial; that is, ah is a medial area. [10.21]

**Step 7.** The rectangle AD·BD is double the triangle ADB, using AD as base and BD as height. The rectangle AB·DC is likewise double that triangle, using AB as base and DC as height. [1.41] Therefore these rectangles are equal, and, since AB = a and DC = h,
AD·BD = AB·DC = ah. [CN1]
By Step 6 this rectangle is medial. Thus the constructed straight lines AD and BD are incommensurable in square, the sum of their squares is rational, and their contained rectangle is medial, as required.

**USED:** 1.10, 1.11, 1.41, 1.47, 10.11, 10.12, 10.13, 10.18, 10.21, 10.30, 3.31, 6.1, 6.17, 6.20, 6.28, 6.8, CN1, D10.1.1, D10.1.2, D10.1.3, D10.1.4, P1, P3
**Human refs (from References field):** 1.47, 10.18, 10.21, 10.23, 10.30, 6.28
**Jaccard:** 0.208 — AI adds ['1.10', '1.11', '1.41', '10.11', '10.12', '10.13', '3.31', '6.1', '6.17', '6.20', '6.8', 'CN1', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.1.4', 'P1', 'P3']; Human adds ['10.23']

## Proposition 10.34
**Statement:** To find two straight lines incommensurable in square which make the sum of the squares on them medial but the rectangle contained by them rational.

**Step 1.** Write u² for the square on a straight line u, and uv for the rectangle contained by u and v. By 10.30, construct rational straight lines a > b, commensurable in square only, such that a² − b² = c², where c is incommensurable in length with a. **Path choice:** this incommensurable-excess construction is chosen because it supplies the hypothesis for the incommensurable division in 10.18.

**Step 2.** Bisect b, calling its half h, and construct the square on h (1.10, 1.46). Apply this square to a, deficient by a square, using 6.28. Its size condition holds because h² is less than the square on half of a. Let p be the base of the applied rectangle and q the remaining part of a. Since the deficiency is a square, the rectangle has height q; hence
p + q = a and pq = h² = b²/4.

**Step 3.** Since a² − b² is the square on c, which is incommensurable in length with a, the division just constructed has p and q incommensurable in length (10.18). Also, pq = h² gives
p:h = h:q
by 6.17.

**Step 4.** Construct a mean proportional x between p and b (6.13), and construct a fourth proportional y such that x:b = h:y (6.12). Thus
p:x = x:b and x:b = h:y.
Consequently,
x² = bp and xy = bh
by 6.17 and 6.16, respectively.

**Step 5.** We show that y² = bq. The proportions in Step 4 give p:x = h:y (5.11), and therefore p:h = x:y by alternation (5.16). Together with Step 3, this gives x:y = h:q (5.11). Alternating yields x:h = y:q (5.16). But alternation of x:b = h:y also gives x:h = b:y (5.16). Hence b:y = y:q (5.11), so
 y² = bq
by 6.17.

**Step 6.** By 6.1, rectangles of the same height are proportional to their bases. Therefore
x²:y² = bp:bq = p:q.
Since p and q are incommensurable, x² and y² are incommensurable (10.11). Thus x and y are incommensurable in square (D10.1.2).

**Step 7.** By the distributive identity for rectangles (2.1),
x² + y² = bp + bq = b(p + q) = ba.
The lines a and b are rational and commensurable in square only. Consequently, the side of the square equal to ba is medial (10.21); that is, ba is a medial area. Thus the sum of the squares on x and y is medial.

**Step 8.** From Step 4, xy = bh. Since b consists of two copies of h, 2.1 gives b² = 2bh. Thus bh is commensurable with b² (D10.1.1). Because b is rational, b² is commensurable with the assigned rational square (D10.1.3, D10.1.4); hence bh is also commensurable with that square (10.12). Therefore xy is rational (D10.1.4). The constructed straight lines x and y are consequently incommensurable in square, their squares have a medial sum, and their contained rectangle is rational, as required.

**USED:** 1.10, 1.46, 10.11, 10.12, 10.18, 10.21, 10.30, 2.1, 5.11, 5.16, 6.1, 6.12, 6.13, 6.16, 6.17, 6.28, D10.1.1, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 1.47, 10.11, 10.18, 10.31, 10.6, 3.31, 6.28
**Jaccard:** 0.125 — AI adds ['1.10', '1.46', '10.12', '10.21', '10.30', '2.1', '5.11', '5.16', '6.1', '6.12', '6.13', '6.16', '6.17', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.1.4']; Human adds ['1.47', '10.31', '10.6', '3.31']

## Proposition 10.35
**Statement:** To find two straight lines incommensurable in square which make the sum of the squares on them medial and the rectangle contained by them medial and moreover incommensurable with the sum of the squares on them.

**Step 1.** Fix the assigned rational straight line r. Our construction will make the required areas rectangles with the common side r, so that their incommensurability can be tested directly through their other sides. Construct mean proportionals a between r and 2r, and b between r and 3r. Then
r : a = a : 2r,    r : b = b : 3r,
and consequently a² = 2r² and b² = 3r². Here uv denotes the rectangle contained by u and v, and u² the square on u. [6.13, 6.17, 2.1]

**Step 2.** The square on 2b equals 4b² = 12r². Thus a and 2b are rational, and each is commensurable in square with r. Their relevant square ratios are
a² : r² = 2 : 1,    (2b)² : r² = 12 : 1,    (2b)² : a² = 6 : 1.
None of these is a ratio of square numbers. Indeed, if m² = kn² for k equal to 2, 6, or 12, reduce m and n to coprime positive integers by 7.2. For k = 2 or 6, 7.30 first forces m to be even; substitution then forces n to be even. For k = 12, the same proposition first forces 3 to divide m; writing m = 3h gives 3h² = 4n², which forces 3 to divide n. Each case contradicts coprimality. Therefore r and a, r and 2b, and a and 2b are respectively incommensurable in length. We use 10.9 here because the square ratios are already known. [2.4, D10.1.2, D10.1.3, 7.2, 7.30, 10.9]

**Step 3.** Since b² = 3r², we have b > r. Put c = b + r and d = b − r, so d is positive. The difference-of-squares identity gives
cd + r² = b².
But b² = a² + r²; hence cd = a², and therefore c : a = a : d. [2.4, CN5, 2.5, CN3, 6.17]

**Step 4.** Construct x as a mean proportional between r and c, and construct y as the fourth proportional to c, a, x. Thus
r : x = x : c,    c : a = x : y.
These constructions determine the two straight lines to be exhibited. [6.13, 6.12]

**Step 5.** Alternating the second proportion gives x : c = y : a. Hence r : x = y : a, and consequently xy = ra. Also, by Step 3, x : y = a : d. Applying ex aequali to
r : x = y : a,    x : y = a : d
gives r : y = y : d. Therefore
x² = rc,    y² = rd,    xy = ra. [5.16, 5.11, 6.16, 5.22, 6.17]

**Step 6.** Write S = x² + y² and P = xy. Since c + d = 2b and c − d = 2r, the preceding equalities yield
S = r(c + d) = r(2b),    P = ra,
and
x² − y² = r(c − d) = 2r². [2.1, CN2, CN3]

**Step 7.** By Step 2, r and 2b are rational straight lines commensurable in square only; therefore their rectangle S is medial. Likewise, r and a are rational straight lines commensurable in square only, so their rectangle P is medial. In particular, S is irrational, hence incommensurable with the assigned rational square r². [10.21, D10.1.4]

**Step 8.** Rectangles with the common side r are proportional to their other sides. Thus
S : P = r(2b) : ra = 2b : a.
Since 2b and a are incommensurable in length by Step 2, S and P are incommensurable. The direct proportionality makes 10.11 the applicable transfer theorem. [6.1, 10.11]

**Step 9.** Finally, suppose that x² and y² were commensurable. Their sum S would then be commensurable with y². Moreover, since x² = y² + 2r², the converse part of 10.15 would make y² commensurable with 2r². Hence S would be commensurable with 2r², and therefore with r², since r² measures 2r². This contradicts Step 7. Thus x and y are incommensurable in square. Together with Steps 7 and 8, this proves that their squares have a medial sum and that their rectangle is medial and incommensurable with that sum, as required. [10.15, 10.12, D10.1.1, D10.1.2]

**USED:** 10.11, 10.12, 10.15, 10.21, 10.9, 2.1, 2.4, 2.5, 5.11, 5.16, 5.22, 6.1, 6.12, 6.13, 6.16, 6.17, 7.2, 7.30, CN2, CN3, CN5, D10.1.1, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 1.47, 10.11, 10.13, 10.18, 10.32, 3.31
**Jaccard:** 0.033 — AI adds ['10.12', '10.15', '10.21', '10.9', '2.1', '2.4', '2.5', '5.11', '5.16', '5.22', '6.1', '6.12', '6.13', '6.16', '6.17', '7.2', '7.30', 'CN2', 'CN3', 'CN5', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.1.4']; Human adds ['1.47', '10.13', '10.18', '10.32', '3.31']

## Proposition 10.36
**Statement:** If two rational straight lines commensurable in square only be added together, the whole is irrational; and let it be called binomial.

**Step 1.** Let a and b be the given rational straight lines, commensurable in square only, and let c be their sum. Denote the squares on a and b by X and Y, and the square on the assigned rational straight line by Q. Since a and b are rational, X and Y are each commensurable with Q; moreover, X and Y are commensurable with one another by the hypothesis. [D10.1.2, D10.1.3]

**Step 2.** Put S = X + Y. Since X and Y are commensurable, S is commensurable with X. Since X is also commensurable with Q, S is commensurable with Q. Thus S is a rational area. [10.15, 10.12, D10.1.4]

**Step 3.** Let T be the rectangle contained by a and b. Because these lines are rational and commensurable in square only, T is irrational, and therefore incommensurable with Q. The areas T and 2T are commensurable, since T measures both; hence 2T is also incommensurable with Q. [10.21, D10.1.4, D10.1.1, 10.13]

**Step 4.** Since S is commensurable with Q, while 2T is incommensurable with Q, S and 2T are incommensurable. Consequently, S + 2T is incommensurable with S. The direct path is to use the forward conclusion of 10.16 here, because the two summands have just been proved incommensurable. [10.13, 10.16]

**Step 5.** The square on the sum c equals the squares on a and b together with twice their rectangle; thus it equals S + 2T. It is therefore incommensurable with S. Since S and Q are commensurable, the square on c is also incommensurable with Q. [2.4, 10.13]

**Step 6.** Hence the square on c is irrational, and its side c is irrational. Therefore the sum of two rational straight lines commensurable in square only is irrational; let this sum be called a **binomial**. [D10.1.4]

**USED:** 10.12, 10.13, 10.15, 10.16, 10.21, 2.4, D10.1.1, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 10.11, 10.13, 10.15, 10.16, 10.6, 2.4, D10.1.4
**Jaccard:** 0.417 — AI adds ['10.12', '10.21', 'D10.1.1', 'D10.1.2', 'D10.1.3']; Human adds ['10.11', '10.6']

## Proposition 10.37
**Statement:** If two medial straight lines commensurable in square only and containing a rational rectangle be added together, the whole is irrational; and let it be called a first bimedial straight line.

**Step 1.** Let a and b be the given medial straight lines, commensurable in square only and containing a rational rectangle R. Let c = a + b. Denote the squares on a, b, and c by A, B, and W respectively, and denote the square on the assigned rational straight line by U. An area is rational precisely when it is commensurable with U (D10.1.4).

**Step 2.** Since a and b are commensurable in square, A and B are commensurable (D10.1.2). Since a is medial, its square A is irrational, and hence is incommensurable with U (10.21, D10.1.4).

**Step 3.** Put S = A + B. Since A and B are commensurable, S is commensurable with A (10.15). Since A is incommensurable with U, S is likewise incommensurable with U (10.13).

**Step 4.** Put T = R + R. The area R measures both R and T, so these areas are commensurable (D10.1.1). Moreover, R is commensurable with U because R is rational (D10.1.4). Therefore T is commensurable with U (10.12).

**Step 5.** Since T and U are commensurable, while U is incommensurable with S, T is incommensurable with S (10.13).

**Step 6.** The square on the sum of two straight lines equals the sum of their squares together with twice their contained rectangle. Thus W = A + B + T = S + T (2.4). We choose the forward addition criterion 10.16 because this decomposition gives W directly as a sum of incommensurable areas. It follows that W is incommensurable with T (10.16).

**Step 7.** Since T is commensurable with U and incommensurable with W, U is incommensurable with W (10.13). Consequently W is irrational, and its side c is irrational (D10.1.4). Therefore the sum of the given straight lines is irrational; let it be called a **first bimedial straight line**.

**USED:** 10.12, 10.13, 10.15, 10.16, 10.21, 2.4, D10.1.1, D10.1.2, D10.1.4
**Human refs (from References field):** 10.16, 10.36, 2.4, D10.1.4
**Jaccard:** 0.300 — AI adds ['10.12', '10.13', '10.15', '10.21', 'D10.1.1', 'D10.1.2']; Human adds ['10.36']

## Proposition 10.38
**Statement:** If two medial straight lines commensurable in square only and containing a medial rectangle be added together, the whole is irrational; and let it be called a second bimedial straight line.

**Step 1.** Let a and b be the given medial straight lines, and let c = a + b. Fix the assigned rational straight line r. Write A and B for the squares on a and b, and M for the rectangle contained by a and b. By hypothesis, A and B are commensurable, a and b are incommensurable in length, and M is medial. [D10.1.2; hypotheses]

**Step 2.** Construct fourth proportionals x, y, z such that r:a = a:x, r:b = b:y, and r:a = b:z. Then the rectangles rx, ry, rz equal A, B, M respectively. [6.12, 6.16] The first two areas are squares on medial straight lines. For M, construct an equal square; its side is medial because M is medial. [2.14; hypothesis] Consequently, applying these three areas to the rational straight line r produces rational breadths x, y, z. [10.22]

**Step 3.** Rectangles with the same height are proportional to their bases. Therefore x:y = A:B and x:z = A:M = a:b. [6.1] Since A and B are commensurable, x and y are commensurable in length. Since a and b are incommensurable in length, x and z are incommensurable in length. [10.11]

**Step 4.** Put p = x + y and q = z + z. Then p is commensurable in length with x, while q is commensurable in length with z. [10.15, D10.1.1] Their respective squares are consequently commensurable: the square on p with the square on x, and the square on q with the square on z. [10.9, 10.6] Since x and z are rational, their squares are commensurable with the square on r. Thus the squares on p and q are likewise commensurable with the square on r, so p and q are rational straight lines. [10.12, D10.1.3]

**Step 5.** Since x and z are incommensurable, and p is commensurable with x, p and z are incommensurable. Since q is commensurable with z, p and q are therefore incommensurable in length. [10.13, applied twice] But their squares are both commensurable with the square on r, and hence with one another. Thus p and q are commensurable in square only. [10.12, D10.1.2]

**Step 6.** The sum p + q is therefore irrational. [10.36] This is the direct reduction: the area applications have produced rational straight lines commensurable in square only, precisely the hypotheses of 10.36.

**Step 7.** The square on c is A + B + 2M. [2.4] Since A = rx, B = ry, and M = rz, this area equals the rectangle contained by r and x + y + 2z, that is, the rectangle contained by r and p + q. [2.1] If the square on c were rational, its application to the rational straight line r would produce a rational breadth. [10.20] That breadth is p + q, contradicting Step 6.

**Step 8.** Hence the square on c is irrational, and therefore its side c = a + b is irrational. [D10.1.4] Under the stated hypotheses, let this sum be called a second bimedial straight line.

**USED:** 10.11, 10.12, 10.13, 10.15, 10.20, 10.22, 10.36, 10.6, 10.9, 2.1, 2.14, 2.4, 6.1, 6.12, 6.16, D10.1.1, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 1.44, 10.11, 10.13, 10.15, 10.20, 10.22, 10.36, 10.6, 2.4, 6.1, D10.1.4
**Jaccard:** 0.500 — AI adds ['10.12', '10.9', '2.1', '2.14', '6.12', '6.16', 'D10.1.1', 'D10.1.2', 'D10.1.3']; Human adds ['1.44']

## Proposition 10.39
**Statement:** If two straight lines incommensurable in square which make the sum of the squares on them rational, but the rectangle contained by them medial, be added together, the whole straight line is irrational: and let it be called major.

**Step 1.** Let a and b be the given straight lines, incommensurable in square, and let c be their sum. Denote the sum of their squares by S and their contained rectangle by M. Let Q be the square on the assigned rational straight line. By hypothesis S is rational, so S is commensurable with Q [D10.1.4].

**Step 2.** By hypothesis M is medial, and therefore irrational [10.21]. Thus M is incommensurable with Q [D10.1.4]. Since Q and S are commensurable, M is also incommensurable with S [10.13].

**Step 3.** The areas M and 2M are commensurable, since M itself measures both [D10.1.1]. Consequently, since M is incommensurable with S, the area 2M is also incommensurable with S [10.13].

**Step 4.** The square on the whole straight line c equals the squares on a and b together with twice their contained rectangle; that is, c² = S + 2M [2.4]. The direct path is now the incommensurable-sum theorem: since S and 2M are incommensurable, their sum c² is incommensurable with S [10.16].

**Step 5.** Since S and Q are commensurable, while c² is incommensurable with S, c² is incommensurable with Q [10.13]. Hence the square on c is irrational, and its side c is irrational [D10.1.4]. Therefore the sum of the given straight lines is irrational; let it be called major.

**USED:** 10.13, 10.16, 10.21, 2.4, D10.1.1, D10.1.4
**Human refs (from References field):** 10.16, 10.23, 10.33, 10.6, D10.1.4
**Jaccard:** 0.222 — AI adds ['10.13', '10.21', '2.4', 'D10.1.1']; Human adds ['10.23', '10.33', '10.6']

## Proposition 10.40
**Statement:** If two straight lines incommensurable in square which make the sum of the squares on them medial, but the rectangle contained by them rational, be added together, the whole straight line is irrational; and let it be called the side of a rational plus a medial area.

**Step 1.** Let a and b be the given straight lines, incommensurable in square, and let c be their sum. Write M for the sum of the squares on a and b, R for the rectangle contained by them, and U for the square on the assigned rational straight line. By hypothesis, M is medial and R is rational. Thus R is commensurable with U, whereas M, being a medial area, is irrational and therefore incommensurable with U (10.21; D10.1.4).

**Step 2.** Take the direct route through the square on the whole. By 2.4, the square on c equals the squares on a and b together with twice their contained rectangle. Hence
c² = M + 2R.

**Step 3.** Since R measures both itself and 2R, these areas are commensurable (D10.1.1). Since U is also commensurable with R, it follows that 2R is commensurable with U (10.12). Consequently, 2R is a rational area (D10.1.4).

**Step 4.** The areas U and 2R are commensurable, while U is incommensurable with M. Therefore 2R is incommensurable with M (10.13). With the two summands now known to be incommensurable, 10.16 applies directly: their sum M + 2R, which is the square on c, is incommensurable with 2R.

**Step 5.** Since 2R and U are commensurable, and 2R is incommensurable with the square on c, U is likewise incommensurable with that square (10.13). Thus the square on c is irrational, and its side c is irrational (D10.1.4). Moreover, by Step 2 its square is the sum of the rational area 2R and the medial area M. Let c therefore be called the **side of a rational plus a medial area**, as required.

**USED:** 10.12, 10.13, 10.16, 10.21, 2.4, D10.1.1, D10.1.4
**Human refs (from References field):** 10.16, 10.34, D10.1.4
**Jaccard:** 0.250 — AI adds ['10.12', '10.13', '10.21', '2.4', 'D10.1.1']; Human adds ['10.34']

## Proposition 10.41
**Statement:** If two straight lines incommensurable in square which make the sum of the squares on them medial, and the rectangle contained by them medial and also incommensurable with the sum of the squares on them, be added together, the whole straight line is irrational; and let it be called the   side of the sum of two medial areas.

**Step 1.** Let the given straight lines be a and b, incommensurable in square, and let x be their sum. Write S for the sum of their squares and R for the rectangle contained by them. By hypothesis, S and R are medial areas and are incommensurable with one another. The square W on x satisfies W = S + 2R. [2.4]

**Step 2.** The area 2R is also medial. Indeed, since R is medial, it equals the square on a medial straight line m, using the terminology introduced in 10.21. The lines m and 2m are commensurable in length, since m measures both; hence 2m is medial. [D10.1.1, 10.23] Their rectangle is therefore medial, and it equals twice the square on m, namely 2R. [10.24, 2.1]

**Step 3.** The areas R and 2R are commensurable, since R measures both. [D10.1.1] Since R is incommensurable with S, it follows that 2R is likewise incommensurable with S. [10.13]

**Step 4.** Apply S and 2R to the assigned rational straight line r as rectangles, obtaining breadths u and v respectively. These applications can be constructed by taking third proportionals to r and the respective square-sides of S and 2R: the resulting rectangles equal those squares. [6.11, 6.17] Since both applied areas are medial, both breadths u and v are rational straight lines. [10.22]

**Step 5.** Rectangles with the same height are to one another as their bases; thus S : 2R = u : v. [6.1] By Step 3, S and 2R are incommensurable, so u and v are incommensurable in length. [10.11] But, being rational, their squares are both commensurable with the square on r, and consequently are commensurable with one another. [D10.1.3, 10.12] Thus u and v are commensurable in square only. [D10.1.2]

**Step 6.** Apply 10.36: the sum u + v is irrational. This is the direct path, since the application of the two areas has produced exactly the rational straight lines commensurable in square only required by that proposition. [10.36]

**Step 7.** The rectangle contained by r and u + v equals the sum of the rectangles contained by r, u and by r, v; it therefore equals S + 2R, which is W by Step 1. [2.1] If W were rational, its application to the rational line r would produce a rational breadth, commensurable in length with r. [10.20] That breadth is u + v, contradicting Step 6. Hence W is an irrational area, and its square-side x is an irrational straight line. [D10.1.4] Thus the sum of the given lines is irrational; since its square is the sum of the two medial areas S and 2R, let it be called the **side of the sum of two medial areas**.

**USED:** 10.11, 10.12, 10.13, 10.20, 10.21, 10.22, 10.23, 10.24, 10.36, 2.1, 2.4, 6.1, 6.11, 6.17, D10.1.1, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 10.11, 10.22, 10.35, 10.36, 2.4, 6.1, D10.1.4
**Jaccard:** 0.316 — AI adds ['10.12', '10.13', '10.20', '10.21', '10.23', '10.24', '2.1', '6.11', '6.17', 'D10.1.1', 'D10.1.2', 'D10.1.3']; Human adds ['10.35']

## Proposition 10.42
**Statement:** A binomial straight line is divided into its terms at one point only.

**Step 1.** Let AB be a binomial divided into its terms at C. By 10.36, AC and CB are rational straight lines commensurable in square only. Suppose there is another division into such terms at D. Compare the terms in the same order, taking the greater term from A: thus AC > CB and AD > DB. This fixes the order of the terms; their interchange is not a different decomposition. [10.36]

**Step 2.** Write S = AC² + CB² and T = AD² + DB², where squares denote areas. Each component square is rational, hence commensurable with the square on the assigned rational straight line. The component squares are therefore commensurable with one another, and each sum is commensurable with its components and consequently with the assigned square. Thus S and T are rational areas. [D10.1.3, D10.1.4, 10.12, 10.15]

**Step 3.** Let P be the rectangle contained by AC and CB, and Q the rectangle contained by AD and DB. Both are medial areas, since each is contained by rational straight lines commensurable in square only. The direct route is to use 10.26: a positive difference between these medial areas cannot be rational. [10.21, 10.26]

**Step 4.** By the square-of-a-sum identity,
AB² = S + 2P = T + 2Q.
If P and Q are unequal, exchange the names of the two proposed divisions if necessary so that Q > P. Subtracting common areas then gives
S − T = 2(Q − P) > 0.
Since S and T are rational, they are commensurable. Applying the converse part of 10.15 to S = T + (S − T), their positive difference is commensurable with T and hence with the assigned rational square. Therefore S − T is rational. [2.4, CN2, CN3, CN5, 10.12, 10.15, D10.1.4]

**Step 5.** The area Q − P measures S − T twice, so these two areas are commensurable. Since S − T is rational, Q − P is rational also. But this says that the medial area Q exceeds the medial area P by a rational area, contrary to 10.26. Consequently P = Q. [D10.1.1, 10.12, D10.1.4, 10.26]

**Step 6.** Bisect AB at O. Because AC > CB and AD > DB, both C and D lie on the B-side of O. Applying 2.5 to the equal division at O and each proposed unequal division gives
P + OC² = AO²,
Q + OD² = AO².
Since P = Q, subtraction yields OC² = OD². [1.10, CN5, 2.5, CN3]

**Step 7.** If C and D were distinct on the same side of O, one of OC and OD would be a proper part of the other. By 2.4, the square on the longer would equal the square on the shorter together with positive additional areas, and would therefore be greater. This contradicts OC² = OD². Hence C = D. Thus the greater and lesser terms are uniquely determined, and, with their order fixed, a binomial straight line is divided into its terms at one point only. [2.4, CN5]

**USED:** 1.10, 10.12, 10.15, 10.21, 10.26, 10.36, 2.4, 2.5, CN2, CN3, CN5, D10.1.1, D10.1.3, D10.1.4
**Human refs (from References field):** 10.21, 10.36, 2.4
**Jaccard:** 0.214 — AI adds ['1.10', '10.12', '10.15', '10.26', '2.5', 'CN2', 'CN3', 'CN5', 'D10.1.1', 'D10.1.3', 'D10.1.4']

## Proposition 10.43
**Statement:** A first bimedial straight line is divided at one point only.

**Step 1.** Let a first bimedial straight line have terms a, b, and suppose it also has terms c, d. Compare the divisions in the conventional order, with the greater term measured from the same endpoint, so that a>b and c>d. Thus a+b=c+d; each pair consists of medial straight lines commensurable in square only, and the rectangles ab and cd are rational [10.37]. Here xy denotes the rectangle contained by x and y, and x² the square on x. We shall use 10.26 directly: the relevant obstruction is that two medial areas cannot differ by a rational area.

**Step 2.** Construct a third proportional e to a, b, so that a:b=b:e [6.11]. Then ae=b² [6.17]. Moreover, a²:ae=a:e [6.1]. Since a² and b² are commensurable, it follows that a and e are commensurable in length [10.11].

**Step 3.** Consequently a+e is commensurable in length with a [10.15], and is therefore medial [10.23]. The rectangle a(a+e) is consequently medial [10.24]. But a(a+e)=a²+ae=a²+b² [2.3]. Hence M=a²+b² is a medial area. Applying the same construction and argument to c, d shows that N=c²+d² is also medial [6.11, 6.17, 6.1, 10.11, 10.15, 10.23, 10.24, 2.3].

**Step 4.** Put R=2ab and S=2cd. Both are rational areas: doubling an area commensurable with the assigned rational square preserves a common measure with that square [D10.1.1, D10.1.4]. By the square-of-a-sum identity and the equality a+b=c+d,
M+R=(a+b)²=(c+d)²=N+S [2.4].

**Step 5.** Suppose M and N are unequal; interchange the two decompositions if necessary so that M>N. The preceding equality then gives S>R and M−N=S−R [CN3, CN5]. Since R and S are rational, they are commensurable [D10.1.4, 10.12]. Since S=R+(S−R), the difference S−R is commensurable with R [10.15], and hence with the assigned rational square [10.12]. Thus S−R is rational [D10.1.4]. This would make the medial area M exceed the medial area N by a rational area, contrary to 10.26. Therefore M=N, and subtraction from M+R=N+S gives R=S [CN3].

**Step 6.** Applying 2.7 to the greater term a and its part b gives (a−b)²=a²+b²−2ab=M−R. Similarly, (c−d)²=N−S [2.7]. Thus these squares are equal [CN3]. Their positive sides must therefore be equal: if one side were greater, its square would be greater by 2.4 and CN5. Hence a−b=c−d.

**Step 7.** We now have both a+b=c+d and a−b=c−d. If a>c, the equality of the sums gives b<d, and consequently a−b>c−d, a contradiction; the case a<c gives the reverse contradiction [CN3, CN5]. Therefore a=c, and subtraction gives b=d [CN3]. The equal greater terms, measured from the same endpoint, terminate at the same point: otherwise one would properly contain the other, contrary to CN5. Thus the division into the first-bimedial terms is unique, as required.

**USED:** 10.11, 10.12, 10.15, 10.23, 10.24, 10.26, 10.37, 2.3, 2.4, 2.7, 6.1, 6.11, 6.17, CN3, CN5, D10.1.1, D10.1.4
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['10.11', '10.12', '10.15', '10.23', '10.24', '10.26', '10.37', '2.3', '2.4', '2.7', '6.1', '6.11', '6.17', 'CN3', 'CN5', 'D10.1.1', 'D10.1.4']

## Proposition 10.44
**Statement:** A second bimedial straight line is divided at one point only.

**Step 1.** Let L be a second bimedial straight line, divided into terms a and b, with a>b. Thus a and b are medial, their squares are commensurable, they are incommensurable in length, and the rectangle ab is medial (10.38; D10.1.2). Divisions into terms are compared with the greater term measured from the same endpoint. **Path choice:** reduce to the uniqueness of binomial division, 10.42, because application of medial areas to a rational straight line produces rational breadths (10.22).

**Step 2.** Fix the assigned rational straight line r. Construct breadths u, v, t such that
ru=a², rv=b², rt=ab.
These constructions are supplied by fourth proportionals and the equality of the corresponding rectangles (6.12; 6.16). Since all three applied areas are medial, u, v, and t are rational straight lines (10.22).

**Step 3.** Put X=u+v and Y=2t. Since u:v=a²:b², the commensurability of a² and b² implies that u and v are commensurable in length (6.1; 10.11). Consequently X is commensurable in length with u (10.15), while Y is commensurable in length with t (D10.1.1). Both X and Y are therefore rational: their squares are respectively commensurable with u² and t² by 10.9 and 10.6, and hence with the assigned rational square by 10.12 and D10.1.3.

**Step 4.** By comparison of rectangles of equal altitude,
u:t=a²:ab=a:b (6.1).
Since a and b are incommensurable in length, so are u and t (10.11). Because X is commensurable with u and Y with t, two applications of 10.13 show that X and Y are incommensurable in length. Being rational, they are nevertheless commensurable in square (D10.1.3; 10.12). Thus X+Y is a binomial, with terms X and Y (10.36).

**Step 5.** Distributing the rectangles gives
rX=a²+b², rY=2ab,
and therefore
r(X+Y)=a²+b²+2ab=L²
(2.1; 2.4; CN2). Moreover,
a²+b²=2ab+(a−b)²
by 2.7. Since a>b, it follows that rX>rY, and hence X>Y (CN5; 6.1). Thus X is the greater term of this binomial.

**Step 6.** Suppose L also has a second-bimedial division L=c+d, with c>d. Applying Steps 2–5 to c and d, using the same rational line r, produces rational straight lines u′, v′, t′ and binomial terms
X′=u′+v′, Y′=2t′,
where X′>Y′ and r(X′+Y′)=L². The equal rectangles on the same altitude r imply X+Y=X′+Y′ (6.1; 5.9). The uniqueness of binomial division now gives X=X′ and Y=Y′, with greater terms corresponding (10.42).

**Step 7.** Since Y=2t and Y′=2t′, the equality Y=Y′ gives t=t′: each has the same ratio, one to two, to that common whole (5.9). Consequently the defining rectangle equalities yield
ab=rt=rt′=cd
(6.16; CN1).

**Step 8.** Bisect L, and let h denote either half (1.10). Applying 2.5 to its two unequal divisions gives
ab+(a−h)²=h²,
cd+(c−h)²=h².
Since ab=cd, subtraction gives (a−h)²=(c−h)² (CN3). Both a−h and c−h are positive, and unequal positive straight lines have unequal squares, as follows immediately from 2.4 and CN5. Hence a−h=c−h, so a=c and then b=d (CN2; CN3). The terms therefore coincide; with the greater term measured from the fixed endpoint, their dividing points coincide as well. Thus a second bimedial straight line is divided into its terms at one point only.

**USED:** 1.10, 10.11, 10.12, 10.13, 10.15, 10.22, 10.36, 10.38, 10.42, 10.6, 10.9, 2.1, 2.4, 2.5, 2.7, 5.9, 6.1, 6.12, 6.16, CN1, CN2, CN3, CN5, D10.1.1, D10.1.2, D10.1.3
**Human refs (from References field):** 10.11, 10.13, 10.22, 10.36, 10.38, 10.6, 2.4, 6.1
**Jaccard:** 0.308 — AI adds ['1.10', '10.12', '10.15', '10.42', '10.9', '2.1', '2.5', '2.7', '5.9', '6.12', '6.16', 'CN1', 'CN2', 'CN3', 'CN5', 'D10.1.1', 'D10.1.2', 'D10.1.3']

## Proposition 10.45
**Statement:** A major straight line is divided at one and the same point only.

**Step 1.** Let AB be a major straight line, divided into its terms at C. Fix the order of the terms by taking the greater term from A, so that AC > CB; merely exchanging the terms is not a different decomposition. Write S = AC² + CB² and P = AC·CB, where products denote rectangular areas. By the characterization of a major straight line, S is rational and P is medial. [10.39]

**Step 2.** Suppose that D is another division into such terms, again with AD > DB. Put T = AD² + DB² and Q = AD·DB. Then T is rational and Q is medial. Moreover, the square on the whole gives
S + 2P = AB² = T + 2Q.
[10.39; 2.4; CN1]

**Step 3.** We compare the medial rectangles directly: the relevant obstruction is that their difference cannot be rational. Suppose P and Q are unequal, and interchange the names of the two divisions if necessary so that P > Q. The equality in Step 2 then gives
T − S = 2(P − Q) > 0.
[CN2; CN3; CN5; path choice: 10.26]

**Step 4.** Let R be the square on the assigned rational straight line. Since S and T are rational, each is commensurable with R, and therefore they are commensurable with one another. Set E = T − S. Because T = S + E is commensurable with S, E is commensurable with S, and hence with R. Thus E is a rational area. [D10.1.4; 10.12; 10.15]

**Step 5.** Set F = P − Q. By Step 3, E = 2F, so F measures both itself and E; hence F and E are commensurable. Since E is commensurable with R, F is also commensurable with R and is therefore rational. But P and Q are medial areas, and P exceeds Q by F, a rational area, contrary to 10.26. Consequently P = Q. [D10.1.1; 10.12; D10.1.4; 10.26]

**Step 6.** Bisect AB at M. Since AC > CB and AD > DB, both C and D lie between M and B. Applying the identity for a line cut equally and unequally to the cuts at C and D gives
P + MC² = AM²,
Q + MD² = AM².
Since P = Q, subtraction yields MC² = MD². [1.10; 2.5; CN1; CN3]

**Step 7.** Equal squares have equal sides: otherwise, placing the squares on the same side of their nested collinear bases, the square on the shorter base would be a proper part of the square on the longer, contradicting their equality. Thus MC = MD. Since C and D lie on the same ray from M, distinct points would make one of these segments a proper part of the other; therefore C = D. Hence a major straight line is divided at one and the same point only. [CN5]

**USED:** 1.10, 10.12, 10.15, 10.26, 10.39, 2.4, 2.5, CN1, CN2, CN3, CN5, D10.1.1, D10.1.4
**Human refs (from References field):** 10.26, 10.39
**Jaccard:** 0.154 — AI adds ['1.10', '10.12', '10.15', '2.4', '2.5', 'CN1', 'CN2', 'CN3', 'CN5', 'D10.1.1', 'D10.1.4']

## Proposition 10.46
**Statement:** The side of a rational plus a medial area is divided at one point only.

**Step 1.** Let AB be a side of a rational plus a medial area, divided into its terms at C. As usual, compare divisions with the greater term adjacent to the same endpoint A. Thus AC > CB, the sum S = AC² + CB² is medial, and the rectangle P contained by AC, CB is rational. These are the defining properties in 10.40.

**Step 2.** Suppose D is another such division, with AD > DB. Then T = AD² + DB² is medial, and the rectangle Q contained by AD, DB is rational (10.40). Applying 2.4 to both divisions gives
S + 2P = AB² = T + 2Q,
and hence S + 2P = T + 2Q (CN1). The direct route is therefore to apply 10.26 to the medial summands, rather than reduce the question to another uniqueness proposition.

**Step 3.** The areas 2P and 2Q are rational: any common measure of P and the assigned rational square also measures 2P, and similarly for Q (D10.1.1, D10.1.4). If these doubled rectangles are unequal, their positive difference is rational also. Indeed, they are commensurable with one another by 10.12; their difference is commensurable with the smaller by 10.15; and that difference is therefore commensurable with the assigned rational square by 10.12. It is consequently rational by D10.1.4.

**Step 4.** If P and Q were unequal, interchange the names of the two divisions if necessary so that P > Q. Subtracting equal areas from the equality in Step 2 gives
T = S + (2P − 2Q) (CN3).
Thus the medial area T would exceed the medial area S by a positive rational area, contrary to 10.26. Therefore P = Q.

**Step 5.** Bisect AB at M (1.10). Since AC > CB and AD > DB, both C and D lie between M and B. Applying 2.5 to the equal division at M and each unequal division gives
P + MC² = AM²,
Q + MD² = AM².
Since P = Q, subtraction yields MC² = MD² (CN1, CN3).

**Step 6.** Therefore MC = MD: otherwise, applying 2.4 to the greater of these lengths as the sum of the smaller and its positive excess would make its square strictly greater (CN5). Since C and D lie on the same side of M, they must coincide; otherwise one of MC, MD would be a proper part of the other, contradicting their equality (CN5). Hence the side of a rational plus a medial area is divided into its terms at one point only.

**USED:** 1.10, 10.12, 10.15, 10.26, 10.40, 2.4, 2.5, CN1, CN3, CN5, D10.1.1, D10.1.4
**Human refs (from References field):** 10.26, 10.40
**Jaccard:** 0.167 — AI adds ['1.10', '10.12', '10.15', '2.4', '2.5', 'CN1', 'CN3', 'CN5', 'D10.1.1', 'D10.1.4']

## Proposition 10.47
**Statement:** The side of the sum of two medial areas is divided at one point only.

**Step 1.** Let L be a side of the sum of two medial areas. Suppose that L = a + b = c + d are two divisions into its defining terms. Take the greater term from the same fixed extremity, so that a > b and c > d. Write t² for the square on t and uv for the rectangle contained by u and v. Set S = a² + b², P = ab, S′ = c² + d², and P′ = cd. By 10.41, S and P are medial and incommensurable with one another; likewise S′ and P′ are medial and incommensurable with one another.

**Step 2.** Take the assigned rational straight line r [D10.1.3]. Apply S, P, S′, and P′ to r as rectangles, and call their respective breadths x, y, x′, and y′. Such applications can be made triangle by triangle using 1.44, adding the resulting breadths by 2.1. Thus rx = S, ry = P, rx′ = S′, and ry′ = P′. All four breadths are rational by 10.22. The chosen route is to obtain a binomial from these breadths: binomial uniqueness, 10.42, is the earlier uniqueness theorem naturally reached by application to a rational line.

**Step 3.** By 2.4, the square on 2y is four times the square on y, and similarly for 2y′ and y′. These pairs of squares are therefore commensurable [D10.1.1, D10.1.2]. Since y and y′ are rational, transitivity of commensurability shows that 2y and 2y′ are rational also [10.12, D10.1.3]. Consequently x and 2y are commensurable in square, as are x′ and 2y′ [10.12, D10.1.3].

**Step 4.** Rectangles on the same base are proportional to their breadths; hence S : P = x : y and S′ : P′ = x′ : y′ [6.1]. The defining incommensurabilities therefore imply that x and y are incommensurable in length, as are x′ and y′ [10.11]. But y and 2y have a common measure, and likewise y′ and 2y′ [D10.1.1]. Thus x and 2y are incommensurable in length, as are x′ and 2y′ [10.13]. Together with Step 3, this proves that x + 2y and x′ + 2y′ are binomials [10.36].

**Step 5.** The square on the whole line satisfies L² = S + 2P = S′ + 2P′ [2.4]. Using the applications in Step 2 and distributing rectangles by 2.1, we obtain r(x + 2y) = r(x′ + 2y′). Since these rectangles have the same base, their breadths are equal: x + 2y = x′ + 2y′ [6.1]. Moreover, 2.7 gives S = 2P + (a − b)² and S′ = 2P′ + (c − d)². Thus S > 2P and S′ > 2P′ [CN5], so x > 2y and x′ > 2y′ [2.1, 6.1].

**Step 6.** We therefore have two divisions of the same binomial into its terms, with the greater terms taken from the same extremity. By 10.42, these divisions coincide. Hence x = x′ and 2y = 2y′. Their corresponding rectangles on r are equal, giving S = S′ and 2P = 2P′ [2.1, 6.1].

**Step 7.** Subtracting these equal doubled rectangles from the equal sums of squares, and using 2.7, gives (a − b)² = (c − d)² [CN3]. Therefore a − b = c − d: otherwise 2.4 would express the square on the greater of these positive differences as the square on the lesser together with positive additional areas, contradicting equality [CN5].

**Step 8.** Adding a − b = c − d to a + b = c + d gives 2a = 2c [CN2], and hence a = c; unequal positive magnitudes cannot have equal doubles [CN2, CN5]. Subtraction then gives b = d [CN3]. Thus the greater segments measured from the fixed extremity are identical, and the division points coincide. The defining division exists by 10.41, and no distinct such division is possible. Therefore the side of the sum of two medial areas is divided at one point only.

**USED:** 1.44, 10.11, 10.12, 10.13, 10.22, 10.36, 10.41, 10.42, 2.1, 2.4, 2.7, 6.1, CN2, CN3, CN5, D10.1.1, D10.1.2, D10.1.3
**Human refs (from References field):** 10.11, 10.22, 10.36, 10.42, 2.4, 6.1
**Jaccard:** 0.333 — AI adds ['1.44', '10.12', '10.13', '10.41', '2.1', '2.7', 'CN2', 'CN3', 'CN5', 'D10.1.1', 'D10.1.2', 'D10.1.3']

## Proposition 10.48
**Statement:** To find the first binomial straight line.

**Step 1.** Let AB be the assigned rational straight line, and write r = AB. By 10.29, construct two rational straight lines a > b, commensurable in square only, such that a² = b² + c² for a straight line c commensurable in length with a. Here x² denotes the square on x. This construction is chosen because its commensurable square-excess is precisely the kind required for a first binomial. [D10.1.3, 10.29, D10.2.1]

**Step 2.** Construct a fourth proportional s to a, b, r, so that a : b = r : s. Since a > b, it follows that r > s. [6.12, 5.14]

**Step 3.** Since a and b are incommensurable in length and a : b = r : s, the straight lines r and s are likewise incommensurable in length. [10.11]

**Step 4.** Apply 6.22 directly to the squares on the four proportional straight lines: a² : b² = r² : s². Since a² and b² are commensurable, r² and s² are commensurable by 10.11. Thus r and s are commensurable in square; together with Step 3, they are commensurable in square only. Moreover, s is rational because it is commensurable in square with the assigned rational straight line r. [6.22, 10.11, D10.1.2, D10.1.3]

**Step 5.** By 10.14, the proportion a : b = r : s transfers the square-excess property from a, b to r, s. Therefore r² = s² + t² for a straight line t commensurable in length with r. [10.14]

**Step 6.** Produce AB beyond B and cut off BC equal to s. Since AB and BC are rational straight lines commensurable in square only, their sum AC is a binomial straight line. [P2, 1.3, 10.36]

**Step 7.** The greater term of this binomial is AB, since r > s. Its square exceeds the square on BC by the square on t, which is commensurable in length with AB. Finally, AB is the assigned rational straight line itself and hence is commensurable in length with it. Therefore AC is a first binomial straight line, as required. [D10.1.1, D10.2.1]

**USED:** 1.3, 10.11, 10.14, 10.29, 10.36, 5.14, 6.12, 6.22, D10.1.1, D10.1.2, D10.1.3, D10.2.1, P2
**Human refs (from References field):** 10.28, 10.36, 10.6, 10.9, 5.19
**Jaccard:** 0.059 — AI adds ['1.3', '10.11', '10.14', '10.29', '5.14', '6.12', '6.22', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.2.1', 'P2']; Human adds ['10.28', '10.6', '10.9', '5.19']

## Proposition 10.49
**Statement:** To find the second binomial straight line.

**Step 1.** Let r be the assigned rational straight line (D10.1.3). By 10.29 construct two rational straight lines a > b, commensurable in square only, such that a² = b² + d² for some straight line d commensurable in length with a. Here u² denotes the square on u. Path choice: use the pair supplied directly by 10.29 and scale its lesser term to r; this preserves the required square-difference condition without a new numerical construction.

**Step 2.** By 6.12 construct the fourth proportional x to b, a, r, so that b:a = r:x. Inverting this proportion gives a:b = x:r, as follows by reversing the equimultiple comparisons in D5.5. Since a > b, we have x > r (5.14).

**Step 3.** Since a and b are incommensurable in length and a:b = x:r, the straight lines x and r are likewise incommensurable in length (10.11).

**Step 4.** The same proportion gives a²:b² = x²:r², because squares are similar figures similarly described on the proportional straight lines (6.22). The squares a² and b² are commensurable by Step 1; consequently x² and r² are commensurable (10.11). Thus x and r are commensurable in square (D10.1.2), and x is rational relative to the assigned line r (D10.1.3). Together with Step 3, this shows that x and r are two rational straight lines commensurable in square only.

**Step 5.** Apply 10.14 to a:b = x:r. Since a² exceeds b² by the square on a straight line commensurable in length with a, there is a straight line e commensurable in length with x such that x² = r² + e².

**Step 6.** Take AB equal to x, produce it beyond B, and cut off BC equal to r on the produced straight line (P2, 1.3). By Step 4, AB and BC are rational and commensurable in square only. Therefore their sum AC is a binomial straight line, with terms AB and BC (10.36).

**Step 7.** The greater term is AB, since x > r. By Step 5, its square exceeds the square on the lesser term BC by the square on a straight line commensurable in length with AB. Moreover, BC equals r and is therefore commensurable in length with the assigned rational straight line (D10.1.1). Hence AC satisfies the common square-difference condition of D10.2.1 and the lesser-term condition of D10.2.2. Therefore AC is a second binomial straight line, as required.

**USED:** 1.3, 10.11, 10.14, 10.29, 10.36, 5.14, 6.12, 6.22, D10.1.1, D10.1.2, D10.1.3, D10.2.1, D10.2.2, D5.5, P2
**Human refs (from References field):** 10.36, 10.6, 10.9, 5.19
**Jaccard:** 0.056 — AI adds ['1.3', '10.11', '10.14', '10.29', '5.14', '6.12', '6.22', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.2.1', 'D10.2.2', 'D5.5', 'P2']; Human adds ['10.6', '10.9', '5.19']

## Proposition 10.50
**Statement:** To find the third binomial straight line.

**Step 1.** Let r be the assigned rational straight line, and let S denote its square. Construct squares equal respectively to rectilineal areas consisting of eight and six copies of S, and call their sides a and b. Thus a² = 8S and b² = 6S. Here a² denotes the square on a, and similarly elsewhere. Path choice: use the square-equal-to-area construction directly, since prescribing these two areas will control both the terms’ commensurability and the difference of their squares. [1.46, 2.14]

**Step 2.** None of the ratios 3:1, 6:1, and 8:1 is a ratio of square numbers. Indeed, if N:1 = p²:q², then q² measures p²; hence q measures p by 8.14. Writing p = kq would give N = k². But 3 lies strictly between the consecutive squares 1 and 4, while 6 and 8 lie strictly between the consecutive squares 4 and 9. Thus none is a square. Moreover, 4:3 is not a ratio of square numbers: if 4:3 = p²:q², then 3p² = 4q² = (2q)², so 3:1 would be a ratio of square numbers, contrary to what was just established. [8.14, D7.15, D7.18, 7.19]

**Step 3.** The area S measures both a² and b². Consequently a and b are each commensurable in square with r, and are also commensurable in square with one another. Since r is the assigned rational straight line, both a and b are rational straight lines. [D10.1.2, D10.1.3]

**Step 4.** The ratios a²:r² = 8:1 and b²:r² = 6:1 are not ratios of square numbers, by Step 2. Therefore neither a nor b is commensurable in length with r. Likewise, a²:b² = 8:6 = 4:3 is not a ratio of square numbers, so a and b are incommensurable in length. Together with Step 3, this proves that a and b are rational straight lines commensurable in square only. [10.9]

**Step 5.** Since a² > b², a is the greater term. Bisect a, and call its half c. Squares have the duplicate ratio of their sides, so a²:c² = 4:1; hence c² = 2S. It follows that a² − b² = 8S − 6S = 2S = c². Moreover, c measures a twice, so c is commensurable in length with a. Thus the square on the greater term exceeds the square on the lesser by the square on a straight line commensurable in length with the greater. [6.20, 1.10, CN3, D10.1.1]

**Step 6.** Produce the segment a and lay off b consecutively with it, forming a straight line of length a + b. Since its two terms are rational and commensurable in square only, their sum is a binomial straight line. [P2, 1.3, 10.36]

**Step 7.** This binomial satisfies the square-difference condition proved in Step 5, and neither of its terms is commensurable in length with the assigned rational straight line r, by Step 4. Therefore a + b is a third binomial straight line, as required. [D10.2.3]

**USED:** 1.10, 1.3, 1.46, 10.36, 10.9, 2.14, 6.20, 7.19, 8.14, CN3, D10.1.1, D10.1.2, D10.1.3, D10.2.3, D7.15, D7.18, P2
**Human refs (from References field):** 10.36, 10.6, 10.9, 5.19, 5.22
**Jaccard:** 0.100 — AI adds ['1.10', '1.3', '1.46', '2.14', '6.20', '7.19', '8.14', 'CN3', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.2.3', 'D7.15', 'D7.18', 'P2']; Human adds ['10.6', '5.19', '5.22']

## Proposition 10.51
**Statement:** To find the fourth binomial straight line.

**Step 1.** Let r be the assigned rational straight line. By 10.30, construct two rational straight lines a > b, commensurable in square only, such that a² = b² + c² for a straight line c incommensurable in length with a. Here x² denotes the square on x. Our path is to use this ready-made square-difference condition and scale the greater term to r. [10.30]

**Step 2.** Construct a fourth proportional s so that a:b = r:s. By alternation, a:r = b:s; since a > b, it follows that r > s. [6.12, 5.16, 5.14]

**Step 3.** The squares on these proportional straight lines are proportional: a²:b² = r²:s². Since a² and b² are commensurable, r² and s² are also commensurable. Thus r and s are commensurable in square, and s is rational relative to the assigned line r. Moreover, since a and b are incommensurable in length and a:b = r:s, r and s are incommensurable in length. Consequently r and s are rational straight lines commensurable in square only. [6.22, 10.11, D10.1.2, D10.1.3]

**Step 4.** Apply 10.14 to a:b = r:s. Since a² exceeds b² by the square on a straight line incommensurable in length with a, r² exceeds s² by the square on a straight line e incommensurable in length with r. Thus r² = s² + e², with e incommensurable in length with r. [10.14]

**Step 5.** Produce the straight line r and cut off on its continuation a straight line equal to s, obtaining the whole r + s. Since its two terms are rational and commensurable in square only, this whole is a binomial straight line. [P2, 1.3, 10.36]

**Step 6.** The greater term is r itself, hence is commensurable in length with the assigned rational straight line. Its square exceeds the square on the lesser term s by the square on e, which is incommensurable in length with r. Therefore, by the definition, r + s is a fourth binomial straight line. The required straight line has been found. [D10.1.1, D10.2.4]

**USED:** 1.3, 10.11, 10.14, 10.30, 10.36, 5.14, 5.16, 6.12, 6.22, D10.1.1, D10.1.2, D10.1.3, D10.2.4, P2
**Human refs (from References field):** 10.6, 10.9, 5.19
**Jaccard:** 0.000 — AI adds ['1.3', '10.11', '10.14', '10.30', '10.36', '5.14', '5.16', '6.12', '6.22', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.2.4', 'P2']; Human adds ['10.6', '10.9', '5.19']

## Proposition 10.52
**Statement:** To find the fifth binomial straight line.

**Step 1.** Let r be the assigned rational straight line [D10.1.3], and write t² for the square on a straight line t. By 10.30, construct two rational straight lines a > b, commensurable in square only, such that a² = b² + c², where c is incommensurable in length with a. Path choice: use this previously constructed pair, which already has the required excess-square property, and rescale it so that its lesser term becomes r.

**Step 2.** Construct a fourth proportional x so that b : a = r : x [6.12]. Inverting gives a : b = x : r [D5.5, D5.13]. Since a > b, this equality of ratios also gives x > r [D5.5].

**Step 3.** The squares on these proportional straight lines are proportional: a² : b² = x² : r² [6.22]. Since a² and b² are commensurable, x² and r² are commensurable [10.11]. Consequently x is commensurable in square with the assigned rational line r, and is therefore rational [D10.1.2, D10.1.3].

**Step 4.** Since a and b are incommensurable in length and a : b = x : r, the straight lines x and r are likewise incommensurable in length [10.11]. Together with Step 3, this shows that x and r are rational straight lines commensurable in square only.

**Step 5.** Apply 10.14 to a : b = x : r. Since a² exceeds b² by the square on c, which is incommensurable in length with a, it follows that x² exceeds r² by the square on a straight line y incommensurable in length with x. Thus x² = r² + y² [10.14].

**Step 6.** Produce a segment of length x and cut off on its continuation a segment of length r, obtaining a straight line L whose consecutive parts are x and r [P2, 1.3]. By Step 4 and 10.36, L is a binomial. Its lesser term is r, which is commensurable in length with the assigned rational straight line, being that very line [D10.1.1]; and, by Step 5, the square on its greater term exceeds the square on its lesser by the square on a line incommensurable in length with the greater. Therefore L is a fifth binomial straight line [D10.2.5]. Thus the required straight line has been found.

**USED:** 1.3, 10.11, 10.14, 10.30, 10.36, 6.12, 6.22, D10.1.1, D10.1.2, D10.1.3, D10.2.5, D5.13, D5.5, P2
**Human refs (from References field):** 10.36, 10.6, 10.9, 5.19
**Jaccard:** 0.059 — AI adds ['1.3', '10.11', '10.14', '10.30', '6.12', '6.22', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.2.5', 'D5.13', 'D5.5', 'P2']; Human adds ['10.6', '10.9', '5.19']

## Proposition 10.53
**Statement:** To find the sixth binomial straight line.

**Step 1.** Let r be the assigned rational straight line, and let Q denote its square. Construct rectilineal figures consisting of two and three adjacent copies of Q [1.46, CN2]. Construct squares equal to these figures, and call their sides b and a respectively. Thus b² = 2Q and a² = 3Q [2.14]. The direct path chosen is to prescribe square areas: 2.14 supplies the construction, and 10.9 will test the required length-incommensurabilities.

**Step 2.** The area Q measures each of r², b², and a². Hence these lines are pairwise commensurable in square, and a and b are rational relative to r [D10.1.2, D10.1.3]. Since a² = 3Q > 2Q = b², we have a > b [CN5, 6.20]. Moreover, subtracting b² gives a² − b² = Q = r² [CN3].

**Step 3.** The constructed square areas have the ratios
r² : a² = 4 : 12,
r² : b² = 4 : 8,
b² : a² = 4 : 6 [D5.5].
None of these numerical ratios is the ratio of a square number to a square number. For 4 is square, whereas 6 and 8 lie strictly between the consecutive squares 4 and 9, and 12 lies strictly between the consecutive squares 9 and 16 [D7.18]. If any of 4 : 12, 4 : 8, or 4 : 6 were a ratio of square numbers, its second term would also be square, by 8.24, a contradiction.

**Step 4.** Applying 10.9 to the three square-area ratios in Step 3, r is incommensurable in length with a, r is incommensurable in length with b, and b is incommensurable in length with a. Together with Step 2, this shows that a and b are rational straight lines commensurable in square only [10.9, D10.1.2, D10.1.3].

**Step 5.** Let AB be the constructed side a. Produce AB beyond B and cut off BC equal to b [P2, 1.3]. Since AB and BC are rational and commensurable in square only, their sum AC is a binomial straight line [10.36].

**Step 6.** Its greater term is AB = a, and the square on this term exceeds the square on its lesser term BC = b by r². The side r of this difference-square is incommensurable in length with the greater term a; moreover, neither term a nor b is commensurable in length with the assigned rational line r, by Step 4. Therefore AC is a sixth binomial straight line [D10.2.4, D10.2.6]. Thus the required straight line has been found.

**USED:** 1.3, 1.46, 10.36, 10.9, 2.14, 6.20, 8.24, CN2, CN3, CN5, D10.1.2, D10.1.3, D10.2.4, D10.2.6, D5.5, D7.18, P2
**Human refs (from References field):** 10.36, 10.6, 10.9, 5.19, 5.22
**Jaccard:** 0.100 — AI adds ['1.3', '1.46', '2.14', '6.20', '8.24', 'CN2', 'CN3', 'CN5', 'D10.1.2', 'D10.1.3', 'D10.2.4', 'D10.2.6', 'D5.5', 'D7.18', 'P2']; Human adds ['10.6', '5.19', '5.22']

## Proposition 10.54
**Statement:** If an area be contained by a rational straight line and the first binomial, the âsideâ of the area is the irrational straight line which is called binomial.

**Step 1.** Let the given area be the rectangle r(a+b), where r is the rational straight line set out and a+b is a first binomial, with a the greater term. Write st for the rectangle contained by s and t, and s² for the square on s. The terms a and b are rational and commensurable in square only; moreover, a is commensurable in length with r, and a² exceeds b² by the square on a straight line commensurable in length with a. [10.36, D10.2.1]

**Step 2.** Bisect b, writing b=2h; thus h² is one fourth of b². Apply to a a rectangle equal to h² and deficient by a square. This application is possible because b<a. Let the resulting parts of a be u and v, so that u+v=a and uv=h². By the converse direction of 10.17, u and v are commensurable in length. This is the direct path: the first-binomial square-excess condition supplies precisely the hypothesis of that converse. [1.10, 2.4, 6.28, 10.17]

**Step 3.** Since u and v are commensurable, their sum a is commensurable with each of them. Since a is also commensurable in length with r, both u and v are commensurable in length with r and are therefore rational straight lines. [10.15, 10.12, D10.1.3]

**Step 4.** Construct x as a mean proportional between r and u, and construct y as the fourth proportional to u, h, x. Then
r:x=x:u, and u:h=x:y.
Also, since uv=h², we have u:h=h:v. Consequently x:y=h:v. [6.13, 6.12, 6.17]

**Step 5.** Alternating x:y=u:h gives x:u=y:h. Hence r:x=y:h. Combining this with x:y=h:v, ex aequali gives r:y=y:v. The mean-proportional and rectangle identities therefore yield
x²=ru, y²=rv, and xy=rh. [5.16, 5.22, 6.17, 6.16]

**Step 6.** The rectangles ru and rv are rational, because their containing straight lines are rational and commensurable in length. Thus x² and y² are rational areas, and x and y are rational straight lines. Their squares are each commensurable with the square on the assigned rational line, hence with one another; therefore x and y are commensurable in square. [10.19, D10.1.4, D10.1.3, 10.12, D10.1.2]

**Step 7.** They are not commensurable in length. For, if x and y were commensurable in length, the proportion x:y=u:h would make u and h commensurable. But a is commensurable with u, while b=2h is commensurable with h. It would follow that a and b are commensurable in length, contrary to their being the terms of a binomial. Thus x and y are commensurable in square only. [10.11, D10.1.1, 10.12, 10.36]

**Step 8.** By the square-of-a-sum identity and the identities established above,
(x+y)² = x²+y²+2xy = ru+rv+2rh = r(u+v)+r(2h) = r(a+b).
Thus the square on x+y equals the given area. [2.4, 2.1, CN2]

**Step 9.** Since x and y are rational straight lines commensurable in square only, their sum x+y is irrational and is called binomial. Since its square equals the given area, the side of that area is therefore the irrational straight line called binomial, as required. [10.36, D10.1.4]

**USED:** 1.10, 10.11, 10.12, 10.15, 10.17, 10.19, 10.36, 2.1, 2.4, 5.16, 5.22, 6.12, 6.13, 6.16, 6.17, 6.28, CN2, D10.1.1, D10.1.2, D10.1.3, D10.1.4, D10.2.1
**Human refs (from References field):** 10.11, 10.12, 10.13, 10.15, 10.17, 10.19, 10.36, 2.14, 6.1, 6.17, D10.2.1
**Jaccard:** 0.320 — AI adds ['1.10', '2.1', '2.4', '5.16', '5.22', '6.12', '6.13', '6.16', '6.28', 'CN2', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.1.4']; Human adds ['10.13', '2.14', '6.1']

## Proposition 10.55
**Statement:** If an area be contained by a rational straight line and the second binomial, the âsideâ of the area is the irrational straight line which is called a first bimedial.

**Step 1.** Let r be the given rational straight line, and let a+b, with a>b, be the second binomial relative to r. Write st for the rectangle contained by s,t, and s² for the square on s. By the definition of a binomial and of the second binomial, a,b are rational and commensurable in square only; b is commensurable in length with r; and a²=b²+c² for some c commensurable in length with a (10.36; D10.2.1; D10.2.2). Consequently a is incommensurable in length with r (10.13).

**Step 2.** Bisect b, calling its half h (1.10); thus b²=4h² (2.4). Apply to a a rectangle equal to h² and deficient by a square, obtaining segments u,v such that
u+v=a, uv=h².
This application is possible by 6.28, since b<a and therefore h² is less than the square on half a. The commensurable-division direction of 10.17 now gives that u,v are commensurable in length. This is the direct path furnished by the defining excess-square condition of the second binomial.

**Step 3.** Since u,v are commensurable in length, each is commensurable in length with their sum a (10.15). Their squares are therefore commensurable with a² (10.9; 10.6), so u,v are rational (10.12; D10.1.3). But a is incommensurable in length with r; hence both u and v are incommensurable in length with r (10.13). Since these lines are rational, their squares are nevertheless commensurable with r² (10.12; D10.1.2; D10.1.3). Thus each of u,v is commensurable in square only with r.

**Step 4.** Construct x as a mean proportional between r,u, and y as a mean proportional between r,v (6.13). Then
x²=ru, y²=rv
by 6.17. Each of these rectangles is contained by rational straight lines commensurable in square only; therefore x,y are medial straight lines (10.21). Moreover,
x²:y²=ru:rv=u:v
by 6.1. Since u,v are commensurable, x²,y² are commensurable (10.11); hence x,y are commensurable in square (D10.1.2).

**Step 5.** We next determine their rectangle. By 6.1 and uv=h²,
x²:y²=u:v=u²:(uv)=u²:h².
The converse part of 6.22, applied to these squares, gives x:y=u:h. Alternating gives x:u=y:h (5.16). But r:x=x:u by the construction of x, so r:x=y:h (5.11). Therefore
xy=rh
by 6.16.

**Step 6.** The rectangle rb is rational, since r,b are rational and commensurable in length (10.19). Since b=2h, we have rb=2rh (2.1). Thus rh is commensurable with rb (D10.1.1), and is consequently rational (10.12; D10.1.4). By Step 5, the rectangle xy is therefore rational.

**Step 7.** The square on x+y is
(x+y)²=x²+y²+2xy=ru+rv+2rh
by 2.4 and substitution of the established equalities (CN2). Since u+v=a and 2h=b, distribution of the rectangles gives
(x+y)²=r(u+v)+rb=ra+rb=r(a+b)
by 2.1. Thus x+y is the side of the given area (D10.1.4).

**Step 8.** The medial lines x,y cannot be commensurable in length: otherwise their rectangle would be medial by 10.24, whereas Step 6 proves it rational. A medial area is irrational and cannot be rational (10.21; D10.1.4). Hence x,y are commensurable in square only. They are medial and contain a rational rectangle, so their sum x+y is irrational and is called a first bimedial straight line (10.37). Since its square equals r(a+b), the side of the given area is a first bimedial, as required.

**USED:** 1.10, 10.11, 10.12, 10.13, 10.15, 10.17, 10.19, 10.21, 10.24, 10.36, 10.37, 10.6, 10.9, 2.1, 2.4, 5.11, 5.16, 6.1, 6.13, 6.16, 6.17, 6.22, 6.28, CN2, D10.1.1, D10.1.2, D10.1.3, D10.1.4, D10.2.1, D10.2.2
**Human refs (from References field):** 10.11, 10.12, 10.13, 10.15, 10.17, 10.19, 10.21, 10.37, 6.1, D10.2.2
**Jaccard:** 0.333 — AI adds ['1.10', '10.24', '10.36', '10.6', '10.9', '2.1', '2.4', '5.11', '5.16', '6.13', '6.16', '6.17', '6.22', '6.28', 'CN2', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.1.4', 'D10.2.1']

## Proposition 10.56
**Statement:** If an area be contained by a rational straight line and the third binomial, the âsideâ of the area is the irrational straight line called a second bimedial.

**Step 1.** Let r be the given rational straight line, and let a+b be the third binomial relative to r, with a>b. Write st for the rectangle contained by s and t, and s² for the square on s. By the meaning of binomial, a and b are rational and commensurable in square only [10.36]. Moreover, neither is commensurable in length with r, and a²=b²+c² for some c commensurable in length with a [D10.2.1, D10.2.3]. We must identify the side of r(a+b).

**Step 2.** Bisect b, calling its half t [1.10]. Apply to a a rectangle equal to t² and deficient by a square. This construction is possible because t² is smaller than the square on half of a [6.28]. It divides a into positive parts u and v such that
u+v=a, and uv=t².
Since a² exceeds b² by the square on a line commensurable in length with a, the converse direction of 10.17 gives that u and v are commensurable in length. This is the direct route from the defining square-difference condition to the required commensurable division [10.17]. Consequently, each of u and v is commensurable in length with a [10.15]. Also, t is commensurable in length with b, since b=2t [D10.1.1].

**Step 3.** Commensurability in length implies commensurability of the corresponding squares: the squares have a square-number ratio, hence are commensurable [10.9, 10.6]. Thus u² and v² are commensurable with a², and t² with b². Since a and b are rational, it follows that u, v, and t are rational [10.12, D10.1.3]. Since a and b are each incommensurable in length with r, so are u, v, and t [10.13]. Furthermore, a and b are incommensurable in length; therefore u and b, and then u and t, are incommensurable in length [10.13].

**Step 4.** Since the rectangles ru and rv are already specified, construct their square-sides x and y, so that
x²=ru, and y²=rv [2.14].
Each rectangle is contained by rational straight lines commensurable in square only. Therefore x and y are medial straight lines [10.21].

**Step 5.** Rectangles of the same height are proportional to their bases, so
x²:y²=ru:rv=u:v [6.1].
Since u and v are commensurable, x² and y² are commensurable [10.11]. Thus x and y are commensurable in square [D10.1.2].

**Step 6.** Again using rectangles of the same height and the equality uv=t², we have
x²:y²=u:v=u²:uv=u²:t² [6.1].
Proportional squares have proportional sides; hence
x:y=u:t [6.22].
But u and t are incommensurable in length by Step 3. Therefore x and y are incommensurable in length [10.11]. Together with Step 5, this proves that x and y are commensurable in square only.

**Step 7.** The proportion just obtained gives
x²:xy=x:y=u:t=ru:rt [6.1].
Since x²=ru, equality of these ratios implies xy=rt [5.9]. Now r and t are rational straight lines commensurable in square only, so rt is a medial area—that is, its square-side is medial [10.21]. Consequently, the rectangle xy is medial.

**Step 8.** The square on the sum of two straight lines equals the sum of their squares together with twice their rectangle [2.4]. Substituting the equalities already proved and distributing rectangles over their divided sides gives
(x+y)²=x²+y²+2xy
=ru+rv+2rt
=r(u+v)+r(2t)
=r(a+b) [2.1, CN2].
Thus x+y is the side of the given area.

**Step 9.** The straight lines x and y are medial, are commensurable in square only, and contain a medial rectangle. Their sum is therefore the irrational straight line called a second bimedial [10.38]. By Step 8, this sum is the side of the area contained by r and the third binomial a+b. Hence the required side is a second bimedial.

**USED:** 1.10, 10.11, 10.12, 10.13, 10.15, 10.17, 10.21, 10.36, 10.38, 10.6, 10.9, 2.1, 2.14, 2.4, 5.9, 6.1, 6.22, 6.28, CN2, D10.1.1, D10.1.2, D10.1.3, D10.2.1, D10.2.3
**Human refs (from References field):** 10.13, 10.21, 10.38, D10.2.3
**Jaccard:** 0.167 — AI adds ['1.10', '10.11', '10.12', '10.15', '10.17', '10.36', '10.6', '10.9', '2.1', '2.14', '2.4', '5.9', '6.1', '6.22', '6.28', 'CN2', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.2.1']

## Proposition 10.57
**Statement:** If an area be contained by a rational straight line and the fourth binomial, the âsideâ of the area is the irrational straight line called major.

**Step 1.** Let r be the given rational straight line, and let a+b be the fourth binomial, with a>b. Write pq for the rectangle contained by p and q, and p² for the square on p. The terms a and b are rational and commensurable in square only (10.36). Moreover, a is commensurable in length with r, and a² exceeds b² by the square on a straight line incommensurable in length with a (D10.2.4).

**Step 2.** Bisect b, calling its half c (1.10). Since b<a, the square c² is smaller than the square on half a (2.4). Therefore apply to a a rectangle equal to c² and deficient by a square, using 6.28. Let u and v be the resulting segments of a: the applied rectangle has sides u,v, and the deficient square has side v. Thus u+v=a and uv=c²=b²/4. By 10.18, u and v are incommensurable in length. This is the direct path: the fourth-binomial condition supplies exactly the hypothesis of the converse assertion in 10.18.

**Step 3.** Construct straight lines x and y whose squares equal ru and rv respectively (2.14). By 6.1, x²:y²=ru:rv=u:v. Since u and v are incommensurable, their equal ratio shows that x² and y² are incommensurable (10.11). Hence x and y are incommensurable in square (D10.1.2).

**Step 4.** Adding the equal areas and using u+v=a gives x²+y²=ru+rv=ra (CN2, 2.1). Since r and a are rational and commensurable in length, ra is rational (10.19). Thus the sum of the squares on x and y is rational.

**Step 5.** We next show that xy=rc. Since x²=ru, the squares r² and x² have the ratio r:u (6.1). Since y²=rv and c²=uv, the squares y² and c² also have the ratio r:u (6.1). Consequently r²:x²=y²:c² (5.11). Applying the converse of 6.22 to these squares gives r:x=y:c; therefore rc=xy (6.16).

**Step 6.** Because b=2c, b² consists of four squares equal to c² (2.4). Thus b² and c² are commensurable (D10.1.1). Since b is rational, c is rational also (10.12, D10.1.2, D10.1.3). In particular, c and r are commensurable in square (10.12, D10.1.3). On the other hand, a is commensurable in length with r and incommensurable in length with b, so r and b are incommensurable in length (10.13). Since c is commensurable in length with b, being its half, c and r are likewise incommensurable in length (D10.1.1, 10.13). Hence c and r are rational straight lines commensurable in square only.

**Step 7.** The rectangle rc is therefore medial (10.21), and Step 5 shows that xy is medial. We have thus obtained two straight lines x,y incommensurable in square, with x²+y² rational and xy medial. The direct criterion 10.39 consequently shows that x+y is irrational and is called major.

**Step 8.** Finally, by 2.4, the square on x+y equals x²+y²+2xy. Substituting the equalities established above, and using b=2c, gives (x+y)²=ra+2rc=ra+rb=r(a+b) (CN1, CN2, 2.1). Thus x+y is the side of the given area contained by r and the fourth binomial a+b. Since x+y is major by Step 7, the side of that area is the irrational straight line called major, as required.

**USED:** 1.10, 10.11, 10.12, 10.13, 10.18, 10.19, 10.21, 10.36, 10.39, 2.1, 2.14, 2.4, 5.11, 6.1, 6.16, 6.22, 6.28, CN1, CN2, D10.1.1, D10.1.2, D10.1.3, D10.2.4
**Human refs (from References field):** 10.11, 10.13, 10.18, 10.19, 10.21, 10.39, 6.1, D10.2.4
**Jaccard:** 0.348 — AI adds ['1.10', '10.12', '10.36', '2.1', '2.14', '2.4', '5.11', '6.16', '6.22', '6.28', 'CN1', 'CN2', 'D10.1.1', 'D10.1.2', 'D10.1.3']

## Proposition 10.58
**Statement:** If an area be contained by a rational straight line and the fifth binomial, the âsideâ of the area is the irrational straight line called the side of a rational plus a medial area.

**Step 1.** Let r be the given rational straight line, and let a+b be the fifth binomial, with a>b. Write st for the rectangle contained by straight lines s,t, and s² for the square on s. The terms a,b are rational and commensurable in square only; b is commensurable in length with r; and a²=b²+c², where c is incommensurable in length with a. [10.36, D10.2.4, D10.2.5]

**Step 2.** Bisect b, and put h=b/2. Apply to a a rectangle equal to h² and deficient by a square. This construction is possible because h² is less than the square on half of a. Let the resulting parts of a be u,v, so that u+v=a and uv=h²=b²/4. [1.10, 6.28] We choose the direct incommensurability criterion of 10.18, since its excess-square hypothesis is precisely the defining condition established in Step 1. Consequently, u and v are incommensurable in length. [10.18]

**Step 3.** Construct straight lines x,y,z whose squares equal the rectangles ru,rv,rh respectively. Thus x²=ru, y²=rv, and z²=rh. [2.14]

**Step 4.** Rectangles having the same altitude are proportional to their bases, so x²:y²=ru:rv=u:v. [6.1] Since u,v are incommensurable, their corresponding squares x²,y² are incommensurable. Therefore x,y are incommensurable in square. [10.11, D10.1.2]

**Step 5.** Since b is commensurable in length with r but incommensurable in length with a, r and a are incommensurable in length. [10.13] Since r and a are both rational, their squares are commensurable with the assigned rational square and hence with one another. Thus r,a are commensurable in square only. [D10.1.3, 10.12] Their rectangle ra is therefore medial. [10.21] Moreover, x²+y²=ru+rv=r(u+v)=ra, so the sum of the squares on x,y is medial. [2.1]

**Step 6.** From uv=h² we have u:h=h:v. [6.17] Taking rectangles of common altitude r gives ru:rh=rh:rv, and hence x²:z²=z²:y². [6.1] Applying the converse proportionality theorem for similar figures to these squares yields x:z=z:y. [6.22] Consequently xy=z²=rh. [6.17]

**Step 7.** The rectangle rb is rational, because r,b are rational and commensurable in length. [10.19] Since b=2h, the rectangle rb is twice rh. [6.1] Thus rh is commensurable with rb and therefore with the assigned rational square; consequently rh, and hence xy, is rational. [D10.1.1, 10.12, D10.1.4]

**Step 8.** The square on x+y equals x²+y²+2xy. [2.4] By Steps 5–7, this is ra+2rh=ra+rb=r(a+b). [6.1, CN2, 2.1] Therefore x+y is the side of the given area. [D10.1.4]

**Step 9.** The lines x,y are incommensurable in square, the sum of their squares is medial, and their rectangle is rational. These are exactly the hypotheses of 10.40. Hence x+y is irrational and is called the side of a rational plus a medial area. Since its square equals the given area, the required conclusion follows. [10.40]

**USED:** 1.10, 10.11, 10.12, 10.13, 10.18, 10.19, 10.21, 10.36, 10.40, 2.1, 2.14, 2.4, 6.1, 6.17, 6.22, 6.28, CN2, D10.1.1, D10.1.2, D10.1.3, D10.1.4, D10.2.4, D10.2.5
**Human refs (from References field):** 10.11, 10.12, 10.13, 10.18, 10.19, 10.21, 10.40, 6.1, D10.2.5
**Jaccard:** 0.391 — AI adds ['1.10', '10.36', '2.1', '2.14', '2.4', '6.17', '6.22', '6.28', 'CN2', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.1.4', 'D10.2.4']

## Proposition 10.59
**Statement:** If an area be contained by a rational straight line and the sixth binomial, the âsideâ of the area is the irrational straight line called the side of the sum of two medial areas.

**Step 1.** Write st for the rectangle contained by straight lines s and t, and s² for the square on s. Let the given area be r(a+b), where r is rational and a+b is a sixth binomial relative to r, with a>b. Its terms a and b are rational and commensurable in square only [10.36]. Neither is commensurable in length with r, and a²=b²+d² for a straight line d incommensurable in length with a [D10.2.4, D10.2.6].

**Step 2.** Bisect b, calling its half h [1.10]. Then b²=4h² [2.4]. Thus h and b are commensurable in length, and their squares are commensurable [D10.1.1]. Since a, b, and r are rational, transitivity of commensurability shows that h is rational and that a and h are each commensurable in square with r [D10.1.3, 10.12]. Moreover, b is incommensurable in length with both a and r; consequently its commensurable half h is also incommensurable in length with both [10.13].

**Step 3.** Apply to a a rectangle equal to h² and deficient by a square [6.28]. This application is possible because h²=b²/4<a²/4 [2.4]. Denote the resulting parts of a by u and v, so that u+v=a and uv=h²=b²/4. Since a² exceeds b² by the square on d, which is incommensurable in length with a, the parts u and v are incommensurable in length [10.18]. This is the direct path: 10.18 supplies the needed incommensurable division without re-establishing its deficient-square criterion.

**Step 4.** Construct straight lines x and y whose squares equal ru and rv respectively [2.14]. Rectangles of equal height are proportional to their bases, so x²:y²=ru:rv=u:v [6.1]. Since u and v are incommensurable, x² and y² are incommensurable [10.11]. Hence x and y are incommensurable in square [D10.1.2].

**Step 5.** The sum of these squares is
x²+y²=ru+rv=r(u+v)=ra [2.1].
The rational straight lines r and a are commensurable in square only, by Steps 1–2. Therefore ra, and thus x²+y², is a medial area [10.21].

**Step 6.** Using x²=ru, y²=rv, and h²=uv, comparison of rectangles of equal height gives
r²:y²=r²:rv=r:v=ru:uv=x²:h² [6.1].
The converse part of 6.22, applied to these squares, therefore gives r:y=x:h. Consequently rh=xy [6.16]. Since r and h are rational and commensurable in square only, this rectangle xy is medial [10.21].

**Step 7.** Furthermore,
(x²+y²):xy=ra:rh=a:h [6.1].
The straight lines a and h are incommensurable in length by Step 2. Therefore the medial area x²+y² is incommensurable with the medial rectangle xy [10.11].

**Step 8.** Finally,
(x+y)²=x²+y²+2xy=ra+2rh=ra+rb=r(a+b) [2.4, 2.1].
Thus x+y is the side of the given area. The lines x and y are incommensurable in square; the sum of their squares is medial; and their rectangle is medial and incommensurable with that sum. Therefore their sum x+y is irrational and is precisely the straight line called the side of the sum of two medial areas [10.41]. This proves the proposition.

**USED:** 1.10, 10.11, 10.12, 10.13, 10.18, 10.21, 10.36, 10.41, 2.1, 2.14, 2.4, 6.1, 6.16, 6.22, 6.28, D10.1.1, D10.1.2, D10.1.3, D10.2.4, D10.2.6
**Human refs (from References field):** 10.11, 10.13, 10.21, 10.41, 6.1
**Jaccard:** 0.250 — AI adds ['1.10', '10.12', '10.18', '10.36', '2.1', '2.14', '2.4', '6.16', '6.22', '6.28', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.2.4', 'D10.2.6']

## Proposition 10.60
**Statement:** The square on the binomial straight line applied to a rational straight line produces as breadth the first binomial.

**Step 1.** Let the given binomial be a+b, where a>b are rational straight lines commensurable in square only, as specified in 10.36. Let r be the rational straight line to which its square is applied. Products below denote rectangles, and squares denote square areas. Path choice: the applications of a² and b² will furnish a commensurable division, so the criterion in 10.17 gives the defining square-difference condition directly.

**Step 2.** Choose straight lines u, v, w such that ru=a², rv=b², and rw=ab. These applications can be constructed by fourth proportionals (6.12, 6.16). Put x=u+v and y=2w. By distributivity of rectangles and the square-of-a-sum identity,
r(x+y)=ru+rv+2rw=a²+b²+2ab=(a+b)² (2.1, 2.4).
Thus x+y is the breadth produced by applying the given square to r.

**Step 3.** Since a and b are rational, a² and b² are rational areas (D10.1.3, D10.1.4). Their applications to r therefore give u and v each commensurable in length with r (10.20), so u and v are commensurable in length with one another (10.12). Moreover, a² and b² are commensurable; hence their sum is commensurable with a² (10.15), and consequently with the assigned rational square (10.12). Thus a²+b² is rational (D10.1.4). Since rx=a²+b², x is rational and commensurable in length with r (10.20).

**Step 4.** Because a and b are rational and commensurable in square only, ab is the square on a medial straight line (10.21). Its application to r gives w rational and incommensurable in length with r (10.22). Since y=2w, y and w are commensurable in length (D10.1.1); therefore y is incommensurable in length with r (10.13). Also, y²=4w² by 2.4, so y² is commensurable with w² (D10.1.1), and hence with the assigned rational square (10.12). Consequently y is rational (D10.1.3).

**Step 5.** Since x and y are rational, their squares are commensurable with the assigned rational square and therefore with one another (D10.1.3, 10.12). Thus x and y are commensurable in square (D10.1.2). But x is commensurable in length with r, whereas y is not; hence x and y are incommensurable in length (10.13). Their sum x+y is therefore a binomial, with terms x and y (10.36).

**Step 6.** Rectangles having the same height are proportional to their bases (6.1). Using ru=a², rv=b², and rw=ab, we obtain
u:w=a²:ab=a:b,
and
w:v=ab:b²=a:b.
Thus u:w=w:v (5.11), and therefore uv=w² (6.17). Since y=2w and y²=4w², the rectangle uv equals the fourth part of y² (2.4).

**Step 7.** Since a>b, Proposition 2.7 gives
a²+b²=2ab+(a−b)²>2ab (CN5).
Consequently rx>ry, and therefore x>y, since these rectangles have the same height r (6.1). Now x=u+v, so the rectangle uv is applied to x with deficiency the square v²: indeed, xv=uv+v² (2.1). By Step 6 this applied rectangle equals the fourth part of y², and its division of x is into the commensurable lengths u and v established in Step 3. Proposition 10.17 therefore shows that x² exceeds y² by the square on a straight line commensurable in length with x.

**Step 8.** The breadth x+y is a binomial; its greater term is x; x is commensurable in length with the rational straight line r; and x² exceeds y² by the square on a straight line commensurable in length with x. These are precisely the conditions defining a first binomial relative to r (D10.2.1). Therefore the square on the binomial straight line, applied to a rational straight line, produces as breadth the first binomial.

**USED:** 10.12, 10.13, 10.15, 10.17, 10.20, 10.21, 10.22, 10.36, 2.1, 2.4, 2.7, 5.11, 6.1, 6.12, 6.16, 6.17, CN5, D10.1.1, D10.1.2, D10.1.3, D10.1.4, D10.2.1
**Human refs (from References field):** 10.11, 10.13, 10.15, 10.17, 10.20, 10.21, 10.22, 10.36, 10.53, 6.1, 6.17, D10.2.1
**Jaccard:** 0.417 — AI adds ['10.12', '2.1', '2.4', '2.7', '5.11', '6.12', '6.16', 'CN5', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.1.4']; Human adds ['10.11', '10.53']

## Proposition 10.61
**Statement:** The square on the first bimedial straight line applied to a rational straight line produces as breadth the second binomial.

**Step 1.** Let L be a first bimedial straight line, and let r be the rational straight line to which its square is applied. By 10.37, write L = a + b, where a and b are medial straight lines commensurable in square only, and the rectangle ab is rational. Since a and b are unequal, name them so that a > b. Products below denote rectangular areas, and squares denote square areas.

**Step 2.** Construct straight lines p, q, t satisfying r:a = a:p, r:b = b:q, and r:a = b:t (6.12). The equivalence between proportional straight lines and equal rectangles gives
rp = a², rq = b², rt = ab
(6.16).

**Step 3.** Put x = p + q and y = 2t. By distribution of rectangles over their divided sides (2.1),
rx = a² + b², ry = 2ab.
Consequently,
r(x + y) = a² + b² + 2ab = (a + b)² = L²
(2.1, 2.4). Thus x + y is the breadth produced by applying the square on L to r.

**Step 4.** Since a and b are medial, applying their squares to r makes p and q rational and incommensurable in length with r (10.22). Since ab is rational, t is rational and commensurable in length with r (10.20). Moreover,
p:q = rp:rq = a²:b²
(6.1). The areas a² and b² are commensurable (D10.1.2), so p and q are commensurable in length (10.11). Therefore x = p + q is commensurable in length with p (10.15), and hence incommensurable in length with r (10.13). Also y = t + t is commensurable in length with t (10.15), and therefore with r (10.12).

**Step 5.** A straight line commensurable in length with a rational straight line is itself rational: 10.9 and 10.6 make their squares commensurable, and 10.12 transfers commensurability to the square on the assigned rational straight line (D10.1.3). Thus x and y are rational. Their squares are therefore commensurable with one another (D10.1.3, 10.12, D10.1.2). But x and y are incommensurable in length, since y is commensurable in length with r whereas x is not (10.13). Hence x + y is a binomial (10.36).

**Step 6.** Cutting a into b and a − b gives
 a² + b² = 2ab + (a − b)²
(2.7). Since a > b, the area on the left exceeds 2ab (CN5). Thus rx > ry, and consequently x > y (6.1, 5.14). Accordingly, x is the greater term of our binomial and y the lesser.

**Step 7.** Ratios of rectangles having the same height give
p:t = rp:rt = a²:ab = a:b,
and
t:q = rt:rq = ab:b² = a:b
(6.1). Hence p:t = t:q (5.11), so the rectangle-proportion equivalence already used in Step 2 gives pq = t² (6.16). Since y = 2t, we have y² = 4t² (2.4). Therefore pq is one fourth of the square on y.

**Step 8.** Apply the rectangle pq to x = p + q, placing its side p along x and taking q as its height. Its deficiency is the square on the remaining segment q. Thus a rectangle equal to one fourth of the square on y has been applied to the greater line x, deficient by a square, and its division of x is into the commensurable parts p and q. This is precisely the commensurable-division criterion of 10.17—the direct route here because that division has already been obtained. Hence the square on x exceeds the square on y by the square on a straight line commensurable in length with x (10.17).

**Step 9.** The breadth x + y is therefore a binomial whose greater term x has the required commensurable square-difference, and whose lesser term y is commensurable in length with the rational straight line r. By D10.2.2, it is a second binomial. Thus the square on a first bimedial straight line, applied to a rational straight line, produces as breadth the second binomial.

**USED:** 10.11, 10.12, 10.13, 10.15, 10.17, 10.20, 10.22, 10.36, 10.37, 10.6, 10.9, 2.1, 2.4, 2.7, 5.11, 5.14, 6.1, 6.12, 6.16, CN5, D10.1.2, D10.1.3, D10.2.2
**Human refs (from References field):** 10.11, 10.13, 10.15, 10.17, 10.20, 10.21, 10.22, 10.23, 10.36, 10.37, 6.1, D10.2.2
**Jaccard:** 0.400 — AI adds ['10.12', '10.6', '10.9', '2.1', '2.4', '2.7', '5.11', '5.14', '6.12', '6.16', 'CN5', 'D10.1.2', 'D10.1.3']; Human adds ['10.21', '10.23']

## Proposition 10.62
**Statement:** The square on the second bimedial straight line applied to a rational straight line produces as breadth the third binomial.

**Step 1.** Let L be a second bimedial straight line, and let r be the rational straight line to which its square is to be applied. By the characterization in 10.38, write L=a+b, where a and b are medial straight lines commensurable in square only, and the rectangle ab is medial. Products below denote rectangular areas.

**Step 2.** By fourth proportionals, construct straight lines u, v, and t such that ru=a², rv=b², and rt=ab (6.12, 6.16). Each of these three areas is medial. Consequently, u, v, and t are rational straight lines, each incommensurable in length with r (10.22).

**Step 3.** Comparing rectangles of equal height gives
u:v=a²:b²,
u:t=a²:ab=a:b,
and t:v=ab:b²=a:b
(6.1). Since a² and b² are commensurable, u and v are commensurable in length; since a and b are incommensurable in length, u and t are incommensurable in length (D10.1.2, 10.11). Moreover, u:t=t:v (5.11), so uv=t² (6.16).

**Step 4.** Put U=u+v and W=2t. Since u and v are commensurable, U is commensurable in length with u (10.15); and W is commensurable in length with t, which measures it twice (D10.1.1). Commensurability in length implies commensurability of the squares, by 10.9 and 10.6. Therefore U² is commensurable with u², and W² with t². As u and t are rational, it follows by transitivity of commensurability that U and W are rational, and hence commensurable in square with one another (10.12, D10.1.3, D10.1.2).

**Step 5.** Because U is commensurable in length with u, while u is incommensurable in length with r, U is incommensurable in length with r. Likewise, W is incommensurable in length with r (10.13). Furthermore, u is incommensurable in length with t; thus U is incommensurable in length with t, and consequently with W (10.13). Hence U and W are rational straight lines commensurable in square only, so U+W is a binomial (10.36).

**Step 6.** The lines u and v are unequal, since their applied areas are the unequal squares on a and b. Applying 2.5 to U divided into the unequal parts u and v shows that uv is less than the square on half of U: the latter square equals uv together with a nonzero square (2.5, CN5). Since uv=t², we obtain t<U/2, and therefore W<U; comparison of sides follows from comparison of their squares (2.4, CN5).

**Step 7.** Place the rectangle uv on the part u of U=u+v, with height v. It is then applied to U deficient by the square on v. Its area is t², which is one quarter of W² (Step 3; 2.4). Its subdivision of U is into the commensurable parts u and v. Thus 10.17 shows that U² exceeds W² by the square on a straight line commensurable in length with U. This is the direct path through 10.17: the applications of the two component squares have already supplied exactly its required commensurable subdivision.

**Step 8.** By distribution of rectangles and the square-of-a-sum identity,
r(U+W)=ru+rv+2rt=a²+b²+2ab=(a+b)²=L²
(2.1, 2.4). Hence U+W is the breadth produced when the square on L is applied to r.

**Step 9.** This breadth is a binomial whose greater term is U; the excess U²−W² is the square on a straight line commensurable in length with U, and neither U nor W is commensurable in length with the rational line r. These are precisely the common square-difference condition and the third-binomial alternative in D10.2.1 and D10.2.3. Therefore the square on a second bimedial straight line, applied to a rational straight line, produces as breadth the third binomial.

**USED:** 10.11, 10.12, 10.13, 10.15, 10.17, 10.22, 10.36, 10.38, 10.6, 10.9, 2.1, 2.4, 2.5, 5.11, 6.1, 6.12, 6.16, CN5, D10.1.1, D10.1.2, D10.1.3, D10.2.1, D10.2.3
**Human refs (from References field):** 10.11, 10.12, 10.13, 10.15, 10.22, 10.23, 10.36, 10.38, 6.1, D10.2.3
**Jaccard:** 0.375 — AI adds ['10.17', '10.6', '10.9', '2.1', '2.4', '2.5', '5.11', '6.12', '6.16', 'CN5', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.2.1']; Human adds ['10.23']

## Proposition 10.63
**Statement:** The square on the major straight line applied to a rational straight line produces as breadth the fourth binomial.

**Step 1.** Let m be a major straight line and r any rational straight line. By the characterization of the major straight line, write m = a + b, where a² and b² are incommensurable areas, a² + b² is rational, and the rectangle ab is medial. The lines a and b are unequal; interchange their names if necessary so that a > b. Throughout, products denote rectangular areas. [10.39, D10.1.2]

**Step 2.** Construct straight lines u, v, z satisfying
ru = a², rv = b², rz = ab.
These constructions are obtained by fourth proportionals and the equality of the corresponding rectangles. Set x = u + v and y = 2z. Then
rx = a² + b², ry = 2ab,
and consequently
r(x + y) = a² + b² + 2ab = (a + b)² = m².
Thus x + y is the breadth produced by applying the square on m to r. [6.12, 6.16, 2.1, 2.4]

**Step 3.** Since rx = a² + b² is rational, x is rational and commensurable in length with r. Since rz = ab is medial, z is rational and incommensurable in length with r. [10.20, 10.22]

**Step 4.** Since y = 2z, the lines y and z are commensurable in length, and y² = 4z². Their squares are therefore commensurable; because z is rational, y is rational also. Moreover, y is incommensurable in length with r, since it is commensurable with z, which is incommensurable with r. Since x is commensurable in length with r, y is likewise incommensurable in length with x. But the rational lines x and y are commensurable in square, their squares being commensurable with the square on the assigned rational line. Hence x and y are rational straight lines commensurable in square only, and x + y is a binomial. [D10.1.1, 2.4, 10.12, D10.1.3, D10.1.2, 10.13, 10.36]

**Step 5.** Since a > b,
a² + b² = 2ab + (a − b)² > 2ab.
Thus rx > ry. Rectangles of the same altitude are proportional to their bases, so x > y. Therefore x is the greater term of the binomial. [2.7, CN5, 6.1, 5.14]

**Step 6.** The rectangles ru and rv have the same altitude, so
u : v = a² : b².
Since a² and b² are incommensurable, u and v are incommensurable in length. [6.1, 10.11]

**Step 7.** Again, comparison of rectangles of the same altitude gives
u : z = a² : ab = a : b,
and
z : v = ab : b² = a : b.
Hence u : z = z : v, and therefore uv = z². By Step 4, this is one fourth of y². [6.1, 5.11, 6.17, 2.4]

**Step 8.** Apply the rectangle uv to x = u + v along the segment u, with breadth v. It is deficient by the square on v, since xv = uv + v². This rectangle equals one fourth of the square on y, and it divides x into the incommensurable parts u and v. Path choice: 10.18 is the direct criterion here, because the required incommensurable division has already been established. Since x > y, that proposition shows that
x² = y² + d²
for a straight line d incommensurable in length with x. [2.1, 10.18]

**Step 9.** The breadth x + y is a binomial whose greater term x is commensurable in length with the rational line r, while the square on x exceeds the square on y by the square on a line incommensurable in length with x. It is therefore a fourth binomial. Since r(x + y) = m², the square on the major straight line applied to the rational straight line produces as breadth the fourth binomial. [D10.2.4]

**USED:** 10.11, 10.12, 10.13, 10.18, 10.20, 10.22, 10.36, 10.39, 2.1, 2.4, 2.7, 5.11, 5.14, 6.1, 6.12, 6.16, 6.17, CN5, D10.1.1, D10.1.2, D10.1.3, D10.2.4
**Human refs (from References field):** 10.11, 10.13, 10.18, 10.20, 10.22, 10.36, 10.39, 6.1, D10.2.4
**Jaccard:** 0.409 — AI adds ['10.12', '2.1', '2.4', '2.7', '5.11', '5.14', '6.12', '6.16', '6.17', 'CN5', 'D10.1.1', 'D10.1.2', 'D10.1.3']

## Proposition 10.64
**Statement:** The square on the side of a rational plus a medial area applied to a rational straight line produces as breadth the fifth binomial.

**Step 1.** Let r be the given rational straight line, s the given side of a rational plus a medial area, and z the breadth obtained by applying s² to r, so that rz = s². Products below denote rectangular areas (D2.1). By the designation in 10.40, write s = a + b, with a > b, where a² and b² are incommensurable, M = a² + b² is medial, and R = ab is rational.

**Step 2.** Choose breadths p, q, h such that rp = a², rq = b², and rh = ab; these area applications are obtainable by fourth proportionals (6.12, 6.16). Put X = p + q and Y = 2h. By 2.1, rX = M and rY = 2R. Consequently, by 2.4 and 2.1,
 r(X + Y) = a² + b² + 2ab = (a + b)² = s².
The rectangles r(X + Y) and rz are therefore equal, and their common altitude gives z = X + Y (6.1).

**Step 3.** Since the medial area M is applied to the rational line r, X is rational and incommensurable in length with r (10.22). Also, 2R is commensurable with R, since R measures it (D10.1.1). Because R is rational, 2R is rational as well (10.12, D10.1.4). Applying this rational area to r shows that Y is rational and commensurable in length with r (10.20).

**Step 4.** Since X and Y are rational, their squares are commensurable with the square on the assigned rational line, and hence with one another (D10.1.2, D10.1.3, 10.12). But X and Y are incommensurable in length: Y is commensurable with r, whereas X is incommensurable with r (10.13). Thus X and Y are rational straight lines commensurable in square only, and X + Y is a binomial (10.36).

**Step 5.** Applying 2.7 to a divided into b and a − b gives
 a² + b² = 2ab + (a − b)².
Since a > b, this makes M greater than 2R (CN5). Therefore rX > rY, and consequently X > Y (6.1). Thus Y is the lesser term of the binomial.

**Step 6.** Rectangles of equal altitude are proportional to their bases, so
 p : q = a² : b²
by 6.1. Since a² and b² are incommensurable, p and q are incommensurable in length (10.11). Moreover, again by 6.1,
 p : h = a² : ab = a : b,
 h : q = ab : b² = a : b.
Hence p : h = h : q (5.11), and therefore pq = h² (6.17).

**Step 7.** Since Y = 2h, 2.4 gives Y² = 4h² = 4pq. The rectangle contained by p and q is thus one quarter of the square on Y. Applied to X = p + q, this rectangle is deficient by the square on q: the rectangle Xq consists of pq together with q² (2.1). Its division of X is into the incommensurable parts p and q. **Path choice:** use 10.18 directly, since its incommensurable-division hypothesis is precisely what Step 6 supplies. As X > Y, that proposition shows that X² exceeds Y² by the square on a straight line incommensurable in length with X.

**Step 8.** We have proved that X + Y is a binomial, that its lesser term Y is commensurable in length with the given rational line r, and that the excess of the square on its greater term over the square on its lesser term is the square on a straight line incommensurable in length with the greater. Therefore X + Y is a fifth binomial (D10.2.5). Since z = X + Y, the square on the side of a rational plus a medial area, applied to a rational straight line, produces as breadth the fifth binomial.

**USED:** 10.11, 10.12, 10.13, 10.18, 10.20, 10.22, 10.36, 10.40, 2.1, 2.4, 2.7, 5.11, 6.1, 6.12, 6.16, 6.17, CN5, D10.1.1, D10.1.2, D10.1.3, D10.1.4, D10.2.5, D2.1
**Human refs (from References field):** 10.13, 10.18, 10.20, 10.22, 10.36, 10.40
**Jaccard:** 0.261 — AI adds ['10.11', '10.12', '2.1', '2.4', '2.7', '5.11', '6.1', '6.12', '6.16', '6.17', 'CN5', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.1.4', 'D10.2.5', 'D2.1']

## Proposition 10.65
**Statement:** The square on the side of the sum of two medial areas applied to a rational straight line produces as breadth the sixth binomial.

**Step 1.** Let s be the side of the sum of two medial areas, and let r be the rational straight line to which its square is applied. By the defining description in 10.41, write s = x + y, with x > y, where x² and y² are incommensurable, M = x² + y² is medial, and N = xy is medial and incommensurable with M. Here u² denotes the square on u, and uv the rectangle contained by u and v. [10.41]

**Step 2.** Apply x², y², and N to r as rectangles, obtaining breadths c, d, and e respectively, so that rc = x², rd = y², and re = N. These applications can be made by applying their triangular halves and doubling. Put a = c + d and b = 2e. Then ra = M and rb = 2N; consequently r(a + b) = M + 2N = (x + y)² = s². Thus the breadth whose character must be proved is a + b. [1.44, 2.1, 2.4]

**Step 3.** Since M and N are medial areas, their applications to r show that a and e are rational straight lines, each incommensurable in length with r. [10.22] Since b = 2e, b and e are commensurable in length, and b² = 4e². Thus b is also rational: its square is commensurable with e² and hence with the square on the assigned rational straight line. Moreover, b is incommensurable in length with r because e is. [D10.1.1, 2.4, D10.1.2, D10.1.3, 10.12, 10.13]

**Step 4.** Rectangles with the same altitude are proportional to their bases, so a:e = M:N. Since M and N are incommensurable, a and e are incommensurable in length. [6.1, 10.11] Because b is commensurable in length with e, a and b are likewise incommensurable in length. [10.13] But a and b are rational, so their squares are commensurable with one another. Hence a and b are rational straight lines commensurable in square only, and a + b is a binomial. [D10.1.2, D10.1.3, 10.12, 10.36]

**Step 5.** Since x > y, the identity x² + y² = 2xy + (x − y)² gives M > 2N. [2.7, CN5] Therefore ra > rb, and consequently a > b. Thus a is the greater term of this binomial. [6.1, 5.14]

**Step 6.** The applications of x² and y² give c:d = x²:y². Therefore c and d are incommensurable in length. [6.1, 10.11] Furthermore, comparison of rectangles with common altitudes gives c:e = x²:xy = x:y and e:d = xy:y² = x:y. Hence c:e = e:d, and therefore cd = e² = b²/4. [6.1, 5.11, 6.17, 2.4]

**Step 7.** Since a = c + d, the rectangle cd is applied to a deficient by the square on d: adjoining d² to it fills the rectangle ad. [2.1] This deficient rectangle equals the fourth part of b² and divides a into the incommensurable parts c and d. We use 10.18 directly, because its incommensurable-segment hypothesis is exactly what this application supplies. Since a > b, that proposition shows that a² exceeds b² by the square on a straight line incommensurable in length with a. [10.18]

**Step 8.** The breadth a + b is therefore a binomial whose greater term is a, neither of whose terms is commensurable in length with r, and whose greater term exceeds the lesser in square by the square on a straight line incommensurable in length with the greater. By the definition, it is a sixth binomial. Since r(a + b) = s², the square on the side of the sum of two medial areas, applied to a rational straight line, produces as breadth a sixth binomial. [D10.2.6]

**USED:** 1.44, 10.11, 10.12, 10.13, 10.18, 10.22, 10.36, 10.41, 2.1, 2.4, 2.7, 5.11, 5.14, 6.1, 6.17, CN5, D10.1.1, D10.1.2, D10.1.3, D10.2.6
**Human refs (from References field):** 10.11, 10.22, 10.36, 10.41, 6.1
**Jaccard:** 0.250 — AI adds ['1.44', '10.12', '10.13', '10.18', '2.1', '2.4', '2.7', '5.11', '5.14', '6.17', 'CN5', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.2.6']

## Proposition 10.66
**Statement:** A straight line commensurable in length with a binomial straight line is itself also binomial and the same in order.

**Step 1.** Fix the assigned rational straight line r, relative to which rationality and binomial order are understood (D10.1.3, D10.2.1–D10.2.6). Let x be a binomial, and let y be commensurable in length with x. Write x = a + b, where a > b and a, b are rational straight lines commensurable in square only, as in 10.36. We take the direct route: transfer the terms proportionally, then use 10.14 to preserve the square-excess condition determining the order. Write a² for the square on a, and similarly for other lines.

**Step 2.** Divide y similarly to the division x = a + b, obtaining y = c + d with a:b = c:d (6.10). Alternating gives a:c = b:d (5.16), and taking the sums of antecedents and consequents gives
x:y = (a + b):(c + d) = a:c = b:d
(5.12). Since a > b, the proportion a:c = b:d also gives c > d (5.14).

**Step 3.** Since x and y are commensurable in length, the proportions x:y = a:c and x:y = b:d show that a and c, and likewise b and d, are commensurable in length (10.11). Since a and b are incommensurable in length, the proportion a:b = c:d shows that c and d are incommensurable in length (10.11). Here 10.11 is the natural direct choice because the required proportions are already established.

**Step 4.** The length-commensurability of a with c implies that a²:c² is the ratio of a square number to a square number (10.9); hence a² and c² are commensurable (10.6). Likewise b² and d² are commensurable. Since a and b are rational, a² and b² are each commensurable with r² (D10.1.2, D10.1.3). Therefore c² and d² are each commensurable with r², and consequently with one another (10.12). Thus c and d are rational and commensurable in square; by Step 3 they are incommensurable in length (D10.1.2, D10.1.3). Their sum y is therefore binomial (10.36).

**Step 5.** Because a and c are commensurable in length, 10.12 applied in both directions shows that a is commensurable in length with r if and only if c is. Similarly, b is commensurable in length with r if and only if d is (10.12). Consequently, whether the greater term, the lesser term, or neither term is commensurable in length with r is unchanged.

**Step 6.** Apply 10.14 to a:b = c:d. If a² exceeds b² by the square on a line commensurable in length with a, then c² exceeds d² by the square on a line commensurable in length with c. If instead the excess for a, b is the square on a line incommensurable in length with a, then the excess for c, d is the square on a line incommensurable in length with c (10.14). Thus the square-excess condition is also unchanged.

**Step 7.** Steps 5 and 6 preserve both conditions defining each binomial order. Hence, if x is a first, second, or third binomial, y is respectively a first, second, or third binomial (D10.2.1, D10.2.2, D10.2.3). If x is a fourth, fifth, or sixth binomial, y is respectively a fourth, fifth, or sixth binomial (D10.2.4, D10.2.5, D10.2.6). Therefore a straight line commensurable in length with a binomial straight line is itself binomial and the same in order.

**USED:** 10.11, 10.12, 10.14, 10.36, 10.6, 10.9, 5.12, 5.14, 5.16, 6.10, D10.1.2, D10.1.3, D10.2.1, D10.2.2, D10.2.3, D10.2.4, D10.2.5, D10.2.6
**Human refs (from References field):** 10.11, 10.12, 10.13, 10.14, 10.36, 5.11, 5.16, 5.19, 6.12, D10.2.1, D10.2.2, D10.2.3, D10.2.4, D10.2.5, D10.2.6
**Jaccard:** 0.500 — AI adds ['10.6', '10.9', '5.12', '5.14', '6.10', 'D10.1.2', 'D10.1.3']; Human adds ['10.13', '5.11', '5.19', '6.12']

## Proposition 10.67
**Statement:** A straight line commensurable in length with a bimedial straight line is itself also bimedial and the same in order.

**Step 1.** Let a be a bimedial straight line, and let b be commensurable in length with a. Fix a rational straight line r [D10.1.3]. Path choice: pass through the binomial breadths obtained by applying the squares to r, so that the already established preservation of binomial order [10.66] can be used without reconstructing the bimedial terms.

**Step 2.** Construct straight lines x and y such that r:a = a:x and r:b = b:y [6.12]. Then the rectangle contained by r and x equals the square on a, and the rectangle contained by r and y equals the square on b [6.17]. Thus x and y are the breadths obtained by applying these squares to the same rational straight line r.

**Step 3.** Since a and b are commensurable in length, their squares have the ratio of a square number to a square number [10.9], and therefore those squares are commensurable areas [10.6]. The rectangles contained by r, x and by r, y have the same height r, so their ratio is x:y [6.1]. Consequently, the ratio of the square on a to the square on b is also x:y. Hence x and y are commensurable in length [10.11].

**Step 4.** Suppose first that a is a first bimedial. Its square, applied to the rational straight line r, produces a second binomial as breadth; hence x is a second binomial [10.61]. Since y is commensurable in length with x, y is likewise a second binomial [10.66]. The side of the area contained by a rational straight line and a second binomial is a first bimedial [10.55]. But the rectangle contained by r and y equals the square on b by Step 2. Therefore b is a first bimedial, of the same order as a.

**Step 5.** Suppose instead that a is a second bimedial. Its square, applied to r, produces a third binomial as breadth; hence x is a third binomial [10.62]. Since y is commensurable in length with x, y is likewise a third binomial [10.66]. The side of the area contained by a rational straight line and a third binomial is a second bimedial [10.56]. Since the rectangle contained by r and y equals the square on b, b is therefore a second bimedial, again of the same order as a. Thus, in either case, a straight line commensurable in length with a bimedial straight line is itself bimedial and the same in order.

**USED:** 10.11, 10.55, 10.56, 10.6, 10.61, 10.62, 10.66, 10.9, 6.1, 6.12, 6.17, D10.1.3
**Human refs (from References field):** 10.11, 10.23, 10.37, 10.38, 5.11, 5.16, 5.19
**Jaccard:** 0.056 — AI adds ['10.55', '10.56', '10.6', '10.61', '10.62', '10.66', '10.9', '6.1', '6.12', '6.17', 'D10.1.3']; Human adds ['10.23', '10.37', '10.38', '5.11', '5.16', '5.19']

## Proposition 10.68
**Statement:** A straight line commensurable with a major straight line is itself also major.

**Step 1.** Let a be a major straight line, and let b be commensurable in length with a. Set out a rational straight line r. Construct straight lines x and y such that r:a = a:x and r:b = b:y (6.12). Then the rectangles contained by r, x and by r, y equal the squares on a and b, respectively (6.17). Write these equalities as rx = a² and ry = b².

**Step 2.** Since applying the square on a major straight line to a rational straight line produces a fourth binomial as breadth, x is a fourth binomial (10.63). We use this directly available representation rather than reconstructing the terms of the major line.

**Step 3.** Because a and b are commensurable in length, their squares have the ratio of a square number to a square number (10.9). Therefore a² and b² are commensurable areas (10.6).

**Step 4.** The rectangles rx and ry have the same height r, so they are to one another as their bases x and y (6.1). Consequently,
 a²:b² = rx:ry = x:y.
Since the first two magnitudes are commensurable, x and y are commensurable in length (10.11). A straight line commensurable in length with a binomial is itself binomial and of the same order; hence y, like x, is a fourth binomial (10.66).

**Step 5.** The rectangle ry is thus contained by a rational straight line and a fourth binomial. Its square-root side is therefore major (10.57). But ry is the square on b, so that side is b. Hence a straight line commensurable with a major straight line is itself also major.

**USED:** 10.11, 10.57, 10.6, 10.63, 10.66, 10.9, 6.1, 6.12, 6.17
**Human refs (from References field):** 10.11, 10.23, 10.39, 5.11, 5.16, 5.18, 6.20
**Jaccard:** 0.067 — AI adds ['10.57', '10.6', '10.63', '10.66', '10.9', '6.1', '6.12', '6.17']; Human adds ['10.23', '10.39', '5.11', '5.16', '5.18', '6.20']

## Proposition 10.69
**Statement:** A straight line commensurable with the side of a rational plus a medial area is itself also the side of a rational plus a medial area.

**Step 1.** Let a be the side of a rational plus a medial area, and let b be commensurable in length with a. Fix the assigned rational straight line r [D10.1.3]. We choose the square-application route: 10.64 directly converts the given kind into a fifth binomial, avoiding any reconstruction of its constituent terms.

**Step 2.** Construct straight lines u and v such that r:a = a:u and r:b = b:v [6.12]. Then the rectangle contained by r and u equals the square on a, and the rectangle contained by r and v equals the square on b [6.17]. Thus u is the breadth obtained by applying the square on a to the rational straight line r; consequently u is a fifth binomial [10.64].

**Step 3.** Since a and b are commensurable in length, their squares have the ratio of a square number to a square number [10.9]. Therefore the squares on a and b are commensurable areas [10.6].

**Step 4.** The rectangles contained by r, u and by r, v have the same height r, so they are to one another as their bases u and v [6.1]. Using their equalities with the respective squares from Step 2, we obtain
(square on a):(square on b) = u:v.
Hence u and v are commensurable in length [10.11]. Since u is a fifth binomial, v is also a fifth binomial: a line commensurable in length with a binomial is binomial and the same in order [10.66].

**Step 5.** The rectangle contained by the rational straight line r and the fifth binomial v has as its side a straight line of the kind called the side of a rational plus a medial area [10.58]. But this rectangle equals the square on b by Step 2, so b is its side. Therefore b is itself the side of a rational plus a medial area, as required.

**USED:** 10.11, 10.58, 10.6, 10.64, 10.66, 10.9, 6.1, 6.12, 6.17, D10.1.3
**Human refs (from References field):** 10.40
**Jaccard:** 0.000 — AI adds ['10.11', '10.58', '10.6', '10.64', '10.66', '10.9', '6.1', '6.12', '6.17', 'D10.1.3']; Human adds ['10.40']

## Proposition 10.70
**Statement:** A straight line commensurable with the side of the sum of two medial areas is the side of the sum of two medial areas.

**Step 1.** Let a be the side of the sum of two medial areas, and let b be commensurable in length with a. Fix the assigned rational straight line r [D10.1.3]. We use the sixth-binomial correspondence, since 10.65 applies directly to the square on the given kind of straight line, avoiding reconstruction of its defining terms.

**Step 2.** Construct straight lines x and y such that r:a = a:x and r:b = b:y [6.12]. Then the rectangle contained by r and x equals the square on a, and the rectangle contained by r and y equals the square on b [6.17]. Thus x and y are the respective breadths obtained by applying these squares to r.

**Step 3.** Since a is the side of the sum of two medial areas and r is rational, the breadth x is a sixth binomial straight line [10.65].

**Step 4.** Since a and b are commensurable in length, their squares have the ratio of a square number to a square number [10.9], and therefore those squares are commensurable [10.6]. The rectangles contained by r, x and by r, y have the same height r, so their ratio is x:y [6.1]. By their equalities with the squares established in Step 2, the square on a is to the square on b as x is to y. Consequently x and y are commensurable in length [10.11].

**Step 5.** A straight line commensurable in length with a binomial is itself binomial and of the same order. Since x is a sixth binomial, y is therefore also a sixth binomial [10.66].

**Step 6.** The rectangle contained by the rational straight line r and the sixth binomial y has as its side the side of the sum of two medial areas [10.59]. But this rectangle equals the square on b by Step 2 [6.17]. Hence b is the side of the sum of two medial areas, as required.

**USED:** 10.11, 10.59, 10.6, 10.65, 10.66, 10.9, 6.1, 6.12, 6.17, D10.1.3
**Human refs (from References field):** 10.41
**Jaccard:** 0.000 — AI adds ['10.11', '10.59', '10.6', '10.65', '10.66', '10.9', '6.1', '6.12', '6.17', 'D10.1.3']; Human adds ['10.41']

## Proposition 10.71
**Statement:** If a rational and a medial area be added together, four irrational straight lines arise, namely a binomial or a first bimedial or a major or a side of a rational plus a medial area.

**Step 1.** Let R be a rational area and M a medial area, and let r be the assigned rational straight line. Apply R and M to r, obtaining breadths a and b respectively. By 10.20, a is rational and commensurable in length with r; by 10.22, b is rational and incommensurable in length with r. Thus, writing xy for the rectangle contained by x and y, we have ra = R and rb = M. The direct path is to classify the combined breadth and then use the forward rectangle-to-side propositions, rather than their converses.

**Step 2.** Since a and b are rational, their squares are each commensurable with the square on r (D10.1.3), and hence with one another (10.12). Thus a and b are commensurable in square (D10.1.2). But a is commensurable in length with r, whereas b is not, so a and b are incommensurable in length (10.13). Therefore a + b is a binomial (10.36), and in particular a and b are unequal.

**Step 3.** By 2.1,
 r(a + b) = ra + rb = R + M.
Construct a square equal to this area, and denote its side by s (2.14). Also let c be the side of a square equal to the difference between the squares on the greater and lesser of a and b (2.14). The line c is either commensurable or incommensurable in length with the greater term (D10.1.1). We now distinguish which term is greater and which of these two alternatives holds.

**Step 4.** Suppose a > b. The greater term a is commensurable in length with r. If c is commensurable in length with a, then a + b is a first binomial (D10.2.1), and the side s of the rectangle r(a + b) is a binomial (10.54). If c is incommensurable in length with a, then a + b is a fourth binomial (D10.2.4), and s is a major straight line (10.57).

**Step 5.** Suppose b > a. The lesser term a is commensurable in length with r. If c is commensurable in length with b, then a + b is a second binomial (D10.2.2), and s is a first bimedial (10.55). If c is incommensurable in length with b, then a + b is a fifth binomial (D10.2.5), and s is the straight line called the side of a rational plus a medial area (10.58). These cases exhaust the possibilities, since exactly one of a and b is commensurable in length with r.

**Step 6.** All four possibilities occur. Indeed, 10.48, 10.49, 10.51, and 10.52 construct first, second, fourth, and fifth binomials respectively. In each construction, relative to the assigned rational line r, one term u is commensurable in length with r, by the corresponding definition (D10.2.1, D10.2.2, D10.2.4, D10.2.5). The other term v is rational and incommensurable in length with u, as required for a binomial (10.36); consequently v is incommensurable in length with r (10.13). The rectangle ru is therefore rational (10.19), while rv is medial (10.21), since r and v are rational and commensurable in square only (D10.1.3, D10.1.2, 10.12). By 2.1, the rectangle r(u + v) is their sum. Its side is, respectively, a binomial, a first bimedial, a major, or a side of a rational plus a medial area (10.54, 10.55, 10.57, 10.58).

**Step 7.** Hence adding a rational area and a medial area yields a square-side of one of precisely these four kinds: a binomial, a first bimedial, a major, or a side of a rational plus a medial area. Each kind occurs, and each is irrational by the corresponding rectangle-to-side proposition (10.54, 10.55, 10.57, 10.58). This proves the proposition.

**USED:** 10.12, 10.13, 10.19, 10.20, 10.21, 10.22, 10.36, 10.48, 10.49, 10.51, 10.52, 10.54, 10.55, 10.57, 10.58, 2.1, 2.14, D10.1.1, D10.1.2, D10.1.3, D10.2.1, D10.2.2, D10.2.4, D10.2.5
**Human refs (from References field):** 10.11, 10.20, 10.22, 10.36, 10.54, 10.55, 10.57, 10.58, 6.1, D10.2.1, D10.2.2, D10.2.4, D10.2.5
**Jaccard:** 0.423 — AI adds ['10.12', '10.13', '10.19', '10.21', '10.48', '10.49', '10.51', '10.52', '2.1', '2.14', 'D10.1.1', 'D10.1.2', 'D10.1.3']; Human adds ['10.11', '6.1']

## Proposition 10.72
**Statement:** If two medial areas incommensurable with one another be added together, the remaining two irrational straight lines arise, namely either a second bimedial or a side of the sum of two medial areas.

**Step 1.** Let M and N be two medial areas incommensurable with one another. Apply them to the same assigned rational straight line r, obtaining respective breadths a and b, so that rect(r,a) = M and rect(r,b) = N. By 10.22, both a and b are rational and each is incommensurable in length with r. We choose the direct route of classifying their combined breadth and then using the established binomial area-to-side propositions.

**Step 2.** Rectangles of the same height are proportional to their bases, so M:N = a:b (6.1). Since M and N are incommensurable, a and b are incommensurable in length (10.11). This proportionality makes 10.11 the immediate means of transferring the given incommensurability.

**Step 3.** Since a and b are rational, their squares are each commensurable with the square on the assigned rational line r (D10.1.3). Their squares are therefore commensurable with one another (10.12). Thus a and b are commensurable in square only (D10.1.2 and Step 2), and their sum t = a+b is a binomial (10.36).

**Step 4.** By 2.1 and CN2,
rect(r,t) = rect(r,a) + rect(r,b) = M+N.
Let s be the side of a square equal to this area, constructed by 2.14. It remains to identify the order of the binomial t, since s is the side of the rectangle contained by r and t.

**Step 5.** The incommensurable lines a and b cannot be equal (D10.1.1); interchange their names if necessary so that a>b. Construct a square equal to the excess of the square on a over the square on b, and call its side d (2.14). Thus a² = b²+d². By D10.1.1, d is either commensurable or incommensurable in length with a. These alternatives exhaust the possibilities.

**Step 6.** Suppose d is commensurable in length with a. Neither term a nor term b is commensurable in length with r, by Step 1. Consequently, t is a third binomial (D10.2.3). Since rect(r,t) = M+N, its side s is the irrational straight line called a second bimedial (10.56).

**Step 7.** Suppose instead that d is incommensurable in length with a. Again, neither term is commensurable in length with r, so t is a sixth binomial (D10.2.6). The side s of rect(r,t) is therefore the irrational straight line called the side of the sum of two medial areas (10.59). Hence, in the two exhaustive cases, the side of the sum of the given incommensurable medial areas is either a second bimedial or a side of the sum of two medial areas, as required.

**USED:** 10.11, 10.12, 10.22, 10.36, 10.56, 10.59, 2.1, 2.14, 6.1, CN2, D10.1.1, D10.1.2, D10.1.3, D10.2.3, D10.2.6
**Human refs (from References field):** 10.11, 10.22, 10.36, 10.56, 10.59, 6.1, D10.2.3, D10.2.6
**Jaccard:** 0.533 — AI adds ['10.12', '2.1', '2.14', 'CN2', 'D10.1.1', 'D10.1.2', 'D10.1.3']

## Proposition 10.73
**Statement:** If from a rational straight line there be subtracted a rational straight line commensurable with the whole in square only, the remainder is irrational; and let it be called   an apotome.

**Step 1.** Let AB be a rational straight line, and let the rational straight line AC be subtracted from it, with C between A and B. Suppose AB and AC are commensurable in square only; thus they are incommensurable in length. The remainder is CB. [Hypothesis; D10.1.1, D10.1.2]

**Step 2.** Since AB = AC + CB and the whole AB is incommensurable in length with AC, the converse part of 10.16 shows that AC and CB are incommensurable in length. This proposition applies directly to the given relation between the whole and one part. [10.16]

**Step 3.** Suppose, for a contradiction, that CB is rational. Let R be the assigned rational straight line. Since AC and CB are both rational, their squares are each commensurable with the square on R. Consequently their squares are commensurable with one another, so AC and CB are commensurable in square. Together with Step 2, this makes them rational straight lines commensurable in square only. [D10.1.3, D10.1.2, 10.12]

**Step 4.** Apply the established sum theorem, rather than rederive an identity involving squares: the sum of two rational straight lines commensurable in square only is irrational. Therefore AC + CB, which is AB, is irrational, contrary to the hypothesis that AB is rational. [10.36; D10.1.3]

**Step 5.** Hence CB cannot be rational and is therefore irrational. Thus the remainder obtained by subtracting from a rational straight line a rational straight line commensurable with the whole in square only is irrational; let this remainder be called an **apotome**. [D10.1.3; naming stipulated in the proposition]

**USED:** 10.12, 10.16, 10.36, D10.1.1, D10.1.2, D10.1.3
**Human refs (from References field):** 10.11, 10.13, 10.15, 10.16, 10.6, 2.7, D10.1.4
**Jaccard:** 0.083 — AI adds ['10.12', '10.36', 'D10.1.1', 'D10.1.2', 'D10.1.3']; Human adds ['10.11', '10.13', '10.15', '10.6', '2.7', 'D10.1.4']

## Proposition 10.74
**Statement:** If from a medial straight line there be subtracted a medial straight line which is commensurable with the whole in square only, and which contains with the whole a rational rectangle, the remainder is irrational. And let it be called a first apotome of a medial straight line.

**Step 1.** Let AB be the given medial straight line, and let BC be the medial straight line subtracted from it, with C between A and B. Thus AB and BC are commensurable in square only, and the rectangle contained by AB and BC is rational. We must prove that AC is irrational. Let Q be the square on the assigned rational straight line; an area is rational precisely when it is commensurable with Q [D10.1.4].

**Step 2.** Write S for the sum of the squares on AB and BC. These two squares are commensurable by hypothesis [D10.1.2], so S is commensurable with the square on AB [10.15]. Since AB is medial, its square is irrational and therefore incommensurable with Q [10.21, D10.1.4]. Consequently S is incommensurable with Q [10.13].

**Step 3.** Write P for the rectangle contained by AB and BC. By hypothesis, P is commensurable with Q [D10.1.4]. The area 2P, being the sum of two equal areas P, is commensurable with P [10.15], and hence with Q [10.12]. Thus 2P is rational [D10.1.4].

**Step 4.** Since AB is cut at C, the sum of the squares on AB and BC equals twice the rectangle contained by AB and BC together with the square on AC [2.7]. Therefore
S = 2P + (the square on AC).
This is the direct path: the identity brings the given rational rectangle into the expression for the square on the remainder.

**Step 5.** Suppose that the square on AC were commensurable with Q. Since 2P is also commensurable with Q, these two areas would be commensurable with one another [10.12]. Their sum would therefore be commensurable with the square on AC [10.15], and hence with Q [10.12]. But their sum is S by Step 4, whereas S is incommensurable with Q by Step 2. This is a contradiction. Thus the square on AC is incommensurable with Q.

**Step 6.** Accordingly, the square on AC is irrational, and its side AC is irrational [D10.1.4]. Hence the remainder is irrational; let it be called a **first apotome of a medial straight line**, as required.

**USED:** 10.12, 10.13, 10.15, 10.21, 2.7, D10.1.2, D10.1.4
**Human refs (from References field):** 10.16, 2.7, D10.1.4
**Jaccard:** 0.250 — AI adds ['10.12', '10.13', '10.15', '10.21', 'D10.1.2']; Human adds ['10.16']

## Proposition 10.75
**Statement:** If from a medial straight line there be subtracted a medial straight line which is commensurable with the whole in square only, and which contains with the whole a medial rectangle, the remainder is irrational; and let it be called a second apotome of a medial straight line.

**Step 1.** Let a be the whole straight line, b the subtracted straight line, and c = a − b the positive remainder. Write a² for the square on a and ab for the rectangle contained by a and b. By hypothesis, a and b are medial, their squares are commensurable (D10.1.2), and ab is medial. Our route is to express c² as the excess of one medial area over another, so that 10.26 applies directly.

**Step 2.** Construct a third proportional d to a and b, so that a:b = b:d (6.11). Then ad = b² (6.17). The rectangles ad and a² have the same height, and therefore ad:a² = d:a (6.1). Since b² is commensurable with a², it follows that d is commensurable in length with a (10.11).

**Step 3.** Consequently, a + d is commensurable in length with a (10.15), and is therefore medial (10.23). The rectangle contained by a and a + d is thus medial, since its sides are medial and commensurable in length (10.24). But this rectangle equals a² + ad = a² + b² (2.3 and Step 2). Hence the area S = a² + b² is medial.

**Step 4.** Since ab is a medial area, let m be its medial square-side, so that m² = ab, using the medial terminology introduced in 10.21. The lines m and 2m are commensurable in length, with common measure m (D10.1.1); hence 2m is medial (10.23). Their rectangle is therefore medial (10.24). By 2.1, that rectangle equals twice m², and thus equals T = 2ab. Hence T is medial.

**Step 5.** Applying 2.7 to the whole a cut into b and c gives a² + b² = 2ab + c². Thus the medial area S exceeds the medial area T by precisely c².

**Step 6.** A medial area does not exceed a medial area by a rational area (10.26). Therefore c² is not rational, and its side c is irrational (D10.1.4). Hence the stated remainder is irrational; let it be called a **second apotome of a medial straight line**.

**USED:** 10.11, 10.15, 10.21, 10.23, 10.24, 10.26, 2.1, 2.3, 2.7, 6.1, 6.11, 6.17, D10.1.1, D10.1.2, D10.1.4
**Human refs (from References field):** 10.11, 10.13, 10.15, 10.20, 10.22, 10.23, 10.28, 10.6, 10.73, 2.7, 6.1
**Jaccard:** 0.238 — AI adds ['10.21', '10.24', '10.26', '2.1', '2.3', '6.11', '6.17', 'D10.1.1', 'D10.1.2', 'D10.1.4']; Human adds ['10.13', '10.20', '10.22', '10.28', '10.6', '10.73']

## Proposition 10.76
**Statement:** If from a straight line there be subtracted a straight line which is incommensurable in square with the whole and which with the whole makes the squares on them added together rational, but the rectangle contained by them medial, the remainder is irrational; and let it be called minor.

**Step 1.** Let AC be subtracted from AB, with C between A and B, so that CB is the remainder. By hypothesis, AB and AC are incommensurable in square, the area S = AB² + AC² is rational, and the rectangle M contained by AB and AC is medial. Let U be the square on the assigned rational straight line. Then S is commensurable with U (D10.1.4). Since a medial area is irrational, M is incommensurable with U (10.21, D10.1.4).

**Step 2.** Path choice: apply 2.7 directly, since it expresses the given rational sum of squares in terms of the square on the remainder and the given medial rectangle. Writing Q = CB², we obtain
S = 2M + Q.
(2.7.)

**Step 3.** The areas M and 2M are commensurable, since M measures both (D10.1.1). As M is incommensurable with U, so is 2M (10.13). Moreover, S is commensurable with U; therefore S is incommensurable with 2M (10.13).

**Step 4.** Since the whole S = 2M + Q is incommensurable with its part 2M, the converse assertion of 10.16 shows that 2M and Q are incommensurable. The direct assertion of 10.16 then shows that their sum S is incommensurable with Q. Finally, because S and U are commensurable, U is also incommensurable with Q (10.13).

**Step 5.** Thus the square Q on CB is incommensurable with the assigned rational square U. Consequently Q is an irrational area, and its side CB is an irrational straight line (D10.1.4). Therefore the remainder is irrational; let this remainder, under the stated hypotheses, be called **minor**.

**USED:** 10.13, 10.16, 10.21, 2.7, D10.1.1, D10.1.4
**Human refs (from References field):** 10.16, 10.33, 2.7
**Jaccard:** 0.286 — AI adds ['10.13', '10.21', 'D10.1.1', 'D10.1.4']; Human adds ['10.33']

## Proposition 10.77
**Statement:** If from a straight line there be subtracted a straight line which is incommensurable in square with the whole, and which with the whole makes the sum of the squares on them medial, but twice the rectangle contained by them rational, the remainder is irrational: and let it be called that which produces with a rational area a medial whole.

**Step 1.** Let BC be subtracted from AB, leaving AC, where AB and BC satisfy the stated hypotheses. Denote the sum of their squares by M, twice the rectangle contained by them by R, and the square on AC by Q. Let U be the square on the assigned rational straight line. By hypothesis, M is medial and R is rational. Therefore M is irrational and hence incommensurable with U, whereas R is commensurable with U. [10.21, D10.1.4]

**Step 2.** Since AB is cut at C, the squares on AB and BC together equal twice the rectangle contained by AB and BC together with the square on AC. Thus
M = R + Q.
[2.7] Our path is to use this whole-and-part identity directly with the converse clause of 10.16.

**Step 3.** Since U and R are commensurable, while U is incommensurable with M, R is also incommensurable with M. [10.13] Consequently, in the sum M = R + Q, the whole is incommensurable with the part R; therefore the two parts R and Q are incommensurable. [10.16]

**Step 4.** Since R and U are commensurable, while R is incommensurable with Q, U is also incommensurable with Q. [10.13] Thus Q is an irrational area, and its side AC is an irrational straight line. [D10.1.4] Moreover, the square on AC together with the rational area R makes the medial whole M, as established in Step 2. Accordingly, let AC be called **that which produces with a rational area a medial whole**. The required conclusion follows.

**USED:** 10.13, 10.16, 10.21, 2.7, D10.1.4
**Human refs (from References field):** 10.16, 10.34, 2.7
**Jaccard:** 0.333 — AI adds ['10.13', '10.21', 'D10.1.4']; Human adds ['10.34']

## Proposition 10.78
**Statement:** If from a straight line there be subtracted a straight line which is incommensurable in square with the whole and which with the whole makes the sum of the squares on them medial, twice the rectangle contained by them medial, and further the squares on them incommensurable with twice the rectangle contained by them, the remainder is irrational; and let it be called that which produces with a medial area a medial whole.

**Step 1.** Let AB be the whole straight line, AC the straight line subtracted, and CB the remainder, with C between A and B. Denote by S the sum of the squares on AB and AC, and by T twice the rectangle contained by AB and AC. By hypothesis, S and T are medial areas incommensurable with one another, and AB and AC are incommensurable in square.

**Step 2.** By 2.7, the squares on AB and AC together equal twice the rectangle contained by AB and AC together with the square on CB. Thus
S = T + (the square on CB).
Consequently, the medial area S exceeds the medial area T by the square on the remainder CB. [2.7]

**Step 3.** The direct route is to apply the previously proved medial-excess theorem: a medial area does not exceed a medial area by a rational area. Since S and T are medial, their excess, the square on CB, cannot be rational. [10.26]

**Step 4.** Therefore the square on CB is irrational, and its side CB is irrational. [D10.1.4] Moreover, by Step 2, the square on CB together with the medial area T makes the medial whole S. Hence the remainder is irrational, and let it be called **that which produces with a medial area a medial whole**.

**USED:** 10.26, 2.7, D10.1.4
**Human refs (from References field):** 10.11, 10.20, 10.22, 10.35, 10.73, 2.7, 6.1
**Jaccard:** 0.111 — AI adds ['10.26', 'D10.1.4']; Human adds ['10.11', '10.20', '10.22', '10.35', '10.73', '6.1']

## Proposition 10.79
**Statement:** To an apotome only one rational straight line can be annexed which is commensurable with the whole in square only.

**Step 1.** Let a be an apotome. By 10.73, there are rational straight lines x > y, commensurable in square only, such that a = x − y. Thus y is an annex of the required kind. We prove its uniqueness. Write z² for the square on a straight line z, and zw for the rectangle contained by z and w. [10.73]

**Step 2.** Suppose that another rational annex v, different from y, has the required property. Put u = a + v; thus u and v are commensurable in square only. Since v is rational, commensurability of their squares makes u rational also. Interchanging the two representations if necessary, suppose y > v. Since x = a + y and u = a + v, we then have x > u. [D10.1.2, D10.1.3, 10.12; CN2, CN5]

**Step 3.** Set S = x² + y² and T = u² + v². All four squares are rational areas. Magnitudes commensurable with the fixed rational square are commensurable with one another; their sums, and the positive difference of those sums, remain commensurable with that square. Hence S and T are rational. Moreover, x > u and y > v imply S > T, by the square-of-a-sum identity. Therefore E = S − T is a positive rational area. [D10.1.2, D10.1.3, D10.1.4; 10.12, 10.15; 2.4, CN5]

**Step 4.** Put M = xy and N = uv. Each is a medial area: the side of a square equal to either rectangle is medial, because its containing straight lines are rational and commensurable in square only. The direct route is therefore to compare these medial areas and apply 10.26; the common remainder a will allow its square to cancel. [10.21]

**Step 5.** Applied to x = a + y and u = a + v, 2.7 gives
S = a² + 2M, and T = a² + 2N.
Since S = T + E, substitution and subtraction of the common square give
2M = 2N + E.
Consequently M exceeds N by half of E. [2.7; CN2, CN3]

**Step 6.** Let H be that half of E. Since H measures E twice, H and E are commensurable. As E is rational, H is therefore also commensurable with the fixed rational square and is a positive rational area. Thus M = N + H: one medial area exceeds another by a rational area. [D10.1.1, 10.12, D10.1.4]

**Step 7.** This contradicts 10.26, which states that a medial area does not exceed a medial area by a rational area. Hence no second distinct annex exists. Together with the annex supplied in Step 1, this proves that to an apotome only one rational straight line can be annexed which is commensurable with the whole in square only. [10.26, 10.73]

**USED:** 10.12, 10.15, 10.21, 10.26, 10.73, 2.4, 2.7, CN2, CN3, CN5, D10.1.1, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 10.21, 10.26, 10.73, 2.7
**Jaccard:** 0.286 — AI adds ['10.12', '10.15', '2.4', 'CN2', 'CN3', 'CN5', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.1.4']

## Proposition 10.80
**Statement:** To a first apotome of a medial straight line only one medial straight line can be annexed which is commensurable with the whole in square only and which contains with the whole a rational rectangle.

**Step 1.** Let x be a first apotome of a medial straight line. Write uv for the rectangle contained by u and v, and u² for the square on u. By 10.74, there is a medial annex b such that a = x + b is medial, a and b are commensurable in square only, and ab is rational. Suppose that d is another medial annex satisfying the required conditions, and put c = x + d. Thus cd is rational, and c² and d² are commensurable, as are a² and b² (D10.1.2). We shall compare the two sums of squares and use the medial-area obstruction in 10.26.

**Step 2.** For (p,q) successively equal to (b,a) and (d,c), construct a fourth proportional t such that p:q = q:t (6.12). Then pt = q² (6.16). Since p² and q² are commensurable, and p²:pt = p:t by 6.1, the lines p and t are commensurable in length (10.11). Consequently p+t is commensurable in length with p (10.15); since p is medial, p+t is medial also (10.23).

**Step 3.** The rectangle p(p+t) is therefore medial, because its sides are medial and commensurable in length (10.24). But, by 2.1 and Step 2,
 p(p+t) = p²+pt = p²+q².
Applying this to the two pairs shows that both areas
 M₁ = a²+b² and M₂ = c²+d²
are medial.

**Step 4.** Proposition 2.7 applies directly to each whole and its annex, with x as the remaining segment. It gives
 M₁ = x²+2ab,
 M₂ = x²+2cd.
This whole-and-segment identity is the direct choice here because the two remainders are identical.

**Step 5.** If the annexes are unequal, interchange the two pairs if necessary so that d>b. Since a=x+b and c=x+d, we then have c>a (CN2, CN5). Hence cd>ad>ab, by rectangular addition and the fact that the whole exceeds its part (2.1, CN5). Put T=cd−ab, so T is positive. Let Q be the square on the assigned rational straight line. Since cd and ab are rational, each is commensurable with Q (D10.1.4), and therefore they are commensurable with one another (10.12). From cd=T+ab, proposition 10.15 gives that T is commensurable with ab; hence T is commensurable with Q (10.12). A common area measuring T and Q also measures 2T and Q (D10.1.1). Thus 2T is a rational area (D10.1.4).

**Step 6.** Substituting cd=ab+T into the identities of Step 4 gives
 M₂ = M₁+2T
by addition of equal areas (CN2). Thus the medial area M₂ exceeds the medial area M₁ by the positive rational area 2T, contrary to 10.26. The annexes cannot therefore be unequal, so d=b. An annex with the stated properties exists by 10.74, and the argument proves that it is unique. Hence to a first apotome of a medial straight line only one medial straight line can be annexed which is commensurable with the whole in square only and contains with the whole a rational rectangle.

**USED:** 10.11, 10.12, 10.15, 10.23, 10.24, 10.26, 10.74, 2.1, 2.7, 6.1, 6.12, 6.16, CN2, CN5, D10.1.1, D10.1.2, D10.1.4
**Human refs (from References field):** 10.15, 10.23, 10.26, 10.74, 2.7
**Jaccard:** 0.294 — AI adds ['10.11', '10.12', '10.24', '2.1', '6.1', '6.12', '6.16', 'CN2', 'CN5', 'D10.1.1', 'D10.1.2', 'D10.1.4']

## Proposition 10.81
**Statement:** To a second apotome of a medial straight line only one medial straight line can be annexed which is commensurable with the whole in square only and which contains with the whole a medial rectangle.

**Step 1.** Let d be the given second apotome of a medial straight line. An annex with the required properties exists by 10.75. For any such annex v, write u=d+v. Thus v is medial, u and v are commensurable in square only, and the rectangle uv is medial. Here z² denotes the square on z, and yz the rectangle contained by y and z. **Path choice:** apply the relevant areas to a fixed rational straight line, thereby reducing uniqueness to the previously established uniqueness of the annex to an apotome, 10.79.

**Step 2.** Fix the assigned rational straight line r. Construct straight lines a, b, p satisfying ra=u², rb=v², and rp=uv; these constructions follow by taking fourth proportionals and using the equality of the rectangles of the extremes and means (6.12, 6.16). Since v² and uv are medial areas, their application to r produces rational breadths b and p (10.22).

**Step 3.** Rectangles with the same height are proportional to their bases. Consequently,
 a:b=u²:v², and b:p=v²:uv=v:u
(6.1, 5.11). The squares u² and v² are commensurable, whereas v and u are incommensurable in length. Therefore a and b are commensurable in length, but b and p are incommensurable in length (D10.1.2, 10.11).

**Step 4.** Put s=a+b and t=2p. Since a and b are commensurable, s is commensurable in length with b; likewise t is commensurable in length with p (10.15). Since b and p are incommensurable, two applications of 10.13 show that s and t are incommensurable in length.

**Step 5.** Commensurability in length implies commensurability of the corresponding squares (10.9, 10.6). Thus s² is commensurable with b², and t² with p². Since b and p are rational, transitivity of commensurability shows that s and t are rational (10.12, D10.1.3). Their squares are therefore both commensurable with r², and hence with each other (10.12, D10.1.2). Together with Step 4, this proves that s and t are commensurable in square only.

**Step 6.** Since u=d+v, 2.7 gives
 u²+v²=2uv+d².
By the definitions of a, b, p, s, t and the distributivity of rectangles, this becomes
 rs=rt+d²
(2.1). Hence s>t (6.1, CN5), and, on subtracting rt,
 r(s−t)=d²
(2.1, CN3). Set e=s−t. Because s and t are rational and commensurable in square only, e is an apotome, with t as an admissible annex (10.73).

**Step 7.** Suppose v′ is another annex satisfying the requirements, and put u′=d+v′. Repeating Steps 2–6 with the same r produces rational straight lines s′, t′, commensurable in square only, such that e′=s′−t′ and re′=d². Since re′=re, the equal rectangles on the same straight line r have equal breadths, so e′=e (6.1, 5.9). Thus t and t′ are both rational annexes to the same apotome e, each commensurable with its whole in square only. By 10.79, t=t′. Consequently,
 2uv=rt=rt′=2u′v′
(2.1, CN1).

**Step 8.** If v′>v, then u′=d+v′>d+v=u. Placing the rectangles uv and u′v′ at a common corner with corresponding sides along the same rays, the former is a proper part of the latter. Its double is therefore also strictly smaller than the double of the latter, contrary to Step 7 (CN5). The reverse inequality is excluded in the same way. Hence v′=v. Since an admissible annex exists by 10.75, exactly one medial straight line can be annexed with the stated properties.

**USED:** 10.11, 10.12, 10.13, 10.15, 10.22, 10.6, 10.73, 10.75, 10.79, 10.9, 2.1, 2.7, 5.11, 5.9, 6.1, 6.12, 6.16, CN1, CN3, CN5, D10.1.2, D10.1.3
**Human refs (from References field):** 10.11, 10.13, 10.15, 10.22, 10.23, 10.6, 10.73, 10.75, 10.79, 2.7, 6.1
**Jaccard:** 0.435 — AI adds ['10.12', '10.9', '2.1', '5.11', '5.9', '6.12', '6.16', 'CN1', 'CN3', 'CN5', 'D10.1.2', 'D10.1.3']; Human adds ['10.23']

## Proposition 10.82
**Statement:** To a minor straight line only one straight line can be annexed which is incommensurable in square with the whole and which makes, with the whole, the sum of the squares on them rational but twice the rectangle contained by them medial.

**Step 1.** Let a be the given minor straight line. Write st for the rectangular area contained by straight lines s and t (D2.1). By 10.76, there are a whole u and an annex x such that u=a+x, the lines u and x are incommensurable in square, R=u²+x² is rational, and ux is medial. Our route to uniqueness will be the direct prohibition in 10.26 against two medial areas differing by a rational area.

**Step 2.** The area M=2ux is medial as well. Indeed, let m be the medial straight line whose square equals ux, according to the terminology of 10.21. The line 2m is commensurable in length with m, since m measures both (D10.1.1), and is therefore medial by 10.23. Consequently, the rectangle contained by m and 2m is medial by 10.24. But this rectangle equals 2m²=2ux by 2.1 and CN2. Thus x is an annex satisfying all the required conditions.

**Step 3.** Suppose that a second, unequal annex y satisfies those same conditions, and put v=a+y, S=v²+y², and N=2vy. Thus S is rational and N is medial. Interchanging the names of the two annexes if necessary, assume y>x; then v>u. A larger positive straight line has a larger square, by 2.4 and CN5. Hence S>R.

**Step 4.** Apply 2.7 to the whole u divided into a and x, and to the whole v divided into a and y. It gives
R=a²+M and S=a²+N.
Subtracting the common area a² shows that the excess of S over R equals the excess of N over M (CN3). Therefore N>M and
S−R=N−M.

**Step 5.** The positive area S−R is rational. To see this explicitly, let Q be the square on the assigned rational straight line. Since R and S are rational, each is commensurable with Q (D10.1.4), and hence they are commensurable with one another (10.12). Since S=R+(S−R), the converse assertion of 10.15 shows that S−R is commensurable with R. It is consequently commensurable with Q by 10.12, and therefore rational by D10.1.4.

**Step 6.** Thus the medial area N exceeds the medial area M by the rational area S−R. This contradicts 10.26. No unequal second annex can therefore satisfy the stated conditions. Since Step 2 supplied one such annex, to the given minor straight line only one straight line can be annexed which is incommensurable in square with the whole and makes the sum of their squares rational but twice their rectangle medial.

**USED:** 10.12, 10.15, 10.21, 10.23, 10.24, 10.26, 10.76, 2.1, 2.4, 2.7, CN2, CN3, CN5, D10.1.1, D10.1.4, D2.1
**Human refs (from References field):** 10.26, 10.76
**Jaccard:** 0.125 — AI adds ['10.12', '10.15', '10.21', '10.23', '10.24', '2.1', '2.4', '2.7', 'CN2', 'CN3', 'CN5', 'D10.1.1', 'D10.1.4', 'D2.1']

## Proposition 10.83
**Statement:** To a straight line which produces with a rational area a medial whole only one straight line can be annexed which is incommensurable in square with the whole straight line and which with the whole straight line makes the sum of the squares on them medial, but twice the rectangle contained by them rational.

**Step 1.** Let x be the given straight line. By the designation introduced in 10.77, there is an annex b such that the whole x+b and b are incommensurable in square, the area M_b=(x+b)²+b² is medial, and the area R_b=2(x+b)b is rational. Here products denote rectangular areas (D2.1). Suppose that a different annex c satisfies the same conditions, and put M_c=(x+c)²+c² and R_c=2(x+c)c. We use 10.26 directly, since these hypotheses already supply two medial areas whose difference can be compared.

**Step 2.** Interchanging the names of the annexes if necessary, suppose c>b. Then x+c>x+b (CN2, CN5). The square on a greater straight line exceeds the square on a lesser straight line: this follows by applying 2.4 to the greater line divided into the lesser and its positive excess, and then applying CN5. Thus (x+c)²>(x+b)² and c²>b², whence M_c>M_b (CN2, CN5).

**Step 3.** Apply 2.7 to each whole, divided into x and its annex. It gives
M_b=x²+R_b and M_c=x²+R_c.
Consequently R_c>R_b, and removing the common area x² shows that the positive differences are equal:
M_c−M_b=R_c−R_b (CN3, CN5).

**Step 4.** Let Q be the square on the assigned rational straight line. Since R_b and R_c are rational, both are commensurable with Q (D10.1.4), and therefore with one another (10.12). Write E=R_c−R_b, so that R_c=R_b+E. Since this whole is commensurable with R_b, the converse part of 10.15 makes E commensurable with R_b. Since R_b is commensurable with Q, it follows that E is commensurable with Q (10.12). Thus E is a positive rational area (D10.1.4).

**Step 5.** By Step 3, M_c exceeds M_b by E. Both M_c and M_b are medial, whereas E is rational. This contradicts 10.26, which states that a medial area does not exceed a medial area by a rational area. Hence two distinct annexes satisfying the stated conditions are impossible. An annex exists by the defining designation in 10.77, so exactly one such straight line can be annexed.

**USED:** 10.12, 10.15, 10.26, 10.77, 2.4, 2.7, CN2, CN3, CN5, D10.1.4, D2.1
**Human refs (from References field):** 10.26, 10.77
**Jaccard:** 0.182 — AI adds ['10.12', '10.15', '2.4', '2.7', 'CN2', 'CN3', 'CN5', 'D10.1.4', 'D2.1']

## Proposition 10.84
**Statement:** To a straight line which produces with a medial area a medial whole only one straight line can be annexed which is incommensurable in square with the whole straight line and which with the whole straight line makes the sum of the squares on them medial and twice the rectangle contained by them both medial and also incommensurable with the sum of the squares on them.

**Step 1.** Let c be the given straight line which produces with a medial area a medial whole. By the characterization in 10.78, it has an annex b such that, writing a = c + b, the lines a and b are incommensurable in square, and the areas S = a² + b² and T = 2ab are medial and incommensurable with one another. Suppose another annex b′ satisfies the same conditions; put a′ = c + b′, S′ = a′² + b′², and T′ = 2a′b′. We shall prove b = b′. [10.78]

**Step 2.** Applying 2.7 to the whole a and its parts c, b, and likewise to a′ and its parts c, b′, gives S = T + c² and S′ = T′ + c². Therefore S − T = S′ − T′ = c². [2.7, CN3]

**Step 3.** Choose a rational straight line r, and apply each of the medial areas S, T, S′, T′ to r as a rectangle. Denote their respective breadths by u, v, u′, v′. All four breadths are rational by 10.22. Moreover, u > v and u′ > v′, since S > T and S′ > T′. Our route is to use these rational breadths to reduce the question directly to uniqueness of the annex of an apotome, 10.79. [10.22, 6.1]

**Step 4.** Rectangles on the same base are proportional to their breadths, so S:T = u:v and S′:T′ = u′:v′. Since each pair of areas is incommensurable, each corresponding pair of breadths is incommensurable in length. But the breadths are rational: their squares are commensurable with the square on the assigned rational line, and hence with one another. Thus u, v are commensurable in square only, as are u′, v′. [6.1, 10.11, D10.1.3, 10.12, D10.1.2]

**Step 5.** Put q = u − v and q′ = u′ − v′. Subtracting the smaller rectangle from the larger on their common base r shows that the rectangles contained by r, q and by r, q′ are respectively S − T and S′ − T′, both equal to c². Consequently, by 6.1, q:r and q′:r both equal the ratio of c² to r². Hence q = q′ by 5.9. [2.1, CN3, 6.1, 5.9]

**Step 6.** Since q is the remainder after subtracting the rational line v from the rational line u, these lines being commensurable in square only, q is an apotome. Both v and v′ are rational annexes to this same apotome, and each is commensurable in square only with its respective whole, u or u′. The uniqueness theorem for an apotome therefore gives v = v′. [10.73, 10.79]

**Step 7.** The equal breadths v and v′ on the same base r give equal areas T = T′; thus 2ab = 2a′b′. If the annexes were unequal, interchange their names if necessary so that b′ > b, and put h = b′ − b > 0. Since a = c + b and a′ = c + b′, we have a′ = a + h. Distributing the rectangle gives a′b′ = ab + ah + bh + h², so 2a′b′ > 2ab, a contradiction. Therefore b = b′. An annex exists by Step 1, and every annex satisfying the stated conditions equals it; hence only one such straight line can be annexed. [6.1, CN2, 2.1, CN5]

**USED:** 10.11, 10.12, 10.22, 10.73, 10.78, 10.79, 2.1, 2.7, 5.9, 6.1, CN2, CN3, CN5, D10.1.2, D10.1.3
**Human refs (from References field):** 10.11, 10.22, 10.73, 10.78, 10.79, 2.7, 6.1
**Jaccard:** 0.467 — AI adds ['10.12', '2.1', '5.9', 'CN2', 'CN3', 'CN5', 'D10.1.2', 'D10.1.3']

## Proposition 10.85
**Statement:** To find the first apotome.

**Step 1.** Let r be the assigned rational straight line [D10.1.3]. By 10.48 construct a first binomial relative to r, and denote its greater and lesser terms by a and b. Path choice: reuse this established construction because its terms already satisfy the square-difference and commensurability conditions needed for a first apotome [10.48; D10.2.1].

**Step 2.** By the definition of binomial in 10.36, a and b are rational straight lines commensurable in square only. Since their sum is a first binomial, a is commensurable in length with r, and the square on a exceeds the square on b by the square on a straight line c commensurable in length with a [10.36; D10.2.1].

**Step 3.** Since a is greater than b, cut off from a a segment equal to b, and call the remainder x [1.3]. A rational straight line has thus been subtracted from a rational straight line commensurable with it in square only. Therefore x is an apotome, with whole a and annex b [10.73].

**Step 4.** The whole a is commensurable in length with the assigned rational straight line r, and its square exceeds the square on the annex b by the square on c, which is commensurable in length with a. Hence x is a first apotome by D10.3.1. Thus the first apotome has been found.

**USED:** 1.3, 10.36, 10.48, 10.73, D10.1.3, D10.2.1, D10.3.1
**Human refs (from References field):** 10.6, 10.73, 10.9, 5.19, D10.3.1
**Jaccard:** 0.200 — AI adds ['1.3', '10.36', '10.48', 'D10.1.3', 'D10.2.1']; Human adds ['10.6', '10.9', '5.19']

## Proposition 10.86
**Statement:** To find the second apotome.

**Step 1.** Let R be the assigned rational straight line. By 10.49, construct a second binomial relative to R, with greater term U and lesser term V. This is the direct construction route: its terms already have the required properties, so we shall take their difference instead of their sum. [10.49]

**Step 2.** By the definition of binomial, U and V are rational straight lines commensurable in square only. Since their sum is a second binomial, V is commensurable in length with R, and the square on U exceeds the square on V by the square on a straight line W commensurable in length with U. [10.36, D10.2.1, D10.2.2]

**Step 3.** From U cut off a straight line equal to V, and call the remainder A. This is possible because U is greater than V. Since a rational straight line commensurable with U in square only has been subtracted from the rational straight line U, the remainder A is an apotome. Its whole is U and its annex is V. [1.3, 10.73]

**Step 4.** The annex V is commensurable in length with the assigned rational straight line R; moreover, the square on the whole U exceeds the square on V by the square on W, which is commensurable in length with U. Therefore A is a second apotome. Thus the required second apotome has been found. [D10.3.2]

**USED:** 1.3, 10.36, 10.49, 10.73, D10.2.1, D10.2.2, D10.3.2
**Human refs (from References field):** 10.6, 10.73, 10.9, 5.19, D10.3.2
**Jaccard:** 0.200 — AI adds ['1.3', '10.36', '10.49', 'D10.2.1', 'D10.2.2']; Human adds ['10.6', '10.9', '5.19']

## Proposition 10.87
**Statement:** To find the third apotome.

**Step 1.** Let r be the assigned rational straight line. By 10.50, construct a third binomial relative to r, with greater term u and lesser term v. Path choice: use this existing construction because its terms already possess the conditions required for the whole and annex of a third apotome. [10.50]

**Step 2.** Since u and v are the terms of a binomial, they are rational straight lines commensurable with one another in square only, by the designation of binomial in 10.36. [10.36]

**Step 3.** By the defining conditions of a third binomial, neither u nor v is commensurable in length with r. Moreover, the square on u exceeds the square on v by the square on a straight line w commensurable in length with u. [D10.2.1, D10.2.3]

**Step 4.** Since u is greater than v, cut off from u a segment equal to v, and call the remainder a. This construction is possible by 1.3. A rational straight line commensurable with the rational whole in square only has thus been subtracted from that whole; therefore a is an apotome. Its whole is u and its annex is the segment equal to v. [1.3, 10.73]

**Step 5.** Neither the whole nor the annex is commensurable in length with r, and the square on the whole exceeds the square on the annex by the square on w, which is commensurable in length with the whole. Hence a is a third apotome by definition. Thus the third apotome has been found. [D10.3.3]

**USED:** 1.3, 10.36, 10.50, 10.73, D10.2.1, D10.2.3, D10.3.3
**Human refs (from References field):** 10.6, 10.73, 10.9, 5.19, 5.22, D10.3.3
**Jaccard:** 0.182 — AI adds ['1.3', '10.36', '10.50', 'D10.2.1', 'D10.2.3']; Human adds ['10.6', '10.9', '5.19', '5.22']

## Proposition 10.88
**Statement:** To find the fourth apotome.

**Step 1.** Let r be the assigned rational straight line. Construct a fourth binomial relative to r, and denote its greater and lesser terms by u and v, respectively [10.51]. We use this existing construction because its terms already have the properties required for the desired subtraction.

**Step 2.** Since u and v are the terms of a binomial, they are rational straight lines commensurable in square only [10.36]. Since this binomial is fourth, u is commensurable in length with r, and there is a straight line d, incommensurable in length with u, such that the square on u exceeds the square on v by the square on d [D10.2.4].

**Step 3.** Since u > v, cut off from u a straight line equal to v, leaving x [1.3]. Because the subtracted line and the whole are rational and commensurable in square only, x is an apotome [10.73]. Its whole is u and its annex is v.

**Step 4.** The whole u is commensurable in length with the assigned rational line r, and its square exceeds the square on the annex v by the square on d, which is incommensurable in length with u. Therefore x is a fourth apotome [D10.3.4]. Thus the fourth apotome has been found.

**USED:** 1.3, 10.36, 10.51, 10.73, D10.2.4, D10.3.4
**Human refs (from References field):** 10.6, 10.73, 10.9, 5.19, D10.3.4
**Jaccard:** 0.222 — AI adds ['1.3', '10.36', '10.51', 'D10.2.4']; Human adds ['10.6', '10.9', '5.19']

## Proposition 10.89
**Statement:** To find the fifth apotome.

**Step 1.** Let r be the assigned rational straight line. By 10.52, construct a fifth binomial relative to r, and let its greater and lesser terms be a and b respectively. We choose this construction because its terms already possess the square-difference and commensurability properties required for a fifth apotome.

**Step 2.** By the definition of binomial in 10.36, a and b are rational straight lines commensurable in square only. Since their sum is a fifth binomial, b is commensurable in length with r, and the square on a exceeds the square on b by the square on a straight line c incommensurable in length with a; thus a² = b² + c² (D10.2.4, D10.2.5).

**Step 3.** Since a is greater than b, cut off from a a straight line equal to b, leaving d (1.3). The remainder d is an apotome, because a rational straight line has been subtracted from a rational straight line commensurable with it in square only (10.73). Its whole is a and its annex is b.

**Step 4.** The square on the whole a exceeds the square on the annex b by the square on c, which is incommensurable in length with a; moreover, the annex b is commensurable in length with the assigned rational straight line r. Therefore d is a fifth apotome by D10.3.4–D10.3.5. Thus the required fifth apotome has been found.

**USED:** 1.3, 10.36, 10.52, 10.73, D10.2.4, D10.2.5, D10.3.4, D10.3.5
**Human refs (from References field):** 10.6, 10.73, 10.9, 5.19, D10.3.5
**Jaccard:** 0.182 — AI adds ['1.3', '10.36', '10.52', 'D10.2.4', 'D10.2.5', 'D10.3.4']; Human adds ['10.6', '10.9', '5.19']

## Proposition 10.90
**Statement:** To find the sixth apotome.

**Step 1.** Let r be the assigned rational straight line. By 10.53, construct a sixth binomial relative to r, with greater term u and lesser term v. We choose this direct route because passing from the sum of these terms to their difference preserves the conditions on the terms and on the difference of their squares. [10.53]

**Step 2.** The terms u and v are rational straight lines commensurable in square only, by the definition of a binomial. Since the constructed binomial is sixth, neither u nor v is commensurable in length with r, and the square on u exceeds the square on v by the square on a straight line w incommensurable in length with u. [10.36; D10.2.4; D10.2.6]

**Step 3.** From u cut off a straight line equal to v, and let a be the remainder. This is possible because u is greater than v. Since a rational straight line commensurable with u in square only has been subtracted from the rational straight line u, the remainder a is an apotome, with whole u and annex v. [1.3; 10.73]

**Step 4.** The square on the whole u exceeds the square on the annex v by the square on w, which is incommensurable in length with u; moreover, neither the whole nor the annex is commensurable in length with the assigned rational straight line r. Therefore a is a sixth apotome. Thus the required sixth apotome has been found. [D10.3.4; D10.3.6]

**USED:** 1.3, 10.36, 10.53, 10.73, D10.2.4, D10.2.6, D10.3.4, D10.3.6
**Human refs (from References field):** 10.6, 10.73, 10.9, 5.19, 5.22, D10.3.6
**Jaccard:** 0.167 — AI adds ['1.3', '10.36', '10.53', 'D10.2.4', 'D10.2.6', 'D10.3.4']; Human adds ['10.6', '10.9', '5.19', '5.22']

## Proposition 10.91
**Statement:** If an area be contained by a rational straight line and a first apotome, the âsideâ of the area is an apotome.

**Step 1.** Let the given area be the rectangle r(a−b), where r is the rational straight line set out and a−b is the first apotome. Here a>b are rational straight lines commensurable in square only. Moreover, a is commensurable in length with r, and a²−b²=c² for a straight line c commensurable in length with a (10.73, D10.3.1). Products below denote rectangles, and squares denote square areas.

**Step 2.** Bisect b, writing h=b/2; then h² is one quarter of b² (1.10, 2.4). Apply to a a rectangle equal to h² and deficient by a square (6.28). This is possible because b<a, so h² is less than the square on half of a. Denote the resulting parts of a by m>n>0. Thus
m+n=a, mn=h².
By 10.17, m and n are commensurable in length. This is the direct path: the square-difference condition in the definition of the first apotome is precisely the hypothesis of 10.17.

**Step 3.** Since m and n are commensurable, each is commensurable with their sum a (10.15). Since a is commensurable in length with r, both m and n are commensurable in length with r (10.12), and hence are rational (D10.1.3).

**Step 4.** Construct squares equal to the rectangles rm and rn, and call their sides x and y respectively (2.14). Thus x²=rm and y²=rn. Both rectangles are rational by 10.19. Consequently x and y are rational, and their squares, being commensurable with the same rational square, are commensurable with one another (D10.1.3, D10.1.4, 10.12, D10.1.2). Also x>y: the first rectangle is greater by 6.1, and the square on a smaller side cannot exceed that on a larger side, by CN5 applied to nested squares.

**Step 5.** The ratios of rectangles with the same height give
x²:y² = rm:rn = m:n = m²:mn = m²:h²
(6.1 and the equalities established above). Since proportional squares have proportional sides, it follows that
x:y = m:h
(6.22).

**Step 6.** The line m is commensurable in length with a, whereas b is incommensurable in length with a. Hence m is incommensurable in length with b (10.13). Since h measures b, h is commensurable with b (D10.1.1); therefore m is also incommensurable in length with h (10.13). The proportion in Step 5 now shows that x and y are incommensurable in length (10.11). Together with Step 4, this proves that x and y are rational straight lines commensurable in square only.

**Step 7.** Again using ratios of rectangles with the same height,
x²:xy = x:y = m:h = rm:rh = x²:rh
(6.1). Therefore xy=rh (5.9). Doubling these equal areas and using b=h+h gives
2xy=rb
(CN2, 2.1).

**Step 8.** By 2.1,
x²+y²=rm+rn=r(m+n)=ra.
By 2.7, the squares on x and y together equal twice their rectangle together with the square on their difference. Subtracting the equal areas 2xy and rb therefore gives
(x−y)²=ra−rb=r(a−b)
(CN3, 2.1). Thus x−y is the side of the given area (D10.1.4).

**Step 9.** Since x>y are rational straight lines commensurable in square only, their difference x−y is an apotome by 10.73. Therefore the side of an area contained by a rational straight line and a first apotome is an apotome.

**USED:** 1.10, 10.11, 10.12, 10.13, 10.15, 10.17, 10.19, 10.73, 2.1, 2.14, 2.4, 2.7, 5.9, 6.1, 6.22, 6.28, CN2, CN3, CN5, D10.1.1, D10.1.2, D10.1.3, D10.1.4, D10.3.1
**Human refs (from References field):** 10.11, 10.12, 10.13, 10.15, 10.17, 10.19, 10.21, 10.53, 10.73, 5.11, 6.1, 6.17, 6.26, D10.3.1
**Jaccard:** 0.310 — AI adds ['1.10', '2.1', '2.14', '2.4', '2.7', '5.9', '6.22', '6.28', 'CN2', 'CN3', 'CN5', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.1.4']; Human adds ['10.21', '10.53', '5.11', '6.17', '6.26']

## Proposition 10.92
**Statement:** If an area be contained by a rational straight line and a second apotome, the âsideâ of the area is a first apotome of a medial straight line.

**Step 1.** Let r be the rational straight line and a−b the second apotome, with whole a and annex b. Products of straight lines will denote their rectangles (D2.1). By 10.73 and D10.3.2, a and b are rational and commensurable in square only, b is commensurable in length with r, and a²−b²=c² for some c commensurable in length with a. Consequently a is incommensurable in length with r (10.13). We use 10.17 directly, since its square-excess hypothesis is exactly the condition supplied by the definition of a second apotome.

**Step 2.** Let h be half of b (1.10). Apply an area equal to h² to a, deficient by a square. This is possible by 6.28, because b<a, so h² is less than the square on half of a. Let the resulting parts of a be x and y, labeled so that x>y. Thus x+y=a and xy=h²=b²/4; the parts are unequal because b<a. By 10.17 and the square-excess condition in Step 1, x and y are commensurable in length. Their sum a is therefore commensurable in length with each of them (10.15).

**Step 3.** Since x and y are commensurable in length with a, their squares are commensurable with a² (10.9, 10.6). Since a is rational, x and y are rational (10.12, D10.1.3). Neither is commensurable in length with r, because each is commensurable with a, whereas a is incommensurable with r (10.13). Thus r and either x or y are commensurable in square only. Also h is commensurable in length with b, and hence with r (D10.1.1, 10.12); it is rational by the same square-commensurability argument (10.9, 10.6, D10.1.3).

**Step 4.** Construct straight lines u, v, and w such that u²=rx, v²=ry, and w²=rh (2.14). By 10.21, u and v are medial, since the respective rectangles are contained by rational straight lines commensurable in square only. By 10.19, rh is rational, since r and h are rational and commensurable in length. Moreover, x>y gives u²>v² and hence u>v (6.1, CN5).

**Step 5.** Rectangles of equal height are proportional to their bases, so u²:v²=rx:ry=x:y (6.1). Since x and y are commensurable, u² and v² are commensurable (10.11). Therefore u and v are commensurable in square (D10.1.2).

**Step 6.** We now identify the rectangle uv. Since xy=h², we have x:h=h:y (6.17). Hence, by 6.1,

u²:w²=rx:rh=x:h=h:y=rh:ry=w²:v².

Applying the converse of 6.22 to these squares gives u:w=w:v. Therefore uv=w²=rh (6.17). In particular, uv is rational by Step 4.

**Step 7.** If u and v were commensurable in length, their rectangle would be medial by 10.24. A medial area is irrational (10.21, D10.1.4), whereas uv is rational by Step 6. Thus u and v are incommensurable in length. Together with Step 5, this proves that they are medial straight lines commensurable in square only and containing a rational rectangle.

**Step 8.** By 2.1, u²+v²=r(x+y)=ra, and twice uv equals twice rh, namely rb. Applying 2.7 to the straight line u cut into v and u−v, and subtracting equal areas, gives

(u−v)²=u²+v²−2uv=ra−rb=r(a−b)

(2.7, CN3, 2.1). Thus u−v is the side of the given area. By Step 7 and 10.74, this difference is a first apotome of a medial straight line. Therefore the side of an area contained by a rational straight line and a second apotome is a first apotome of a medial straight line.

**USED:** 1.10, 10.11, 10.12, 10.13, 10.15, 10.17, 10.19, 10.21, 10.24, 10.6, 10.73, 10.74, 10.9, 2.1, 2.14, 2.7, 6.1, 6.17, 6.22, 6.28, CN3, CN5, D10.1.1, D10.1.2, D10.1.3, D10.1.4, D10.3.2, D2.1
**Human refs (from References field):** 10.11, 10.13, 10.15, 10.17, 10.19, 10.21, 10.73, 10.74, 5.11, 6.1, 6.17, 6.26, D10.3.2
**Jaccard:** 0.367 — AI adds ['1.10', '10.12', '10.24', '10.6', '10.9', '2.1', '2.14', '2.7', '6.22', '6.28', 'CN3', 'CN5', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.1.4', 'D2.1']; Human adds ['5.11', '6.26']

## Proposition 10.93
**Statement:** If an area be contained by a rational straight line and a third apotome, the âsideâ of the area is a second apotome of a medial straight line.

**Step 1.** Let r be the given rational straight line, and write the third apotome as a − b, where a > b. Here a and b are rational and commensurable in square only (10.73). By the definition of a third apotome, neither a nor b is commensurable in length with r, and a² − b² = c² for some straight line c commensurable in length with a (D10.3.3). Throughout, pq denotes the rectangle contained by p and q.

**Step 2.** Bisect b, putting h = b/2; thus h is commensurable in length with b (1.10; D10.1.1). Apply to a a rectangle equal to h² and deficient by a square, obtaining parts x and y such that
x + y = a,   xy = h².
This construction is possible by 6.28, since h² is less than the square on half of a. Label the unequal parts so that x > y > 0. The relevant path is the commensurable deficient-square case of 10.17: because a² − b² = c² and c is commensurable with a, that proposition gives that x and y are commensurable in length. Their sum a is therefore commensurable in length with each of them (10.15).

**Step 3.** Length commensurability implies square commensurability by 10.9 and 10.6. Consequently, since x and y are commensurable in length with the rational line a, and h with the rational line b, all three lines x, y, h are rational (10.12; D10.1.3). Moreover, x and y are incommensurable in length with r, as is h, by 10.13 and Step 1. Finally, x and h are incommensurable in length: otherwise their commensurabilities with a and b would, by repeated application of 10.12, make a and b commensurable in length, contrary to Step 1.

**Step 4.** Construct u as a mean proportional between r and x, and v as a mean proportional between r and y (6.13). Then
u² = rx,   v² = ry
by 6.17. Since x > y, we have u > v (6.1; CN5). The pairs r, x and r, y consist of rational lines commensurable in square only; hence u and v are medial straight lines (10.21).

**Step 5.** Rectangles of the same height are proportional to their bases, so
u² : v² = rx : ry = x : y
(6.1). Since x and y are commensurable in length, their corresponding squares u² and v² are commensurable as areas (10.11); thus u and v are commensurable in square (D10.1.2). Also, because h² = xy,
x² : h² = x² : xy = x : y
(6.1). Therefore u² : v² = x² : h², and consequently u : v = x : h (6.22). Since x and h are incommensurable in length, u and v are likewise incommensurable in length (10.11). Thus u and v are commensurable in square only.

**Step 6.** Alternating u : v = x : h gives u : x = v : h (5.16). But the construction of u gives r : u = u : x. Hence r : u = v : h (CN1), and therefore
uv = rh
by 6.16. Since r and h are rational and commensurable in square only, this rectangle is medial (10.21).

**Step 7.** Applying 2.7 to the line u cut into v and u − v gives
u² + v² = 2uv + (u − v)².
On the other hand, the distributive identity for rectangles gives
u² + v² = rx + ry = r(x + y) = ra,
and
2uv = 2rh = rb
(2.1). Subtracting equal areas therefore yields
(u − v)² = ra − rb = r(a − b)
(CN3; 2.1).

**Step 8.** The lines u and v are medial, commensurable in square only, and contain a medial rectangle. Their difference u − v is therefore a second apotome of a medial straight line (10.75). Its square equals the given area r(a − b), by Step 7; hence it is the required side of that area (D10.1.4).

**USED:** 1.10, 10.11, 10.12, 10.13, 10.15, 10.17, 10.21, 10.6, 10.73, 10.75, 10.9, 2.1, 2.7, 5.16, 6.1, 6.13, 6.16, 6.17, 6.22, 6.28, CN1, CN3, CN5, D10.1.1, D10.1.2, D10.1.3, D10.1.4, D10.3.3
**Human refs (from References field):** 10.11, 10.13, 10.15, 10.17, 10.21, 10.75, 5.11, 6.1, 6.17, 6.26, D10.3.3
**Jaccard:** 0.300 — AI adds ['1.10', '10.12', '10.6', '10.73', '10.9', '2.1', '2.7', '5.16', '6.13', '6.16', '6.22', '6.28', 'CN1', 'CN3', 'CN5', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.1.4']; Human adds ['5.11', '6.26']

## Proposition 10.94
**Statement:** If an area be contained by a rational straight line and a fourth apotome, the âsideâ of the area is minor.

**Step 1.** Let r be the given rational straight line, and write the fourth apotome as a−b, where a is its whole and b its annex. Products below denote rectangular areas. By the definition of an apotome, a and b are rational and commensurable in square only [10.73]. Since this is a fourth apotome, a is commensurable in length with r, and a²−b² is the square on a straight line incommensurable in length with a [D10.3.4].

**Step 2.** Path choice: pass to the binomial with the same terms, so that the already established area-side theorem applies directly. The straight line a+b is binomial [10.36], and the properties in Step 1 make it a fourth binomial [D10.2.4]. Construct the side s of the area r(a+b) [2.14]. Then s is major [10.57]. Consequently, by the defining description of a major straight line, write s=u+v, with u>v, where u and v are incommensurable in square, U=u²+v² is rational, and uv is medial [10.39].

**Step 3.** Put R=ra and M=rb. Since r and a are rational and commensurable in length, R is rational [10.19]. The rational lines r and b are commensurable in square [D10.1.3, 10.12]. They are incommensurable in length, because r is commensurable in length with a, whereas b is not [10.13]. Hence M is a medial area [10.21].

**Step 4.** The area N=2uv is also medial. Indeed, construct m with m²=uv; since uv is medial, m is its medial side [2.14, 10.21]. The lines m and 2m are commensurable in length [D10.1.1], so 2m is medial [10.23]. Their rectangle is therefore medial [10.24], and that rectangle equals 2m²=2uv=N [2.1].

**Step 5.** Expanding the square on u+v gives s²=U+N [2.4]. Distributing the rectangle r(a+b) gives r(a+b)=R+M [2.1]. Since s² was constructed equal to r(a+b), it follows that U+N=R+M [CN1].

**Step 6.** We claim that U=R. Both U and R are rational areas. If unequal, their positive difference would also be rational: they are commensurable with the assigned rational square and hence with one another, and their difference is commensurable with the lesser [D10.1.4, 10.12, 10.15]. But U+N=R+M would then make one of the medial areas M and N exceed the other by that rational difference [CN3], contrary to 10.26. Thus U=R, and subtraction in the equality of Step 5 gives N=M [CN3].

**Step 7.** Let t=u−v. By the identity for the square on a difference and Step 6,
 t²=u²+v²−2uv=U−N=R−M=r(a−b)
[2.7, 2.1, CN3]. Thus t is the side of the given area. Moreover, u and v are incommensurable in square, their squares together form the rational area U, and their rectangle uv is medial. Therefore their difference t is minor [10.76]. Hence the side of an area contained by a rational straight line and a fourth apotome is minor.

**USED:** 10.12, 10.13, 10.15, 10.19, 10.21, 10.23, 10.24, 10.26, 10.36, 10.39, 10.57, 10.73, 10.76, 2.1, 2.14, 2.4, 2.7, CN1, CN3, D10.1.1, D10.1.3, D10.1.4, D10.2.4, D10.3.4
**Human refs (from References field):** 10.11, 10.18, 10.19, 10.21, 10.76, 5.11, 6.1, 6.17, 6.26, D10.3.4
**Jaccard:** 0.133 — AI adds ['10.12', '10.13', '10.15', '10.23', '10.24', '10.26', '10.36', '10.39', '10.57', '10.73', '2.1', '2.14', '2.4', '2.7', 'CN1', 'CN3', 'D10.1.1', 'D10.1.3', 'D10.1.4', 'D10.2.4']; Human adds ['10.11', '10.18', '5.11', '6.1', '6.17', '6.26']

## Proposition 10.95
**Statement:** If an area be contained by a rational straight line and a fifth apotome, the âsideâ of the area is a straight line which produces with a rational area a medial whole.

**Step 1.** Let r be the given rational straight line, and write the given fifth apotome as a−b, where a>b. Write pq for the rectangle contained by straight lines p,q, and p² for the square on p. By the description of an apotome and the definition of the fifth kind, a and b are rational and commensurable in square only, b is commensurable in length with r, and a²=b²+d² for a straight line d incommensurable in length with a. (10.73; D10.3.5.)

**Step 2.** We take the corresponding fifth binomial, so that the previously established area-side theorem applies without reconstructing its side. By 10.36, a+b is binomial; the conditions in Step 1 make it a fifth binomial by D10.2.5. Therefore the side s of the area r(a+b) is the straight line called the side of a rational plus a medial area. (10.58.)

**Step 3.** Since b and r are commensurable in length, while a and b are incommensurable in length, a and r are incommensurable in length. (10.13.) Being rational, a and r are nevertheless commensurable in square. (D10.1.3; 10.12.) Consequently the area M₀=ra is medial, whereas R₀=rb is rational. (10.21; 10.19.)

**Step 4.** By the defining description in 10.40, write s=u+v, choosing u>v, where u and v are incommensurable in square, M=u²+v² is medial, and uv is rational. Put R=2uv. The double of a rational area is commensurable with that area and is therefore rational. (10.15; 10.12; D10.1.4.) The square-of-a-sum identity and the division of a rectangle now give
M+R=s²=r(a+b)=M₀+R₀.
(2.4; 2.1.)

**Step 5.** We identify these summands by 10.26, which applies directly to the two medial areas. First, a positive difference of rational areas is rational: the two areas are commensurable by D10.1.4 and 10.12; their difference is commensurable with the smaller by 10.15, and hence is rational by 10.12 and D10.1.4. If M>M₀, the equality in Step 4 gives M−M₀=R₀−R>0 by cancellation. (CN3.) Thus one medial area would exceed another by a rational area, contrary to 10.26. The case M₀>M gives the same contradiction. Hence M=M₀, and cancellation also gives R=R₀. (CN3.)

**Step 6.** By the square-of-a-difference identity, Step 5, and the division of a rectangle,
(u−v)²=M−R=M₀−R₀=ra−rb=r(a−b).
(2.7; CN3; 2.1.) Thus u−v is the side of the given area. But u and v are incommensurable in square, their squares together form the medial area M, and twice their rectangle is the rational area R. Therefore 10.77 states precisely that u−v is a straight line which produces with a rational area a medial whole. This proves the proposition.

**USED:** 10.12, 10.13, 10.15, 10.19, 10.21, 10.26, 10.36, 10.40, 10.58, 10.73, 10.77, 2.1, 2.4, 2.7, CN3, D10.1.3, D10.1.4, D10.2.5, D10.3.5
**Human refs (from References field):** 10.18, 10.19, 10.21, 10.77, 6.26, D10.3.5
**Jaccard:** 0.190 — AI adds ['10.12', '10.13', '10.15', '10.26', '10.36', '10.40', '10.58', '10.73', '2.1', '2.4', '2.7', 'CN3', 'D10.1.3', 'D10.1.4', 'D10.2.5']; Human adds ['10.18', '6.26']

## Proposition 10.96
**Statement:** If an area be contained by a rational straight line and a sixth apotome, the âsideâ of the area is a straight line which produces with a medial area a medial whole.

**Step 1.** Let r be the given rational straight line, and let a − b, with a > b, be the given sixth apotome. By 10.73 and D10.3.6, a and b are rational straight lines commensurable in square only; neither is commensurable in length with r; and a² exceeds b² by the square on a straight line incommensurable in length with a. Consequently, a + b is a sixth binomial (10.36, D10.2.6). We choose the companion-binomial route, since the previously proved sixth-binomial area theorem applies immediately.

**Step 2.** By 10.59, the side s of the rectangle r(a + b) is the straight line called the side of the sum of two medial areas. Thus, by the defining characterization in 10.41, write s = u + v, where u > v, u and v are incommensurable in square, and, putting S = u² + v² and T = uv, both S and T are medial areas and are incommensurable with one another. In particular, (u + v)² = r(a + b).

**Step 3.** The area 2T is also medial. Indeed, write the medial area T as m², with m medial. The straight line 2m is commensurable in length with m and therefore medial by 10.23. Hence the rectangle contained by m and 2m is medial by 10.24; this rectangle equals 2T by 2.1. Moreover, T and 2T have the common measure T (D10.1.1). Since T is incommensurable with S, so is 2T, by 10.13.

**Step 4.** Apply the medial areas S and 2T to r, obtaining breadths c and d respectively, so that rc = S and rd = 2T. By 10.22, c and d are rational straight lines. Their squares are therefore commensurable with one another (D10.1.3, 10.12). Since the rectangles have the same height r, 6.1 gives c : d = S : 2T. The latter areas are incommensurable by Step 3, so c and d are incommensurable in length by 10.11. Thus c and d are commensurable in square only, and c + d is a binomial by 10.36.

**Step 5.** By 2.7, S = (u − v)² + 2T. Since u > v, S > 2T (CN5), and therefore c > d (6.1). Also, by 2.4 and Step 2, S + 2T = (u + v)² = r(a + b). On the other hand, 2.1 gives S + 2T = r(c + d). Equal rectangles having the same height have equal bases, by 6.1; hence c + d = a + b.

**Step 6.** The equal binomial straight lines in Step 5 have been divided into rational terms commensurable in square only, with the greater term taken first in each case. A binomial has only one division into its terms (10.42). Therefore c = a and d = b, and consequently S = ra and 2T = rb.

**Step 7.** Let z = u − v. By 2.7, z² + 2T = S. Substituting the equalities from Step 6 gives z² + rb = ra. But 2.1 gives r(a − b) + rb = ra; subtracting the common area rb yields z² = r(a − b) (CN3). Thus z is the side of the given area. Now u and v are incommensurable in square, their squares have the medial sum S, and twice their rectangle is the medial area 2T, incommensurable with S. Therefore 10.78 applies: z is the irrational straight line which produces with a medial area a medial whole. This proves the proposition.

**USED:** 10.11, 10.12, 10.13, 10.22, 10.23, 10.24, 10.36, 10.41, 10.42, 10.59, 10.73, 10.78, 2.1, 2.4, 2.7, 6.1, CN3, CN5, D10.1.1, D10.1.3, D10.2.6, D10.3.6
**Human refs (from References field):** 10.11, 10.18, 10.21, 10.78, 6.1, 6.26, D10.3.6
**Jaccard:** 0.160 — AI adds ['10.12', '10.13', '10.22', '10.23', '10.24', '10.36', '10.41', '10.42', '10.59', '10.73', '2.1', '2.4', '2.7', 'CN3', 'CN5', 'D10.1.1', 'D10.1.3', 'D10.2.6']; Human adds ['10.18', '10.21', '6.26']

## Proposition 10.97
**Statement:** The square on an apotome applied to a rational straight line produces as breadth a first apotome.

**Step 1.** Write st for the rectangle contained by straight lines s and t, and s² for the square on s (D2.1). Let c be the given apotome and r the given rational straight line. By 10.73, write c = a − b, where a > b and a, b are rational straight lines commensurable in square only. Let x be the breadth produced by applying c² to r, so that rx = c². We shall use the commensurable-division criterion 10.17: separate applications of a² and b² naturally supply the division it requires.

**Step 2.** Construct breadths p, q, t such that rp = a², rq = b², and rt = ab; these constructions follow by taking fourth proportionals and using the equality of the corresponding rectangles (6.12, 6.16). Since a² and b² are rational areas, p and q are rational and commensurable in length with r (D10.1.3, D10.1.4, 10.20). Since a and b are rational and commensurable in square only, ab equals the square on a medial straight line (10.21). Consequently t is rational and incommensurable in length with r (10.22).

**Step 3.** Put u = p + q and v = 2t. Then ru = a² + b² and rv = 2ab (2.1). The sum of the commensurable rational areas a² and b² is rational (10.15, 10.12, D10.1.4); hence u is rational and commensurable in length with r (10.20). Also v² = 4t² (2.4). Thus v² is commensurable with the rational area t² and is itself rational; therefore v is rational (D10.1.1, 10.12, D10.1.4, D10.1.3).

**Step 4.** Since v = 2t, v and t are commensurable in length (D10.1.1). Since t is incommensurable in length with r, so is v (10.13). Since u is commensurable in length with r, u and v are incommensurable in length (10.13). But their rationality makes their squares commensurable with the same assigned rational square, and therefore with one another (D10.1.3, 10.12, D10.1.2). Thus u and v are rational straight lines commensurable in square only.

**Step 5.** Since c = a − b, we have c² + 2ab = a² + b² (2.7). Substituting the rectangle equalities already established gives r(x + v) = ru (2.1). Equal rectangles with the same height have equal breadths, so u = x + v (6.1). Hence u > v (CN5), and x = u − v is an apotome, with whole u and annex v (10.73).

**Step 6.** Ratios of rectangles with the same height give
p : t = a² : ab = a : b,
and
t : q = ab : b² = a : b
(6.1). Therefore p : t = t : q (5.11), whence pq = t² (6.17). Since v = 2t, it follows that pq is one fourth of v² (2.4).

**Step 7.** The straight lines p and q are commensurable in length, since both are commensurable in length with r (10.12). On u = p + q, the rectangle pq is applied deficient by the square q², since uq = pq + q² (2.1). By Step 6, this applied rectangle equals one fourth of the square on v. Therefore 10.17 applies to u > v and their commensurable division p, q: there is a straight line h commensurable in length with u such that u² = v² + h².

**Step 8.** The breadth x is an apotome whose whole u is commensurable in length with the given rational straight line r, and the square on u exceeds the square on its annex v by the square on h, which is commensurable in length with u. Thus x is a first apotome (D10.3.1). Therefore the square on an apotome, applied to a rational straight line, produces as breadth a first apotome.

**USED:** 10.12, 10.13, 10.15, 10.17, 10.20, 10.21, 10.22, 10.73, 2.1, 2.4, 2.7, 5.11, 6.1, 6.12, 6.16, 6.17, CN5, D10.1.1, D10.1.2, D10.1.3, D10.1.4, D10.3.1, D2.1
**Human refs (from References field):** 10.11, 10.17, 10.20, 10.22, 10.73, 2.7, 6.1, 6.17, D10.3.1
**Jaccard:** 0.333 — AI adds ['10.12', '10.13', '10.15', '10.21', '2.1', '2.4', '5.11', '6.12', '6.16', 'CN5', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.1.4', 'D2.1']; Human adds ['10.11']

## Proposition 10.98
**Statement:** The square on a first apotome of a medial straight line applied to a rational straight line produces as breadth a second apotome.

**Step 1.** Let x be a first apotome of a medial straight line, and let r be the rational straight line to which its square is to be applied. Write u² for the square on a straight line u, and uv for the rectangle contained by u and v. By 10.74, write x = a − b, where a > b are medial straight lines commensurable in square only, and ab is rational. Thus a² and b² are commensurable areas. [10.74, D10.1.2]

**Step 2.** Construct straight lines p, q, t such that
rp = a², rq = b², and rt = ab.
These constructions are obtained by fourth proportionals and the equivalence between proportions and equal rectangles. Since a and b are medial, p and q are rational and each is incommensurable in length with r. Since ab is rational, t is commensurable in length with r. Put U = p + q and V = 2t. [6.12, 6.16, 6.17, 10.22, 10.20]

**Step 3.** Rectangles with the same height are proportional to their bases, so
p : q = rp : rq = a² : b².
Since a² and b² are commensurable, p and q are commensurable in length. Consequently U = p + q is commensurable in length with p. Because p is incommensurable in length with r, U is also incommensurable in length with r. Moreover, V = t + t is commensurable with t, and therefore with r. [6.1, 10.11, 10.15, 10.13, 10.12]

**Step 4.** Straight lines commensurable in length have commensurable squares: their squares have the ratio of a square number to a square number, and hence are commensurable. Therefore U, being commensurable in length with the rational line p, is rational; likewise V, being commensurable in length with r, is rational. Their squares are consequently commensurable with one another. But U and V are incommensurable in length, since V is commensurable with r whereas U is not. Thus U and V are rational straight lines commensurable in square only. [10.9, 10.6, 10.12, D10.1.3, 10.13]

**Step 5.** By the square identity for a line cut into b and a − b,
a² + b² = 2ab + (a − b)².
Distributing rectangles over sums gives
rU = a² + b² and rV = 2ab.
Hence rU = rV + x². Since x² is positive, U > V; subtracting the rectangle rV gives
r(U − V) = x².
Thus U − V is precisely the breadth produced by applying x² to r. [2.7, 2.1, CN5, CN3, 6.1]

**Step 6.** Using rectangles with common heights again,
p : t = a² : ab = a : b,
and
t : q = ab : b² = a : b.
Therefore p, t, q are proportional, and pq = t². Since V = 2t, the square on V is four times the square on t. Consequently pq is one quarter of V². [6.1, 6.17, 2.4]

**Step 7.** Apply the rectangle pq to U = p + q by taking p as its base and q as its height. Its deficiency from the rectangle on the whole U with height q is exactly the square q². It therefore applies one quarter of V² to U, deficient by a square, and divides U into the length-commensurable parts p and q. This makes 10.17 the direct criterion for the required square-excess condition: since U > V, that proposition gives that U² exceeds V² by the square on a straight line commensurable in length with U. [2.1, 10.17]

**Step 8.** Since U and V are rational and commensurable in square only, U − V is an apotome. Its annex V is commensurable in length with the given rational line r, and U² exceeds V² by the square on a straight line commensurable in length with U. Therefore U − V is a second apotome. By Step 5, it is the required breadth. Hence the square on a first apotome of a medial straight line, applied to a rational straight line, produces as breadth a second apotome. [10.73, D10.3.2]

**USED:** 10.11, 10.12, 10.13, 10.15, 10.17, 10.20, 10.22, 10.6, 10.73, 10.74, 10.9, 2.1, 2.4, 2.7, 6.1, 6.12, 6.16, 6.17, CN3, CN5, D10.1.2, D10.1.3, D10.3.2
**Human refs (from References field):** 10.11, 10.15, 10.17, 10.20, 10.22, 10.23, 10.73, 10.74, 2.7, 5.11, 6.1, 6.17, D10.3.2
**Jaccard:** 0.440 — AI adds ['10.12', '10.13', '10.6', '10.9', '2.1', '2.4', '6.12', '6.16', 'CN3', 'CN5', 'D10.1.2', 'D10.1.3']; Human adds ['10.23', '5.11']

## Proposition 10.99
**Statement:** The square on a second apotome of a medial straight line applied to a rational straight line produces as breadth a third apotome.

**Step 1.** Let d be a second apotome of a medial straight line, and let r be the rational straight line to which its square is applied. Write xy for the rectangle contained by x and y, and x² for the square on x [D2.1]. By the defining description in 10.75, write d = a − b, where a > b are medial straight lines commensurable in square only, and ab is medial. Thus a² and b² are commensurable [D10.1.2]. Our path is to apply the previously proved additive counterpart, 10.62, to a + b, and then identify its binomial terms using 10.42.

**Step 2.** Apply the three medial areas a², b², and ab to r, obtaining respective breadths u, v, and w. Thus ru = a², rv = b², and rw = ab. Each of u, v, and w is rational [10.22]. Moreover, u:v = a²:b², since rectangles on the same base are proportional to their breadths [6.1]. Therefore u and v are commensurable in length [10.11].

**Step 3.** Put U = u + v and V = 2w. Since u and v are commensurable, U is commensurable in length with u [10.15]; also V is commensurable in length with w, which measures it [D10.1.1]. Consequently U² is commensurable with u², and V² with w² [10.9, 10.6]. Since u and w are rational, U and V are likewise rational [10.12, D10.1.3].

**Step 4.** Distributing the rectangles and expanding the square gives
r(U + V) = a² + b² + 2ab = (a + b)² [2.1, 2.4].
Now a + b is a second bimedial straight line, because a and b are medial, commensurable in square only, and contain a medial rectangle [10.38]. Hence U + V is a third binomial [10.62], and in particular is irrational [10.36].

**Step 5.** If U and V were commensurable in length, U + V would be commensurable in length with the rational straight line U [10.15]. Its square would then be commensurable with U², making U + V rational [10.9, 10.6, 10.12, D10.1.3], contrary to Step 4. Therefore U and V are incommensurable in length. Since both are rational, their squares are commensurable [10.12, D10.1.3]. Thus U and V are commensurable in square only [D10.1.2].

**Step 6.** The square identity for a straight line cut into two parts gives
a² + b² = 2ab + (a − b)² [2.7].
Consequently rU = rV + d² [2.1]. The rectangle rU is therefore greater than rV, so U > V [CN5, 6.1]. Subtracting rV gives
r(U − V) = d² [2.1, CN3].
Thus U − V is precisely the breadth produced by applying the square on d to r [6.1].

**Step 7.** By Step 5, U and V are rational straight lines commensurable in square only; hence they exhibit a binomial division of U + V [10.36]. A binomial has only one division into its terms [10.42]. Therefore U and V, with U the greater, are the terms of the third binomial obtained in Step 4. By the definition of a third binomial, neither term is commensurable in length with r, and U² exceeds V² by the square on a straight line commensurable in length with U [D10.2.1, D10.2.3].

**Step 8.** Since U and V are rational and commensurable in square only, U − V is an apotome, with whole U and annex V [10.73]. Neither its whole nor its annex is commensurable in length with r, and the square on its whole exceeds that on its annex by the square on a straight line commensurable in length with the whole. It is therefore a third apotome [D10.3.3]. By Step 6, this is the required breadth. Hence the square on a second apotome of a medial straight line, applied to a rational straight line, produces as breadth a third apotome.

**USED:** 10.11, 10.12, 10.15, 10.22, 10.36, 10.38, 10.42, 10.6, 10.62, 10.73, 10.75, 10.9, 2.1, 2.4, 2.7, 6.1, CN3, CN5, D10.1.1, D10.1.2, D10.1.3, D10.2.1, D10.2.3, D10.3.3, D2.1
**Human refs (from References field):** 10.11, 10.13, 10.15, 10.17, 10.22, 10.23, 10.73, 10.75, 2.7, 5.11, 6.1, D10.3.3
**Jaccard:** 0.276 — AI adds ['10.12', '10.36', '10.38', '10.42', '10.6', '10.62', '10.9', '2.1', '2.4', 'CN3', 'CN5', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.2.1', 'D10.2.3', 'D2.1']; Human adds ['10.13', '10.17', '10.23', '5.11']

## Proposition 10.100
**Statement:** The square on a minor straight line applied to a rational straight line produces as breadth a fourth apotome.

**Step 1.** Let m be the given minor straight line and r the rational straight line to which its square is to be applied. Write xy for the rectangle contained by x and y. By the characterization of a minor in 10.76, there are straight lines u > v such that m = u − v, the squares u² and v² are incommensurable, u² + v² is rational, and uv is medial. Consequently n = u + v is major (10.39). We shall use the associated major and the established major-to-fourth-binomial result to obtain the required order condition.

**Step 2.** Apply u² + v² and uv separately to r, obtaining breadths p and t, so that rp = u² + v² and rt = uv. These applications can be effected by successive applications of 1.44 to the triangles composing the areas, combining the resulting rectangles by 2.1. Since the first area is rational, p is rational and commensurable in length with r (10.20). Since the second is medial, t is rational but incommensurable in length with r (10.22).

**Step 3.** Put q = 2t. Then q is commensurable in length with t, since t measures both (D10.1.1). Moreover, q² = 4t² (2.4). A common area-measure of t² and the assigned rational square therefore also measures q²; hence q is rational (D10.1.1, D10.1.2, D10.1.3). Since p and q are rational, their squares are commensurable with the same assigned rational square and therefore with one another (10.12; D10.1.2). But q is incommensurable in length with r, because it is commensurable with t; and it is consequently incommensurable in length with p, because p is commensurable with r (10.13, applied twice). Thus p and q are rational straight lines commensurable in square only.

**Step 4.** By 2.1, rq = 2rt = 2uv. Also, 2.7 gives m² + 2uv = u² + v². Therefore rp = rq + m², so rp > rq (CN5), and consequently p > q (6.1). Meanwhile, by 2.4 and 2.1,
 n² = u² + v² + 2uv = rp + rq = r(p + q).
Thus p + q is the breadth obtained by applying the square on the major n to r. It is also a binomial with greater term p and lesser term q (10.36).

**Step 5.** By 10.63, this breadth p + q is a fourth binomial. This is the direct previously proved correspondence reached from the associated major. Since a binomial has only one division into its terms (10.42), the terms determining its fourth order are precisely p and q. Hence p² exceeds q² by the square on a straight line incommensurable in length with p (D10.2.4).

**Step 6.** Let b = p − q. Since p and q are rational and commensurable in square only, b is an apotome, with whole p and annex q (10.73). Subtracting rq from the equality rp = rq + m² in Step 4 gives rp − rq = m² (CN3). By 2.1, r(p − q) = rp − rq; therefore rb = m². Thus b is the breadth obtained by applying the square on m to r.

**Step 7.** The whole p is commensurable in length with the rational straight line r by Step 2, while p² exceeds the square on its annex q by the square on a straight line incommensurable in length with p by Step 5. Therefore b is a fourth apotome (D10.3.4). Hence the square on a minor straight line, applied to a rational straight line, produces as breadth a fourth apotome.

**USED:** 1.44, 10.12, 10.13, 10.20, 10.22, 10.36, 10.39, 10.42, 10.63, 10.73, 10.76, 2.1, 2.4, 2.7, 6.1, CN3, CN5, D10.1.1, D10.1.2, D10.1.3, D10.2.4, D10.3.4
**Human refs (from References field):** 10.11, 10.18, 10.20, 10.22, 10.73, 10.76, 2.7, 5.11, 6.1, 6.17, D10.3.4
**Jaccard:** 0.269 — AI adds ['1.44', '10.12', '10.13', '10.36', '10.39', '10.42', '10.63', '2.1', '2.4', 'CN3', 'CN5', 'D10.1.1', 'D10.1.2', 'D10.1.3', 'D10.2.4']; Human adds ['10.11', '10.18', '5.11', '6.17']

## Proposition 10.101
**Statement:** The square on the straight line which produces with a rational area a medial whole, if applied to a rational straight line, produces as breadth a fifth apotome.

**Step 1.** Let x be the given straight line, let r be the rational straight line to which its square is applied, and let t be the resulting breadth; thus rt = x². Here products denote rectangular areas. By the defining characterization in 10.77, write x = a − b, where a > b, the squares on a and b are incommensurable, M = a² + b² is medial, and R = 2ab is rational. [10.77]

**Step 2.** The area ab is commensurable with R, since it measures R twice. Since R is rational, ab is therefore rational also. Consequently a + b is the straight line called the side of a rational plus a medial area. Our path is to use this corresponding sum and the previously established application theorem 10.64, which supplies the required square-excess condition directly. [D10.1.1, D10.1.4, 10.12, 10.40]

**Step 3.** Apply R to r, and call its breadth q. Then rq = R, and q is rational and commensurable in length with r. Put p = t + q. By the square identity for a line cut into two parts,
M = a² + b² = (a − b)² + 2ab = x² + R.
Hence, by addition of rectangles on the same base,
rp = rt + rq = x² + R = M.
Since M is medial, p is rational and incommensurable in length with r. Moreover, p > q and t = p − q. [10.20, 2.7, 2.1, CN1, 10.22, CN5]

**Step 4.** Since p and q are rational, their squares are commensurable with the fixed rational square and therefore with one another. But q is commensurable in length with r, whereas p is incommensurable in length with r; consequently p and q are incommensurable in length. Thus p and q are rational straight lines commensurable in square only, and p + q is a binomial with terms p and q. [D10.1.3, 10.12, 10.13, 10.36]

**Step 5.** The square on a + b satisfies
(a + b)² = a² + b² + 2ab = M + R = rp + rq = r(p + q).
Thus p + q is the breadth obtained by applying the square on a + b to r. Since a + b is the side of a rational plus a medial area, this breadth is a fifth binomial. [2.4, 2.1, CN1, 10.64]

**Step 6.** A binomial has only one division into its terms. Therefore the fifth binomial just obtained has precisely the greater term p and the lesser term q identified in Step 4. By the definition of a fifth binomial, there is a straight line d such that p² = q² + d², with d incommensurable in length with p; its lesser term q is commensurable in length with r. [10.42, D10.2.4, D10.2.5]

**Step 7.** Since p and q are rational and commensurable in square only, t = p − q is an apotome, with whole p and annex q. The square on its whole exceeds the square on its annex by the square on d, which is incommensurable in length with the whole, while its annex is commensurable in length with r. These are exactly the defining conditions of a fifth apotome. Therefore the square on the given straight line, applied to the rational straight line r, produces as breadth a fifth apotome. [10.73, D10.3.4, D10.3.5]

**USED:** 10.12, 10.13, 10.20, 10.22, 10.36, 10.40, 10.42, 10.64, 10.73, 10.77, 2.1, 2.4, 2.7, CN1, CN5, D10.1.1, D10.1.3, D10.1.4, D10.2.4, D10.2.5, D10.3.4, D10.3.5
**Human refs (from References field):** 10.11, 10.18, 10.20, 10.22, 10.73, 10.77, 2.7, 6.1, D10.3.5
**Jaccard:** 0.240 — AI adds ['10.12', '10.13', '10.36', '10.40', '10.42', '10.64', '2.1', '2.4', 'CN1', 'CN5', 'D10.1.1', 'D10.1.3', 'D10.1.4', 'D10.2.4', 'D10.2.5', 'D10.3.4']; Human adds ['10.11', '10.18', '6.1']

## Proposition 10.102
**Statement:** The square on the straight line which produces with a medial area a medial whole, if applied to a rational straight line, produces as breadth a sixth apotome.

**Step 1.** Let x be the given straight line which produces with a medial area a medial whole, and let r be the rational straight line to which its square is applied. By the defining characterization in 10.78, write x = a − b, where a > b, the squares a² and b² are incommensurable, and the areas S = a² + b² and T = 2ab are medial and incommensurable with one another. Here products denote rectangular areas. [10.78]

**Step 2.** Construct positive straight lines p, q, h as fourth proportionals so that r:a = a:p, r:b = b:q, and r:a = b:h. Then rp = a², rq = b², and rh = ab. Put u = p + q and v = 2h. Distributing the rectangles gives ru = S and rv = T. [6.12, 6.16, 2.1]

**Step 3.** Since S and T are medial areas applied to the rational straight line r, their breadths u and v are rational and each is incommensurable in length with r. Moreover, u:v = S:T, so u and v are incommensurable in length. Their squares are nevertheless commensurable, since u and v are rational. Thus u and v are commensurable in square only. [10.22, 6.1, 10.11, D10.1.3, 10.12]

**Step 4.** Since x = a − b, the square identity gives S = T + x². Hence S > T and consequently u > v. Subtracting rv = T from ru = S gives r(u − v) = x². Thus u − v is exactly the breadth produced by applying x² to r. Since u and v are rational and commensurable in square only, this breadth is an apotome, with whole u and annex v. [2.7, 6.1, 2.1, CN3, 10.73]

**Step 5.** The rectangles rp and rq have the same height, so p:q = a²:b². Since a² and b² are incommensurable, p and q are incommensurable in length. [6.1, 10.11]

**Step 6.** Comparing rectangles of equal height gives p:h = rp:rh = a²:ab = a:b, and h:q = rh:rq = ab:b² = a:b. Therefore p:h = h:q, whence pq = h². Since v = 2h, its square is four times h². Consequently pq is one fourth of v². [6.1, 5.11, 6.17, 2.4]

**Step 7.** Regard the rectangle pq as applied to u = p + q, occupying the segment p and having height q. It is deficient by the square on q, and its area is one fourth of v². Its application divides u into the incommensurable segments p and q. Proposition 10.18 therefore shows that u² exceeds v² by the square on a straight line incommensurable in length with u. This is the direct path: 10.18 applies immediately to the exhibited incommensurable division and supplies precisely the required square-excess condition. [10.18]

**Step 8.** The breadth u − v is an apotome; neither its whole u nor its annex v is commensurable in length with the rational straight line r; and u² exceeds v² by the square on a straight line incommensurable in length with u. These are exactly the conditions defining a sixth apotome. Therefore the square on x, applied to r, produces as breadth a sixth apotome. [D10.3.6]

**USED:** 10.11, 10.12, 10.18, 10.22, 10.73, 10.78, 2.1, 2.4, 2.7, 5.11, 6.1, 6.12, 6.16, 6.17, CN3, D10.1.3, D10.3.6
**Human refs (from References field):** 10.11, 10.18, 10.22, 10.73, 10.78, 2.7, 6.1, D10.3.6
**Jaccard:** 0.471 — AI adds ['10.12', '2.1', '2.4', '5.11', '6.12', '6.16', '6.17', 'CN3', 'D10.1.3']

## Proposition 10.103
**Statement:** A straight line commensurable in length with an apotome is an apotome and the same in order.

**Step 1.** Let a be an apotome, and let b be commensurable in length with a. Fix the assigned rational straight line r. By the definition of an apotome in 10.73, write a = u − v, where u > v and u, v are rational straight lines commensurable in square only. Write x² for the square on a straight line x. Our path is to transfer the whole u and annex v proportionally, then apply 10.14 directly to preserve the square-excess condition determining the order. [10.73; D10.1.3]

**Step 2.** Construct V such that a:b = v:V, and put U = b + V. Since u = a + v, addition of the antecedents and consequents gives
u:U = a:b = v:V.
Alternating u:U = v:V also gives u:v = U:V. Moreover, U − V = b. [6.12; 5.12; 5.16]

**Step 3.** Since a and b are commensurable in length, the proportions in Step 2 imply that u and U are commensurable in length, and likewise v and V. Here 10.11 applies directly because the proportional pairs are already available. Consequently, u² and U² have the ratio of a square number to a square number, as do v² and V²; hence each pair of squares is commensurable. [10.11; 10.9; 10.6]

**Step 4.** Because u and v are rational, their squares are commensurable with r². Step 3 and transitivity of commensurability therefore show that U² and V² are each commensurable with r², and hence also with one another. Thus U and V are rational and commensurable in square. But u and v are incommensurable in length; the proportion u:v = U:V therefore makes U and V incommensurable in length also. They are consequently rational straight lines commensurable in square only. Since U > V and b = U − V, b is an apotome. [D10.1.2; D10.1.3; 10.12; 10.11; 10.73]

**Step 5.** The corresponding wholes u, U have the same commensurability status in length with r: if u is commensurable with r, so is U, since U is commensurable with u; if u is incommensurable with r, so is U. The same argument applies to the corresponding annexes v, V. Thus the alternatives “whole commensurable with r,” “annex commensurable with r,” and “neither commensurable with r” are preserved. [10.12; 10.13]

**Step 6.** Apply 10.14 to u:v = U:V. If u² exceeds v² by the square on a straight line commensurable in length with u, then U² exceeds V² by the square on a straight line commensurable in length with U. If the former excess is instead the square on a straight line incommensurable in length with u, the latter excess is likewise the square on a straight line incommensurable in length with U. Thus the other condition determining the order is preserved as well. [10.14]

**Step 7.** When the excess-square side is commensurable with the whole, Step 5 preserves respectively the conditions for a first, second, or third apotome. [D10.3.1; D10.3.2; D10.3.3] When that side is incommensurable with the whole, Step 5 preserves respectively the conditions for a fourth, fifth, or sixth apotome. [D10.3.4; D10.3.5; D10.3.6] Therefore b is an apotome of exactly the same order as a, as required.

**USED:** 10.11, 10.12, 10.13, 10.14, 10.6, 10.73, 10.9, 5.12, 5.16, 6.12, D10.1.2, D10.1.3, D10.3.1, D10.3.2, D10.3.3, D10.3.4, D10.3.5, D10.3.6
**Human refs (from References field):** 10.11, 10.12, 10.13, 10.14, 10.73, 5.12, 5.16, 6.12
**Jaccard:** 0.444 — AI adds ['10.6', '10.9', 'D10.1.2', 'D10.1.3', 'D10.3.1', 'D10.3.2', 'D10.3.3', 'D10.3.4', 'D10.3.5', 'D10.3.6']

## Proposition 10.104
**Statement:** A straight line commensurable with an apotome of a medial straight line is an apotome of a medial straight line and the same in order.

**Step 1.** Let a be an apotome of a medial straight line, and let b be commensurable in length with a. Take the assigned rational straight line r (D10.1.3). Our path is to transfer the order through the breadths of their square applications, so that the preceding preservation theorem for apotomes, 10.103, applies directly without reconstructing the medial terms.

**Step 2.** Construct straight lines u and v such that r:a = a:u and r:b = b:v (6.12). Then the rectangle contained by r and u equals the square on a, and the rectangle contained by r and v equals the square on b (6.17). Thus u and v are the breadths obtained by applying those squares to the same rational straight line r.

**Step 3.** Since a and b are commensurable in length, their squares have the ratio of a square number to a square number (10.9), and hence are commensurable areas (10.6). Moreover, the rectangles contained by r,u and r,v have the ratio u:v, since they have the same height r (6.1). Consequently u and v are commensurable in length (10.11).

**Step 4.** If a is a first apotome of a medial straight line, its square applied to r produces a second apotome; thus u is a second apotome (10.98). If a is a second apotome of a medial straight line, the corresponding breadth u is a third apotome (10.99).

**Step 5.** Since v is commensurable in length with u, it is an apotome of the same order as u (10.103). Therefore v is a second apotome in the first case and a third apotome in the second case.

**Step 6.** The square on b is the rectangle contained by the rational straight line r and v. In the first case, v is a second apotome, so b is a first apotome of a medial straight line (10.92). In the second case, v is a third apotome, so b is a second apotome of a medial straight line (10.93). Therefore a straight line commensurable with an apotome of a medial straight line is itself an apotome of a medial straight line, and the same in order.

**USED:** 10.103, 10.11, 10.6, 10.9, 10.92, 10.93, 10.98, 10.99, 6.1, 6.12, 6.17, D10.1.3
**Human refs (from References field):** 10.11, 10.13, 10.23, 10.74, 10.75, 5.12, 5.16, 6.12, D10.1.4
**Jaccard:** 0.105 — AI adds ['10.103', '10.6', '10.9', '10.92', '10.93', '10.98', '10.99', '6.1', '6.17', 'D10.1.3']; Human adds ['10.13', '10.23', '10.74', '10.75', '5.12', '5.16', 'D10.1.4']

## Proposition 10.105
**Statement:** A straight line commensurable with a minor straight line is minor.

**Step 1.** Let a be a minor straight line, and let b be commensurable in length with a. Choose the assigned rational straight line r (D10.1.3). Construct fourth proportionals p and q such that r:a = a:p and r:b = b:q (6.12). Then the rectangles contained by r,p and by r,q equal the squares on a and b respectively (6.17).

**Step 2.** The square on the minor a has thus been applied to the rational straight line r, producing breadth p. Therefore p is a fourth apotome (10.100). This selects the fourth-apotome route: it directly classifies the breadth associated with the given minor, without reconstructing the minor’s defining subtraction.

**Step 3.** Since a and b are commensurable in length, their squares have the ratio of a square number to a square number (10.9). The rectangles contained by r,p and by r,q have the same altitude r, so their ratio is p:q (6.1). Since these rectangles equal the squares on a and b, p:q is consequently a ratio of numbers. Hence p and q are commensurable in length (10.6).

**Step 4.** A straight line commensurable in length with an apotome is an apotome of the same order (10.103). Since p is a fourth apotome, q is therefore a fourth apotome.

**Step 5.** The square on b equals the rectangle contained by the rational straight line r and the fourth apotome q. The side of such an area is minor (10.94). Thus b is minor, proving that a straight line commensurable with a minor straight line is minor.

**USED:** 10.100, 10.103, 10.6, 10.9, 10.94, 6.1, 6.12, 6.17, D10.1.3
**Human refs (from References field):** 10.11, 10.13, 10.23, 10.76, 5.12, 5.16, 5.18, 6.22, D10.1.4
**Jaccard:** 0.000 — AI adds ['10.100', '10.103', '10.6', '10.9', '10.94', '6.1', '6.12', '6.17', 'D10.1.3']; Human adds ['10.11', '10.13', '10.23', '10.76', '5.12', '5.16', '5.18', '6.22', 'D10.1.4']

## Proposition 10.106
**Statement:** A straight line commensurable with that which produces with a rational area a medial whole is a straight line which produces with a rational area a medial whole.

**Step 1.** Let a be a straight line which produces with a rational area a medial whole, and let b be commensurable in length with a. Choose the assigned rational straight line r [D10.1.3]. We use the fifth-apotome route: 10.101 applies directly to the given type, 10.103 preserves the resulting apotome’s order, and 10.95 returns to the required type, avoiding reconstruction of its defining subtraction.

**Step 2.** Since a and b are commensurable in length, their squares have the ratio of a square number to a square number [10.9]. Consequently, the squares on a and b are commensurable areas [10.6].

**Step 3.** Construct straight lines x and y such that r:a = a:x and r:b = b:y [6.12]. The rectangle contained by r and x therefore equals the square on a, and the rectangle contained by r and y equals the square on b [6.17]. Thus these rectangles apply the respective squares to the same rational straight line r. Since a is of the given type, x is a fifth apotome [10.101].

**Step 4.** Rectangles having the same height are to one another as their bases [6.1]. Hence the square on a is to the square on b as x is to y. The squares are commensurable by Step 2, so x and y are commensurable in length [10.11]. Since x is a fifth apotome, y is also an apotome of the same order, namely a fifth apotome [10.103].

**Step 5.** The rectangle contained by the rational straight line r and the fifth apotome y has as its square-side a straight line which produces with a rational area a medial whole [10.95]. By Step 3, that rectangle equals the square on b, so b is its square-side. Therefore b is a straight line which produces with a rational area a medial whole, as required.

**USED:** 10.101, 10.103, 10.11, 10.6, 10.9, 10.95, 6.1, 6.12, 6.17, D10.1.3
**Human refs (from References field):** 10.77
**Jaccard:** 0.000 — AI adds ['10.101', '10.103', '10.11', '10.6', '10.9', '10.95', '6.1', '6.12', '6.17', 'D10.1.3']; Human adds ['10.77']

## Proposition 10.107
**Statement:** A straight line commensurable with that which produces with a medial area a medial whole is itself also a straight line which produces with a medial area a medial whole.

**Step 1.** Let a be a straight line which produces with a medial area a medial whole, and let b be commensurable in length with a. Fix the assigned rational straight line r. Write S(t) for the square on a straight line t, and R(s,t) for the rectangle contained by s and t. [D10.1.3; D2.1]

**Step 2.** Construct third proportionals x and y such that r:a = a:x and r:b = b:y. Then R(r,x) = S(a) and R(r,y) = S(b). Thus x and y are the breadths obtained by applying the respective squares to the same rational straight line r. [6.11; 6.17]

**Step 3.** Since a produces with a medial area a medial whole, x is a sixth apotome, relative to r. We choose this route because applying the square immediately gives an apotome whose order can be preserved by the previously proved commensurability theorem. [10.102]

**Step 4.** Since a and b are commensurable in length, S(a):S(b) is the ratio of a square number to a square number; consequently these square areas are commensurable. Moreover, the rectangles R(r,x) and R(r,y), having the same height r, are to one another as their bases x and y. Hence
x:y = R(r,x):R(r,y) = S(a):S(b).
It follows that x and y are commensurable in length. [10.9; 10.6; 6.1; 10.11]

**Step 5.** A straight line commensurable in length with an apotome is itself an apotome of the same order. Since x is a sixth apotome, y is therefore also a sixth apotome relative to the same rational straight line r. [10.103]

**Step 6.** The rectangle contained by the rational straight line r and the sixth apotome y has as its square-side a straight line which produces with a medial area a medial whole. But this rectangle equals S(b), so its square-side is b. Therefore b also produces with a medial area a medial whole, as required. [10.96; Step 2]

**USED:** 10.102, 10.103, 10.11, 10.6, 10.9, 10.96, 6.1, 6.11, 6.17, D10.1.3, D2.1
**Human refs (from References field):** 10.78
**Jaccard:** 0.000 — AI adds ['10.102', '10.103', '10.11', '10.6', '10.9', '10.96', '6.1', '6.11', '6.17', 'D10.1.3', 'D2.1']; Human adds ['10.78']

## Proposition 10.108
**Statement:** If from a rational area a medial area be subtracted, the âsideâ of the remaining area becomes one of two irrational straight lines, either an apotome or a minor straight line.

**Step 1.** Let R be a rational area and M a medial area smaller than R. Apply both areas to the assigned rational straight line r, obtaining rectangular breadths a and b respectively. Thus R = rect(r,a) and M = rect(r,b), with a > b because the rectangles have the same height (6.1). By 10.20, a is rational and commensurable in length with r; by 10.22, b is rational and incommensurable in length with r.

**Step 2.** Since a and b are rational, their squares are each commensurable with the square on r, and consequently with one another (D10.1.3, 10.12). But a and b cannot be commensurable in length: otherwise, since a is commensurable in length with r, b would also be commensurable in length with r, contrary to Step 1 (10.12). Therefore a and b are commensurable in square only, and c = a − b is an apotome (10.73).

**Step 3.** By the distributive relation for rectangles, rect(r,a) = rect(r,b) + rect(r,c) (2.1). Subtracting equal areas therefore gives R − M = rect(r,c) (CN3). Let s be the side of a square equal to this remaining area (2.14).

**Step 4.** Construct a straight line d whose square equals the excess of the square on a over the square on b (2.14). Either d is commensurable in length with a or it is incommensurable with a (D10.1.1). Since the whole term a is commensurable in length with r, these alternatives classify c directly as a first or a fourth apotome (D10.3.1, D10.3.4). Thus the natural route is to use the corresponding area-to-side propositions 10.91 and 10.94.

**Step 5.** If d is commensurable in length with a, then c is a first apotome relative to r (D10.3.1). The remaining area is contained by the rational straight line r and this first apotome. Hence its side s is an apotome (10.91).

**Step 6.** If d is incommensurable in length with a, then c is a fourth apotome relative to r (D10.3.4). The remaining area is therefore contained by a rational straight line and a fourth apotome, so its side s is minor (10.94).

**Step 7.** The two cases exhaust the possibilities. An apotome is irrational by 10.73, and a minor straight line is irrational by 10.76. Consequently, the side of the area remaining when a medial area is subtracted from a rational area is one of the two stated irrational straight lines: either an apotome or a minor straight line.

**USED:** 10.12, 10.20, 10.22, 10.73, 10.76, 10.91, 10.94, 2.1, 2.14, 6.1, CN3, D10.1.1, D10.1.3, D10.3.1, D10.3.4
**Human refs (from References field):** 10.13, 10.20, 10.22, 10.73, 10.91, 10.94, D10.3.1, D10.3.4
**Jaccard:** 0.438 — AI adds ['10.12', '10.76', '2.1', '2.14', '6.1', 'CN3', 'D10.1.1', 'D10.1.3']; Human adds ['10.13']

## Proposition 10.109
**Statement:** If from a medial area a rational area be subtracted, there arise two other irrational straight lines, either a first apotome of a medial straight line or a straight line which produces with a rational area a medial whole.

**Step 1.** Let M be a medial area and R a rational area smaller than M. Let r be the assigned rational straight line. Apply M and R to r, obtaining breadths a and b respectively, so that M = ra and R = rb, where juxtaposition denotes a rectangle. Then a is rational and incommensurable in length with r, while b is rational and commensurable in length with r [10.22, 10.20]. We choose this application route because the earlier rectangle-to-side classifications will apply directly.

**Step 2.** Rectangles with the same base are proportional to their breadths; therefore M > R implies a > b [6.1, 5.14]. Since a and b are rational, their squares are each commensurable with the square on r, and hence with one another [D10.1.3, 10.12]. Thus a and b are commensurable in square [D10.1.2]. But b is commensurable in length with r, whereas a is not; consequently a and b are incommensurable in length [10.13]. They are therefore rational straight lines commensurable in square only.

**Step 3.** Put x = a − b. By the preceding step, x is an apotome, with whole a and annex b [10.73]. Moreover, ra = rb + rx, so the remaining area M − R equals rx [2.3, CN3]. Construct a square equal to this remaining area, and denote its side by s [2.14]. Thus s² = rx = M − R.

**Step 4.** Construct a straight line c whose square equals the excess of the square on a over the square on b; thus a² = b² + c² [2.14]. Either c is commensurable in length with a or it is incommensurable in length with a; these alternatives exhaust the possibilities [D10.1.1]. In both cases the annex b is commensurable in length with the assigned rational line r, as established in Step 1.

**Step 5.** Suppose first that c is commensurable in length with a. Since a² exceeds b² by c² and the annex b is commensurable in length with r, x is a second apotome [D10.3.2]. The area rx is therefore contained by a rational straight line and a second apotome. Its square-side s is consequently a first apotome of a medial straight line [10.92], and is irrational [10.74].

**Step 6.** Suppose instead that c is incommensurable in length with a. Since the annex b is commensurable in length with r, x is now a fifth apotome [D10.3.5]. Hence the square-side s of rx is a straight line which produces with a rational area a medial whole [10.95], and is irrational [10.77]. The two cases are exhaustive. Therefore the side of the area remaining when a rational area is subtracted from a medial area is either a first apotome of a medial straight line or a straight line which produces with a rational area a medial whole, as required.

**USED:** 10.12, 10.13, 10.20, 10.22, 10.73, 10.74, 10.77, 10.92, 10.95, 2.14, 2.3, 5.14, 6.1, CN3, D10.1.1, D10.1.2, D10.1.3, D10.3.2, D10.3.5
**Human refs (from References field):** 10.13, 10.73, 10.92, 10.95, D10.3.2, D10.3.5
**Jaccard:** 0.316 — AI adds ['10.12', '10.20', '10.22', '10.74', '10.77', '2.14', '2.3', '5.14', '6.1', 'CN3', 'D10.1.1', 'D10.1.2', 'D10.1.3']

## Proposition 10.110
**Statement:** If from a medial area there be subtracted a medial area incommensurable with the whole, the two remaining irrational straight lines arise, either a second apotome of a medial straight line or a straight line which produces with a medial area a medial whole.

**Step 1.** Let M and N be medial areas, with M greater than N and incommensurable with N. Apply both areas to the same assigned rational straight line r, obtaining rectangles with respective breadths a and b. By 10.22, a and b are rational straight lines, each incommensurable in length with r. Moreover, M:N = a:b, and a > b, since rectangles on the same base are proportional to their breadths [6.1]. We use this common-base route to bring the remainder directly under the established area-to-side propositions.

**Step 2.** Since M and N are incommensurable, the proportion M:N = a:b shows that a and b are incommensurable in length [10.11]. Since both are rational, their squares are commensurable with the square on r, and therefore with one another [D10.1.3, 10.12]. Thus a and b are commensurable in square only [D10.1.2]. Consequently, c = a − b is an apotome, whose whole is a and whose annex is b [10.73].

**Step 3.** Cutting a into the parts b and c divides the rectangle contained by r and a into the rectangles contained by r and b, and by r and c [2.1]. Subtracting the rectangle equal to N from that equal to M therefore gives
M − N = the rectangle contained by r and c [CN3].

**Step 4.** Construct a straight line d whose square equals the excess of the square on a over the square on b [2.14]. Thus a² = b² + d². The straight lines d and a are either commensurable or incommensurable in length [D10.1.1]. These give the two cases below.

**Step 5.** Suppose d is commensurable in length with a. Neither the whole a nor the annex b is commensurable in length with the assigned rational straight line r, by Step 1. Hence c is a third apotome relative to r [D10.3.3]. The rectangle contained by r and c therefore has as its side a second apotome of a medial straight line [10.93]. By Step 3, this is the side of M − N.

**Step 6.** Suppose instead that d is incommensurable in length with a. Again neither a nor b is commensurable in length with r. Hence c is a sixth apotome relative to r [D10.3.6]. The rectangle contained by r and c therefore has as its side a straight line which produces with a medial area a medial whole [10.96]. By Step 3, this is the side of M − N.

**Step 7.** The alternatives in Step 4 are exhaustive. Therefore the side of the remaining area is either a second apotome of a medial straight line or a straight line which produces with a medial area a medial whole; both are irrational by the cited area-to-side propositions [10.93, 10.96]. This proves the proposition.

**USED:** 10.11, 10.12, 10.22, 10.73, 10.93, 10.96, 2.1, 2.14, 6.1, CN3, D10.1.1, D10.1.2, D10.1.3, D10.3.3, D10.3.6
**Human refs (from References field):** 10.11, 10.22, 10.73, 10.93, 10.96, 6.1, D10.3.3, D10.3.6
**Jaccard:** 0.533 — AI adds ['10.12', '2.1', '2.14', 'CN3', 'D10.1.1', 'D10.1.2', 'D10.1.3']

## Proposition 10.111
**Statement:** The apotome is not the same with the binomial straight line.

**Step 1.** Let r be the assigned rational straight line, and suppose, for a contradiction, that a straight line x is both an apotome and a binomial. Apply the square on x to r, and call the resulting breadth y. Since x is binomial, y is a first binomial (10.60); since x is an apotome, y is a first apotome (10.97). This square-application route reduces both descriptions directly to their first orders, avoiding distinctions among the six orders.

**Step 2.** From the first-binomial description, write y = b + c, where b > c and b, c are rational straight lines commensurable in square only (10.36); moreover, b is commensurable in length with r (D10.2.1). From the first-apotome description, write y = a − d, where a, d are rational straight lines commensurable in square only (10.73); moreover, a is commensurable in length with r (D10.3.1).

**Step 3.** The equality b + c = a − d gives a = b + c + d. Thus, putting t = a − b, we have t = c + d, and therefore t > c (CN2, CN3, CN5).

**Step 4.** Since a and b are each commensurable in length with r, they are commensurable in length with one another (10.12). Since a = b + t, the converse assertion of 10.15 shows that t and b are commensurable in length. Consequently t is commensurable in length with r (10.12). By 10.9 the squares on t and r have the ratio of a square number to a square number, and hence are commensurable by 10.6. Therefore t is rational (D10.1.3).

**Step 5.** The lines b and c are incommensurable in length, whereas t and b are commensurable in length. Hence t and c are incommensurable in length (10.13). But t and c are rational, so their squares are each commensurable with the square on r (D10.1.3), and therefore with one another (10.12). Thus t and c are rational straight lines commensurable in square only.

**Step 6.** Since t > c and t − c = d, the subtraction criterion 10.73 applies directly: d is irrational. But d is rational by Step 2, contradicting the distinction between rational and irrational straight lines (D10.1.3). Therefore no straight line can be both an apotome and a binomial: the apotome is not the same with the binomial straight line.

**USED:** 10.12, 10.13, 10.15, 10.36, 10.6, 10.60, 10.73, 10.9, 10.97, CN2, CN3, CN5, D10.1.3, D10.2.1, D10.3.1
**Human refs (from References field):** 10.12, 10.13, 10.15, 10.60, 10.73, 10.97, D10.2.1, D10.3.1
**Jaccard:** 0.533 — AI adds ['10.36', '10.6', '10.9', 'CN2', 'CN3', 'CN5', 'D10.1.3']

## Proposition 10.112
**Statement:** The square on a rational straight line applied to the binomial straight line produces as breadth an apotome the terms of which are commensurable with the terms of the binomial and moreover in the same ratio; and further the apotome so arising will have the same order as the binomial straight line.

**Step 1.** Let the given binomial be L = a + b, where a > b. Its terms a and b are rational straight lines commensurable in square only (10.36). Keep fixed the assigned rational straight line with respect to which rationality and order are determined. Let r be the rational straight line whose square is applied, and let h be the resulting breadth; thus Lh = r², where juxtaposition denotes a rectangle (D2.1).

Put t = a − b. Then t is an apotome, with whole a and annex b (10.73). Moreover, t has the same order as L: the greater term and lesser term of L are exactly the whole and annex of t, respectively, so both the condition concerning the difference a² − b² and the conditions concerning commensurability with the assigned rational line are unchanged (D10.2.1, D10.2.2, D10.2.3, D10.2.4, D10.2.5, D10.2.6; D10.3.1, D10.3.2, D10.3.3, D10.3.4, D10.3.5, D10.3.6).

**Step 2.** Let D be the rectangle Lt. By 2.5,
D = (a + b)(a − b) = a² − b².
Since a² and b² are commensurable, their positive difference D is commensurable with a² (10.15). Since a is rational, D is therefore a rational area (10.12, D10.1.4). The area r² is also rational; hence D and r², being commensurable with the square on the assigned rational line, are commensurable with one another (D10.1.4, 10.12).

**Step 3.** The rectangles Lh and Lt have the same altitude L. Therefore their areas are as their breadths (6.1):
h : t = Lh : Lt = r² : D.
Consequently h and t are commensurable in length (10.11). The direct path is now to apply the established preservation theorem 10.103, rather than reclassify six cases: h is an apotome of the same order as t, and hence of the same order as L.

**Step 4.** Construct fourth proportionals u and v such that
t : h = a : u,    t : h = b : v
(6.12). Because t and h are commensurable, a and u are commensurable in length, and b and v are commensurable in length (10.11). Also a : u = b : v (5.11), so, alternately,
a : b = u : v
(5.16). Since a > b, the proportion a : u = b : v gives u > v (5.14).

**Step 5.** Since the wholes a and u have the same ratio as the subtracted parts b and v, their remainders have that same ratio (5.19):
(a − b) : (u − v) = a : u.
Using a − b = t and a : u = t : h, we obtain
t : (u − v) = t : h
(5.11). Therefore u − v = h (5.9).

**Step 6.** The length-commensurabilities of u with a and of v with b imply the corresponding commensurabilities of their squares (10.9, 10.6). Since a and b are rational, u and v are rational as well, and their squares are commensurable with one another (10.12, D10.1.3). But a and b are incommensurable in length, so the proportion a : b = u : v implies that u and v are also incommensurable in length (10.11). Thus u and v are rational straight lines commensurable in square only, and h = u − v is an apotome with whole u and annex v (10.73).

Its terms u and v are respectively commensurable in length with a and b, and u : v = a : b, by Step 4. Its order is the same as that of L by Step 3. Therefore the square on the rational straight line, applied to the binomial, produces precisely an apotome having all the asserted properties.

**USED:** 10.103, 10.11, 10.12, 10.15, 10.36, 10.6, 10.73, 10.9, 2.5, 5.11, 5.14, 5.16, 5.19, 5.9, 6.1, 6.12, D10.1.3, D10.1.4, D10.2.1, D10.2.2, D10.2.3, D10.2.4, D10.2.5, D10.2.6, D10.3.1, D10.3.2, D10.3.3, D10.3.4, D10.3.5, D10.3.6, D2.1
**Human refs (from References field):** 10.11, 10.12, 10.14, 10.15, 10.20, 10.36, 10.73, 5.11, 5.12, 5.14, 5.16, 5.17, 6.16, 6.22, D5.9
**Jaccard:** 0.211 — AI adds ['10.103', '10.6', '10.9', '2.5', '5.19', '5.9', '6.1', '6.12', 'D10.1.3', 'D10.1.4', 'D10.2.1', 'D10.2.2', 'D10.2.3', 'D10.2.4', 'D10.2.5', 'D10.2.6', 'D10.3.1', 'D10.3.2', 'D10.3.3', 'D10.3.4', 'D10.3.5', 'D10.3.6', 'D2.1']; Human adds ['10.14', '10.20', '5.12', '5.17', '6.16', '6.22', 'D5.9']

## Proposition 10.113
**Statement:** The square on a rational straight line, if applied to an apotome, produces as, breadth the binomial straight line the terms of which are commensurable with the terms of the apotome and in the same ratio; and further the binomial so arising has the same order as the apotome.

**Step 1.** Let r be the given rational straight line, and let A be the given apotome. Write A = u − v, where u > v are its whole and annex: thus u and v are rational and commensurable in square only [10.73]. Let X be the breadth produced by applying the square on r to A, so that AX = r², where juxtaposition denotes a rectangle [D2.1]. Our route is to establish that X is commensurable with an auxiliary binomial, invoke 10.66, and then apply 10.112 to the same rectangle with its sides interchanged.

**Step 2.** Put S = u + v. Since u and v are rational and commensurable in square only, S is binomial [10.36]. Let T be the rectangle AS. Then
T + v² = u².
For this identity we use 2.5: a line of length 2u is divided equally into u, u and unequally into u − v, u + v; the distance between the division points is v. Thus its unequal parts are exactly A and S, making 2.5 directly applicable [2.5].

**Step 3.** Since u, v, and r are rational, their squares are each commensurable with the square on the assigned rational straight line, and hence are mutually commensurable [D10.1.2, D10.1.3, 10.12]. In particular, the whole area u² = T + v² is commensurable with v². The converse part of 10.15 therefore shows that T is commensurable with v². Since v² is also commensurable with r², T is commensurable with r² [10.15, 10.12].

**Step 4.** The rectangles T = AS and r² = AX have the same height A. Consequently,
T : r² = S : X
[6.1]. Because T and r² are commensurable, S and X are commensurable in length [10.11].

**Step 5.** Since S is binomial and X is commensurable with it in length, X is itself binomial [10.66]. Denote its greater and lesser terms by c and d, so that X = c + d.

**Step 6.** Regard the original rectangle AX = r² as applied to X. Its breadth is precisely the original apotome A [D2.1]. Proposition 10.112 now applies: the terms of A are respectively commensurable in length with the terms of X, their ratios are equal, and the apotome and binomial have the same order. Thus u is commensurable in length with c, v with d, and
u : v = c : d;
moreover, X has the same order as A [10.112]. Therefore the square on the rational straight line, applied to the given apotome, produces exactly the binomial breadth asserted.

**USED:** 10.11, 10.112, 10.12, 10.15, 10.36, 10.66, 10.73, 2.5, 6.1, D10.1.2, D10.1.3, D2.1
**Human refs (from References field):** 10.11, 10.12, 10.14, 10.15, 10.20, 10.36, 10.73, 5.11, 5.14, 5.16, 5.19, 6.16, D10.1.3, D5.9
**Jaccard:** 0.300 — AI adds ['10.112', '10.66', '2.5', '6.1', 'D10.1.2', 'D2.1']; Human adds ['10.14', '10.20', '5.11', '5.14', '5.16', '5.19', '6.16', 'D5.9']

## Proposition 10.114
**Statement:** If an area be contained by an apotome and the binomial straight line the terms of which are commensurable with the terms of the apotome and in the same ratio, the âsideâ of the area is rational.

**Step 1.** Write the given apotome as x = a − b and the given binomial as y = c + d, with corresponding terms a, c and b, d. By hypothesis, a and c are commensurable in length, b and d are commensurable in length, and a:b = c:d. Let E be the rectangle contained by x and y. We must prove that the side of a square equal to E is rational. (Hypothesis; D2.1.)

**Step 2.** Let r be the assigned rational straight line, and let Q be its square. Apply Q to x. By 10.113, the resulting breadth is a binomial z = e + f whose terms satisfy a:b = e:f, with a commensurable in length with e and b commensurable in length with f; moreover, the rectangle contained by x and z equals Q. This is the direct path: 10.113 applies to the given apotome and supplies a comparison rectangle with rational square area, without distinguishing the six orders. (D10.1.3; 10.113.)

**Step 3.** Since c and e are each commensurable in length with a, they are commensurable in length with one another. Also, since c:d and e:f both equal a:b, we have c:d = e:f. (10.12; 5.11.)

**Step 4.** Taking the last proportion alternately gives c:e = d:f. Therefore, by the proposition on sums of antecedents and consequents,
(c + d):(e + f) = c:e,
that is, y:z = c:e. Since c and e are commensurable in length, y and z are likewise commensurable in length. (5.16; 5.12; 10.11.)

**Step 5.** The rectangles contained by x, y and by x, z have the same height x. Hence their areas are in the ratio y:z; since the latter rectangle equals Q, we obtain E:Q = y:z. The commensurability of y and z therefore implies that E and Q are commensurable areas. (6.1; 10.11.)

**Step 6.** Construct a square equal to E, and let its side be s. Its square is commensurable with Q, the square on r; thus s is commensurable in square with the assigned rational straight line r. Consequently s is rational. Therefore the side of the given area is rational, as required. (2.14; D10.1.2; D10.1.3.)

**USED:** 10.11, 10.113, 10.12, 2.14, 5.11, 5.12, 5.16, 6.1, D10.1.2, D10.1.3, D2.1
**Human refs (from References field):** 10.11, 10.112, 10.12, 5.19, 6.1
**Jaccard:** 0.231 — AI adds ['10.113', '2.14', '5.11', '5.12', '5.16', 'D10.1.2', 'D10.1.3', 'D2.1']; Human adds ['10.112', '5.19']

## Proposition 10.115
**Statement:** From a medial straight line there arise irrational straight lines infinite in number, and none of them is the same as any of the preceding.

**Step 1.** Let u be the assigned rational straight line, and let m be the given medial straight line. The line m is irrational by 10.21. Throughout, rationality and irrationality are understood relative to u (D10.1.3). Write S(a) for the square on a, and R(a,b) for the rectangle contained by a and b.

**Step 2.** Put x_0 = m. Given x_n, construct x_{n+1} as a mean proportional between u and x_n (6.13). Then
S(x_{n+1}) = R(u,x_n)
by 6.17. Thus the square on x_{n+1}, applied to u, has breadth x_n. This construction can be repeated after any finite number of steps. **Path choice:** repeated mean proportionals are used because they give exactly the square-to-breadth relation to which the previously proved classification propositions apply directly.

**Step 3.** The initial line x_0 is neither binomial nor apotome. Indeed, its square, applied to u, has a rational breadth because x_0 is medial (10.22). If x_0 were binomial, that breadth would instead be a first binomial (10.60), hence irrational (10.36). If x_0 were an apotome, that breadth would be a first apotome (10.97), hence irrational (10.73). Either alternative contradicts the distinction between rational and irrational straight lines (D10.1.3).

**Step 4.** Suppose that x_n is irrational and is neither binomial nor apotome; Steps 1 and 3 establish this for n = 0. The next line x_{n+1} cannot be rational: otherwise its square would be a rational area (D10.1.3, D10.1.4), and applying that square to u would give a rational breadth by 10.20. But this breadth is x_n by Step 2, contrary to the hypothesis. Hence x_{n+1} is irrational. Nor can x_{n+1} be medial, since 10.22 would again make its breadth x_n rational.

**Step 5.** Moreover, x_{n+1} belongs to none of the twelve previously introduced non-medial irrational kinds. If it belonged to one of the six additive kinds—binomial, first bimedial, second bimedial, major, side of a rational plus a medial area, or side of the sum of two medial areas—then its square, applied to u, would have a binomial breadth, respectively of the first through sixth orders (10.60, 10.61, 10.62, 10.63, 10.64, 10.65). This would make x_n binomial, contrary to the hypothesis. Likewise, if x_{n+1} belonged to one of the six subtractive kinds, its square, applied to u, would have an apotome breadth, respectively of the first through sixth orders (10.97, 10.98, 10.99, 10.100, 10.101, 10.102). This would make x_n an apotome, again a contradiction. These square-to-breadth characterizations are the natural direction here because Step 2 already supplies the breadth. In particular, x_{n+1} is neither binomial nor apotome, so the induction continues. Consequently every x_n with n ≥ 1 is irrational and belongs to none of the thirteen previously named irrational kinds, including the medial.

**Step 6.** We now distinguish the generated lines from one another. For positive indices a and b, Step 2 and the proportionality of rectangles of equal height give
S(x_a) : S(x_b) = R(u,x_{a-1}) : R(u,x_{b-1}) = x_{a-1} : x_{b-1}
(6.1). Therefore, if S(x_a) and S(x_b) are commensurable, x_{a-1} and x_{b-1} are commensurable in length (10.11). Furthermore, whenever two straight lines are commensurable in length, their squares are commensurable: their squares have the ratio of a square number to a square number by 10.9, and hence are commensurable by 10.6.

**Step 7.** Suppose, for a contradiction, that two generated lines x_i and x_j, with 1 ≤ i < j, are commensurable in square (D10.1.2). Step 6 first makes x_{i-1} and x_{j-1} commensurable in length. If i > 1, their squares are consequently commensurable, so the same argument can be repeated. After i repetitions, x_0 and x_{j-i} are commensurable in length. Since x_0 is medial, 10.23 makes x_{j-i} medial. But j-i ≥ 1, contradicting Steps 4–5. Thus the generated lines are pairwise incommensurable even in square, and in particular are distinct: equal squares would have a common measure (D10.1.1, D10.1.2).

**Step 8.** After any finite number of these constructions, another mean proportional can be constructed (6.13). By Steps 4–5 it is irrational and is not any of the previously named irrational kinds; by Step 7 it is distinct from every earlier generated line. It also differs from the original medial line, since it is not medial. Therefore, from the given medial straight line there arise irrational straight lines infinite in number, and none is the same as any of the preceding.

**USED:** 10.100, 10.101, 10.102, 10.11, 10.20, 10.21, 10.22, 10.23, 10.36, 10.6, 10.60, 10.61, 10.62, 10.63, 10.64, 10.65, 10.73, 10.9, 10.97, 10.98, 10.99, 6.1, 6.13, 6.17, D10.1.1, D10.1.2, D10.1.3, D10.1.4
**Human refs (from References field):** 10.20, D10.1.4
**Jaccard:** 0.071 — AI adds ['10.100', '10.101', '10.102', '10.11', '10.21', '10.22', '10.23', '10.36', '10.6', '10.60', '10.61', '10.62', '10.63', '10.64', '10.65', '10.73', '10.9', '10.97', '10.98', '10.99', '6.1', '6.13', '6.17', 'D10.1.1', 'D10.1.2', 'D10.1.3']
