# Book 8 of Euclid's Elements — Step-by-Step AI Proofs (Run A)

## Proposition 8.1
**Statement:** If there be as many numbers as we please in continued proportion, and the extremes of them be prime to one another, the numbers are the least of those which have the same ratio with them.

**Step 1.** Let A₁, A₂, …, Aₙ be the given numbers in continued proportion, with A₁ and Aₙ prime to one another. Let B₁, B₂, …, Bₙ be any numbers having the same successive ratios, so that Aᵢ : Aᵢ₊₁ = Bᵢ : Bᵢ₊₁ for every i < n. We shall show that every Aᵢ is no greater than its corresponding Bᵢ. [Hypothesis; D7.20.]

**Step 2.** Apply the numerical ex aequali theorem to the corresponding initial segments of the two sequences. For every i ≥ 2 this gives A₁ : Aᵢ = B₁ : Bᵢ. In particular, A₁ : Aₙ = B₁ : Bₙ. The numerical theorem is the natural choice because all the terms are numbers. [7.14.]

**Step 3.** Use the primality of the extremes directly, rather than constructing another least sequence. Since A₁ and Aₙ are prime to one another, they are the least numbers having their ratio. Consequently, they measure B₁ and Bₙ respectively the same number of times. Denote this common multiplicity by k, allowing k to be one; thus B₁ = kA₁ and Bₙ = kAₙ. [7.21; 7.20.]

**Step 4.** For each i ≥ 2, alternation of the proportion in Step 2 gives A₁ : B₁ = Aᵢ : Bᵢ. Since A₁ measures B₁ exactly k times, the definition of numerical proportion implies that Aᵢ likewise measures Bᵢ exactly k times. Hence Bᵢ = kAᵢ for every i, including i = 1 by Step 3. [7.13; D7.20.]

**Step 5.** If k is one, all corresponding terms are equal. If k is greater than one, each Bᵢ contains Aᵢ as a proper part and is therefore greater than Aᵢ. Thus no sequence having the same ratios can have any corresponding term smaller than the given one. Therefore the given numbers are the least of those having the same ratio with them. [Step 4; CN5.]

**USED:** 7.13, 7.14, 7.20, 7.21, CN5, D7.20
**Human refs (from References field):** 7.14, 7.20, 7.21
**Jaccard:** 0.500 — AI adds ['7.13', 'CN5', 'D7.20']

## Proposition 8.2
**Statement:** To find numbers in continued proportion, as many as may be prescribed, and the least that are in a given ratio.

**Step 1.** Let the given ratio be A:B, and let the prescribed multitude of terms be m ≥ 2. Begin with the two-term list A, B. The chosen route is to construct a list of the required length first, and then apply 7.33, which constructs the least numbers having the same respective ratios as any given finite list. Thus no separate coprimality argument is needed. [7.33]

**Step 2.** Suppose a list X₁, …, Xᵣ has been constructed whose every successive ratio is A:B. Form the list
A·X₁, A·X₂, …, A·Xᵣ, B·Xᵣ,
using multiplication as defined in D7.15. For each i < r, multiplication of Xᵢ and Xᵢ₊₁ by the same number A gives
(A·Xᵢ):(A·Xᵢ₊₁) = Xᵢ:Xᵢ₊₁ = A:B.
The first equality follows from 7.17, and the resulting equality with the given ratio follows from 5.11. Moreover,
(A·Xᵣ):(B·Xᵣ) = A:B,
because A and B multiply the same number Xᵣ, by 7.18. Hence the new list has one more term and remains in continued proportion in the given ratio. [D7.15; 7.17; 5.11; 7.18]

**Step 3.** Starting with A, B, repeat the construction of Step 2 exactly m − 2 times, making no repetition when m = 2. This produces exactly m numbers C₁, …, Cₘ, with Cᵢ:Cᵢ₊₁ = A:B for every i < m, by the preservation of successive ratios established in Step 2. [D7.15; 7.17; 7.18; 5.11]

**Step 4.** By 7.33, find the least numbers L₁, …, Lₘ having the same respective ratios as C₁, …, Cₘ. Then, for every i < m,
Lᵢ:Lᵢ₊₁ = Cᵢ:Cᵢ₊₁ = A:B,
by 5.11. Thus the Lᵢ are in continued proportion in the given ratio. Conversely, any m numbers in continued proportion in that ratio have the same successive ratios as the Cᵢ, again by 5.11, and therefore belong to the class for which 7.33 supplies the least numbers. Consequently L₁, …, Lₘ are the least numbers of the prescribed multitude in continued proportion in the given ratio, as required. [7.33; 5.11]

**USED:** 5.11, 7.17, 7.18, 7.33, D7.15
**Human refs (from References field):** 7.17, 7.18, 7.22, 7.27, 8.1
**Jaccard:** 0.250 — AI adds ['5.11', '7.33', 'D7.15']; Human adds ['7.22', '7.27', '8.1']

## Proposition 8.3
**Statement:** If as many numbers as we please in continued proportion be the least of those which have the same ratio with them, the extremes of them are prime to one another.

**Step 1.** Let A₀, A₁, …, Aᵣ, with r ≥ 1, be the given least numbers in continued proportion. Choose the least pair p, q having the ratio A₀:A₁, by 7.33. Then p and q are prime to one another, by 7.22. Path choice: construct a chain with this same successive ratio and with coprime extremes, then apply 8.1 to establish its leastness and identify it with the given chain.

**Step 2.** For each i from 0 to r, form Bᵢ = p^(r−i)q^i. Here powers denote repeated multiplication, and a zeroth power denotes the unit (D7.15, D7.1). For 0 ≤ i < r, put Tᵢ = p^(r−i−1)q^i. Thus Bᵢ = Tᵢp and Bᵢ₊₁ = Tᵢq, using commutativity of multiplication (7.16). By 7.17, multiplication of p and q by the same number preserves their ratio; when Tᵢ is the unit, the equality of ratios is immediate. Hence Bᵢ:Bᵢ₊₁ = p:q = Aᵢ:Aᵢ₊₁. Therefore B₀, …, Bᵣ are in continued proportion with the same successive ratio as the given numbers.

**Step 3.** The extremes of the constructed chain are B₀ = p^r and Bᵣ = q^r. Since p and q are prime to one another, their corresponding positive powers are prime to one another by 7.27. Thus B₀ and Bᵣ are prime to one another. For r = 1, this follows directly from Step 1.

**Step 4.** By 8.1, a continued proportion whose extremes are prime to one another consists of the least numbers having its successive ratio. Therefore B₀, …, Bᵣ are the least numbers for this ratio and this prescribed number of terms.

**Step 5.** The given chain and the constructed chain have the same number of terms and the same successive ratio, and both are least. Their corresponding terms must therefore be equal: the leastness of each gives Aᵢ ≤ Bᵢ and Bᵢ ≤ Aᵢ (hypothesis and Step 4). In particular, A₀ = B₀ and Aᵣ = Bᵣ. By Step 3, these extremes have only the unit as a common measure. Hence A₀ and Aᵣ are prime to one another, as required (D7.12).

**USED:** 7.16, 7.17, 7.22, 7.27, 7.33, 8.1, D7.1, D7.12, D7.15
**Human refs (from References field):** 7.22, 7.27, 7.33, 8.2
**Jaccard:** 0.300 — AI adds ['7.16', '7.17', '8.1', 'D7.1', 'D7.12', 'D7.15']; Human adds ['8.2']

## Proposition 8.4
**Statement:** Given as many ratios as we please in least numbers, to find numbers in continued proportion which are the least in the given ratios.

**Step 1.** Let the given ratios, in their prescribed order, be a_1:b_1, …, a_m:b_m, each expressed in least numbers. We seek numbers x_0, …, x_m such that x_{i-1}:x_i = a_i:b_i for every i (D7.20). **Path choice:** first construct a chain having the prescribed successive ratios, and then apply 7.33, which directly finds the least numbers proportional to an arbitrary finite list.

**Step 2.** Begin with the chain C_0 = a_1, C_1 = b_1, which has the first prescribed ratio (D7.20). Suppose a chain C_0, …, C_r has already been constructed with C_{i-1}:C_i = a_i:b_i for 1 ≤ i ≤ r, and another ratio a_{r+1}:b_{r+1} remains. Form a new chain by setting
D_j = a_{r+1}C_j for 0 ≤ j ≤ r,
and D_{r+1} = b_{r+1}C_r.
These products are constructed by multiplication (D7.15).

**Step 3.** Multiplication of two numbers by the same number preserves their ratio (7.17). Hence, for 1 ≤ j ≤ r,
D_{j-1}:D_j = C_{j-1}:C_j = a_j:b_j,
where equality with the prescribed ratio follows by 5.11. Moreover, the products obtained by multiplying the same number C_r by a_{r+1} and b_{r+1} have the ratio of those multipliers (7.18). Therefore
D_r:D_{r+1} = a_{r+1}:b_{r+1}.
Thus this construction appends the next prescribed ratio while preserving every preceding one. Repeating it for the finitely many given ratios produces a chain C_0, …, C_m having all the prescribed successive ratios.

**Step 4.** Apply 7.33 to C_0, …, C_m, and obtain the least numbers x_0, …, x_m having the same ratios as that list. In particular,
x_{i-1}:x_i = C_{i-1}:C_i = a_i:b_i
for every i, by 5.11. The constructed numbers therefore have the required successive ratios.

**Step 5.** Let y_0, …, y_m be any other chain having the prescribed successive ratios. Its successive ratios equal those of C_0, …, C_m by 5.11. Applying numerical proportion ex aequali to any corresponding consecutive portions of the two chains gives y_j:y_k = C_j:C_k whenever j < k (7.14). Thus this other chain belongs to the class of lists among which 7.33 selected x_0, …, x_m as least. Consequently no corresponding term y_i is less than x_i (7.33). Hence x_0, …, x_m are the least numbers in the given successive ratios, as required.

**USED:** 5.11, 7.14, 7.17, 7.18, 7.33, D7.15, D7.20
**Human refs (from References field):** 7.13, 7.20, 7.34, 7.35, D7.20
**Jaccard:** 0.091 — AI adds ['5.11', '7.14', '7.17', '7.18', '7.33', 'D7.15']; Human adds ['7.13', '7.20', '7.34', '7.35']

## Proposition 8.5
**Statement:** Plane numbers have to one another the ratio compounded of the ratios of their sides.

**Step 1.** Let A and B be any plane numbers, with sides a, b and c, d respectively. Thus a multiplying b produces A, and c multiplying d produces B (D7.16).

**Step 2.** Let c multiplying b produce M (D7.15). We use this single mixed product as the intermediate number, so that each successive comparison has one common side.

**Step 3.** Since a and c multiply the same number b to produce A and M, respectively, A:M = a:c (7.18). This proposition directly handles the common multiplicand, without requiring an interchange of factors.

**Step 4.** Since the same number c multiplies b and d to produce M and B, respectively, M:B = b:d (7.17). Here the common-multiplier proposition applies directly.

**Step 5.** The ratio A:B is compounded of the successive ratios A:M and M:B: the sizes of these two ratios multiplied together give the size of A:B (D6.5). Substituting the ratios established in Steps 3 and 4, A:B is therefore compounded of a:c and b:d. Hence plane numbers have to one another the ratio compounded of the ratios of their sides.

**USED:** 7.17, 7.18, D6.5, D7.15, D7.16
**Human refs (from References field):** 7.14, 7.17, 8.4
**Jaccard:** 0.143 — AI adds ['7.18', 'D6.5', 'D7.15', 'D7.16']; Human adds ['7.14', '8.4']

## Proposition 8.6
**Statement:** If there be as many numbers as we please in continued proportion, and the first do not measure the second, neither will any other measure any other.

**Step 1.** Let A₀, A₁, …, Aₙ be the given numbers in continued proportion, and suppose that A₀ does not measure A₁. Thus every successive ratio equals A₀:A₁. Fix arbitrary positions i<j, and put m=j−i; we shall prove that Aᵢ does not measure Aⱼ. [D7.20.]

**Step 2.** By 8.2, take a least continued progression B₀, B₁, …, Bₘ having this same successive ratio. In particular, B₀:B₁=A₀:A₁. We choose the least progression for this particular block because 8.3 then gives precisely the coprimality needed for its endpoints, without calculating powers. [8.2.]

**Step 3.** B₀ cannot be the unit. For the unit measures every number; hence, if B₀ were the unit, B₀ would measure B₁. Since B₀:B₁=A₀:A₁, the definition of numerical proportion would then imply that A₀ measures A₁, contrary to the hypothesis. Thus B₀ is greater than the unit. [D7.2; D7.20.]

**Step 4.** Since B₀, B₁, …, Bₘ are the least numbers in their continued proportion, their extremes B₀ and Bₘ are prime to one another. Consequently they have no common measure other than the unit. If Bₘ itself is the unit, this conclusion is immediate from the definition. [8.3; D7.12.]

**Step 5.** The progressions Aᵢ, Aᵢ₊₁, …, Aⱼ and B₀, B₁, …, Bₘ have equally many terms and equal corresponding successive ratios. Therefore, ex aequali, Aᵢ:Aⱼ=B₀:Bₘ. If Aᵢ measured Aⱼ, this proportion would imply that B₀ measured Bₘ. But B₀ also measures itself, so B₀ would be a common measure of the extremes greater than the unit, contradicting Step 4. Hence Aᵢ does not measure Aⱼ. [7.14; D7.20; D7.12; Step 3.]

**Step 6.** Since i<j were arbitrary, no term measures any later term. Therefore, if the first does not measure the second, neither will any other measure any other in the order of the continued proportion. [Steps 1–5.]

**USED:** 7.14, 8.2, 8.3, D7.12, D7.2, D7.20
**Human refs (from References field):** 7.14, 7.33, 8.3, D7.20
**Jaccard:** 0.429 — AI adds ['8.2', 'D7.12', 'D7.2']; Human adds ['7.33']

## Proposition 8.7
**Statement:** If there be as many numbers as we please in continued proportion, and the first measure the last, it will measure the second also.

**Step 1.** Let A₁, A₂, …, Aₙ be the given numbers in continued proportion, and suppose that A₁ measures Aₙ. We must prove that A₁ measures A₂. [Hypotheses]

**Step 2.** Choose the direct route by contraposition of 8.6, since it applies to this very continued proportion. Suppose that A₁ does not measure A₂. Then no term measures another; in particular, A₁ does not measure Aₙ. [8.6]

**Step 3.** This contradicts the hypothesis that A₁ measures Aₙ. Therefore A₁ measures A₂: the first measures the second, as required. [Step 1; Step 2]

**USED:** 8.6
**Human refs (from References field):** 8.6
**Jaccard:** 1.000 — Perfect match.

## Proposition 8.8
**Statement:** If between two numbers there fall numbers in continued proportion with them, then, however many numbers fall between them in continued proportion, so many will also fall in continued proportion between the numbers which have the same ratio with the original numbers.

**Step 1.** Let A_0, A_1, …, A_{m+1} be numbers in continued proportion, with m intermediate numbers, and let B:C = A_0:A_{m+1}. Thus all successive ratios A_i:A_{i+1} are equal. We must place m numbers in continued proportion between B and C. [Hypothesis; D7.20]

**Step 2.** By 8.2, construct m+2 numbers P_0, P_1, …, P_{m+1} in continued proportion, the least having the common ratio A_0:A_1. The chosen route is to construct this least progression and then take one common multiple of all its terms; this preserves the prescribed number of intermediate terms. [8.2]

**Step 3.** The two progressions have equal corresponding successive ratios. Therefore, ex aequali, P_0:P_{m+1} = A_0:A_{m+1}, and hence P_0:P_{m+1} = B:C. Here the numerical ex-aequali theorem is the natural choice because both lists consist of numbers. [7.14; hypothesis; CN1]

**Step 4.** Since the progression P_0, …, P_{m+1} is the least having its common ratio, its extremes P_0 and P_{m+1} are prime to one another. Consequently these extremes are the least numbers having their ratio. [8.3; 7.21]

**Step 5.** Since P_0:P_{m+1} = B:C, the least numbers P_0 and P_{m+1} measure B and C respectively the same number of times. Denote this common multiplicity by t. Thus B = tP_0 and C = tP_{m+1}, where multiplication denotes repeated addition. [7.20; D7.15]

**Step 6.** For every i from 0 through m+1, take Q_i = tP_i. If t is unity, this is the progression already constructed. Otherwise, multiplication of each adjacent pair by the same number preserves its ratio, so Q_i:Q_{i+1} = P_i:P_{i+1} for every i from 0 through m. These successive ratios are therefore all equal. Moreover, Q_0 = B and Q_{m+1} = C. Hence Q_1, …, Q_m are m numbers falling in continued proportion between B and C. Since m was arbitrary, the proposition follows. [D7.15; 7.17; CN1]

**USED:** 7.14, 7.17, 7.20, 7.21, 8.2, 8.3, CN1, D7.15, D7.20
**Human refs (from References field):** 7.14, 7.20, 7.21, 7.33, 8.3, D7.20
**Jaccard:** 0.500 — AI adds ['7.17', '8.2', 'CN1', 'D7.15']; Human adds ['7.33']

## Proposition 8.9
**Statement:** If two numbers be prime to one another, and numbers fall between them in continued proportion, then, however many numbers fall between them in continued proportion, so many will also fall between each of them and an unit in continued proportion.

**Step 1.** Let A = X₀, X₁, …, Xₙ = B be the given numbers in continued proportion, where A and B are prime to one another and n − 1 numbers fall between them. Write 1 for the unit. Thus all successive ratios Xᵢ:Xᵢ₊₁ are equal. We use 8.1 directly, because its hypothesis is precisely the given coprimality of the extremes: this progression is the least of its length having its common ratio. [D7.1, D7.20, 8.1]

**Step 2.** Choose the least terms p, q having the ratio X₀:X₁, by 7.33. These terms are prime to one another by 7.22. Neither term can be a unit. For otherwise one of X₀, X₁ would measure the other; equality of all successive ratios would then make every consecutive pair divide in the same direction. Repeated measurement would consequently make A measure B, or B measure A. Since A and B are numbers, this would give them a common measure other than the unit, contrary to their coprimality. Thus p and q are both numbers greater than the unit. [7.33, 7.22, D7.20, D7.3, D7.15, D7.2, D7.12]

**Step 3.** Write pʲ and qʲ for the products of j copies of p and q respectively, with exponent zero denoting the unit. Form the n + 1 numbers
Cᵢ = pⁿ⁻ⁱqⁱ, for 0 ≤ i ≤ n.
Their extremes are C₀ = pⁿ and Cₙ = qⁿ. For each i < n, the two successive terms Cᵢ and Cᵢ₊₁ result from multiplying p and q respectively by the same number pⁿ⁻ⁱ⁻¹qⁱ. Therefore Cᵢ:Cᵢ₊₁ = p:q. Hence this is another continued proportion of the same length and with the same common ratio as the given one. [D7.1, D7.15, 7.16, 7.17]

**Step 4.** Since p and q are prime to one another, their repeated self-products pⁿ and qⁿ are prime to one another by 7.27. Applying 8.1 to the progression C₀, …, Cₙ, it too is the least progression of this length having this common ratio. Both progressions are therefore least among exactly the same progressions. Each is termwise no greater than the other, so their corresponding terms are equal. In particular,
A = pⁿ and B = qⁿ.
This identifies the extremes directly by leastness, without a separate comparison of their endpoint ratios. [7.27, 8.1]

**Step 5.** Now form
1, p, p², …, pⁿ = A
and
1, q, q², …, qⁿ = B.
In the first list every successor is p times its predecessor, and in the second every successor is q times its predecessor. Both lists are therefore in continued proportion. Each contains exactly n − 1 intervening numbers, namely the powers with exponents 1 through n − 1. This is precisely the number of numbers that fell between A and B. Thus, however many numbers fall between two relatively prime numbers in continued proportion, so many also fall between each of them and the unit in continued proportion. [D7.15, D7.20]

**USED:** 7.16, 7.17, 7.22, 7.27, 7.33, 8.1, D7.1, D7.12, D7.15, D7.2, D7.20, D7.3
**Human refs (from References field):** 8.1, 8.2, D7.20
**Jaccard:** 0.154 — AI adds ['7.16', '7.17', '7.22', '7.27', '7.33', 'D7.1', 'D7.12', 'D7.15', 'D7.2', 'D7.3']; Human adds ['8.2']

## Proposition 8.10
**Statement:** If numbers fall between each of two numbers and an unit in continued proportion, however many numbers fall between each of them and an unit in continued proportion, so many also will fall between the numbers themselves in continued proportion.

**Step 1.** Let there be n−1 intervening numbers in each of the two given continued proportions, where n≥2. Write them as
A = a_n, a_{n−1}, …, a_1, a_0 = 1,
and
B = b_n, b_{n−1}, …, b_1, b_0 = 1.
Put p = a_1 and q = b_1. Thus, for every j from 1 through n,
a_j : a_{j−1} = p : 1 and b_j : b_{j−1} = q : 1. [Hypothesis; D7.20]

**Step 2.** Since p and q consist respectively of p and q units, these proportions say that each a_j is p times its predecessor and each b_j is q times its predecessor. Therefore
a_j = p a_{j−1}, and b_j = q b_{j−1}.
Here and below, a product with the unit denotes the other factor. [D7.1, D7.2, D7.20, D7.15]

**Step 3.** We use a mixed-product construction, arranging successive terms as products with a common multiplier so that 7.17 applies directly. For i = 0, …, n, form
X_i = a_{n−i} b_i.
Then X_0 = A and X_n = B. The remaining X_i are numbers, being products of numbers. [D7.15; D7.1]

**Step 4.** For each i = 0, …, n−1, put
T_i = a_{n−i−1} b_i.
This is a number: the two indices sum to n−1≥1, so at least one factor is a number rather than the unit. Using Step 2 gives
X_i = (p a_{n−i−1})b_i = T_i p,
and
X_{i+1} = a_{n−i−1}(q b_i) = T_i q.
The regrouping of products follows from multiplication as repeated addition, and the interchange of factors from commutativity. [D7.1, D7.2, D7.15; 7.16]

**Step 5.** The same number T_i, multiplying p and q, therefore produces X_i and X_{i+1}. By 7.17, the products have the ratio of the numbers multiplied:
X_i : X_{i+1} = p : q.
This holds for every i from 0 through n−1. The common-multiplier form is precisely why 7.17 is the applicable proportionality result. [7.17]

**Step 6.** Consequently,
A = X_0, X_1, …, X_{n−1}, X_n = B
are in continued proportion, since every successive pair has the same ratio p : q. There are n−1 intervening numbers, exactly the number given between each original number and the unit. Hence the proposition follows. [D7.20]

**USED:** 7.16, 7.17, D7.1, D7.15, D7.2, D7.20
**Human refs (from References field):** 7.17, 7.18, D7.20
**Jaccard:** 0.286 — AI adds ['7.16', 'D7.1', 'D7.15', 'D7.2']; Human adds ['7.18']

## Proposition 8.11
**Statement:** Between two square numbers there is one mean proportional number, and the square has to the square the ratio duplicate of that which the side has to the side.

**Step 1.** Let A and B be the two square numbers, with sides a and b respectively. Thus a multiplying a produces A, and b multiplying b produces B. [D7.18]

**Step 2.** Let a multiply b, producing the number M. Choose this product as the candidate mean: the multiplication-ratio propositions apply directly to its two links with the squares. [D7.15]

**Step 3.** The number a, multiplying a and b, produces A and M respectively. Therefore the products have the same ratio as the numbers multiplied: A:M = a:b. [7.17]

**Step 4.** The numbers a and b, multiplying the same number b, produce M and B respectively. Therefore the products have the same ratio as the multipliers: M:B = a:b. Here the common-multiplicand proposition applies directly, without reversing either product. [7.18]

**Step 5.** Since A:M and M:B are each equal to a:b, they are equal to one another. Thus A:M = M:B, so M is a mean proportional number between A and B. [5.11]

**Step 6.** Since A, M, B are continuously proportional, A has to B the duplicate ratio of that which A has to M. But A:M = a:b by Step 3. Hence the square A has to the square B the ratio duplicate of that which its side a has to the side b. Both assertions are proved. [D5.9]

**USED:** 5.11, 7.17, 7.18, D5.9, D7.15, D7.18
**Human refs (from References field):** 7.17, 7.18, D5.9
**Jaccard:** 0.500 — AI adds ['5.11', 'D7.15', 'D7.18']

## Proposition 8.12
**Statement:** Between two cube numbers there are two mean proportional numbers, and the cube has to the cube the ratio triplicate of that which the side has to the side.

**Step 1.** Let A and B be the given cube numbers, with respective sides a and b. Form p by multiplying a by a, q by multiplying a by b, and r by multiplying b by b. Then a multiplying p produces A, and b multiplying r produces B. [D7.15, D7.19] We choose the direct multiplication–ratio route, since it retains the ratio of the given sides throughout the construction.

**Step 2.** Since a multiplying a and b produces p and q, respectively, 7.17 gives p:q = a:b. Since a and b multiplying b produce q and r, respectively, 7.18 gives q:r = a:b. Thus the three numbers p, q, r have successive ratios equal to the ratio of the sides. [7.17, 7.18]

**Step 3.** Let a multiply q and r to produce M and N, respectively. [D7.15] Since a multiplying p, q, r produces A, M, N, proposition 7.17 gives A:M = p:q and M:N = q:r. By Step 2, therefore, A:M = a:b and M:N = a:b. [7.17, 5.11]

**Step 4.** Since a and b multiplying r produce N and B, respectively, N:B = a:b. [7.18] Combining this with Step 3 gives A:M = M:N = N:B = a:b. Hence M and N are two mean proportional numbers between A and B. [5.11, D7.20]

**Step 5.** Because A, M, N, B are four numbers in continued proportion, A:B is the triplicate ratio of A:M. But A:M = a:b. Therefore the cube A has to the cube B the ratio triplicate of that which its side a has to the side b, and the required two mean proportional numbers have been constructed. [D5.10]

**USED:** 5.11, 7.17, 7.18, D5.10, D7.15, D7.19, D7.20
**Human refs (from References field):** 7.17, 7.18, D5.10
**Jaccard:** 0.429 — AI adds ['5.11', 'D7.15', 'D7.19', 'D7.20']

## Proposition 8.13
**Statement:** If there be as many numbers as we please in continued proportion, and each by multiplying itself make some number, the products will be proportional; and, if the original numbers by multiplying the products make certain numbers, the latter will also be proportional.

**Step 1.** Let a₁, …, aₙ be the given numbers in continued proportion. For each i, let Sᵢ = aᵢ·aᵢ and Tᵢ = aᵢ·Sᵢ. Thus Sᵢ is the square on aᵢ and Tᵢ is its cube (D7.18, D7.19). We choose the direct route through 8.11 and 8.12, since these already determine the ratios of squares and cubes from those of their sides.

**Step 2.** Take any three consecutive original numbers, and call them a, b, c. By the hypothesis of continued proportion, a:b = b:c (D7.20). It suffices to establish the corresponding equality of adjacent ratios for their squares and for their cubes, since the consecutive triple is arbitrary.

**Step 3.** By 8.11, a²:b² is the duplicate ratio of a:b, while b²:c² is the duplicate ratio of b:c. Explicitly, by the meaning of duplicate ratio, the intervening means u and v give chains
 a²:u = u:b² = a:b,
 b²:v = v:c² = b:c
(8.11, D5.9). Since a:b = b:c, these two three-term chains have equal corresponding adjacent ratios. Therefore their extreme ratios are equal by 7.14, the ex aequali theorem for numbers: a²:b² = b²:c².

**Step 4.** Similarly, by 8.12, a³:b³ is the triplicate ratio of a:b, while b³:c³ is the triplicate ratio of b:c. The two intervening means in each case therefore give chains
 a³:p = p:q = q:b³ = a:b,
 b³:r = r:s = s:c³ = b:c
(8.12, D5.10). Their corresponding adjacent ratios are equal by Step 2. Applying 7.14 to these four-term chains gives a³:b³ = b³:c³.

**Step 5.** Steps 3 and 4 apply to every consecutive triple of the original numbers. Hence Sᵢ:Sᵢ₊₁ = Sᵢ₊₁:Sᵢ₊₂ and Tᵢ:Tᵢ₊₁ = Tᵢ₊₁:Tᵢ₊₂ wherever these terms occur. Thus both the products obtained by squaring the original numbers and the products obtained by multiplying those squares by the corresponding original numbers are in continued proportion (D7.20), as required.

**USED:** 7.14, 8.11, 8.12, D5.10, D5.9, D7.18, D7.19, D7.20
**Human refs (from References field):** 7.14
**Jaccard:** 0.125 — AI adds ['8.11', '8.12', 'D5.10', 'D5.9', 'D7.18', 'D7.19', 'D7.20']

## Proposition 8.14
**Statement:** If a square measure a square, the side will also measure the side; and, if the side measure the side, the square will also measure the square.

**Step 1.** Let A and B be square numbers with sides a and b, respectively, so that A = a·a and B = b·b. Form also the mixed product M = a·b. These constructions use the definitions of multiplication and a square number (D7.15, D7.18).

**Step 2.** Multiplying a and b by the common multiplier a gives A:M = a:b (7.17). The multipliers a and b acting on the common number b give M:B = a:b (7.18). Consequently A:M = M:B, so A, M, B are in continued proportion (CN1). The mixed product makes the ratio of the sides explicit; the direct path is therefore to apply 8.7 to divisibility of the extreme terms.

**Step 3.** Suppose first that A measures B. Since A, M, B are in continued proportion, their first term measures their second term by 8.7. Thus A measures M. But A:M = a:b, so a is the same part of b that A is of M; hence a measures b (D7.20, D7.3). Therefore, if the square measures the square, its side measures the other side.

**Step 4.** Conversely, suppose that a measures b. Since A:M = a:b and M:B = a:b, the definition of proportional numbers gives that A measures M and M measures B (D7.20, D7.3). Thus M consists of a whole number of copies of A, and B consists of a whole number of copies of M (D7.5, D7.15).

**Step 5.** Replace each copy of M in B by the copies of A composing it. This expresses B as a whole number of copies of A, so B is a multiple of A and A measures B (D7.15, D7.5). Therefore, if the side measures the side, the square measures the square. Both assertions are proved.

**USED:** 7.17, 7.18, 8.7, CN1, D7.15, D7.18, D7.20, D7.3, D7.5
**Human refs (from References field):** 8.11, 8.7, D7.20
**Jaccard:** 0.200 — AI adds ['7.17', '7.18', 'CN1', 'D7.15', 'D7.18', 'D7.3', 'D7.5']; Human adds ['8.11']

## Proposition 8.15
**Statement:** If a cube number measure a cube number, the side will also measure the side; and, if the side measure the side, the cube will also measure the cube.

**Step 1.** Let A and B be cube numbers, and let a and b be their respective sides. Thus A is the product of three factors equal to a, and B of three factors equal to b. (D7.19)

**Step 2.** By the theorem on the two mean proportionals between cubes, with the meaning of triplicate ratio, take numbers M and N such that
A : M = M : N = N : B = a : b. (8.12, D5.10)
The chosen route is to use this continued proportion, since it allows divisibility of the extreme terms to be transferred directly to the first two terms.

**Step 3.** First suppose that A measures B. Since A, M, N, B are in continued proportion and the first measures the last, A also measures M. (8.7)

**Step 4.** But A : M = a : b. Therefore a is the same part of b that A is of M; hence a measures b. This proves the first implication. (D7.20)

**Step 5.** Conversely, suppose that a measures b, and let b contain a exactly k times. From the equal ratios in Step 2, M contains A exactly k times, N contains M exactly k times, and B contains N exactly k times. (D7.5, D7.20)

**Step 6.** Consequently B consists of k groups of k groups of k copies of A, and is therefore a whole multiple of A. Thus A measures B. (D7.15, D7.5) Hence, if a cube measures a cube, its side measures the other side; and, if the side measures the side, the cube measures the cube.

**USED:** 8.12, 8.7, D5.10, D7.15, D7.19, D7.20, D7.5
**Human refs (from References field):** 8.11, 8.12, 8.7, D7.20
**Jaccard:** 0.375 — AI adds ['D5.10', 'D7.15', 'D7.19', 'D7.5']; Human adds ['8.11']

## Proposition 8.16
**Statement:** If a square number do not measure a square number, neither will the side measure the side; and, if the side do not measure the side, neither will the square measure the square.

**Step 1.** Let A and B be square numbers, with respective sides a and b. We use the two implications of Proposition 8.14 by contradiction: this is the direct route because that proposition already relates measurement of these squares to measurement of their corresponding sides. [8.14]

**Step 2.** Suppose A does not measure B. If a measured b, then, by the second implication of Proposition 8.14, A would measure B, contrary to the supposition. Therefore a does not measure b. Thus, if a square number does not measure a square number, neither does its side measure the other side. [8.14]

**Step 3.** Conversely, suppose a does not measure b. If A measured B, then, by the first implication of Proposition 8.14, a would measure b, contrary to the supposition. Therefore A does not measure B. Thus, if the side does not measure the side, neither does the square measure the square. Both assertions are proved. [8.14]

**USED:** 8.14
**Human refs (from References field):** 8.14
**Jaccard:** 1.000 — Perfect match.

## Proposition 8.17
**Statement:** If a cube number do not measure a cube number, neither will the side measure the side; and, if the side do not measure the side, neither will the cube measure the cube.

**Step 1.** Let A and B be cube numbers, with respective sides a and b. We use the two assertions of 8.15 by contradiction: this is the direct route because that proposition already relates measurement of cubes to measurement of their sides in both directions [8.15].

**Step 2.** Suppose A does not measure B. If a measured b, then, by the second assertion of 8.15, A would measure B, contrary to the supposition. Therefore a does not measure b [8.15].

**Step 3.** Conversely, suppose a does not measure b. If A measured B, then, by the first assertion of 8.15, a would measure b, contrary to the supposition. Therefore A does not measure B. Thus both assertions are proved [8.15].

**USED:** 8.15
**Human refs (from References field):** 8.15
**Jaccard:** 1.000 — Perfect match.

## Proposition 8.18
**Statement:** Between two similar plane numbers there is one mean proportional number; and the plane number has to the plane number the ratio duplicate of that which the corresponding side has to the corresponding side.

**Step 1.** Let A and B be the given similar plane numbers, with sides a, b and c, d respectively, so that A = ab and B = cd. By similarity, a:b = c:d (D7.16, D7.21). Therefore, alternately, a:c = b:d (7.13).

**Step 2.** Form the number M = ad by multiplying a by d (D7.15). Path choice: this mixed product supplies the mean directly, since each adjacent pair of products shares a factor.

**Step 3.** Since a multiplying b and d produces A and M, respectively, A:M = b:d (7.17). Since a and c multiplying d produce M and B, respectively, M:B = a:c (7.18). These propositions apply directly to the common multiplier and common multiplicand, respectively.

**Step 4.** By Step 1, b:d = a:c. Consequently the ratios obtained in Step 3 give A:M = M:B, and their common ratio is a:c, or equivalently b:d (5.11). Thus M is a mean proportional number between A and B.

**Step 5.** Since A, M, B are continuously proportional, A:B is the duplicate ratio of A:M (D5.9). But A:M equals the ratio a:c of corresponding sides, and also b:d, by Step 4. Hence between the two similar plane numbers there is a mean proportional number, and the first plane number has to the second the duplicate ratio of that which a corresponding side has to the corresponding side, as required.

**USED:** 5.11, 7.13, 7.17, 7.18, D5.9, D7.15, D7.16, D7.21
**Human refs (from References field):** 7.13, 7.17, D5.9, D7.21
**Jaccard:** 0.500 — AI adds ['5.11', '7.18', 'D7.15', 'D7.16']

## Proposition 8.19
**Statement:** Between two similar solid numbers there fall two mean proportional numbers; and the solid number has to the similar solid number the ratio triplicate of that which the corresponding side has to the corresponding side.

**Step 1.** Let A and B be similar solid numbers, with corresponding sides a, b, c and d, e, f. Thus A = (ab)c and B = (de)f, and a:d = b:e = c:f. (D7.17, D7.21.)

**Step 2.** Construct the numbers M = (ab)f and N = (db)f. These products are numbers by the definition of multiplication. (D7.15.) Path choice: construct the means directly by changing one corresponding side at a time, using common-factor proportionality without rearranging the triple products.

**Step 3.** The number ab, multiplying c and f, produces A and M. Therefore A:M = c:f. (7.17.)

**Step 4.** The numbers a and d, multiplying b, produce ab and db; hence (ab):(db) = a:d. Again, ab and db, multiplying f, produce M and N; hence M:N = (ab):(db). Consequently M:N = a:d. (7.18, 5.11.)

**Step 5.** The number d, multiplying b and e, produces db and de; hence (db):(de) = b:e. The numbers db and de, multiplying f, produce N and B; hence N:B = (db):(de). Consequently N:B = b:e. (7.17, 7.18, 5.11.)

**Step 6.** Since c:f = a:d = b:e, the preceding equalities give A:M = M:N = N:B = a:d. Thus A, M, N, B are continuously proportional, and M and N are the required two mean proportional numbers between A and B. (D7.21, 5.11, D7.20.)

**Step 7.** For four continuously proportional numbers, the first has to the fourth the ratio triplicate of that which it has to the second. Therefore A:B is triplicate of A:M, which equals a:d, the ratio of corresponding sides. This proves both assertions. (D5.10, Step 6.)

**USED:** 5.11, 7.17, 7.18, D5.10, D7.15, D7.17, D7.20, D7.21
**Human refs (from References field):** 7.13, 7.17, 7.18, 8.18, D5.10, D7.21
**Jaccard:** 0.400 — AI adds ['5.11', 'D7.15', 'D7.17', 'D7.20']; Human adds ['7.13', '8.18']

## Proposition 8.20
**Statement:** If one mean proportional number fall between two numbers, the numbers will be similar plane numbers.

**Step 1.** Let A and B be the given numbers, and let M be their mean proportional. Thus A:M = M:B. We must show that A and B are similar plane numbers. [Hypothesis; D7.20]

**Step 2.** Choose the least numbers p and q having the ratio A:M. Then p:q = A:M = M:B. [7.33] Path choice: reduce the ratio of adjacent terms, since the least-term divisibility theorem will supply factorizations of both extremes directly.

**Step 3.** Since p and q are the least numbers in the ratio A:M, they measure A and M respectively the same number of times. Denote that multiplier by r. Then A = pr and M = qr. [7.20; D7.15]

**Step 4.** Likewise, since M:B = p:q, the same least numbers p and q measure M and B respectively the same number of times. Denote this multiplier by s. Then M = ps and B = qs. [7.20; D7.15]

**Step 5.** The products ps and qr both equal M, and therefore ps = qr. [CN1] Hence p:q = r:s, by the converse assertion that equality of the products of the extremes and the means implies proportionality. [7.19]

**Step 6.** Since A = pr and B = qs, A and B are plane numbers with sides p, r and q, s respectively. [D7.16] Their corresponding sides are proportional, since p:q = r:s. Therefore A and B are similar plane numbers, as required. [D7.21]

**USED:** 7.19, 7.20, 7.33, CN1, D7.15, D7.16, D7.20, D7.21
**Human refs (from References field):** 7.13, 7.17, 7.20, 7.33
**Jaccard:** 0.200 — AI adds ['7.19', 'CN1', 'D7.15', 'D7.16', 'D7.20', 'D7.21']; Human adds ['7.13', '7.17']

## Proposition 8.21
**Statement:** If two mean proportional numbers fall between two numbers, the numbers are similar solid numbers.

**Step 1.** Let the two mean proportional numbers be M and N, so that
A:M = M:N = N:B.
These are the given continued proportions (D7.20). Write 1 for the unit and use ordinary product notation, with x³ denoting xxx (D7.1, D7.15).

**Step 2.** First suppose that one extreme measures the other. Reverse the progression if necessary, so that A measures B. By 8.7, A also measures M. Write M = rA. The given proportions then imply N = rM and B = rN (D7.20). Consequently,
A = k·1³,   B = kr³,
where k = A (D7.15). Thus, in this case, we have representations A = kp³ and B = kq³, taking p = 1 and q = r.

**Step 3.** Now suppose that neither extreme measures the other. Choose the least terms E and F having the ratio A:B, by 7.33. By 7.20, they measure A and B the same number of times; hence, for a common multiplier k,
A = kE,   B = kF.
Neither E nor F is the unit, since otherwise one of A and B would measure the other. Moreover, E and F are prime to one another by 7.22. This least-ratio reduction is the chosen route because it makes 8.9 directly applicable to the reduced extremes.

**Step 4.** Since A and B admit two mean proportionals and E:F = A:B, E and F also admit two mean proportionals, by 8.8. Since E and F are prime to one another, 8.9 supplies two mean proportionals between each of them and the unit. Denote these progressions by
1, p, s, E   and   1, q, t, F.

**Step 5.** From 1:p = p:s = s:E, the definition of numerical proportion gives s = pp and E = ps. Thus E = p³. Likewise, from 1:q = q:t = t:F, we obtain F = q³ (D7.20, D7.15). Substitution into Step 3 gives
A = kp³,   B = kq³.
Together with Step 2, this establishes these representations in every case.

**Step 6.** Regrouping the products, we have
A = (kp)pp,   B = (kq)qq
(D7.15). Thus their respective solid sides are kp, p, p and kq, q, q (D7.17); a unit factor leaves the product unchanged (D7.1, D7.15).

**Step 7.** Multiplication by the common factor k preserves the ratio, so
kp:kq = p:q
by 7.17; when a factor is the unit, the same assertion follows immediately from D7.20. Therefore the three corresponding side ratios are equal:
kp:kq = p:q = p:q.
By D7.21, A and B are similar solid numbers. Hence, if two mean proportional numbers fall between two numbers, those numbers are similar solid numbers.

**USED:** 7.17, 7.20, 7.22, 7.33, 8.7, 8.8, 8.9, D7.1, D7.15, D7.17, D7.20, D7.21
**Human refs (from References field):** 7.14, 7.18, 7.20, 7.21, 7.33, 8.2, 8.20, 8.3
**Jaccard:** 0.111 — AI adds ['7.17', '7.22', '8.7', '8.8', '8.9', 'D7.1', 'D7.15', 'D7.17', 'D7.20', 'D7.21']; Human adds ['7.14', '7.18', '7.21', '8.2', '8.20', '8.3']

## Proposition 8.22
**Statement:** If three numbers be in continued proportion, and the first be square, the third will also be square.

**Step 1.** Let A, B, C be the given numbers in continued proportion, so that A:B = B:C. Since A is square, write A = a·a, where a is its side (D7.18).

**Step 2.** By 7.19, the product of the extremes equals the square of the mean: A·C = B·B. Thus A measures B·B (D7.5), and both A and B·B are squares (D7.18).

**Step 3.** We choose the direct square-divisibility route: 8.14 applies immediately to Step 2 and gives that a measures B. Let b be the multiplier, so that B = a·b (D7.15). Here b is not merely a unit: otherwise B = a, and Step 2 would give A·C = A, whereas multiplication by the number C produces a whole greater than A (D7.2, D7.15, CN5). Form T = b·b, which is square (D7.18).

**Step 4.** Multiplying a and b by a produces A and B; hence A:B = a:b (7.17). Letting a and b multiply b produces B and T; hence B:T = a:b (7.18). Therefore A:B = B:T (5.11).

**Step 5.** The given proportion A:B = B:C and Step 4 yield B:C = B:T (5.11). Numbers to which the same number has the same ratio are equal, so C = T (5.9). Since T = b·b, C is square (D7.18). Therefore the third number is square, as required.

**USED:** 5.11, 5.9, 7.17, 7.18, 7.19, 8.14, CN5, D7.15, D7.18, D7.2, D7.5
**Human refs (from References field):** 8.20
**Jaccard:** 0.000 — AI adds ['5.11', '5.9', '7.17', '7.18', '7.19', '8.14', 'CN5', 'D7.15', 'D7.18', 'D7.2', 'D7.5']; Human adds ['8.20']

## Proposition 8.23
**Statement:** If four numbers be in continued proportion, and the first be cube, the fourth will also be cube.

**Step 1.** Let A, B, C, D be in continued proportion, so that A:B = B:C = C:D, and let A be a cube. Write A = a³, where a is a number (D7.19), and put s = a². Then s³ = A² by repeated multiplication and commutation of factors (D7.15, 7.16). Our route is to obtain a divisibility between cubes and apply the positive divisibility implication of 8.15.

**Step 2.** From A:B = B:C, the product of the extremes equals the product of the means, giving B² = AC. Likewise, from A:B = C:D, we obtain BC = AD (7.19).

**Step 3.** Consequently,
B³ = B(AC) = A(BC) = A²D = s³D,
by the identities in Steps 1–2 and the rules of repeated multiplication and commutation (D7.15, 7.16). Thus the cube s³ measures the cube B³ (D7.3).

**Step 4.** Therefore s measures B, since a cube measuring a cube has its side measuring the other side (8.15). Write B = sb, where b is the integral multiplier, initially either a unit or a number (D7.1, D7.2, D7.15). This multiplier cannot be a unit: otherwise B = s, and Step 3 would give s³ = s³D; but D contains more than one unit, so s³D contains s³ as a proper part and is greater than it (D7.2, D7.15, CN5). Hence b is a number.

**Step 5.** Substituting B = sb into the identity B³ = s³D and regrouping the factors gives s³b³ = s³D (D7.15, 7.16). By the converse direction of 7.19, D:b³ = s³:s³. Since the latter terms are equal, D = b³ (D7.20).

**Step 6.** Thus D is the product of the number b with itself and again with itself, and therefore is a cube (D7.19). Hence, if four numbers are in continued proportion and the first is a cube, the fourth is also a cube.

**USED:** 7.16, 7.19, 8.15, CN5, D7.1, D7.15, D7.19, D7.2, D7.20, D7.3
**Human refs (from References field):** 8.21
**Jaccard:** 0.000 — AI adds ['7.16', '7.19', '8.15', 'CN5', 'D7.1', 'D7.15', 'D7.19', 'D7.2', 'D7.20', 'D7.3']; Human adds ['8.21']

## Proposition 8.24
**Statement:** If two numbers have to one another the ratio which a square number has to a square number, and the first be square, the second will also be square.

**Step 1.** Let A and B be numbers such that A:B = C:D, where C and D are square numbers, and suppose A is square. Choose the mean-proportional route, since the given comparison numbers are squares. By **8.11**, there is a number E such that C:E = E:D.

**Step 2.** Since one mean proportional falls between C and D, and A:B = C:D, **8.8** gives one mean proportional F between A and B. Thus A:F = F:B, so A, F, B are in continued proportion.

**Step 3.** The three numbers A, F, B are in continued proportion and the first, A, is square. Therefore, by **8.22**, the third, B, is also square, as required.

**USED:** 8.11, 8.22, 8.8
**Human refs (from References field):** 8.18, 8.22, 8.8
**Jaccard:** 0.500 — AI adds ['8.11']; Human adds ['8.18']

## Proposition 8.25
**Statement:** If two numbers have to one another the ratio which a cube number has to a cube number, and the first be cube, the second will also be cube.

**Step 1.** Let A and B be numbers such that A:B = C:D, where C and D are cube numbers, and suppose A is cube. By **8.12**, there are two mean proportional numbers E and F between C and D, so that C:E = E:F = F:D. We choose this cube-specific result because it supplies the required means directly, without passing through general solid-number similarity.

**Step 2.** Since A:B = C:D, and two mean proportional numbers fall between C and D, **8.8** gives two mean proportional numbers G and H between A and B. Thus A:G = G:H = H:B.

**Step 3.** The four numbers A, G, H, B are therefore in continued proportion. Since the first, A, is cube, **8.23** implies that the fourth, B, is also cube. This proves the proposition.

**USED:** 8.12, 8.23, 8.8
**Human refs (from References field):** 8.19, 8.23, 8.8
**Jaccard:** 0.500 — AI adds ['8.12']; Human adds ['8.19']

## Proposition 8.26
**Statement:** Similar plane numbers have to one another the ratio which a square number has to a square number.

**Step 1.** Let A and B be similar plane numbers, and let a and c be corresponding sides of them (D7.21). We choose the direct duplicate-ratio route: 8.18 applies immediately to the given similarity, and 8.11 supplies the matching ratio of squares.

**Step 2.** By 8.18, A has to B the ratio duplicate of that which a has to c.

**Step 3.** Let S be the number produced by a multiplying itself, and T the number produced by c multiplying itself. These are square numbers with sides a and c, respectively (D7.18). By 8.11, S has to T the ratio duplicate of that which a has to c.

**Step 4.** These two duplicate ratios are equal. Indeed, a duplicate ratio is the ratio of the extremes of three continued proportionals (D5.9), and two such triples having the same successive ratio have equal ratios of their extremes, by ex aequali (5.22). Therefore A:B = S:T. Since S and T are square numbers, similar plane numbers have to one another the ratio which a square number has to a square number.

**USED:** 5.22, 8.11, 8.18, D5.9, D7.18, D7.21
**Human refs (from References field):** 7.33, 8.18, 8.2
**Jaccard:** 0.125 — AI adds ['5.22', '8.11', 'D5.9', 'D7.18', 'D7.21']; Human adds ['7.33', '8.2']

## Proposition 8.27
**Statement:** Similar solid numbers have to one another the ratio which a cube number has to a cube number.

**Step 1.** Let A and B be similar solid numbers, and let a and b be corresponding sides (D7.21). We choose the triplicate-ratio route: 8.19 applies directly to the given similarity.

**Step 2.** By 8.19, A has to B the triplicate ratio of a to b. Thus, in the continued proportion supplied by that proposition, there are two mean proportional numbers M and N such that
A:M = M:N = N:B = a:b
(8.19; D5.10).

**Step 3.** Form the cubes C = a·a·a and D = b·b·b, whose sides are a and b respectively (D7.19). By 8.12, C has to D the triplicate ratio of a to b. Accordingly, there are two mean proportional numbers U and V such that
C:U = U:V = V:D = a:b
(8.12; D5.10).

**Step 4.** The corresponding successive ratios in the sequences A, M, N, B and C, U, V, D are equal, since each equals a:b (5.11). Therefore, ex aequali, their extremes have the same ratio:
A:B = C:D
(5.22). Since C and D are cube numbers, similar solid numbers have to one another the ratio which a cube number has to a cube number.

**USED:** 5.11, 5.22, 8.12, 8.19, D5.10, D7.19, D7.21
**Human refs (from References field):** 7.33, 8.19, 8.2
**Jaccard:** 0.111 — AI adds ['5.11', '5.22', '8.12', 'D5.10', 'D7.19', 'D7.21']; Human adds ['7.33', '8.2']
