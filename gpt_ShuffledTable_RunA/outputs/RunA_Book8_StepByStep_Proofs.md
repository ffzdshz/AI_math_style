# Book 8 of Euclid's Elements — Step-by-Step AI Proofs (Run A)

## Proposition 8.1
**Statement:** If there be as many numbers as we please in continued proportion, and the extremes of them be prime to one another, the numbers are the least of those which have the same ratio with them.

**Step 1.** Let A₁, A₂, …, Aₙ be the given numbers in continued proportion, with A₁ and Aₙ prime to one another. Let B₁, B₂, …, Bₙ be any numbers having the same successive ratios. We take the direct route through the extremes, using the numerical ex aequali theorem: since Aᵢ : Aᵢ₊₁ = Bᵢ : Bᵢ₊₁ for every successive pair, A₁ : Aₙ = B₁ : Bₙ. [7.14]

**Step 2.** Because A₁ and Aₙ are prime to one another, they are the least numbers having their ratio. This is precisely the coprime-to-least implication needed here. Consequently B₁ ≥ A₁. [7.21]

**Step 3.** For each i with 2 ≤ i ≤ n, applying ex aequali to the corresponding initial portions gives A₁ : Aᵢ = B₁ : Bᵢ (for i = 2 this is already given). Hence A₁Bᵢ = AᵢB₁. Since B₁ ≥ A₁, we obtain A₁Bᵢ ≥ AᵢA₁; as A₁ is positive, Bᵢ ≥ Aᵢ. Together with Step 2, every term of any such sequence is at least the corresponding given term. Therefore the given numbers are the least of those which have the same ratio with them. [7.14, 7.19]

**USED:** 7.14, 7.19, 7.21
**Human refs (from References field):** 7.14, 7.20, 7.21
**Jaccard:** 0.500 — AI adds ['7.19']; Human adds ['7.20']

## Proposition 8.2
**Statement:** To find numbers in continued proportion, as many as may be prescribed, and the least that are in a given ratio.

**Step 1.** Let the given ratio be A:B, and let n ≥ 2 be the prescribed number of terms. We shall first construct n numbers in continued proportion with this ratio, and then apply VII.33 to the whole list. This is the direct choice for minimality, since VII.33 already constructs the least numbers having the ratios of any given list. [7.33]

**Step 2.** Begin with the list A, B. Suppose that a list X₁, …, Xₖ has been constructed in which every successive ratio is A:B. Form the k+1 numbers
A·X₁, A·X₂, …, A·Xₖ, B·Xₖ.
These products are constructed by multiplication. For every i < k, VII.17 gives
(A·Xᵢ):(A·Xᵢ₊₁) = Xᵢ:Xᵢ₊₁ = A:B.
For the final pair, VII.18 gives
(A·Xₖ):(B·Xₖ) = A:B,
since A and B multiply the same number Xₖ. Thus the new list also has every successive ratio equal to the given ratio. [D7.15, 7.17, 7.18, 5.11]

**Step 3.** Each repetition of Step 2 adds exactly one term while preserving the required continued proportion. Starting with A, B and repeating the construction n−2 times therefore produces a list C₁, …, Cₙ of exactly n numbers in continued proportion with successive ratio A:B. [7.17, 7.18, 5.11]

**Step 4.** Apply VII.33 to C₁, …, Cₙ, obtaining the least numbers L₁, …, Lₙ having the same ratios as that list. Consequently, for every i < n,
Lᵢ:Lᵢ₊₁ = Cᵢ:Cᵢ₊₁ = A:B.
Hence these least numbers are themselves in the required continued proportion. Moreover, any other list of n numbers with successive ratio A:B has the same successive ratios as C₁, …, Cₙ, and so belongs to the very class for which VII.33 supplies the least numbers. Therefore L₁, …, Lₙ are the least numbers in continued proportion with the given ratio, and their number is exactly that prescribed. This completes the construction. [7.33, 5.11]

**USED:** 5.11, 7.17, 7.18, 7.33, D7.15
**Human refs (from References field):** 7.17, 7.18, 7.22, 7.27, 8.1
**Jaccard:** 0.250 — AI adds ['5.11', '7.33', 'D7.15']; Human adds ['7.22', '7.27', '8.1']

## Proposition 8.3
**Statement:** If as many numbers as we please in continued proportion be the least of those which have the same ratio with them, the extremes of them are prime to one another.

**Step 1.** Let A₀, A₁, …, Aₙ (n ≥ 1) be the given numbers in continued proportion, least among lists of the same length having their common ratio. By VII.33 choose the least pair a, b such that a:b = A₀:A₁. By VII.22, a and b are prime to one another. We use this least pair to construct a progression whose extremes are powers; this allows VII.27 to establish their coprimality directly. [7.33, 7.22]

**Step 2.** Form the list
B₀ = aⁿ, B₁ = aⁿ⁻¹b, …, Bᵢ = aⁿ⁻ⁱbⁱ, …, Bₙ = bⁿ,
where a zero exponent means that the corresponding factor is omitted. For each i < n, the adjacent terms Bᵢ and Bᵢ₊₁ are obtained by multiplying a and b by the same factor aⁿ⁻ⁱ⁻¹bⁱ. Hence VII.17 gives Bᵢ:Bᵢ₊₁ = a:b. If that factor is the unit, this equality is immediate. Thus the B-list is in continued proportion with precisely the same common ratio as the A-list. [7.17]

**Step 3.** Since a and b are prime to one another, their equal powers aⁿ and bⁿ are prime to one another by VII.27. For n = 1 this is the coprimality already obtained in Step 1. Therefore the extremes B₀ and Bₙ are prime to one another. [7.27, 7.22]

**Step 4.** By VIII.1, the B-list is consequently the least among lists having this common ratio. The A-list is also least by hypothesis. Their corresponding terms must therefore be equal: leastness of the A-list gives Aᵢ ≤ Bᵢ, and leastness of the B-list gives Bᵢ ≤ Aᵢ. In particular, A₀ = B₀ and Aₙ = Bₙ. Since B₀ and Bₙ are prime to one another, so are A₀ and Aₙ. Thus the extremes of the given least continued proportion are prime to one another. [8.1; Step 3]

**USED:** 7.17, 7.22, 7.27, 7.33, 8.1
**Human refs (from References field):** 7.22, 7.27, 7.33, 8.2
**Jaccard:** 0.500 — AI adds ['7.17', '8.1']; Human adds ['8.2']

## Proposition 8.4
**Statement:** Given as many ratios as we please in least numbers, to find numbers in continued proportion which are the least in the given ratios.

**Step 1.** Let the prescribed ratios, given in least numbers, be a₁:b₁, a₂:b₂, …, aₙ:bₙ. We choose the direct route of first constructing a list with these successive ratios and then making the entire list least by VII.33. That proposition is suited to this route because it applies to any finite list of numbers. [7.33]

**Step 2.** Begin with the list a₁, b₁. Suppose a list x₀, …, xₖ has already been constructed with the first k prescribed successive ratios. To incorporate aₖ₊₁:bₖ₊₁, let pᵢ be the number produced by aₖ₊₁ multiplying xᵢ, for each i from 0 to k; and let q be the number produced by bₖ₊₁ multiplying xₖ. Since the same number multiplies each preceding pair, VII.17 gives
pᵢ₋₁:pᵢ = xᵢ₋₁:xᵢ = aᵢ:bᵢ.
Moreover, since aₖ₊₁ and bₖ₊₁ multiply the same number xₖ, VII.18 gives
pₖ:q = aₖ₊₁:bₖ₊₁.
Thus p₀, …, pₖ, q realizes the first k+1 prescribed ratios. [7.17, 7.18]

**Step 3.** Repeat this construction until all n ratios have been incorporated. It produces numbers z₀, …, zₙ satisfying
zᵢ₋₁:zᵢ = aᵢ:bᵢ for every i = 1, …, n.
Each extension preserves every ratio already obtained and adds the next prescribed ratio, as just established. [7.17, 7.18]

**Step 4.** Apply VII.33 to z₀, …, zₙ, obtaining numbers y₀, …, yₙ which are the least of those having the same ratios with them. In particular,
yᵢ₋₁:yᵢ = zᵢ₋₁:zᵢ = aᵢ:bᵢ.
Hence the resulting numbers realize all the prescribed successive ratios. [7.33]

**Step 5.** To verify leastness among all lists realizing the prescribed ratios, let w₀, …, wₙ be any other such list. Its successive ratios equal those of z₀, …, zₙ. Applying the numerical ex-aequali proposition VII.14 to any corresponding consecutive portions of these lists gives wᵢ:wⱼ = zᵢ:zⱼ whenever i < j. Thus this competing list belongs to precisely the class of lists for which VII.33 made y₀, …, yₙ least. Therefore the constructed numbers are least among all numbers in continued proportion in the given sequence of ratios, as required. Every cited proposition is from Book VII and therefore precedes VIII.4. [7.14, 7.33]

**USED:** 7.14, 7.17, 7.18, 7.33
**Human refs (from References field):** 7.13, 7.20, 7.34, 7.35, D7.20
**Jaccard:** 0.000 — AI adds ['7.14', '7.17', '7.18', '7.33']; Human adds ['7.13', '7.20', '7.34', '7.35', 'D7.20']

## Proposition 8.5
**Statement:** Plane numbers have to one another the ratio compounded of the ratios of their sides.

**Step 1.** Let A and B be any plane numbers, with sides a, b and c, d respectively. Thus A = ab and B = cd, by the definition of a plane number. [D7.16]

**Step 2.** Choose the direct common-side route: form the intermediate number C = cb. Since a and c, multiplying the same number b, produce A and C, the products have the ratio of their multipliers. Therefore A:C = a:c. [D7.15, 7.18]

**Step 3.** Since the same number c, multiplying b and d, produces C and B, the products have the ratio of the numbers multiplied. Therefore C:B = b:d. [7.17]

**Step 4.** The sizes of the ratios A:C and C:B multiply to the size of A:B, since (A/C)(C/B) = A/B. Hence A:B is, by definition, compounded of A:C and C:B. Substituting the equal ratios established in Steps 2 and 3, A:B is compounded of a:c and b:d. Therefore plane numbers have to one another the ratio compounded of the ratios of their sides. [D6.5]

**USED:** 7.17, 7.18, D6.5, D7.15, D7.16
**Human refs (from References field):** 7.14, 7.17, 8.4
**Jaccard:** 0.143 — AI adds ['7.18', 'D6.5', 'D7.15', 'D7.16']; Human adds ['7.14', '8.4']

## Proposition 8.6
**Statement:** If there be as many numbers as we please in continued proportion, and the first do not measure the second, neither will any other measure any other.

**Step 1.** Let A₀, A₁, …, Aₙ be in continued proportion, and suppose A₀ does not measure A₁. Choose any indices i<j and put d=j−i. Use the least-progression route: construct d+1 numbers B₀, B₁, …, B_d in continued proportion, least among those having the common ratio A₀:A₁. This construction is supplied by VIII.2. [8.2]

**Step 2.** Since B₀:B₁=A₀:A₁, B₀ cannot measure B₁: otherwise B₀ would be a part of B₁, and proportionality would make A₀ the same part of A₁, contrary to the hypothesis. In particular, B₀ is not a unit, since a unit measures every number. [D7.3, D7.20, D7.2]

**Step 3.** VIII.3 applies directly to the least progression and shows that its extremes B₀ and B_d are prime to one another. Consequently B₀ cannot measure B_d: if it did, B₀ would be a common measure of both extremes other than the unit, contrary to their being prime to one another. [8.3, D7.12]

**Step 4.** The progressions A_i, A_{i+1}, …, A_j and B₀, B₁, …, B_d have the same successive ratios. Therefore A_i:A_j=B₀:B_d, directly when d=1 and ex aequali otherwise. If A_i measured A_j, proportionality would make B₀ the same part of B_d, contradicting Step 3. Thus A_i does not measure A_j. Since i<j were arbitrary, no term measures any following term: neither will any other measure any other in the continued proportion. [7.14, D7.3, D7.20]

**USED:** 7.14, 8.2, 8.3, D7.12, D7.2, D7.20, D7.3
**Human refs (from References field):** 7.14, 7.33, 8.3, D7.20
**Jaccard:** 0.375 — AI adds ['8.2', 'D7.12', 'D7.2', 'D7.3']; Human adds ['7.33']

## Proposition 8.7
**Statement:** If there be as many numbers as we please in continued proportion, and the first measure the last, it will measure the second also.

**Step 1.** Let A₁, A₂, …, Aₙ be numbers in continued proportion, and suppose that A₁ measures Aₙ. We use Proposition 8.6 by contraposition, since it directly connects failure of the first to measure the second with failure of divisibility elsewhere in the progression. [8.6]

**Step 2.** If A₁ did not measure A₂, Proposition 8.6 would imply that no number in the progression measures another; in particular, A₁ would not measure Aₙ. This contradicts the hypothesis. Therefore A₁ measures A₂, as required. [8.6]

**USED:** 8.6
**Human refs (from References field):** 8.6
**Jaccard:** 1.000 — Perfect match.

## Proposition 8.8
**Statement:** If between two numbers there fall numbers in continued proportion with them, then, however many numbers fall between them in continued proportion, so many will also fall in continued proportion between the numbers which have the same ratio with the original numbers.

**Step 1.** Let A₀, A₁, …, Aₙ₊₁ be in continued proportion, so that n numbers fall between A₀ and Aₙ₊₁. Let B and C satisfy B:C = A₀:Aₙ₊₁. We use the least-progression route: by VIII.2, take the least numbers P₀, P₁, …, Pₙ₊₁ in continued proportion, equal in multitude to the given numbers and having their common successive ratio. [8.2]

**Step 2.** The two progressions have equal corresponding successive ratios. Therefore, ex aequali, P₀:Pₙ₊₁ = A₀:Aₙ₊₁. Since B:C also equals A₀:Aₙ₊₁, it follows that P₀:Pₙ₊₁ = B:C. [7.14, 5.11]

**Step 3.** Because P₀, P₁, …, Pₙ₊₁ form the least progression in their ratio, their extremes P₀ and Pₙ₊₁ are prime to one another. Numbers prime to one another are the least numbers having their ratio; hence P₀ and Pₙ₊₁ are the least pair in the ratio B:C. [8.3, 7.21]

**Step 4.** The least numbers in a ratio measure any numbers having that ratio the same number of times. Consequently, there is a common positive integral multiplicity k such that B = kP₀ and C = kPₙ₊₁. [7.20]

**Step 5.** If k is one, the progression P₀, P₁, …, Pₙ₊₁ itself has extremes B and C. Otherwise multiply every term by k. By VII.17—the applicable multiplication result because one common multiplier acts on all the terms—we have, for every i from 0 through n,
(kPᵢ):(kPᵢ₊₁) = Pᵢ:Pᵢ₊₁.
These successive ratios are therefore all equal. Thus B, kP₁, …, kPₙ, C are in continued proportion, with exactly n intermediate numbers. Hence however many numbers fall in continued proportion between the original numbers, so many also fall between any numbers having the same ratio. [7.17, 5.11]

**USED:** 5.11, 7.14, 7.17, 7.20, 7.21, 8.2, 8.3
**Human refs (from References field):** 7.14, 7.20, 7.21, 7.33, 8.3, D7.20
**Jaccard:** 0.444 — AI adds ['5.11', '7.17', '8.2']; Human adds ['7.33', 'D7.20']

## Proposition 8.9
**Statement:** If two numbers be prime to one another, and numbers fall between them in continued proportion, then, however many numbers fall between them in continued proportion, so many will also fall between each of them and an unit in continued proportion.

**Step 1.** Let the given continued proportion be
A₀, A₁, …, Aₙ,
where A₀ and Aₙ are prime to one another and there are n−1 intervening numbers. By VIII.1, this progression is the least of those having the same ratio. We use the direct route of comparing least progressions, since the given coprime extremes immediately supply the hypothesis of VIII.1. [8.1]

**Step 2.** Find the least pair p, q having the ratio A₀:A₁, by VII.33. Then p and q are prime to one another, by VII.22. Neither can be a unit: otherwise, by the definition of numerical proportion, every term in one direction along the given progression would be an integral multiple of its predecessor. One extreme would consequently measure the other, contradicting their being prime to one another. Thus p and q are numbers greater than the unit. [7.33, 7.22, D7.20, D7.12]

**Step 3.** Write powers for repeated multiplication, and form the n+1 numbers
Bᵢ = p^(n−i)q^i, for i = 0, …, n,
with a zeroth power denoting the unit. Thus the progression is
p^n, p^(n−1)q, …, pq^(n−1), q^n.
For each i<n, its adjacent terms are obtained by multiplying p and q by the same number p^(n−i−1)q^i; the product identities follow from repeated multiplication and commutativity. Hence VII.17 gives Bᵢ:Bᵢ₊₁ = p:q. This is therefore a continued proportion with the same number of terms and the same consecutive ratio as the given progression. [D7.15, 7.16, 7.17]

**Step 4.** Since p and q are prime to one another, their corresponding powers p^n and q^n are prime to one another by VII.27. Consequently the progression B₀, …, Bₙ is also least, by VIII.1. The two progressions are least among the same collection of progressions of this length and ratio. Thus each corresponding term of either is no greater than the other, so they are equal term by term. In particular,
A₀ = p^n and Aₙ = q^n. [7.27, 8.1]

**Step 5.** Now place between the unit and A₀ the numbers
p, p², …, p^(n−1),
and between the unit and Aₙ the numbers
q, q², …, q^(n−1).
In each list, including its endpoints, every term after the first is the same multiple of its predecessor. Each list is therefore in continued proportion, by the definitions of multiplication and numerical proportion. Each contains exactly n−1 intervening numbers, the same number as in the original progression. Hence, however many numbers fall between the given coprime numbers in continued proportion, so many also fall between each of them and the unit in continued proportion. [D7.15, D7.20]

**USED:** 7.16, 7.17, 7.22, 7.27, 7.33, 8.1, D7.12, D7.15, D7.20
**Human refs (from References field):** 8.1, 8.2, D7.20
**Jaccard:** 0.200 — AI adds ['7.16', '7.17', '7.22', '7.27', '7.33', 'D7.12', 'D7.15']; Human adds ['8.2']

## Proposition 8.10
**Statement:** If numbers fall between each of two numbers and an unit in continued proportion, however many numbers fall between each of them and an unit in continued proportion, so many also will fall between the numbers themselves in continued proportion.

**Step 1.** Let the two given continued proportions be
\[
1=u_0,u_1,\ldots,u_n=A,
\qquad
1=v_0,v_1,\ldots,v_n=B,
\]
so that each contains \(n-1\) numbers between the unit and its last term. Put \(a=u_1\) and \(b=v_1\). Since \(u_i:u_{i+1}=1:a\), each \(u_i\) is the same part of \(u_{i+1}\) that the unit is of \(a\); hence \(u_{i+1}=a u_i\). Likewise, \(v_{i+1}=b v_i\), for \(0\le i<n\). [D7.20, D7.15]

**Step 2.** Use a direct mixed-product construction, since the given progressions already supply the required integer multipliers. For \(0\le i\le n\), form
\[
C_i=u_{n-i}v_i.
\]
Here a product with the unit means the other factor itself, as follows from multiplication by repeated addition. Thus \(C_0=A\) and \(C_n=B\). [D7.15]

**Step 3.** For every \(0\le i<n\), the relations in Step 1 give
\[
\begin{aligned}
bC_i
 &=u_{n-i}(bv_i)\\
 &=u_{n-i}v_{i+1}\\
 &=(a u_{n-i-1})v_{i+1}\\
 &=aC_{i+1}.
\end{aligned}
\]
Regrouping these repeated additions uses the definition of multiplication, and interchanging factors uses VII.16. The product of \(C_i\) and \(b\) therefore equals the product of \(C_{i+1}\) and \(a\); by VII.19,
\[
C_i:C_{i+1}=a:b.
\]
[D7.15, 7.16, 7.19]

**Step 4.** Consequently every successive pair in
\[
A=C_0,\ C_1,\ldots,\ C_{n-1},\ C_n=B
\]
has the same ratio. These numbers are therefore in continued proportion, and precisely \(n-1\) numbers intervene between \(A\) and \(B\), just as between each of them and the unit. This proves the proposition. [D7.20]

**USED:** 7.16, 7.19, D7.15, D7.20
**Human refs (from References field):** 7.17, 7.18, D7.20
**Jaccard:** 0.167 — AI adds ['7.16', '7.19', 'D7.15']; Human adds ['7.17', '7.18']

## Proposition 8.11
**Statement:** Between two square numbers there is one mean proportional number, and the square has to the square the ratio duplicate of that which the side has to the side.

**Step 1.** Let A and B be the two square numbers, with sides a and b respectively. Thus A = a·a and B = b·b. Choose the direct product construction: let M = a·b. This produces a number and will give both the mean proportional and the required side ratio. [D7.18, D7.15]

**Step 2.** The number a, multiplying a and b, produces A and M. Therefore
A:M = a:b.
Here the common-multiplier rule applies directly. [7.17]

**Step 3.** The numbers a and b, each multiplying b, produce M and B. Therefore
M:B = a:b.
Here the common-multiplicand rule applies directly, without needing to reverse either product. [7.18]

**Step 4.** Since A:M and M:B are both the same as a:b, they are the same as one another. Hence
A:M = M:B,
so M is a mean proportional number between A and B. [5.11]

**Step 5.** Since A, M, B are three proportional numbers, A:B is the duplicate ratio of A:M. But A:M = a:b by Step 2. Thus the square A has to the square B the ratio duplicate of that which its side a has to the side b. This proves both assertions. [D5.9]

**USED:** 5.11, 7.17, 7.18, D5.9, D7.15, D7.18
**Human refs (from References field):** 7.17, 7.18, D5.9
**Jaccard:** 0.500 — AI adds ['5.11', 'D7.15', 'D7.18']

## Proposition 8.12
**Statement:** Between two cube numbers there are two mean proportional numbers, and the cube has to the cube the ratio triplicate of that which the side has to the side.

**Step 1.** Let C and D be cube numbers with sides a and b. We use direct multiplication, since it explicitly supplies the required means. Form P = a·a, Q = a·b, and R = b·b, where the first factor is the multiplier. By the definition of a cube, C = a·P and D = b·R. [D7.15, D7.19]

**Step 2.** Since a multiplies a and b to produce P and Q, respectively, P:Q = a:b. Also, since a and b multiply the same number b to produce Q and R, respectively, Q:R = a:b. [7.17, 7.18]

**Step 3.** Form M = a·Q and N = a·R. Multiplying P and Q by a gives C:M = P:Q; multiplying Q and R by a gives M:N = Q:R. Finally, since a and b multiply R to produce N and D, respectively, N:D = a:b. [D7.15, 7.17, 7.18]

**Step 4.** Combining these ratios gives
C:M = M:N = N:D = a:b,
since ratios equal to the same ratio are equal to one another. Therefore M and N are two mean proportional numbers between the cubes C and D. [5.11]

**Step 5.** The four numbers C, M, N, D are continuously proportional. Consequently, C:D is triplicate of C:M. But C:M = a:b, so the cube C has to the cube D the ratio triplicate of that which its side a has to the side b. Thus both assertions are proved. [D5.10]

**USED:** 5.11, 7.17, 7.18, D5.10, D7.15, D7.19
**Human refs (from References field):** 7.17, 7.18, D5.10
**Jaccard:** 0.500 — AI adds ['5.11', 'D7.15', 'D7.19']

## Proposition 8.13
**Statement:** If there be as many numbers as we please in continued proportion, and each by multiplying itself make some number, the products will be proportional; and, if the original numbers by multiplying the products make certain numbers, the latter will also be proportional.

**Step 1.** Let a, b, c be any three consecutive numbers in the given continued proportion. Thus a:b = b:c. Write a² = a·a and a³ = a·a², and similarly for b and c. We take the direct route: preserve ratios by multiplication [7.17, 7.18], then apply ex aequali [7.14], without introducing duplicate or triplicate ratios.

**Step 2.** Put x = a·b and y = b·c. Multiplying a and b by a, and b and c by b, gives

a²:x = a:b = b:c = b²:y. [7.17]

Likewise, taking a and b as multipliers of b, and b and c as multipliers of c, gives

x:b² = a:b = b:c = y:c². [7.18]

**Step 3.** The two triples a², x, b² and b², y, c² therefore have their corresponding successive ratios equal. Hence, ex aequali,

a²:b² = b²:c². [7.14]

Thus the squares of any three consecutive original numbers are in continued proportion.

**Step 4.** Put s = a·b² and t = b·c². Multiplying a² and b² by a, and b² and c² by b, gives

a³:s = a²:b²,     b³:t = b²:c². [7.17]

These ratios are equal by Step 3. Also, taking a and b as multipliers of b², and b and c as multipliers of c², gives

s:b³ = a:b = b:c = t:c³. [7.18]

**Step 5.** The two triples a³, s, b³ and b³, t, c³ consequently have their corresponding successive ratios equal. Hence, ex aequali,

a³:b³ = b³:c³. [7.14]

Since a, b, c were any three consecutive original numbers, Step 3 establishes continued proportion throughout the sequence of squares, and this step establishes continued proportion throughout the sequence obtained by multiplying each square by its original number. Therefore both sets of products are proportional, as required.

**USED:** 7.14, 7.17, 7.18
**Human refs (from References field):** 7.14
**Jaccard:** 0.333 — AI adds ['7.17', '7.18']

## Proposition 8.14
**Statement:** If a square measure a square, the side will also measure the side; and, if the side measure the side, the square will also measure the square.

**Step 1.** Let A and B be square numbers with sides a and b, respectively, so that A = a·a and B = b·b. Form the mixed product M = a·b. We use this mixed-product route to obtain explicitly a continued proportion whose successive ratios equal the ratio of the sides. [D7.18, D7.15]

**Step 2.** Since a multiplying a and b produces A and M, respectively, A:M = a:b. Since a and b multiplying b produce M and B, respectively, M:B = a:b. Hence A:M = M:B, so A, M, B are in continued proportion. [7.17, 7.18]

**Step 3.** Suppose A measures B. Applying VIII.7 directly to the continued proportion A, M, B, we obtain that A measures M. But A:M = a:b; therefore a is the same part of b that A is of M, and consequently a measures b. Thus, if a square measures a square, its side measures the other side. [8.7, D7.20, D7.3]

**Step 4.** Conversely, suppose a measures b. From A:M = a:b and M:B = a:b, A measures M and M measures B. Thus M consists of a whole number of copies of A, and B consists of a whole number of copies of M. Replacing each copy of M by its copies of A shows that B consists of a whole number of copies of A; hence A measures B. Therefore, if the side measures the side, the square measures the square. Both assertions are proved. [D7.20, D7.3, D7.15]

**USED:** 7.17, 7.18, 8.7, D7.15, D7.18, D7.20, D7.3
**Human refs (from References field):** 8.11, 8.7, D7.20
**Jaccard:** 0.250 — AI adds ['7.17', '7.18', 'D7.15', 'D7.18', 'D7.3']; Human adds ['8.11']

## Proposition 8.15
**Statement:** If a cube number measure a cube number, the side will also measure the side; and, if the side measure the side, the cube will also measure the cube.

**Step 1.** Let a and b be the sides of the cube numbers A and B, respectively. Thus A = a³ and B = b³ (D7.19). If a = b, both assertions hold immediately, since each number measures itself once. Hence consider unequal sides.

**Step 2.** Put X = a²b and Y = ab². Multiplying a and b successively by a², ab, and b² gives, by VII.17,

A:X = X:Y = Y:B = a:b.

Here products are regrouped according to multiplication as repeated addition and reordered by VII.16 (D7.15, VII.16). Thus A, X, Y, B are in continued proportion. We choose this progression because the assumed divisibility of its extremes is exactly the hypothesis of VIII.7.

**Step 3.** Suppose that A measures B. Since A, X, Y, B are in continued proportion, A measures X by VIII.7. But A:X = a:b, so a is the same part of b that A is of X (D7.20). Therefore a measures b (D7.3). Thus, if a cube measures a cube, its side measures the other side.

**Step 4.** Conversely, suppose that a measures b. From the proportions in Step 2, A is the same part of X, X the same part of Y, and Y the same part of B that a is of b. Consequently A measures X, X measures Y, and Y measures B (D7.20, D7.3).

**Step 5.** Write X = rA, Y = sX, and B = tY, where r, s, and t count the respective repetitions. Substitution gives B = (tsr)A; hence A measures B, by the meaning of multiplication as repeated addition (D7.15). Thus, if the side measures the side, the cube also measures the cube. Both assertions are proved.

**USED:** 7.16, 7.17, 8.7, D7.15, D7.19, D7.20, D7.3
**Human refs (from References field):** 8.11, 8.12, 8.7, D7.20
**Jaccard:** 0.222 — AI adds ['7.16', '7.17', 'D7.15', 'D7.19', 'D7.3']; Human adds ['8.11', '8.12']

## Proposition 8.16
**Statement:** If a square number do not measure a square number, neither will the side measure the side; and, if the side do not measure the side, neither will the square measure the square.

**Step 1.** Let A and B be square numbers, with respective sides a and b. We use VIII.14 directly by contradiction, since its two implications are precisely the positive assertions corresponding to the claims here. Suppose A does not measure B. If a measured b, then A would measure B by VIII.14, contrary to the supposition. Therefore a does not measure b. [8.14]

**Step 2.** Conversely, suppose a does not measure b. If A measured B, then a would measure b by VIII.14, contrary to the supposition. Therefore A does not measure B. Thus, if a square does not measure a square, neither does its side measure the other side; and if the side does not measure the side, neither does the square measure the square. [8.14]

**USED:** 8.14
**Human refs (from References field):** 8.14
**Jaccard:** 1.000 — Perfect match.

## Proposition 8.17
**Statement:** If a cube number do not measure a cube number, neither will the side measure the side; and, if the side do not measure the side, neither will the cube measure the cube.

**Step 1.** Let A and B be cube numbers, with respective sides a and b. We use 8.15 directly because it supplies both corresponding positive implications. Suppose A does not measure B. If a measured b, then A would measure B by 8.15, contrary to the supposition. Therefore a does not measure b. [8.15]

**Step 2.** Conversely, suppose a does not measure b. If A measured B, then a would measure b by 8.15, contrary to the supposition. Therefore A does not measure B. Thus both asserted implications hold. [8.15]

**USED:** 8.15
**Human refs (from References field):** 8.15
**Jaccard:** 1.000 — Perfect match.

## Proposition 8.18
**Statement:** Between two similar plane numbers there is one mean proportional number; and the plane number has to the plane number the ratio duplicate of that which the corresponding side has to the corresponding side.

**Step 1.** Let A and B be similar plane numbers. Write A = ab and B = cd, where a, b and c, d are their respective sides, with a corresponding to c and b to d. By similarity, a:b = c:d. [D7.16, D7.21]

**Step 2.** Alternating this proportion gives a:c = b:d. [7.13]

**Step 3.** Choose the direct mixed-product construction M = ad: it allows both comparisons with the proposed mean to use a common factor. Since a multiplying b and d produces A and M, respectively, A:M = b:d. Since a and c multiplying d produce M and B, respectively, M:B = a:c. These are precisely the common-multiplier and common-multiplicand cases. [7.17, 7.18]

**Step 4.** By Step 2, both ratios in Step 3 equal a:c. Therefore A:M = M:B = a:c, and M is a mean proportional number between A and B. [5.11]

**Step 5.** Since A, M, B are proportional, A:B is the duplicate ratio of A:M. But A:M = a:c = b:d. Thus the plane number A has to the plane number B the ratio duplicate of that which either side has to its corresponding side. Hence both assertions are proved. [D5.9]

**USED:** 5.11, 7.13, 7.17, 7.18, D5.9, D7.16, D7.21
**Human refs (from References field):** 7.13, 7.17, D5.9, D7.21
**Jaccard:** 0.571 — AI adds ['5.11', '7.18', 'D7.16']

## Proposition 8.19
**Statement:** Between two similar solid numbers there fall two mean proportional numbers; and the solid number has to the similar solid number the ratio triplicate of that which the corresponding side has to the corresponding side.

**Step 1.** Let A and B be similar solid numbers. By the definitions of solid numbers and similarity, choose corresponding sides a,b,c and d,e,f such that
A=(ab)c,  B=(de)f,  and  a:d=b:e=c:f.
Use the direct mixed-product construction, since it produces the means from the given sides themselves. Put p=ab, q=db, r=de, and form M=qc and N=qf. [D7.17, D7.21]

**Step 2.** Since a and d multiply the same number b, their products satisfy p:q=a:d. Since d multiplies b and e, the resulting products satisfy q:r=b:e. [7.18, 7.17]

**Step 3.** Multiplying p and q by c gives A and M, so A:M=p:q. Multiplying c and f by q gives M and N, so M:N=c:f. Finally, multiplying q and r by f gives N and B, so N:B=q:r. [7.18, 7.17]

**Step 4.** Combining these equalities with the proportionality of the corresponding sides gives
A:M=M:N=N:B=a:d.
Thus M and N are two mean proportional numbers between A and B. [5.11]

**Step 5.** Because A,M,N,B are continuously proportional, A has to B the triplicate ratio of that which A has to M. But A:M=a:d=b:e=c:f. Therefore the solid number A has to the similar solid number B the ratio triplicate of that which any corresponding side has to its corresponding side, as required. [D5.10, 5.11]

**USED:** 5.11, 7.17, 7.18, D5.10, D7.17, D7.21
**Human refs (from References field):** 7.13, 7.17, 7.18, 8.18, D5.10, D7.21
**Jaccard:** 0.500 — AI adds ['5.11', 'D7.17']; Human adds ['7.13', '8.18']

## Proposition 8.20
**Statement:** If one mean proportional number fall between two numbers, the numbers will be similar plane numbers.

**Step 1.** Let B be a mean proportional between the given numbers A and C, so that A:B = B:C. Choose the least terms d,e having the ratio A:B. We use this least-pair route because it directly supplies factorizations of both end numbers. [D7.20, 7.33]

**Step 2.** Since d,e are the least terms in the common ratio of A:B and B:C, they measure each pair the same number of times. Consequently, there are multipliers p,q such that
A = dp,  B = ep,
and
B = dq,  C = eq.
[7.20, D7.15]

**Step 3.** The two expressions for B give dq = ep. These are the products of the first and fourth, and of the second and third, among d,e,p,q. Hence d:e = p:q. [7.19]

**Step 4.** From A = dp and C = eq, the end numbers are plane numbers with respective sides d,p and e,q. By Step 3 their corresponding sides are proportional. Therefore A and C are similar plane numbers, as required. [D7.16, D7.21]

**USED:** 7.19, 7.20, 7.33, D7.15, D7.16, D7.20, D7.21
**Human refs (from References field):** 7.13, 7.17, 7.20, 7.33
**Jaccard:** 0.222 — AI adds ['7.19', 'D7.15', 'D7.16', 'D7.20', 'D7.21']; Human adds ['7.13', '7.17']

## Proposition 8.21
**Statement:** If two mean proportional numbers fall between two numbers, the numbers are similar solid numbers.

**Step 1.** Let B and C be two mean proportional numbers between A and D, so that
A:B = B:C = C:D.
Choose the least numbers p and q having the ratio A:B [7.33]. These are prime to one another [7.22].

**Step 2.** We take the direct product route: matching the common ratio by multiplication supplies the factors needed for solid numbers. Multiplying p and q by p², pq, and q², respectively, gives
p³:p²q = p²q:pq² = pq²:q³ = p:q
[7.17].

**Step 3.** Thus the successive ratios in A, B, C, D equal the corresponding successive ratios in p³, p²q, pq², q³. Taking the ratios ex aequali gives
A:D = p³:q³
[7.14].

**Step 4.** Since p and q are prime to one another, their cubes p³ and q³ are prime to one another [7.27]. Consequently these cubes are the least numbers having their ratio [7.21]. They therefore measure A and D the same number of times [7.20]. For a common integral multiplier k, we have
A = kp³ and D = kq³.

**Step 5.** Accordingly,
A = (kp)·p·p and D = (kq)·q·q.
Thus A and D are solid numbers with respective sides kp, p, p and kq, q, q [D7.17].

**Step 6.** Multiplication by k preserves the ratio, so
kp:kq = p:q [7.17].
The three corresponding pairs of sides therefore have the same ratio. Hence A and D are similar solid numbers [D7.21], as required.

**USED:** 7.14, 7.17, 7.20, 7.21, 7.22, 7.27, 7.33, D7.17, D7.21
**Human refs (from References field):** 7.14, 7.18, 7.20, 7.21, 7.33, 8.2, 8.20, 8.3
**Jaccard:** 0.308 — AI adds ['7.17', '7.22', '7.27', 'D7.17', 'D7.21']; Human adds ['7.18', '8.2', '8.20', '8.3']

## Proposition 8.22
**Statement:** If three numbers be in continued proportion, and the first be square, the third will also be square.

**Step 1.** Let A, B, C be the three numbers, with A:B = B:C. Since A is square, write A = a², where a is its side. [D7.18]

**Step 2.** Apply VII.19 to A:B = B:C. It gives AC = B², hence a²C = B². Thus the square a² measures the square B². [7.19, D7.15]

**Step 3.** Use the forward square-divisibility statement VIII.14: it applies directly to the divisibility just obtained. The side a therefore measures the side B. Consequently B = ad for some positive integer d. [8.14, D7.15]

**Step 4.** Substituting B = ad into the equality of Step 2 gives a²C = (ad)² = a²d². Cancelling the positive factor a² yields C = d². Thus C is equal multiplied by equal and is therefore square, as required. [7.19, D7.18]

**USED:** 7.19, 8.14, D7.15, D7.18
**Human refs (from References field):** 8.20
**Jaccard:** 0.000 — AI adds ['7.19', '8.14', 'D7.15', 'D7.18']; Human adds ['8.20']

## Proposition 8.23
**Statement:** If four numbers be in continued proportion, and the first be cube, the fourth will also be cube.

**Step 1.** Let A, B, C, D be in continued proportion, so that A:B = B:C = C:D, and let A = a³, since A is a cube. If A = B, all four numbers are equal and the conclusion is immediate. Otherwise, take the least terms p, q having the ratio A:B, allowing a term to be the unit. We choose this route because reducing the common ratio makes divisibility of cubes directly applicable. [D7.19, 7.33]

**Step 2.** The least terms p, q are prime to one another. Their cubes p³, q³ are therefore prime to one another, and consequently are the least terms having their ratio. If either p or q is the unit, the leastness of p³, q³ is immediate instead. [7.22, 7.27, 7.21]

**Step 3.** Since each successive ratio is p:q, the equality of cross-products gives
pB = qA,  pC = qB,  pD = qC.
Successive substitution therefore gives
p³D = p²qC = pq²B = q³A.
Hence, again by the converse equality of cross-products,
A:D = p³:q³. [7.19]

**Step 4.** Since p³, q³ are the least terms of this ratio, they measure A, D respectively the same number of times. Thus, for some positive integral multiplier n,
A = np³,  D = nq³.
If either least term is the unit, these equations follow directly from p³D = q³A. [7.20]

**Step 5.** Now p³ measures A = a³. Because a cube measuring a cube has its side measuring the other side, p measures a. Write a = kp, where k is a number or the unit. (If p is the unit, this divisibility is immediate.) Substituting into a³ = np³ gives k³p³ = np³, and cancellation yields n = k³. [8.15]

**Step 6.** Consequently,
D = nq³ = k³q³ = (kq)³.
Thus D is contained by three equal numbers and is a cube. Therefore, if four numbers are in continued proportion and the first is a cube, the fourth is also a cube. [D7.19]

**USED:** 7.19, 7.20, 7.21, 7.22, 7.27, 7.33, 8.15, D7.19
**Human refs (from References field):** 8.21
**Jaccard:** 0.000 — AI adds ['7.19', '7.20', '7.21', '7.22', '7.27', '7.33', '8.15', 'D7.19']; Human adds ['8.21']

## Proposition 8.24
**Statement:** If two numbers have to one another the ratio which a square number has to a square number, and the first be square, the second will also be square.

**Step 1.** Let A and B be numbers such that A:B = C:D, where C and D are square numbers, and suppose A is square. Choose the direct mean-proportional route, since the given squares immediately admit a mean: by 8.11 there is a number E such that C:E = E:D.

**Step 2.** Since one mean proportional falls between C and D, and A:B = C:D, proposition 8.8 supplies one mean proportional F between A and B. Thus A:F = F:B, so A, F, B are in continued proportion. [8.8]

**Step 3.** The first of these three numbers, A, is square. Therefore the third, B, is also square, by 8.22. Hence, if two numbers have the ratio of a square number to a square number and the first is square, the second is also square. [8.22]

**USED:** 8.11, 8.22, 8.8
**Human refs (from References field):** 8.18, 8.22, 8.8
**Jaccard:** 0.500 — AI adds ['8.11']; Human adds ['8.18']

## Proposition 8.25
**Statement:** If two numbers have to one another the ratio which a cube number has to a cube number, and the first be cube, the second will also be cube.

**Step 1.** Let A and B be numbers such that A:B = C:D, where C and D are cube numbers, and suppose that A is a cube. Choose the direct route through two mean proportionals, since the cube-specific proposition applies immediately: by VIII.12, there are numbers E and F such that C:E = E:F = F:D. [8.12]

**Step 2.** Since A:B = C:D, and two numbers fall between C and D in continued proportion, VIII.8 gives two numbers G and H between A and B in continued proportion. Thus A:G = G:H = H:B. [8.8]

**Step 3.** The four numbers A, G, H, B are therefore in continued proportion, and the first, A, is a cube. By VIII.23, the fourth, B, is also a cube. Hence, if two numbers have the ratio of a cube number to a cube number and the first is a cube, the second is also a cube. [8.23]

**USED:** 8.12, 8.23, 8.8
**Human refs (from References field):** 8.19, 8.23, 8.8
**Jaccard:** 0.500 — AI adds ['8.12']; Human adds ['8.19']

## Proposition 8.26
**Statement:** Similar plane numbers have to one another the ratio which a square number has to a square number.

**Step 1.** Let A and B be similar plane numbers, and let a and b be corresponding sides in their proportional representations (D7.21). We take the corresponding-side route because VIII.18 applies directly to the given similarity: A has to B the duplicate ratio of that which a has to b (8.18).

**Step 2.** Form S by multiplying a by itself, and T by multiplying b by itself. Then S and T are square numbers with sides a and b respectively (D7.18). Hence S has to T the duplicate ratio of that which a has to b (8.11).

**Step 3.** Thus A:B and S:T are both the duplicate ratio of the same ratio a:b. Ratios which are the same with the same ratio are the same with one another, so A:B = S:T (5.11). Since S and T are square numbers, similar plane numbers have to one another the ratio which a square number has to a square number. ∎

**USED:** 5.11, 8.11, 8.18, D7.18, D7.21
**Human refs (from References field):** 7.33, 8.18, 8.2
**Jaccard:** 0.143 — AI adds ['5.11', '8.11', 'D7.18', 'D7.21']; Human adds ['7.33', '8.2']

## Proposition 8.27
**Statement:** Similar solid numbers have to one another the ratio which a cube number has to a cube number.

**Step 1.** Let A and B be similar solid numbers, and let a and b be corresponding sides. We choose the direct route through triplicate ratios, since VIII.19 applies immediately: A:B is the triplicate of a:b. [8.19]

**Step 2.** Form C = a·a·a and D = b·b·b. These are cube numbers with sides a and b, respectively. By VIII.12, C:D is likewise the triplicate of a:b. [D7.19, 8.12]

**Step 3.** Thus A:B and C:D are the same with the same ratio. Ratios which are the same with the same ratio are also the same with one another; hence A:B = C:D. Since C and D are cube numbers, similar solid numbers have to one another the ratio which a cube number has to a cube number. [5.11]

**USED:** 5.11, 8.12, 8.19, D7.19
**Human refs (from References field):** 7.33, 8.19, 8.2
**Jaccard:** 0.167 — AI adds ['5.11', '8.12', 'D7.19']; Human adds ['7.33', '8.2']
