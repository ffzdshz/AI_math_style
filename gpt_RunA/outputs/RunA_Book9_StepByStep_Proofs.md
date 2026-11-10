# Book 9 of Euclid's Elements — Step-by-Step AI Proofs (Run A)

## Proposition 9.1
**Statement:** If two similar plane numbers by multiplying one another make some number, the product will be square.

**Step 1.** Let A and B be the given similar plane numbers, and let P be the number produced by multiplying A by B (D7.15). If A = B, then P is already square, being equal multiplied by equal (D7.18). It therefore remains to consider A ≠ B.

**Step 2.** By 8.18, there is a mean proportional number M between A and B, so that A : M = M : B. This is the direct path: 8.18 applies immediately to the given similarity and supplies a numerical mean without requiring a construction from the sides.

**Step 3.** Apply 7.19 to the four proportional numbers A, M, M, B. The product of the first and fourth equals the product of the second and third. Thus P = A·B = M·M. We use 7.19 because the proportional terms are numbers.

**Step 4.** Therefore P is produced by multiplying the number M by itself, and hence is square by D7.18. Thus the product of two similar plane numbers is square.

**USED:** 7.19, 8.18, D7.15, D7.18
**Human refs (from References field):** 7.17, 8.18, 8.22, 8.8
**Jaccard:** 0.143 — AI adds ['7.19', 'D7.15', 'D7.18']; Human adds ['7.17', '8.22', '8.8']

## Proposition 9.2
**Statement:** If two numbers by multiplying one another make a square number, they are similar plane numbers.

**Step 1.** Let A and B be the two numbers whose product is square. By the definition of a square number, there is a number C such that A multiplied by B equals C multiplied by C. [D7.18]

**Step 2.** Apply 7.19 to the four numbers A, C, C, B. Since the product of the first and fourth equals the product of the second and third, these four numbers are proportional. Thus A : C = C : B, so C is a mean proportional between A and B. [7.19]

**Step 3.** If one mean proportional number falls between two numbers, those numbers are similar plane numbers. Applying this to A, C, B proves that A and B are similar plane numbers, as required. This criterion is the direct path because the side of the given square has supplied precisely the required numerical mean. [8.20]

**USED:** 7.19, 8.20, D7.18
**Human refs (from References field):** 7.17, 8.18, 8.20, 8.8
**Jaccard:** 0.167 — AI adds ['7.19', 'D7.18']; Human adds ['7.17', '8.18', '8.8']

## Proposition 9.3
**Statement:** If a cube number by multiplying itself make some number, the product will be cube.

**Step 1.** Let A be a cube number, and let N = A·A. By the definition of a cube, there is a number a such that, setting b = a·a, we have A = a·b. Our direct path is to show that N is the cube with side b. [D7.15, D7.19]

**Step 2.** Since a multiplying a and b produces b and A respectively, we have a:b = b:A. We use the fixed-multiplier theorem here because the same number a multiplies both numbers being compared. [7.17]

**Step 3.** Form c = b·b. By commutativity, b·a = a·b = A. Thus b multiplying a and b produces A and c respectively, so a:b = A:c. [D7.15, 7.16, 7.17]

**Step 4.** The two preceding proportions give b:A = A:c. Therefore the product of the extremes equals the product of the means: b·c = A·A = N. [CN1, 7.19]

**Step 5.** Since c = b·b and N = b·c = c·b, N is obtained by multiplying b by itself and then multiplying the result by b. Hence N is a cube number, as required. [7.16, D7.19]

**USED:** 7.16, 7.17, 7.19, CN1, D7.15, D7.19
**Human refs (from References field):** 8.23, 8.8, D7.20
**Jaccard:** 0.000 — AI adds ['7.16', '7.17', '7.19', 'CN1', 'D7.15', 'D7.19']; Human adds ['8.23', '8.8', 'D7.20']

## Proposition 9.4
**Statement:** If a cube number by multiplying a cube number make some number, the product will be cube.

**Step 1.** Let A and B be cube numbers, and let C be the product obtained when A multiplies B. Let D be the product obtained when A multiplies itself. Since A is a cube, D is a cube by **9.3**. Our path is to compare C with this known cube D.

**Step 2.** The same number A, multiplying A and B respectively, produces D and C. Therefore the products have the same ratio as the numbers multiplied:
D : C = A : B. (**7.17**)

**Step 3.** Thus D and C have to one another the ratio of the cube A to the cube B. By **8.25**, if two numbers have the ratio of a cube to a cube and the first is a cube, the second is also a cube. This ratio criterion applies directly to the proportion in Step 2. Since D is a cube by Step 1, C is a cube. Therefore a cube number multiplied by a cube number produces a cube.

**USED:** 7.17, 8.25, 9.3
**Human refs (from References field):** 7.17, 8.19, 8.23, 8.8, 9.3
**Jaccard:** 0.333 — AI adds ['8.25']; Human adds ['8.19', '8.23', '8.8']

## Proposition 9.5
**Statement:** If a cube number by multiplying any number make a cube number, the multiplied number will also be cube.

**Step 1.** Let the cube number A multiply the number B to produce the cube number C, so AB=C (D7.15). Let a and c be their respective sides: A=(a·a)·a and C=(c·c)·c (D7.19).

**Step 2.** Since AB=C, A measures C (D7.15). Therefore a measures c, by 8.15. This is the direct path: the hypothesis already supplies measurement between cubes, and 8.15 immediately transfers that measurement to their sides.

**Step 3.** Let d be the number of times a measures c; thus c=ad (D7.15). This measure-count is not merely a unit. For then c=a and consequently C=A, whereas AB=C is greater than A: B is a multitude of units, so AB contains A together with further copies of A (D7.2, D7.15, CN5). Hence d is a number.

**Step 4.** Form D=(d·d)·d, which is a cube number (D7.19). Regrouping multiplication by expanding it as repeated addition (D7.15), and interchanging factors by 7.16, gives
AD=((a·a)·a)((d·d)·d)=((ad)·(ad))·(ad)=(c·c)·c=C.

**Step 5.** Since AB=C and AD=C, AB=AD (CN1). Therefore B=D. Indeed, if either B or D were greater, multiplying it by A would give a greater product: by D7.15 and 7.16, that product would contain all the copies of A in the other product and additional copies, contrary to equality (CN5). Since D is a cube, B is a cube also (D7.19). Thus the multiplied number is cube.

**USED:** 7.16, 8.15, CN1, CN5, D7.15, D7.19, D7.2
**Human refs (from References field):** 7.17, 8.19, 8.23, 8.8, 9.3
**Jaccard:** 0.000 — AI adds ['7.16', '8.15', 'CN1', 'CN5', 'D7.15', 'D7.19', 'D7.2']; Human adds ['7.17', '8.19', '8.23', '8.8', '9.3']

## Proposition 9.6
**Statement:** If a number by multiplying itself make a cube number, it will itself also be cube.

**Step 1.** Let A be the given number, and let B be the number produced by multiplying A by itself, so B = A·A. By hypothesis, B is a cube. [D7.15; hypothesis]

**Step 2.** Let B by multiplying A produce C. Then C = (A·A)·A, so C is contained by three equal numbers A, A, A. Therefore C is a cube. [D7.15; D7.19]

**Step 3.** Thus the cube B, by multiplying A, makes the cube C. Apply 9.5 directly, since both its cube hypotheses have now been established: the multiplied number A is itself a cube, as required. [9.5]

**USED:** 9.5, D7.15, D7.19
**Human refs (from References field):** 8.19, 8.23, 8.8, D7.20
**Jaccard:** 0.000 — AI adds ['9.5', 'D7.15', 'D7.19']; Human adds ['8.19', '8.23', '8.8', 'D7.20']

## Proposition 9.7
**Statement:** If a composite number by multiplying any number make some number, the product will be solid.

**Step 1.** Let the composite number A multiply any number B to produce C. Since A is composite, choose a proper numerical measure D of A. We take the direct definitional route, using this measure to exhibit three numbers producing C. [D7.13]

**Step 2.** Let E be the multitude of times D measures A. Since D is less than A, this multitude contains more than one unit, so E is a number. Thus A consists of D added to itself as many times as there are units in E; that is, E multiplying D produces A. [D7.2, D7.15]

**Step 3.** Therefore E multiplying D produces A, and this resulting number A multiplying B produces C by hypothesis. Hence the three numbers E, D, and B, multiplied successively, produce C. By the definition of a solid number, C is solid, as required. [D7.17]

**USED:** D7.13, D7.15, D7.17, D7.2
**Human refs (from References field):** D7.13, D7.15
**Jaccard:** 0.500 — AI adds ['D7.17', 'D7.2']

## Proposition 9.8
**Statement:** If as many numbers as we please beginning from an unit be in continued proportion, the third from the unit will be square, as will also those which successively leave out one; the fourth will be cube, as will also all those which leave out two; and the seventh will be at once cube and square, as will also those which leave out five.

**Step 1.** Let the given progression be u₀, u₁, …, u_N, where u₀ = 1 is the unit, and put a = u₁. Count the unit as the first term. By hypothesis, u_j : u_{j+1} = 1 : a. Since a consists of units, u_{j+1} therefore consists of as many copies of u_j as there are units in a. Consequently, for every j ≥ 1 for which the next term occurs,
u_{j+1} = a·u_j.
Here x·y denotes the product obtained when x multiplies y. [D7.1, D7.2, D7.20, D7.15]

**Step 2.** Path choice: use 7.18, since we shall keep the multiplied number fixed while the multipliers run through the progression. Fix positive indices r and s with r+s ≤ N, and form P_j = u_j·u_r for j = 1, …, s. For each adjacent pair, multiplication of the same number u_r gives
P_j : P_{j+1} = u_j : u_{j+1}.
Thus P_{j+1}, like u_{j+1} relative to u_j, consists of as many copies of P_j as there are units in a; that is, P_{j+1} = a·P_j. [7.18, D7.20, D7.15]

**Step 3.** The first product is P₁ = a·u_r = u_{r+1}, by Step 1. Whenever P_j = u_{r+j}, adding the same number of copies of these equal numbers gives P_{j+1} = u_{r+j+1}, by Steps 1–2 and CN2. Repeating this along the finite sequence proves P_s = u_{r+s}. Hence, whenever r and s are positive and the indicated term occurs,
u_{r+s} = u_s·u_r. [D7.15, CN2]

**Step 4.** Taking s = r in Step 3 gives u_{2r} = u_r·u_r. Therefore every such u_{2r} is square, being equal multiplied by equal. Its position, counting the unit first, is 2r+1. These are precisely the third, fifth, seventh, and successive terms obtained by leaving out one term each time. [Step 3; D7.18]

**Step 5.** Taking s = 2r in Step 3 gives u_{3r} = u_{2r}·u_r. By Step 4, u_{2r} = u_r·u_r; hence
u_{3r} = (u_r·u_r)·u_r.
Thus u_{3r} is cube, being equal multiplied by equal and again by equal. Its position is 3r+1: the fourth, seventh, tenth, and successive terms obtained by leaving out two terms each time. [Steps 3–4; D7.19]

**Step 6.** Whenever u_{6r} occurs, Step 4 applied with index 3r shows that it is square, while Step 5 applied with index 2r shows that it is cube. Its position is 6r+1: the seventh, thirteenth, nineteenth, and successive terms obtained by leaving out five terms each time. Thus all three assertions hold throughout the given progression. [Steps 4–5; D7.18, D7.19]

**USED:** 7.18, CN2, D7.1, D7.15, D7.18, D7.19, D7.2, D7.20
**Human refs (from References field):** 8.22, 8.23, D7.20
**Jaccard:** 0.100 — AI adds ['7.18', 'CN2', 'D7.1', 'D7.15', 'D7.18', 'D7.19', 'D7.2']; Human adds ['8.22', '8.23']

## Proposition 9.9
**Statement:** If as many numbers as we please beginning from an unit be in continued proportion, and the number after the unit be square, all the rest will also be square.

**Step 1.** Let u, A_1, A_2, …, A_n be in continued proportion, where u is the unit and A_1 is square. Thus, for each i with 1 ≤ i < n, u : A_1 = A_i : A_{i+1}. [Hypothesis; D7.20]

**Step 2.** The unit measures A_1 as many times as there are units in A_1. By the proportion in Step 1, A_i measures A_{i+1} the same number of times. Hence A_{i+1} consists of A_i added to itself as many times as there are units in A_1: it is precisely the number produced when A_1 multiplies A_i. [D7.2, D7.20, D7.15]

**Step 3.** Suppose A_i is square. Since A_1 is also square, there are numbers r and s such that A_1 is produced by r multiplying r, and A_i by s multiplying s. These are plane numbers with sides r, r and s, s respectively. Since r : r = s : s, their sides are proportional; therefore A_1 and A_i are similar plane numbers. [D7.18, D7.16, D7.20, D7.21]

**Step 4.** Apply 9.1: two similar plane numbers, by multiplying one another, produce a square. Therefore the product of A_1 and A_i, which is A_{i+1} by Step 2, is square. This is the direct path: the similar-plane representation of the two squares makes the product criterion immediately applicable. [9.1; Steps 2–3]

**Step 5.** Starting with the given square A_1, Step 4 proves successively that A_2 is square, then A_3, and so on through A_n. Thus all the remaining numbers in the continued proportion are square, as required. [Hypothesis; Steps 3–4]

**USED:** 9.1, D7.15, D7.16, D7.18, D7.2, D7.20, D7.21
**Human refs (from References field):** 8.22, 8.23, 9.3, 9.8
**Jaccard:** 0.000 — AI adds ['9.1', 'D7.15', 'D7.16', 'D7.18', 'D7.2', 'D7.20', 'D7.21']; Human adds ['8.22', '8.23', '9.3', '9.8']

## Proposition 9.10
**Statement:** If as many numbers as we please beginning from an unit be in continued proportion, and the number after the unit be not square, neither will any other be square except the third from the unit and all those which leave out one.

**Step 1.** Write the given progression as u, A₁, A₂, …, Aₘ, where u is the unit and A₁ is not square. Its consecutive ratios are equal by hypothesis (D7.20). Counting the unit as the first term, the third term and those which successively leave out one are A₂, A₄, A₆, … .

**Step 2.** By 9.8, every such term A₂, A₄, A₆, … that occurs in the progression is square. It therefore remains to exclude squares among the odd-indexed terms.

**Step 3.** Suppose, for a contradiction, that some later odd-indexed term A₂ₖ₊₁ is square, where k ≥ 1. Consider the two lists
A₁, A₂, …, Aₖ₊₁
and
Aₖ₊₁, Aₖ₊₂, …, A₂ₖ₊₁.
They contain equally many terms, and corresponding consecutive ratios are equal. Hence, by 7.14,
A₁ : Aₖ₊₁ = Aₖ₊₁ : A₂ₖ₊₁.

**Step 4.** Inverting this proportion gives
A₂ₖ₊₁ : Aₖ₊₁ = Aₖ₊₁ : A₁
(D7.20). Thus these three numbers, in reverse order, are in continued proportion. The direct three-term route is appropriate here: 8.22 states that if three numbers are in continued proportion and the first is square, the third is also square. Since A₂ₖ₊₁ was supposed square, 8.22 makes A₁ square, contrary to the hypothesis.

**Step 5.** Consequently no later odd-indexed term is square, and A₁ itself is not square by hypothesis. Together with Step 2, this proves that the only square numbers in the progression are the third term from the unit and all those which successively leave out one, as required.

**USED:** 7.14, 8.22, 9.8, D7.20
**Human refs (from References field):** 8.25, 8.26, 9.6, 9.8
**Jaccard:** 0.143 — AI adds ['7.14', '8.22', 'D7.20']; Human adds ['8.25', '8.26', '9.6']

## Proposition 9.11
**Statement:** If as many numbers as we please beginning from an unit be in continued proportion, the less measures the greater according to some one of the numbers which have place among the proportional numbers.

**Step 1.** Let a₀, a₁, …, aₙ be the given continued proportion, where a₀ is the unit. Thus a₀:a₁ = aₖ:aₖ₊₁ for every k < n. Since a₁ contains more than one unit, each aₖ₊₁ consists of as many copies of aₖ as a₁ contains units (D7.1, D7.2, D7.20). Consequently aₖ₊₁ > aₖ, so the terms increase in their given order (CN5).

**Step 2.** Choose any less term aᵢ and greater term aⱼ. By Step 1, i < j. Put d = j − i, and consider the two chains
(a₀, a₁, …, a_d) and (aᵢ, aᵢ₊₁, …, aⱼ).
They contain equally many terms, and every consecutive ratio in either chain equals the common ratio of the given continued proportion (hypothesis; D7.20).

**Step 3.** The direct path is numerical ex aequali: it applies immediately to these equal-length chains with matching consecutive ratios. Hence their extreme terms are proportional:
a₀:a_d = aᵢ:aⱼ (7.14).

**Step 4.** The unit a₀ measures a_d as many times as there are units in a_d (D7.1, D7.2). By the proportion in Step 3, aᵢ is the same part of aⱼ that a₀ is of a_d (D7.20). Therefore aᵢ measures aⱼ that same number of times—that is, according to a_d (D7.3). Since 1 ≤ d ≤ n, a_d is one of the numbers in the given continued proportion. Thus the less measures the greater according to some one of the numbers having place among the proportional numbers.

**USED:** 7.14, CN5, D7.1, D7.2, D7.20, D7.3
**Human refs (from References field):** 7.15
**Jaccard:** 0.000 — AI adds ['7.14', 'CN5', 'D7.1', 'D7.2', 'D7.20', 'D7.3']; Human adds ['7.15']

## Proposition 9.12
**Statement:** If as many numbers as we please beginning from an unit be in continued proportion, by however many prime numbers the last is measured, the next to the unit will also be measured by the same.

**Step 1.** Let u, a₁, a₂, …, aₙ be the given finite sequence beginning with the unit u and continuing in proportion. Let p be any prime number measuring aₙ. We must show that p measures a₁. If n = 1, this is already the hypothesis; therefore suppose n ≥ 2. [Hypothesis]

**Step 2.** For each j from 2 through n, continued proportion gives u : a₁ = aⱼ₋₁ : aⱼ. The unit measures a₁ as many times as there are units in a₁; hence aⱼ₋₁ measures aⱼ that same number of times. Thus a₁ multiplied by aⱼ₋₁ produces aⱼ:
 aⱼ = a₁ · aⱼ₋₁. [D7.2, D7.20, D7.15]

**Step 3.** The direct path is to apply the prime-divisor-of-a-product proposition, since Step 2 supplies exactly such products. Whenever p measures aⱼ with j ≥ 2, it measures at least one of the factors a₁ and aⱼ₋₁. [7.30; Step 2]

**Step 4.** Begin with p measuring aₙ. By Step 3, either p measures a₁, as required, or it measures aₙ₋₁. In the latter case apply Step 3 again, continuing backwards through the finite sequence unless p has already been shown to measure a₁. If a₂ is reached, then a₂ = a₁ · a₁, so p necessarily measures a₁. Thus every prime number measuring the last term also measures the term next to the unit. Consequently, by however many prime numbers the last is measured, the next to the unit is measured by those same primes. [7.30; Steps 1–3]

**USED:** 7.30, D7.15, D7.2, D7.20
**Human refs (from References field):** 7.19, 7.20, 7.21, 7.29, 9.11, 9.8, D7.14
**Jaccard:** 0.000 — AI adds ['7.30', 'D7.15', 'D7.2', 'D7.20']; Human adds ['7.19', '7.20', '7.21', '7.29', '9.11', '9.8', 'D7.14']

## Proposition 9.13
**Statement:** If as many numbers as we please beginning from an unit be in continued proportion, and the number after the unit be prime, the greatest will not be measured by any except those which have a place among the proportional numbers.

**Step 1.** Let the given continued proportion be
\[a_0=1,\quad a_1=p,\quad a_2,\ldots,a_n,\]
where 1 is the unit and p is prime. Since \(1:p=a_i:a_{i+1}\), each \(a_{i+1}\) consists of p copies of \(a_i\). Because p is a number, it exceeds the unit; consequently the terms increase strictly, and \(a_n\) is the greatest. [D7.1, D7.2, D7.20, D7.15, CN5]

**Step 2.** Suppose that a number d measures \(a_n\) but equals none of the listed terms. Then \(d<a_n\). Among the listed terms that measure d, choose the one with greatest index, say \(a_k\). Such a term exists because the unit measures every number. Since d is not a listed term, \(a_k<d<a_n\); hence \(k<n\), and \(a_{k+1}\) exists. Our path is to show that this next term also measures d, contradicting the choice of k. [D7.2, D7.3, CN5]

**Step 3.** Let q be the number of times \(a_k\) measures d, so that d consists of q copies of \(a_k\). Since \(a_k<d\), q exceeds the unit. Moreover, q measures d: if \(a_k\) is the unit, then \(q=d\); otherwise, interchange the factors by 7.16, so that d also consists of \(a_k\) copies of q. [D7.1, D7.2, D7.15, 7.16]

**Step 4.** By 7.32, q either is prime or has a prime measure; thus choose a prime r equal to q or measuring q. This proposition is appropriate because q has not been assumed composite. Since q measures d and d measures \(a_n\), r measures \(a_n\): replacing each successive measure by its constituent copies gives copies of r. By 9.12, r therefore measures the term p immediately after the unit. Since p is prime and r is a number, \(r=p\). Consequently q either equals p or is measured by p. [7.32, D7.15, 9.12, D7.11]

**Step 5.** Group the q copies of \(a_k\) constituting d into groups of p copies. This is possible by Step 4. Each group equals \(a_{k+1}\), by Step 1, so \(a_{k+1}\) measures d. This contradicts the maximal choice of k in Step 2. Hence no number outside the given progression measures \(a_n\). The unit is already its first term, so the greatest is measured only by terms having a place in the given continued proportion. [D7.15; Steps 1–4]

**USED:** 7.16, 7.32, 9.12, CN5, D7.1, D7.11, D7.15, D7.2, D7.20, D7.3
**Human refs (from References field):** 7.19, 7.31, 9.11, 9.12, 9.8
**Jaccard:** 0.071 — AI adds ['7.16', '7.32', 'CN5', 'D7.1', 'D7.11', 'D7.15', 'D7.2', 'D7.20', 'D7.3']; Human adds ['7.19', '7.31', '9.11', '9.8']

## Proposition 9.14
**Statement:** If a number be the least that is measured by prime numbers, it will not be measured by any other prime number except those originally measuring it.

**Step 1.** Let N be the least number measured by the given prime numbers p₁, …, pᵣ. Suppose, for contradiction, that another prime q measures N, with q different from every pᵢ. [Hypothesis; D7.11.]

**Step 2.** None of the pᵢ measures q, since q is prime and each pᵢ is a number different from q. Consequently N cannot equal q, because every pᵢ measures N. [D7.11; Step 1.]

**Step 3.** Since q measures N, let M be the number of times it measures N. Thus M multiplying q produces N. Because N is not q, M is a number rather than the unit. Moreover, taking one unit from each of these M copies of q gives M units and leaves units over, since q is itself a number. Hence M is less than N. [D7.5; D7.15; D7.2; CN5; Step 2.]

**Step 4.** Take any of the given primes pᵢ. It measures N, the product of M and q; therefore it measures M or q, by 7.30. It does not measure q by Step 2, so it measures M. Thus every given prime measures M. The direct path is to use 7.30 here, because the required product is already supplied by the supposed extra prime divisor. [7.30; Steps 1–3.]

**Step 5.** Therefore M is a number less than N measured by all the given primes, contradicting the hypothesis that N is the least such number. Hence no prime other than the originally given primes measures N. [Steps 3–4; leastness hypothesis.]

**USED:** 7.30, CN5, D7.11, D7.15, D7.2, D7.5
**Human refs (from References field):** 7.30
**Jaccard:** 0.167 — AI adds ['CN5', 'D7.11', 'D7.15', 'D7.2', 'D7.5']

## Proposition 9.15
**Statement:** If three numbers in continued proportion be the least of those which have the same ratio with them, any two whatever added together will be prime to the remaining number.

**Step 1.** Let A, B, C be the given numbers, least among those having their ratio, with A:B = B:C. By 8.3, A and C are prime to one another. By 7.19, AC = B², where B² denotes B multiplied by itself. **Path choice:** 8.3 applies immediately to the leastness hypothesis; the product identity then permits a direct argument using prime measures.

**Step 2.** If two numbers are not prime to one another, they have a common numerical measure d (D7.12). By 7.32, d either is prime or is measured by a prime; consequently, the two numbers have a prime common measure p (D7.5, D7.15). We use 7.32 because d is arbitrary, not assumed composite. We shall also use these elementary consequences of measurement: a measure of either factor measures their product (D7.15, 7.16), and a common measure of a whole and a part measures the remainder, since removing whole copies of the measure leaves whole copies (D7.5, CN3).

**Step 3.** Suppose A+B and C are not prime to one another. By Step 2, some prime p measures both. Since p measures C, it measures AC, hence B² by Step 1 (D7.15, 7.16). Therefore p measures B, by 7.30 applied to B multiplied by itself. Since p measures A+B and B, it also measures A (D7.5, CN3). Thus p measures both A and C, contradicting their being prime to one another (Step 1; D7.12). Hence A+B is prime to C.

**Step 4.** Suppose B+C and A are not prime to one another. By Step 2, some prime p measures both. Since p measures A, it measures AC = B² (D7.15, 7.16; Step 1). By 7.30, p therefore measures B. Subtracting B from B+C shows that p also measures C (D7.5, CN3). Again p measures both A and C, contradicting Step 1 and D7.12. Hence B+C is prime to A.

**Step 5.** Suppose A+C and B are not prime to one another. By Step 2, some prime p measures both. Since p measures B, it measures B² = AC (D7.15; Step 1). By 7.30, p measures A or C. If it measures A, subtracting A from A+C shows that it measures C; if it measures C, subtracting C shows that it measures A (D7.5, CN3). Either way, p measures both extremes, contradicting Step 1 and D7.12. Hence A+C is prime to B.

**Step 6.** Steps 3–5 establish all three possible choices. Therefore any two of the given numbers added together are prime to the remaining number, as required.

**USED:** 7.16, 7.19, 7.30, 7.32, 8.3, CN3, D7.12, D7.15, D7.5
**Human refs (from References field):** 2.3, 2.4, 7.22, 7.24, 7.25, 7.28, 8.2
**Jaccard:** 0.000 — AI adds ['7.16', '7.19', '7.30', '7.32', '8.3', 'CN3', 'D7.12', 'D7.15', 'D7.5']; Human adds ['2.3', '2.4', '7.22', '7.24', '7.25', '7.28', '8.2']

## Proposition 9.16
**Statement:** If two numbers be prime to one another, the second will not be to any other number as the first is to the second.

**Step 1.** Let A and B be numbers prime to one another. Thus their only common measure is an unit [D7.12]. Suppose, for a contradiction, that there is a number C such that A:B = B:C.

**Step 2.** Since A and B are prime to one another, they are the least numbers having their ratio [7.21]. We choose the least-terms route because 7.21 applies directly to the given coprimality.

**Step 3.** The least numbers having a given ratio measure the corresponding numbers of any pair having that ratio [7.20]. Applying this to A:B = B:C, we obtain that A measures B.

**Step 4.** Since A also measures itself once, A is a common measure of A and B. But A is a number, a multitude of units, and not an unit [D7.1, D7.2]. This contradicts their being prime to one another [D7.12]. Therefore no number C can satisfy B:C = A:B: the second cannot be to any other number as the first is to the second.

**USED:** 7.20, 7.21, D7.1, D7.12, D7.2
**Human refs (from References field):** 7.20, 7.21
**Jaccard:** 0.400 — AI adds ['D7.1', 'D7.12', 'D7.2']

## Proposition 9.17
**Statement:** If there be as many numbers as we please in continued proportion, and the extremes of them be prime to one another, the last will not be to any other number as the first to the second.

**Step 1.** Let A_1, A_2, …, A_n be numbers in continued proportion, with A_1 and A_n prime to one another. Suppose, for a contradiction, that there is a number B such that A_n : B = A_1 : A_2. Then A_1, A_2, …, A_n, B are in continued proportion, since the appended ratio equals their common ratio (hypothesis; D7.20).

**Step 2.** Path choice: apply the numerical ex aequali theorem to the original sequence and its one-place shift; this directly brings the given coprime extremes into a proportion. The two sequences
A_1, A_2, …, A_n
and
A_2, A_3, …, A_n, B
have corresponding successive ratios equal. Therefore, ex aequali,
A_1 : A_n = A_2 : B (7.14).

**Step 3.** Since A_1 and A_n are prime to one another, they are the least numbers having their ratio (7.21). The least numbers having a given ratio measure the corresponding numbers of any pair having that ratio (7.20). Applying this to the proportion in Step 2, we conclude that A_1 measures A_2.

**Step 4.** Because all successive ratios in the original sequence are equal, each succeeding term consists of the same whole number of copies of its predecessor as A_2 does of A_1 (D7.20). Thus A_2 consists of copies of A_1, A_3 consists of copies of A_2, and so on. Repeatedly substituting these decompositions expresses A_n as a whole number of copies of A_1; hence A_1 measures A_n (D7.15).

**Step 5.** Consequently, A_1 itself measures both A_1 and A_n. Since A_1 is a number, and therefore a multitude of units rather than an unit, this contradicts the hypothesis that their only common measure is an unit (D7.2; D7.12). Therefore no number B can satisfy A_n : B = A_1 : A_2: the last is not to any other number as the first is to the second.

**USED:** 7.14, 7.20, 7.21, D7.12, D7.15, D7.2, D7.20
**Human refs (from References field):** 7.13, 7.20, 7.21
**Jaccard:** 0.250 — AI adds ['7.14', 'D7.12', 'D7.15', 'D7.2', 'D7.20']; Human adds ['7.13']

## Proposition 9.18
**Statement:** Given two numbers, to investigate whether it is possible to find a third proportional to them.

**Step 1.** Let the given numbers, in their assigned order, be A and B. Form S = B·B by repeated addition [D7.15, D7.18]. By 7.19, a number C satisfies A:B = B:C if and only if A·C = S. **Path choice:** use this product criterion directly, rather than first reducing the ratio to least terms, because it immediately supplies a measurement test [7.19].

**Step 2.** Starting with S, repeatedly subtract A while possible, counting the copies removed. Stop when nothing remains or when the remainder is smaller than A. This process terminates: S consists of finitely many units, and each subtraction removes units and leaves a strictly smaller remainder [D7.2, CN5].

**Step 3.** Suppose S is exhausted after at least two copies of A have been removed. Let C be the number containing as many units as there were copies removed [D7.2]. Then A·C = S by the definition of multiplication [D7.15]. Since S = B·B, proposition 7.19 gives A:B = B:C. Thus C is the required third proportional [7.19].

**Step 4.** Suppose instead that a nonempty remainder is left, or that S is exhausted after only one copy of A. If a third proportional number C existed, 7.19 would give S = A·C. By the definition of multiplication, S would therefore consist of exactly as many copies of A as there are units in C [D7.15]. Since C is a number, not merely a unit, the subtraction would exhaust S after at least two copies, contrary to the outcome of the test [D7.1, D7.2]. Hence no third proportional number exists in these cases. Consequently, a third proportional exists exactly when B·B consists of whole copies of A whose count is a number rather than a single unit; the finite test above both decides the question and constructs the third proportional whenever possible [7.19, D7.15].

**USED:** 7.19, CN5, D7.1, D7.15, D7.18, D7.2
**Human refs (from References field):** 7.19, 9.16
**Jaccard:** 0.143 — AI adds ['CN5', 'D7.1', 'D7.15', 'D7.18', 'D7.2']; Human adds ['9.16']

## Proposition 9.19
**Statement:** Given three numbers, to investigate when it is possible to find a fourth proportional to them.

**Step 1.** Let the three given numbers, in their prescribed order, be A, B, C. We seek a number X such that A:B = C:X (D7.20). **Path choice:** use 7.19 directly, since it characterizes this four-term proportion by equality of products and avoids first reducing A:B to least terms.

**Step 2.** Form the product P = BC (D7.15). From P repeatedly subtract A whenever the remainder contains at least A units, recording one unit for each subtraction. This process terminates: P consists of finitely many units, and each subtraction removes a positive multitude of them (D7.1, D7.2). Thus we can determine whether the subtraction exhausts P exactly and, if so, how many copies of A it contained.

**Step 3.** Suppose the process exhausts P exactly and the recorded units constitute a number X. Then X copies of A make P, so XA = P by D7.15. By 7.16, AX = XA; hence AX = BC (CN1). Therefore A:B = C:X by the converse direction of 7.19. The required fourth proportional has been constructed.

**Step 4.** Conversely, suppose a fourth proportional number Y exists, so that A:B = C:Y. By 7.19, AY = BC = P; and by 7.16, YA = P. Consequently P consists of exactly Y copies of A (D7.15). The procedure in Step 2 must therefore exhaust P exactly, recording the number Y. Thus, if that procedure leaves a remainder, or does not record a number of copies, no fourth proportional number exists.

**Step 5.** The investigation is therefore complete: multiply the second given number by the third, and test by repeated subtraction whether the product contains the first an exact number of times. If it does, that number of times is the fourth proportional; otherwise none exists, by Steps 3–4 and 7.19. In particular, if BC = A, the procedure records only an unit, not a number in Euclid’s terminology, so this boundary case supplies an unit rather than a fourth proportional number (D7.1, D7.2).

**USED:** 7.16, 7.19, CN1, D7.1, D7.15, D7.2, D7.20
**Human refs (from References field):** 7.14, 7.19, 7.20, 7.21, 9.17
**Jaccard:** 0.091 — AI adds ['7.16', 'CN1', 'D7.1', 'D7.15', 'D7.2', 'D7.20']; Human adds ['7.14', '7.20', '7.21', '9.17']

## Proposition 9.20
**Statement:** Prime numbers are more than any assigned multitude of prime numbers.

**Step 1.** Let p₁, …, pᵣ be any assigned finite collection of distinct prime numbers. Construct a common multiple M as follows: begin with p₁, and successively take the least common multiple of the current number and the next assigned prime by 7.34. Every earlier prime continues to measure the resulting number, since repeating a sum of copies of that prime again gives a sum of copies of it [D7.15]. Thus every pᵢ measures M. If only one prime is assigned, take M = p₁. Construction choice: only the common-multiple property is needed; leastness is not used.

**Step 2.** Let u be a unit and form N = M + u, which is a number [D7.1, D7.2]. Since each pᵢ measures M, each is at most M; and N is greater than M. Consequently N is greater than every assigned prime [D7.5, CN5].

**Step 3.** By 7.32, N either is prime or is measured by some prime number. This unconditional alternative is the direct choice because the primality of N has not been determined. If N is prime, Step 2 already gives a prime different from all the assigned primes. In the other case, let q be a prime measuring N [7.32].

**Step 4.** Suppose that q were one of the assigned primes. Then q would measure M by Step 1, as well as N by Step 3. Express M and N as sums of copies of q. Since N > M, cancelling from the latter sum the copies that make M leaves a positive number of copies of q equal to N − M = u [D7.15, CN3].

**Step 5.** But q, being a number, is a multitude of units and is therefore greater than a single unit [D7.1, D7.2, CN5]. A positive sum of copies of q cannot equal u: one copy already exceeds u, and further copies only increase the whole [CN5]. Thus the supposition in Step 4 is impossible, and q is different from every assigned prime.

**Step 6.** In either alternative of Step 3, a prime has been found outside the assigned collection. Adjoining it produces a collection of prime numbers greater in multitude than the assigned collection, which is a proper part of the enlarged collection [Steps 3–5, CN5]. Since the assigned collection was arbitrary, prime numbers are more than any assigned multitude of prime numbers.

**USED:** 7.32, 7.34, CN3, CN5, D7.1, D7.15, D7.2, D7.5
**Human refs (from References field):** 7.31
**Jaccard:** 0.000 — AI adds ['7.32', '7.34', 'CN3', 'CN5', 'D7.1', 'D7.15', 'D7.2', 'D7.5']; Human adds ['7.31']

## Proposition 9.21
**Statement:** If as many even numbers as we please be added together, the whole is even.

**Step 1.** We proceed directly from the definition of evenness, which supplies the required equal parts. Let A₁, …, Aₙ be any finite collection of even numbers. Divide each Aᵢ into two parts Bᵢ and Cᵢ such that Bᵢ = Cᵢ. [D7.6]

**Step 2.** Collect all the parts Bᵢ into one total B, and all the corresponding parts Cᵢ into another total C. Since each Bᵢ equals its corresponding Cᵢ, successive addition of equals to equals gives B = C. [CN2]

**Step 3.** These two totals together contain exactly the two parts of every original summand, so they constitute the whole A₁ + ⋯ + Aₙ. By Steps 1–2, the whole is therefore divided into two equal parts, B and C. Hence the whole is even. [D7.6]

**USED:** CN2, D7.6
**Human refs (from References field):** D7.6
**Jaccard:** 0.500 — AI adds ['CN2']

## Proposition 9.22
**Statement:** If as many odd numbers as we please be added together, and their multitude be even, the whole will be even.

**Step 1.** Let the given odd numbers be a₁, …, aₙ, where their multitude n is even. Remove one unit from each, leaving even numbers e₁, …, eₙ (D7.7). This unit-removal route is chosen because it makes the even-sum theorem 9.21 directly applicable.

**Step 2.** Let E be the sum of e₁, …, eₙ. Since all these remainders are even, E is even (9.21).

**Step 3.** Let U be the sum of the removed units. Exactly one unit was removed from each of the n given numbers, so U is the number n, a multitude of n units (D7.2). Thus U is even by the hypothesis on the multitude.

**Step 4.** Adding the equalities aᵢ = eᵢ + one unit, the original whole equals E + U (CN2). Both E and U are even, so their sum is even (9.21). Therefore the whole of the given odd numbers is even.

**USED:** 9.21, CN2, D7.2, D7.7
**Human refs (from References field):** 9.21, D7.7
**Jaccard:** 0.500 — AI adds ['CN2', 'D7.2']

## Proposition 9.23
**Statement:** If as many odd numbers as we please be added together, and their multitude be odd, the whole will also be odd.

**Step 1.** Let an odd multitude of odd numbers be given. If there is only one summand, their sum is odd by hypothesis. Otherwise, set aside one summand A. Since the original multitude is odd, the remaining multitude is even. [D7.7]

**Step 2.** Let E be the sum of the remaining summands. These are odd numbers in an even multitude; therefore E is even. We use 9.22 first because setting aside one summand gives exactly its hypothesis. [9.22]

**Step 3.** Remove one unit from A, and call the remainder B. Since A is odd, B is even, and A = B + 1. [D7.7]

**Step 4.** Since E and B are both even, E + B is even. Adding E to the equality A = B + 1 shows that the sum S of all the given numbers satisfies S = E + A = (E + B) + 1. [9.21; CN2]

**Step 5.** Thus S exceeds the even number E + B by one unit, so S is odd. Therefore, if an odd multitude of odd numbers is added together, the whole is odd. [D7.7]

**USED:** 9.21, 9.22, CN2, D7.7
**Human refs (from References field):** 9.21, 9.22, D7.7
**Jaccard:** 0.750 — AI adds ['CN2']

## Proposition 9.24
**Statement:** If from an even number an even number be subtracted, the remainder will be even.

**Step 1.** Let A be an even number, B a smaller even number, and R the remainder after subtracting B from A. We use the defining division into equal parts directly: write A = A₁ + A₂ and B = B₁ + B₂, where A₁ = A₂ and B₁ = B₂. (D7.6)

**Step 2.** Each half of A is greater than the corresponding half of B. For if the halves were equal, their sums would be equal; and if the halves of B were greater, B would contain two parts together equal to A and something more, so B would be greater than A. Both alternatives contradict A > B. (CN2, CN5)

**Step 3.** Subtract B₁ from A₁ and B₂ from A₂, calling the remainders C₁ and C₂. Since A₁ = A₂ and B₁ = B₂, the remainders are equal: C₁ = C₂. (CN3)

**Step 4.** Combining A₁ = B₁ + C₁ and A₂ = B₂ + C₂ gives A = B + (C₁ + C₂). Subtracting B therefore gives R = C₁ + C₂. (CN2, CN3)

**Step 5.** Thus R is divided into the two equal parts C₁ and C₂. Therefore R is even: subtracting an even number from an even number leaves an even remainder. (D7.6)

**USED:** CN2, CN3, CN5, D7.6
**Human refs (from References field):** D7.6
**Jaccard:** 0.250 — AI adds ['CN2', 'CN3', 'CN5']

## Proposition 9.25
**Statement:** If from an even number an odd number be subtracted, the remainder will be odd.

**Step 1.** Let A be an even number, B an odd number subtracted from A, and R the remainder, so A = B + R. Thus A is divisible into two equal parts, whereas B is not (D7.6, D7.7).

**Step 2.** Suppose, for contradiction, that R is even. Choose the subtraction route, since 9.24 applies directly to the even whole A and the supposed even remainder R. By 9.24, subtracting R from A leaves an even number. But subtracting R from both sides of A = B + R gives A − R = B (CN3). Therefore B is even.

**Step 3.** This contradicts B being odd: an even number is divisible into two equal parts, while an odd number is not (D7.6, D7.7). Hence R is not even, and therefore is not divisible into two equal parts (D7.6). Consequently R is odd (D7.7), as required.

**USED:** 9.24, CN3, D7.6, D7.7
**Human refs (from References field):** 9.24, D7.7
**Jaccard:** 0.500 — AI adds ['CN3', 'D7.6']

## Proposition 9.26
**Statement:** If from an odd number an odd number be subtracted, the remainder will be even.

**Step 1.** Let A and B be odd numbers, with B smaller than A, and let R be the remainder after B is subtracted from A. Thus A = B + R. Since A is odd, it is not divisible into two equal parts. [Hypothesis; D7.7]

**Step 2.** Suppose R were not even. Then R would be odd, since being even means being divisible into two equal parts, and being odd means not being so divisible. [D7.6; D7.7]

**Step 3.** Use the two-term case of 9.22: this is the natural sum theorem because adding B back to R recovers A. The numbers B and R are both odd, and their multitude, two, is even, being divisible into two equal units. Therefore B + R, which is A, would be even. [D7.6; 9.22]

**Step 4.** This contradicts Step 1: A cannot both be divisible and not be divisible into two equal parts. Hence the supposition that R is not even is false. Therefore the remainder after an odd number is subtracted from an odd number is even. [D7.6; D7.7]

**USED:** 9.22, D7.6, D7.7
**Human refs (from References field):** 9.24, D7.7
**Jaccard:** 0.250 — AI adds ['9.22', 'D7.6']; Human adds ['9.24']

## Proposition 9.27
**Statement:** If from an odd number an even number be subtracted, the remainder will be odd.

**Step 1.** Let A be the given odd number, B the even number subtracted from it, and R the remainder. Thus A = B + R. Since A is odd, it is not divisible into two equal parts (D7.7).

**Step 2.** Choose the sum-of-evens route, since B and R together reconstruct A. Suppose R were even. Then B and R would both be even, so their sum A would be even (9.21).

**Step 3.** Consequently A would be divisible into two equal parts (D7.6), contradicting Step 1 (D7.7). Therefore R is not even.

**Step 4.** Since R is not even, it is not divisible into two equal parts (D7.6), and hence it is odd (D7.7). Therefore, if an even number is subtracted from an odd number, the remainder is odd.

**USED:** 9.21, D7.6, D7.7
**Human refs (from References field):** 9.24, D7.7
**Jaccard:** 0.250 — AI adds ['9.21', 'D7.6']; Human adds ['9.24']

## Proposition 9.28
**Statement:** If an odd number by multiplying an even number make some number, the product will be even.

**Step 1.** Let A be the given odd number, B the given even number, and C the product made when A multiplies B. By D7.15, C is the sum of as many copies of B as there are units in A. We choose this direct repeated-addition route because it immediately expresses C as a sum of even numbers, without interchanging the factors.

**Step 2.** Every summand is B and is therefore even by hypothesis. By 9.21, the sum of any multitude of even numbers is even. Consequently C is even, as required.

**USED:** 9.21, D7.15
**Human refs (from References field):** 9.21, D7.15
**Jaccard:** 1.000 — Perfect match.

## Proposition 9.29
**Statement:** If an odd number by multiplying an odd number make some number, the product will be odd.

**Step 1.** Let A and B be odd numbers, and let A by multiplying B produce C. By the definition of multiplication, C is the sum of as many copies of B as there are units in A (D7.15).

**Step 2.** Every summand is odd because B is odd, and their multitude is odd because A is odd. Thus 9.23 applies directly: an odd multitude of odd numbers has an odd sum. This repeated-addition route is the natural choice because Step 1 gives exactly its hypotheses. Therefore C is odd, as required (9.23).

**USED:** 9.23, D7.15
**Human refs (from References field):** 9.23, D7.15
**Jaccard:** 1.000 — Perfect match.

## Proposition 9.30
**Statement:** If an odd number measure an even number, it will also measure the half of it.

**Step 1.** Let the odd number A measure the even number B. Then B consists of m copies of A, for some whole multiplier m (D7.5, D7.15). Since an even number cannot equal an odd number, B is not A; hence m is at least two (D7.6, D7.7).

**Step 2.** Path choice: use the parity of the multiplier, since measurement has already expressed B as a product. If m were odd, then m multiplying the odd number A would produce an odd number, by 9.29. But its product B is even, a contradiction. Thus m is not odd and therefore is even (D7.6, D7.7).

**Step 3.** Since m is even, divide the m copies of A into two groups containing equally many copies (D7.6). Let H be the sum of the copies in the first group. The second group also has sum H, since its summands are respectively equal to those of the first group (CN2, applied repeatedly). The two groups together constitute B, so B = H + H (D7.15).

**Step 4.** Therefore H is the half of B (D7.6). Since H consists of a whole multitude of copies of A, A measures H; if a group contains only one copy, A measures H once (D7.5, D7.15). Hence the odd number A also measures the half of the even number B, as required.

**USED:** 9.29, CN2, D7.15, D7.5, D7.6, D7.7
**Human refs (from References field):** 9.23
**Jaccard:** 0.000 — AI adds ['9.29', 'CN2', 'D7.15', 'D7.5', 'D7.6', 'D7.7']; Human adds ['9.23']

## Proposition 9.31
**Statement:** If an odd number be prime to any number, it will also be prime to the double of it.

**Step 1.** Let A be an odd number prime to B, and let C = B + B be the double of B. Thus C is even, and B is its half. [D7.6]

**Step 2.** Suppose that A and C are not prime to one another. Then some number D greater than a unit measures both A and C. [D7.12]

**Step 3.** D must be odd. For if D were even, then A, being either D itself or a sum of copies of D, would be even: in the latter case, a sum of even numbers is even. This contradicts the oddness of A. Therefore D is not divisible into two equal parts and is odd. [D7.5, 9.21, D7.7]

**Step 4.** Since the odd number D measures the even number C, it also measures its half, B. We choose 9.30 directly because the given doubling makes B precisely the half required by that proposition. [9.30]

**Step 5.** Consequently D measures both A and B, contrary to their being prime to one another. Hence no number greater than a unit measures both A and C. Therefore A is prime to C, the double of B, as required. [D7.12]

**USED:** 9.21, 9.30, D7.12, D7.5, D7.6, D7.7
**Human refs (from References field):** 9.30
**Jaccard:** 0.167 — AI adds ['9.21', 'D7.12', 'D7.5', 'D7.6', 'D7.7']

## Proposition 9.32
**Statement:** Each of the numbers which are continually doubled beginning from a dyad is even-times even only.

**Step 1.** Let u be the unit and A₀ the dyad, u + u. Let A₁, A₂, …, Aᵣ be its successive doubles, so that Aᵢ = Aᵢ₋₁ + Aᵢ₋₁. Here A₀ is the starting dyad, and A₁, …, Aᵣ are the numbers obtained by doubling it. The dyad is even because it consists of two equal units; every subsequent term is even because it consists of two equal parts. [D7.1, D7.2, D7.6]

**Step 2.** Choose any of these doubled numbers, N = Aₖ, where k ≥ 1. Its predecessor Aₖ₋₁ measures N according to the dyad, since two copies of Aₖ₋₁ make N. Both the predecessor and the dyad are even by Step 1. Therefore N is even-times even. [D7.15, D7.8]

**Step 3.** To establish exclusivity, use descent by halves: proposition 9.30 applies directly to the given doubling chain. Suppose an odd number O measures N. Since N is even, O also measures its half Aₖ₋₁. Repeating 9.30 along the chain shows that O measures A₀, the dyad. Applying 9.30 once more shows that O measures its half, the unit. This is impossible: a number is a multitude of units and therefore exceeds a single unit, whereas even one copy of it cannot be contained in the unit. Thus no odd number measures N. [9.30, D7.1, D7.2, CN5]

**Step 4.** Suppose N were also even-times odd. Then an even number E would measure N according to an odd number O; that is, O multiplying E would produce N. By commutativity of multiplication, E multiplying O would also produce N, so O would measure N. This contradicts Step 3. Hence N is not even-times odd. [D7.9, D7.15, 7.16]

**Step 5.** Thus N is even-times even, but not even-times odd: it is even-times even only. Since N was any number obtained by successive doubling from the dyad, each of the stated numbers is even-times even only. [D7.8, D7.9]

**USED:** 7.16, 9.30, CN5, D7.1, D7.15, D7.2, D7.6, D7.8, D7.9
**Human refs (from References field):** 9.13, D7.8
**Jaccard:** 0.100 — AI adds ['7.16', '9.30', 'CN5', 'D7.1', 'D7.15', 'D7.2', 'D7.6', 'D7.9']; Human adds ['9.13']

## Proposition 9.33
**Statement:** If a number have its half odd, it is even-times odd only.

**Step 1.** Let N be a number whose half H is odd. Then N = H + H, so N is even. [D7.6]

**Step 2.** By the definition of multiplication, twice H makes N; by commutativity of multiplication, H times the dyad also makes N. Thus the dyad, which is even, measures N according to the odd number H. Therefore N is even-times odd. [D7.15, 7.16, D7.6, D7.9]

**Step 3.** To establish “only,” we exclude an even-times even representation. We choose to halve the count of equal even summands, since this leads directly to the sum-of-even-numbers result. Suppose, then, that N is also even-times even. There would be an even number E measuring N according to an even number K; thus N consists of K copies of E. [D7.8, D7.15]

**Step 4.** Since K is even, divide these copies into two groups containing equal numbers of copies. Their sums are equal by repeated addition of equals, and together they constitute N; hence each group sums to its half H. If a group contains just one copy, H equals the even number E. Otherwise, H is a sum of even numbers and is therefore even. [D7.6, CN2, 9.21]

**Step 5.** This contradicts the hypothesis that H is odd, for an odd number is not divisible into two equal parts. Consequently N is not even-times even. Since Step 2 established that N is even-times odd, N is even-times odd only. [D7.6, D7.7, D7.8, D7.9]

**USED:** 7.16, 9.21, CN2, D7.15, D7.6, D7.7, D7.8, D7.9
**Human refs (from References field):** D7.8, D7.9
**Jaccard:** 0.250 — AI adds ['7.16', '9.21', 'CN2', 'D7.15', 'D7.6', 'D7.7']

## Proposition 9.34
**Statement:** If a number neither be one of those which are continually doubled from a dyad, nor have its half odd, it is both even-times even and even-times odd.

**Step 1.** Let A be the given number and B its half. By hypothesis B is not odd, and therefore B is even (D7.6, D7.7). We use successive halving, since this directly continues the information given about the first half.

**Step 2.** Since A consists of two copies of B, the even number B measures A according to the dyad. The dyad is itself even, being divisible into two equal units. Hence A is even-times even (D7.6, D7.8).

**Step 3.** Starting with A, continue taking halves whenever the current number is even (D7.6). Each half is strictly smaller than the number halved (CN5). Since A is a finite multitude of units, this process must terminate, either at the unit or at a number which is not even (D7.2). It cannot terminate at the unit: reversing the halvings would then obtain A by continually doubling from the dyad, contrary to the hypothesis. Therefore it terminates at a number C which is odd (D7.7).

**Step 4.** Starting with the unit, perform exactly as many doublings as there were halvings from A to C, and call the resulting number E. There were at least two halvings, since both A and its first half B are even. In particular, E is a double and is even (D7.6). Now reverse the halvings from C back to A. Starting with one copy of C, each reversal doubles the number of copies; thus the final number of copies is E. Consequently A is the sum of E copies of C, that is, the product of E and C (CN2, D7.15).

**Step 5.** By commutativity of multiplication, A is also the sum of C copies of E (7.16, D7.15). Thus the even number E measures A according to the odd number C, so A is even-times odd (D7.9). Together with Step 2, this proves that A is both even-times even and even-times odd.

**USED:** 7.16, CN2, CN5, D7.15, D7.2, D7.6, D7.7, D7.8, D7.9
**Human refs (from References field):** D7.8
**Jaccard:** 0.111 — AI adds ['7.16', 'CN2', 'CN5', 'D7.15', 'D7.2', 'D7.6', 'D7.7', 'D7.9']

## Proposition 9.35
**Statement:** If as many numbers as we please be in continued proportion, and there be subtracted from the second and the last numbers equal to the first, then, as the excess of the second is to the first, so will the excess of the last be to all those before it.

**Step 1.** Let a₁, a₂, …, aₙ be the given numbers in continued proportion, so that a₁:a₂ = a₂:a₃ = ⋯ = aₙ₋₁:aₙ. The stipulated excess of the second over the first presupposes a₂ > a₁; consequently the equal successive ratios imply a₁ < a₂ < ⋯ < aₙ. Put d = a₂ − a₁ and e = aₙ − a₁. If there are only two terms, the required proportion is identical on both sides; hence suppose n ≥ 3. [D7.20]

**Step 2.** Put S = a₁ + a₂ + ⋯ + aₙ₋₁ and T = a₂ + a₃ + ⋯ + aₙ. Since the successive ratios are equal, the ratio of one antecedent to its consequent equals the ratio of all antecedents together to all consequents together. Thus a₁:a₂ = S:T. We choose this numerical summation theorem first because these two shifted sums lead directly to the required excess. [7.12]

**Step 3.** Since aₙ = a₁ + e, adding a₂ + ⋯ + aₙ₋₁ to both sides gives T = S + e. Therefore the remainder after subtracting S from T is precisely e. [CN2]

**Step 4.** Alternating the proportion in Step 2 gives a₂:T = a₁:S. Thus the wholes a₂ and T have the same ratio as the quantities a₁ and S subtracted from them. By the numerical subtraction theorem, their remainders have that same ratio. Consequently d:e = a₁:S. [7.13, 7.11]

**Step 5.** Alternating this last proportion gives d:a₁ = e:S, or explicitly
(a₂ − a₁):a₁ = (aₙ − a₁):(a₁ + a₂ + ⋯ + aₙ₋₁).
Hence the excess of the second over the first is to the first as the excess of the last over the first is to all the numbers before the last added together. [7.13]

**USED:** 7.11, 7.12, 7.13, CN2, D7.20
**Human refs (from References field):** 7.11, 7.12, 7.13
**Jaccard:** 0.600 — AI adds ['CN2', 'D7.20']

## Proposition 9.36
**Statement:** If as many numbers as we please beginning from an unit be set out continuously in double proportion, until the sum of all becomes prime, and if the sum multiplied into the last make some number, the product will be perfect.

**Step 1.** Write the given progression as a₀ = 1, a₁ = 2, …, aₖ = A, where each term is double its predecessor. Let p = a₀ + a₁ + … + aₖ be prime, and let N = pA be the proposed perfect number. Since the unit is not a prime number, k ≥ 1; consequently A ≥ 2 and p > A. Products here denote repeated addition. [D7.2, D7.11, D7.15, CN5]

**Step 2.** Let B = a₀ + a₁ + … + aₖ₋₁. Doubling these terms gives precisely a₁, a₂, …, aₖ, so p = 1 + 2B. But also p = B + A. Subtracting B from these equal expressions gives A = 1 + B. This obtains the needed summation identity directly from the doubling of the progression. [D7.15, CN2, CN3]

**Step 3.** The dyad is prime, since its only smaller positive measure is the unit. Each term of the progression measures A, by 9.11, with the unit and A itself included directly. Conversely, 9.13 shows that A has no numerical divisor outside this progression. Thus its positive divisors are exactly a₀, a₁, …, aₖ. We choose 9.13 because it applies directly to the given progression with the prime dyad next to the unit, without requiring a general factorization argument. [D7.2, D7.11, D7.15, 9.11, 9.13]

**Step 4.** Consider the following two lists:

(a) a₀, a₁, …, aₖ;

(b) pa₀, pa₁, …, paₖ₋₁.

Every entry measures N: whenever A = aᵢc, multiplication gives N = aᵢ(pc) = (paᵢ)c. Regrouping products follows from repeated addition, and their factors may be interchanged. Every entry in (a) is at most A < N, while every entry in (b) is less than pA = N. Hence all are proper divisors. Each list is strictly increasing, and the lists are disjoint because every entry in (a) is at most A whereas every entry in (b) is at least p > A. [9.11, D7.15, 7.16, CN5]

**Step 5.** To show that these are all the proper divisors, let d > 1 be any proper divisor of N. Write N = de; since d < N, the complementary factor e is also greater than the unit. The prime p measures de, so it measures d or e. [D7.3, D7.15, CN5, 7.30]

**Step 6.** If p measures d, write d = pb, allowing b to be the unit. Then pA = de = p(be), and cancellation gives A = be. Such cancellation is legitimate because, by repeated addition, a greater multiplicand would give a greater product with the same positive multiplier. Thus b is a divisor of A, so Step 3 gives b = aᵢ for some i. Since d = pb < pA, we have b < A and therefore i < k. Hence d occurs in list (b). [D7.15, CN5, 9.13]

**Step 7.** If p measures e, write e = pc, allowing c to be the unit. Then pA = d(pc) = p(dc). Cancelling p as in Step 6 gives A = dc. Thus d measures A and, by Step 3, equals one of a₀, a₁, …, aₖ. Hence d occurs in list (a). The unit already occurs there as a₀, so the two disjoint lists contain every proper divisor of N exactly once. [D7.15, 7.16, CN5, 9.13]

**Step 8.** The sum of list (a) is p, and the sum of list (b) is pB. Therefore the sum of all the proper divisors of N is p + pB = p(1 + B) = pA = N, using A = 1 + B from Step 2. Thus N equals the sum of its own parts and is perfect, as required. [D7.15, CN2, D7.3, D7.22]

**USED:** 7.16, 7.30, 9.11, 9.13, CN2, CN3, CN5, D7.11, D7.15, D7.2, D7.22, D7.3
**Human refs (from References field):** 7.14, 7.19, 7.20, 7.21, 7.29, 9.13, 9.35, D7.20, D7.22
**Jaccard:** 0.105 — AI adds ['7.16', '7.30', '9.11', 'CN2', 'CN3', 'CN5', 'D7.11', 'D7.15', 'D7.2', 'D7.3']; Human adds ['7.14', '7.19', '7.20', '7.21', '7.29', '9.35', 'D7.20']
