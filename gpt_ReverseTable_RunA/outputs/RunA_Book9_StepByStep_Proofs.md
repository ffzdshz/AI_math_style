# Book 9 of Euclid's Elements — Step-by-Step AI Proofs (Run A)

## Proposition 9.1
**Statement:** If two similar plane numbers by multiplying one another make some number, the product will be square.

**Step 1.** Let A and B be similar plane numbers, and let P be the number produced by multiplying A by B. Choose the mean-proportional route because it directly supplies a number whose square can be identified with P. By 8.18, there is a number M such that A:M = M:B. [8.18]

**Step 2.** Apply 7.19 to the four proportional numbers A, M, M, B. The product of the first and fourth equals the product of the second and third; hence P = A·B = M·M. [7.19]

**Step 3.** A number produced by multiplying equal numbers is a square number. Since P = M·M, P is square. Thus the product of two similar plane numbers is square, as required. [D7.18]

**USED:** 7.19, 8.18, D7.18
**Human refs (from References field):** 7.17, 8.18, 8.22, 8.8
**Jaccard:** 0.167 — AI adds ['7.19', 'D7.18']; Human adds ['7.17', '8.22', '8.8']

## Proposition 9.2
**Statement:** If two numbers by multiplying one another make a square number, they are similar plane numbers.

**Step 1.** Let A and B be numbers whose product is square. By the definition of a square number, there is a number C such that AB = CC. [D7.18]

**Step 2.** Apply the converse direction of VII.19 to the four numbers A, C, C, B. Since the product of the first and fourth equals the product of the second and third, A:C = C:B. Thus C is a mean proportional between A and B. [7.19]

**Step 3.** Use the mean-proportional criterion, since Step 2 supplies exactly its hypothesis: numbers between which one mean proportional falls are similar plane numbers. Therefore A and B are similar plane numbers, as required. [8.20]

**USED:** 7.19, 8.20, D7.18
**Human refs (from References field):** 7.17, 8.18, 8.20, 8.8
**Jaccard:** 0.167 — AI adds ['7.19', 'D7.18']; Human adds ['7.17', '8.18', '8.8']

## Proposition 9.3
**Statement:** If a cube number by multiplying itself make some number, the product will be cube.

**Step 1.** Let A be a cube number, and let B = A·A. By the definition of a cube, there is a number c such that, putting d = c·c, we have A = d·c. By commutativity of multiplication, also A = c·d. [D7.19, 7.16]

**Step 2.** Since c multiplying c and d produces d and A respectively, the products have the same ratio as the numbers multiplied. Hence c:d = d:A. [7.17]

**Step 3.** Form E = d·d and F = d·A. Applying the same multiplication theorem gives:
- A:E = c:d, since d multiplying c and d produces A and E;
- E:F = d:A, since d multiplying d and A produces E and F;
- F:B = d:A, since A multiplying d and A produces F and B.
The first and third assertions use commutativity to identify the products. [7.17, 7.16]

**Step 4.** Combining Steps 2 and 3, we obtain A:E = E:F = F:B. Thus A, E, F, B are four numbers in continued proportion. [CN1]

**Step 5.** Apply VIII.23, the direct choice because the constructed four numbers are in continued proportion and their first number A is already cube. Their fourth number B is therefore cube. Since B = A·A, a cube number multiplying itself produces a cube number, as required. [8.23]

**USED:** 7.16, 7.17, 8.23, CN1, D7.19
**Human refs (from References field):** 8.23, 8.8, D7.20
**Jaccard:** 0.143 — AI adds ['7.16', '7.17', 'CN1', 'D7.19']; Human adds ['8.8', 'D7.20']

## Proposition 9.4
**Statement:** If a cube number by multiplying a cube number make some number, the product will be cube.

**Step 1.** Let A and B be cube numbers, and let A by multiplying B produce C. Take the direct route of comparing C with the self-product of A: let A by multiplying itself produce D. Then D is a cube by IX.3. [9.3]

**Step 2.** Since A by multiplying A and B produces D and C respectively, the products have the same ratio as the numbers multiplied. Hence D:C = A:B. [7.17]

**Step 3.** Thus D and C have to one another the ratio of the cube A to the cube B. VIII.25 applies directly to this ratio: since D is a cube, C is also a cube. Therefore a cube number multiplied by a cube number produces a cube. [8.25]

**USED:** 7.17, 8.25, 9.3
**Human refs (from References field):** 7.17, 8.19, 8.23, 8.8, 9.3
**Jaccard:** 0.333 — AI adds ['8.25']; Human adds ['8.19', '8.23', '8.8']

## Proposition 9.5
**Statement:** If a cube number by multiplying any number make a cube number, the multiplied number will also be cube.

**Step 1.** Let A be the given cube number and B the number multiplied by it, so that C = AB is cube. Form D = A·A. Then D is cube by 9.3. We choose this self-product construction because the specific self-product theorem suffices. [9.3]

**Step 2.** Since A multiplying A and B produces D and C respectively, the products have the same ratio as the multiplied numbers. Thus D:C = A:B. [7.17]

**Step 3.** Therefore A and B have the ratio of the cube number D to the cube number C. Since A is cube, 8.25 implies that B is also cube. Hence the multiplied number is cube, as required. [8.25]

**USED:** 7.17, 8.25, 9.3
**Human refs (from References field):** 7.17, 8.19, 8.23, 8.8, 9.3
**Jaccard:** 0.333 — AI adds ['8.25']; Human adds ['8.19', '8.23', '8.8']

## Proposition 9.6
**Statement:** If a number by multiplying itself make a cube number, it will itself also be cube.

**Step 1.** Let A multiplied by itself make B, and suppose B is a cube. Let B multiplied by A make C. Then C is A multiplied by A and again by A, so C is a cube by the definition of a cube number. [D7.19]

**Step 2.** Apply IX.5 directly, since we have a cube factor and a cube product: the cube B, by multiplying A, makes the cube C. Therefore the multiplied number A is itself a cube, as required. [9.5]

**USED:** 9.5, D7.19
**Human refs (from References field):** 8.19, 8.23, 8.8, D7.20
**Jaccard:** 0.000 — AI adds ['9.5', 'D7.19']; Human adds ['8.19', '8.23', '8.8', 'D7.20']

## Proposition 9.7
**Statement:** If a composite number by multiplying any number make some number, the product will be solid.

**Step 1.** Let the composite number A, by multiplying any number B, produce C. We take the direct route through the definition of composite: choose a number D measuring A as a proper part, and let E be the number of times D measures A. Since D is less than A, E is a number, not merely a unit. By the definition of multiplication, E multiplied by D produces A. [D7.13, D7.3, D7.15]

**Step 2.** Thus C is produced by multiplying the three numbers E, D, and B in succession: first E multiplied by D makes A, and then A multiplied by B makes C. In symbols, C = (ED)B. [D7.15]

**Step 3.** A number produced by three numbers multiplying one another is, by definition, solid. Therefore C is a solid number, with sides E, D, and B. Hence a composite number multiplying any number produces a solid number. [D7.17]

**USED:** D7.13, D7.15, D7.17, D7.3
**Human refs (from References field):** D7.13, D7.15
**Jaccard:** 0.500 — AI adds ['D7.17', 'D7.3']

## Proposition 9.8
**Statement:** If as many numbers as we please beginning from an unit be in continued proportion, the third from the unit will be square, as will also those which successively leave out one; the fourth will be cube, as will also all those which leave out two; and the seventh will be at once cube and square, as will also those which leave out five.

**Step 1.** Let the given continued proportion be u, a₁, a₂, …, aₙ, where u is the unit, counted as the first term. We use the arithmetic ex-aequali theorem, since comparing equal-length portions of this progression directly supplies the required factors. For any positive integer r with 2r ≤ n, compare the portions u, a₁, …, aᵣ and aᵣ, aᵣ₊₁, …, a₂ᵣ. Their corresponding successive ratios are equal, so
u : aᵣ = aᵣ : a₂ᵣ.
If 3r ≤ n, comparison with the portion a₂ᵣ, a₂ᵣ₊₁, …, a₃ᵣ likewise gives
u : aᵣ = a₂ᵣ : a₃ᵣ.
For r = 1 these equalities belong to the given continued proportion itself. [7.14]

**Step 2.** From u : aᵣ = aᵣ : a₂ᵣ, the unit measures aᵣ the same number of times that aᵣ measures a₂ᵣ. Thus a₂ᵣ consists of as many copies of aᵣ as there are units in aᵣ: it is aᵣ multiplied by itself, and hence a square. This holds for every r with 2r ≤ n. These terms occupy positions 3, 5, 7, …, counting the unit first; therefore the third term and all those thereafter obtained by leaving out one term are square. [D7.2, D7.20, D7.15, D7.18]

**Step 3.** Whenever 3r ≤ n, the second equality in Step 1 shows that a₂ᵣ measures a₃ᵣ as many times as the unit measures aᵣ. Therefore aᵣ multiplying a₂ᵣ produces a₃ᵣ. By Step 2, a₂ᵣ is aᵣ multiplied by itself; consequently a₃ᵣ is contained by three equal numbers, each equal to aᵣ, and is a cube. These terms occupy positions 4, 7, 10, …; therefore the fourth term and all those thereafter obtained by leaving out two terms are cube. [D7.2, D7.20, D7.15, D7.19]

**Step 4.** For every positive integer k with 6k ≤ n, Step 2 applied with r = 3k makes a₆ₖ a square with side a₃ₖ, while Step 3 applied with r = 2k makes that same a₆ₖ a cube with side a₂ₖ. Thus these terms are simultaneously square and cube. They occupy positions 7, 13, 19, …: the seventh term and all those thereafter obtained by leaving out five terms. All three assertions follow. [Steps 2–3; D7.18, D7.19]

**USED:** 7.14, D7.15, D7.18, D7.19, D7.2, D7.20
**Human refs (from References field):** 8.22, 8.23, D7.20
**Jaccard:** 0.125 — AI adds ['7.14', 'D7.15', 'D7.18', 'D7.19', 'D7.2']; Human adds ['8.22', '8.23']

## Proposition 9.9
**Statement:** If as many numbers as we please beginning from an unit be in continued proportion, and the number after the unit be square, all the rest will also be square.

**Step 1.** Write the given continued proportion as \(1,a_1,a_2,\ldots,a_n\), where \(a_1\) is square. Separate the terms after the unit into alternate positions, using IX.8 first because it applies directly to this progression: the third, fifth, seventh, and subsequent alternate terms, counting the unit as first, are square. Thus every existing term \(a_2,a_4,a_6,\ldots\) is square. [9.8]

**Step 2.** For the remaining positions, use VIII.22: in three numbers in continued proportion, if the first is square, the third is square. Since \(a_1\) is square, applying this to \(a_1,a_2,a_3\) shows that \(a_3\) is square; applying it next to \(a_3,a_4,a_5\) shows that \(a_5\) is square. Repeating for as long as the finite progression continues proves that every existing term \(a_1,a_3,a_5,\ldots\) is square. Together with Step 1, this covers every number after the unit. Therefore all the rest are square. [8.22]

**USED:** 8.22, 9.8
**Human refs (from References field):** 8.22, 8.23, 9.3, 9.8
**Jaccard:** 0.500 — Human adds ['8.23', '9.3']

## Proposition 9.10
**Statement:** If as many numbers as we please beginning from an unit be in continued proportion, and the number after the unit be not square, neither will any other be square except the third from the unit and all those which leave out one.

**Step 1.** Write the given progression as 1, a₁, a₂, …, aₙ, where a₁ is not square. By IX.8, a₂, a₄, a₆, …, whenever present, are square. These are precisely the third term from the unit and the terms obtained thereafter by leaving out one. [9.8]

**Step 2.** Since 1 : a₁ = aⱼ : aⱼ₊₁, each succeeding number is the same multiple of its predecessor. Thus, for j ≥ 1, every reversed triple aⱼ₊₂, aⱼ₊₁, aⱼ is also in continued proportion: its successive ratios express that same multiple. [D7.20]

**Step 3.** We use VIII.22 on these reversed triples, since it directly transfers squareness by two places. Suppose that some a₂ᵣ₊₁ with r ≥ 1 were square. Applying VIII.22 to a₂ᵣ₊₁, a₂ᵣ, a₂ᵣ₋₁ shows that a₂ᵣ₋₁ is square. Repeating the same application backwards through the progression shows successively that a₂ᵣ₋₃, …, a₁ are square. This contradicts the hypothesis that a₁ is not square. Hence none of a₁, a₃, a₅, … is square. [8.22]

**Step 4.** Therefore, among the numbers following the unit, only the third term from the unit and those which successively leave out one are square, and all those terms are indeed square. This proves the proposition. [9.8, 8.22]

**USED:** 8.22, 9.8, D7.20
**Human refs (from References field):** 8.25, 8.26, 9.6, 9.8
**Jaccard:** 0.167 — AI adds ['8.22', 'D7.20']; Human adds ['8.25', '8.26', '9.6']

## Proposition 9.11
**Statement:** If as many numbers as we please beginning from an unit be in continued proportion, the less measures the greater according to some one of the numbers which have place among the proportional numbers.

**Step 1.** Let the given continued proportion be a₀, a₁, …, aₙ, where a₀ is the unit. The unit is a part of a₁; hence, since a₀:a₁ = aₖ:aₖ₊₁, each aₖ is likewise a part of aₖ₊₁. Thus the terms increase. Take any less term aᵢ and greater term aⱼ, so that i < j. If i = 0, the unit measures aⱼ according to aⱼ itself, which is one of the given terms. It remains to consider i > 0. [D7.2, D7.3, D7.20]

**Step 2.** Put d = j − i. The direct route is to compare two equally long portions of the progression by ex aequali. Consider

a₀, a₁, …, a_d
and
aᵢ, aᵢ₊₁, …, aⱼ.

Corresponding successive terms have the same ratio, by the given continued proportion. Therefore, ex aequali,

a₀:a_d = aᵢ:aⱼ. [7.14]

**Step 3.** The unit a₀ measures a_d as many times as there are units in a_d. By the proportion just obtained, aᵢ is the same part of aⱼ that the unit is of a_d. Consequently aᵢ measures aⱼ according to a_d. Since 1 ≤ d ≤ n, this measuring number a_d has a place among the given proportional numbers. Thus every less term measures every greater term according to one of those numbers, as required. [D7.2, D7.3, D7.20]

**USED:** 7.14, D7.2, D7.20, D7.3
**Human refs (from References field):** 7.15
**Jaccard:** 0.000 — AI adds ['7.14', 'D7.2', 'D7.20', 'D7.3']; Human adds ['7.15']

## Proposition 9.12
**Statement:** If as many numbers as we please beginning from an unit be in continued proportion, by however many prime numbers the last is measured, the next to the unit will also be measured by the same.

**Step 1.** Let the given progression be 1, a₁, a₂, …, aₙ, where 1 denotes the unit and a₁ is the number next to it. For every i ≥ 2, continued proportion gives 1 : a₁ = aᵢ₋₁ : aᵢ. Thus aᵢ₋₁ is the same part of aᵢ that the unit is of a₁. Since a number is composed of units, aᵢ consists of as many copies of aᵢ₋₁ as there are units in a₁. By the definition of multiplication, therefore, aᵢ = a₁ · aᵢ₋₁. [D7.2, D7.20, D7.15]

**Step 2.** Let p be any prime number measuring aₙ. Among a₁, …, aₙ, choose the first term aⱼ measured by p; such a term exists because p measures the last. We apply the prime-divisor-of-a-product theorem directly, since Step 1 expresses each term after a₁ as a product of earlier terms. If j > 1, then aⱼ = a₁ · aⱼ₋₁, so p measures either a₁ or aⱼ₋₁. Both occur before aⱼ, contradicting its choice as the first term measured by p. Hence j = 1, and p measures a₁. [7.30]

**Step 3.** The prime p in Step 2 was arbitrary. Consequently, every prime number measuring the last term also measures the number next to the unit. Thus, by however many prime numbers the last is measured, the next to the unit is measured by those same prime numbers, as required.

**USED:** 7.30, D7.15, D7.2, D7.20
**Human refs (from References field):** 7.19, 7.20, 7.21, 7.29, 9.11, 9.8, D7.14
**Jaccard:** 0.000 — AI adds ['7.30', 'D7.15', 'D7.2', 'D7.20']; Human adds ['7.19', '7.20', '7.21', '7.29', '9.11', '9.8', 'D7.14']

## Proposition 9.13
**Statement:** If as many numbers as we please beginning from an unit be in continued proportion, and the number after the unit be prime, the greatest will not be measured by any except those which have a place among the proportional numbers.

**Step 1.** Write the given progression as
\(a_0=1,a_1=p,a_2,\ldots,a_n=N\), where \(p\) is prime. Since \(1:p=a_i:a_{i+1}\), each term after the unit is obtained by multiplying its predecessor by \(p\). Thus \(a_i=p^i\), where \(p^0=1\). A number contains more than one unit, so \(p>1\), and these successive products strictly increase. [D7.20, D7.15, D7.2, CN5]

**Step 2.** Use IX.12 directly, since it transfers prime measures of the last term to the term next to the unit. If a prime \(q\) measures \(N\), IX.12 says that \(q\) measures \(p\). Since \(p\) is prime and \(q\) is not the unit, \(q=p\). Consequently, every prime measure of \(N\) is \(p\). [9.12, D7.11]

**Step 3.** Let \(b>1\) be any measure of \(N\). If \(b\) is prime, Step 2 gives \(b=p\). Otherwise \(b\) is composite, and VII.31 supplies a prime \(q\) measuring \(b\). Because \(N\) consists of repetitions of \(b\), and \(b\) of repetitions of \(q\), \(q\) also measures \(N\). Step 2 again gives \(q=p\). Hence every nonunit measure of \(N\) is measured by \(p\). [D7.11, D7.13, 7.31, D7.15]

**Step 4.** Now let \(d\) be any measure of \(N\). If \(d=1\), it already occurs in the progression. Otherwise Step 3 permits division by \(p\), giving \(d=p d_1\). The quotient \(d_1\) also measures \(N\): it measures \(d\), by commutativity of multiplication, and grouping the repetitions shows that it measures \(N\). Moreover, \(d_1<d\). Whenever the quotient is not the unit, repeat this operation. Every quotient still measures \(N\), and each contains strictly fewer units than its predecessor. Therefore the process must reach the unit after finitely many divisions, say \(r\). Reversing these divisions gives \(d=p^r\). [D7.15, 7.16, CN5, D7.2]

**Step 5.** Since \(d\) measures \(N\), we have \(d\leq N=p^n\). If \(r>n\), the successive multiplications by \(p>1\) would give \(p^r>p^n\), contrary to that inequality. Thus \(r\leq n\), and \(d=p^r=a_r\), a term of the given progression. Therefore the greatest number is measured by no number except those having a place among the proportional numbers. [D7.15, CN5; Steps 1 and 4]

**USED:** 7.16, 7.31, 9.12, CN5, D7.11, D7.13, D7.15, D7.2, D7.20
**Human refs (from References field):** 7.19, 7.31, 9.11, 9.12, 9.8
**Jaccard:** 0.167 — AI adds ['7.16', 'CN5', 'D7.11', 'D7.13', 'D7.15', 'D7.2', 'D7.20']; Human adds ['7.19', '9.11', '9.8']

## Proposition 9.14
**Statement:** If a number be the least that is measured by prime numbers, it will not be measured by any other prime number except those originally measuring it.

**Step 1.** Let N be the least number measured by the given prime numbers p₁, …, pᵣ. Suppose that another prime q, distinct from every pᵢ, measures N. No pᵢ can measure q, since a prime has no number other than itself as a divisor. Consequently q cannot equal N, for every pᵢ measures N. [D7.11]

**Step 2.** Since q measures N and q ≠ N, write N = qM, where M counts the copies of q making up N. Because q < N, M is a number rather than the unit. [D7.3, D7.15] Also q, being a number, contains more than one unit; thus qM contains more than one copy of M, and M < N. [D7.2, D7.15, CN5]

**Step 3.** Apply VII.30 directly to the product qM: this is the natural route because each given prime pᵢ measures that product. It follows that pᵢ measures q or M. The former is excluded by Step 1, so every pᵢ measures M. [7.30, D7.11] Thus M is a number smaller than N measured by all the given primes, contrary to the defining leastness of N. Therefore N is measured by no prime other than those originally measuring it, as required.

**USED:** 7.30, CN5, D7.11, D7.15, D7.2, D7.3
**Human refs (from References field):** 7.30
**Jaccard:** 0.167 — AI adds ['CN5', 'D7.11', 'D7.15', 'D7.2', 'D7.3']

## Proposition 9.15
**Statement:** If three numbers in continued proportion be the least of those which have the same ratio with them, any two whatever added together will be prime to the remaining number.

**Step 1.** Let A, B, C be the three numbers, with A:B = B:C, and suppose they are the least numbers having these ratios. By VIII.3, A and C are prime to one another. By VII.19 applied to A:B = B:C, AC = B². We use the coprimality of the extremes directly, without constructing a representation of the progression. [8.3, 7.19]

**Step 2.** To prove two numbers prime to one another, it suffices to exclude a prime common measure. Indeed, if they are not prime to one another, they have a common measure d greater than the unit. If d is prime, take p = d; otherwise d is composite, and VII.31 supplies a prime p measuring d and therefore both numbers. We use VII.31 only in the composite case, since the prime case needs no further theorem. Here and below, the elementary rules about measures follow by writing measured numbers as multiples: a measure of a number measures its products; a measure of two numbers measures their positive difference; and measurement is transitive. [D7.12, D7.11, D7.13, 7.31, D7.5]

**Step 3.** Suppose A+B and C are not prime to one another. By Step 2, some prime p measures both. Since p measures C, it measures AC, and hence B² by Step 1. By VII.30 applied to B·B, p measures B. Since it also measures A+B, it measures (A+B)−B = A. Thus p measures both A and C, contrary to Step 1. Therefore A+B is prime to C. [7.30, D7.5, D7.12; Steps 1–2]

**Step 4.** Suppose B+C and A are not prime to one another, and take a prime common measure p as in Step 2. Since p measures A, it measures AC = B². By VII.30, it measures B. Subtracting B from B+C shows that p also measures C. This again contradicts the coprimality of A and C. Therefore B+C is prime to A. [7.30, D7.5, D7.12; Steps 1–2]

**Step 5.** Suppose A+C and B are not prime to one another, and take a prime common measure p. Since p measures B, it measures B² = AC. By VII.30, p measures A or C. If it measures A, then it also measures (A+C)−A = C; if it measures C, then it also measures (A+C)−C = A. Either way, p measures both extremes, a contradiction. Therefore A+C is prime to B. Together with Steps 3–4, this proves that any two of the three numbers added together are prime to the remaining number. [7.30, D7.5, D7.12; Steps 1–2]

**USED:** 7.19, 7.30, 7.31, 8.3, D7.11, D7.12, D7.13, D7.5
**Human refs (from References field):** 2.3, 2.4, 7.22, 7.24, 7.25, 7.28, 8.2
**Jaccard:** 0.000 — AI adds ['7.19', '7.30', '7.31', '8.3', 'D7.11', 'D7.12', 'D7.13', 'D7.5']; Human adds ['2.3', '2.4', '7.22', '7.24', '7.25', '7.28', '8.2']

## Proposition 9.16
**Statement:** If two numbers be prime to one another, the second will not be to any other number as the first is to the second.

**Step 1.** Let A and B be numbers prime to one another. Thus an unit alone is their common measure [D7.12]. Suppose, for a contradiction, that there is a number C such that A:B = B:C.

**Step 2.** Choose the least-ratio route, since it applies directly to the given coprimality: A and B are the least numbers among those having the same ratio with them [7.21].

**Step 3.** The least numbers having a given ratio measure the corresponding numbers of any pair having that ratio. Applying this to A:B = B:C, we obtain that A measures B and B measures C [7.20].

**Step 4.** Since A also measures itself, A is a common measure of A and B. But A, being a number—a multitude of units—is not an unit [D7.2]. This contradicts their being prime to one another [D7.12]. Therefore no number C satisfies A:B = B:C: the second number cannot be to any other number as the first is to the second.

**USED:** 7.20, 7.21, D7.12, D7.2
**Human refs (from References field):** 7.20, 7.21
**Jaccard:** 0.500 — AI adds ['D7.12', 'D7.2']

## Proposition 9.17
**Statement:** If there be as many numbers as we please in continued proportion, and the extremes of them be prime to one another, the last will not be to any other number as the first to the second.

**Step 1.** Let a₁, a₂, …, aₙ be numbers in continued proportion, with a₁ and aₙ prime to one another. Suppose, contrary to the assertion, that there is a number b such that aₙ:b = a₁:a₂. The sequence therefore remains in continued proportion when b is appended. Apply ex aequali to the two chains a₁, …, aₙ and a₂, …, aₙ, b. Their corresponding consecutive ratios are equal, so a₁:aₙ = a₂:b. This shifted-chain route brings the given coprime extremes directly into a single ratio. [7.14]

**Step 2.** Since a₁ and aₙ are prime to one another, they are the least numbers having their ratio. We use this given pair directly, without constructing another least pair. Since a₁:aₙ = a₂:b, these least numbers measure the corresponding numbers a₂ and b the same number of times. In particular, a₁ measures a₂. [7.21, 7.20]

**Step 3.** Let a₂ consist of k repetitions of a₁. Every successive ratio aᵢ:aᵢ₊₁ equals a₁:a₂. By the definition of proportional numbers, each aᵢ₊₁ therefore consists of the same k repetitions of aᵢ. Starting from a₁ and proceeding along the sequence, every term is consequently a whole multiple of a₁. In particular, a₁ measures aₙ. [D7.20]

**Step 4.** Thus a₁ measures both itself and aₙ. But a₁ is a number, a multitude of units, and not the unit; it is therefore a common measure other than the unit. This contradicts the hypothesis that a₁ and aₙ are prime to one another, whose only common measure is the unit. Hence no number b can satisfy aₙ:b = a₁:a₂: the last is not to any other number as the first is to the second. [D7.2, D7.12]

**USED:** 7.14, 7.20, 7.21, D7.12, D7.2, D7.20
**Human refs (from References field):** 7.13, 7.20, 7.21
**Jaccard:** 0.286 — AI adds ['7.14', 'D7.12', 'D7.2', 'D7.20']; Human adds ['7.13']

## Proposition 9.18
**Statement:** Given two numbers, to investigate whether it is possible to find a third proportional to them.

**Step 1.** Let the given numbers, in their given order, be A and B. A third proportional must be a number C such that A:B = B:C. Choose the product criterion, since it translates this requirement immediately into an equality involving the given numbers: by VII.19, such a C exists exactly when A·C = B·B for some number C. [7.19]

**Step 2.** Form P = B·B. Repeatedly subtract A from P while the remainder is at least A, keeping count of the subtractions. This process terminates, since each subtraction removes units from a fixed finite multitude of units. Answer yes precisely when P is exhausted and the count is a number C; answer no when a positive remainder remains or exhaustion requires only one subtraction. The latter count is merely a unit, not a number in Euclid’s sense. Thus the test is finite and uses only multiplication and subtraction. [D7.15, D7.2]

**Step 3.** If the answer is yes, P consists of C copies of A. Hence C·A = P by the definition of multiplication, and A·C = P by commutativity. Since P = B·B, VII.19 gives A:B = B:C. The count C therefore supplies the required third proportional. [D7.15, 7.16, 7.19]

**Step 4.** If the answer is no, suppose nevertheless that a number X is third proportional, so that A:B = B:X. Then VII.19 gives A·X = B·B = P. By commutativity and the definition of multiplication, P therefore consists of exactly X copies of A. Consequently, successive subtraction of A must exhaust P after a numerical count X of subtractions, contrary to the outcome of the test. No third proportional then exists. Thus the investigation is complete: a third proportional exists exactly when B·B is an exact multiple of A with a number, rather than merely a unit, as multiplier. [7.19, 7.16, D7.15, D7.2]

**USED:** 7.16, 7.19, D7.15, D7.2
**Human refs (from References field):** 7.19, 9.16
**Jaccard:** 0.200 — AI adds ['7.16', 'D7.15', 'D7.2']; Human adds ['9.16']

## Proposition 9.19
**Statement:** Given three numbers, to investigate when it is possible to find a fourth proportional to them.

**Step 1.** Let the three given numbers, in their assigned order, be A, B, C. Form the product P = BC. We use VII.19 directly, because it converts the required proportion A:B = C:D into the product equality AD = P. This gives a direct test without first reducing a ratio to least terms. [D7.15, 7.19]

**Step 2.** Suppose a fourth proportional number D exists. By VII.19, AD = BC = P. By commutativity of multiplication and its definition, P therefore consists of as many copies of A as there are units in D. Consequently A measures P. Moreover, since D is a number—a multitude of units, not merely a unit—P is greater than A. Thus P must be a proper multiple of A. [7.19, 7.16, D7.15, D7.2, D7.5]

**Step 3.** Conversely, suppose A measures P and P is greater than A. Let D contain as many units as the number of times A measures P. Since that count exceeds one, D is a number. By the definition of multiplication, DA = P; hence AD = P by commutativity. Therefore AD = BC, and the converse part of VII.19 gives A:B = C:D. Thus D is the required fourth proportional. [D7.5, D7.2, D7.15, 7.16, 7.19]

**Step 4.** The investigation is therefore this: multiply B by C and test whether A measures the resulting product with a quotient that is a number. If it does, that quotient is the fourth proportional; otherwise no fourth proportional number exists. Equivalently, a fourth proportional exists exactly when BC is a proper multiple of A, and then D = BC/A. The qualification excludes BC = A, which yields only a unit rather than a number in Euclid’s terminology. This completes the investigation. [7.19, D7.2]

**USED:** 7.16, 7.19, D7.15, D7.2, D7.5
**Human refs (from References field):** 7.14, 7.19, 7.20, 7.21, 9.17
**Jaccard:** 0.111 — AI adds ['7.16', 'D7.15', 'D7.2', 'D7.5']; Human adds ['7.14', '7.20', '7.21', '9.17']

## Proposition 9.20
**Statement:** Prime numbers are more than any assigned multitude of prime numbers.

**Step 1.** Let p₁, …, pᵣ be any assigned finite multitude of distinct prime numbers. Obtain a number M measured by every pᵢ by starting with p₁ and applying VII.34 successively to the current common multiple and the next prime. Each former measure still measures the new multiple, since copies of the former multiple can be regrouped into copies of that measure. We choose the two-number construction because it applies successively to any finite list; leastness itself is not needed. [7.34, D7.3, D7.5]

**Step 2.** Add a unit u to M, and call the resulting number N. Since each pᵢ measures M, each is at most M; and N is greater than M. If N is prime, it is therefore a prime different from every assigned prime. This settles that case. [D7.1, D7.2, D7.3, D7.5, CN5, D7.11]

**Step 3.** Otherwise N is composite. By VII.31, some prime number q measures N. Thus the composite case leads directly to a prime measure, without requiring any further factorization. [D7.11, D7.13, 7.31]

**Step 4.** Suppose q were one of the assigned primes. Then q would measure both M and N. Subtracting from N the whole copies of q which constitute M leaves N − M = u; hence u would also consist of one or more whole copies of q. But q, being a number, is a multitude of units and is greater than a single unit. It therefore cannot measure u. Consequently q is different from every assigned prime. [D7.3, D7.5, CN3, D7.1, D7.2, CN5]

**Step 5.** In either case there is a prime outside the assigned multitude. Adjoining it gives a greater multitude of prime numbers. Since the assigned multitude was arbitrary, prime numbers are more than any assigned multitude of prime numbers. [D7.2, CN5]

**USED:** 7.31, 7.34, CN3, CN5, D7.1, D7.11, D7.13, D7.2, D7.3, D7.5
**Human refs (from References field):** 7.31
**Jaccard:** 0.100 — AI adds ['7.34', 'CN3', 'CN5', 'D7.1', 'D7.11', 'D7.13', 'D7.2', 'D7.3', 'D7.5']

## Proposition 9.21
**Statement:** If as many even numbers as we please be added together, the whole is even.

**Step 1.** Let any finite collection of even numbers be given. We use the direct route through the definition of evenness: divide each given number into two equal parts, calling one its first part and the other its second part. Such a division exists for each number because it is even. [D7.6]

**Step 2.** Add together all the first parts, and separately add together all the second parts. Each first part equals its corresponding second part; therefore the two resulting sums are equal, by repeated application of the principle that equals added to equals give equal wholes. [CN2]

**Step 3.** These two sums together constitute the whole of the given numbers, since they contain both parts of every given number. Thus the whole is divided into two equal parts and is therefore even. Hence, if as many even numbers as we please are added together, the whole is even. [D7.6]

**USED:** CN2, D7.6
**Human refs (from References field):** D7.6
**Jaccard:** 0.500 — AI adds ['CN2']

## Proposition 9.22
**Statement:** If as many odd numbers as we please be added together, and their multitude be even, the whole will be even.

**Step 1.** Let the given odd numbers be \(a_1,\ldots,a_m\), where their multitude \(m\) is even. Choose the direct unit-removal route: subtract one unit from each odd number, leaving even numbers \(e_1,\ldots,e_m\). Thus \(a_i=e_i+1\) for each \(i\). This uses the even-plus-unit characterization of oddness. [D7.7]

**Step 2.** The sum \(E=e_1+\cdots+e_m\) is even, since a sum of any multitude of even numbers is even. This immediately preceding proposition is the natural result to apply after removing the units. [9.21]

**Step 3.** The removed units are exactly \(m\) in multitude. Since a number is a multitude composed of units, their sum is \(m\), which is even by hypothesis. [D7.2]

**Step 4.** Adding the equalities from Step 1 gives
\[
a_1+\cdots+a_m=E+m.
\]
Both \(E\) and \(m\) are even, so their sum is even. Therefore the whole of the given odd numbers is even, as required. [CN2, 9.21]

**USED:** 9.21, CN2, D7.2, D7.7
**Human refs (from References field):** 9.21, D7.7
**Jaccard:** 0.500 — AI adds ['CN2', 'D7.2']

## Proposition 9.23
**Statement:** If as many odd numbers as we please be added together, and their multitude be odd, the whole will also be odd.

**Step 1.** If there is only one summand, the conclusion is immediate from the hypothesis. Otherwise, set aside one odd summand, calling it A. Since the original multitude is odd, removing one leaves an even multitude (D7.7). We choose this separation because it brings the remaining summands directly under IX.22.

**Step 2.** Let B be the sum of the remaining summands. They are odd numbers, and their multitude is even; therefore B is even (9.22).

**Step 3.** Since A is odd, it differs by a unit from an even number E (D7.7). Both B and E are even, so B + E is even (9.21).

**Step 4.** The whole sum is B + A. It differs by a unit from B + E, which is even. Therefore the whole sum is odd (D7.7). Thus, whenever an odd multitude of odd numbers is added together, the whole is odd.

**USED:** 9.21, 9.22, D7.7
**Human refs (from References field):** 9.21, 9.22, D7.7
**Jaccard:** 1.000 — Perfect match.

## Proposition 9.24
**Statement:** If from an even number an even number be subtracted, the remainder will be even.

**Step 1.** Let A be the given even number and B the even number subtracted, with B<A. We take the direct route through the definition of even: divide A into equal parts A₁, A₂, and B into equal parts B₁, B₂. Thus A=A₁+A₂, B=B₁+B₂, A₁=A₂, and B₁=B₂. [D7.6]

**Step 2.** Since B<A, each half of B is smaller than each half of A. Subtract B₁ from A₁ and B₂ from A₂. The remainders R₁ and R₂ are equal, because equals have been subtracted from equals. [CN3]

**Step 3.** The two parts removed together constitute B; therefore the two remainders together constitute A−B. By Step 2 these remainders are equal, so A−B is divisible into two equal parts and is therefore even. Thus, if an even number is subtracted from an even number, the remainder is even. [D7.6]

**USED:** CN3, D7.6
**Human refs (from References field):** D7.6
**Jaccard:** 0.500 — AI adds ['CN3']

## Proposition 9.25
**Statement:** If from an even number an odd number be subtracted, the remainder will be odd.

**Step 1.** Let A be the given even number, B the odd number subtracted, and C the remainder; thus A consists of B and C. By the definitions, A is divisible into two equal parts, whereas B is not. [D7.6, D7.7]

**Step 2.** Use the preceding subtraction proposition, 9.24, since subtracting C from A leaves B. If C were even, then subtracting the even number C from the even number A would leave an even number. Thus B would be even. [9.24]

**Step 3.** This contradicts B being odd: an even number is divisible into two equal parts, while an odd number is not. Therefore C is not even, and hence is odd. Thus, if an odd number is subtracted from an even number, the remainder is odd. [D7.6, D7.7]

**USED:** 9.24, D7.6, D7.7
**Human refs (from References field):** 9.24, D7.7
**Jaccard:** 0.667 — AI adds ['D7.6']

## Proposition 9.26
**Statement:** If from an odd number an odd number be subtracted, the remainder will be even.

**Step 1.** Let A and B be odd numbers, with B less than A, and let R be the remainder, so A = B + R. We take the direct route of removing one unit from each odd number, reducing the question to subtraction of even numbers. Set E = A − 1 and F = B − 1; E and F are even by the definition of an odd number. [D7.7]

**Step 2.** Subtract one unit from both sides of A = B + R. Since equal quantities leave equal remainders when equals are subtracted, E = F + R. Thus R is precisely the remainder when the even number F is subtracted from the even number E. [CN3]

**Step 3.** If an even number is subtracted from an even number, the remainder is even. Hence R is even. Therefore, if an odd number is subtracted from an odd number, the remainder is even. [9.24]

**USED:** 9.24, CN3, D7.7
**Human refs (from References field):** 9.24, D7.7
**Jaccard:** 0.667 — AI adds ['CN3']

## Proposition 9.27
**Statement:** If from an odd number an even number be subtracted, the remainder will be odd.

**Step 1.** Let A be the given odd number, B the even number subtracted from it, and R the remainder, so that A = B + R. By the definitions, A is not divisible into two equal parts, whereas B is divisible into two equal parts. [D7.6, D7.7]

**Step 2.** Use the even-sum proposition, since adding B to the remainder reconstructs A. Suppose R were divisible into two equal parts. Then R would be even, and the sum B + R would be even by 9.21. Thus A would be divisible into two equal parts, contradicting Step 1. [D7.6, 9.21]

**Step 3.** Therefore R is not divisible into two equal parts and hence is odd. Thus, if an even number is subtracted from an odd number, the remainder is odd. [D7.7]

**USED:** 9.21, D7.6, D7.7
**Human refs (from References field):** 9.24, D7.7
**Jaccard:** 0.250 — AI adds ['9.21', 'D7.6']; Human adds ['9.24']

## Proposition 9.28
**Statement:** If an odd number by multiplying an even number make some number, the product will be even.

**Step 1.** Let an odd number A multiply an even number B to produce C. Choose the direct repeated-addition route: by the definition of multiplication, C is the sum of as many copies of B as there are units in A. Thus C is a sum of even numbers. [D7.15]

**Step 2.** The sum of any multitude of even numbers is even. Therefore C is even, as required. [9.21]

**USED:** 9.21, D7.15
**Human refs (from References field):** 9.21, D7.15
**Jaccard:** 1.000 — Perfect match.

## Proposition 9.29
**Statement:** If an odd number by multiplying an odd number make some number, the product will be odd.

**Step 1.** Let the odd number A multiply the odd number B, producing C. By the definition of multiplication, C is the sum of as many copies of B as there are units in A. We use this direct repeated-addition route because it puts the product immediately in the form of a sum of odd numbers. [D7.15]

**Step 2.** Every summand is B and hence odd; their multitude is A and hence also odd. A sum of an odd multitude of odd numbers is odd. Therefore C is odd, as required. [9.23]

**USED:** 9.23, D7.15
**Human refs (from References field):** 9.23, D7.15
**Jaccard:** 1.000 — Perfect match.

## Proposition 9.30
**Statement:** If an odd number measure an even number, it will also measure the half of it.

**Step 1.** Let the odd number A measure the even number B. Then B consists of q copies of A; that is, q multiplying A produces B. The multiplier q is not the unit, since otherwise B=A, whereas an even number cannot be odd. [D7.5, D7.15, D7.6, D7.7]

**Step 2.** Take the direct parity route, applying 9.29 to the multiplier and the given odd measure. If q were odd, then q multiplying the odd number A would produce an odd number. But its product B is even, a contradiction. Therefore q is not odd and so is divisible into two equal parts: q is even. [9.29, D7.7, D7.6]

**Step 3.** Divide the q copies of A constituting B into two groups, each containing half as many copies. The sums of these groups are equal, since each is formed by adding the same number of copies of A. Call either sum C. Thus B consists of the two equal parts C and C, so C is half of B. Moreover, A measures C, since C consists of whole copies of A; if a group contains just one copy, C=A and A measures it once. Hence A measures the half of B, as required. [D7.6, D7.15, CN2, D7.5]

**USED:** 9.29, CN2, D7.15, D7.5, D7.6, D7.7
**Human refs (from References field):** 9.23
**Jaccard:** 0.000 — AI adds ['9.29', 'CN2', 'D7.15', 'D7.5', 'D7.6', 'D7.7']; Human adds ['9.23']

## Proposition 9.31
**Statement:** If an odd number be prime to any number, it will also be prime to the double of it.

**Step 1.** Let A be an odd number prime to B, and let C=B+B be the double of B. Thus C is even, with half B [D7.6], and A and B have no common measure other than the unit [D7.12]. We use the half-measure theorem [9.30], since it applies directly to C and its half B.

**Step 2.** Let d be any number greater than the unit measuring both A and C. If d were even, A would be even: either A=d, or A is a sum of copies of the even number d, and such a sum is even [9.21]. This contradicts the oddness of A. Hence d is odd [D7.6, D7.7].

**Step 3.** Since the odd number d measures the even number C, it also measures its half B [9.30]. Therefore d measures both A and B, contrary to their being prime to one another [D7.12].

**Step 4.** Consequently no number greater than the unit measures both A and C. They are therefore prime to one another [D7.12]. Thus an odd number prime to any number is also prime to its double.

**USED:** 9.21, 9.30, D7.12, D7.6, D7.7
**Human refs (from References field):** 9.30
**Jaccard:** 0.200 — AI adds ['9.21', 'D7.12', 'D7.6', 'D7.7']

## Proposition 9.32
**Statement:** Each of the numbers which are continually doubled beginning from a dyad is even-times even only.

**Step 1.** Let a₀ be the dyad, and let a₁, a₂, …, aᵣ be obtained by successively doubling it, where r ≥ 1. Thus a₀ is the starting value and a₁, …, aᵣ are the numbers obtained by doubling. The dyad is even, since it divides into two units; each subsequent number is even, since it divides into two equal copies of its predecessor. [D7.6]

**Step 2.** Put N = aᵣ. Its half aᵣ₋₁ is even by Step 1, and this half measures N twice. Therefore an even number measures N according to the even number two, so N is even-times even. [D7.8]

**Step 3.** We use direct repeated halving, since it follows the given doubling chain. Suppose an odd number q measures N. By IX.30, q also measures its half aᵣ₋₁. Repeating the same argument down the chain, q measures a₀, the dyad. Applying IX.30 once more, q measures the unit. But a number is a multitude of units, and no positive number of repetitions of such a multitude can produce a single unit. This is impossible. Hence no odd number measures N. [9.30, D7.2, D7.15]

**Step 4.** If N were even-times odd, an even number e would measure it according to an odd number o; thus o copies of e would produce N. By commutativity of multiplication, e copies of o would also produce N, so the odd number o would measure N, contrary to Step 3. Therefore N is not even-times odd. Since it is even-times even by Step 2, it is even-times even only. As N was any number obtained by continually doubling the initial dyad, the proposition follows. [D7.9, D7.15, 7.16, D7.8]

**USED:** 7.16, 9.30, D7.15, D7.2, D7.6, D7.8, D7.9
**Human refs (from References field):** 9.13, D7.8
**Jaccard:** 0.125 — AI adds ['7.16', '9.30', 'D7.15', 'D7.2', 'D7.6', 'D7.9']; Human adds ['9.13']

## Proposition 9.33
**Statement:** If a number have its half odd, it is even-times odd only.

**Step 1.** Let N be a number whose half H is odd. Thus N is twice H. By commutativity of multiplication, N is also the dyad taken H times. Since the dyad is even and H is odd, N is measured by an even number according to an odd number: it is even-times odd. [D7.6, D7.15, 7.16, D7.9]

**Step 2.** To prove “only,” we directly exclude an even-times-even expression; this route uses the given half without classifying the divisors of N. Suppose, contrary to the assertion, that N is measured by an even number E according to an even number K. Then N consists of K copies of E. Because K is even, divide these copies into two groups containing equally many copies. The groups have equal sums, so the sum of each is the half H of N. [D7.8, D7.15, D7.6]

**Step 3.** Each such group consists entirely of even numbers E. Its sum is therefore even by 9.21; if the group contains just one copy, its sum is E itself and is already even. Hence H is even, contrary to its being odd. Thus N cannot be even-times even. Since it is even-times odd by Step 1, it is even-times odd only. [9.21, D7.7, D7.8, D7.9]

**USED:** 7.16, 9.21, D7.15, D7.6, D7.7, D7.8, D7.9
**Human refs (from References field):** D7.8, D7.9
**Jaccard:** 0.286 — AI adds ['7.16', '9.21', 'D7.15', 'D7.6', 'D7.7']

## Proposition 9.34
**Statement:** If a number neither be one of those which are continually doubled from a dyad, nor have its half odd, it is both even-times even and even-times odd.

**Step 1.** Let A be the given number and H its numerical half. By hypothesis H is not odd, so it is even. The dyad therefore measures A according to the even number H. Hence A is even-times even. [D7.6, D7.7, D7.8]

**Step 2.** For the second classification, use successive halving—the direct reverse of the doubling specified in the hypothesis. Starting with A, halve each even term until an odd number or the unit is reached. This process must terminate, since each halving strictly decreases the finite multitude of units. It cannot terminate at the unit: reversing such a chain would make A the dyad or one of its successive doubles, contrary to the hypothesis. Thus it terminates at an odd number Q. [D7.2, D7.6, D7.7]

**Step 3.** Let r be the number of halvings, and let D be obtained by doubling the unit r times. Reversing the halving chain shows that A is the sum of D copies of Q: each reversal doubles the number of copies. Thus D multiplying Q produces A. Moreover, D is even, since its last construction is a doubling. [D7.15, D7.6]

**Step 4.** Interchange these two factors by VII.16: Q multiplying D also produces A. Thus the even number D measures A according to the odd number Q, so A is even-times odd. Together with Step 1, this proves that A is both even-times even and even-times odd. [7.16, D7.15, D7.9, D7.8]

**USED:** 7.16, D7.15, D7.2, D7.6, D7.7, D7.8, D7.9
**Human refs (from References field):** D7.8
**Jaccard:** 0.143 — AI adds ['7.16', 'D7.15', 'D7.2', 'D7.6', 'D7.7', 'D7.9']

## Proposition 9.35
**Statement:** If as many numbers as we please be in continued proportion, and there be subtracted from the second and the last numbers equal to the first, then, as the excess of the second is to the first, so will the excess of the last be to all those before it.

**Step 1.** Let the given numbers in continued proportion be a₁, a₂, …, aₙ, and denote the stated excesses by d = a₂ − a₁ and e = aₙ − a₁. Put
S = a₁ + a₂ + ⋯ + aₙ₋₁,
T = a₂ + a₃ + ⋯ + aₙ.
Since aₙ = a₁ + e, adding the common intermediate terms gives T = S + e. Thus T − S = e. When n = 2, this is the original equality itself. [CN2]

**Step 2.** We use the numerical sum-of-proportions theorem first, since these two shifted sums differ by precisely the last excess. Continued proportion gives
a₁ : a₂ = a₂ : a₃ = ⋯ = aₙ₋₁ : aₙ.
Therefore, by VII.12,
a₁ : a₂ = S : T.
Alternating by VII.13 gives
a₁ : S = a₂ : T. [7.12, 7.13]

**Step 3.** From the wholes a₂ and T subtract a₁ and S respectively. By Step 2, the wholes have the same ratio as the numbers subtracted. Hence VII.11 gives
(a₂ − a₁) : (T − S) = a₂ : T = a₁ : S.
Using Step 1, this is d : e = a₁ : S. [7.11]

**Step 4.** Alternating this last proportion yields d : a₁ = e : S. Consequently,
(a₂ − a₁) : a₁ = (aₙ − a₁) : (a₁ + a₂ + ⋯ + aₙ₋₁).
Thus the excess of the second is to the first as the excess of the last is to all the numbers before it, as required. [7.13]

**USED:** 7.11, 7.12, 7.13, CN2
**Human refs (from References field):** 7.11, 7.12, 7.13
**Jaccard:** 0.750 — AI adds ['CN2']

## Proposition 9.36
**Statement:** If as many numbers as we please beginning from an unit be set out continuously in double proportion, until the sum of all becomes prime, and if the sum multiplied into the last make some number, the product will be perfect.

**Step 1.** Write the given progression as
\[
1,2,2^2,\ldots,2^n,
\]
where powers denote repeated doubling. Put \(L=2^n\), let \(p=1+2+\cdots+2^n\) be the given prime sum, and let \(N=pL\). Since the unit is not a number, the prime sum requires \(n\geq1\). Also, \(2\) is prime, since its only smaller measure is the unit, and \(p>L\). [D7.2, D7.11, D7.15]

**Step 2.** Doubling the sum gives
\[
2p=2+2^2+\cdots+2^n+2L.
\]
The terms from \(2\) through \(2^n\) sum to \(p-1\); hence \(2p=p-1+2L\). Subtracting equal quantities therefore gives
\[
p=2L-1,\qquad 1+2+\cdots+2^{n-1}=p-L=L-1.
\]
This obtains the needed sum directly by shifting the given doubling progression. [D7.15, CN3]

**Step 3.** Every entry in the following two lists is a proper measure, and therefore a part, of \(N\):
\[
1,2,\ldots,2^n;
\qquad
p,2p,\ldots,2^{n-1}p.
\]
Indeed, the complementary factors are respectively \(p2^{n-j}\), for \(0\leq j\leq n\), and \(2^{n-j}\), for \(0\leq j<n\); these are all greater than the unit. Each list is strictly increasing, and the lists are disjoint because every entry in the first is at most \(L\), whereas every entry in the second is at least \(p>L\). [D7.3, D7.15]

**Step 4.** We show that there are no other parts. The direct route is to use IX.13 for the measures of \(L\), and VII.30 to pass from \(L\) to \(pL\); no general prime-factor decomposition is needed.

Let \(d\) be any proper measure of \(N\) other than the unit. Write \(dq=N=pL\), with \(d,q>1\). Since the prime \(p\) measures \(dq\), VII.30 says that it measures \(d\) or \(q\).

If \(d=pe\), cancellation in \(peq=pL\) gives \(eq=L\). Thus \(e\) is the unit or a measure of \(L\). By IX.13, applied to the progression beginning with the unit whose next term is the prime \(2\), \(e=2^j\) for some \(0\leq j\leq n\). Since \(d<N\), actually \(j<n\), so \(d=p2^j\) belongs to the second list.

If \(q=pe\), the same cancellation gives \(de=L\). IX.13 then gives \(d=2^j\) for some \(0\leq j\leq n\), placing \(d\) in the first list. These product rearrangements and cancellations express multiplication as repeated addition, with factors interchangeable by VII.16. The unit was already listed. Hence Step 3 lists every part exactly once. [7.30, 9.13, 7.16, D7.15, D7.3]

**Step 5.** Consequently, the sum of all the parts of \(N\) is
\[
(1+2+\cdots+2^n)+p(1+2+\cdots+2^{n-1})
=p+p(L-1)=pL=N.
\]
Here multiplication collects the repeated additions, and Step 2 supplies the second sum. Thus \(N\) is equal to the sum of its own parts and is therefore perfect. [D7.15, D7.22]

**USED:** 7.16, 7.30, 9.13, CN3, D7.11, D7.15, D7.2, D7.22, D7.3
**Human refs (from References field):** 7.14, 7.19, 7.20, 7.21, 7.29, 9.13, 9.35, D7.20, D7.22
**Jaccard:** 0.125 — AI adds ['7.16', '7.30', 'CN3', 'D7.11', 'D7.15', 'D7.2', 'D7.3']; Human adds ['7.14', '7.19', '7.20', '7.21', '7.29', '9.35', 'D7.20']
