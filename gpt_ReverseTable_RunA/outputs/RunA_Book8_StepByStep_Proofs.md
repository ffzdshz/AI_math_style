# Book 8 of Euclid's Elements — Step-by-Step AI Proofs (Run A)

## Proposition 8.1
**Statement:** If there be as many numbers as we please in continued proportion, and the extremes of them be prime to one another, the numbers are the least of those which have the same ratio with them.

**Step 1.** Let A₁, A₂, …, Aₙ be the given numbers in continued proportion, with A₁ and Aₙ prime to one another. We use the extreme pair, since the coprimality hypothesis applies directly to VII.21: A₁ and Aₙ are the least numbers having their ratio. [7.21]

**Step 2.** Let B₁, B₂, …, Bₙ be any numbers having the same successive ratios as the given numbers. By equality of ratios ex aequali,
B₁ : Bₙ = A₁ : Aₙ.
Since A₁ and Aₙ are the least numbers in this ratio, they measure B₁ and Bₙ respectively the same number of times. Thus, for some positive integer k,
B₁ = kA₁ and Bₙ = kAₙ. [7.14, 7.20]

**Step 3.** For any intermediate index i, apply the same ex aequali result to the sequences ending at Bᵢ and Aᵢ. It gives
B₁ : Bᵢ = A₁ : Aᵢ.
Alternating yields
B₁ : A₁ = Bᵢ : Aᵢ.
Because B₁ is k times A₁, the definition of proportional numbers makes Bᵢ likewise k times Aᵢ. Hence every Bᵢ is kAᵢ, including the extremes already treated. Since k is a positive integer, no corresponding Bᵢ is smaller than Aᵢ. Therefore the given numbers are the least of those which have the same ratio with them. [7.14, 7.13, D7.20]

**USED:** 7.13, 7.14, 7.20, 7.21, D7.20
**Human refs (from References field):** 7.14, 7.20, 7.21
**Jaccard:** 0.600 — AI adds ['7.13', 'D7.20']

## Proposition 8.2
**Statement:** To find numbers in continued proportion, as many as may be prescribed, and the least that are in a given ratio.

**Step 1.** Let the given ratio be A:B, and let the prescribed number of terms be n ≥ 2. By VII.33, find the least numbers a,b having the ratio A:B. By VII.22, a and b are prime to one another. If n = 2, these already answer the problem. For more terms, we choose the coprime-extremes construction, since VIII.1 directly supplies the required leastness criterion. [7.33, 7.22, 8.1]

**Step 2.** Suppose n ≥ 3. By repeated multiplication construct the following n numbers:
T_i = a^(n−1−i)b^i, for i = 0,1,…,n−1.
Thus the list is a^(n−1), a^(n−2)b, …, ab^(n−2), b^(n−1). Powers here denote repeated multiplication, and factors with exponent zero are omitted. These products can be formed for any prescribed finite n. [D7.15]

**Step 3.** For each i = 0,…,n−2, put C_i = a^(n−2−i)b^i. The adjacent terms T_i and T_(i+1) are respectively C_i a and C_i b, rearranging multiplication by VII.16. Since they are obtained by multiplying a and b by the same number, VII.17 gives
T_i:T_(i+1) = a:b = A:B.
The common-factor form makes VII.17 the direct choice here. Consequently all n constructed numbers are in continued proportion with the given ratio. [D7.15, 7.16, 7.17]

**Step 4.** The extreme terms are a^(n−1) and b^(n−1). Since a and b are prime to one another, VII.27, continued through the repeated multiplications, shows that these equal powers are also prime to one another. [7.27]

**Step 5.** The constructed numbers are in continued proportion and their extremes are prime to one another. Therefore VIII.1 shows that they are the least numbers having the same successive ratios. We have thus found as many numbers as prescribed, in continued proportion in the given ratio, and the least such numbers. [8.1]

**USED:** 7.16, 7.17, 7.22, 7.27, 7.33, 8.1, D7.15
**Human refs (from References field):** 7.17, 7.18, 7.22, 7.27, 8.1
**Jaccard:** 0.500 — AI adds ['7.16', '7.33', 'D7.15']; Human adds ['7.18']

## Proposition 8.3
**Statement:** If as many numbers as we please in continued proportion be the least of those which have the same ratio with them, the extremes of them are prime to one another.

**Step 1.** Let A₀, A₁, …, Aₙ (n ≥ 1) be in continued proportion and be the least numbers having their successive ratios. We take the direct route of comparing them with a progression whose extremes are explicitly coprime. By VII.33 choose the least pair p, q such that p:q = A₀:A₁. By VII.22, p and q are prime to one another. [7.33, 7.22]

**Step 2.** Form the n + 1 numbers
Bᵢ = pⁿ⁻ⁱqⁱ, for 0 ≤ i ≤ n,
where a zeroth power denotes the unit. For each i < n, the adjacent terms Bᵢ and Bᵢ₊₁ are obtained by multiplying p and q respectively by the common factor pⁿ⁻ⁱ⁻¹qⁱ. Hence Bᵢ:Bᵢ₊₁ = p:q by VII.17; if that factor is the unit, the equality is immediate. We use VII.17 because it directly preserves a ratio under a common multiplier. Thus the Bᵢ are in continued proportion with the same successive ratios as the Aᵢ. [7.17]

**Step 3.** The extremes of the constructed progression are B₀ = pⁿ and Bₙ = qⁿ. Since p and q are prime to one another, VII.27, continued through the successive powers, shows that pⁿ and qⁿ are prime to one another. For n = 1 this is already the conclusion of Step 1. [7.27, 7.22]

**Step 4.** The constructed progression is therefore in continued proportion and has extremes prime to one another. By VIII.1 it is the least of those having the same ratios. This preceding leastness criterion supplies the required comparison. [8.1]

**Step 5.** The given progression and the constructed progression are both least in the same ratios. Consequently their corresponding terms are equal: leastness gives Aᵢ ≤ Bᵢ and Bᵢ ≤ Aᵢ for every i. In particular, A₀ = pⁿ and Aₙ = qⁿ. By Step 3 these extremes are prime to one another. Therefore the extremes of the given least continued proportion are prime to one another, as required. [8.1, 7.27, 7.22]

**USED:** 7.17, 7.22, 7.27, 7.33, 8.1
**Human refs (from References field):** 7.22, 7.27, 7.33, 8.2
**Jaccard:** 0.500 — AI adds ['7.17', '8.1']; Human adds ['8.2']

## Proposition 8.4
**Statement:** Given as many ratios as we please in least numbers, to find numbers in continued proportion which are the least in the given ratios.

**Step 1.** Write the prescribed ratios, in their given order, as a₁:b₁, …, aₘ:bₘ, each expressed in least numbers. We seek numbers whose successive ratios are these ratios. We choose to construct such a chain first and then apply the general reduction to least proportional numbers of VII.33, since the prescribed ratios need not all be equal. Begin with the chain a₁, b₁. [VII.33]

**Step 2.** Suppose a chain x₀, …, xₖ has already been constructed with its successive ratios equal to the first k prescribed ratios. To incorporate the next ratio aₖ₊₁:bₖ₊₁, replace this chain by

aₖ₊₁x₀, aₖ₊₁x₁, …, aₖ₊₁xₖ, bₖ₊₁xₖ.

Multiplication by aₖ₊₁ preserves each successive ratio within the original chain, by VII.17. The last two numbers have ratio aₖ₊₁:bₖ₊₁, by VII.18, since they are produced by these two multipliers multiplying the same number xₖ. Thus all the required ratios are preserved and the next one is added. Equality with the prescribed ratios follows by V.11. [VII.17, VII.18, V.11]

**Step 3.** Repeat Step 2 until every prescribed ratio has been incorporated. This finite construction produces numbers X₀, …, Xₘ satisfying

Xᵢ₋₁:Xᵢ = aᵢ:bᵢ for every i = 1, …, m.

Each repetition is justified by the multiplication results and equality of ratios used above. [VII.17, VII.18, V.11]

**Step 4.** By VII.33, find numbers N₀, …, Nₘ which have the same mutual ratios as X₀, …, Xₘ and are the least numbers having those ratios. In particular,

Nᵢ₋₁:Nᵢ = Xᵢ₋₁:Xᵢ = aᵢ:bᵢ.

Therefore the numbers N₀, …, Nₘ satisfy every prescribed successive ratio. [VII.33, V.11]

**Step 5.** To verify that they are least among all chains satisfying the prescription, let Y₀, …, Yₘ be any other such chain. By V.11, each successive ratio of the Y-chain equals the corresponding successive ratio of the X-chain. For any i < j, apply VII.14 to the consecutive portions Xᵢ, …, Xⱼ and Yᵢ, …, Yⱼ. It follows ex aequali that Xᵢ:Xⱼ = Yᵢ:Yⱼ. Thus the Y-chain has all the same mutual ratios as the X-chain and belongs to the very class in which VII.33 made the N-chain least. Consequently no other admissible chain has smaller corresponding numbers. Hence N₀, …, Nₘ are the required least numbers in continued proportion in the given ratios. [V.11, VII.14, VII.33]

**USED:** 5.11, 7.14, 7.17, 7.18, 7.33
**Human refs (from References field):** 7.13, 7.20, 7.34, 7.35, D7.20
**Jaccard:** 0.000 — AI adds ['5.11', '7.14', '7.17', '7.18', '7.33']; Human adds ['7.13', '7.20', '7.34', '7.35', 'D7.20']

## Proposition 8.5
**Statement:** Plane numbers have to one another the ratio compounded of the ratios of their sides.

**Step 1.** Let A and B be any plane numbers, with sides a, b and c, d respectively. Thus A = ab and B = cd. Form the intermediate number M = cb. We choose this mixed product so that the common-factor ratio propositions apply directly, without reversing either multiplication. [D7.16]

**Step 2.** Since a and c, multiplying the same number b, produce A and M, respectively, A:M = a:c. Proposition VII.18 applies directly in this orientation. [7.18]

**Step 3.** Since c, multiplying b and d, produces M and B, respectively, M:B = b:d. Here Proposition VII.17 applies directly. [7.17]

**Step 4.** By the definition of compounded ratio, A:B is compounded of A:M and M:B: the sizes of these successive ratios multiply to A/B, since (A/M)(M/B) = A/B. By Steps 2 and 3, these component ratios are a:c and b:d. Therefore the plane numbers A and B have to one another the ratio compounded of the ratios of their sides. [D6.5]

**USED:** 7.17, 7.18, D6.5, D7.16
**Human refs (from References field):** 7.14, 7.17, 8.4
**Jaccard:** 0.167 — AI adds ['7.18', 'D6.5', 'D7.16']; Human adds ['7.14', '8.4']

## Proposition 8.6
**Statement:** If there be as many numbers as we please in continued proportion, and the first do not measure the second, neither will any other measure any other.

**Step 1.** Let A₁, A₂, …, Aₙ be the given numbers in continued proportion, with A₁ not measuring A₂. Every adjacent pair has the ratio A₁:A₂. Consequently, no term measures the next: otherwise, by the definition of proportional numbers, A₁ would be the same part of A₂ and would measure it. [D7.3, D7.20]

**Step 2.** Choose any indices i<j, and put d=j−i. By VII.33, take the least terms B₀, B₁, …, B_d having the same successive ratios as Aᵢ, Aᵢ₊₁, …, Aⱼ. This reduction of the existing block is the natural route; no new progression with a separately prescribed ratio is needed. These least terms are themselves in continued proportion. Moreover, B₀ cannot be a unit: a unit measures B₁, so B₀:B₁=Aᵢ:Aᵢ₊₁ would imply that Aᵢ measures Aᵢ₊₁, contrary to Step 1. [7.33, D7.2, D7.20]

**Step 3.** Since B₀, B₁, …, B_d are the least terms in their continued proportion, their extremes B₀ and B_d are prime to one another. Therefore B₀ does not measure B_d: if it did, B₀, which is not a unit, would be a common measure of both extremes, contrary to their being prime to one another. [8.3, D7.12]

**Step 4.** Applying proportion ex aequali to the two blocks gives Aᵢ:Aⱼ=B₀:B_d. If Aᵢ measured Aⱼ, the definition of proportional numbers would therefore make B₀ measure B_d, contrary to Step 3. Hence Aᵢ does not measure Aⱼ. Since i<j were arbitrary, no term measures any subsequent term, whether adjacent or separated by intervening terms. Thus, if the first does not measure the second, neither will any other measure any other in the continued order. [7.14, D7.3, D7.20]

**USED:** 7.14, 7.33, 8.3, D7.12, D7.2, D7.20, D7.3
**Human refs (from References field):** 7.14, 7.33, 8.3, D7.20
**Jaccard:** 0.571 — AI adds ['D7.12', 'D7.2', 'D7.3']

## Proposition 8.7
**Statement:** If there be as many numbers as we please in continued proportion, and the first measure the last, it will measure the second also.

**Step 1.** Let A₁, A₂, …, Aₙ be numbers in continued proportion, and suppose that A₁ measures Aₙ. Choose the direct contrapositive route through the immediately preceding proposition: if the first does not measure the second, no number in the progression measures another. [8.6]

**Step 2.** If A₁ did not measure A₂, proposition 8.6 would imply that A₁ did not measure Aₙ, contrary to the hypothesis. Therefore A₁ measures A₂, as required. [8.6]

**USED:** 8.6
**Human refs (from References field):** 8.6
**Jaccard:** 1.000 — Perfect match.

## Proposition 8.8
**Statement:** If between two numbers there fall numbers in continued proportion with them, then, however many numbers fall between them in continued proportion, so many will also fall in continued proportion between the numbers which have the same ratio with the original numbers.

**Step 1.** Let A₀, A₁, …, Aₙ₊₁ be numbers in continued proportion, with n numbers between the extremes. Let B and C satisfy B:C = A₀:Aₙ₊₁. By VII.33, choose the least numbers P₀, P₁, …, Pₙ₊₁ having the same corresponding ratios as the A’s. We use this reduction of the whole progression because it retains both its length and its successive ratios. Thus the P’s are themselves in continued proportion. [7.33]

**Step 2.** Since the corresponding successive ratios of the two progressions are equal, their extreme ratios are equal ex aequali. Hence P₀:Pₙ₊₁ = A₀:Aₙ₊₁ = B:C. [7.14]

**Step 3.** The P’s are the least numbers in their continued proportion, so their extremes P₀ and Pₙ₊₁ are prime to one another. Consequently these extremes are the least numbers having their ratio. [8.3, 7.21]

**Step 4.** Since P₀:Pₙ₊₁ = B:C, these least numbers measure B and C respectively the same number of times. Let that common number of times be k. Thus B = kP₀ and C = kPₙ₊₁. [7.20]

**Step 5.** Take each Pᵢ the same k times, obtaining Qᵢ = kPᵢ. If k is one, the Q’s are simply the P’s. Otherwise, multiplication by the same number preserves each successive ratio, so Qᵢ:Qᵢ₊₁ = Pᵢ:Pᵢ₊₁ for every i from 0 through n. Thus the Q’s are in continued proportion. Their extremes are Q₀ = B and Qₙ₊₁ = C, and exactly n terms, Q₁, …, Qₙ, fall between them. Therefore, however many numbers fall in continued proportion between the original numbers, so many also fall between any numbers having the same ratio. [7.17]

**USED:** 7.14, 7.17, 7.20, 7.21, 7.33, 8.3
**Human refs (from References field):** 7.14, 7.20, 7.21, 7.33, 8.3, D7.20
**Jaccard:** 0.714 — AI adds ['7.17']; Human adds ['D7.20']

## Proposition 8.9
**Statement:** If two numbers be prime to one another, and numbers fall between them in continued proportion, then, however many numbers fall between them in continued proportion, so many will also fall between each of them and an unit in continued proportion.

**Step 1.** Let A = X₀, X₁, …, Xᵣ = B be the given continued proportion, with n intervening numbers, so that r = n + 1. Since A and B are prime to one another, this progression is the least among progressions having the same successive ratios. We take this direct least-progression route because the hypothesis supplies exactly the condition required by VIII.1. [8.1]

**Step 2.** Choose the least terms p, q having the ratio X₀ : X₁, by VII.33. Neither can be a unit. For if p were a unit, every term Xᵢ₊₁ would be q times Xᵢ, so A would measure B; if q were a unit, every Xᵢ would be p times Xᵢ₊₁, so B would measure A. Either case contradicts the fact that A and B have only a unit as a common measure. Thus p and q are numbers, and, being the least in their ratio, they are prime to one another by VII.22. [7.33, D7.20, D7.12, 7.22]

**Step 3.** Using repeated multiplication, form the r + 1 numbers
pʳ, pʳ⁻¹q, pʳ⁻²q², …, pqʳ⁻¹, qʳ.
Here powers denote repeated products, and an exponent zero denotes the unit. Each adjacent pair is obtained by multiplying p and q by the same factor: for the pair in positions i and i + 1, that factor is pʳ⁻ⁱ⁻¹qⁱ. Multiplication and its commutativity identify these products with the displayed terms, and VII.17 gives their ratio as p : q. If the factor is a unit, the pair is simply p, q. Consequently this progression has exactly the same successive ratios as the given progression. [D7.15, 7.16, 7.17]

**Step 4.** Since p and q are prime to one another, their corresponding powers pʳ and qʳ are prime to one another by repeated application of VII.27. Therefore the progression constructed in Step 3 is also least in its successive ratios, by VIII.1. Both it and the given progression are least in the same ratios; hence their corresponding terms are equal. In particular,
A = pʳ and B = qʳ.
[7.27, 8.1]

**Step 5.** Now form
1, p, p², …, pʳ = A
and
1, q, q², …, qʳ = B.
In the first sequence each term is the same part of its successor, namely the part determined by multiplication by p; the corresponding assertion holds with q in the second. Thus both sequences are continued proportions. Each contains precisely r − 1 = n numbers between the unit and its final term. Reversing either sequence gives the required continued proportion from A or B to the unit. Therefore, however many numbers fall between the two given numbers in continued proportion, so many also fall between each of them and a unit. [D7.15, D7.20]

**USED:** 7.16, 7.17, 7.22, 7.27, 7.33, 8.1, D7.12, D7.15, D7.20
**Human refs (from References field):** 8.1, 8.2, D7.20
**Jaccard:** 0.200 — AI adds ['7.16', '7.17', '7.22', '7.27', '7.33', 'D7.12', 'D7.15']; Human adds ['8.2']

## Proposition 8.10
**Statement:** If numbers fall between each of two numbers and an unit in continued proportion, however many numbers fall between each of them and an unit in continued proportion, so many also will fall between the numbers themselves in continued proportion.

**Step 1.** Let exactly k numbers fall in continued proportion between the unit and each of the numbers A and B, and put n = k + 1. Write the given chains as
1 = a₀, a₁, …, aₙ = A,
1 = b₀, b₁, …, bₙ = B.
Thus, putting a = a₁ and b = b₁, their continued proportions give, for every 0 ≤ j < n,
aⱼ₊₁ : aⱼ = a : 1 and bⱼ₊₁ : bⱼ = b : 1. [D7.20]

**Step 2.** Since a is a times the unit, aⱼ₊₁ is a times aⱼ; likewise bⱼ₊₁ is b times bⱼ. Consequently,
aⱼ₊₁ = a·aⱼ and bⱼ₊₁ = b·bⱼ.
We therefore take the direct route of constructing mixed products: the given chains already supply the requisite integral multipliers, so no reduction to least terms is needed. [D7.20, D7.15]

**Step 3.** For every i from 0 to n, form
Cᵢ = aₙ₋ᵢ·bᵢ.
A unit factor leaves the other factor unchanged, so C₀ = A and Cₙ = B. This supplies exactly n − 1 = k intermediate numbers, namely C₁, …, Cₙ₋₁. [D7.15]

**Step 4.** For each 0 ≤ i < n, the relations in Step 2 yield
b·Cᵢ = b·(aₙ₋ᵢ·bᵢ)
= b·((a·aₙ₋ᵢ₋₁)·bᵢ)
= a·(aₙ₋ᵢ₋₁·(b·bᵢ))
= a·(aₙ₋ᵢ₋₁·bᵢ₊₁)
= a·Cᵢ₊₁.
Here interchanging factors is justified by VII.16, and regrouping products merely regroups the repeated additions defining multiplication; equal repeated additions give equal wholes. Unit factors, when present, are omitted. [7.16, D7.15, CN2]

**Step 5.** Since Cᵢ·b = Cᵢ₊₁·a, the converse direction of VII.19 gives
Cᵢ : Cᵢ₊₁ = a : b
for every i. Hence A = C₀, C₁, …, Cₙ = B are in continued proportion. There are exactly k numbers between their endpoints, the same number as in each given chain between a number and the unit. Therefore the required number of means falls between A and B in continued proportion. [7.16, 7.19, D7.20]

**USED:** 7.16, 7.19, CN2, D7.15, D7.20
**Human refs (from References field):** 7.17, 7.18, D7.20
**Jaccard:** 0.143 — AI adds ['7.16', '7.19', 'CN2', 'D7.15']; Human adds ['7.17', '7.18']

## Proposition 8.11
**Statement:** Between two square numbers there is one mean proportional number, and the square has to the square the ratio duplicate of that which the side has to the side.

**Step 1.** Let A and B be any two square numbers, with sides a and b respectively. Thus A = a·a and B = b·b. [D7.18]

**Step 2.** Take M = a·b. By commutativity of numerical multiplication, M = b·a also. This product is the direct choice of mean because it shares a side-factor with each square. [7.16]

**Step 3.** Apply the common-multiplier rule directly: multiplying a and b by a gives A and M, so A:M = a:b. Multiplying a and b by b gives M and B, so M:B = a:b. [7.17]

**Step 4.** Since A:M and M:B are both the same as a:b, they are the same as one another. Hence A:M = M:B, and M is a mean proportional between the two squares. [5.11]

**Step 5.** Since A, M, B are proportional, A:B is the duplicate ratio of A:M. But A:M = a:b by Step 3. Therefore the square A has to the square B the ratio duplicate of that which its side a has to the side b. Thus between two square numbers there is one mean proportional number, and the asserted duplicate ratio holds. [D5.9]

**USED:** 5.11, 7.16, 7.17, D5.9, D7.18
**Human refs (from References field):** 7.17, 7.18, D5.9
**Jaccard:** 0.333 — AI adds ['5.11', '7.16', 'D7.18']; Human adds ['7.18']

## Proposition 8.12
**Statement:** Between two cube numbers there are two mean proportional numbers, and the cube has to the cube the ratio triplicate of that which the side has to the side.

**Step 1.** Let A and B be the given cube numbers, with sides a and b. Write xy for the number produced when x multiplies y. Form P = aa, Q = ab, and R = bb; then A = aP and B = bR. We take the direct product construction, checking ratios through common multipliers or common multiplicands. [D7.15, D7.19]

**Step 2.** Since a multiplies a and b to produce P and Q, respectively, P:Q = a:b by VII.17. Since a and b multiply b to produce Q and R, respectively, Q:R = a:b by VII.18. These are the natural choices: VII.17 applies directly to the common multiplier, and VII.18 directly to the common multiplicand, without rearranging products. [7.17, 7.18]

**Step 3.** Construct M = aQ and N = aR. Multiplying P and Q by a gives A:M = P:Q; multiplying Q and R by a gives M:N = Q:R. Hence, by Step 2, A:M = a:b and M:N = a:b. [D7.15, 7.17, 5.11]

**Step 4.** Since a and b multiply R to produce N and B, respectively, N:B = a:b. Consequently A:M = M:N = N:B, so M and N are two mean proportional numbers between the given cubes A and B. [7.18, 5.11]

**Step 5.** Since A, M, N, B are continuously proportional, A:B is the triplicate ratio of A:M. But A:M = a:b. Therefore the cube A has to the cube B the ratio triplicate of that which its side a has to the side b, as required. [D5.10]

**USED:** 5.11, 7.17, 7.18, D5.10, D7.15, D7.19
**Human refs (from References field):** 7.17, 7.18, D5.10
**Jaccard:** 0.500 — AI adds ['5.11', 'D7.15', 'D7.19']

## Proposition 8.13
**Statement:** If there be as many numbers as we please in continued proportion, and each by multiplying itself make some number, the products will be proportional; and, if the original numbers by multiplying the products make certain numbers, the latter will also be proportional.

**Step 1.** Let A, B, C be any three consecutive numbers of the given continued proportion, so A:B = B:C. Write A², B², C² for their respective squares, and A³ = A·A², B³ = B·B², C³ = C·C². We use multiplication to obtain proportional triples and then apply numerical ex aequali: this is the direct choice because every term is a number. [7.17, 7.18, 7.14]

**Step 2.** Introduce the products AB and BC. Multiplication by A and by B, respectively, gives
A²:AB = A:B = B:C = B²:BC. [7.17]
Also, using A and B as multipliers of B, and B and C as multipliers of C, gives
AB:B² = A:B = B:C = BC:C². [7.18]

**Step 3.** Thus the triples A², AB, B² and B², BC, C² have equal corresponding successive ratios. By ex aequali,
A²:B² = B²:C².
Since A, B, C were any consecutive triple, all the squares are in continued proportion. [7.14]

**Step 4.** Introduce the products A·B² and B·C². Multiplication by A and by B, together with Step 3, gives
A³:(A·B²) = A²:B² = B²:C² = B³:(B·C²). [7.17]
Using A and B as multipliers of B², and B and C as multipliers of C², also gives
(A·B²):B³ = A:B = B:C = (B·C²):C³. [7.18]

**Step 5.** Apply ex aequali to the triples A³, A·B², B³ and B³, B·C², C³. It follows that
A³:B³ = B³:C³. [7.14]
Again the consecutive triple was arbitrary, so all the products obtained by multiplying each original number by its square are in continued proportion. With fewer than three original numbers there is no further equality of successive ratios to check. Therefore both the squares and the latter products are proportional, as required.

**USED:** 7.14, 7.17, 7.18
**Human refs (from References field):** 7.14
**Jaccard:** 0.333 — AI adds ['7.17', '7.18']

## Proposition 8.14
**Statement:** If a square measure a square, the side will also measure the side; and, if the side measure the side, the square will also measure the square.

**Step 1.** Let A and B be square numbers with sides a and b, so that A = a·a and B = b·b. Form the mixed product M = a·b. We use this explicit mean because the common-multiplier rule applies directly. If a = b, both assertions are immediate, since equal numbers measure one another once. [D7.18, D7.15]

**Step 2.** Multiplying a and b by a gives A:M = a:b. Multiplying a and b by b gives (b·a):B = a:b; and b·a = a·b = M. Thus
A:M = M:B = a:b,
so A, M, B are in continued proportion. [7.17, 7.16]

**Step 3.** Suppose that the square A measures the square B. Since A, M, B are in continued proportion and the first measures the last, A also measures M. [8.7]

**Step 4.** Since A:M = a:b, the definition of proportional numbers makes a the same part of b that A is of M. Therefore a measures b: the side of the measuring square measures the side of the measured square. [D7.20, D7.3]

**Step 5.** Conversely, suppose that a measures b. From A:M = a:b and M:B = a:b, A is the same part of M, and M the same part of B, that a is of b. Hence A measures M and M measures B. [D7.20, D7.3]

**Step 6.** Consequently M consists of a whole number of copies of A, and B consists of a whole number of copies of M. Replacing each copy of M by its copies of A expresses B as a whole number of copies of A. Thus A measures B. Therefore, if a square measures a square, its side measures the other side; and if the side measures the side, the square measures the square. [D7.15, D7.3]

**USED:** 7.16, 7.17, 8.7, D7.15, D7.18, D7.20, D7.3
**Human refs (from References field):** 8.11, 8.7, D7.20
**Jaccard:** 0.250 — AI adds ['7.16', '7.17', 'D7.15', 'D7.18', 'D7.3']; Human adds ['8.11']

## Proposition 8.15
**Statement:** If a cube number measure a cube number, the side will also measure the side; and, if the side measure the side, the cube will also measure the cube.

**Step 1.** Let A and B be cube numbers with respective sides a and b. Write x·y for the number obtained when x multiplies y. Put c=a·a, d=b·a, and e=b·b; thus A=a·c and B=b·e. Also put X=a·d and Y=a·e. These are products in the sense of the definition of multiplication, and A and B are the given cubes. [D7.15, D7.19]

**Step 2.** By VII.18, c:d=a:b and Y:B=a:b. By VII.17, d:e=a:b; moreover, multiplication of c,d,e by a gives A:X=c:d and X:Y=d:e. Consequently
A:X = X:Y = Y:B = a:b.
Thus A,X,Y,B are in continued proportion. [7.18, 7.17]

**Step 3.** Suppose A measures B. We choose VIII.7 directly, because its hypothesis is precisely measurement of the last term of this chain by the first. It follows that A measures X. Since A:X=a:b, the definition of proportional numbers implies that a measures b the same number of times. Therefore, if a cube measures a cube, its side measures the other side. [8.7, D7.20, D7.3]

**Step 4.** Conversely, suppose a measures b, say b consists of n copies of a. By the proportionalities in Step 2, X consists of n copies of A, Y of n copies of X, and B of n copies of Y. Substituting these repeated sums shows that B consists of n·n·n copies of A; hence A measures B. Therefore, if the side measures the side, the cube also measures the cube. Both assertions are proved. [D7.20, D7.15, D7.3]

**USED:** 7.17, 7.18, 8.7, D7.15, D7.19, D7.20, D7.3
**Human refs (from References field):** 8.11, 8.12, 8.7, D7.20
**Jaccard:** 0.222 — AI adds ['7.17', '7.18', 'D7.15', 'D7.19', 'D7.3']; Human adds ['8.11', '8.12']

## Proposition 8.16
**Statement:** If a square number do not measure a square number, neither will the side measure the side; and, if the side do not measure the side, neither will the square measure the square.

**Step 1.** Let A and B be square numbers with sides a and b, respectively. We take the direct route through VIII.14, which already gives both affirmative implications, and argue by contradiction. Suppose A does not measure B. If a measured b, then A would measure B by the second implication of VIII.14, contrary to the supposition. Therefore a does not measure b. [8.14]

**Step 2.** Suppose now that a does not measure b. If A measured B, then a would measure b by the first implication of VIII.14, again a contradiction. Therefore A does not measure B. Thus, if a square number does not measure a square number, its side does not measure the other's side; and, if the side does not measure the side, neither does the square measure the square. [8.14]

**USED:** 8.14
**Human refs (from References field):** 8.14
**Jaccard:** 1.000 — Perfect match.

## Proposition 8.17
**Statement:** If a cube number do not measure a cube number, neither will the side measure the side; and, if the side do not measure the side, neither will the cube measure the cube.

**Step 1.** Let A and B be cube numbers, with sides a and b respectively. We use 8.15 directly, since it gives precisely the corresponding assertions about measurement. Suppose A does not measure B. If a measured b, then A would measure B by the second assertion of 8.15, contradicting the supposition. Therefore a does not measure b. [8.15]

**Step 2.** Conversely, suppose a does not measure b. If A measured B, then a would measure b by the first assertion of 8.15, again a contradiction. Therefore A does not measure B. Thus, if a cube number does not measure a cube number, neither does its side measure the other's side; and if the side does not measure the side, neither does the cube measure the cube. [8.15]

**USED:** 8.15
**Human refs (from References field):** 8.15
**Jaccard:** 1.000 — Perfect match.

## Proposition 8.18
**Statement:** Between two similar plane numbers there is one mean proportional number; and the plane number has to the plane number the ratio duplicate of that which the corresponding side has to the corresponding side.

**Step 1.** Let A and B be similar plane numbers. Write A = ab and B = cd, where a, b are the sides of A and c, d are the corresponding sides of B. By similarity, a:b = c:d. [D7.16, D7.21]

**Step 2.** By alternation, a:c = b:d. Thus the ratios of the corresponding sides are equal. [7.13]

**Step 3.** Form the number M = cb. We choose this mixed product directly because it shares a factor with each given plane number. Since a and c multiply the same number b, A:M = a:c. Since c multiplies b and d, M:B = b:d. [7.18, 7.17]

**Step 4.** The ratios a:c and b:d are equal by Step 2. Therefore the ratios obtained in Step 3 are equal: A:M = M:B. Hence M is a mean proportional number between A and B, and their common successive ratio is a:c, equally b:d. [5.11]

**Step 5.** Since A, M, B are proportional, A:B is the duplicate ratio of A:M. But A:M = a:c, the ratio of a side of A to the corresponding side of B. Thus between the two similar plane numbers there is one mean proportional number, and the plane number has to the plane number the duplicate ratio of that which a corresponding side has to the corresponding side. [D5.9]

**USED:** 5.11, 7.13, 7.17, 7.18, D5.9, D7.16, D7.21
**Human refs (from References field):** 7.13, 7.17, D5.9, D7.21
**Jaccard:** 0.571 — AI adds ['5.11', '7.18', 'D7.16']

## Proposition 8.19
**Statement:** Between two similar solid numbers there fall two mean proportional numbers; and the solid number has to the similar solid number the ratio triplicate of that which the corresponding side has to the corresponding side.

**Step 1.** Let A and B be similar solid numbers, with corresponding sides a,b,c and d,e,f respectively. Thus A=abc and B=def (D7.17). By similarity, a:b=d:e and b:c=e:f (D7.21). Alternating these proportions gives a:d=b:e and b:e=c:f (7.13).

**Step 2.** Choose the direct mixed-product construction, since the proportional sides already supply the required ratios. Form the numbers M=dbc and N=dec by multiplication (D7.15).

**Step 3.** Multiplication by the common factors bc, dc, and de respectively gives
A:M=a:d,
M:N=b:e,
N:B=c:f
by 7.17. In these product expressions, multiplication is repeated addition (D7.15), and factors may be interchanged by 7.16.

**Step 4.** The three corresponding-side ratios are equal by Step 1. Hence the ratios in Step 3 are equal (5.11), so
A:M=M:N=N:B.
Therefore M and N are two mean proportional numbers between A and B.

**Step 5.** Since A,M,N,B are continuously proportional, A has to B the triplicate ratio of that which A has to M (D5.10). But A:M=a:d by Step 3, and this also equals b:e and c:f. Thus the solid number has to the similar solid number the ratio triplicate of that which any corresponding side has to its corresponding side. Both assertions are proved.

**USED:** 5.11, 7.13, 7.16, 7.17, D5.10, D7.15, D7.17, D7.21
**Human refs (from References field):** 7.13, 7.17, 7.18, 8.18, D5.10, D7.21
**Jaccard:** 0.400 — AI adds ['5.11', '7.16', 'D7.15', 'D7.17']; Human adds ['7.18', '8.18']

## Proposition 8.20
**Statement:** If one mean proportional number fall between two numbers, the numbers will be similar plane numbers.

**Step 1.** Let B be a mean proportional between A and C, so that A:B = B:C. By VII.33, choose the least numbers D, E having the ratio A:B. We take this least-pair route because the same pair can be applied directly to both given equal ratios. [7.33]

**Step 2.** Since D:E = A:B, VII.20 gives a number p such that A = Dp and B = Ep. Since also D:E = B:C, the same proposition gives a number q such that B = Dq and C = Eq. [7.20]

**Step 3.** The two expressions for B give Ep = Dq. By commutativity of multiplication, pE = Dq. Therefore, by the converse direction of VII.19, D:p = E:q. [7.16, 7.19]

**Step 4.** Since A = Dp and C = Eq, A and C are plane numbers with sides D, p and E, q, respectively. Their sides are proportional by Step 3, so they are similar plane numbers. Thus, if one mean proportional number falls between two numbers, those numbers are similar plane numbers. [D7.16, D7.21]

**USED:** 7.16, 7.19, 7.20, 7.33, D7.16, D7.21
**Human refs (from References field):** 7.13, 7.17, 7.20, 7.33
**Jaccard:** 0.250 — AI adds ['7.16', '7.19', 'D7.16', 'D7.21']; Human adds ['7.13', '7.17']

## Proposition 8.21
**Statement:** If two mean proportional numbers fall between two numbers, the numbers are similar solid numbers.

**Step 1.** Let A, B, C, D be numbers such that A:B = B:C = C:D. By VII.33, take the least numbers p, q having the ratio A:B. By VII.22, p and q are prime to one another. We use this least consecutive ratio because its cubes will provide coprime representatives of the ratio of the extremes. [7.33, 7.22]

**Step 2.** Form the four products p³, p²q, pq², q³, with powers denoting repeated multiplication. Multiplying p and q respectively by p², pq, and q² gives
p³:p²q = p:q,
p²q:pq² = p:q,
pq²:q³ = p:q.
Here products are regrouped according to the definition of multiplication and their factors interchanged by VII.16; the ratio equalities follow from VII.17. Thus these four products have the same successive ratios as A, B, C, D. [D7.15, 7.16, 7.17]

**Step 3.** Apply VII.14, the numerical ex aequali rule appropriate to these two four-term sequences. It follows that
A:D = p³:q³. [7.14]

**Step 4.** Since p and q are prime to one another, their cubes p³ and q³ are prime to one another by VII.27. Therefore they are the least numbers in their ratio by VII.21. By VII.20, they measure A and D respectively the same number of times. Consequently, for one common multiplier k, possibly the unit,
A = kp³ and D = kq³. [7.27, 7.21, 7.20]

**Step 5.** Regrouping these products gives
A = p·p·(kp),     D = q·q·(kq).
Hence A and D are solid numbers with sides p, p, kp and q, q, kq respectively. [D7.15, 7.16, D7.17]

**Step 6.** By VII.17, kp:kq = p:q; if k is the unit, this equality is immediate. Thus the corresponding sides satisfy
p:q = p:q = kp:kq.
The sides of the two solid numbers are therefore proportional, so A and D are similar solid numbers by Definition VII.21. Hence, if two mean proportional numbers fall between two numbers, those numbers are similar solid numbers. [7.17, D7.21]

**USED:** 7.14, 7.16, 7.17, 7.20, 7.21, 7.22, 7.27, 7.33, D7.15, D7.17, D7.21
**Human refs (from References field):** 7.14, 7.18, 7.20, 7.21, 7.33, 8.2, 8.20, 8.3
**Jaccard:** 0.267 — AI adds ['7.16', '7.17', '7.22', '7.27', 'D7.15', 'D7.17', 'D7.21']; Human adds ['7.18', '8.2', '8.20', '8.3']

## Proposition 8.22
**Statement:** If three numbers be in continued proportion, and the first be square, the third will also be square.

**Step 1.** Let A, B, C be numbers in continued proportion, so A:B = B:C, and suppose A is square. Write A = a², where a is its side. [D7.18]

**Step 2.** By the equality of products of the extremes and means, AC = B². Hence a²C = B², so the square a² measures the square B². We take the direct square-divisibility route, since this equality supplies precisely its hypothesis. [7.19]

**Step 3.** Since a² measures B², its side a measures the side B. Therefore write B = ad, where d is the integral multiplier. [8.14, D7.15]

**Step 4.** Substituting into a²C = B² gives a²C = (ad)² = a²d². Cancelling the positive factor a² yields C = d². Thus C is equal multiplied by equal, and is therefore square, as required. [D7.15, D7.18]

**USED:** 7.19, 8.14, D7.15, D7.18
**Human refs (from References field):** 8.20
**Jaccard:** 0.000 — AI adds ['7.19', '8.14', 'D7.15', 'D7.18']; Human adds ['8.20']

## Proposition 8.23
**Statement:** If four numbers be in continued proportion, and the first be cube, the fourth will also be cube.

**Step 1.** Let the four numbers be A, B, C, D, with A:B = B:C = C:D. Since A is a cube, write A = a³. Throughout, powers denote repeated multiplication. [D7.15, D7.19]

**Step 2.** Choose the least terms p, q of the common ratio, so that A:B = B:C = C:D = p:q. Such least terms are obtained by VII.33 and are prime to one another by VII.22. A least term may be the unit; those cases are treated explicitly below. We choose this route because the cubes of the least terms will provide a cube divisor of A, allowing a direct passage to its side. [7.33, 7.22]

**Step 3.** By the equality of cross-products of proportional numbers,
pB = qA,  pC = qB,  pD = qC.
Successive substitution therefore gives
p³D = q³A.
Equivalently, A:D = p³:q³. [7.19; D7.15]

**Step 4.** If p and q both exceed the unit, their cubes are prime to one another by VII.27. Hence p³ and q³ are the least numbers in their ratio by VII.21. Since A:D = p³:q³, VII.20 shows that p³ measures A. If p is the unit, the same divisibility is immediate; if q is the unit, it follows directly from p³D = A. Thus in every case p³ measures A = a³. [7.27, 7.21, 7.20]

**Step 5.** Since the cube p³ measures the cube a³, its side p measures the side a by VIII.15. When p is the unit this is immediate as well. Consequently a = pk for some whole multiplier k, possibly the unit. This is the direct application of cube divisibility appropriate to the divisor established in Step 4. [8.15; D7.15]

**Step 6.** Substitute a = pk and A = a³ into the identity from Step 3:
p³D = q³(pk)³ = p³(qk)³.
Cancelling the positive factor p³ gives D = (qk)³. Thus D is contained by three equal numbers and is a cube. Therefore, if four numbers are in continued proportion and the first is a cube, the fourth is also a cube. [D7.15, D7.19]

**USED:** 7.19, 7.20, 7.21, 7.22, 7.27, 7.33, 8.15, D7.15, D7.19
**Human refs (from References field):** 8.21
**Jaccard:** 0.000 — AI adds ['7.19', '7.20', '7.21', '7.22', '7.27', '7.33', '8.15', 'D7.15', 'D7.19']; Human adds ['8.21']

## Proposition 8.24
**Statement:** If two numbers have to one another the ratio which a square number has to a square number, and the first be square, the second will also be square.

**Step 1.** Let A and B be numbers such that A:B=C:D, where C and D are square numbers, and suppose A is square. Choose the square-number mean-proportional route, since it applies directly to the given comparison numbers. By 8.11, there is a number E such that C:E=E:D.

**Step 2.** Since one mean proportional falls between C and D, and A:B=C:D, proposition 8.8 gives one mean proportional F between A and B. Thus A:F=F:B, so A, F, B are in continued proportion. [8.8]

**Step 3.** Three numbers are therefore in continued proportion, and their first, A, is square. By 8.22, their third, B, is also square. Hence the second of the two given numbers is square, as required.

**USED:** 8.11, 8.22, 8.8
**Human refs (from References field):** 8.18, 8.22, 8.8
**Jaccard:** 0.500 — AI adds ['8.11']; Human adds ['8.18']

## Proposition 8.25
**Statement:** If two numbers have to one another the ratio which a cube number has to a cube number, and the first be cube, the second will also be cube.

**Step 1.** Let A and B be numbers such that A:B = C:D, where C and D are cube numbers, and suppose that A is a cube. Choose the direct route through two mean proportionals, since the given comparison numbers are cubes. By VIII.12, there are numbers E and F such that C:E = E:F = F:D. [8.12]

**Step 2.** Since A:B = C:D, and two numbers fall between C and D in continued proportion, VIII.8 gives two numbers G and H between A and B in continued proportion. Thus A:G = G:H = H:B. [8.8]

**Step 3.** The four numbers A, G, H, B are therefore in continued proportion, and the first, A, is a cube. By VIII.23, the fourth, B, is also a cube, as required. [8.23]

**USED:** 8.12, 8.23, 8.8
**Human refs (from References field):** 8.19, 8.23, 8.8
**Jaccard:** 0.500 — AI adds ['8.12']; Human adds ['8.19']

## Proposition 8.26
**Statement:** Similar plane numbers have to one another the ratio which a square number has to a square number.

**Step 1.** Let A and B be similar plane numbers, and let a and c be corresponding sides. Use the duplicate-ratio conclusion of VIII.18 directly, since it describes the required ratio: A:B is the duplicate of a:c. [8.18]

**Step 2.** Form S = a·a and T = c·c. These are square numbers, with sides a and c respectively. [D7.18]

**Step 3.** The ratio S:T is the duplicate of the ratio of their sides, a:c. [8.11]

**Step 4.** Thus A:B and S:T are both the same duplicate ratio of a:c. Ratios which are the same with the same ratio are the same with one another; hence A:B = S:T. Since S and T are square numbers, similar plane numbers have to one another the ratio which a square number has to a square number. [5.11]

**USED:** 5.11, 8.11, 8.18, D7.18
**Human refs (from References field):** 7.33, 8.18, 8.2
**Jaccard:** 0.167 — AI adds ['5.11', '8.11', 'D7.18']; Human adds ['7.33', '8.2']

## Proposition 8.27
**Statement:** Similar solid numbers have to one another the ratio which a cube number has to a cube number.

**Step 1.** Let A and B be similar solid numbers, and let a and b be corresponding sides. Choose the direct triplicate-ratio route: by VIII.19, A has to B the triplicate ratio of that which a has to b. [8.19]

**Step 2.** Form C = a·a·a and D = b·b·b. These are cube numbers with sides a and b, respectively. [D7.19] For these cubes, use the earlier, cube-specific proposition VIII.12: C has to D the triplicate ratio of that which a has to b. [8.12]

**Step 3.** Thus A:B and C:D are both the same triplicate ratio of a:b. Ratios which are the same with the same ratio are the same with one another, so A:B = C:D. [5.11] Since C and D are cube numbers, similar solid numbers have to one another the ratio which a cube number has to a cube number.

**USED:** 5.11, 8.12, 8.19, D7.19
**Human refs (from References field):** 7.33, 8.19, 8.2
**Jaccard:** 0.167 — AI adds ['5.11', '8.12', 'D7.19']; Human adds ['7.33', '8.2']
