# Book 7 of Euclid's Elements — Step-by-Step AI Proofs (Run A)

## Proposition 7.1
**Statement:** Two unequal numbers being set out, and the less being continually subtracted in turn from the greater, if the number which is left never measures the one before it until an unit is left, the original numbers will be prime to one another.

**Step 1.** Let A>B be the given numbers, whose stipulated successive subtractions eventually leave an unit. The unit measures both numbers, since each is composed of units. It therefore suffices to show that no common measure other than the unit is possible. We take the direct route of preserving an arbitrary common measure through each individual subtraction. [D7.2, D7.12]

**Step 2.** Let d be any common measure of A and B. At any stage suppose that d measures both current quantities X>Y. Each then consists of whole copies of d. From the copies constituting X remove as many copies as constitute Y. The removed quantity equals Y, so the remaining copies equal X−Y, by subtraction of equals from equals. Since X−Y is positive, it is still composed of one or more whole copies of d. Thus d measures X−Y as well as Y. [D7.5, CN3]

**Step 3.** Apply Step 2 at every individual subtraction, interchanging the roles of the quantities whenever necessary. The same d continues to measure both current quantities throughout the stipulated process. Consequently, when an unit is left, d measures that unit: the unit consists of one or more whole copies of d. [D7.5, CN3]

**Step 4.** Such a d must itself be an unit. Indeed, if d were a number rather than an unit, it would be a multitude of units and hence greater than a single unit. But a quantity composed of one or more copies of d cannot be smaller than d, so it could not equal an unit. Thus every common measure of A and B is an unit. Since the unit does measure both, the original numbers are prime to one another, as required. [D7.1, D7.2, CN5, D7.12]

**USED:** CN3, CN5, D7.1, D7.12, D7.2, D7.5
**Human refs (from References field):** D7.12
**Jaccard:** 0.167 — AI adds ['CN3', 'CN5', 'D7.1', 'D7.2', 'D7.5']

## Proposition 7.2
**Statement:** Given two numbers not prime to one another, to find their greatest common measure.

**Step 1.** Let A and B be the given numbers, not prime to one another, and name them so that A ≥ B. If A = B, return B. If B measures A, likewise return B. In either case B measures both numbers, and no common measure can exceed B, since it must measure B itself. Thus B is their greatest common measure. Henceforth suppose A > B and B does not measure A. [D7.5, CN5]

**Step 2.** For this remaining case choose successive subtraction, the route supplied by the immediately preceding proposition 7.1. At each stage, stop if the lesser member of the current pair measures the greater. Otherwise subtract the lesser from the greater and reorder the lesser and the positive remainder as a new pair. The greater member of the new pair is strictly smaller than the previous greater member. Since a number is a finite multitude of units, these decreases cannot continue indefinitely. Consequently the procedure reaches a pair in which the lesser, say D, measures the greater. [7.1, D7.2, CN5]

**Step 3.** D is not an unit. For if an unit were reached, no earlier remainder would have measured its predecessor, since the procedure would already have stopped. Proposition 7.1 would then imply that A and B were prime to one another—that an unit alone measured them in common—contrary to the hypothesis. Thus D is a number. [7.1, D7.12]

**Step 4.** D measures both members of the terminal pair: the greater by the stopping condition, and itself once. Now reverse the subtractions. At any stage, the former greater member is the sum of the former lesser member and the remainder. If both of these consist of whole copies of D, their sum also consists of whole copies of D. Thus D measures both members of the preceding pair. Repeating this through the finite sequence shows that D measures both A and B. [D7.5, CN2]

**Step 5.** Let E be any common measure of A and B. Follow the subtractions forwards. Whenever E measures both members of a pair, subtracting the lesser removes whole copies of E from the greater, so the remainder also consists of whole copies of E. Hence E measures both members of every succeeding pair, and in particular E measures D. [D7.5, CN3]

**Step 6.** Since E measures D, it cannot be greater than D: either it equals D or it is a part of D. Therefore every common measure of A and B is at most D. By Step 4, D itself is a common measure. Thus D is their greatest common measure, and the stated finite procedure finds it. [D7.5, CN5]

**USED:** 7.1, CN2, CN3, CN5, D7.12, D7.2, D7.5
**Human refs (from References field):** 7.1
**Jaccard:** 0.143 — AI adds ['CN2', 'CN3', 'CN5', 'D7.12', 'D7.2', 'D7.5']

## Proposition 7.3
**Statement:** Given three numbers not prime to one another, to find their greatest common measure.

**Step 1.** Let the given numbers be A, B, and C. Since they are not prime to one another, they have a common measure H greater than a unit; H need not be known for the construction. Choose the direct route of repeated subtraction on the three numbers themselves, preserving their common measures throughout. [D7.12, D7.2]

**Step 2.** Write down the three numbers. Whenever they are not all equal, choose a greatest entry X and a least entry Y, and replace X by X − Y, leaving the other two entries unchanged. Here X > Y, so the remainder is positive. This replacement preserves exactly the common measures of the triple: if E measures X and Y, removing from the whole copies of E composing X those composing Y leaves whole copies of E composing X − Y. Conversely, if E measures X − Y and Y, adding those copies shows that E measures X. The unchanged third entry imposes the same condition before and after the replacement. [D7.5, CN3, CN2]

**Step 3.** Repeat this operation until all three entries are equal. By Step 2, H continues to measure every entry, so each entry remains a number greater than a unit. Moreover, each operation decreases the total number of units in the three entries by the positive number Y. That total starts as a finite multitude of units and cannot undergo indefinitely many such decreases. Thus the process terminates; since another operation is possible whenever the entries are not all equal, its terminal entries are D, D, D for some number D. [D7.2, D7.5, CN5]

**Step 4.** The number D measures each terminal entry. Reversing the replacements, at each reversal the restored entry is the sum of two entries measured by D, and therefore is also measured by D. Consequently D measures the original numbers A, B, and C. [D7.5, CN2]

**Step 5.** Let E be any common measure of A, B, and C. By the preservation established in Step 2, E measures every terminal entry, and hence measures D. Therefore E cannot exceed D: either D is one copy of E and equals it, or D contains more than one such copy and is greater than E. Thus no common measure of A, B, and C is greater than D. The constructed number D is therefore their greatest common measure, as required. [D7.5, CN5]

**USED:** CN2, CN3, CN5, D7.12, D7.2, D7.5
**Human refs (from References field):** 7.2
**Jaccard:** 0.000 — AI adds ['CN2', 'CN3', 'CN5', 'D7.12', 'D7.2', 'D7.5']; Human adds ['7.2']

## Proposition 7.4
**Statement:** Any number is either a part or parts of any number, the less of the greater.

**Step 1.** Let A and B be any numbers, with A less than B. Use the defining distinction directly, rather than a common-measure construction. If A measures B, then A is a part of B, by the definition of a part. [D7.3]

**Step 2.** If A does not measure B, then A is parts of B, by the definition of parts. [D7.4] Since A either measures B or does not, these cases exhaust the possibilities. Therefore any number is either a part or parts of any number, the less of the greater.

**USED:** D7.3, D7.4
**Human refs (from References field):** 7.2
**Jaccard:** 0.000 — AI adds ['D7.3', 'D7.4']; Human adds ['7.2']

## Proposition 7.5
**Statement:** If a number be a part of a number, and another be the same part of another, the sum will also be the same part of the sum that the one is of the one.

**Step 1.** Let a be a part of b, and let c be the same part of d. We proceed directly by grouping equal measuring parts. By the definition of a part and the hypothesis that the parts are the same, b consists of some number k of copies of a, while d consists of exactly k copies of c, with k greater than one. [D7.3]

**Step 2.** Pair each copy of a in b with one copy of c in d. Each pair has sum a+c, since equals added to equals give equal wholes. There are exactly k such pairs. Moreover, these pairs together contain exactly all the units composing b and d, so their total is b+d. Thus b+d consists of exactly k equal portions, each equal to a+c. [CN2, D7.2]

**Step 3.** Consequently a+c measures b+d exactly k times and, since k is greater than one, is less than b+d. Hence a+c is a part of b+d. Its measuring count is the same as that of a in b, so it is the same part of b+d that a is of b. Therefore the sum is the same part of the sum that the one is of the one. [D7.3]

**USED:** CN2, D7.2, D7.3
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['CN2', 'D7.2', 'D7.3']

## Proposition 7.6
**Statement:** If a number be parts of a number, and another be the same parts of another, the sum will also be the same parts of the sum that the one is of the one.

**Step 1.** Let A be parts of B, and let C be the same parts of D. Unpacking “the same parts,” take constituent quantities u and v and whole counts m<n such that A consists of m copies of u, B of n copies of u, C of m copies of v, and D of n copies of v. Thus each constituent is the same single part of its respective whole, and the two given numbers contain equally many such constituents. Here a constituent may be a number or a unit, and expressions such as mu mean repeated addition. [D7.2, D7.3, D7.4]

**Step 2.** We take the direct route through the immediately preceding single-part addition theorem, VII.5. Since u is the same single part of B that v is of D, that theorem gives that u+v is the same single part of B+D: the latter consists of n copies of u+v. If either constituent is a unit, obtain this assertion directly by pairing the n constituent copies in B with those in D; the resulting n pairs are each equal to u+v. [7.5; D7.2, CN2 for the unit case]

**Step 3.** Likewise, pair the m copies of u composing A with the m copies of v composing C. Addition of these equal constituent pairs shows that A+C consists of m copies of u+v. Consequently, A+C contains m of the n equal parts composing B+D, just as A contains m of the n equal parts composing B. [CN2, D7.2]

**Step 4.** Moreover, A+C does not measure B+D. For suppose B+D consisted of k copies of A+C. By Step 3 it would then consist of km copies of u+v, whereas Step 2 gives n copies. These counts must agree: otherwise the sum with fewer copies would be a proper part of the other sum and could not equal it. Thus n=km. But then B, consisting of n copies of u, would consist of k groups of m copies of u—that is, k copies of A. This contradicts the hypothesis that A is parts of B and therefore does not measure B. [CN2, CN5, D7.3, D7.4]

**Step 5.** Hence A+C is parts, not a single measuring part, of B+D; and its parts are precisely the same m out of n equal parts that A is of B. Therefore the sum is the same parts of the sum that the one is of the one. [D7.3, D7.4]

**USED:** 7.5, CN2, CN5, D7.2, D7.3, D7.4
**Human refs (from References field):** 7.5
**Jaccard:** 0.167 — AI adds ['CN2', 'CN5', 'D7.2', 'D7.3', 'D7.4']

## Proposition 7.7
**Statement:** If a number be that part of a number, which a number subtracted is of a number subtracted, the remainder will also be the same part of the remainder that the whole is of the whole.

**Step 1.** Let A be the given part of B, and let C, subtracted from A, be the same part of D, subtracted from B. Thus C < A and D < B. Take the direct route through measurement and repeated addition: there is one integer m > 1 such that B consists of m copies of A, while D consists of m copies of C. This is what it means for A and C to be the same part of B and D respectively. [D7.3, D7.15]

**Step 2.** From each of the m copies of A forming B, subtract a copy of C. The remainders are all equal to A − C, since equals subtracted from equals leave equal remainders. The amount removed altogether is precisely the m copies of C forming D. Consequently, B − D consists of m copies of A − C. [CN3, D7.15]

**Step 3.** Therefore A − C measures B − D exactly m times, just as A measures B. Hence the remainder A − C is the same part of the remainder B − D that the whole A is of the whole B, as required. [D7.3]

**USED:** CN3, D7.15, D7.3
**Human refs (from References field):** 7.5
**Jaccard:** 0.000 — AI adds ['CN3', 'D7.15', 'D7.3']; Human adds ['7.5']

## Proposition 7.8
**Statement:** If a number be the same parts of a number that a number subtracted is of a number subtracted, the remainder will also be the same parts of the remainder that the whole is of the whole.

**Step 1.** Let A be the same parts of B that C, subtracted from A, is of D, subtracted from B. Thus C<A and D<B. Unpack the hypothesis into equal constituent parts: for the same counts m<n, A consists of m copies of a measure a and B of n copies of a, while C consists of m copies of a measure c and D of n copies of c. The measures may themselves be units. We use direct subtraction of corresponding constituent parts, without transforming proportions. [D7.2, D7.3, D7.4]

**Step 2.** Since A>C and each consists of the same number m of equal constituent parts, a>c: otherwise repeated addition would give A≤C. Let e be the positive remainder after c is subtracted from a. Thus each a consists of c together with e. [D7.2, CN2]

**Step 3.** In the m constituent parts of A, replace each a by c together with e. Adding these equal decompositions shows that A consists of C together with m copies of e. Subtracting C therefore leaves A−C equal to m copies of e. In precisely the same way, the n constituent parts of B show that B consists of D together with n copies of e; subtracting D leaves B−D equal to n copies of e. [CN2, CN3]

**Step 4.** Consequently, A−C consists of m of the n equal constituent parts of B−D, just as A consists of m of the n equal constituent parts of B. Hence the remainder A−C is the same parts of the remainder B−D that the whole A is of the whole B, as required. [D7.3, D7.4]

**USED:** CN2, CN3, D7.2, D7.3, D7.4
**Human refs (from References field):** 7.7
**Jaccard:** 0.000 — AI adds ['CN2', 'CN3', 'D7.2', 'D7.3', 'D7.4']; Human adds ['7.7']

## Proposition 7.9
**Statement:** If a number be a part of a number, and another be the same part of another, alternately also, whatever part or parts the first is of the third, the same part, or the same parts, will the second also be of the fourth.

**Step 1.** Let A be a part of B, and C the same part of D. Thus B is composed of some number n of copies of A, and D of the same number n of copies of C:
B = A + ⋯ + A, D = C + ⋯ + C,
with n summands in each. This expresses that A and C measure B and D respectively the same number of times. We use the direct route of adding these corresponding copies. [D7.2, D7.3]

**Step 2.** Suppose A is a part of C. By 7.5, the sum of two copies of A is the same part of the sum of two copies of C. Apply 7.5 again to these sums and one further copy of A and C respectively. Continuing through the n copies, B is the same part of D that A is of C. Thus 7.5 is the directly applicable addition result in this case. [7.5]

**Step 3.** Suppose instead that A is parts of C. By 7.6, the sum of two copies of A is the same parts of the sum of two copies of C. Apply 7.6 again to these sums and one further corresponding copy, and continue through all n copies. Consequently B is the same parts of D that A is of C. Here 7.6 supplies precisely the required parts-case addition result. [7.6]

**Step 4.** A lesser number is either a part or parts of a greater number, so these cases exhaust the comparison asserted in the proposition. Therefore, whatever part or parts the first number A is of the third C, the second B is the same part or the same parts of the fourth D. [7.4]

**USED:** 7.4, 7.5, 7.6, D7.2, D7.3
**Human refs (from References field):** 7.5, 7.6
**Jaccard:** 0.400 — AI adds ['7.4', 'D7.2', 'D7.3']

## Proposition 7.10
**Statement:** If a number be parts of a number, and another be the same parts of another, alternately also, whatever parts or part the first is of the third, the same parts or the same part will the second also be of the fourth.

**Step 1.** Let A be parts of B, and C the same parts of D. By the meaning of the same parts, there are measuring quantities u and v and the same two counts m and n such that A consists of m copies of u, B of n copies of u, C of m copies of v, and D of n copies of v. Thus u is the same part of B that v is of D, and u is also the same part of A that v is of C. In the part-or-parts comparison asserted in the conclusion, A<C; hence u<v. [D7.2, D7.3, D7.4]

**Step 2.** First dispose of the possibility that u is a unit. If v consists of q units, C consists of m groups of q units. Regrouping these units into q groups of m units shows that C consists of q copies of A. Likewise D consists of q copies of B. Therefore A is the same part of C that B is of D, as required. Henceforth u and v are both numbers. [D7.2, D7.3]

**Step 3.** Since u<v, u is either a part or parts of v. We use the earlier equal-part alternation theorem, VII.9, directly on the measuring numbers: both pairs of equal-part relations needed for it were obtained in Step 1. This avoids a separate argument about sums. [7.4, 7.9]

**Step 4.** Since u is the same part of B that v is of D, VII.9 gives, alternately, that whatever part or parts u is of v, B is the same part or parts of D. [7.9]

**Step 5.** Since u is also the same part of A that v is of C, VII.9 gives that A is the same part or parts of C that u is of v. Together with Step 4, this proves that whatever parts or part A is of C, B is the same parts or the same part of D. This is the required conclusion. [7.9]

**USED:** 7.4, 7.9, D7.2, D7.3, D7.4
**Human refs (from References field):** 7.5, 7.6, 7.9
**Jaccard:** 0.143 — AI adds ['7.4', 'D7.2', 'D7.3', 'D7.4']; Human adds ['7.5', '7.6']

## Proposition 7.11
**Statement:** If, as whole is to whole, so is a number subtracted to a number subtracted, the remainder will also be to the remainder as whole to whole.

**Step 1.** Let the wholes be A and B, and let a and b be subtracted from them, respectively, with positive remainders R = A − a and S = B − b. Suppose A:B = a:b. By the definition of numerical proportion, the corresponding relations are the same part, the same parts, or the same multiple. We take the direct numerical route, using the earlier subtraction proposition appropriate to each relation. [D7.20]

**Step 2.** If A = B, the given proportion implies a = b. Subtracting equals from equals gives R = S, so R:S = A:B. [D7.20, CN3]

**Step 3.** Suppose A is the same part of B that a is of b. Proposition 7.7, the first directly applicable subtraction result, says that R is the same part of S that A is of B. Hence R:S = A:B by the definition of numerical proportion. [7.7, D7.20]

**Step 4.** Suppose A is the same parts of B that a is of b. Here the parts version, Proposition 7.8, applies: R is the same parts of S that A is of B. Consequently R:S = A:B. [7.8, D7.20]

**Step 5.** Suppose A is the same multiple of B that a is of b, with the wholes unequal. Then B is the same part of A that b is of a, by the definitions of part and multiple. Apply Proposition 7.7 to these reversed pairs: after b is subtracted from B and a from A, S is the same part of R that B is of A. Thus R is the same multiple of S that A is of B, and therefore R:S = A:B. [D7.3, D7.5, 7.7, D7.20]

**Step 6.** The cases furnished by the definition of numerical proportion have all been covered. Therefore the remainder is to the remainder as the whole is to the whole: (A − a):(B − b) = A:B. [D7.20]

**USED:** 7.7, 7.8, CN3, D7.20, D7.3, D7.5
**Human refs (from References field):** 7.7, 7.8, D7.20
**Jaccard:** 0.500 — AI adds ['CN3', 'D7.3', 'D7.5']

## Proposition 7.12
**Statement:** If there be as many numbers as we please in proportion, then, as one of the antecedents is to one of the consequents, so are all the antecedents to all the consequents.

**Step 1.** Let the given proportional pairs be A₁:B₁, A₂:B₂, …, Aₙ:Bₙ, and put A = A₁ + ⋯ + Aₙ and B = B₁ + ⋯ + Bₙ. By the definition of numerical proportion, the antecedents are respectively the same multiple, the same part, or the same parts of their consequents. We use the direct numerical addition results: 7.5 for a part and 7.6 for parts. [D7.20]

**Step 2.** If each Aᵢ equals Bᵢ, adding these equalities gives A = B. Thus A:B is the same equality ratio as each Aᵢ:Bᵢ. [CN2, D7.20]

**Step 3.** Suppose each Aᵢ is the same part of Bᵢ. By 7.5, A₁ + A₂ is that same part of B₁ + B₂. Applying 7.5 again to these sums and the next pair, and continuing through all the given pairs, shows that A is that same part of B. Hence A:B = Aᵢ:Bᵢ for every i. [7.5, D7.20]

**Step 4.** Suppose each Aᵢ is the same parts of Bᵢ. By 7.6, A₁ + A₂ is those same parts of B₁ + B₂. Repeating this addition with each succeeding pair shows that A is those same parts of B. Hence again A:B = Aᵢ:Bᵢ for every i. [7.6, D7.20]

**Step 5.** Suppose each Aᵢ is the same multiple, greater than one, of Bᵢ. Then each Bᵢ is the same part of Aᵢ. Repeated application of 7.5 to these reversed pairs shows that B is that same part of A. Therefore A is the same multiple of B that each Aᵢ is of Bᵢ, and so A:B = Aᵢ:Bᵢ. [D7.3, D7.5, 7.5, D7.20]

**Step 6.** Thus in every case permitted by numerical proportion, as any antecedent is to its corresponding consequent, so is the sum of all the antecedents to the sum of all the consequents. This proves the proposition. [D7.20]

**USED:** 7.5, 7.6, CN2, D7.20, D7.3, D7.5
**Human refs (from References field):** 7.5, 7.6, D7.20
**Jaccard:** 0.500 — AI adds ['CN2', 'D7.3', 'D7.5']

## Proposition 7.13
**Statement:** If four numbers be proportional, they will also be proportional alternately.

**Step 1.** Let A:B = C:D. We must prove A:C = B:D. Interchanging the two given ratios or reversing both preserves proportionality: reversal exchanges a common multiple with a common part, and exchanges the two counts in a common parts relation. These operations also merely interchange or reverse the ratios in the desired conclusion. Thus we may arrange that A is a least of the four numbers. (D7.3, D7.4, D7.5, D7.20.)

**Step 2.** The equality cases are immediate. If A=B, the given proportionality implies C=D, so A:C = B:D. If A=C, reverse the given ratios to obtain B:A = D:A; thus B and D are the same multiple, part, or parts of the same number, and hence B=D. Again A:C = B:D. We may therefore suppose A<B and A<C. We use the direct part-or-parts route, taking the part case first. (D7.20.)

**Step 3.** Suppose A measures B. Then A is a part of B, and the hypothesis says that C is the same part of D. By 7.9, alternately, whatever part or parts A is of C, B is the same part or parts of D. Consequently A:C = B:D. (D7.3, D7.20, 7.9.)

**Step 4.** Suppose A does not measure B. Then A is parts of B, and the hypothesis says that C is the same parts of D. By 7.10, alternately, whatever parts or part A is of C, B is the same parts or part of D. Consequently A:C = B:D. These cases exhaust the possibilities, and undoing any relabeling from Step 1 gives the required conclusion for the original numbers. Therefore four proportional numbers are also proportional alternately. (D7.4, D7.20, 7.10.)

**USED:** 7.10, 7.9, D7.20, D7.3, D7.4, D7.5
**Human refs (from References field):** 7.10, D7.20
**Jaccard:** 0.333 — AI adds ['7.9', 'D7.3', 'D7.4', 'D7.5']

## Proposition 7.14
**Statement:** If there be as many numbers as we please, and others equal to them in multitude, which taken two and two are in the same ratio, they will also be in the same ratio ex aequali.

**Step 1.** Let the two collections be A₁, …, Aₙ and B₁, …, Bₙ, with n ≥ 2, and suppose that Aᵢ : Aᵢ₊₁ = Bᵢ : Bᵢ₊₁ for every i < n. By the definition of ex aequali, we must show A₁ : Aₙ = B₁ : Bₙ. We choose the direct numerical route through alternation, so that no passage from numbers to magnitudes is needed. [D5.17]

**Step 2.** Apply numerical alternation to each given proportion. For every i < n, this gives
Aᵢ : Bᵢ = Aᵢ₊₁ : Bᵢ₊₁. [7.13]

**Step 3.** By the definition of proportional numbers, each equality in Step 2 says that Aᵢ is the same multiple, or the same part, or the same parts, of Bᵢ that Aᵢ₊₁ is of Bᵢ₊₁. This relation is therefore unchanged along the finite chain: A₁ is the same multiple, part, or parts of B₁ that Aₙ is of Bₙ. By the same definition, A₁ : B₁ = Aₙ : Bₙ. [D7.20]

**Step 4.** Alternating this last proportion gives A₁ : Aₙ = B₁ : Bₙ. Thus the first and last numbers of the two collections are proportional, which is precisely that the collections are in the same ratio ex aequali. [7.13; D5.17]

**USED:** 7.13, D5.17, D7.20
**Human refs (from References field):** 7.13
**Jaccard:** 0.333 — AI adds ['D5.17', 'D7.20']

## Proposition 7.15
**Statement:** If an unit measure any number, and another number measure any other number the same number of times, alternately also, the unit will measure the third number the same number of times that the second measures the fourth.

**Step 1.** Let u be the unit, B the second number, C the third, and D the fourth. Suppose that u measures B the same number of times that C measures D. We use a direct decomposition into units, keeping the unit distinct from a number. Denote the common repetition count by r: B consists of r copies of u, and D consists of r copies of C. Here r denotes only a repetition count. [D7.1, D7.2]

**Step 2.** Since C is a multitude composed of units, let it consist of s copies of u. Decompose each of the r copies of C composing D into these s units. Thus D is composed of r groups, each containing s units. [D7.2]

**Step 3.** Regroup these units as follows: take the first unit from every group to form one new group, the second unit from every group to form another, and continue through the s positions. Each new group contains exactly r units, and therefore equals B, by repeated addition of equals. There are exactly s new groups. Every original unit occurs in exactly one new group, so the regrouped collection coincides with the original collection composing D; its whole is therefore D. Hence D consists of s copies of B. [D7.2, CN2, CN4]

**Step 4.** Consequently B measures D exactly s times. But C consists of s units, so u also measures C exactly s times. Therefore, alternately, the unit measures the third number the same number of times that the second measures the fourth, as required. [D7.1, D7.2]

**USED:** CN2, CN4, D7.1, D7.2
**Human refs (from References field):** 7.12
**Jaccard:** 0.000 — AI adds ['CN2', 'CN4', 'D7.1', 'D7.2']; Human adds ['7.12']

## Proposition 7.16
**Statement:** If two numbers by multiplying one another make certain numbers, the numbers so produced will be equal to one another.

**Step 1.** Let A, by multiplying B, produce C, and let B, by multiplying A, produce D. Take a unit u. Since a number is composed of units, and multiplication repeats the multiplied number as many times as there are units in the multiplier, u measures A the same number of times that B measures C. [D7.2, D7.15]

**Step 2.** Apply VII.15 directly: this is the natural choice because Step 1 gives exactly its equal-count-of-measures hypothesis. Alternately, u measures B the same number of times that A measures C. [7.15]

**Step 3.** Since B, by multiplying A, produces D, A is repeated in D as many times as there are units in B. Thus u measures B the same number of times that A measures D. [D7.2, D7.15]

**Step 4.** Consequently C and D each consist of the same number of copies of A. Adding these equal copies to equal copies gives equal wholes, by repeated application of Common Notion 2. Hence C = D: the numbers produced by the two numbers multiplying one another are equal. [CN2]

**USED:** 7.15, CN2, D7.15, D7.2
**Human refs (from References field):** 7.15
**Jaccard:** 0.250 — AI adds ['CN2', 'D7.15', 'D7.2']

## Proposition 7.17
**Statement:** If a number by multiplying two numbers make certain numbers, the numbers so produced will have the same ratio as the numbers multiplied.

**Step 1.** Let the number A, by multiplying the numbers B and C, produce D and E respectively. By the definition of multiplication, D consists of as many copies of B as there are units in A, and E consists of the same number of copies of C. Thus D is the same multiple of B that E is of C. [D7.15, D7.5]

**Step 2.** Use these equal multiplicities directly, since they give a proportion by the definition of proportional numbers:
D : B = E : C. [D7.20]

**Step 3.** Alternating this proportion gives
D : E = B : C. [7.13]
Therefore the numbers produced have the same ratio as the numbers multiplied, as required.

**USED:** 7.13, D7.15, D7.20, D7.5
**Human refs (from References field):** 7.13, D7.20
**Jaccard:** 0.500 — AI adds ['D7.15', 'D7.5']

## Proposition 7.18
**Statement:** If two numbers by multiplying any number make certain numbers, the numbers so produced will have the same ratio as the multipliers.

**Step 1.** Let the numbers A and B, by multiplying a number C, produce D and E respectively. We take the direct common-multiplier route, since reversing the products brings the hypothesis into that form. By VII.16, C multiplying A produces D, and C multiplying B produces E. [7.16]

**Step 2.** Thus the same number C, by multiplying A and B, produces D and E. By VII.17, the products have the same ratio as the numbers multiplied: D:E = A:B. Therefore the numbers originally produced have the same ratio as the original multipliers, as required. [7.17]

**USED:** 7.16, 7.17
**Human refs (from References field):** 7.16, 7.17
**Jaccard:** 1.000 — Perfect match.

## Proposition 7.19
**Statement:** If four numbers be proportional, the number produced from the first and fourth will be equal to the number produced from the second and third; and, if the number produced from the first and fourth be equal to that produced from the second and third, the four numbers will be proportional.

**Step 1.** Let the four numbers, in order, be A, B, C, D. Write P = AD, Q = BC, and R = BD, where XY denotes the number produced by X multiplying Y. We use R as a common consequent, so that the multiplication propositions apply directly without interchanging factors. Since A and B, by multiplying D, produce P and R, respectively, we have
A : B = P : R.
Here 7.18 is the direct choice because the multipliers vary while the number multiplied remains fixed. [7.18]

**Step 2.** Since B, by multiplying C and D, produces Q and R, respectively, we have
C : D = Q : R.
Here 7.17 applies directly because the multiplier is fixed while the numbers multiplied vary. [7.17]

**Step 3.** Suppose first that the four numbers are proportional: A : B = C : D. Combining this hypothesis with the ratios in Steps 1 and 2 gives P : R = Q : R, since ratios equal to the same ratio are equal to one another. Numbers having the same ratio to the same number are equal; hence P = Q. Therefore AD = BC: the product of the first and fourth equals the product of the second and third. [5.11, 5.9]

**Step 4.** Conversely, suppose AD = BC, so P = Q. Consequently P : R and Q : R are the same ratio. By Steps 1 and 2, A : B and C : D are each equal to this same ratio, and therefore A : B = C : D. Thus the four numbers are proportional. Both implications are proved. [5.11]

**USED:** 5.11, 5.9, 7.17, 7.18
**Human refs (from References field):** 5.7, 5.9, 7.17, 7.18
**Jaccard:** 0.600 — AI adds ['5.11']; Human adds ['5.7']

## Proposition 7.20
**Statement:** The least numbers of those which have the same ratio with them measure those which have the same ratio the same number of times, the greater the greater and the less the less.

**Step 1.** Let A, B be the least numbers having the same ratio as C, D, with A corresponding to C and B to D. Thus A:B = C:D, and leastness gives A ≤ C and B ≤ D. By alternation, A:C = B:D. If A = C, this proportion gives B = D, and each least number measures its corresponding number once. We may therefore suppose A < C and B < D. [7.13, D7.20]

**Step 2.** By VII.4, A is either a part or parts of C. We choose this alternative directly because leastness will exclude the parts case by producing a smaller pair in the original ratio. [7.4]

**Step 3.** Suppose that A does not measure C, so that A is parts, rather than a part, of C. Since A:C = B:D, B is the same parts of D. Accordingly, divide C and D into the same number of equal numerical parts, so that A consists of a certain number of the parts of C and B consists of that same number of the parts of D. Let E be one such part of C and F one such part of D. The number of parts making up A and B is greater than one: otherwise A would itself be a part of C and would measure it. Thus E measures A the same number of times that F measures B, while E < A and F < B. [D7.3, D7.4, D7.20, CN5]

**Step 4.** Since E and F measure A and B respectively the same number of times, E:A = F:B. Alternating gives E:F = A:B. But E < A and F < B, contradicting the choice of A, B as the least numbers in this ratio. Hence the parts case is impossible. [D7.20, 7.13]

**Step 5.** Therefore A is a part of C and measures it. Because A:C = B:D, B is the same part of D and consequently measures D the same number of times that A measures C. Thus the least numbers in a given ratio measure any numbers having that ratio the same number of times, the greater measuring the greater and the less the less. [D7.3, D7.20]

**USED:** 7.13, 7.4, CN5, D7.20, D7.3, D7.4
**Human refs (from References field):** 7.12, 7.13, 7.4, D7.20
**Jaccard:** 0.429 — AI adds ['CN5', 'D7.3', 'D7.4']; Human adds ['7.12']

## Proposition 7.21
**Statement:** Numbers prime to one another are the least of those which have the same ratio with them.

**Step 1.** Let A and B be numbers prime to one another. Thus their only common measure is the unit. Suppose, for a contradiction, that they are not the least numbers having their ratio, and take C and D to be the least numbers with C:D = A:B. [D7.12]

**Step 2.** Apply VII.20 directly, since it concerns the least representatives of this very ratio. C measures A as many times as D measures B. This common number of repetitions cannot be one, for then C = A and D = B, contrary to the supposition. Hence the repetitions constitute a number E greater than the unit. [7.20; D7.2]

**Step 3.** By the definition of multiplication, E multiplying C produces A, and E multiplying D produces B. By commutativity of multiplication, C multiplying E therefore produces A, and D multiplying E produces B. Consequently E measures both A and B. [D7.15; 7.16]

**Step 4.** Thus A and B have a common measure E other than the unit, contradicting their being prime to one another. The supposition is therefore false: numbers prime to one another are the least of those which have the same ratio with them. [D7.12]

**USED:** 7.16, 7.20, D7.12, D7.15, D7.2
**Human refs (from References field):** 7.16, 7.20, D7.12
**Jaccard:** 0.600 — AI adds ['D7.15', 'D7.2']

## Proposition 7.22
**Statement:** The least numbers of those which have the same ratio with them are prime to one another.

**Step 1.** Let A and B be the least numbers among those having their ratio. Suppose that they are not prime to one another. Then they have a common measure d greater than the unit. We use any such common measure; finding the greatest is unnecessary. [D7.12]

**Step 2.** Let a and b count how many times d measures A and B, respectively. Thus a multiplying d produces A, and b multiplying d produces B. [D7.15]

**Step 3.** By commutativity of multiplication, d multiplying a produces A, and d multiplying b produces B. Consequently A:B = a:b. We choose the common-multiplier proposition because it gives the required equality of ratios directly. [7.16, 7.17]

**Step 4.** Since d is greater than the unit, A consists of more than one copy of a, and B consists of more than one copy of b. Hence a < A and b < B, since the whole is greater than its part. This contradicts the assumption that A and B are the least numbers having their ratio. [D7.15, CN5]

**Step 5.** Therefore A and B have no common measure other than the unit. They are accordingly prime to one another. Thus the least numbers of those which have the same ratio with them are prime to one another. [D7.12]

**USED:** 7.16, 7.17, CN5, D7.12, D7.15
**Human refs (from References field):** 7.17, D7.15
**Jaccard:** 0.400 — AI adds ['7.16', 'CN5', 'D7.12']

## Proposition 7.23
**Statement:** If two number be prime to one another, the number which measures the one of them will be prime to the remaining number.

**Step 1.** Let A and B be prime to one another, and let C measure A. We use the common-measure definition directly: the unit alone measures both A and B. [D7.12]

**Step 2.** Let E be any common measure of C and B. Since C measures A, A consists of a whole number of copies of C. Since E measures C, each such copy consists of a whole number of copies of E. Substituting these copies and collecting them, A also consists of a whole number of copies of E. Thus E measures A as well as B. This is the repeated-addition meaning of measurement and multiplication. [D7.3, D7.15]

**Step 3.** Since A and B are prime to one another, their common measure E must be the unit. Consequently the unit alone is a common measure of C and B; therefore C and B are prime to one another, as required. [D7.12]

**USED:** D7.12, D7.15, D7.3
**Human refs (from References field):** D7.12
**Jaccard:** 0.333 — AI adds ['D7.15', 'D7.3']

## Proposition 7.24
**Statement:** If two numbers be prime to any number, their product also will be prime to the same.

**Step 1.** Let a and b each be prime to c, and let p = ab be the number produced when a multiplies b. We must show that p and c have no common measure greater than a unit. [D7.15, D7.12]

**Step 2.** Suppose, to the contrary, that a number d greater than a unit measures both p and c. Since c and b are prime to one another and d measures c, d and b are prime to one another. We use VII.23 directly here because d is already a measure of c. [7.23]

**Step 3.** Since d measures p, let e be the number of times it measures p; thus e multiplying d produces p, so ed = ab. If e were a unit, then d = p; but b measures p, since p is produced by adding b to itself a times. Then b would be a common measure greater than a unit of b and d, contrary to Step 2. Hence e is a number, not a unit. [D7.15, D7.12]

**Step 4.** From ed = ab, VII.19 gives e:a = b:d. Since b and d are prime to one another, they are the least numbers having their ratio, by VII.21. Therefore, by VII.20, they measure the corresponding numbers e and a; in particular, d measures a. This least-pair route is appropriate because coprimality is already established and the required consequence is divisibility. [7.19, 7.21, 7.20]

**Step 5.** Thus d measures both a and c and is greater than a unit, contradicting the hypothesis that a and c are prime to one another. Consequently p and c have no common measure except a unit. Therefore the product of a and b is prime to c. [D7.12]

**USED:** 7.19, 7.20, 7.21, 7.23, D7.12, D7.15
**Human refs (from References field):** 7.16, 7.19, 7.20, 7.21, 7.23, D7.12, D7.15
**Jaccard:** 0.857 — Human adds ['7.16']

## Proposition 7.25
**Statement:** If two numbers be prime to one another, the product of one of them into itself will be prime to the remaining one.

**Step 1.** Let A and B be prime to one another. Choose the direct specialization of VII.24, which states that the product of two numbers each prime to a given number is also prime to that number. Take both factors to be A and the given number to be B; VII.24 imposes no requirement that the factors be unequal. Each factor is prime to B by hypothesis, so their product A·A is prime to B. Thus the product of one of the original numbers into itself is prime to the remaining one, as required. [7.24]

**USED:** 7.24
**Human refs (from References field):** 7.24
**Jaccard:** 1.000 — Perfect match.

## Proposition 7.26
**Statement:** If two numbers be prime to two numbers, both to each, their products also will be prime to one another.

**Step 1.** Let a and b be the first two numbers, and c and d the second two. Thus each of a and b is prime to each of c and d. Put P = ab and Q = cd. Coprimality is symmetric, since its definition requires that the unit alone be a common measure of the two numbers (D7.12).

**Step 2.** Choose the direct product criterion 7.24, since it applies immediately to two numbers prime to a fixed number. As a and b are both prime to c, their product P is prime to c (7.24).

**Step 3.** Likewise, as a and b are both prime to d, their product P is prime to d (7.24).

**Step 4.** By symmetry, c and d are therefore both prime to P (D7.12). Hence their product Q is prime to P (7.24). Thus P and Q are prime to one another: the products of the given pairs are prime to one another, as required.

**USED:** 7.24, D7.12
**Human refs (from References field):** 7.24
**Jaccard:** 0.500 — AI adds ['D7.12']

## Proposition 7.27
**Statement:** If two numbers be prime to one another, and each by multiplying itself make a certain number, the products will be prime to one another; and, if the original numbers by multiplying the products make certain numbers, the latter will also be prime to one another [and this is always the case with the extremes].

**Step 1.** Let a and b be prime to one another. Put c=a·a and d=b·b, and then e=a·c and f=b·d. We use the direct product rule VII.24: two factors each prime to a fixed number have their product prime to that number. This rule applies at the first multiplication and continues to apply at every subsequent multiplication. [7.24]

**Step 2.** Since a is prime to b, applying VII.24 with both factors equal to a shows that c is prime to b. Hence b is prime to c; applying VII.24 with both factors equal to b shows that d is prime to c. Thus the squares c and d are prime to one another. [7.24]

**Step 3.** Both a and c are prime to b, so their product e is prime to b. Consequently b is prime to e. Applying VII.24 first to the factors b,b shows that d is prime to e, and then applying it to the factors b,d shows that f is prime to e. Thus the cubes e and f are also prime to one another. [7.24]

**Step 4.** The same rule establishes the assertion for every further pair of extremes. For any positive integer n, start with a prime to b and repeatedly multiply by a. At each stage VII.24 preserves primality to b, so aⁿ is prime to b. Now hold aⁿ fixed: b is prime to aⁿ, and repeated multiplication by b preserves primality to aⁿ by VII.24. Hence bⁿ is prime to aⁿ. Therefore the corresponding powers of the original two numbers are prime to one another at every stage, as required. [7.24]

**USED:** 7.24
**Human refs (from References field):** 7.25, 7.26
**Jaccard:** 0.000 — AI adds ['7.24']; Human adds ['7.25', '7.26']

## Proposition 7.28
**Statement:** If two numbers be prime to one another, the sum will also be prime to each of them; and, if the sum of two numbers be prime to any one of them, the original numbers will also be prime to one another.

**Step 1.** Let the two numbers be A and B, and let S = A + B. We take the direct common-measure route: by definition, two numbers are prime to one another precisely when their only common measure is a unit. This criterion applies directly to both assertions. [D7.12]

**Step 2.** Suppose A and B are prime to one another. If a number D measured both S and A, then S and A would each consist of whole copies of D. Subtracting the copies constituting A from those constituting S leaves B consisting of whole copies of D. Thus D would measure both A and B, contrary to their having only a unit as a common measure. Hence S and A are prime to one another. Likewise, if a number D measured both S and B, subtracting B from S would show that D measures A, giving the same contradiction. Therefore S is prime to each of A and B. [D7.5, CN3, D7.12]

**Step 3.** Conversely, suppose S is prime to either A or B, and denote that chosen number by C. If a number D measured both A and B, then adding the whole copies of D constituting A to those constituting B would show that D measures S. Since D also measures C, this contradicts the supposition that S and C have only a unit as a common measure. Thus A and B have no common measure other than a unit and are prime to one another. Both assertions are proved. [D7.5, CN2, D7.12]

**USED:** CN2, CN3, D7.12, D7.5
**Human refs (from References field):** D7.12
**Jaccard:** 0.250 — AI adds ['CN2', 'CN3', 'D7.5']

## Proposition 7.29
**Statement:** Any prime number is prime to any number which it does not measure.

**Step 1.** Let P be a prime number, and let N be a number which P does not measure. We use the defining common-measure criterion directly: it suffices to show that an unit alone is a common measure of P and N. [D7.12]

**Step 2.** Since P is prime, no number smaller than P measures P. Thus any number measuring P must be P itself. A number measuring both P and N would therefore be P, which would make P measure N, contrary to the hypothesis. Hence no number is a common measure of P and N. [D7.11]

**Step 3.** Every number is composed of units, so an unit measures both P and N. By Step 2, it is their only common measure. Therefore P and N are prime to one another: any prime number is prime to any number which it does not measure. [D7.2, D7.12]

**USED:** D7.11, D7.12, D7.2
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['D7.11', 'D7.12', 'D7.2']

## Proposition 7.30
**Statement:** If two numbers by multiplying one another make some number, and any prime number measure the product, it will also measure one of the original numbers.

**Step 1.** Let A multiplied by B produce C, and let the prime number P measure C. If P measures A, the conclusion already holds. Suppose, therefore, that P does not measure A. Then P is prime to A by Proposition 7.29. We take the direct route through the least-ratio property of these relatively prime numbers. [7.29]

**Step 2.** Since A is a multitude of units, C is a proper multiple of B; hence C is not prime. Thus P cannot equal C. Because P measures C, there is consequently a number Q such that Q multiplied by P produces C. Reversing the multiplication gives PQ = C, while by hypothesis AB = C. [D7.2, D7.15, D7.11, 7.16]

**Step 3.** The products PQ and AB are equal. Applying Proposition 7.19 to the four numbers P, A, B, Q therefore gives
P : A = B : Q. [7.19]

**Step 4.** Since P and A are prime to one another, they are the least numbers having their ratio, by Proposition 7.21. Proposition 7.20 now says that they measure the corresponding numbers in any equal ratio. Applied to P : A = B : Q, this shows that P measures B. Thus P either measures A, as in the first case, or measures B, as in the remaining case. Therefore any prime number measuring the product measures one of the original numbers. [7.21, 7.20]

**USED:** 7.16, 7.19, 7.20, 7.21, 7.29, D7.11, D7.15, D7.2
**Human refs (from References field):** 7.19, 7.20, 7.21, 7.29, D7.15
**Jaccard:** 0.625 — AI adds ['7.16', 'D7.11', 'D7.2']

## Proposition 7.31
**Statement:** Any composite number is measured by some prime number.

**Step 1.** Let A be a composite number. It therefore has a proper numerical measure: a number greater than the unit and less than A which measures A (D7.13, D7.3). Choose the least such measure P. This choice is possible because A is a finite multitude of units, so only finitely many numbers are less than A (D7.2). We use this least-measure route because it proceeds directly from the definitions.

**Step 2.** Suppose P were not prime. By the definition of a prime number, P would then have a proper numerical measure Q, greater than the unit and less than P (D7.11, D7.3).

**Step 3.** Since P measures A, A is a sum of equal copies of P; since Q measures P, each such copy is a sum of equal copies of Q (D7.5, D7.15). Substituting these equal sums preserves equality (CN2), so A is a sum of equal copies of Q. Thus Q measures A (D7.5, D7.15). But Q is greater than the unit and less than P, contradicting the choice of P as the least proper numerical measure of A.

**Step 4.** Consequently P has no proper numerical measure and is therefore prime (D7.11). Since P measures A, the arbitrary composite number A is measured by a prime number. Hence any composite number is measured by some prime number.

**USED:** CN2, D7.11, D7.13, D7.15, D7.2, D7.3, D7.5
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['CN2', 'D7.11', 'D7.13', 'D7.15', 'D7.2', 'D7.3', 'D7.5']

## Proposition 7.32
**Statement:** Any number either is prime or is measured by some prime number.

**Step 1.** Let A be any number. If A is measured by a unit alone, then A is prime, and the first alternative holds. [D7.11]

**Step 2.** Otherwise, A is measured by some number and is therefore composite. [D7.11, D7.13]

**Step 3.** Apply VII.31 directly, since it supplies exactly the prime measure required in the composite case: some prime number measures A. Thus any number either is prime or is measured by some prime number. [7.31]

**USED:** 7.31, D7.11, D7.13
**Human refs (from References field):** 7.31
**Jaccard:** 0.333 — AI adds ['D7.11', 'D7.13']

## Proposition 7.33
**Statement:** Given as many numbers as we please, to find the least of those which have the same ratio with them.

**Step 1.** Let the given numbers be A₁, …, Aₙ. We use common-measure reduction, followed by the direct leastness criterion VII.21. Find a greatest common measure d as follows: starting with a smallest given number, test successive smaller multitudes of units, ending with the unit, and take the first that measures every Aᵢ. This is a finite construction; the unit measures every number, and no measure can exceed the number it measures. Thus d exists and is the greatest common measure of all the given numbers. [D7.2, D7.3, CN5]

**Step 2.** For each i, take Bᵢ to be the number of times d measures Aᵢ, so that Aᵢ = dBᵢ, allowing Bᵢ to be the unit. The lists B₁, …, Bₙ and A₁, …, Aₙ have the same corresponding ratios: VII.17 applies because the same multiplier d produces the given terms from the constructed terms. If d is the unit, the lists coincide; ratios involving a unit among the Bᵢ follow directly from the definition of numerical proportion. [D7.15, 7.17, D7.20]

**Step 3.** The Bᵢ have no common measure greater than the unit. For suppose e were such a measure. Each Bᵢ would consist of some number of groups of e units; consequently Aᵢ = dBᵢ would consist of that many groups of de units. Hence de would measure every Aᵢ. But de, containing more than one copy of d, is greater than d, contrary to the choice of d. Therefore the Bᵢ are prime to one another, meaning that the unit alone measures them all. [D7.15, CN5, D7.12]

**Step 4.** By VII.21, numbers prime to one another are the least of those having the same ratios. This is the direct criterion needed here, since Step 3 establishes precisely its hypothesis. If a constructed term Bⱼ is the unit, leastness also follows immediately from the definition: any proportional list C₁, …, Cₙ satisfies Cᵢ = BᵢCⱼ, since Bᵢ is Bᵢ times the unit. Thus each Cᵢ is at least Bᵢ. Accordingly, in every case the constructed B₁, …, Bₙ are the least terms having the same corresponding ratios as the given numbers, as required. [7.21, D7.20, D7.2, D7.15, CN5]

**USED:** 7.17, 7.21, CN5, D7.12, D7.15, D7.2, D7.20, D7.3
**Human refs (from References field):** 7.16, 7.19, 7.21, 7.3, D7.15, D7.20
**Jaccard:** 0.273 — AI adds ['7.17', 'CN5', 'D7.12', 'D7.2', 'D7.3']; Human adds ['7.16', '7.19', '7.3']

## Proposition 7.34
**Statement:** Given two numbers, to find the least number which they measure.

**Step 1.** Let the given numbers be A and B. If either measures the other, take the latter as the answer: both measure it, and every number measured by it consists of one or more copies of it and therefore cannot be smaller. Henceforth suppose that neither A nor B measures the other. [D7.5, D7.15, CN5]

**Step 2.** By 7.33, find the least numbers C and D having the ratio C:D = A:B. We choose this direct route because the least proportional pair supplies both the construction and the means of establishing minimality. [7.33]

**Step 3.** Let D multiply A, producing L; thus L consists of D copies of A. Applying 7.19 to C:D = A:B, the product of C with B equals the product of D with A. Therefore L also consists of C copies of B. Consequently both A and B measure L. [D7.15, 7.19, D7.5]

**Step 4.** Let M be any number measured by both A and B. Let M consist of H copies of A and K copies of B. Neither count can be merely a unit: otherwise M would equal one given number and the other would measure it, contrary to Step 1. Thus H and K are numbers. The product of K with B equals the product of H with A, both being M; hence the converse in 7.19 gives K:H = A:B. [D7.15, 7.19]

**Step 5.** Since C and D are the least numbers in this ratio, and K:H has this same ratio, D cannot exceed H. If D equals H, then L and M consist of the same number of copies of A and are equal. If D is less than H, the D copies forming L constitute a proper part of the H copies forming M, so L is less than M. Thus L is no greater than any number measured by both A and B. Since both measure L, L is the least number which they measure, as required. [7.33, D7.15, CN5]

**USED:** 7.19, 7.33, CN5, D7.15, D7.5
**Human refs (from References field):** 7.16, 7.17, 7.19, 7.20, 7.21, 7.33, D7.15
**Jaccard:** 0.333 — AI adds ['CN5', 'D7.5']; Human adds ['7.16', '7.17', '7.20', '7.21']

## Proposition 7.35
**Statement:** If two numbers measure any number, the least number measured by them will also measure the same.

**Step 1.** Let A and B measure N, and let L be the least number measured by both A and B, whose existence is supplied by VII.34. Since N is itself measured by both, L is not greater than N. We use leastness directly, by repeated subtraction, rather than passing to ratios. [7.34]

**Step 2.** Repeatedly subtract L from N while the remaining quantity is at least L. This process terminates: a number is a finite multitude of units, and each subtraction removes the positive multitude of units composing L. Thus either nothing remains, or a positive remainder R less than L remains. [D7.2]

**Step 3.** At every subtraction, the remainder, if positive, is still measured by both A and B. Indeed, the initial number N consists of whole copies of A, and the quantity L removed consists of whole copies of A; removing those copies leaves whole copies of A. The same reasoning applies to B. Consequently, a positive final remainder R would be a number measured by both A and B and smaller than L, contrary to the choice of L. Hence nothing remains. [D7.15, CN3, 7.34]

**Step 4.** Therefore repeated subtraction of L exhausts N exactly: N consists of whole copies of L. Thus L measures N, as required. [D7.15, D7.5]

**USED:** 7.34, CN3, D7.15, D7.2, D7.5
**Human refs (from References field):** 
**Jaccard:** 0.000 — AI adds ['7.34', 'CN3', 'D7.15', 'D7.2', 'D7.5']

## Proposition 7.36
**Statement:** Given three numbers, to find the least number which they measure.

**Step 1.** Let the three given numbers be A, B, and C. Choose the direct route of applying the two-number construction successively, first to A and B and then to its result and C. By 7.34, find D, the least number which A and B measure. [7.34]

**Step 2.** Again by 7.34, find E, the least number which D and C measure. I say that E is the required number. [7.34]

**Step 3.** Since A and B each measure D, D consists of whole repetitions of A and also of whole repetitions of B. Since D measures E, E consists of whole repetitions of D. Replacing each such repetition of D by its repetitions of A shows that A measures E; doing the same with B shows that B measures E. (If any of these numbers coincide, the corresponding assertion is immediate.) Moreover, C measures E by its construction. Thus all three given numbers measure E. [D7.5, D7.15; 7.34]

**Step 4.** Let N be any number measured by A, B, and C. Since A and B measure N, their least common measured number D also measures N, by 7.35. Hence D and C both measure N. But E was constructed as the least number which D and C measure, so E is no greater than N. Therefore E is the least number which A, B, and C measure, as required. [7.35, 7.34]

**USED:** 7.34, 7.35, D7.15, D7.5
**Human refs (from References field):** 7.34, 7.35
**Jaccard:** 0.500 — AI adds ['D7.15', 'D7.5']

## Proposition 7.37
**Statement:** If a number be measured by any number, the number which is measured will have a part called by the same name as the measuring number.

**Step 1.** Let the number A be measured by the number B. A part called by the same name as B is a Bth part: one of B equal parts composing A. If A = B, then A consists of B units, so a unit is the required Bth part. We may therefore suppose B < A. [D7.2]

**Step 2.** Let C be the number of times B measures A. Thus C copies of B make A; in the language of multiplication, C multiplying B produces A. [D7.15]

**Step 3.** We take the direct route of interchanging the factors. By VII.16, B multiplying C also produces A. Consequently, A consists of as many copies of C as there are units in B. [7.16, D7.15]

**Step 4.** Since B is a number, it contains more than one unit. Hence C is less than A and measures A, so C is a part of A. Moreover, exactly B copies of C compose A; therefore C is the Bth part of A, called by the same name as the measuring number B. Thus the number measured has the required part. [D7.2, D7.3, D7.15]

**USED:** 7.16, D7.15, D7.2, D7.3
**Human refs (from References field):** 7.15
**Jaccard:** 0.000 — AI adds ['7.16', 'D7.15', 'D7.2', 'D7.3']; Human adds ['7.15']

## Proposition 7.38
**Statement:** If a number have any part whatever, it will be measured by a number called by the same name as the part.

**Step 1.** Let A be a number having a part B, and let n be the number called by the same name as that part. Thus, if B is an nth part of A, exactly as many copies of B make A as there are units in n. This expresses the given part as a measure of A. [D7.2, D7.3]

**Step 2.** If B is a unit, A consists of precisely n units, so A equals n. Hence n measures A once, as required. [D7.2]

**Step 3.** Otherwise B is a number. By the definition of multiplication, n multiplying B produces A. We take the direct route through commutativity, since the hypothesis already describes a repeated sum: by VII.16, B multiplying n also produces A. [D7.15, 7.16]

**Step 4.** Consequently A is made up of as many copies of n as there are units in B. Therefore n measures A. Thus a number having any part is measured by the number called by the same name as that part. [D7.15]

**USED:** 7.16, D7.15, D7.2, D7.3
**Human refs (from References field):** 7.15
**Jaccard:** 0.000 — AI adds ['7.16', 'D7.15', 'D7.2', 'D7.3']; Human adds ['7.15']

## Proposition 7.39
**Statement:** To find the number which is the least that will have given parts.

**Step 1.** Let the given parts be named by the numbers a₁, …, aᵣ; thus, for example, a third part is named by three. We use the two-number construction successively, rather than restrict the construction to three numbers, because the given list may have any finite length. Put M₁ = a₁. For each j from 2 through r, construct Mⱼ as the least number measured by both Mⱼ₋₁ and aⱼ, using Proposition 7.34. Let M = Mᵣ. [7.34]

**Step 2.** Every aᵢ measures M. Indeed, a₁ measures M₁; at each subsequent stage, Mⱼ₋₁ and aⱼ measure Mⱼ by construction. Any number measuring Mⱼ₋₁ also measures Mⱼ: repeat its groups in each of the equal copies of Mⱼ₋₁ making up Mⱼ. Consequently all the named numbers measure the final number M. By Proposition 7.37, M therefore has a part called by the name of each aᵢ, and hence has all the given parts. [7.34, 7.37]

**Step 3.** Let N be any number having all the given parts. By Proposition 7.38, every aᵢ measures N. Thus M₁ measures N. If Mⱼ₋₁ measures N, then both Mⱼ₋₁ and aⱼ measure N; Proposition 7.35 says that the least number measured by these two, namely Mⱼ, also measures N. Continuing through the construction, M measures N. Therefore N consists of one or more copies of M and cannot be less than M. Since M itself has all the given parts, it is the least number having them, as required. [7.38, 7.35]

**USED:** 7.34, 7.35, 7.37, 7.38
**Human refs (from References field):** 7.36, 7.37, 7.38
**Jaccard:** 0.400 — AI adds ['7.34', '7.35']; Human adds ['7.36']
