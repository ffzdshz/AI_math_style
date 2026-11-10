# Book 9 of Euclid's Elements — Step-by-Step AI Proofs (Run A)

## Proposition 9.1
**Statement:** If two similar plane numbers by multiplying one another make some number, the product will be square.

**Step 1.** Let A and B be the given similar plane numbers, and let N be their product. By **8.18**, there is a number M such that A:M = M:B. This mean-proportional route applies directly to the given similarity, avoiding a reconstruction from the sides.

**Step 2.** Apply **7.19** to the four proportional numbers A, M, M, B. The product of the first and fourth equals the product of the second and third. Hence N = A·B = M·M.

**Step 3.** A number produced by multiplying a number by itself is square, by **D7.18**. Therefore N, the product of the two similar plane numbers, is square.

**USED:** 7.19, 8.18, D7.18
**Human refs (from References field):** 7.17, 8.18, 8.22, 8.8
**Jaccard:** 0.167 — AI adds ['7.19', 'D7.18']; Human adds ['7.17', '8.22', '8.8']

## Proposition 9.2
**Statement:** If two numbers by multiplying one another make a square number, they are similar plane numbers.

**Step 1.** Let A and B be the two numbers whose product is square. By the definition of a square number, there is a number C such that AB = CC. [Hypothesis; D7.18]

**Step 2.** Apply the converse direction of 7.19 to the four numbers A, C, C, B. Since the product of the extremes equals the product of the means, these numbers are proportional: A:C = C:B. Thus C is a mean proportional between A and B. [7.19]

**Step 3.** Use the mean-proportional criterion, since the side of the given square has supplied precisely such a mean. If one mean proportional number falls between two numbers, those numbers are similar plane numbers. Therefore A and B are similar plane numbers, as required. [8.20]

**USED:** 7.19, 8.20, D7.18
**Human refs (from References field):** 7.17, 8.18, 8.20, 8.8
**Jaccard:** 0.167 — AI adds ['7.19', 'D7.18']; Human adds ['7.17', '8.18', '8.8']

## Proposition 9.3
**Statement:** If a cube number by multiplying itself make some number, the product will be cube.

**Step 1.** Let C be a cube number, and let P be the product of C with itself. By D7.19, there is a number r such that, putting S = r·r, we have C = r·S; also P = C·C (D7.15). Our chosen route is to apply 8.23 by exhibiting C and P as the first and fourth terms of a continued proportion.

**Step 2.** Let r multiply C to produce X, and let S multiply C to produce Y. Thus X = r·C and Y = S·C (D7.15).

**Step 3.** Multiplication by r sends r, S, C to S, C, X respectively. Applying 7.17 to the successive pairs gives
r:S = S:C and S:C = C:X.

**Step 4.** The multipliers r, S, C, acting on the common number C, produce X, Y, P respectively. Hence, by 7.18,
X:Y = r:S and Y:P = S:C.

**Step 5.** Combining these equalities gives C:X = X:Y = Y:P (CN1). Therefore C, X, Y, P are four numbers in continued proportion. Since the first, C, is a cube, the fourth, P, is also a cube by 8.23. Thus a cube number multiplied by itself produces a cube.

**USED:** 7.17, 7.18, 8.23, CN1, D7.15, D7.19
**Human refs (from References field):** 8.23, 8.8, D7.20
**Jaccard:** 0.125 — AI adds ['7.17', '7.18', 'CN1', 'D7.15', 'D7.19']; Human adds ['8.8', 'D7.20']

## Proposition 9.4
**Statement:** If a cube number by multiplying a cube number make some number, the product will be cube.

**Step 1.** Let A and B be the given cube numbers, and let C be the product obtained when A multiplies B. Let D be the product obtained when A multiplies itself. Since A is cube, D is cube by **9.3**.

**Step 2.** The same number A, multiplying A and B, produces D and C respectively. Consequently, by **7.17**, D:C = A:B.

**Step 3.** Use **8.25**, the natural direct choice because Step 2 supplies a ratio of two cube numbers: if two numbers have the ratio of a cube to a cube and the first is cube, the second is also cube. Here D:C equals the ratio A:B of two cubes, and D is cube by Step 1. Therefore C is cube. Thus the product of the two given cube numbers is cube.

**USED:** 7.17, 8.25, 9.3
**Human refs (from References field):** 7.17, 8.19, 8.23, 8.8, 9.3
**Jaccard:** 0.333 — AI adds ['8.25']; Human adds ['8.19', '8.23', '8.8']

## Proposition 9.5
**Statement:** If a cube number by multiplying any number make a cube number, the multiplied number will also be cube.

**Step 1.** Let the cube number A, by multiplying the number N, produce the cube number C, so that AN = C. Let a and c be the respective sides of these cubes: A = a³ and C = c³. We must prove that N is a cube. [D7.15, D7.19]

**Step 2.** Since AN = C, A measures C. Therefore a measures c, because a cube measuring a cube has its side measuring the other's side. This is the direct path: 8.15 applies immediately to the divisibility supplied by the hypothesis. [D7.3, D7.15, 8.15]

**Step 3.** Since a measures c, let d be the number according to which it measures c; thus c = ad. Form E = d³, which is a cube. [D7.3, D7.15, D7.19]

**Step 4.** Regrouping the repeated additions that define multiplication, and interchanging factors, gives
C = c³ = (ad)(ad)(ad) = (aaa)(ddd) = AE.
Thus A, by multiplying E, also produces C. [D7.15, 7.16]

**Step 5.** A multiplied by N and by E produces C in both cases. Hence N:E = C:C, since products by the same number have the same ratio as the numbers multiplied. Therefore N = E. Since E is a cube, N is also a cube, as required. [7.17, D7.20, D7.19]

**USED:** 7.16, 7.17, 8.15, D7.15, D7.19, D7.20, D7.3
**Human refs (from References field):** 7.17, 8.19, 8.23, 8.8, 9.3
**Jaccard:** 0.091 — AI adds ['7.16', '8.15', 'D7.15', 'D7.19', 'D7.20', 'D7.3']; Human adds ['8.19', '8.23', '8.8', '9.3']

## Proposition 9.6
**Statement:** If a number by multiplying itself make a cube number, it will itself also be cube.

**Step 1.** Let A be the given number, and let B = A·A be the number it produces by multiplying itself. By hypothesis, B is a cube. [D7.15; hypothesis]

**Step 2.** Form C = B·A = (A·A)·A. Since C is contained by the three equal numbers A, A, A, it is a cube. [D7.15, D7.19]

**Step 3.** Choose the direct route through 9.5: the known cube B, by multiplying A, produces the cube C. Therefore the multiplied number A is itself a cube, as required. [9.5]

**USED:** 9.5, D7.15, D7.19
**Human refs (from References field):** 8.19, 8.23, 8.8, D7.20
**Jaccard:** 0.000 — AI adds ['9.5', 'D7.15', 'D7.19']; Human adds ['8.19', '8.23', '8.8', 'D7.20']

## Proposition 9.7
**Statement:** If a composite number by multiplying any number make some number, the product will be solid.

**Step 1.** Let A be a composite number, and let A multiplying any number B produce C. We use the direct factorization route. Since A is composite, it has a numerical measure D smaller than itself (D7.13).

**Step 2.** Let E consist of as many units as there are times that D measures A. Since D is smaller than A, it measures A at least twice; hence E is a number (D7.2). By the definition of multiplication, E multiplying D produces A (D7.15).

**Step 3.** Thus the three numbers E, D, and B produce C by successive multiplication: E multiplying D produces A, and A multiplying B produces C by hypothesis. Therefore C is a solid number, with sides E, D, and B (D7.17). Hence the product of a composite number with any number is solid.

**USED:** D7.13, D7.15, D7.17, D7.2
**Human refs (from References field):** D7.13, D7.15
**Jaccard:** 0.500 — AI adds ['D7.17', 'D7.2']

## Proposition 9.8
**Statement:** If as many numbers as we please beginning from an unit be in continued proportion, the third from the unit will be square, as will also those which successively leave out one; the fourth will be cube, as will also all those which leave out two; and the seventh will be at once cube and square, as will also those which leave out five.

**Step 1.** Write the given progression as a_0, a_1, …, a_N, where a_0 is the unit, counted as the first term. Thus all consecutive ratios a_j : a_{j+1} are equal. We use the numerical ex-aequali theorem, 7.14, because equal-length portions of this progression already have equal corresponding ratios; this exhibits the required squares and cubes directly. [Hypothesis; D7.1; D7.20]

**Step 2.** Let r and k be positive integers with r + k ≤ N. Compare the two equally long lists a_0, a_1, …, a_k and a_r, a_{r+1}, …, a_{r+k}. Their corresponding consecutive ratios are equal by hypothesis. Therefore, ex aequali,

a_0 : a_k = a_r : a_{r+k}. [7.14]

**Step 3.** Since a_0 is the unit, it measures a_k as many times as there are units in a_k. The proportion in Step 2 therefore says that a_r measures a_{r+k} that same number of times. Consequently, a_{r+k} is obtained by adding a_r to itself as many times as there are units in a_k: it is a_r multiplied by a_k. Hence

a_{r+k} = a_r · a_k. [D7.2; D7.20; D7.15]

**Step 4.** For every positive k with 2k ≤ N, put r = k in Step 3. Then a_{2k} = a_k · a_k, so a_{2k} is square. Counting the unit first, these are precisely the third, fifth, seventh, and succeeding terms obtained by leaving out one term each time. [Step 3; D7.18]

**Step 5.** For every positive k with 3k ≤ N, put r = 2k in Step 3. Then

a_{3k} = a_{2k} · a_k = (a_k · a_k) · a_k.

Thus a_{3k} is contained by three equal numbers and is cube. These are precisely the fourth, seventh, tenth, and succeeding terms obtained by leaving out two terms each time. [Steps 3–4; D7.19]

**Step 6.** For every positive k with 6k ≤ N, the term a_{6k} is square by Step 4, taking its index as 2(3k), and cube by Step 5, taking its index as 3(2k). These are precisely the seventh, thirteenth, nineteenth, and succeeding terms obtained by leaving out five terms each time. Hence all three assertions hold for every indicated term present in the given progression. [Steps 4–5]

**USED:** 7.14, D7.1, D7.15, D7.18, D7.19, D7.2, D7.20
**Human refs (from References field):** 8.22, 8.23, D7.20
**Jaccard:** 0.111 — AI adds ['7.14', 'D7.1', 'D7.15', 'D7.18', 'D7.19', 'D7.2']; Human adds ['8.22', '8.23']

## Proposition 9.9
**Statement:** If as many numbers as we please beginning from an unit be in continued proportion, and the number after the unit be square, all the rest will also be square.

**Step 1.** Let u, A₁, A₂, …, Aₙ be the given progression, where u is the unit and A₁ is square. Thus u:A₁ = A₁:A₂ = A₂:A₃ = …, wherever these terms occur. [Hypothesis; D7.20]

**Step 2.** Apply 9.8 first: it directly supplies the alternating square terms under the given continued-proportion hypothesis. Counting the unit as the first term, the third term is A₂; hence A₂, A₄, A₆, …, insofar as they occur, are all square. [9.8]

**Step 3.** For the intervening terms, use 8.22, which states that if three numbers are in continued proportion and the first is square, the third is also square. Indeed, whenever j ≥ 1 and j + 2 ≤ n, the numbers Aⱼ, Aⱼ₊₁, Aⱼ₊₂ are in continued proportion. Consequently, if Aⱼ is square, then Aⱼ₊₂ is square. [Step 1; 8.22]

**Step 4.** Since A₁ is square by hypothesis, Step 3 gives successively that A₃ is square, then A₅ is square, and so on through every odd-indexed term present in the finite progression. [Hypothesis; Step 3]

**Step 5.** Every number after the unit has either an even or an odd index. The even-indexed terms are square by Step 2, and the odd-indexed terms are square by Step 4. Therefore all the remaining numbers are square, as required. [Steps 2 and 4]

**USED:** 8.22, 9.8, D7.20
**Human refs (from References field):** 8.22, 8.23, 9.3, 9.8
**Jaccard:** 0.400 — AI adds ['D7.20']; Human adds ['8.23', '9.3']

## Proposition 9.10
**Statement:** If as many numbers as we please beginning from an unit be in continued proportion, and the number after the unit be not square, neither will any other be square except the third from the unit and all those which leave out one.

**Step 1.** Let the given progression be a₁, a₂, …, aₙ, where a₁ is the unit and a₂ is not square. By hypothesis, the successive ratios a₁:a₂, a₂:a₃, … are equal (D7.20).

**Step 2.** By 9.8, every existing term in positions 3, 5, 7, … is square. These are precisely the third from the unit and the terms obtained thereafter by leaving out one.

**Step 3.** For the remaining positions, use 8.22: if three numbers are in continued proportion and the first is square, the third is also square. This is the direct route because applying it to three consecutive terms in reverse order carries squareness backwards by two positions.

**Step 4.** Suppose some term a₂ₖ in an even position beyond the second is square, with k ≥ 2. Since a₂ₖ₋₂:a₂ₖ₋₁ = a₂ₖ₋₁:a₂ₖ, inversion gives a₂ₖ:a₂ₖ₋₁ = a₂ₖ₋₁:a₂ₖ₋₂ (D7.20). Thus a₂ₖ, a₂ₖ₋₁, a₂ₖ₋₂ are in continued proportion, and 8.22 makes a₂ₖ₋₂ square. Repeating this same application through the preceding triples makes a₂ₖ₋₄, …, a₂ square. This contradicts the hypothesis that a₂ is not square.

**Step 5.** Therefore no even-positioned term is square: the second is not square by hypothesis, and every later even position is excluded by Step 4. Together with Step 2, this proves that, among the numbers following the unit, exactly the third from the unit and all those which successively leave out one are square (9.8; 8.22).

**USED:** 8.22, 9.8, D7.20
**Human refs (from References field):** 8.25, 8.26, 9.6, 9.8
**Jaccard:** 0.167 — AI adds ['8.22', 'D7.20']; Human adds ['8.25', '8.26', '9.6']

## Proposition 9.11
**Statement:** If as many numbers as we please beginning from an unit be in continued proportion, the less measures the greater according to some one of the numbers which have place among the proportional numbers.

**Step 1.** Let a₀ = u, a₁, …, aₙ be the given terms, where u is the unit and
u : a₁ = a₁ : a₂ = ⋯ = aₙ₋₁ : aₙ.
Since a₁ is a multitude of units, u is a proper part of a₁. By the equality of the successive ratios, each term is likewise a proper part of the next. Thus a₀ < a₁ < ⋯ < aₙ. (Hypothesis; D7.2, D7.20, D7.3, CN5.)

**Step 2.** Choose any lesser term aᵢ and greater term aⱼ, so that i < j, and put d = j − i. Compare the two blocks
a₀, a₁, …, a_d
and
aᵢ, aᵢ₊₁, …, aⱼ.
They contain equally many terms, and their corresponding successive ratios are equal by the continued-proportion hypothesis. (Step 1; hypothesis.) Path choice: these matching blocks lead directly to numerical ex aequali, without constructing products.

**Step 3.** Applying numerical ex aequali to these blocks gives
u : a_d = aᵢ : aⱼ. (7.14.)
If d = 1, this equality is already given by the continued proportion; if i = 0, the two ratios are identical.

**Step 4.** The unit measures a_d according to the number a_d, since a_d consists of that multitude of units. (D7.2.) Therefore the proportion in Step 3 says that aᵢ is the same part of aⱼ that the unit is of a_d: consequently, aᵢ measures aⱼ according to a_d. (D7.20, D7.3.) Since 1 ≤ d ≤ n, a_d is one of the given proportional numbers. The chosen lesser and greater terms were arbitrary; hence the less measures the greater according to some one of the numbers having place among the proportional numbers.

**USED:** 7.14, CN5, D7.2, D7.20, D7.3
**Human refs (from References field):** 7.15
**Jaccard:** 0.000 — AI adds ['7.14', 'CN5', 'D7.2', 'D7.20', 'D7.3']; Human adds ['7.15']

## Proposition 9.12
**Statement:** If as many numbers as we please beginning from an unit be in continued proportion, by however many prime numbers the last is measured, the next to the unit will also be measured by the same.

**Step 1.** Let 1, A₁, A₂, …, Aₙ be the given finite continued proportion, and let p be any prime number measuring Aₙ. By the hypothesis of continued proportion, for every k with 2 ≤ k ≤ n,
1 : A₁ = Aₖ₋₁ : Aₖ.
These proportions express equality of the respective parts or multiples (D7.20).

**Step 2.** In each such proportion, the unit is the same part of A₁ that Aₖ₋₁ is of Aₖ. Consequently, Aₖ consists of as many copies of Aₖ₋₁ as there are units in A₁ (D7.20). By the definition of multiplication, therefore,
Aₖ = A₁ · Aₖ₋₁ (D7.15).

**Step 3.** Choose the first term Aⱼ among A₁, …, Aₙ which p measures; such a term exists because p measures Aₙ. We use 7.30 directly, since Step 2 supplies a product to which its prime-divisor conclusion applies. If j > 1, then Aⱼ = A₁ · Aⱼ₋₁ by Step 2, so p measures either A₁ or Aⱼ₋₁ (7.30). Both precede Aⱼ, contradicting its choice as the first term measured by p. Hence j = 1, and p measures A₁.

**Step 4.** Since p was any prime number measuring the last term, Step 3 applies separately to every such prime. Therefore, by however many prime numbers the last term is measured, the term next to the unit is also measured by those same primes, as required.

**USED:** 7.30, D7.15, D7.20
**Human refs (from References field):** 7.19, 7.20, 7.21, 7.29, 9.11, 9.8, D7.14
**Jaccard:** 0.000 — AI adds ['7.30', 'D7.15', 'D7.20']; Human adds ['7.19', '7.20', '7.21', '7.29', '9.11', '9.8', 'D7.14']

## Proposition 9.13
**Statement:** If as many numbers as we please beginning from an unit be in continued proportion, and the number after the unit be prime, the greatest will not be measured by any except those which have a place among the proportional numbers.

**Step 1.** Write the given progression as a₀ = 1, a₁ = p, a₂, …, aₙ, where p is prime. The continued proportion gives aᵢ₊₁ = p·aᵢ for every i < n, by the definitions of numerical proportion and multiplication (D7.20, D7.15). Since p is a number, it exceeds the unit; consequently each successive term exceeds its predecessor, and aₙ is the greatest (D7.2, CN5).

**Step 2.** Path choice: use 9.12 directly to identify the possible prime divisors, then handle arbitrary divisors by choosing a greatest listed divisor. If a prime r divides aₙ, then r also divides p by 9.12. Since p is prime, r cannot be a proper numerical divisor of p; hence r = p (D7.11). Thus p is the only possible prime divisor of aₙ.

**Step 3.** Let d divide aₙ, and suppose, for a contradiction, that d is not one of a₀, a₁, …, aₙ. The unit divides every number (D7.2), so among this finite list there is a greatest term aₖ dividing d. Write d = aₖ·q, where q is the number of times aₖ measures d (D7.5, D7.15, 7.16). Since d is not a listed term, d ≠ aₖ, so q exceeds the unit. Moreover, aₖ < d ≤ aₙ, because a proper multiple exceeds its measure; hence k < n (D7.15, CN5).

**Step 4.** By 7.32, q is either prime or measured by a prime. Thus choose a prime r dividing q, taking r = q if q itself is prime. This proposition applies directly without requiring q to be composite. Since d = aₖ·q, q divides d (D7.15, 7.16). Therefore r divides d and hence aₙ: measurement is transitive because a repeated sum of repeated sums of a number is again a repeated sum of that number (D7.15). Step 2, by 9.12 and D7.11, now gives r = p. Consequently p divides q.

**Step 5.** Write q = p·t, where t is a number or the unit. Regrouping the repeated additions defining multiplication, and interchanging factors where necessary, gives

d = aₖ·q = aₖ·(p·t) = (p·aₖ)·t = aₖ₊₁·t

(D7.15, 7.16, and Step 1). Thus aₖ₊₁ divides d. But k < n, so aₖ₊₁ is a listed term greater than aₖ, contradicting the choice of aₖ. Therefore every divisor of the greatest term has a place among the given proportional terms, as required.

**USED:** 7.16, 7.32, 9.12, CN5, D7.11, D7.15, D7.2, D7.20, D7.5
**Human refs (from References field):** 7.19, 7.31, 9.11, 9.12, 9.8
**Jaccard:** 0.077 — AI adds ['7.16', '7.32', 'CN5', 'D7.11', 'D7.15', 'D7.2', 'D7.20', 'D7.5']; Human adds ['7.19', '7.31', '9.11', '9.8']

## Proposition 9.14
**Statement:** If a number be the least that is measured by prime numbers, it will not be measured by any other prime number except those originally measuring it.

**Step 1.** Let N be the least number measured by the given prime numbers p₁, …, pᵣ. Suppose, for contradiction, that another prime q measures N, with q different from every pᵢ. These are the hypothesis and the assumed contrary of the conclusion.

**Step 2.** Since q is prime, no prime different from q measures it. Thus none of the pᵢ measures q. In particular, N cannot equal q, since every pᵢ measures N. [D7.11; Step 1]

**Step 3.** Because q measures N and N is not q, there is a number M such that multiplying M by q produces N. [D7.5, D7.15] Moreover, M<N: N consists of M copies of q, each containing more than one unit, so one unit from each copy constitutes a proper part of N equal to M. [D7.2, D7.15, CN5]

**Step 4.** Take any of the given primes pᵢ. It measures N, the product of M and q; therefore it measures M or q. [7.30] The latter is excluded by Step 2, so pᵢ measures M. Since pᵢ was arbitrary, every given prime measures M. The direct prime-product proposition 7.30 is the natural choice here because the required product is already available; no auxiliary coprimality argument is needed.

**Step 5.** Thus M is a number smaller than N and measured by all the given primes, contradicting the assumed leastness of N. [Steps 3–4; hypothesis] Consequently, no prime other than the primes originally specified can measure N, as required.

**USED:** 7.30, CN5, D7.11, D7.15, D7.2, D7.5
**Human refs (from References field):** 7.30
**Jaccard:** 0.167 — AI adds ['CN5', 'D7.11', 'D7.15', 'D7.2', 'D7.5']

## Proposition 9.15
**Statement:** If three numbers in continued proportion be the least of those which have the same ratio with them, any two whatever added together will be prime to the remaining number.

**Step 1.** Let A, B, C be in continued proportion, A:B = B:C, and be the least numbers having this ratio. By 8.3, A and C are prime to one another. This is the direct path: 8.3 applies immediately to the leastness hypothesis, without constructing another proportional triple.

**Step 2.** Applying 7.19 to A:B = B:C gives A·C = B·B.

**Step 3.** Suppose that the sum of some two of A, B, C is not prime to the remaining number. They therefore have a common numerical measure d [D7.12]. By 7.32, either d is prime, in which case take p = d, or some prime p measures d. Thus a prime p measures both the chosen sum and the remaining number. Here and below, a measure passes to multiples, and a measure of a sum and one summand measures the other summand: these are consequences of repeated addition and subtraction of equal multiples [D7.5, D7.15, CN2, CN3].

**Step 4.** First suppose that the remaining number is an extreme. Since the argument is unchanged on interchanging A and C, let it be A. Then p measures A and B+C. Because p measures A, it measures A·C, and hence B·B by Step 2 [D7.15, 7.19]. Since p is prime, 7.30 implies that p measures B. Subtracting B from B+C shows that p also measures C [CN3 and the measuring rule in Step 3]. Thus p measures both A and C, contrary to their being prime to one another [8.3, D7.12]. This excludes either extreme as the remaining number.

**Step 5.** Now suppose that the remaining number is B. Then p measures B and A+C. It therefore measures B·B = A·C [D7.15, 7.19]. By 7.30, p measures A or C. In the first case, subtracting A from A+C shows that p measures C; in the second, subtracting C shows that p measures A [CN3 and the measuring rule in Step 3]. Again p measures both extremes, contradicting 8.3 and D7.12.

**Step 6.** Every possible choice of the remaining number has been covered. No numerical common measure can therefore exist between any two of A, B, C added together and the remaining number. Consequently A+B is prime to C, A+C is prime to B, and B+C is prime to A [D7.12], as required.

**USED:** 7.19, 7.30, 7.32, 8.3, CN2, CN3, D7.12, D7.15, D7.5
**Human refs (from References field):** 2.3, 2.4, 7.22, 7.24, 7.25, 7.28, 8.2
**Jaccard:** 0.000 — AI adds ['7.19', '7.30', '7.32', '8.3', 'CN2', 'CN3', 'D7.12', 'D7.15', 'D7.5']; Human adds ['2.3', '2.4', '7.22', '7.24', '7.25', '7.28', '8.2']

## Proposition 9.16
**Statement:** If two numbers be prime to one another, the second will not be to any other number as the first is to the second.

**Step 1.** Let A and B be numbers prime to one another; thus their only common measure is a unit (D7.12). Suppose, for a contradiction, that there is a number C such that A:B = B:C.

**Step 2.** Since A and B are prime to one another, they are the least numbers having their ratio (7.21). This least-terms route is the direct choice because 7.21 applies immediately to the given coprimality.

**Step 3.** The least numbers having a given ratio measure the corresponding numbers in any pair having that ratio (7.20). Applying this to A:B = B:C, we obtain that A measures B.

**Step 4.** Since A also measures itself once, A is a common measure of A and B. But A, being a number, is a multitude of units and not a unit (D7.2). This contradicts their being prime to one another (D7.12). Therefore no number C satisfies B:C = A:B: the second number is not to any other number as the first is to the second.

**USED:** 7.20, 7.21, D7.12, D7.2
**Human refs (from References field):** 7.20, 7.21
**Jaccard:** 0.500 — AI adds ['D7.12', 'D7.2']

## Proposition 9.17
**Statement:** If there be as many numbers as we please in continued proportion, and the extremes of them be prime to one another, the last will not be to any other number as the first to the second.

**Step 1.** Let A₁, A₂, …, Aₙ be the given numbers in continued proportion, with n ≥ 2, and let A₁ and Aₙ be prime to one another. Thus no number other than the unit measures both extremes (D7.12).

**Step 2.** Suppose, for a contradiction, that there is a number X such that Aₙ:X = A₁:A₂. The extended list A₁, A₂, …, Aₙ, X is therefore in continued proportion. Path choice: compare the original chain with its one-place shift, since this brings the given coprime extremes directly into a proportion. The chains A₁, …, Aₙ and A₂, …, Aₙ, X have corresponding successive ratios equal; hence, ex aequali,
A₁:Aₙ = A₂:X (7.14).

**Step 3.** Since A₁ and Aₙ are prime to one another, they are the least numbers having their ratio (7.21). The least numbers in a ratio measure the corresponding numbers in every equal ratio (7.20). Applied to the proportion in Step 2, this shows that A₁ measures A₂.

**Step 4.** Every successive ratio Aᵢ:Aᵢ₊₁ equals A₁:A₂. Since A₁ measures A₂, the definition of proportional numbers therefore gives that each Aᵢ measures Aᵢ₊₁ (D7.20). Consequently A₁ measures Aₙ: successively, each next term consists of repetitions of the preceding term, so repetitions of a term measured by A₁ remain measured by A₁ (D7.15).

**Step 5.** Thus A₁ measures both itself and Aₙ. Since A₁ is a number, not a unit (D7.2), this contradicts the hypothesis that the extremes are prime to one another (D7.12). Therefore no number X satisfies Aₙ:X = A₁:A₂: the last is not to any other number as the first is to the second.

**USED:** 7.14, 7.20, 7.21, D7.12, D7.15, D7.2, D7.20
**Human refs (from References field):** 7.13, 7.20, 7.21
**Jaccard:** 0.250 — AI adds ['7.14', 'D7.12', 'D7.15', 'D7.2', 'D7.20']; Human adds ['7.13']

## Proposition 9.18
**Statement:** Given two numbers, to investigate whether it is possible to find a third proportional to them.

**Step 1.** Let the given numbers, in their assigned order, be A and B. We seek a number C such that A:B = B:C (D7.20). Choose the product criterion of 7.19: it applies directly to A, B, B, C and makes the required proportion equivalent to AC = BB. This avoids an unnecessary preliminary reduction of the given ratio.

**Step 2.** Multiply B by itself, producing the square number S = BB (D7.15, D7.18). Investigate whether S is the sum of at least two copies of A: begin with A and successively add another A until the sum equals or exceeds S. This is a finite investigation, since S consists of finitely many units and each addition strictly increases the sum (D7.2, D7.15, CN5). Equality with only one copy is not accepted, because the required third term must be a number, not merely the unit (D7.1, D7.2).

**Step 3.** Suppose equality occurs with at least two copies of A, and let C be the number of these copies. Then CA = S by the definition of multiplication, and AC = CA by commutativity (D7.15, 7.16). Hence AC = BB. The converse direction of 7.19 therefore gives A:B = B:C. Thus C is the required third proportional.

**Step 4.** Suppose instead that the investigation finds no equality with at least two copies of A. If a third proportional number C nevertheless existed, then A:B = B:C would imply AC = BB = S by 7.19. By 7.16 and D7.15, S would consequently consist of C copies of A. Since C is a number rather than the unit, these would be at least two copies (D7.1, D7.2), contradicting the investigation. Thus no third proportional number exists in this case.

**Step 5.** Therefore the investigation is complete: form the square of the second given number and test whether it consists of a number of copies of the first. If it does, that number of copies is a third proportional; if it does not, no third proportional number is possible (D7.15, 7.19).

**USED:** 7.16, 7.19, CN5, D7.1, D7.15, D7.18, D7.2, D7.20
**Human refs (from References field):** 7.19, 9.16
**Jaccard:** 0.111 — AI adds ['7.16', 'CN5', 'D7.1', 'D7.15', 'D7.18', 'D7.2', 'D7.20']; Human adds ['9.16']

## Proposition 9.19
**Statement:** Given three numbers, to investigate when it is possible to find a fourth proportional to them.

**Step 1.** Let the three given numbers, in their assigned order, be A, B, C. We seek a number X such that A:B = C:X (D7.20). **Path choice:** use 7.19 directly: this proportion holds if and only if the product AX equals the product BC. This gives an immediate test without first reducing the given ratios.

**Step 2.** Form the number P = BC (D7.15). Count successive whole copies of A until their sum either equals or first exceeds P. This is a finite test, since A and P are finite multitudes of units (D7.2, D7.15). Accept precisely when equality is reached after two or more copies; otherwise reject. The restriction to two or more copies ensures that their count is a number, rather than merely the unit (D7.1, D7.2).

**Step 3.** If the test accepts, let X be the number of copies counted. Then AX = P = BC by the definition of multiplication (D7.15). Hence A:B = C:X by the converse direction of 7.19. Thus X is the required fourth proportional.

**Step 4.** Conversely, suppose a fourth proportional number X exists. By 7.19, AX = BC = P. Therefore P consists of exactly X whole copies of A (D7.15). Since X is a number and not the unit, there are at least two such copies (D7.1, D7.2). The test in Step 2 must therefore accept. Consequently, whenever that test rejects, no fourth proportional number exists.

**Step 5.** The investigation is complete: a fourth proportional number exists exactly when A measures BC and BC is greater than A—that is, when A is a proper divisor of BC—and the required number is the number of times A measures BC (D7.3, D7.15; 7.19). If BC = A, the count is only the unit, so it does not supply a fourth proportional number in the sense of D7.1–D7.2.

**USED:** 7.19, D7.1, D7.15, D7.2, D7.20, D7.3
**Human refs (from References field):** 7.14, 7.19, 7.20, 7.21, 9.17
**Jaccard:** 0.100 — AI adds ['D7.1', 'D7.15', 'D7.2', 'D7.20', 'D7.3']; Human adds ['7.14', '7.20', '7.21', '9.17']

## Proposition 9.20
**Statement:** Prime numbers are more than any assigned multitude of prime numbers.

**Step 1.** Let p₁, …, pₖ be any assigned finite collection of distinct prime numbers. Obtain a common multiple M by starting with p₁ and successively applying 7.34 to the preceding common multiple and the next prime. Each preceding prime continues to measure the resulting number, since grouping repetitions shows that a multiple of a multiple is again a multiple of the original number (D7.5). Thus every pᵢ measures M. Path choice: iterate the two-number common-multiple construction; its leastness property is not needed.

**Step 2.** Adjoin one unit u to M, forming the number N = M + u (D7.1, D7.2). Since each pᵢ measures M, each is at most M; and N is greater than M (D7.5, CN5). Hence N is greater than every assigned prime. If N is prime, it is therefore a prime outside the assigned collection, and adjoining it increases that collection (CN5).

**Step 3.** It remains to consider the case in which N is not prime. Then N is composite (D7.11, D7.13), so some prime q measures N by 7.31. Path choice: use the composite-number prime-divisor theorem directly, since the prime case has already been settled.

**Step 4.** Suppose q were one of the assigned primes. Then q would measure M by Step 1, as well as N by Step 3. Subtract the q-sized groups composing M from the q-sized groups composing N. Since N > M, a positive number of such groups remains; thus q measures N − M = u (CN3, D7.5). But q is a number, hence a multitude of units, and is greater than one unit (D7.1, D7.2, CN5). Even one q-sized group therefore exceeds u, so q cannot measure u. This contradiction shows that q is different from every assigned prime.

**Step 5.** In either case, a prime outside the assigned collection has been found: N in Step 2, or q in Steps 3–4. Adjoining that prime gives a strictly greater multitude of distinct primes (CN5). Since the assigned collection was arbitrary, prime numbers are more than any assigned multitude of prime numbers.

**USED:** 7.31, 7.34, CN3, CN5, D7.1, D7.11, D7.13, D7.2, D7.5
**Human refs (from References field):** 7.31
**Jaccard:** 0.111 — AI adds ['7.34', 'CN3', 'CN5', 'D7.1', 'D7.11', 'D7.13', 'D7.2', 'D7.5']

## Proposition 9.21
**Statement:** If as many even numbers as we please be added together, the whole is even.

**Step 1.** Let E₁, …, Eₙ be any finite collection of even numbers. By D7.6, divide each Eᵢ into two equal parts Aᵢ and Bᵢ. Thus Aᵢ = Bᵢ for every i. (Path choice: combine these equal parts directly, since the definition already supplies the required divisions.)

**Step 2.** Let A be the sum of all the parts Aᵢ, and let B be the sum of all the parts Bᵢ. Since the corresponding parts are equal, repeated application of CN2 gives A = B.

**Step 3.** A number is a multitude of units (D7.2). Gathering the first part of each summand into A and the second into B therefore partitions the whole sum E₁ + ⋯ + Eₙ into these two parts, without omitting or repeating any unit. By Step 2 the parts are equal. Hence the whole sum is divisible into two equal parts and is therefore even (D7.6).

**USED:** CN2, D7.2, D7.6
**Human refs (from References field):** D7.6
**Jaccard:** 0.333 — AI adds ['CN2', 'D7.2']

## Proposition 9.22
**Statement:** If as many odd numbers as we please be added together, and their multitude be even, the whole will be even.

**Step 1.** Let A₁, …, Aₙ be the given odd numbers, where their multitude n is even. Remove one unit from each Aᵢ, leaving an even number Eᵢ, so that Aᵢ = Eᵢ + 1 (D7.7). This route reduces the question directly to the already established addition theorem for even numbers, 9.21.

**Step 2.** Let E be the sum of E₁, …, Eₙ. Since every Eᵢ is even, E is even (9.21).

**Step 3.** The removed units, one from each of the n given numbers, together constitute the number n (D7.2). Their sum is therefore even, by the hypothesis that the multitude of the given numbers is even.

**Step 4.** Adding the equalities Aᵢ = Eᵢ + 1 shows that the sum of the given odd numbers equals E + n (CN2). Both E and n are even, so their sum is even (9.21). Therefore, if an even multitude of odd numbers is added together, the whole is even.

**USED:** 9.21, CN2, D7.2, D7.7
**Human refs (from References field):** 9.21, D7.7
**Jaccard:** 0.500 — AI adds ['CN2', 'D7.2']

## Proposition 9.23
**Statement:** If as many odd numbers as we please be added together, and their multitude be odd, the whole will also be odd.

**Step 1.** Let the given odd numbers be a₁, …, aₙ, with their multitude n odd, and let S be their sum. If there is only one summand, S is odd by hypothesis. Otherwise, removing one from the odd multitude leaves the even multitude n − 1. [D7.7]

**Step 2.** Let T be the sum of a₂, …, aₙ. These are odd numbers in an even multitude, so T is even. [9.22] This is the direct path: separating one summand makes the preceding proposition immediately applicable.

**Step 3.** Remove a unit from a₁, and call the remainder b. Since a₁ is odd, b is even. [D7.7] Therefore E = T + b is even, being the sum of two even numbers. [9.21]

**Step 4.** Since a₁ = b + 1, adding T to both sides gives S = E + 1. [CN2] Thus S differs by a unit from the even number E, and consequently S is odd. [D7.7] Therefore the sum of any odd multitude of odd numbers is odd.

**USED:** 9.21, 9.22, CN2, D7.7
**Human refs (from References field):** 9.21, 9.22, D7.7
**Jaccard:** 0.750 — AI adds ['CN2']

## Proposition 9.24
**Statement:** If from an even number an even number be subtracted, the remainder will be even.

**Step 1.** Let A be an even number, B the smaller even number subtracted from it, and R = A − B. Since A and B are even, they have equal halves a and b respectively, so A = a + a and B = b + b. (D7.6)

**Step 2.** We have a > b. For if a = b, adding equals gives A = B; if a < b, then a + a is a proper part of b + b, giving A < B. Both contradict A > B. (CN2, CN5)

**Step 3.** Apply the previously proved subtraction rule for equimultiples: if a whole and a subtracted part are the same multiples of another whole and its subtracted part, their remainders are also those same multiples. Here A is twice a, and B is twice b; therefore A − B is twice a − b. Thus R = (a − b) + (a − b). This route is chosen because the equal halves immediately supply the doubles required by the theorem. (5.5)

**Step 4.** Consequently R is divisible into the two equal parts a − b and a − b. Hence the remainder is even. (D7.6)

**USED:** 5.5, CN2, CN5, D7.6
**Human refs (from References field):** D7.6
**Jaccard:** 0.250 — AI adds ['5.5', 'CN2', 'CN5']

## Proposition 9.25
**Statement:** If from an even number an odd number be subtracted, the remainder will be odd.

**Step 1.** Let A be the given even number, B the odd number subtracted, and R the remainder, so A = B + R. By D7.6, A is divisible into two equal parts; by D7.7, B is not.

**Step 2.** Suppose, for a contradiction, that R is even. Then subtracting R from the even number A leaves an even remainder, by 9.24. (Path choice: 9.24 applies directly to the original whole and the supposed even remainder, requiring no auxiliary construction.)

**Step 3.** Subtracting R from both sides of A = B + R gives A − R = B [CN3]. Thus B is even by Step 2, contradicting its oddness: it cannot both be divisible and not divisible into two equal parts [D7.6, D7.7].

**Step 4.** Therefore R is not even, so it is not divisible into two equal parts [D7.6]. Hence R is odd [D7.7]. Thus, if an odd number is subtracted from an even number, the remainder is odd.

**USED:** 9.24, CN3, D7.6, D7.7
**Human refs (from References field):** 9.24, D7.7
**Jaccard:** 0.500 — AI adds ['CN3', 'D7.6']

## Proposition 9.26
**Statement:** If from an odd number an odd number be subtracted, the remainder will be even.

**Step 1.** Let A be the given odd number, B the smaller odd number subtracted, and R the remainder; thus A = B + R (hypothesis). Suppose that R is not even. Then R is odd, since an even number is divisible into two equal parts and an odd number is not (D7.6, D7.7).

**Step 2.** The two summands B and R are therefore odd. Their multitude, two, is even, being divisible into two equal units (D7.6). Hence their sum B + R, which is A, is even by 9.22. This is the chosen route: 9.22 applies directly to the two odd summands, without reconstructing their halves.

**Step 3.** But A is odd by hypothesis, and therefore cannot be divisible into two equal parts (D7.7), whereas its being even requires precisely that divisibility (D7.6). This contradiction rules out the supposition that R is not even. Therefore R is even: if an odd number is subtracted from an odd number, the remainder is even.

**USED:** 9.22, D7.6, D7.7
**Human refs (from References field):** 9.24, D7.7
**Jaccard:** 0.250 — AI adds ['9.22', 'D7.6']; Human adds ['9.24']

## Proposition 9.27
**Statement:** If from an odd number an even number be subtracted, the remainder will be odd.

**Step 1.** Let A be an odd number, and let an even number B be subtracted from it, leaving R. Thus A = B + R. Since A is odd, it is not divisible into two equal parts. [Hypothesis; D7.7]

**Step 2.** Choose the contradiction route using 9.21, since the whole A is already expressed as the sum B + R; no auxiliary numbers are needed. Suppose R were even. Then B and R would both be even, so their sum A would be even. [9.21]

**Step 3.** A would therefore be divisible into two equal parts, contrary to Step 1. Hence R is not even, and thus is not divisible into two equal parts. By the definition of odd, R is odd. Therefore, if an even number is subtracted from an odd number, the remainder is odd. [D7.6; D7.7]

**USED:** 9.21, D7.6, D7.7
**Human refs (from References field):** 9.24, D7.7
**Jaccard:** 0.250 — AI adds ['9.21', 'D7.6']; Human adds ['9.24']

## Proposition 9.28
**Statement:** If an odd number by multiplying an even number make some number, the product will be even.

**Step 1.** Let A be an odd number and B an even number, and let A by multiplying B produce C. By the definition of multiplication, C is the sum of as many copies of B as there are units in A. [D7.15]

**Step 2.** Every summand is B and therefore even by hypothesis. By 9.21, the sum of any multitude of even numbers is even; hence C is even, as required. This is the direct route: the given order of multiplication already expresses C as a sum of even numbers, so no interchange of factors or restriction on the multitude of summands is needed. [9.21]

**USED:** 9.21, D7.15
**Human refs (from References field):** 9.21, D7.15
**Jaccard:** 1.000 — Perfect match.

## Proposition 9.29
**Statement:** If an odd number by multiplying an odd number make some number, the product will be odd.

**Step 1.** Let the odd number A multiply the odd number B to produce C. By the definition of multiplication, C is the sum of as many copies of B as there are units in A. [D7.15]

**Step 2.** Every summand is odd, since B is odd, and their multitude is odd, since A is odd. Thus the direct applicable result is 9.23: a sum of odd numbers whose multitude is odd is itself odd. Applying it to the defining sum gives that C is odd, as required. [9.23]

**USED:** 9.23, D7.15
**Human refs (from References field):** 9.23, D7.15
**Jaccard:** 1.000 — Perfect match.

## Proposition 9.30
**Statement:** If an odd number measure an even number, it will also measure the half of it.

**Step 1.** Let the odd number A measure the even number B. Then B consists of a certain number Q of copies of A, so Q multiplying A produces B. The count Q is not merely a unit, since otherwise B would equal A, contrary to their being even and odd respectively. [D7.5, D7.15, D7.6, D7.7]

**Step 2.** If Q were odd, then Q multiplying the odd number A would produce an odd number, by 9.29. But its product B is even, which is impossible. Therefore Q is not odd and hence is even. Path choice: the multiplication supplied by the hypothesis makes the already-proved odd-product theorem the direct tool. [9.29, D7.6, D7.7]

**Step 3.** Since Q is even, divide the Q copies of A constituting B into two groups containing equally many copies. The sums of these groups are equal, by repeated addition of equals, and together they constitute B. Thus each group has sum equal to the half of B. [D7.6, D7.15, CN2]

**Step 4.** Each group consists of whole copies of A, possibly just one copy. Consequently A measures its sum, and therefore A measures the half of B, as required. [D7.5, D7.15]

**USED:** 9.29, CN2, D7.15, D7.5, D7.6, D7.7
**Human refs (from References field):** 9.23
**Jaccard:** 0.000 — AI adds ['9.29', 'CN2', 'D7.15', 'D7.5', 'D7.6', 'D7.7']; Human adds ['9.23']

## Proposition 9.31
**Statement:** If an odd number be prime to any number, it will also be prime to the double of it.

**Step 1.** Let A be an odd number prime to a number B, and let C = B + B be the double of B. Then C is even, with B as its half. [D7.6]

**Step 2.** Suppose that A and C are not prime to one another. Then some number D greater than the unit measures both A and C. [D7.12]

**Step 3.** D cannot be even. For, since D measures A, A is either D itself or a sum of copies of D. If D were even, A would therefore be even, in the latter case by 9.21, contrary to its being odd. Hence D is odd. [9.21; D7.6; D7.7]

**Step 4.** Apply 9.30: since the odd number D measures the even number C, it also measures its half B. This is the direct path, because 9.30 passes immediately from the double to its half. [9.30]

**Step 5.** Thus D measures both A and B, contradicting the hypothesis that they are prime to one another. Consequently A and C are prime to one another: the odd number A is prime to the double of B. [D7.12]

**USED:** 9.21, 9.30, D7.12, D7.6, D7.7
**Human refs (from References field):** 9.30
**Jaccard:** 0.200 — AI adds ['9.21', 'D7.12', 'D7.6', 'D7.7']

## Proposition 9.32
**Statement:** Each of the numbers which are continually doubled beginning from a dyad is even-times even only.

**Step 1.** Let N be any number obtained by one or more successive doublings of the dyad. Write the finite sequence as a₀ = 2, a₁, …, aᵣ = N, where r ≥ 1 and each term doubles its predecessor. The dyad is the starting seed; its successive doubles are the numbers under consideration. Prefixing a unit gives 1, a₀, a₁, …, aᵣ in continued proportion, since each succeeding term is twice the preceding one. [D7.15, D7.20]

**Step 2.** The dyad divides into two equal units, and each subsequent term divides into two equal copies of its predecessor. Hence every numerical term in this progression is even. Moreover, the dyad is prime: a number is a multitude of units, so no number smaller than the dyad can measure it; its only proper measure is therefore the unit. [D7.2, D7.6, D7.11, CN5]

**Step 3.** The even number aᵣ₋₁ measures N according to the dyad, which is also even. Consequently N is even-times even. [D7.15, D7.8]

**Step 4.** For exclusivity, use the direct divisor-classification route: 9.13 applies naturally because the progression begins with a unit followed by the prime dyad. It follows that every numerical proper measure M of N occurs among a₀, a₁, …, aᵣ₋₁. Thus every such measure M is even, by Step 2. [9.13, D7.6]

**Step 5.** Since M and N belong to this progression and M is less than N, M measures N according to one of the numbers in the progression. That number is not the unit, because M is less than N; hence it too is even by Step 2. Thus every numerical proper measure of N measures it according to an even number, never an odd number. In particular, N is not even-times odd. Together with Step 3, this proves that N is even-times even only. Since N was an arbitrary successive double of the dyad, the proposition follows. [9.11, D7.6, D7.7, D7.8, D7.9]

**USED:** 9.11, 9.13, CN5, D7.11, D7.15, D7.2, D7.20, D7.6, D7.7, D7.8, D7.9
**Human refs (from References field):** 9.13, D7.8
**Jaccard:** 0.182 — AI adds ['9.11', 'CN5', 'D7.11', 'D7.15', 'D7.2', 'D7.20', 'D7.6', 'D7.7', 'D7.9']

## Proposition 9.33
**Statement:** If a number have its half odd, it is even-times odd only.

**Step 1.** Let N be a number whose half H is odd. Thus N = H + H, and N is even by D7.6.

**Step 2.** The dyad multiplying H produces N (D7.15). Therefore H multiplying the dyad also produces N (7.16). Consequently the dyad, which is even, measures N according to the odd number H; hence N is even-times odd (D7.6, D7.9).

**Step 3.** To establish “only,” we exclude an even-times-even representation. Suppose, for a contradiction, that an even number E measures N according to an even number F (D7.8). Then N consists of F equal summands, each equal to E (D7.15).

**Step 4.** Since F is even, divide those summands into two groups containing equally many summands (D7.6). Their sums are equal, since they contain equally many equal terms (CN2), and together they make N; thus each group sums to the half H. Each group consists entirely of even numbers E, so its sum H is even by 9.21. This is the direct prior result to use, because the half has been exhibited as a sum of even numbers.

**Step 5.** But H is odd and therefore is not divisible into two equal parts (D7.7), contradicting its being even (D7.6). Thus N is not even-times even (D7.8). Since it is even-times odd by Step 2, N is even-times odd only (D7.9).

**USED:** 7.16, 9.21, CN2, D7.15, D7.6, D7.7, D7.8, D7.9
**Human refs (from References field):** D7.8, D7.9
**Jaccard:** 0.250 — AI adds ['7.16', '9.21', 'CN2', 'D7.15', 'D7.6', 'D7.7']

## Proposition 9.34
**Statement:** If a number neither be one of those which are continually doubled from a dyad, nor have its half odd, it is both even-times even and even-times odd.

**Step 1.** Let N satisfy the hypotheses, and let H be the numerical half referred to in the statement, so that N = 2H. Since N is not a term of the sequence 2, 4, 8, …, H is not a unit. By hypothesis H is not odd; therefore H is even. (D7.1, D7.6, D7.7.)

**Step 2.** The dyad, an even number, measures N according to the even number H. Thus N is even-times even. (D7.6, D7.15, D7.8.)

**Step 3.** To obtain an odd multiplicity directly, choose the greatest term D of the dyad-doubling sequence that measures N, allowing equality when considering these measures. Such a term exists: the dyad measures N by Step 2, every such measure is at most N, and the successive doubles strictly increase. Since N is a finite multitude of units, there are only finitely many possible such terms. Moreover, D is even, being either the dyad or the double of its preceding term. (D7.2, D7.15, CN5, D7.6.)

**Step 4.** Write N = qD, where q is the multiplicity of this measure. Since N is not itself a term of the dyad-doubling sequence, N is not D; hence q is a number, not a unit. If q were even, its q equal copies of D could be grouped into pairs. Each pair equals 2D, so 2D would also measure N. But 2D is the next term of the sequence and is greater than D, contradicting the choice of D. Consequently q is not even and therefore is odd. (D7.1, D7.2, D7.15, D7.6, CN2, CN5, D7.7.)

**Step 5.** The even number D therefore measures N according to the odd number q, so N is even-times odd. Together with Step 2, this proves that N is both even-times even and even-times odd. (D7.9, D7.8.)

**USED:** CN2, CN5, D7.1, D7.15, D7.2, D7.6, D7.7, D7.8, D7.9
**Human refs (from References field):** D7.8
**Jaccard:** 0.111 — AI adds ['CN2', 'CN5', 'D7.1', 'D7.15', 'D7.2', 'D7.6', 'D7.7', 'D7.9']

## Proposition 9.35
**Statement:** If as many numbers as we please be in continued proportion, and there be subtracted from the second and the last numbers equal to the first, then, as the excess of the second is to the first, so will the excess of the last be to all those before it.

**Step 1.** Let a₁, a₂, …, aₙ be the given numbers in continued proportion, so that a₁:a₂ = a₂:a₃ = ⋯ = aₙ₋₁:aₙ (hypothesis; D7.20). Let e = a₂ − a₁ and f = aₙ − a₁ be the stated excesses, and put S = a₁ + ⋯ + aₙ₋₁ and T = a₂ + ⋯ + aₙ. We use the numerical summation theorem 7.12 followed by the numerical subtraction theorem 7.11, since these apply directly to the shifted lists and their differences.

**Step 2.** By 7.12, the common ratio of the corresponding terms equals the ratio of their sums; hence a₁:a₂ = S:T. Alternating this proportion gives a₁:S = a₂:T (7.13).

**Step 3.** Since aₙ = a₁ + f, replacing the last term in T shows that T = S + f: both sums contain the same intermediate terms a₂, …, aₙ₋₁ (CN2). Subtracting S therefore gives T − S = f (CN3).

**Step 4.** Regard a₂ and T as the wholes, and a₁ and S as the respective numbers subtracted. Step 2 shows that the wholes have the same ratio as the numbers subtracted. Consequently, their remainders have that same ratio (7.11):
(a₂ − a₁):(T − S) = a₂:T.
Using Step 3 and the equality of ratios in Step 2, this becomes e:f = a₁:S (CN1).

**Step 5.** Alternating the last proportion gives e:a₁ = f:S (7.13). Thus, as the excess of the second number over the first is to the first, so is the excess of the last number over the first to the sum of all the numbers before the last, as required.

**USED:** 7.11, 7.12, 7.13, CN1, CN2, CN3, D7.20
**Human refs (from References field):** 7.11, 7.12, 7.13
**Jaccard:** 0.429 — AI adds ['CN1', 'CN2', 'CN3', 'D7.20']

## Proposition 9.36
**Statement:** If as many numbers as we please beginning from an unit be set out continuously in double proportion, until the sum of all becomes prime, and if the sum multiplied into the last make some number, the product will be perfect.

**Step 1.** Let the given progression be a₀ = 1, a₁ = 2, …, aₘ = a, where each term doubles its predecessor. Put p = a₀ + a₁ + ⋯ + aₘ, and let N = pa. By hypothesis p is prime. Since the unit is not a number, m ≥ 1, and consequently a ≥ 2. Products below denote repeated addition. [D7.2, D7.11, D7.15]

**Step 2.** Use 9.35 directly to evaluate the sum, rather than derive a geometric-sum formula. Apply it to the doubled progression 2a₀, 2a₁, …, 2aₘ. Its first two terms are 2 and 4, its last term is 2a, and the sum of all terms before the last is a₁ + ⋯ + aₘ = p − 1. Therefore
2 : 2 = (2a − 2) : (p − 1).
Thus p − 1 = 2a − 2, and hence p = 2a − 1 and p − a = a − 1. In particular, p = a + (a − 1) > a. [9.35, D7.20, CN2, CN3, CN5]

**Step 3.** Determine the measures of a by the directly applicable progression theorem 9.13. The dyad is prime: no number is smaller than it, so its only proper measure is the unit. [D7.2, D7.11] Every numerical term of the original progression smaller than a measures a by 9.11; the unit and a itself also measure a. Since the first term after the unit is prime, 9.13 excludes every other numerical measure. Consequently the complete list of positive measures of a, including the unit and a itself, is a₀, a₁, …, aₘ. [9.11, 9.13, D7.15]

**Step 4.** Let d > 1 be any proper measure of N. Write N = de, where e > 1. [D7.3, D7.15] Since the prime p measures de, it measures d or e. [7.30] In the following equalities, regrouping products follows from repeated addition, and interchanging factors is justified by 7.16. Cancellation of a common multiplier follows directly from 7.17 and D7.20. [D7.15, CN2, 7.16, 7.17, D7.20]

If p measures d, write d = pb, allowing b to be the unit. Then pa = (pb)e = p(be), so a = be. Thus b measures a and is some aᵢ by Step 3. Since d < N, b < a; hence i < m, and d = paᵢ.

If p measures e, write e = pc, allowing c to be the unit. Then pa = d(pc) = p(dc), so a = dc. Thus d measures a and is some aᵢ by Step 3.

Therefore every proper measure of N other than the unit belongs to one of the lists a₀, …, aₘ or pa₀, …, paₘ₋₁.

**Step 5.** Conversely, since each aᵢ measures a, both aᵢ and paᵢ measure pa = N. [Step 3; D7.15, 7.16] Every aᵢ is less than N, and every paᵢ with i < m is less than N, because aᵢ < a. [D7.15, CN5] The terms within each list are distinct, since successive terms double; the two lists are disjoint, since every term of the first is at most a, whereas every term of the second is at least p > a. [Step 2; D7.15, CN5] Including the unit a₀, the proper measures of N are therefore exactly
 a₀, a₁, …, aₘ, and pa₀, pa₁, …, paₘ₋₁. [Step 4; D7.3]

**Step 6.** The sum of these proper measures is
(a₀ + ⋯ + aₘ) + p(a₀ + ⋯ + aₘ₋₁)
= p + p(p − a)
= p + p(a − 1)
= pa
= N.
Here the first list sums to p by Step 1, the shorter sum is p − a, and Step 2 gives p − a = a − 1; collecting the repeated additions is justified by D7.15 and CN2. Thus N equals the sum of all its own parts and is perfect. [CN3, D7.15, CN2, D7.3, D7.22]

**USED:** 7.16, 7.17, 7.30, 9.11, 9.13, 9.35, CN2, CN3, CN5, D7.11, D7.15, D7.2, D7.20, D7.22, D7.3
**Human refs (from References field):** 7.14, 7.19, 7.20, 7.21, 7.29, 9.13, 9.35, D7.20, D7.22
**Jaccard:** 0.200 — AI adds ['7.16', '7.17', '7.30', '9.11', 'CN2', 'CN3', 'CN5', 'D7.11', 'D7.15', 'D7.2', 'D7.3']; Human adds ['7.14', '7.19', '7.20', '7.21', '7.29']
