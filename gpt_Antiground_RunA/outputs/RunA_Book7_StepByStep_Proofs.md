# Book 7 of Euclid's Elements — Step-by-Step AI Proofs (Run A)

## Proposition 7.1
**Statement:** Two unequal numbers being set out, and the less being continually subtracted in turn from the greater, if the number which is left never measures the one before it until an unit is left, the original numbers will be prime to one another.

**Step 1.** Let A > B be the given numbers, and let u denote the unit eventually left by the stipulated successive subtractions. The unit measures both original numbers, since numbers are composed of units. It therefore suffices to exclude any number as a common measure of A and B. Our route is to preserve a hypothetical common measure through each subtraction, using the earlier equimultiple-subtraction theorem 5.6 rather than any later arithmetic theorem. [Hypothesis; D7.2; D7.12]

**Step 2.** Suppose that a number d measures both A and B. Since d is a multitude of units, rather than a single unit, d > u. [D7.1; D7.2; CN5]

**Step 3.** We show that whenever d measures two current quantities X > Y, it also measures X − Y. Being measured by d, each quantity consists of whole copies of d. If Y = d, subtracting Y removes one such copy from X and leaves one or more whole copies, because X > Y. [D7.5; CN3] If Y > d, apply 5.6 with the two base magnitudes both equal to d, their two greater equimultiples both equal to X, and the two subtracted equimultiples both equal to Y. The two remainders, both X − Y, are either equal to d or equimultiples of d. Thus in either case d measures X − Y. This uses the previously proved subtraction result; only its single-copy case requires immediate cancellation. [5.6; D7.5]

**Step 4.** Initially d measures both current quantities A and B. At every individual subtraction, it continues to measure the quantity retained and, by Step 3, measures the new remainder. Interchanging which quantity is greater changes nothing about their common measure. Repeating this argument through the given sequence shows that d measures the final remainder u. [Step 3; hypothesis]

**Step 5.** But a quantity measured by d contains at least one whole copy of d: it is either equal to d or greater than d. Consequently d cannot measure u, since d > u by Step 2. This contradiction excludes every number as a common measure of A and B. The unit alone therefore measures them both, so the original numbers are prime to one another. [D7.5; CN5; D7.12]

**USED:** 5.6, CN3, CN5, D7.1, D7.12, D7.2, D7.5
**Human refs (from References field):** D7.12
**Jaccard:** 0.143 — AI adds ['5.6', 'CN3', 'CN5', 'D7.1', 'D7.2', 'D7.5']

## Proposition 7.2
**Statement:** Given two numbers not prime to one another, to find their greatest common measure.

**Step 1.** Let A and B be the given numbers, not prime to one another. If they are equal, either measures both once and is their greatest common measure. Otherwise name them so that A > B. If B measures A, return B: it measures both, and no common measure can exceed B, since a measure cannot exceed the number composed of its copies. These cases are therefore settled. [D7.2, D7.3, D7.5, CN5]

**Step 2.** Suppose now that B does not measure A. **Path choice:** use successive subtraction, because the immediately preceding proposition, 7.1, applies directly to this process. Put r₀ = A and r₁ = B. Subtract copies of r₁ from r₀ until a positive remainder r₂ < r₁ is left. Then proceed with r₁ and r₂, and continue in the same manner. Stop whenever the smaller member measures the larger, or an unit is left. At every nonterminal stage, rᵢ₋₁ consists of the copies of rᵢ removed from it together with the positive remainder rᵢ₊₁ < rᵢ. Each subtraction is possible by removing units from a finite multitude. [D7.2, CN3, CN5]

**Step 3.** This process must terminate: its successive positive remainders contain strictly fewer units, and there are only finitely many units in B. It cannot terminate with an unit before a remainder measures its predecessor, for 7.1 would then imply that A and B are prime to one another, contrary to the hypothesis. Consequently the process reaches a number g = rₙ, greater than an unit, which measures rₙ₋₁. [D7.2, CN5, 7.1]

**Step 4.** The number g measures both original numbers. Indeed, it measures rₙ₋₁ and itself. Working backwards, suppose it measures rᵢ and rᵢ₊₁. The construction expresses rᵢ₋₁ as several copies of rᵢ together with rᵢ₊₁. Each of these consists of whole copies of g; adding those copies shows that g measures rᵢ₋₁. Repeating this through the finite chain proves that g measures r₁ = B and r₀ = A. [D7.5, CN2]

**Step 5.** Let H be any common measure of A and B. It also measures every remainder. For if H measures rᵢ₋₁ and rᵢ, then both rᵢ₋₁ and the copies of rᵢ removed from it consist of whole copies of H. Cancelling the removed copies leaves the remainder rᵢ₊₁ composed of whole copies of H. Starting with A and B and repeating this argument along the chain, H therefore measures the final number g. This argument also applies when H is the unit. [D7.2, D7.5, CN3]

**Step 6.** Since every common measure H measures g, none can exceed g: either g is one copy of H and equals it, or H is a proper part of g and is less than it. By Step 4, g itself measures both A and B. Thus g is their greatest common measure, and the prescribed finite process finds it, as required. [D7.3, D7.5, CN5]

**USED:** 7.1, CN2, CN3, CN5, D7.2, D7.3, D7.5
**Human refs (from References field):** 7.1
**Jaccard:** 0.143 — AI adds ['CN2', 'CN3', 'CN5', 'D7.2', 'D7.3', 'D7.5']

## Proposition 7.3
**Statement:** Given three numbers not prime to one another, to find their greatest common measure.

**Step 1.** Let A, B, C be the given numbers. Since they are not prime to one another, some number K measures all three (D7.12). Thus A and B are not prime to one another; find their greatest common measure D by 7.2. We choose the pairwise route: use 7.2 first on A, B, and then on D, C, after verifying the needed transfer of common measures.

**Step 2.** Every common measure of A and B measures D. To verify this without assuming that divisibility follows merely from greatness, repeatedly subtract the lesser of A, B from the greater, stopping when the two remaining numbers are equal. A common measure of two numbers measures their positive difference; conversely, a measure of the lesser and the difference measures their sum. Indeed, subtraction removes whole copies of the measure, and addition joins such copies. Thus each subtraction preserves exactly the common measures (D7.5, CN3, CN2). The process terminates because each subtraction decreases the finite total of units (D7.2, CN5). Write the equal final entries as R, R. Since K remains a common measure, R is a number. Preservation of common measures shows both that R measures A and B and that every common measure of A and B measures R. No measure of R exceeds R (D7.5, CN5). Hence R is their greatest common measure and therefore equals D, the greatest common measure found in Step 1 (7.2). Consequently every common measure of A and B measures D.

**Step 3.** In particular, K measures D by Step 2; it also measures C. Therefore D and C are not prime to one another (D7.12). Find their greatest common measure E by 7.2. If D already measures C, this application simply gives E = D; otherwise it gives the required further reduction (7.2).

**Step 4.** E measures D, and D measures both A and B. Replacing every copy of D in A and B by its constituent copies of E shows that E measures both A and B (D7.5, CN2). Since E also measures C by its construction, E is a common measure of all three (7.2).

**Step 5.** Let H be any common measure of A, B, C. Since H measures A and B, Step 2 shows that H measures D. It also measures C, so it is a common measure of D and C. Since E is their greatest common measure, H cannot exceed E (7.2). Thus E measures all three given numbers, and no greater number does. Therefore E is their greatest common measure, as required.

**USED:** 7.2, CN2, CN3, CN5, D7.12, D7.2, D7.5
**Human refs (from References field):** 7.2
**Jaccard:** 0.143 — AI adds ['CN2', 'CN3', 'CN5', 'D7.12', 'D7.2', 'D7.5']

## Proposition 7.4
**Statement:** Any number is either a part or parts of any number, the less of the greater.

**Step 1.** Let A and B be arbitrary numbers with A less than B. Choose the direct definitional route: “part” and “parts” are distinguished precisely by whether the less measures the greater. [D7.3, D7.4]

**Step 2.** If A measures B, then A is a part of B, since it is less than B and measures it. [D7.3]

**Step 3.** If A does not measure B, then A is parts of B, since it is less than B and does not measure it. [D7.4]

**Step 4.** Either A measures B or it does not. The two cases therefore exhaust the possibilities, and in each case A is either a part or parts of B. Thus any number is either a part or parts of any number, the less of the greater. [D7.3, D7.4]

**USED:** D7.3, D7.4
**Human refs (from References field):** 7.2
**Jaccard:** 0.000 — AI adds ['D7.3', 'D7.4']; Human adds ['7.2']

## Proposition 7.5
**Statement:** If a number be a part of a number, and another be the same part of another, the sum will also be the same part of the sum that the one is of the one.

**Step 1.** Let A be a part of B, and let C be the same part of D. Thus A measures B as many times as C measures D. Denote this common count by m, which is greater than one. Consequently, B and D are respectively the same m-fold multiples of A and C. [Hypothesis; D7.3; D7.5]

**Step 2.** Use the equimultiple-sum theorem directly: the hypothesis already supplies equimultiples, so no passage through proportions is needed. Numbers are quantities composed of units [D7.2]. By 5.1, when corresponding quantities are equimultiples, their sum is that same multiple of the sum of the quantities measured. Hence B + D is the m-fold multiple of A + C. [5.1]

**Step 3.** Therefore A + C measures B + D exactly m times. Since m is greater than one, A + C is a part of B + D; and since A measures B exactly m times also, it is the same part that A is of B. Thus the sum is the same part of the sum that the one is of the one. [D7.3]

**USED:** 5.1, D7.2, D7.3, D7.5
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['5.1', 'D7.2', 'D7.3', 'D7.5']

## Proposition 7.6
**Statement:** If a number be parts of a number, and another be the same parts of another, the sum will also be the same parts of the sum that the one is of the one.

**Step 1.** Let A be parts of B, and C the same parts of D. Unpacking the hypothesis of the same parts, choose part-sizes u and v and common counts m<n such that
A=mu, B=nu, C=mv, and D=nv.
Here kx denotes a sum of k copies of x, and either part-size may be a unit. Thus each lesser number comprises m equal parts of which its corresponding greater comprises n. [D7.1, D7.2, D7.3, D7.4]

**Step 2.** We use the previously established addition rule for equimultiples, 5.1: the displayed decompositions make it directly applicable, including when a part-size is a unit, without introducing ratios. Since A and C are respectively m-fold multiples of u and v, and B and D are respectively n-fold multiples of them, that proposition gives
A+C=m(u+v), and B+D=n(u+v). [5.1]

**Step 3.** Put w=u+v. Since m<n, mw is less than nw. Moreover, mw does not measure nw. For otherwise nw would consist of some whole number k of copies of mw, hence of km copies of w. Equal sums of copies of the same positive size have equal counts: otherwise the sum with more copies would be greater. Consequently n=km. But then B, consisting of n copies of u, could be grouped into k groups of m copies of u; each group equals A. Thus A would measure B, contrary to the hypothesis that A is parts of B. [D7.2, CN5, D7.3, D7.4]

**Step 4.** Therefore A+C consists of m of the n equal parts w making up B+D, and it does not measure B+D. These are precisely the same parts as the m parts u which A contains out of the n making up B. Hence the sum A+C is the same parts of the sum B+D that A is of B, as required. [D7.3, D7.4]

**USED:** 5.1, CN5, D7.1, D7.2, D7.3, D7.4
**Human refs (from References field):** 7.5
**Jaccard:** 0.000 — AI adds ['5.1', 'CN5', 'D7.1', 'D7.2', 'D7.3', 'D7.4']; Human adds ['7.5']

## Proposition 7.7
**Statement:** If a number be that part of a number, which a number subtracted is of a number subtracted, the remainder will also be the same part of the remainder that the whole is of the whole.

**Step 1.** Let A be a part of B, and let C, subtracted from A, be the same part of D, subtracted from B. Denote the positive remainders by R = A − C and S = B − D. Thus A measures B exactly as many times as C measures D. [Hypothesis; D7.3]

**Step 2.** Consequently, B is the same multiple of A that D is of C. Let their common multiplicity be m. Since A and C are proper parts of B and D respectively, m is greater than one. [D7.3; D7.5]

**Step 3.** Path choice: apply the previously established subtraction theorem 5.5 directly to these equal multiplicities; no passage through ratios is needed. Numbers are multitudes of units, so they may here be regarded as magnitudes measured by a common unit. Proposition 5.5 states that, when a whole is the same multiple of another whole as a subtracted part is of the corresponding subtracted part, the remainders retain that multiplicity. Apply it to B and A, subtracting D and C respectively. It follows that S is the same multiple of R that B is of A, namely the m-fold multiple. [D7.2; 5.5]

**Step 4.** Therefore R measures S exactly m times. Since m is greater than one, R is less than S and is the same part of S that A is of B. Thus the remainder is the same part of the remainder that the whole is of the whole, as required. [D7.3]

**USED:** 5.5, D7.2, D7.3, D7.5
**Human refs (from References field):** 7.5
**Jaccard:** 0.000 — AI adds ['5.5', 'D7.2', 'D7.3', 'D7.5']; Human adds ['7.5']

## Proposition 7.8
**Statement:** If a number be the same parts of a number that a number subtracted is of a number subtracted, the remainder will also be the same parts of the remainder that the whole is of the whole.

**Step 1.** Let A be the same parts of B that C is of D, and let C be subtracted from A and D from B, with C < A and D < B. Unpacking “the same parts,” let a and c be corresponding measures, each a number or a unit, and let m and n be the same counts in both decompositions, so that
A = ma, B = na, C = mc, D = nc,
where 1 < m < n. Here kx denotes the sum of k copies of x. Thus A contains m of the n equal parts composing B, and C contains m of the n equal parts composing D. (D7.1, D7.2, D7.3, D7.4, D7.15.)

**Step 2.** Since ma = A > C = mc, we have a > c: otherwise, adding m corresponding copies would give A ≤ C. Put e = a − c, R = A − C, and S = B − D. Subtracting c from each of the m copies of a removes precisely C from A and leaves m copies of e. Hence R = me. (CN2, CN3, CN5.)

**Step 3.** Path choice: apply the already established single-part subtraction theorem, 7.7, to the corresponding measures; these are supplied directly by the hypothesis. If c is a number, then a is also a number, and a is the nth part of B while c is the nth part of D. Proposition 7.7 therefore gives that e is the nth part of S, so S = ne. If c is a unit, obtain the same identity directly: subtract that unit from each of the n copies of a composing B. The removed units together constitute D, and the remainder consists of n copies of e. Thus in either case S = ne. (D7.1, D7.2, D7.3, 7.7, CN2, CN3.)

**Step 4.** Moreover, R does not measure S. For suppose S consisted of k copies of R. Since R = me and S = ne, grouping these repeated sums would make n copies of e equal to km copies of e. Because e is positive, unequal counts would make one sum a proper part of the other; therefore n = km. But then B = na = k(ma) = kA, so A would measure B, contrary to the hypothesis that A is parts of B. Thus R does not measure S. (D7.15, CN2, CN5, D7.3, D7.4.)

**Step 5.** Now R consists of m of the n equal parts composing S, exactly as A consists of m of the n equal parts composing B; and R does not measure S. Therefore the remainder A − C is the same parts of the remainder B − D that the whole A is of the whole B, as required. (D7.3, D7.4.)

**USED:** 7.7, CN2, CN3, CN5, D7.1, D7.15, D7.2, D7.3, D7.4
**Human refs (from References field):** 7.7
**Jaccard:** 0.111 — AI adds ['CN2', 'CN3', 'CN5', 'D7.1', 'D7.15', 'D7.2', 'D7.3', 'D7.4']

## Proposition 7.9
**Statement:** If a number be a part of a number, and another be the same part of another, alternately also, whatever part or parts the first is of the third, the same part, or the same parts, will the second also be of the fourth.

**Step 1.** Let A be a part of B, and let C be the same part of D. Thus B consists of some number k of copies of A, and D consists of the same number k of copies of C. Write rX for the sum of r copies of X; then B = kA and D = kC. [D7.3]

**Step 2.** Consider whatever part or parts A is of C. These alternatives exhaust the possibilities when A is less than C. [7.4] Path choice: use addition of the same part in the first case and addition of the same parts in the second, since Step 1 expresses B and D as equal-count sums. The directly applicable propositions are 7.5 and 7.6, respectively.

**Step 3.** Suppose A is a part of C. If rA is that same part of rC, then, because A is also that part of C, their sums (r + 1)A and (r + 1)C have the same part relation. [7.5] Starting with r = 1 and applying this successively up to r = k, we obtain that kA is the same part of kC that A is of C. Hence B is the same part of D that A is of C. [Step 1]

**Step 4.** Suppose instead that A is parts of C. If rA is those same parts of rC, then, because A is also those parts of C, their sums (r + 1)A and (r + 1)C have the same parts relation. [7.6] Starting with r = 1 and applying this successively up to r = k, we obtain that kA is the same parts of kC that A is of C. Hence B is the same parts of D that A is of C. [Step 1]

**Step 5.** Therefore, in either case, whatever part or parts the first number A is of the third C, the second B is the same part or the same parts of the fourth D, as required. [Steps 2–4]

**USED:** 7.4, 7.5, 7.6, D7.3
**Human refs (from References field):** 7.5, 7.6
**Jaccard:** 0.500 — AI adds ['7.4', 'D7.3']

## Proposition 7.10
**Statement:** If a number be parts of a number, and another be the same parts of another, alternately also, whatever parts or part the first is of the third, the same parts or the same part will the second also be of the fourth.

**Step 1.** Let A be parts of B, and C the same parts of D. Take A<C, as understood when A is a part or parts of C. By the hypothesis of the same parts, there are measuring pieces e and f, each a unit or a number, and counts m<n such that A consists of m copies of e, B of n copies of e, C of m copies of f, and D of n copies of f. Here m>1, since otherwise A would measure B. [D7.2, D7.3, D7.4]

**Step 2.** Our route is to apply 7.9 to these measuring pieces. To ensure that its terms are numbers even when a measuring piece is a unit, put E=e+e and F=f+f, and let A′, B′, C′, D′ be the doubles of A, B, C, D respectively. Then A′ consists of m copies of E, B′ of n copies of E, C′ of m copies of F, and D′ of n copies of F. All these quantities, including E and F, are numbers. [D7.2, CN2]

**Step 3.** Since A<C and both contain the same number m of their respective pieces, e<f. Consequently E<F and B<D. Thus E is either a part or parts of F. Also, E is the same part of A′ that F is of C′, since each measures its respective whole m times; and E is the same part of B′ that F is of D′, since each measures its respective whole n times. [CN2, CN5, 7.4, D7.3]

**Step 4.** Apply 7.9 to E, A′, F, C′. Whatever part or parts E is of F, A′ is the same part or parts of C′. Apply 7.9 again, now to E, B′, F, D′. Whatever part or parts E is of F, B′ is the same part or parts of D′. Hence A′ is the same part or parts of C′ as B′ is of D′. [7.9]

**Step 5.** A is the same part—one half—of A′ that C is of C′. Therefore, by 7.9, whatever part or parts A is of C, A′ is the same part or parts of C′. Likewise, B is one half of B′ and D is one half of D′; hence whatever part or parts B is of D, B′ is the same part or parts of D′. [D7.3, 7.9]

**Step 6.** By Steps 4 and 5, the part-or-parts relation of A to C is exactly that of B to D. Therefore, alternately, whatever parts or part the first number is of the third, the second is the same parts or the same part of the fourth, as required. [Steps 4–5]

**USED:** 7.4, 7.9, CN2, CN5, D7.2, D7.3, D7.4
**Human refs (from References field):** 7.5, 7.6, 7.9
**Jaccard:** 0.111 — AI adds ['7.4', 'CN2', 'CN5', 'D7.2', 'D7.3', 'D7.4']; Human adds ['7.5', '7.6']

## Proposition 7.11
**Statement:** If, as whole is to whole, so is a number subtracted to a number subtracted, the remainder will also be to the remainder as whole to whole.

**Step 1.** Let A and B be the whole numbers, and let C and D be subtracted from them respectively, with A:B = C:D. Write E = A − C and F = B − D for the remainders. By D7.20, the hypothesis specifies the same multiple, part, or parts relation between A and B as between C and D. We use the established numerical subtraction rules 7.7 and 7.8 directly.

**Step 2.** If A = B, the proportionality gives C = D (D7.20). Subtracting equals from equals gives E = F (CN3). Consequently E:F = A:B (D7.20).

**Step 3.** If A is the same part of B that C is of D, then E is the same part of F that A is of B, by 7.7. Hence E:F = A:B, by D7.20. Here 7.7 is the direct choice because the hypothesis concerns a single part.

**Step 4.** If A is the same parts of B that C is of D, then E is the same parts of F that A is of B, by 7.8. Hence E:F = A:B, by D7.20. This is precisely the parts case addressed by 7.8.

**Step 5.** Suppose instead that A is the same multiple of B that C is of D, with the multiple greater than one. Then B is the same part of A that D is of C (D7.3, D7.5). Apply 7.7 to these numbers, subtracting D from B and C from A: F is the same part of E that B is of A. Therefore E is the same multiple of F that A is of B (D7.3, D7.5), and so E:F = A:B (D7.20).

**Step 6.** These cases exhaust the relations specified by D7.20. Thus, in every case, (A − C):(B − D) = A:B: the remainder is to the remainder as whole to whole.

**USED:** 7.7, 7.8, CN3, D7.20, D7.3, D7.5
**Human refs (from References field):** 7.7, 7.8, D7.20
**Jaccard:** 0.500 — AI adds ['CN3', 'D7.3', 'D7.5']

## Proposition 7.12
**Statement:** If there be as many numbers as we please in proportion, then, as one of the antecedents is to one of the consequents, so are all the antecedents to all the consequents.

**Step 1.** Let the given proportional pairs be a₁:b₁, a₂:b₂, …, aₙ:bₙ, and put A = a₁ + ⋯ + aₙ and B = b₁ + ⋯ + bₙ. By D7.20, the antecedents have the same numerical relation to their respective consequents: the same multiple, the same part, or the same parts. We use 7.5 and 7.6 directly, since these are the numerical addition rules corresponding to these alternatives.

**Step 2.** First suppose a₁ = b₁. The given proportionality then gives aᵢ = bᵢ for every i (D7.20). Adding these equalities gives A = B (CN2). Thus each aᵢ is to bᵢ as A is to B (D7.20).

**Step 3.** Suppose each aᵢ is the same part of bᵢ. By 7.5, a₁ + a₂ is that same part of b₁ + b₂. Applying 7.5 again to these sums and the next pair preserves that same part. Continuing through the finite list shows that A is the same part of B that each aᵢ is of bᵢ. Therefore aᵢ:bᵢ = A:B (D7.20).

**Step 4.** Suppose each aᵢ is the same parts of bᵢ. By 7.6, a₁ + a₂ is those same parts of b₁ + b₂. Repeated application of 7.6, adding one further corresponding pair at each stage, shows that A is the same parts of B that each aᵢ is of bᵢ. Therefore aᵢ:bᵢ = A:B (D7.20).

**Step 5.** Finally, suppose each aᵢ is the same proper multiple of bᵢ. Then each bᵢ measures aᵢ the same number of times, so each bᵢ is the same part of aᵢ (D7.5, D7.3). Applying 7.5 repeatedly to these reversed pairs shows that B is that same part of A. Consequently A is the same multiple of B that each aᵢ is of bᵢ (D7.3, D7.5), and therefore aᵢ:bᵢ = A:B (D7.20).

**Step 6.** These cases exhaust the numerical relations in the given proportionality (D7.20). Hence, as any one antecedent is to its corresponding consequent, so is the sum of all the antecedents to the sum of all the consequents. This proves the proposition.

**USED:** 7.5, 7.6, CN2, D7.20, D7.3, D7.5
**Human refs (from References field):** 7.5, 7.6, D7.20
**Jaccard:** 0.500 — AI adds ['CN2', 'D7.3', 'D7.5']

## Proposition 7.13
**Statement:** If four numbers be proportional, they will also be proportional alternately.

**Step 1.** Let A, B, C, D be numbers such that A:B = C:D. We must prove A:C = B:D, which is the alternate proportion (D5.12).

**Step 2.** We may interchange the two given ratios or reverse both of them: by D7.20, interchanging preserves their common relationship, while reversal interchanges the common counts of parts, with the same multiple becoming the same part and conversely. These operations change the required alternate proportion only by simultaneous reversal or interchange of its two ratios. Thus, by placing a least of the four numbers first, we may suppose A ≤ B and A ≤ C (D7.20).

**Step 3.** If A = B, then C = D. If A = C, then B = D. Indeed, the common part-counts in D7.20 give these equalities: equally numerous sums of unequal parts cannot be equal, whereas sums of equal parts are equal (CN2, CN5). In either case A:C = B:D by substitution of equals. We may therefore suppose A < B and A < C.

**Step 4.** Since A < B, A is either a part or parts of B (7.4). The hypothesis says that C is the same part or the same parts of D, respectively (D7.20). We use the already-proved numerical alternation results: 7.9 for the single-part case and 7.10 for the parts case, without transferring the question to magnitudes.

**Step 5.** If A is a part of B, and C the same part of D, then whatever part or parts A is of C, B is the same part or parts of D (7.9). If A is parts of B, and C the same parts of D, the identical alternate conclusion follows from 7.10. In either case, therefore, A:C = B:D (D7.20).

**Step 6.** Undoing any relabeling in Step 2 preserves this conclusion, since it merely interchanges the two alternate ratios or reverses both (D7.20). Hence the original four numbers are proportional alternately, as required (D5.12).

**USED:** 7.10, 7.4, 7.9, CN2, CN5, D5.12, D7.20
**Human refs (from References field):** 7.10, D7.20
**Jaccard:** 0.286 — AI adds ['7.4', '7.9', 'CN2', 'CN5', 'D5.12']

## Proposition 7.14
**Statement:** If there be as many numbers as we please, and others equal to them in multitude, which taken two and two are in the same ratio, they will also be in the same ratio ex aequali.

**Step 1.** Let the two given lists be A₁, A₂, …, Aₙ and B₁, B₂, …, Bₙ, where n ≥ 2. By hypothesis, Aᵢ : Aᵢ₊₁ = Bᵢ : Bᵢ₊₁ for every i with 1 ≤ i < n, with numerical proportionality understood according to D7.20. We must show A₁ : Aₙ = B₁ : Bₙ; this is precisely the required proportion ex aequali. [D7.20; D5.17]

**Step 2.** Choose the numerical alternation route: 7.13 applies directly to the given proportions, without transferring them to magnitudes. Applying it to each consecutive pair gives Aᵢ : Bᵢ = Aᵢ₊₁ : Bᵢ₊₁ for every 1 ≤ i < n. [7.13]

**Step 3.** Hence A₁ : B₁, A₂ : B₂, …, Aₙ : Bₙ are successively the same ratio. Under D7.20, these equalities identify the same multiple, part, or parts relation at each link. Repeated application of the common notion that things equal to the same thing are equal to one another therefore gives A₁ : B₁ = Aₙ : Bₙ. [D7.20; CN1]

**Step 4.** Apply alternation once more to this last proportion. Then A₁ : Aₙ = B₁ : Bₙ. Thus the first and last numbers in the two lists are proportional, the intermediate terms having been removed: the numbers are in the same ratio ex aequali, as required. [7.13; D5.17]

**USED:** 7.13, CN1, D5.17, D7.20
**Human refs (from References field):** 7.13
**Jaccard:** 0.250 — AI adds ['CN1', 'D5.17', 'D7.20']

## Proposition 7.15
**Statement:** If an unit measure any number, and another number measure any other number the same number of times, alternately also, the unit will measure the third number the same number of times that the second measures the fourth.

**Step 1.** Let u be the unit, and let A, B, C be the second, third, and fourth terms respectively. Suppose u measures A exactly r times and B measures C exactly r times. Let s be the number of units composing B. Thus A consists of r copies of u, C of r copies of B, and B of s copies of u. [Hypothesis; D7.2]

**Step 2.** Set U = u + u, V = A + A, W = B + B, and X = C + C. These are all numbers. Adding the decompositions in Step 1 to themselves and pairing corresponding summands shows that V consists of r copies of U, X of r copies of W, and W of s copies of U. Hence U is the same part of V that W is of X, and U measures W exactly s times. [D7.2; CN2; D7.3]

**Step 3.** Apply the same-part alternation theorem to U, V, W, X. It follows that V is the same part of X that U is of W. Therefore V measures X exactly s times. This is the chosen route: doubling makes every term a number, and the same-part hypotheses lead directly to 7.9 without requiring a more general proportion theorem. [7.9; D7.3]

**Step 4.** Let T be the sum of s copies of A. Since V = A + A, the sum of s copies of V equals T + T, by adding corresponding equal summands. But Step 3 says that this sum equals X, and X = C + C. Consequently T + T = C + C. [D7.2; CN2; CN1]

**Step 5.** Therefore T = C. For if T were greater than C, then T + T would consist of C + C together with two copies of the positive excess; it would consequently be greater than C + C, contrary to Step 4. If C were greater than T, the same argument with the terms interchanged would give the opposite contradiction. [CN2; CN5]

**Step 6.** Since T is the sum of s copies of A and T = C, A measures C exactly s times. By Step 1, u also measures B exactly s times. Thus, alternately, the unit measures the third term the same number of times that the second measures the fourth, as required. [D7.2; D7.3]

**USED:** 7.9, CN1, CN2, CN5, D7.2, D7.3
**Human refs (from References field):** 7.12
**Jaccard:** 0.000 — AI adds ['7.9', 'CN1', 'CN2', 'CN5', 'D7.2', 'D7.3']; Human adds ['7.12']

## Proposition 7.16
**Statement:** If two numbers by multiplying one another make certain numbers, the numbers so produced will be equal to one another.

**Step 1.** Let A multiplying B produce C, and B multiplying A produce D. Take a unit U. Since C consists of as many copies of B as there are units in A, U measures A the same number of times that B measures C. (D7.1, D7.2, D7.15.)

**Step 2.** Choose 7.15 directly, because the preceding unit-and-measure relation is exactly its hypothesis. Applying it to U, A, B, C, we obtain that U measures B the same number of times that A measures C. (7.15.)

**Step 3.** Since B multiplying A produces D, D consists of as many copies of A as there are units in B. Thus A measures D the same number of times that U measures B, and therefore, by Step 2, the same number of times that A measures C. (D7.2, D7.15.)

**Step 4.** Consequently C and D consist of equally many copies of the same number A. Adding these corresponding equal copies gives equal wholes, so C = D. Therefore the numbers produced by the two numbers multiplying one another are equal. (CN2, repeatedly.)

**USED:** 7.15, CN2, D7.1, D7.15, D7.2
**Human refs (from References field):** 7.15
**Jaccard:** 0.200 — AI adds ['CN2', 'D7.1', 'D7.15', 'D7.2']

## Proposition 7.17
**Statement:** If a number by multiplying two numbers make certain numbers, the numbers so produced will have the same ratio as the numbers multiplied.

**Step 1.** Let the number A, by multiplying the numbers B and C, produce D and E respectively. By the definition of multiplication, D consists of as many copies of B as there are units in A, and E consists of equally many copies of C. [D7.15]

**Step 2.** Thus D is the same multiple of B that E is of C. Hence, by the definition of proportional numbers, D:B = E:C. [D7.20]

**Step 3.** We use numerical alternation, since Step 2 already supplies four proportional numbers. Applying it to D, B, E, C gives D:E = B:C. Therefore the numbers produced have the same ratio as the numbers multiplied, as required. [7.13]

**USED:** 7.13, D7.15, D7.20
**Human refs (from References field):** 7.13, D7.20
**Jaccard:** 0.667 — AI adds ['D7.15']

## Proposition 7.18
**Statement:** If two numbers by multiplying any number make certain numbers, the numbers so produced will have the same ratio as the multipliers.

**Step 1.** Let the numbers A and B, by multiplying the same number C, produce D and E respectively. We must prove D:E = A:B. Here multiplication is understood as in D7.15. [D7.15]

**Step 2.** By commutativity of multiplication, C multiplying A produces D, and C multiplying B produces E. [7.16] This puts both products under the common multiplier C, making 7.17 the direct applicable proposition rather than requiring a new argument from the definition of proportion.

**Step 3.** Since C, by multiplying A and B, produces D and E respectively, the products have the same ratio as the numbers multiplied: D:E = A:B. [7.17] Thus the numbers originally produced have the same ratio as the original multipliers, as required.

**USED:** 7.16, 7.17, D7.15
**Human refs (from References field):** 7.16, 7.17
**Jaccard:** 0.667 — AI adds ['D7.15']

## Proposition 7.19
**Statement:** If four numbers be proportional, the number produced from the first and fourth will be equal to the number produced from the second and third; and, if the number produced from the first and fourth be equal to that produced from the second and third, the four numbers will be proportional.

**Step 1.** Let A, B, C, D be the four numbers in their stated order. Write XY for the number produced when X multiplies Y, and set E = AD, F = BD, and G = BC. [D7.15]

**Step 2.** Since A and B multiply the same number D, we have E:F = A:B. [7.18] Since B multiplies C and D, we have G:F = C:D. [7.17] Path choice: use 7.18 for the common multiplicand D and 7.17 for the common multiplier B; these directly give ratios with the common consequent F, without reversing any factors.

**Step 3.** Suppose first that the four numbers are proportional, so A:B = C:D. [D7.20] Combining this with the two proportions in Step 2 gives E:F = G:F, by applying transitivity of equal ratios twice. [5.11]

**Step 4.** Things having the same ratio to the same thing are equal; therefore E = G. [5.9] By their definitions in Step 1, AD = BC. Thus the number produced from the first and fourth equals that produced from the second and third.

**Step 5.** Conversely, suppose AD = BC, so E = G. Substituting E for G in Step 2 gives E:F = A:B and E:F = C:D. Hence A:B = C:D, since ratios equal to the same ratio are equal to one another. [5.11] The four numbers are therefore proportional. [D7.20] Both implications are proved.

**USED:** 5.11, 5.9, 7.17, 7.18, D7.15, D7.20
**Human refs (from References field):** 5.7, 5.9, 7.17, 7.18
**Jaccard:** 0.429 — AI adds ['5.11', 'D7.15', 'D7.20']; Human adds ['5.7']

## Proposition 7.20
**Statement:** The least numbers of those which have the same ratio with them measure those which have the same ratio the same number of times, the greater the greater and the less the less.

**Step 1.** Let a, b be the least numbers having the same ratio as c, d, with the greater terms a, c corresponding and the less terms b, d corresponding. Thus a:b = c:d, and by leastness a ≤ c and b ≤ d. We must show that a measures c as many times as b measures d. [Hypothesis; D7.20]

**Step 2.** By alternation, a:c = b:d. If a = c, this proportion gives b = d, so each measures its corresponding number once. We may therefore suppose a < c. By 7.4, a is either a part or parts of c. This is the direct path: alternation makes the part-or-parts alternative apply to corresponding terms. [7.13; D7.20; 7.4]

**Step 3.** Suppose that a does not measure c. Then a is parts of c; and, because a:c = b:d, b is the same parts of d. Accordingly, let e and f be the respective equal parts, and let m, n be their common counts, so that a = me, c = ne, b = mf, and d = nf. Here m > 1, since m = 1 would make a itself a measure of c, contrary to the supposition. [D7.4; D7.20; D7.15]

**Step 4.** Since the same number m multiplies e and f to produce a and b, respectively, a:b = e:f. Proposition 7.17 is the natural choice because the multiplier is common. But m > 1, so e < a and f < b: each is a proper part of the corresponding whole. Thus e, f are smaller numbers having the same ratio as a, b, contradicting their leastness. Consequently, a must measure c. [7.17; CN5; hypothesis of leastness]

**Step 5.** Let a measure c k times. Then a is the kth part of c. Since a:c = b:d, b is the same part of d, and therefore b measures d exactly k times. Hence the least numbers measure any numbers having the same ratio the same number of times, the greater the greater and the less the less. [D7.3; D7.20]

**USED:** 7.13, 7.17, 7.4, CN5, D7.15, D7.20, D7.3, D7.4
**Human refs (from References field):** 7.12, 7.13, 7.4, D7.20
**Jaccard:** 0.333 — AI adds ['7.17', 'CN5', 'D7.15', 'D7.3', 'D7.4']; Human adds ['7.12']

## Proposition 7.21
**Statement:** Numbers prime to one another are the least of those which have the same ratio with them.

**Step 1.** Let A and B be numbers prime to one another. Thus no number other than the unit measures both A and B. [D7.12]

**Step 2.** Suppose that A and B are not the least numbers having their ratio, and let C and D be the least numbers such that C:D = A:B. By 7.20, C measures A and D measures B the same number of times. This common count exceeds one, since otherwise C = A and D = B, contrary to the supposition. The direct path is to use 7.20, which supplies precisely the equal measuring counts needed below. [7.20]

**Step 3.** Let E be the number composed of as many units as this common count. Since the count exceeds one, E is a number, not the unit. The unit therefore measures E as many times as C measures A, and as many times as D measures B. [D7.2]

**Step 4.** Apply 7.15 to the unit measuring E and C measuring A: E measures A as many times as the unit measures C. Apply it again to the unit measuring E and D measuring B: E measures B as many times as the unit measures D. Hence E measures both A and B. We use 7.15 directly because its hypothesis is exactly the equality of measuring counts established in Step 3. [7.15]

**Step 5.** Thus the number E, which is not the unit, is a common measure of A and B, contradicting their being prime to one another. The supposition is therefore false: numbers prime to one another are the least of those which have the same ratio with them. [D7.12]

**USED:** 7.15, 7.20, D7.12, D7.2
**Human refs (from References field):** 7.16, 7.20, D7.12
**Jaccard:** 0.400 — AI adds ['7.15', 'D7.2']; Human adds ['7.16']

## Proposition 7.22
**Statement:** The least numbers of those which have the same ratio with them are prime to one another.

**Step 1.** Let A and B be the least numbers having their ratio. Suppose that they are not prime to one another. Then some number C, other than the unit, measures both A and B (D7.12). Since C is a multitude of units, it exceeds the unit (D7.2).

**Step 2.** Let D and E be the respective quotients when C measures A and B. Thus D multiplying C produces A, and E multiplying C produces B (D7.15). By commutativity of multiplication, C multiplying D produces A, and C multiplying E produces B (7.16).

**Step 3.** Consequently A:B = D:E, since the products obtained by multiplying two numbers by the same number have the ratio of those two numbers (7.17). Path choice: use 7.17, the first applicable common-multiplier proposition; finding a greatest common measure is unnecessary.

**Step 4.** Because C contains more than one unit, A consists of more than one copy of D, and B consists of more than one copy of E (D7.2, D7.15). Therefore D is less than A, and E is less than B: each is a proper part of the corresponding whole (CN5).

**Step 5.** Thus D and E are smaller than A and B respectively while having the same ratio, contradicting the assumed leastness of A and B. Hence no number other than the unit measures both A and B. Therefore A and B are prime to one another (D7.12).

**USED:** 7.16, 7.17, CN5, D7.12, D7.15, D7.2
**Human refs (from References field):** 7.17, D7.15
**Jaccard:** 0.333 — AI adds ['7.16', 'CN5', 'D7.12', 'D7.2']

## Proposition 7.23
**Statement:** If two number be prime to one another, the number which measures the one of them will be prime to the remaining number.

**Step 1.** Let A and B be numbers prime to one another, and let C measure A. By D7.12, an unit alone measures A and B in common. We use this common-measure criterion directly; finding a greatest common measure is unnecessary.

**Step 2.** Suppose that C and B are not prime to one another. Then some number D, other than an unit, measures both C and B. [D7.12]

**Step 3.** Since C measures A, A consists of equal copies of C; since D measures C, each such copy consists of equal copies of D. Adding these equal decompositions shows that A consists of equal copies of D. Consequently D measures A. [D7.5; CN2]

**Step 4.** Thus D measures both A and B, although D is not an unit. This contradicts their being prime to one another. Therefore C and B are prime to one another: a number measuring one of two numbers prime to one another is prime to the remaining number. [D7.12]

**USED:** CN2, D7.12, D7.5
**Human refs (from References field):** D7.12
**Jaccard:** 0.333 — AI adds ['CN2', 'D7.5']

## Proposition 7.24
**Statement:** If two numbers be prime to any number, their product also will be prime to the same.

**Step 1.** Let A and B each be prime to C, and let P = AB be their product. By 7.16, P = BA also; hence A measures P. [D7.12, D7.15, 7.16]

**Step 2.** Suppose, for a contradiction, that P and C are not prime to one another. There is then a number D, greater than the unit, measuring both P and C. Since A and C are prime to one another and D measures C, A and D are prime to one another. This transfers the given coprimality directly to the common measure. [D7.12, 7.23]

**Step 3.** D cannot equal P: otherwise A, which measures P, would be a common measure of A and D, contrary to their coprimality. Thus D measures P more than once. Let E be the number of times it measures P; then P = ED = DE. [D7.12, D7.5, D7.15, 7.16]

**Step 4.** We have AB = DE. Applying the equal-products direction of 7.19 directly gives the proportion A : D = E : B. [7.19]

**Step 5.** Since A and D are prime to one another, they are the least numbers having their ratio. Here 7.21 is the natural direction to use, from the known coprimality to leastness. These least numbers measure the corresponding terms of every pair having the same ratio; consequently D measures B. [7.21, 7.20]

**Step 6.** But D also measures C. Thus B and C have the common measure D, greater than the unit, contradicting the hypothesis that they are prime to one another. Therefore P and C are prime to one another: the product of two numbers each prime to C is also prime to C. [D7.12]

**USED:** 7.16, 7.19, 7.20, 7.21, 7.23, D7.12, D7.15, D7.5
**Human refs (from References field):** 7.16, 7.19, 7.20, 7.21, 7.23, D7.12, D7.15
**Jaccard:** 0.875 — AI adds ['D7.5']

## Proposition 7.25
**Statement:** If two numbers be prime to one another, the product of one of them into itself will be prime to the remaining one.

**Step 1.** Let A and B be the given numbers, prime to one another. Each of the two factors in A·A is therefore prime to B. [Hypothesis]

**Step 2.** Choose the direct specialization of 7.24 with both factors equal to A and the common number equal to B; that proposition does not require the factors to be distinct. It follows that their product A·A is prime to B. Thus the product of one of the given numbers into itself is prime to the remaining number, as required. [7.24]

**USED:** 7.24
**Human refs (from References field):** 7.24
**Jaccard:** 1.000 — Perfect match.

## Proposition 7.26
**Statement:** If two numbers be prime to two numbers, both to each, their products also will be prime to one another.

**Step 1.** Let A and B each be prime to each of C and D, as given. Let E be the product of A and B, and F the product of C and D (D7.15). We use 7.24 repeatedly, since it directly combines two factors prime to a fixed number.

**Step 2.** Since A and B are both prime to C, their product E is prime to C (7.24).

**Step 3.** Since A and B are both prime to D, their product E is prime to D (7.24).

**Step 4.** Being prime to one another is symmetric, since the condition concerns common measures (D7.12). Thus C and D are both prime to E by Steps 2 and 3. Therefore their product F is prime to E (7.24), and hence E and F are prime to one another (D7.12). The products of the two given pairs are therefore prime to one another, as required.

**USED:** 7.24, D7.12, D7.15
**Human refs (from References field):** 7.24
**Jaccard:** 0.333 — AI adds ['D7.12', 'D7.15']

## Proposition 7.27
**Statement:** If two numbers be prime to one another, and each by multiplying itself make a certain number, the products will be prime to one another; and, if the original numbers by multiplying the products make certain numbers, the latter will also be prime to one another [and this is always the case with the extremes].

**Step 1.** Let a and b be prime to one another. This relation is symmetric, since it says that their only common measure is the unit (D7.12). Write a¹ = a and b¹ = b, and denote the successive products by aⁿ⁺¹ = a·aⁿ and bⁿ⁺¹ = b·bⁿ (D7.15).

**Step 2.** Each of the two factors a, a is prime to each of the two factors b, b. Therefore their products a² and b² are prime to one another by 7.26. This is the direct path: the two-product criterion applies immediately to the given factors, without an intermediate argument about common measures.

**Step 3.** Every successive product aⁿ is prime to b. Indeed, this holds initially for a¹ = a; whenever aⁿ is prime to b, both a and aⁿ are prime to b, so their product aⁿ⁺¹ is prime to b by 7.24. Repeating this application establishes the assertion at every stage. Likewise, starting from b prime to a, repeated application of 7.24 shows that every bⁿ is prime to a, and hence a is prime to every bⁿ (D7.12).

**Step 4.** Suppose that at any stage aⁿ and bⁿ are prime to one another. The two numbers a and aⁿ are then prime, both to each, to the two numbers b and bⁿ: the pair a, b is covered by the hypothesis; the pairs a, bⁿ and aⁿ, b are covered by Step 3; and the pair aⁿ, bⁿ is covered by the supposition. Thus 7.26 gives that a·aⁿ and b·bⁿ, namely aⁿ⁺¹ and bⁿ⁺¹, are prime to one another. Taking n = 2 and using Step 2 proves that the products a³ and b³ are prime to one another. Repeating the same argument proves the assertion at every subsequent stage. Therefore the squares, the products obtained by multiplying those squares by their respective original numbers, and all further corresponding extreme products are prime to one another.

**USED:** 7.24, 7.26, D7.12, D7.15
**Human refs (from References field):** 7.25, 7.26
**Jaccard:** 0.200 — AI adds ['7.24', 'D7.12', 'D7.15']; Human adds ['7.25']

## Proposition 7.28
**Statement:** If two numbers be prime to one another, the sum will also be prime to each of them; and, if the sum of two numbers be prime to any one of them, the original numbers will also be prime to one another.

**Step 1.** Let A and B be the given numbers, and let S=A+B. Choose X to be either A or B, and let Y be the other, so that S=X+Y. Path choice: use common measures directly, since being prime to one another means having the unit alone as a common measure; no ratio or greatest-common-measure construction is needed (D7.12).

**Step 2.** Suppose A and B are prime to one another. If S and X were not prime to one another, some measure d other than the unit would measure both (D7.12). Thus S and X consist of complete copies of d, allowing a single copy when X=d (D7.5, D7.15). Removing from the copies forming S the copies forming X leaves complete copies of d forming S−X=Y (CN3). Hence d measures both X and Y, contrary to the assumed primality of A and B (D7.12). Therefore S is prime to X. Since X was either summand, S is prime to each of A and B.

**Step 3.** Conversely, suppose S is prime to one summand X. If A and B were not prime to one another, some measure d other than the unit would measure both X and Y (D7.12). Each summand therefore consists of complete copies of d, again allowing a single copy (D7.5, D7.15). Adjoining these copies gives complete copies of d forming X+Y=S (CN2). Thus d measures both S and X, contrary to their being prime to one another (D7.12). Consequently A and B are prime to one another.

**Step 4.** Therefore the sum of two numbers prime to one another is prime to each summand; and, if their sum is prime to either summand, the original numbers are prime to one another (Steps 2–3, D7.12).

**USED:** CN2, CN3, D7.12, D7.15, D7.5
**Human refs (from References field):** D7.12
**Jaccard:** 0.200 — AI adds ['CN2', 'CN3', 'D7.15', 'D7.5']

## Proposition 7.29
**Statement:** Any prime number is prime to any number which it does not measure.

**Step 1.** Let p be a prime number, and let a be a number which p does not measure. The unit measures both, since every number is composed of units (D7.2). Path choice: use the common-measure criterion directly; it suffices to exclude any numerical common measure (D7.12).

**Step 2.** Suppose a number d measures both p and a. Since p consists of one or more copies of d, d cannot exceed p (CN5). Nor can d equal p, for then p would measure a, contrary to the hypothesis. Consequently d is less than p (CN5 and the hypothesis).

**Step 3.** Thus d is a numerical measure of p smaller than p. This contradicts the primality of p, which permits only the unit as a proper measure (D7.11). Hence no number measures both p and a.

**Step 4.** The unit is therefore their only common measure. By D7.12, p and a are prime to one another. Thus any prime number is prime to any number which it does not measure.

**USED:** CN5, D7.11, D7.12, D7.2
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['CN5', 'D7.11', 'D7.12', 'D7.2']

## Proposition 7.30
**Statement:** If two numbers by multiplying one another make some number, and any prime number measure the product, it will also measure one of the original numbers.

**Step 1.** Let A and B be the two numbers whose product is C, and let the prime number p measure C. We must show that p measures A or B. (Hypotheses.)

**Step 2.** Suppose, for a contradiction, that p measures neither A nor B. By 7.29, p is prime to A and also prime to B. Hence A and B are each prime to p, since having the unit alone as a common measure is a symmetric relation (D7.12). This selects the direct product route: the supposition gives precisely the hypotheses needed for 7.24.

**Step 3.** Since A and B are each prime to p, their product C is also prime to p, by 7.24. Thus C and p have the unit alone as a common measure (D7.12).

**Step 4.** But p measures C by hypothesis, and p measures itself once. Therefore p is a common measure of C and p; being a number, it is not the unit (D7.2). This contradicts their being prime to one another (D7.12). Consequently p cannot fail to measure both original numbers: it measures A or B, as required.

**USED:** 7.24, 7.29, D7.12, D7.2
**Human refs (from References field):** 7.19, 7.20, 7.21, 7.29, D7.15
**Jaccard:** 0.125 — AI adds ['7.24', 'D7.12', 'D7.2']; Human adds ['7.19', '7.20', '7.21', 'D7.15']

## Proposition 7.31
**Statement:** Any composite number is measured by some prime number.

**Step 1.** Let A be any composite number. Then A has a numerical measure B other than the unit, with B less than A: B is a proper part of A. [D7.13, D7.3, CN5]

**Step 2.** Choose the least numerical measure P of A. This choice requires only a finite inspection: since A is a multitude of units, inspect the numbers less than A in increasing order of their numbers of units, stopping at the first that measures A. The measure B from Step 1 ensures that this inspection succeeds. Thus P measures A, and no number less than P measures A. This is the least-measure route, avoiding a succession of factorizations. [D7.2; Step 1]

**Step 3.** Suppose P were not prime. It would then have a numerical measure Q other than the unit. Such a measure is a proper part of P, so Q is less than P. [D7.11, D7.13, D7.3, CN5]

**Step 4.** Since P measures A, A consists of a whole number of copies of P. Since Q measures P, each such copy consists of a whole number of copies of Q. Replacing each copy of P by its copies of Q therefore expresses A as a whole number of copies of Q; hence Q measures A. This uses precisely the repeated-addition meaning of multiplication and measurement. But Q is less than P, contradicting the choice of P in Step 2. [D7.15, D7.3; Steps 2–3]

**Step 5.** Therefore P has no proper numerical measure and is measured by the unit alone; hence P is prime. Since P measures A, the arbitrary composite number A is measured by a prime number. [D7.2, D7.11; Steps 2–4]

**USED:** CN5, D7.11, D7.13, D7.15, D7.2, D7.3
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['CN5', 'D7.11', 'D7.13', 'D7.15', 'D7.2', 'D7.3']

## Proposition 7.32
**Statement:** Any number either is prime or is measured by some prime number.

**Step 1.** Let N be any number. If N is measured by an unit alone, then N is prime, and the first alternative holds (D7.11).

**Step 2.** Otherwise, N is measured by some number, not by an unit alone. Hence N is composite (D7.11, D7.13).

**Step 3.** Apply 7.31 directly: since N is composite, some prime number measures N. This is the direct route because the immediately preceding proposition already supplies precisely the required conclusion in the composite case. Together with Step 1, this proves that any number either is prime or is measured by some prime number (7.31; Steps 1–2).

**USED:** 7.31, D7.11, D7.13
**Human refs (from References field):** 7.31
**Jaccard:** 0.333 — AI adds ['D7.11', 'D7.13']

## Proposition 7.33
**Statement:** Given as many numbers as we please, to find the least of those which have the same ratio with them.

**Step 1.** Let the given numbers be A₁, …, Aₙ. Find their greatest common measure g by successive applications of the two-number construction of 7.2, taking the unit when a pair is prime to one another (D7.12). The iteration is justified as follows: in successive subtraction, the common measures of x and y are exactly those of y and x − y, since multiples of a common measure remain multiples under subtraction and addition (D7.15, CN2, CN3). Thus a two-number reduction preserves all common measures; adjoining each further number preserves precisely those also measuring that number. Consequently the final g is the greatest common measure of the entire list. This pairwise route works for any finite number of given terms.

**Step 2.** For each i, let aᵢ be the count of how many times g measures Aᵢ, so that Aᵢ = g·aᵢ; a count of one is represented by the unit (D7.1, D7.2, D7.15). Since the same multiplier g produces every Aᵢ from aᵢ, we have Aᵢ:Aⱼ = aᵢ:aⱼ for every pair of indices, by 7.17, with unit cases following directly from D7.20. We choose 7.17 because its common-multiplier hypothesis is exactly the construction just made.

**Step 3.** No number greater than the unit measures every aᵢ. For suppose e did so. Grouping the g-sized portions of each Aᵢ into groups of e would show that e·g measures every Aᵢ (D7.15, CN2). But e·g is greater than g, since it contains more than one copy of g (CN5). This contradicts the choice of g as the greatest common measure. Thus the aᵢ have only the unit as a common measure (D7.12).

**Step 4.** Let B₁, …, Bₙ be any other list having the same ratios as the given list. By Step 2 and 5.11, aᵢ:aⱼ = Bᵢ:Bⱼ. Alternating gives aᵢ:Bᵢ = aⱼ:Bⱼ (7.13). In particular, all corresponding pairs aᵢ, Bᵢ have the ratio a₁:B₁. If a unit occurs, the corresponding assertion follows directly by expressing the other terms as its multiples (D7.20).

**Step 5.** Find the greatest common measure h of a₁ and B₁ by 7.2, taking h to be the unit if either entry is the unit or if the pair is prime to one another (D7.12). Write a₁ = h·r and B₁ = h·s. Then r:s = a₁:B₁, by 7.17, with unit cases given by D7.20. Moreover, r and s have no common measure greater than the unit: such a measure t would make t·h a common measure of a₁ and B₁ greater than h, exactly as in Step 3 (D7.15, CN2, CN5). Thus, when r and s are numbers, they are prime to one another (D7.12).

**Step 6.** We claim that r is the unit. Suppose instead that r is greater than the unit. If s is also greater than the unit, then r and s are the least numbers in their ratio, by 7.21. Each pair aᵢ, Bᵢ has that ratio, by Steps 4–5 and 5.11; hence 7.20 says that r measures every aᵢ. If s is the unit, the proportions aᵢ:Bᵢ = r:unit say directly that aᵢ is r times Bᵢ, so again r measures every aᵢ (D7.20, D7.15). Both cases contradict Step 3. Therefore r is the unit. Here 7.21 is applied only to a pair already shown prime to one another; no pairwise coprimality of the entire list is assumed.

**Step 7.** It follows that aᵢ:Bᵢ = unit:s for every i (Steps 4–6; 5.11). Therefore Bᵢ = s·aᵢ (D7.20). Each Bᵢ is consequently equal to aᵢ when s is the unit, and greater than aᵢ otherwise (D7.15, CN5). Since the competing list was arbitrary, a₁, …, aₙ are the least terms having the same ratios as A₁, …, Aₙ. They have been constructed by dividing the given terms by their greatest common measure, as required.

**USED:** 5.11, 7.13, 7.17, 7.2, 7.20, 7.21, CN2, CN3, CN5, D7.1, D7.12, D7.15, D7.2, D7.20
**Human refs (from References field):** 7.16, 7.19, 7.21, 7.3, D7.15, D7.20
**Jaccard:** 0.176 — AI adds ['5.11', '7.13', '7.17', '7.2', '7.20', 'CN2', 'CN3', 'CN5', 'D7.1', 'D7.12', 'D7.2']; Human adds ['7.16', '7.19', '7.3']

## Proposition 7.34
**Statement:** Given two numbers, to find the least number which they measure.

**Step 1.** Let A and B be the given numbers. If they are equal, take their common value. If one measures the other, take the greater. In either case the chosen number is measured by both, and no smaller number can be measured by the chosen number itself. Thus it is the required least number. Henceforth suppose that neither A nor B measures the other. [D7.3, D7.5, CN5]

**Step 2.** Construct the least numbers C and D having the same ratio as A and B, so that C:D = A:B. [7.33] Path choice: use this preceding construction directly, since it supplies exactly the least proportional pair to which 7.20 applies.

**Step 3.** Let D multiply A to produce L; thus L consists of D copies of A. Since C:D = A:B, the product of C and B equals the product of D and A. Therefore L also consists of C copies of B. Consequently both A and B measure L. [D7.15, 7.19, D7.5]

**Step 4.** Let T be any number measured by both A and B. Let A measure T u times, and B measure T v times. Thus multiplying A by u, or B by v, produces T. Both counts are greater than an unit: otherwise T would equal one of A and B, and the other would measure it, contrary to Step 1. Hence u and v are numbers. [D7.5, D7.15]

**Step 5.** The product of v and B equals the product of u and A, both being T. Therefore v:u = A:B. [7.19] Since C and D are the least numbers having this ratio, they measure v and u respectively the same number of times. In particular, D measures u, so u is not less than D. [7.20, D7.5, CN5]

**Step 6.** Now T consists of u copies of A, while L consists of D copies of A. If u equals D, these sums are equal; if u exceeds D, the D copies forming L are a proper part of the u copies forming T, so T is greater than L. Thus every number measured by both A and B is at least L. Since both measure L by Step 3, L is the least number which they measure, as required. [D7.15, CN2, CN5]

**USED:** 7.19, 7.20, 7.33, CN2, CN5, D7.15, D7.3, D7.5
**Human refs (from References field):** 7.16, 7.17, 7.19, 7.20, 7.21, 7.33, D7.15
**Jaccard:** 0.364 — AI adds ['CN2', 'CN5', 'D7.3', 'D7.5']; Human adds ['7.16', '7.17', '7.21']

## Proposition 7.35
**Statement:** If two numbers measure any number, the least number measured by them will also measure the same.

**Step 1.** Let A and B measure C, and let L be the least number measured by A and B, obtained by 7.34. If A equals B, or either measures the other, L is the greater of A and B (or their common value), and therefore measures C by hypothesis. Indeed, that number is a common multiple, and no number smaller than it can be measured by it (D7.5; CN5). Hence assume that neither A nor B measures the other.

**Step 2.** Since A and B measure both L and C, write
L = uA = vB, C = pA = qB,
where u, v, p, and q are the respective numbers of repetitions. They are all numbers rather than units, since equality of L or C with either A or B would make one of A and B measure the other (D7.5; D7.15). Applying 7.19 to these equal products gives
u:v = B:A and p:q = B:A.

**Step 3.** By 7.33, take the least numbers r and s having the ratio B:A. Thus u:v = r:s and p:q = r:s (5.11). Consequently, r measures u and also p, by 7.20. **Path choice:** 7.20 applies directly because r and s were chosen as the least proportional pair; there is no need to introduce coprimality.

**Step 4.** Since r:s = B:A, proposition 7.19 gives rA = sB. Call this common product M. The expression rA shows that A measures M, and the expression sB shows that B measures M. Thus M is a common multiple of A and B (D7.15; D7.5).

**Step 5.** Because r measures u, group the u copies of A making up uA into groups of r copies. Each group equals rA = M, so M measures uA = L (D7.15; CN2). If M were unequal to L, it would therefore be smaller than L (CN5). But Step 4 makes M a common multiple of A and B, contradicting the defining leastness of L from Step 1 (7.34). Hence M = L.

**Step 6.** Similarly, because r measures p, grouping the p copies of A into groups of r copies shows that M = rA measures pA = C (D7.15; CN2). Since M = L, L measures C. Therefore, if two numbers measure any number, the least number measured by them also measures that same number.

**USED:** 5.11, 7.19, 7.20, 7.33, 7.34, CN2, CN5, D7.15, D7.5
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['5.11', '7.19', '7.20', '7.33', '7.34', 'CN2', 'CN5', 'D7.15', 'D7.5']

## Proposition 7.36
**Statement:** Given three numbers, to find the least number which they measure.

**Step 1.** Let A, B, C be the three given numbers. By 7.34, find D, the least number which A and B measure. Path choice: apply the two-number construction successively, since it directly supplies the required numbers without a new construction from common measures. [7.34]

**Step 2.** Again by 7.34, find E, the least number which D and C measure. Thus D and C both measure E. [7.34]

**Step 3.** Since A and B measure D, and D measures E, both A and B measure E. Indeed, E consists of a whole number of copies of D; replacing each such copy by its constituent copies of A expresses E as a whole number of copies of A, and likewise for B. This is measurement through repeated addition. Since C also measures E, all three given numbers measure E. [D7.5, D7.15; Step 2]

**Step 4.** Let N be any number measured by A, B, and C. Since A and B measure N, their least common measured number D also measures N, by 7.35. Hence both D and C measure N. [7.35]

**Step 5.** But E was constructed as the least number measured by D and C; therefore N cannot be less than E. Since every number measured by A, B, and C has this property, and E itself is measured by all three, E is the required least number which the three given numbers measure. [7.34; Steps 2–4]

**USED:** 7.34, 7.35, D7.15, D7.5
**Human refs (from References field):** 7.34, 7.35
**Jaccard:** 0.500 — AI adds ['D7.15', 'D7.5']

## Proposition 7.37
**Statement:** If a number be measured by any number, the number which is measured will have a part called by the same name as the measuring number.

**Step 1.** Let the number B measure the number A, and let u be a unit. If A equals B, then A consists of as many units as B contains; consequently u is the B-th part of A, and the assertion holds in this case. [D7.1, D7.2]

**Step 2.** Suppose now that B is less than A. Take C consisting of as many units as there are times that B measures A. Since B measures A more than once, C is a number. By its construction, u measures C the same number of times that B measures A. [D7.2]

**Step 3.** Therefore, alternately, u measures B the same number of times that C measures A. We use the measurement-interchange proposition directly, since Step 2 supplies exactly its hypotheses. [7.15]

**Step 4.** Since B contains more than one unit, C measures A more than once; hence C is less than A and is a part of A. [D7.2, CN5, D7.3] Moreover, by Step 3, A consists of as many equal portions C as there are units in B. Thus C is precisely the B-th part of A—the part called by the same name as the measuring number B. Therefore the number measured has the required part. [D7.2, D7.3]

**USED:** 7.15, CN5, D7.1, D7.2, D7.3
**Human refs (from References field):** 7.15
**Jaccard:** 0.200 — AI adds ['CN5', 'D7.1', 'D7.2', 'D7.3']

## Proposition 7.38
**Statement:** If a number have any part whatever, it will be measured by a number called by the same name as the part.

**Step 1.** Let A have an nth part B, and let C be the number composed of n units. Thus n copies of B make A, and C is the number called by the same name as the given part. [D7.2, D7.3; meaning of “nth part.”]

**Step 2.** If B is a unit, A and C consist of the same multitude of units and therefore are equal; consequently C measures A once. The conclusion therefore holds in this case. Henceforth suppose B is a number. [D7.1, D7.2, CN4.]

**Step 3.** Take a unit u. The unit u measures C exactly n times, while B measures A exactly n times. Thus these two measurements are made equally often. [D7.2, D7.3; Step 1.]

**Step 4.** Apply 7.15 directly, since it interchanges precisely these equally repeated measurements: u measures B the same number of times that C measures A. In particular, C measures A. Since C is the number called by the same name as the given part, the required conclusion follows. [7.15; Step 1.]

**USED:** 7.15, CN4, D7.1, D7.2, D7.3
**Human refs (from References field):** 7.15
**Jaccard:** 0.200 — AI adds ['CN4', 'D7.1', 'D7.2', 'D7.3']

## Proposition 7.39
**Statement:** To find the number which is the least that will have given parts.

**Step 1.** Let the given parts be the a₁-th, a₂-th, …, aᵣ-th parts, where a₁, a₂, …, aᵣ are their naming numbers. By 7.37 and 7.38, a number has all these parts if and only if every aᵢ measures it. Thus the chosen route is to construct their least common multiple. The two-number construction 7.34 is the natural starting point because it can be repeated for any finite list.

**Step 2.** Set L₁ = a₁. For each j from 2 through r, construct Lⱼ as the least number measured by both Lⱼ₋₁ and aⱼ, using 7.34.

**Step 3.** Every aᵢ with i ≤ j measures Lⱼ. This holds immediately for j = 1. At each succeeding stage, Lⱼ₋₁ and aⱼ measure Lⱼ by its construction (7.34). Each earlier aᵢ measures Lⱼ₋₁ and therefore measures Lⱼ: whole copies of Lⱼ₋₁ consist in turn of whole copies of aᵢ, by the definitions of number and multiplication (D7.2, D7.15). Consequently every naming number aᵢ measures Lᵣ.

**Step 4.** Moreover, Lⱼ measures every number measured by all of a₁, …, aⱼ. For j = 1 this follows from L₁ = a₁. Suppose it holds at the preceding stage, and let T be measured by a₁, …, aⱼ. Then Lⱼ₋₁ measures T, and aⱼ also measures T. Their least common multiple Lⱼ therefore measures T, by 7.35. Repeating this argument shows that Lᵣ measures every common multiple of all the naming numbers.

**Step 5.** Since every aᵢ measures Lᵣ, the number Lᵣ has every prescribed part, by 7.37. If T is any number having those parts, every aᵢ measures T, by 7.38; hence Lᵣ measures T by Step 4. Thus T is a multiple of Lᵣ (D7.5), and is either equal to Lᵣ or greater than it, since a whole containing more than one copy is greater than one copy (CN5). Therefore Lᵣ is the least number having the given parts, as required.

**USED:** 7.34, 7.35, 7.37, 7.38, CN5, D7.15, D7.2, D7.5
**Human refs (from References field):** 7.36, 7.37, 7.38
**Jaccard:** 0.222 — AI adds ['7.34', '7.35', 'CN5', 'D7.15', 'D7.2', 'D7.5']; Human adds ['7.36']
