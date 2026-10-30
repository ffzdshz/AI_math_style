# Book 8 of Euclid's Elements — Step-by-Step AI Proofs (Run C)

## Proposition 8.1
**Statement:** If there be as many numbers as we please in continued proportion, and the extremes of them be prime to one another, the numbers are the least of those which have the same ratio with them.

**Step 1.** Let A1, A2, ..., An be as many numbers as we please in continued proportion, and let the extremes A1 and An be prime to one another. We must show that A1, A2, ..., An are the least numbers of those which have the same ratio with them.

**Step 2.** By 7.33, we can find numbers B1, B2, ..., Bn which are the least of those having the same ratio as A1, A2, ..., An. Since these are the least, either the Bi equal the Ai respectively, or the Bi are less than the Ai respectively.

**Step 3.** Since B1, B2, ..., Bn are the least in the same continued proportion as A1, A2, ..., An, each consecutive pair Bi, Bi+1 are the least numbers in the ratio Ai : Ai+1. By 7.20, the least numbers of those which have the same ratio measure those which have the same ratio the same number of times. Applying this to the first consecutive pair: B1 measures A1 and B2 measures A2, and A1/B1 = A2/B2.

**Step 4.** Applying 7.20 similarly to the second consecutive pair B2, B3 and A2, A3: B2 measures A2 and B3 measures A3, and A2/B2 = A3/B3. Continuing this process for each consecutive pair through the entire sequence, we obtain A1/B1 = A2/B2 = A3/B3 = ... = An/Bn. Let this common value be m, so that Ai = m * Bi for each i.

**Step 5.** In particular, A1 = m * B1 and An = m * Bn. Therefore m measures both A1 and An.

**Step 6.** But A1 and An are prime to one another by hypothesis, meaning by D7.12 they are measured by a unit alone as a common measure. Since m measures both A1 and An, m must be a unit, that is, m = 1.

**Step 7.** Therefore Ai = 1 * Bi = Bi for each i from 1 to n. Hence A1, A2, ..., An are themselves the least numbers of those which have the same ratio with them. Q.E.D.

**USED:** 7.20, 7.33, D7.12
**Human refs (from References field):** 7.14, 7.20, 7.21
**Jaccard:** 0.200 — AI adds ['7.33', 'D7.12']; Human adds ['7.14', '7.21']

## Proposition 8.2
**Statement:** To find numbers in continued proportion, as many as may be prescribed, and the least that are in a given ratio.

**Step 1.** Let the given ratio be that of A to B, and let the number of terms in continued proportion required be n. We must find the least n numbers in continued proportion having the ratio A:B.

**Step 2.** By 7.33, reduce A:B to their least terms; call these least terms a and b. Since a and b are the least numbers having the ratio A:B, they are prime to one another [7.22].

**Step 3.** First consider the case n = 2. The least two numbers in the ratio a:b are a and b themselves, which are already in least terms [7.33]. So the result holds for two terms.

**Step 4.** Now consider n = 3. We seek the least three numbers in continued proportion with ratio a:b. Form the products: let the first term be a multiplied by a (that is, a*a), the second term be a multiplied by b (that is, a*b), and the third term be b multiplied by b (that is, b*b) [D7.15]. Then a*a : a*b = a : b [7.17], and a*b : b*b = a : b [7.17]. So the three numbers a*a, a*b, b*b are in continued proportion with ratio a:b.

**Step 5.** We must show these are the least such. Since a and b are prime to one another [Step 2], a*a and b*b are prime to one another [7.27]. Now a*a, a*b, b*b are in continued proportion, and the extremes a*a and b*b are prime to one another. Therefore, by 8.1, these are the least numbers in continued proportion having the same ratio. This establishes the case n = 3.

**Step 6.** For the general case of n terms, proceed by successive multiplication. Having found the least (n-1) terms in continued proportion with ratio a:b, say c_1, c_2, ..., c_{n-1}, we construct n terms as follows: multiply each of c_1, c_2, ..., c_{n-1} by a to obtain a*c_1, a*c_2, ..., a*c_{n-1}, and adjoin b*c_{n-1} as the last term [D7.15].

**Step 7.** Since c_1 : c_2 = a : b and in general c_i : c_{i+1} = a : b for each consecutive pair, multiplying each c_i by the same number a preserves all these ratios: a*c_i : a*c_{i+1} = c_i : c_{i+1} = a : b [7.17]. For the last pair, a*c_{n-1} : b*c_{n-1} = a : b [7.20], since c_{n-1} is a common factor. Therefore the n numbers a*c_1, a*c_2, ..., a*c_{n-1}, b*c_{n-1} are in continued proportion with ratio a:b.

**Step 8.** Now we show these are the least such n numbers. By the construction, c_1 = a^{n-2} and c_{n-1} = b^{n-2} (in general, the sequence of (n-1) least terms consists of a^{n-2}, a^{n-3}*b, ..., b^{n-2}). So the first of the n terms is a*c_1 = a^{n-1} and the last is b*c_{n-1} = b^{n-1}. Since a and b are prime to one another [Step 2], by repeated application of 7.27, a^{n-1} and b^{n-1} are prime to one another. The n numbers are in continued proportion, and their extremes are prime to one another. Therefore, by 8.1, they are the least numbers in continued proportion having ratio a:b.

**Step 9.** Thus we have found numbers in continued proportion, as many as prescribed, and the least that are in the given ratio. Q.E.F.

**USED:** 7.17, 7.20, 7.22, 7.27, 7.33, 8.1, D7.15
**Human refs (from References field):** 7.17, 7.18, 7.22, 7.27, 8.1
**Jaccard:** 0.500 — AI adds ['7.20', '7.33', 'D7.15']; Human adds ['7.18']

## Proposition 8.3
**Statement:** If as many numbers as we please in continued proportion be the least of those which have the same ratio with them, the extremes of them are prime to one another.

**Step 1.** Let A, B, C, ..., K be as many numbers as we please in continued proportion, and let them be the least of those which have the same ratio with them. We must show that the extremes A and K are prime to one another.

**Step 2.** Consider the ratio A : B. By 7.33, there exist least numbers e, f in the ratio A : B, so that A : B = e : f and e, f are the least numbers having this ratio.

**Step 3.** Since e and f are the least numbers having the ratio e : f, by 7.22 they are prime to one another.

**Step 4.** By 8.2, we can find the least numbers in continued proportion having the ratio e : f with the same number of terms as A, B, ..., K. Let these be the numbers P_1, P_2, ..., P_n constructed by 8.2.

**Step 5.** Since A : B = e : f, the numbers A, B, ..., K are in continued proportion with the same ratio e : f and the same number of terms. But A, B, ..., K are by hypothesis the least numbers in continued proportion having this ratio. Likewise, P_1, P_2, ..., P_n are the least such numbers by 8.2. Therefore A = P_1, B = P_2, ..., K = P_n.

**Step 6.** By the construction in 8.2, the extremes of the least continued proportion with ratio e : f in n terms are: the first term is e multiplied by itself (n - 1) times, and the last term is f multiplied by itself (n - 1) times. That is, A = e^(n-1) and K = f^(n-1).

**Step 7.** Since e and f are prime to one another (Step 3), by 7.27, e multiplied by itself gives e^2, and f multiplied by itself gives f^2, and e^2 and f^2 are prime to one another. Again by 7.27, if the original numbers e, f multiply these products e^2, f^2, the results e^3, f^3 are also prime to one another. Continuing in this manner, e^(n-1) and f^(n-1) are prime to one another.

**Step 8.** Therefore A and K, being equal to e^(n-1) and f^(n-1) respectively, are prime to one another. This is what was to be proved.

**USED:** 7.22, 7.27, 7.33, 8.2
**Human refs (from References field):** 7.22, 7.27, 7.33, 8.2
**Jaccard:** 1.000 — Perfect match.

## Proposition 8.4
**Statement:** Given as many ratios as we please in least numbers, to find numbers in continued proportion which are the least in the given ratios.

**Step 1.** Let the given ratios in least numbers be A:B, C:D, and E:F. We wish to find numbers in continued proportion which are the least having these successive ratios. (The argument generalizes to any number of given ratios.)

**Step 2.** By 7.34, find G, the least number measured by both B and C (that is, the least common multiple of B and C). Then B measures G; let B measure G according to H, so that B * H = G. Likewise C measures G; let C measure G according to K, so that C * K = G. [7.34, D7.15]

**Step 3.** Since B * H = G, by 7.17, A * H is to B * H as A is to B. That is, A * H : G = A : B. Similarly, since C * K = G, by 7.17, G : D * K = C : D. [7.17]

**Step 4.** Set L = A * H, M = G, and N = D * K. Then L : M = A : B and M : N = C : D, so L, M, N are in continued proportion with the first two given ratios.

**Step 5.** Now chain the next ratio. By 7.34, find O, the least common multiple of N and E. Then N measures O; let N measure O according to P, so that N * P = O. Likewise E measures O; let E measure O according to Q, so that E * Q = O. [7.34]

**Step 6.** By 7.17, multiplying each of L, M, N by P preserves all ratios: L * P : M * P = L : M = A : B, and M * P : N * P = M : N = C : D. Also N * P = O, and by 7.17, O : F * Q = E : F. [7.17]

**Step 7.** Thus the numbers L * P, M * P, O, F * Q are in continued proportion with ratios A : B, C : D, E : F respectively. This construction extends to any number of given ratios by iterating the chaining procedure.

**Step 8.** It remains to show these are the least such numbers. Suppose there exist smaller numbers R, S, T, U in continued proportion with the same ratios A : B, C : D, E : F. Since A : B is in least numbers and R : S = A : B, by 7.20, A measures R and B measures S. Similarly, since C : D is in least terms and S : T = C : D, C measures S and D measures T. [7.20]

**Step 9.** Since B measures S and C measures S, S is a common multiple of B and C. But G is the least common multiple of B and C (by 7.34). Therefore G measures S, by 7.35. [7.35]

**Step 10.** Since G measures S, let S = G * r for some number r. Since R : S = A : B = L : M, and S = G * r while M = G, we have R = L * r by 7.17 and 7.20. Similarly T = N * r. [7.17, 7.20]

**Step 11.** Continuing the chain: since D measures T and E measures T (as T plays the role of the junction for the next ratio), the same argument via 7.34 and 7.35 shows that O measures the corresponding term in R, S, T, U. Specifically, since T = N * r and the next junction requires E to measure T and the LCM O of N and E to divide the corresponding scaled term, we obtain that U = F * Q * r (or the corresponding scaled value), so each of R, S, T, U is r times the corresponding constructed number.

**Step 12.** Since R, S, T, U are numbers (positive integers), r is a positive integer, so r >= 1. If r = 1, then R, S, T, U equal our constructed numbers. If r > 1, then R, S, T, U are strictly larger than our constructed numbers, contradicting the assumption that they are smaller. Therefore our constructed numbers are the least in continued proportion having the given ratios. [D7.2, D7.5]

**Step 13.** Therefore, given as many ratios as we please in least numbers, we have found numbers in continued proportion which are the least in the given ratios. Q.E.F.

**USED:** 7.17, 7.20, 7.34, 7.35, D7.15, D7.2, D7.5
**Human refs (from References field):** 7.13, 7.20, 7.34, 7.35, D7.20
**Jaccard:** 0.333 — AI adds ['7.17', 'D7.15', 'D7.2', 'D7.5']; Human adds ['7.13', 'D7.20']

## Proposition 8.5
**Statement:** Plane numbers have to one another the ratio compounded of the ratios of their sides.

**Step 1.** Let A and C be plane numbers. By D7.16, A is the product of two numbers which are its sides; let A = a * b, where a and b are the sides of A. Similarly, let C = c * d, where c and d are the sides of C.

**Step 2.** Consider the number E = a * d, formed by multiplying the side a of A by the side d of C.

**Step 3.** Since the number a multiplies both b and d to produce A = a * b and E = a * d respectively, by 7.17, A : E = b : d. That is, the ratio of A to E equals the ratio of the side b to the side d.

**Step 4.** Since the numbers a and c each multiply d to produce E = a * d and C = c * d respectively, by 7.18, E : C = a : c. That is, the ratio of E to C equals the ratio of the side a to the side c.

**Step 5.** We now have three numbers A, E, C such that A : E = b : d and E : C = a : c. By the definition of compounded ratio (D6.5), the ratio A : C is compounded of the ratios A : E and E : C, that is, compounded of b : d and a : c.

**Step 6.** But b : d and a : c are precisely the ratios of the sides of the plane numbers A and C. Therefore the plane numbers A and C have to one another the ratio compounded of the ratios of their sides. Q.E.D.

**USED:** 7.17, 7.18, D6.5, D7.16
**Human refs (from References field):** 7.14, 7.17, 8.4
**Jaccard:** 0.167 — AI adds ['7.18', 'D6.5', 'D7.16']; Human adds ['7.14', '8.4']

## Proposition 8.6
**Statement:** If there be as many numbers as we please in continued proportion, and the first do not measure the second, neither will any other measure any other.

**Step 1.** Let A_1, A_2, ..., A_n be as many numbers as we please in continued proportion, so that A_1 : A_2 = A_2 : A_3 = ... = A_{n-1} : A_n, and suppose that A_1 does not measure A_2. We must show that no term measures any later term.

**Step 2.** Suppose, for the sake of contradiction, that some A_i measures A_j, where 1 <= i < j <= n.

**Step 3.** By 7.33, find p, q the least numbers in the ratio A_1 : A_2. By 7.22, since p and q are the least numbers in their ratio, p and q are prime to one another.

**Step 4.** By 8.2, find the least numbers in continued proportion with ratio p : q and having (j - i + 1) terms. Call these e_1, e_2, ..., e_{j-i+1}. Then e_1 : e_2 = e_2 : e_3 = ... = p : q = A_1 : A_2.

**Step 5.** By 8.1, since e_1, e_2, ..., e_{j-i+1} are the least numbers in continued proportion, the extremes e_1 and e_{j-i+1} are prime to one another.

**Step 6.** Now A_i, A_{i+1}, ..., A_j are also in continued proportion with the same ratio A_1 : A_2, and their consecutive ratios equal those of the e-sequence. That is, e_1 : e_2 = A_i : A_{i+1}, e_2 : e_3 = A_{i+1} : A_{i+2}, and so on. Therefore, by 7.14 (ex aequali for numbers), the ratio of extremes is the same: e_1 : e_{j-i+1} = A_i : A_j.

**Step 7.** Since e_1 and e_{j-i+1} are prime to one another (Step 5), by 7.21 they are the least numbers in the ratio e_1 : e_{j-i+1}, which equals A_i : A_j.

**Step 8.** By 7.20, since e_1 and e_{j-i+1} are the least numbers in ratio A_i : A_j, they measure A_i and A_j respectively: there exists a number m such that A_i = m * e_1 and A_j = m * e_{j-i+1}.

**Step 9.** Since A_i measures A_j (our supposition in Step 2), we have A_j = k * A_i for some number k. Substituting from Step 8: m * e_{j-i+1} = k * m * e_1, so e_{j-i+1} = k * e_1, which means e_1 measures e_{j-i+1}.

**Step 10.** But e_1 and e_{j-i+1} are prime to one another (Step 5). The only number that is prime to another and yet measures it is the unit. Therefore e_1 = 1.

**Step 11.** Since e_1 : e_2 = p : q (Step 4), and e_1 = 1, we have 1 : e_2 = p : q. Since p and q are the least in ratio A_1 : A_2 (Step 3), and since 1 and e_2 are in the same ratio, by 7.20 p measures 1. The only number that measures 1 is the unit itself, so p = 1.

**Step 12.** Since p = 1 and p : q = A_1 : A_2, by 7.20, p measures A_1 and q measures A_2 with the same multiplier: A_1 = m' * 1 = m' and A_2 = m' * q for some m'. Thus A_2 = A_1 * q, which means A_1 measures A_2.

**Step 13.** This contradicts the hypothesis that A_1 does not measure A_2. Therefore our supposition in Step 2 is false, and no term of the continued proportion measures any later term. Q.E.D.

**USED:** 7.14, 7.20, 7.21, 7.22, 7.33, 8.1, 8.2
**Human refs (from References field):** 7.14, 7.33, 8.3, D7.20
**Jaccard:** 0.222 — AI adds ['7.20', '7.21', '7.22', '8.1', '8.2']; Human adds ['8.3', 'D7.20']

## Proposition 8.7
**Statement:** If there be as many numbers as we please in continued proportion, and the first measure the last, it will measure the second also.

**Step 1.** Let A_1, A_2, ..., A_n be as many numbers as we please in continued proportion, and let A_1 measure A_n.

**Step 2.** Suppose, for the sake of contradiction, that A_1 does not measure A_2.

**Step 3.** Since A_1, A_2, ..., A_n are numbers in continued proportion and A_1 does not measure A_2, then by Proposition 8.6, neither will any other of the terms measure any other. In particular, A_1 does not measure A_n.

**Step 4.** But this contradicts our hypothesis that A_1 measures A_n.

**Step 5.** Therefore the supposition is false, and A_1 must measure A_2. Q.E.D.

**USED:** 8.6
**Human refs (from References field):** 8.6
**Jaccard:** 1.000 — Perfect match.

## Proposition 8.8
**Statement:** If between two numbers there fall numbers in continued proportion with them, then, however many numbers fall between them in continued proportion, so many will also fall in continued proportion between the numbers which have the same ratio with the original numbers.

**Step 1.** Let A and B be two numbers, and let C1, C2, ..., Cn fall between them in continued proportion, so that A, C1, C2, ..., Cn, B are all in continued proportion (n+2 terms total). Let D and E be numbers such that A:B = D:E. We must show that there also fall n numbers in continued proportion between D and E.

**Step 2.** Since A, C1, C2, ..., Cn, B are in continued proportion, the ratio A:C1 = C1:C2 = ... = Cn:B. By 7.33, take F and G, the least numbers in the ratio A:C1.

**Step 3.** By 8.2, find the least numbers in continued proportion with n+2 terms in the ratio F:G. Call these F0, F1, F2, ..., Fn, F(n+1), so that F0:F1 = F1:F2 = ... = Fn:F(n+1) = F:G = A:C1.

**Step 4.** Since F0, F1, ..., F(n+1) are the least numbers in continued proportion in the ratio F:G, by 8.1 the extremes F0 and F(n+1) are prime to one another.

**Step 5.** Now A, C1, C2, ..., Cn, B are in continued proportion in the same ratio F:G, and F0, F1, ..., F(n+1) are the least such. Since A:C1 = F0:F1, and A:B is the ratio compounded of the n+1 equal ratios A:C1, while F0:F(n+1) is the ratio compounded of the n+1 equal ratios F0:F1, and these individual ratios are equal, it follows that A:B = F0:F(n+1). Similarly, the terms A, C1, ..., Cn, B are equimultiples of F0, F1, ..., F(n+1) respectively. By 7.20, since F0 and F(n+1) are the least numbers in the ratio A:B, they measure A and B the same number of times. Let A = m * F0 and B = m * F(n+1) for some number m, and correspondingly Ci = m * Fi for each i.

**Step 6.** Since A:B = D:E (given) and A:B = F0:F(n+1) (from Step 5), we have F0:F(n+1) = D:E by CN1. Since F0 and F(n+1) are prime to one another (Step 4), and F0, F(n+1) are the least numbers in the ratio D:E, by 7.20 F0 measures D and F(n+1) measures E the same number of times. Let D = p * F0 and E = p * F(n+1) for some number p.

**Step 7.** Define the numbers G1 = p * F1, G2 = p * F2, ..., Gn = p * Fn. We claim that D, G1, G2, ..., Gn, E are in continued proportion.

**Step 8.** For each consecutive pair in the sequence F0, F1, F2, ..., F(n+1), we have the ratio Fi:F(i+1) = F:G. By 7.17, since the number p multiplies both Fi and F(i+1), we have p * Fi : p * F(i+1) = Fi : F(i+1). Therefore D:G1 = p*F0:p*F1 = F0:F1 = F:G, and G1:G2 = p*F1:p*F2 = F1:F2 = F:G, and so on through Gn:E = p*Fn:p*F(n+1) = Fn:F(n+1) = F:G.

**Step 9.** Thus D, G1, G2, ..., Gn, E are all in continued proportion, and the count of numbers falling between D and E is n, which is the same as the count of numbers that fell between A and B.

**Step 10.** Therefore, if between two numbers there fall numbers in continued proportion with them, however many numbers fall between them in continued proportion, so many will also fall in continued proportion between numbers which have the same ratio with the original numbers. Q.E.D.

**USED:** 7.17, 7.20, 7.33, 8.1, 8.2, CN1
**Human refs (from References field):** 7.14, 7.20, 7.21, 7.33, 8.3, D7.20
**Jaccard:** 0.200 — AI adds ['7.17', '8.1', '8.2', 'CN1']; Human adds ['7.14', '7.21', '8.3', 'D7.20']

## Proposition 8.9
**Statement:** If two numbers be prime to one another, and numbers fall between them in continued proportion, then, however many numbers fall between them in continued proportion, so many will also fall between each of them and an unit in continued proportion.

**Step 1.** Let A and B be two numbers prime to one another, and let C1, C2, ..., Cn be numbers falling between A and B in continued proportion, so that A, C1, C2, ..., Cn, B form n+2 terms in continued proportion. We are to show that n numbers also fall between A and 1 in continued proportion, and n numbers fall between B and 1 in continued proportion.

**Step 2.** Let the ratio A:C1 be reduced to its least terms d:e, so that A:C1 :: d:e and d, e are the least numbers with this ratio [7.33]. Since d:e is in lowest terms, d and e are prime to one another [7.22].

**Step 3.** Since A, C1, ..., Cn, B are n+2 numbers in continued proportion with ratio d:e, and A and B are prime to one another, by Proposition 8.1, the sequence A, C1, ..., Cn, B consists of the least numbers in continued proportion with ratio d:e (for there are no smaller n+2 numbers in continued proportion with the same ratio whose extremes would divide A and B) [8.1].

**Step 4.** By Proposition 8.2, we can construct the least n+2 numbers in continued proportion with ratio d:e. The construction of 8.2 yields the terms d^(n+1), d^n * e, d^(n-1) * e^2, ..., d * e^n, e^(n+1) as the least such sequence [8.2]. Since by Step 3 the sequence A, C1, ..., Cn, B is itself the least, we identify A = d^(n+1) and B = e^(n+1).

**Step 5.** Now consider the ratio 1:d. By Proposition 8.2, construct the least n+2 numbers in continued proportion with ratio 1:d. The construction yields the sequence 1, d, d^2, d^3, ..., d^n, d^(n+1) [8.2]. This is a sequence of n+2 terms in continued proportion, and d^(n+1) = A by Step 4. Therefore the n numbers d, d^2, ..., d^n fall between the unit 1 and A in continued proportion.

**Step 6.** Similarly, consider the ratio 1:e. By Proposition 8.2, construct the least n+2 numbers in continued proportion with ratio 1:e, obtaining the sequence 1, e, e^2, e^3, ..., e^n, e^(n+1) [8.2]. Since e^(n+1) = B by Step 4, the n numbers e, e^2, ..., e^n fall between the unit 1 and B in continued proportion.

**Step 7.** Therefore, however many numbers (n) fall between A and B in continued proportion, so many (n) also fall between A and the unit in continued proportion, and so many (n) also fall between B and the unit in continued proportion. This is what was to be proved.

**USED:** 7.22, 7.33, 8.1, 8.2
**Human refs (from References field):** 8.1, 8.2, D7.20
**Jaccard:** 0.400 — AI adds ['7.22', '7.33']; Human adds ['D7.20']

## Proposition 8.10
**Statement:** If numbers fall between each of two numbers and an unit in continued proportion, however many numbers fall between each of them and an unit in continued proportion, so many also will fall between the numbers themselves in continued proportion.

**Step 1.** Let A and B be two numbers, and let there fall k numbers between the unit and A in continued proportion, so that the sequence is 1, c, c^2, ..., c^(k+1) = A, and likewise let k numbers fall between the unit and B in continued proportion, so that the sequence is 1, d, d^2, ..., d^(k+1) = B. We must show that k numbers also fall between A and B in continued proportion.

**Step 2.** Since 1, c, c^2, ..., c^(k+1) are in continued proportion, the common ratio of consecutive terms is 1:c, and each term is obtained from the previous by multiplying by c. Thus A = c^(k+1). Similarly, since 1, d, d^2, ..., d^(k+1) are in continued proportion with common ratio 1:d, we have B = d^(k+1).

**Step 3.** Construct the following sequence of k+2 numbers: c^(k+1), c^k * d, c^(k-1) * d^2, ..., c^j * d^(k+1-j), ..., c * d^k, d^(k+1). That is, the j-th term (counting from 0) is c^(k+1-j) * d^j, for j = 0, 1, 2, ..., k+1. The first term is c^(k+1) = A and the last term is d^(k+1) = B, and there are k terms strictly between A and B. Each of these terms is a number, since by the definition of multiplication (D7.15), the product of numbers is a number.

**Step 4.** We now show that consecutive terms in this sequence have the same ratio, namely c : d. Consider the j-th and (j+1)-th terms: the j-th term is c^(k+1-j) * d^j and the (j+1)-th term is c^(k-j) * d^(j+1). We can write these as: the j-th term equals c^(k-j) * d^j * c, and the (j+1)-th term equals c^(k-j) * d^j * d, using the commutativity of multiplication (7.16).

**Step 5.** Since c^(k-j) * d^j is a number that multiplies both c and d, by Proposition 7.17, the products have to one another the ratio which c has to d. That is, c^(k-j) * d^j * c : c^(k-j) * d^j * d = c : d. Therefore the j-th term is to the (j+1)-th term as c is to d.

**Step 6.** Since this holds for every pair of consecutive terms (for j = 0, 1, ..., k), all k+2 numbers in the sequence c^(k+1), c^k * d, c^(k-1) * d^2, ..., c * d^k, d^(k+1) are in continued proportion with common ratio c : d (D7.20).

**Step 7.** The first term of this sequence is A and the last is B, and there are k numbers between them. Since k is the same number that falls between the unit and each of A and B in continued proportion, we have shown that however many numbers fall between each of A, B and the unit in continued proportion, so many also fall between A and B in continued proportion. Q.E.D.

**USED:** 7.16, 7.17, D7.15, D7.20
**Human refs (from References field):** 7.17, 7.18, D7.20
**Jaccard:** 0.400 — AI adds ['7.16', 'D7.15']; Human adds ['7.18']

## Proposition 8.11
**Statement:** Between two square numbers there is one mean proportional number, and the square has to the square the ratio duplicate of that which the side has to the side.

**Step 1.** Let A and B be two numbers, and let A multiplied by A produce C, and B multiplied by B produce D, so that C and D are square numbers with sides A and B respectively [D7.18].

**Step 2.** Let A multiplied by B produce E. Since A has multiplied A to produce C and has multiplied B to produce E, therefore C is to E as A is to B, that is, A*A is to A*B as A is to B [7.17].

**Step 3.** Again, since A has multiplied B to produce E and B has multiplied B to produce D, therefore E is to D as A is to B, that is, A*B is to B*B as A is to B [7.18].

**Step 4.** But from Step 2, C is to E as A is to B, and from Step 3, E is to D as A is to B. Therefore C is to E as E is to D [CN1]. Thus C, E, D are in continued proportion, and E is one mean proportional number between the square numbers C and D.

**Step 5.** Since C, E, D are three numbers in continued proportion, C has to D the ratio duplicate of that which C has to E [D5.9]. But C is to E as A is to B [Step 2]. Therefore C has to D the ratio duplicate of that which A has to B; that is, the square A*A has to the square B*B the ratio duplicate of that which the side A has to the side B.

Therefore, between two square numbers there is one mean proportional number, and the square has to the square the ratio duplicate of that which the side has to the side. Q.E.D.

**USED:** 7.17, 7.18, CN1, D5.9, D7.18
**Human refs (from References field):** 7.17, 7.18, D5.9
**Jaccard:** 0.600 — AI adds ['CN1', 'D7.18']

## Proposition 8.12
**Statement:** Between two cube numbers there are two mean proportional numbers, and the cube has to the cube the ratio triplicate of that which the side has to the side.

**Step 1.** Let a and b be numbers, and let a^3 and b^3 be cube numbers, where a^3 = a * a * a and b^3 = b * b * b [D7.19].

**Step 2.** Let a multiply a to produce a^2, and let b multiply b to produce b^2. Let a multiply a*b to produce a^2*b, and let b multiply a*b to produce a*b^2. These products exist by the definition of multiplication [D7.15].

**Step 3.** Since a^3 = a * a^2 and a^2*b = b * a^2 (that is, both a and b have multiplied a^2), by 7.18, a * a^2 : b * a^2 = a : b. Therefore a^3 : a^2*b = a : b.

**Step 4.** Since a^2*b = a * (a*b) and a*b^2 = b * (a*b) (that is, both a and b have multiplied a*b), by 7.18, a * (a*b) : b * (a*b) = a : b. Therefore a^2*b : a*b^2 = a : b.

**Step 5.** Since a*b^2 = a * b^2 and b^3 = b * b^2 (that is, both a and b have multiplied b^2), by 7.18, a * b^2 : b * b^2 = a : b. Therefore a*b^2 : b^3 = a : b.

**Step 6.** From Steps 3, 4, and 5, we have a^3 : a^2*b = a^2*b : a*b^2 = a*b^2 : b^3, all equal to a : b. Therefore a^3, a^2*b, a*b^2, b^3 are four numbers in continued proportion, and a^2*b and a*b^2 are two mean proportional numbers between the cubes a^3 and b^3.

**Step 7.** Since a^3, a^2*b, a*b^2, b^3 are four magnitudes in continued proportion, by definition [D5.10], the first (a^3) has to the fourth (b^3) the triplicate ratio of that which the first (a^3) has to the second (a^2*b), which is the ratio a : b. But a : b is the ratio of the side to the side.

**Step 8.** Therefore, between two cube numbers there are two mean proportional numbers, and the cube has to the cube the ratio triplicate of that which the side has to the side. Q.E.D.

**USED:** 7.18, D5.10, D7.15, D7.19
**Human refs (from References field):** 7.17, 7.18, D5.10
**Jaccard:** 0.400 — AI adds ['D7.15', 'D7.19']; Human adds ['7.17']

## Proposition 8.13
**Statement:** If there be as many numbers as we please in continued proportion, and each by multiplying itself make some number, the products will be proportional; and, if the original numbers by multiplying the products make certain numbers, the latter will also be proportional.

**Step 1.** Let A, B, C be as many numbers as we please in continued proportion, so that A : B = B : C. Let each multiply itself: let A * A = D, B * B = E, C * C = F (the squares). And let each original number multiply its square: let A * D = G, B * E = H, C * F = K (the cubes). We must show that D, E, F are in continued proportion, and that G, H, K are in continued proportion.

**Step 2.** Since A : B = B : C (given), by 7.17 (a number multiplying two numbers produces results in the same ratio as the numbers multiplied), A multiplying A and B gives: A * A : A * B = A : B, that is, D : AB = A : B.

**Step 3.** By 7.18 (two numbers multiplying the same number produce results in the same ratio as the multipliers), A and B multiplying B gives: A * B : B * B = A : B, that is, AB : E = A : B.

**Step 4.** From Steps 2 and 3, D : AB = A : B and AB : E = A : B. Therefore D : AB = AB : E, so D, AB, E are three numbers in continued proportion with common ratio A : B.

**Step 5.** Similarly, since B : C = A : B (the same ratio in the continued proportion), B multiplying B and C gives B * B : B * C = B : C by 7.17, that is, E : BC = B : C. And B and C multiplying C gives B * C : C * C = B : C by 7.18, that is, BC : F = B : C. Therefore E : BC = BC : F, so E, BC, F are three numbers in continued proportion with common ratio B : C.

**Step 6.** Since A : B = B : C, the common ratio of the sequence D, AB, E equals the common ratio of the sequence E, BC, F. Therefore the four numbers D, AB, E and E, BC, F can be combined into the sequence D, AB, E, BC, F, all in continued proportion with the same common ratio A : B.

**Step 7.** By 7.14 (ex aequali), applied to the continued proportion D, AB, E: since D : AB = AB : E, we conclude D : E is the ratio compounded from these. Likewise from E, BC, F: E : F is the ratio compounded from E : BC and BC : F. Since D : AB = AB : E = E : BC = BC : F (all equal to A : B), the ex aequali ratios are equal: D : E = E : F. Therefore D, E, F are in continued proportion, which is to say A^2, B^2, C^2 are proportional. This establishes the first part.

**Step 8.** For the second part, we must show G, H, K (i.e., A^3, B^3, C^3) are in continued proportion. Since D : E = A^2 : B^2 and A : B are established ratios, consider A multiplying D and E. By 7.17, A * D : A * E = D : E, that is, G : AE = D : E.

**Step 9.** By 7.18, A and B multiplying E gives A * E : B * E = A : B, that is, AE : H = A : B.

**Step 10.** From Step 7, D : E = E : F, and from Step 4, D : E is compounded from two copies of the ratio A : B. Now from Steps 8 and 9, G : AE = D : E and AE : H = A : B. By 7.14 (ex aequali) applied to G, AE, H: G : H is the ratio compounded from G : AE and AE : H, that is, from D : E and A : B. Since D : E is itself compounded from A : B and A : B (Step 7), G : H is compounded from three copies of A : B.

**Step 11.** Similarly, B multiplying E and F gives B * E : B * F = E : F by 7.17, that is, H : BF = E : F. And B and C multiplying F gives B * F : C * F = B : C by 7.18, that is, BF : K = B : C. By 7.14 (ex aequali) applied to H, BF, K: H : K is the ratio compounded from E : F and B : C. Since E : F is compounded from two copies of B : C (by the same argument as D : E from A : B), and B : C = A : B, H : K is compounded from three copies of A : B.

**Step 12.** From Steps 10 and 11, G : H and H : K are each the ratio compounded from three copies of A : B. Therefore G : H = H : K, so G, H, K are in continued proportion, which is to say A^3, B^3, C^3 are proportional.

**Step 13.** The argument extends to any number of terms in the original continued proportion by the same method: each successive application of 7.17 and 7.18 establishes the proportionality among the squares and cubes of consecutive terms, and 7.14 combines the intermediate ratios.

**Step 14.** Therefore, if there be as many numbers as we please in continued proportion, and each by multiplying itself make some number, the products (squares) are proportional; and if the original numbers by multiplying the products make certain numbers, the latter (cubes) are also proportional. Q.E.D.

**USED:** 7.14, 7.17, 7.18, D7.15, D7.18, D7.20
**Human refs (from References field):** 7.14
**Jaccard:** 0.167 — AI adds ['7.17', '7.18', 'D7.15', 'D7.18', 'D7.20']

## Proposition 8.14
**Statement:** If a square measure a square, the side will also measure the side; and, if the side measure the side, the square will also measure the square.

**Step 1.** Let A and B be numbers, and let A*A and B*B be their squares. We must prove two things: (i) if A*A measures B*B, then A measures B; and (ii) if A measures B, then A*A measures B*B.

**Step 2.** By 8.11, between two square numbers A*A and B*B there is one mean proportional number, namely A*B, so that A*A, A*B, B*B are in continued proportion.

**Step 3.** Furthermore, by 7.17, since A multiplied by A produces A*A and A multiplied by B produces A*B, we have A*A : A*B = A : B. Similarly, by 7.18, since A multiplied by B produces A*B and B multiplied by B produces B*B, we have A*B : B*B = A : B.

**Step 4.** (Proof of Part i) Suppose A*A measures B*B. Since A*A, A*B, B*B are in continued proportion (Step 2) and the first term A*A measures the last term B*B, by 8.7, A*A also measures the second term A*B.

**Step 5.** Since A*A measures A*B, and A*A : A*B = A : B (Step 3), A is the same part of B (or equal to B) that A*A is of A*B, by D7.20. Therefore A measures B.

**Step 6.** (Proof of Part ii) Conversely, suppose A measures B. Since A*A : A*B = A : B (Step 3) and A measures B, then A*A measures A*B, by D7.20 (A being a part or equal measure of B means A*A is the same part or equal measure of A*B).

**Step 7.** Since A*B : B*B = A : B (Step 3) and A measures B, then similarly A*B measures B*B, by D7.20.

**Step 8.** Since A*A measures A*B (Step 6), there is a number k such that A*B equals A*A taken k times. Since A*B measures B*B (Step 7), there is a number m such that B*B equals A*B taken m times. Then B*B equals A*A taken k times m, that is, A*A multiplied by the product of k and m, by 7.16. Therefore A*A measures B*B.

**Step 9.** Thus, if a square measures a square, the side also measures the side; and if the side measures the side, the square also measures the square. Q.E.D.

**USED:** 7.16, 7.17, 7.18, 8.11, 8.7, D7.20, D7.3
**Human refs (from References field):** 8.11, 8.7, D7.20
**Jaccard:** 0.429 — AI adds ['7.16', '7.17', '7.18', 'D7.3']

## Proposition 8.15
**Statement:** If a cube number measure a cube number, the side will also measure the side; and, if the side measure the side, the cube will also measure the cube.

**Step 1.** Let A and B be cube numbers with sides a and b respectively, so that A = a * a * a and B = b * b * b (D7.19).

**Part I: If the cube A measures the cube B, then the side a measures the side b.**

**Step 2.** By 8.12, between the two cube numbers A and B there are two mean proportional numbers. Let C and D be these mean proportionals, so that A, C, D, B are four numbers in continued proportion, and A has to B the ratio triplicate of that which a has to b.

**Step 3.** Since A, C, D, B are in continued proportion, the ratio A:C equals a:b. This follows from 8.12, which establishes that the continued proportion between two cubes a^3 and b^3 has common ratio a:b, so that C = a * a * b and D = a * b * b.

**Step 4.** Since A measures B, and A, C, D, B are in continued proportion (with A first and B last), by 8.7 the first term A also measures the second term C.

**Step 5.** Since A:C = a:b (Step 3), and A measures C (Step 4), it follows that a measures b. For if A measures C, then C is a multiple of A, say C = k * A. Since A:C = a:b, we have a * C = b * A (D7.20). Substituting C = k * A gives a * k * A = b * A, hence a * k = b, so a measures b (D7.3, D7.15).

**Part II: If the side a measures the side b, then the cube A measures the cube B.**

**Step 6.** Suppose a measures b. By 8.12, between A and B there are two mean proportional numbers C and D, with A, C, D, B in continued proportion, where C = a * a * b and D = a * b * b.

**Step 7.** Since A, C, D, B are in continued proportion, the common ratio is a:b (from 8.12). In particular, A:C = a:b, C:D = a:b, and D:B = a:b.

**Step 8.** Since a measures b (hypothesis), there exists a number k such that b = k * a (D7.3, D7.15). Then C = a * a * b = a * a * (k * a) = k * (a * a * a) = k * A. Therefore A measures C.

**Step 9.** Similarly, D = a * b * b = a * (k * a) * (k * a). And C = a * a * b = a * a * (k * a). So D = k * C, which means C measures D. Since A measures C (Step 8), A also measures D. This follows because if A measures C and C measures D, then D is a multiple of C which is a multiple of A, so D is a multiple of A (by 7.17 applied to the multiplication relationships, together with D7.3).

**Step 10.** By the same reasoning, B = b * b * b = (k * a) * (k * a) * (k * a) = k * (a * b * b) = k * D. So D measures B. Since A measures D (Step 9), A also measures B. Again, B being a multiple of D which is a multiple of A makes B a multiple of A (D7.3, 7.17).

**Step 11.** Therefore, if the side a measures the side b, the cube A measures the cube B.

**Step 12.** Combining Parts I and II: if a cube number measure a cube number, the side will also measure the side; and if the side measure the side, the cube will also measure the cube. Q.E.D.

**USED:** 7.17, 8.12, 8.7, D7.15, D7.19, D7.20, D7.3
**Human refs (from References field):** 8.11, 8.12, 8.7, D7.20
**Jaccard:** 0.375 — AI adds ['7.17', 'D7.15', 'D7.19', 'D7.3']; Human adds ['8.11']

## Proposition 8.16
**Statement:** If a square number do not measure a square number, neither will the side measure the side; and, if the side do not measure the side, neither will the square measure the square.

**Step 1.** Let A and B be square numbers with sides C and D respectively, so that A = C * C and B = D * D.

**Step 2.** (Part 1) Suppose the square A does not measure the square B. We claim that the side C does not measure the side D. For assume, for the sake of contradiction, that C does measure D. Then by Proposition 8.14 (if the side measure the side, the square will also measure the square), A would measure B. But this contradicts the hypothesis that A does not measure B. Therefore C does not measure D.

**Step 3.** (Part 2) Now suppose the side C does not measure the side D. We claim that the square A does not measure the square B. For assume, for the sake of contradiction, that A does measure B. Then by Proposition 8.14 (if a square measure a square, the side will also measure the side), C would measure D. But this contradicts the hypothesis that C does not measure D. Therefore A does not measure B.

**Step 4.** Thus both directions are established: if a square number does not measure a square number, neither does the side measure the side; and if the side does not measure the side, neither does the square measure the square. Q.E.D.

**USED:** 8.14
**Human refs (from References field):** 8.14
**Jaccard:** 1.000 — Perfect match.

## Proposition 8.17
**Statement:** If a cube number do not measure a cube number, neither will the side measure the side; and, if the side do not measure the side, neither will the cube measure the cube.

**Step 1.** Let A and B be numbers, and let A^3 and B^3 be their cubes. We must prove two things: (i) if A^3 does not measure B^3, then A does not measure B; and (ii) if A does not measure B, then A^3 does not measure B^3.

**Step 2.** Proof of (i): Suppose, for the sake of contradiction, that A^3 does not measure B^3, yet A does measure B. Since A measures B, by Proposition 8.15 (if the side measure the side, the cube will also measure the cube), A^3 measures B^3. But this contradicts the hypothesis that A^3 does not measure B^3. Therefore A does not measure B.

**Step 3.** Proof of (ii): Suppose, for the sake of contradiction, that A does not measure B, yet A^3 does measure B^3. Since A^3 measures B^3, by Proposition 8.15 (if a cube number measure a cube number, the side will also measure the side), A measures B. But this contradicts the hypothesis that A does not measure B. Therefore A^3 does not measure B^3.

**Step 4.** Therefore, if a cube number does not measure a cube number, neither does the side measure the side; and if the side does not measure the side, neither does the cube measure the cube. Q.E.D.

**USED:** 8.15
**Human refs (from References field):** 8.15
**Jaccard:** 1.000 — Perfect match.

## Proposition 8.18
**Statement:** Between two similar plane numbers there is one mean proportional number; and the plane number has to the plane number the ratio duplicate of that which the corresponding side has to the corresponding side.

**Step 1.** Let A and B be two similar plane numbers. Since A is a plane number, by D7.16, let A = c * d where c and d are its sides. Similarly, let B = e * f where e and f are the sides of B.

**Step 2.** Since A and B are similar plane numbers, by D7.21 their sides are proportional. Arranging corresponding sides, we have c : e = d : f.

**Step 3.** Since c : e = d : f, by 7.19 (if four numbers are proportional then the product of the extremes equals the product of the means), we obtain c * f = e * d. Let G denote this common product, so G = c * f = e * d.

**Step 4.** Consider the ratio A : G. We have A = c * d and G = c * f, so c multiplies both d and f to produce A and G respectively. By 7.17, since one number c multiplies two numbers d and f, the products are in the same ratio as the numbers multiplied. Therefore A : G = d : f.

**Step 5.** Consider the ratio G : B. We have G = e * d and B = e * f, so e multiplies both d and f to produce G and B respectively. By 7.17 again, G : B = d : f.

**Step 6.** Since A : G = d : f and G : B = d : f, by CN1 we conclude A : G = G : B. Therefore the three numbers A, G, B are in continued proportion, and G is one mean proportional number between A and B.

**Step 7.** Since A, G, B are three numbers in continued proportion, by D5.9 the first A has to the third B the duplicate ratio of that which A has to the second G. But A : G = d : f, where d and f are corresponding sides of the two plane numbers. Therefore A has to B the ratio duplicate of that which the corresponding side d has to the corresponding side f.

**Step 8.** Since c : e = d : f (from Step 2), the same duplicate ratio relationship holds for either pair of corresponding sides. Therefore the plane number A has to the plane number B the ratio duplicate of that which the corresponding side has to the corresponding side. Q.E.D.

**USED:** 7.17, 7.19, CN1, D5.9, D7.16, D7.21
**Human refs (from References field):** 7.13, 7.17, D5.9, D7.21
**Jaccard:** 0.429 — AI adds ['7.19', 'CN1', 'D7.16']; Human adds ['7.13']

## Proposition 8.19
**Statement:** Between two similar solid numbers there fall two mean proportional numbers; and the solid number has to the similar solid number the ratio triplicate of that which the corresponding side has to the corresponding side.

**Step 1.** Let A and B be similar solid numbers. Then by D7.17, A = d * e * f and B = g * h * k for some numbers d, e, f and g, h, k respectively, which are the sides of these solid numbers.

**Step 2.** Since A and B are similar solid numbers, by D7.21 their sides are proportional: d:g = e:h = f:k.

**Step 3.** Since d:g = e:h = f:k, consider the numbers A = d*e*f, the number d*e*k, the number d*h*k, and B = g*h*k. We shall show these four numbers are in continued proportion with common ratio f:k.

**Step 4.** First, A : d*e*k = d*e*f : d*e*k. Since d*e multiplies both f and k, by 7.17, (d*e)*f : (d*e)*k = f : k.

**Step 5.** Next, d*e*k : d*h*k. Since k multiplies both e and h, by 7.17 we have e*k : h*k = e : h. Then since d multiplies both e*k and h*k, by 7.17 we have d*(e*k) : d*(h*k) = e*k : h*k. Therefore d*e*k : d*h*k = e*k : h*k = e : h. But e:h = f:k by Step 2, so d*e*k : d*h*k = f : k.

**Step 6.** Next, d*h*k : g*h*k. Since d and g each multiply h*k, by 7.18, d*(h*k) : g*(h*k) = d : g. But d:g = f:k by Step 2, so d*h*k : g*h*k = f : k. That is, d*h*k : B = f : k.

**Step 7.** From Steps 4, 5, and 6, we have A : d*e*k = d*e*k : d*h*k = d*h*k : B = f : k. Therefore A, d*e*k, d*h*k, B are four numbers in continued proportion, so d*e*k and d*h*k are two mean proportional numbers falling between A and B.

**Step 8.** Since A, d*e*k, d*h*k, B are four magnitudes in continued proportion, by D5.10 A has to B the triplicate ratio of that which A has to d*e*k.

**Step 9.** But A : d*e*k = f : k (from Step 4), and f:k = d:g = e:h (from Step 2). Therefore A has to B the triplicate ratio of that which the corresponding side has to the corresponding side.

**Step 10.** Therefore, between two similar solid numbers there fall two mean proportional numbers, and the solid number has to the similar solid number the ratio triplicate of that which the corresponding side has to the corresponding side. Q.E.D.

**USED:** 7.17, 7.18, D5.10, D7.17, D7.21
**Human refs (from References field):** 7.13, 7.17, 7.18, 8.18, D5.10, D7.21
**Jaccard:** 0.571 — AI adds ['D7.17']; Human adds ['7.13', '8.18']

## Proposition 8.20
**Statement:** If one mean proportional number fall between two numbers, the numbers will be similar plane numbers.

**Step 1.** Let C be one mean proportional number between A and B, so that A:C = C:B. We are to show that A and B are similar plane numbers.

**Step 2.** Take D and E to be the least numbers in the ratio A:C [7.33]. Then A:C = D:E and also C:B = D:E.

**Step 3.** Since D:E is in least terms and A:C = D:E, by 7.20, D measures A and E measures C. Let A = D*F for some number F, and let C = E*F.

**Step 4.** Since C:B = D:E and D:E is in least terms, by 7.20, D measures C and E measures B. Let C = D*G for some number G, and let B = E*G.

**Step 5.** From Steps 3 and 4 we have C = E*F and C = D*G, so E*F = D*G.

**Step 6.** Since D and E are the least numbers in their ratio, by 7.22 they are prime to one another.

**Step 7.** Since E*F = D*G, by 7.19 we have D:E = F:G.

**Step 8.** Now A = D*F, so A is a plane number with sides D and F [D7.16]. Likewise B = E*G, so B is a plane number with sides E and G [D7.16].

**Step 9.** Since D:E = F:G (Step 7), the sides of A are proportional to the corresponding sides of B. Therefore A and B are similar plane numbers [D7.21].

**Step 10.** Therefore, if one mean proportional number falls between two numbers, the numbers are similar plane numbers. Q.E.D.

**USED:** 7.19, 7.20, 7.22, 7.33, D7.16, D7.21
**Human refs (from References field):** 7.13, 7.17, 7.20, 7.33
**Jaccard:** 0.250 — AI adds ['7.19', '7.22', 'D7.16', 'D7.21']; Human adds ['7.13', '7.17']

## Proposition 8.21
**Statement:** If two mean proportional numbers fall between two numbers, the numbers are similar solid numbers.

**Step 1.** Let A and D be two numbers, and let B and C fall between them as two mean proportional numbers, so that A, B, C, D are in continued proportion: A:B = B:C = C:D.

**Step 2.** By 8.2, find the least numbers in continued proportion having the same ratios as A:B:C:D. Let these be E, F, G, H, so that E:F = A:B, F:G = B:C, and G:H = C:D, and E, F, G, H are in continued proportion and are the least such numbers.

**Step 3.** Since E, F, G, H are the least numbers in continued proportion with these ratios, by 8.3, the extremes E and H are prime to one another.

**Step 4.** Since E and H are prime to one another and two mean proportional numbers F and G fall between them in continued proportion, by 8.9, two numbers also fall between E and the unit in continued proportion, and two numbers also fall between H and the unit in continued proportion.

**Step 5.** Let the two mean proportionals between the unit and E be p and q, so that 1, p, q, E are in continued proportion: 1:p = p:q = q:E. From 1:p = p:q, by 7.19, the product of the extremes equals the product of the means, so q = p times p. From p:q = q:E, by 7.19 again, p times E = q times q = (p times p) times (p times p). Therefore E = p times p times p, so E is a solid number which is a cube with all three sides equal to p, by D7.17.

**Step 6.** Similarly, let the two mean proportionals between the unit and H be r and s, so that 1, r, s, H are in continued proportion. By the same reasoning using 7.19, s = r times r, and H = r times r times r. So H is a cube with all three sides equal to r, by D7.17.

**Step 7.** Since E, F, G, H are the least numbers in continued proportion with the same ratio as A, B, C, D, and E:F = A:B, by 7.20, E measures A. Let A = m times E for some number m.

**Step 8.** Now A:D is the ratio compounded of A:B, B:C, and C:D, which is the triplicate ratio of A:B by D5.10. Likewise E:H is the triplicate ratio of E:F. Since A:B = E:F, we have A:D = E:H. Since A = m times E and A:D = E:H, by 7.17 and 7.18, D = m times H.

**Step 9.** Since E = p times p times p, we have A = m times (p times p times p). Therefore A = (m times p) times p times p, so A is a solid number with sides m times p, p, and p, by D7.17.

**Step 10.** Since H = r times r times r, we have D = m times (r times r times r). Therefore D = (m times r) times r times r, so D is a solid number with sides m times r, r, and r, by D7.17.

**Step 11.** We must now show that the sides of A and D are proportional. The sides of A are (m times p), p, p and the sides of D are (m times r), r, r. By 7.17, since m is common, (m times p):(m times r) = p:r. Trivially p:r = p:r. Therefore the three pairs of corresponding sides are in the same ratio p:r.

**Step 12.** Since A and D are each solid numbers, and their corresponding sides are proportional, A and D are similar solid numbers by D7.21.

**Step 13.** Therefore, if two mean proportional numbers fall between two numbers, the numbers are similar solid numbers. Q.E.F.

**USED:** 7.17, 7.18, 7.19, 7.20, 8.2, 8.3, 8.9, D5.10, D7.17, D7.21
**Human refs (from References field):** 7.14, 7.18, 7.20, 7.21, 7.33, 8.2, 8.20, 8.3
**Jaccard:** 0.286 — AI adds ['7.17', '7.19', '8.9', 'D5.10', 'D7.17', 'D7.21']; Human adds ['7.14', '7.21', '7.33', '8.20']

## Proposition 8.22
**Statement:** If three numbers be in continued proportion, and the first be square, the third will also be square.

**Step 1.** Let A, B, C be three numbers in continued proportion, so that A : B = B : C, and let A be a square number. We are to prove that C is also square.

**Step 2.** Since A is a square number, A is equal multiplied by equal, that is, A = s * s for some number s [D7.18].

**Step 3.** Since A, B, C are in continued proportion, B is one mean proportional number falling between A and C.

**Step 4.** Since one mean proportional number B falls between A and C, by Proposition 8.20, A and C are similar plane numbers.

**Step 5.** Since A and C are similar plane numbers, their sides are proportional [D7.21]. Now A = s * s has both sides equal to s. Let C = p * q where p, q are its sides. Then since A and C are similar plane numbers, we have s : p = s : q.

**Step 6.** Since s : p = s : q, by Proposition 7.19 (if four numbers be proportional, the product of the first and fourth equals the product of the second and third), we have s * q = p * s, that is, s * q = s * p.

**Step 7.** By Proposition 7.17 (if a number by multiplying two numbers make certain numbers, the products have the same ratio as the numbers multiplied), s * p : s * q = p : q. But s * p = s * q from Step 6, so p : q is a ratio of equals, and therefore p = q.

**Step 8.** Since C = p * q and p = q, we have C = p * p, that is, C is equal multiplied by equal. Therefore C is a square number [D7.18]. Q.E.D.

**USED:** 7.17, 7.19, 8.20, D7.18, D7.21
**Human refs (from References field):** 8.20
**Jaccard:** 0.200 — AI adds ['7.17', '7.19', 'D7.18', 'D7.21']

## Proposition 8.23
**Statement:** If four numbers be in continued proportion, and the first be cube, the fourth will also be cube.

**Step 1.** Let A, B, C, D be four numbers in continued proportion, so that A : B = B : C = C : D, and let A be a cube number.

**Step 2.** Since A is a cube, there exists a number a such that A = a * a * a [D7.19].

**Step 3.** By 7.33, reduce the ratio A : B to least terms, and let the ratio in least terms be e : f. Then A : B = e : f, where e and f are prime to one another [7.22].

**Step 4.** By 8.2, we can find the least four numbers in continued proportion having the ratio e : f. These least four numbers are e^3, e^2 * f, e * f^2, f^3 [8.2]. Call them E, F, G, H respectively.

**Step 5.** Since A, B, C, D are four numbers in continued proportion with the same ratio as E, F, G, H (which are the least such), and E, F, G, H are the least of those having the same ratio with them, E measures A, that is, e^3 measures A [7.20]. Let A = k * e^3 for some number k. Likewise D = k * f^3.

**Step 6.** Now A = a^3 and A = k * e^3, so a^3 = k * e^3. Therefore e^3 measures a^3 [from the equality].

**Step 7.** Since e^3 is a cube and a^3 is a cube, and e^3 measures a^3, by 8.15 the side e measures the side a. Let a = e * m for some number m.

**Step 8.** Then A = a^3 = (e * m)^3 = e^3 * m^3 [by 7.17, 7.18 applied repeatedly]. Since A = k * e^3, we have k * e^3 = m^3 * e^3, whence k = m^3 [CN3, dividing both sides by e^3, equivalently by 7.17 and the uniqueness of the product].

**Step 9.** Therefore D = k * f^3 = m^3 * f^3. Now m * f is a number; and m^3 * f^3 = (m * f) * (m * f) * (m * f) [by 7.17, 7.18 applied repeatedly]. Thus D is equal multiplied by equal and again by equal, so D is a cube [D7.19].

**Step 10.** Therefore, if four numbers be in continued proportion and the first be cube, the fourth will also be cube. Q.E.D.

**USED:** 7.17, 7.18, 7.20, 7.22, 7.33, 8.15, 8.2, CN3, D7.19
**Human refs (from References field):** 8.21
**Jaccard:** 0.000 — AI adds ['7.17', '7.18', '7.20', '7.22', '7.33', '8.15', '8.2', 'CN3', 'D7.19']; Human adds ['8.21']

## Proposition 8.24
**Statement:** If two numbers have to one another the ratio which a square number has to a square number, and the first be square, the second will also be square.

**Step 1.** Let A and B be two numbers such that A : B = C^2 : D^2, where C^2 and D^2 are square numbers (i.e., C^2 = C * C and D^2 = D * D), and let A itself be a square number. We must show that B is also a square number.

**Step 2.** Since C^2 and D^2 are both square numbers, by Proposition 8.11 there is one mean proportional number between them. That is, there exists a number E such that C^2, E, D^2 are in continued proportion.

**Step 3.** Now A : B = C^2 : D^2 (given), and there is one mean proportional between C^2 and D^2 (Step 2). Therefore, by Proposition 8.8, there is also one mean proportional number between A and B. That is, there exists a number F such that A, F, B are three numbers in continued proportion.

**Step 4.** Since A, F, B are three numbers in continued proportion and A is a square number (given), by Proposition 8.22 the third number B is also a square number.

**Step 5.** Therefore, if two numbers have to one another the ratio which a square number has to a square number, and the first is square, the second will also be square. Q.E.D.

**USED:** 8.11, 8.22, 8.8
**Human refs (from References field):** 8.18, 8.22, 8.8
**Jaccard:** 0.500 — AI adds ['8.11']; Human adds ['8.18']

## Proposition 8.25
**Statement:** If two numbers have to one another the ratio which a cube number has to a cube number, and the first be cube, the second will also be cube.

**Step 1.** Let A and B be two numbers such that A:B = C³:D³, where C³ and D³ are cube numbers, and let A be cube. We must show that B is also cube.

**Step 2.** Since C³ and D³ are cube numbers, by Proposition 8.12, between two cube numbers there fall two mean proportional numbers. Therefore there exist numbers E and F such that C³, E, F, D³ are in continued proportion.

**Step 3.** Thus there are four numbers in continued proportion from C³ to D³, meaning there are two mean proportionals between C³ and D³.

**Step 4.** Now A:B = C³:D³, and between C³ and D³ there fall two numbers in continued proportion (namely E and F). Therefore, by Proposition 8.8, however many numbers fall between C³ and D³ in continued proportion, so many will also fall between A and B in continued proportion. Hence there exist numbers G and H such that A, G, H, B are in continued proportion.

**Step 5.** Therefore A, G, H, B are four numbers in continued proportion. Since A is cube and A is the first of four numbers in continued proportion, by Proposition 8.23, the fourth number B is also cube.

**Step 6.** Therefore, if two numbers have to one another the ratio which a cube number has to a cube number, and the first be cube, the second will also be cube. Q.E.D.

**USED:** 8.12, 8.23, 8.8
**Human refs (from References field):** 8.19, 8.23, 8.8
**Jaccard:** 0.500 — AI adds ['8.12']; Human adds ['8.19']

## Proposition 8.26
**Statement:** Similar plane numbers have to one another the ratio which a square number has to a square number.

**Step 1.** Let A and B be similar plane numbers. By D7.16, A = a * b and B = c * d for some numbers a, b, c, d (the sides of A and B respectively). By D7.21, since A and B are similar plane numbers, their sides are proportional, so a : c :: b : d (where a corresponds to c and b corresponds to d).

**Step 2.** By 7.33, let e and f be the least numbers in the ratio a : c. Then a : c :: e : f.

**Step 3.** By 8.18, between two similar plane numbers A and B there is one mean proportional number, and A has to B the ratio duplicate of that which the corresponding side a has to the corresponding side c. That is, A : B is the duplicate ratio of a : c.

**Step 4.** Since a : c :: e : f (Step 2), the duplicate ratio of a : c is the same as the duplicate ratio of e : f.

**Step 5.** By 8.11, between two square numbers e^2 and f^2 there is one mean proportional number e * f, and e^2 has to f^2 the ratio duplicate of that which e has to f. That is, e^2 : f^2 is the duplicate ratio of e : f.

**Step 6.** From Steps 3, 4, and 5, A : B is the duplicate ratio of a : c, which equals the duplicate ratio of e : f, which is e^2 : f^2. Therefore A : B :: e^2 : f^2.

**Step 7.** By D7.18, e^2 = e * e is a square number, and f^2 = f * f is a square number. Therefore A and B have to one another the ratio which a square number (e^2) has to a square number (f^2).

Therefore, similar plane numbers have to one another the ratio which a square number has to a square number. Q.E.D.

**USED:** 7.33, 8.11, 8.18, D5.9, D7.16, D7.18, D7.21
**Human refs (from References field):** 7.33, 8.18, 8.2
**Jaccard:** 0.250 — AI adds ['8.11', 'D5.9', 'D7.16', 'D7.18', 'D7.21']; Human adds ['8.2']

## Proposition 8.27
**Statement:** Similar solid numbers have to one another the ratio which a cube number has to a cube number.

**Step 1.** Let A and B be similar solid numbers. By the definition of similar solid numbers (D7.21), their sides are proportional. Let the sides of A be a, b, c and the sides of B be d, e, f, so that a:d = b:e = c:f.

**Step 2.** By 8.19, between two similar solid numbers there fall two mean proportional numbers, and the solid number has to the similar solid number the ratio triplicate of that which the corresponding side has to the corresponding side. Therefore A:B is the triplicate ratio of a:d.

**Step 3.** Now consider the cube numbers a*a*a and d*d*d. Since a and d are numbers, a*a*a is a cube number and d*d*d is a cube number (D7.19).

**Step 4.** By 8.12, between two cube numbers there are two mean proportional numbers, and the cube has to the cube the ratio triplicate of that which the side has to the side. Therefore the cube a*a*a has to the cube d*d*d the ratio triplicate of that which a has to d.

**Step 5.** From Step 2, A:B is the triplicate ratio of a:d. From Step 4, (a*a*a):(d*d*d) is also the triplicate ratio of a:d. Since A:B and (a*a*a):(d*d*d) are each the triplicate of the same ratio a:d, by 5.11 (ratios which are the same with the same ratio are also the same with one another), A:B = (a*a*a):(d*d*d).

**Step 6.** Since a*a*a and d*d*d are cube numbers (D7.19), A and B have to one another the ratio which a cube number has to a cube number. Therefore similar solid numbers have to one another the ratio which a cube number has to a cube number. Q.E.F.

**USED:** 5.11, 8.12, 8.19, D7.19, D7.21
**Human refs (from References field):** 7.33, 8.19, 8.2
**Jaccard:** 0.143 — AI adds ['5.11', '8.12', 'D7.19', 'D7.21']; Human adds ['7.33', '8.2']
