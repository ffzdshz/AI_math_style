# Book 9 of Euclid's Elements — Step-by-Step AI Proofs (Run C)

## Proposition 9.1
**Statement:** If two similar plane numbers by multiplying one another make some number, the product will be square.

**Step 1.** Let A and B be similar plane numbers, and let A multiplied by B produce C. We aim to show that C is a square number.

**Step 2.** Since A and B are similar plane numbers, by Proposition 8.18, there falls one mean proportional number between them. Let this mean proportional be D, so that A, D, B are in continued proportion, that is, A : D = D : B.

**Step 3.** Since A, D, D, B are four numbers in proportion (A : D = D : B), by Proposition 7.19, the product of the first and fourth equals the product of the second and third. That is, A multiplied by B equals D multiplied by D.

**Step 4.** But A multiplied by B produces C (given). Therefore C equals D multiplied by D.

**Step 5.** A number that is equal multiplied by equal is a square number, by Definition 7.18. Since C = D multiplied by D, C is a square number.

**Step 6.** Therefore, if two similar plane numbers by multiplying one another make some number, the product is square. Q.E.D.

**USED:** 7.19, 8.18, D7.18, D7.21
**Human refs (from References field):** 7.17, 8.18, 8.22, 8.8
**Jaccard:** 0.143 — AI adds ['7.19', 'D7.18', 'D7.21']; Human adds ['7.17', '8.22', '8.8']

## Proposition 9.2
**Statement:** If two numbers by multiplying one another make a square number, they are similar plane numbers.

**Step 1.** Let A and B be two numbers such that A multiplied by B produces a square number. Call this product S, so that A * B = S, and S is a square number.

**Step 2.** Since S is a square number, by Definition D7.18, there exists a number C such that S = C * C, that is, A * B = C * C.

**Step 3.** Since A * B = C * C, the number produced from A and B equals the number produced from C and C. By the converse part of Proposition 7.19, the four numbers A, C, C, B are proportional, that is, A : C = C : B.

**Step 4.** Therefore C is one mean proportional number falling between A and B.

**Step 5.** Since between A and B there falls one mean proportional number, by Proposition 8.20, A and B are similar plane numbers.

Therefore, if two numbers by multiplying one another make a square number, they are similar plane numbers. Q.E.D.

**USED:** 7.19, 8.20, D7.18
**Human refs (from References field):** 7.17, 8.18, 8.20, 8.8
**Jaccard:** 0.167 — AI adds ['7.19', 'D7.18']; Human adds ['7.17', '8.18', '8.8']

## Proposition 9.3
**Statement:** If a cube number by multiplying itself make some number, the product will be cube.

**Step 1.** Let A be a cube number. By D7.19, there exists a number a such that A = a * a * a, where a is the side of the cube.

**Step 2.** Let B = A * A. We wish to show that B is a cube number.

**Step 3.** Let c = a * a. Let D = a * A (that is, a multiplying A), let E = a * D (that is, a multiplying D), and let F = a * E (that is, a multiplying E). [D7.15]

**Step 4.** Since a multiplying a produces c, and a multiplying c produces A (for A = a * a * a = a * c by D7.19), by 7.17 (if a number multiplying two numbers make certain numbers, the products have the same ratio as the numbers multiplied), we have a : c = c : A. Thus a, c, A are three numbers in continued proportion. [7.17]

**Step 5.** Since a multiplying c produces A, and a multiplying A produces D, by 7.17 we have c : A = A : D. [7.17]

**Step 6.** Since a multiplying A produces D, and a multiplying D produces E, by 7.17 we have A : D = D : E. [7.17]

**Step 7.** Since a multiplying D produces E, and a multiplying E produces F, by 7.17 we have D : E = E : F. [7.17]

**Step 8.** From Steps 4 through 7, we have a : c = c : A = A : D = D : E = E : F, so the six numbers a, c, A, D, E, F are in continued proportion.

**Step 9.** In particular, from Steps 5 and 8, we have c : A = A : D. By 7.19 (if four numbers be proportional, the number produced from the first and fourth equals the number produced from the second and third), c * D = A * A = B. [7.19]

**Step 10.** From Step 8, since all consecutive ratios are equal, in particular a : c = D : E (the ratio between the first and second terms equals the ratio between the fourth and fifth terms). By 7.19, a * E = c * D. [7.19]

**Step 11.** From Step 9, c * D = B. From Step 10, a * E = c * D. Therefore a * E = B. But by construction (Step 3), a * E = F. Hence F = B.

**Step 12.** From Steps 6 and 7, A : D = D : E = E : F, so A, D, E, F are four numbers in continued proportion. The first of these, A, is a cube number (given). Therefore by 8.23 (if four numbers be in continued proportion and the first be cube, the fourth will also be cube), F is a cube number. [8.23]

**Step 13.** Since F = B (Step 11), B = A * A is a cube number. Therefore, if a cube number by multiplying itself make some number, the product is cube. Q.E.D.

**USED:** 7.17, 7.19, 8.23, D7.15, D7.19
**Human refs (from References field):** 8.23, 8.8, D7.20
**Jaccard:** 0.143 — AI adds ['7.17', '7.19', 'D7.15', 'D7.19']; Human adds ['8.8', 'D7.20']

## Proposition 9.4
**Statement:** If a cube number by multiplying a cube number make some number, the product will be cube.

**Step 1.** Let A be a cube number with side a, so that a multiplied by a and again by a gives A, that is, a*a*a = A [D7.19]. Let B be a cube number with side b, so that b*b*b = B [D7.19]. Let C be the product A multiplied by B [D7.15]. We must show that C is cube.

**Step 2.** Let G = b*b [D7.15]. Then G*b = b*b*b = B [D7.19]. Define D = A*b [D7.15], E = D*b [D7.15], and F = E*b [D7.15].

**Step 3.** Since b multiplies A and D, by 7.17 the products b*A and b*D have the same ratio as A and D. Now b*A = D and b*D = E, so D : E = A : D, that is, A : D = D : E.

**Step 4.** Since b multiplies D and E, by 7.17 the products b*D and b*E have the same ratio as D and E. Now b*D = E and b*E = F, so E : F = D : E, that is, D : E = E : F.

**Step 5.** From Steps 3 and 4, A : D = D : E = E : F, so A, D, E, F are four numbers in continued proportion.

**Step 6.** We now show that F equals A*B. Since b and A each multiply the number b, by 7.18 the products b*b and A*b are in the same ratio as the multipliers: b*b : A*b = b : A, that is, G : D = b : A. By 7.19 applied to the proportion G : D = b : A, the product of the extremes equals the product of the means: G*A = D*b. By 7.16, A*G = G*A. Therefore A*G = D*b = E.

**Step 7.** Since b and A each multiply G, by 7.18 the products b*G and A*G are in the same ratio as the multipliers: b*G : A*G = b : A. Now b*G = b*(b*b) = b*b*b = B [D7.19], and A*G = E [Step 6]. So B : E = b : A. By 7.19 applied to B : E = b : A, we get B*A = E*b. By 7.16, A*B = B*A. Therefore A*B = E*b = F. Since C = A*B by definition, F = C.

**Step 8.** Since A, D, E, F are four numbers in continued proportion [Step 5] and A is cube [given], by 8.23 the fourth number F is also cube. Since F = C = A*B [Step 7], the product C is cube. Q.E.D.

**USED:** 7.16, 7.17, 7.18, 7.19, 8.23, D7.15, D7.19
**Human refs (from References field):** 7.17, 8.19, 8.23, 8.8, 9.3
**Jaccard:** 0.200 — AI adds ['7.16', '7.18', '7.19', 'D7.15', 'D7.19']; Human adds ['8.19', '8.8', '9.3']

## Proposition 9.5
**Statement:** If a cube number by multiplying any number make a cube number, the multiplied number will also be cube.

**Step 1.** Let A be a cube number, and let A by multiplying some number B make the cube number C. We are to prove that B is also cube. Since A is cube, let A = D*D*D for some number D [D7.19].

**Step 2.** Since A is a cube number and A is a cube number, by multiplying one another they make A*A. By Proposition 9.4, the product of two cube numbers is cube. Therefore A*A, that is A squared, is a cube number [9.4].

**Step 3.** Now A by multiplying A produces A squared, and A by multiplying B produces C (by hypothesis). By Proposition 7.17, if a number by multiplying two numbers make certain numbers, the numbers so produced will have the same ratio as the numbers multiplied. Therefore A squared is to C as A is to B [7.17].

**Step 4.** But A squared is a cube number (Step 2), and C is a cube number (by hypothesis). Therefore A is to B as a cube number is to a cube number.

**Step 5.** And A is a cube number. Since two numbers A and B have to one another the ratio which a cube number has to a cube number, and the first of them A is cube, therefore by Proposition 8.24 the second number B is also cube [8.24].

**Step 6.** Therefore, if a cube number by multiplying any number make a cube number, the multiplied number will also be cube. Q.E.D.

**USED:** 7.17, 8.24, 9.4, D7.19
**Human refs (from References field):** 7.17, 8.19, 8.23, 8.8, 9.3
**Jaccard:** 0.125 — AI adds ['8.24', '9.4', 'D7.19']; Human adds ['8.19', '8.23', '8.8', '9.3']

## Proposition 9.6
**Statement:** If a number by multiplying itself make a cube number, it will itself also be cube.

**Step 1.** Let A be a number such that A multiplied by itself makes B, so that A * A = B, and let B be a cube number. We are to show that A is itself a cube number.

**Step 2.** Since A * A = B, consider the product B * A. By substitution, B * A = (A * A) * A, which is A multiplied by A and the result multiplied again by A. By Definition 7.17, this is a solid number with three sides each equal to A, and by Definition 7.19, a cube number is equal multiplied by equal and again by equal. Since all three factors are A, the product B * A is the cube of A, and hence is a cube number.

**Step 3.** Now B is a cube number (given), and B multiplied by A produces B * A, which is a cube number (Step 2). By Proposition 9.5 (if a cube number by multiplying any number make a cube number, the multiplied number will also be cube), since B is cube and B * A is cube, it follows that A is a cube number.

**Step 4.** Therefore, if a number by multiplying itself makes a cube number, it will itself also be cube. Q.E.D.

**USED:** 9.5, D7.17, D7.19
**Human refs (from References field):** 8.19, 8.23, 8.8, D7.20
**Jaccard:** 0.000 — AI adds ['9.5', 'D7.17', 'D7.19']; Human adds ['8.19', '8.23', '8.8', 'D7.20']

## Proposition 9.7
**Statement:** If a composite number by multiplying any number make some number, the product will be solid.

**Step 1.** Let A be a composite number, and let A by multiplying any number D make E. We must show that E is solid.

**Step 2.** Since A is composite, by definition (D7.13), some number B measures A. Let B measure A according to the units in C, so that B multiplied by C equals A (D7.15).

**Step 3.** Since B multiplied by C produces A, the number A is plane with sides B and C (D7.16).

**Step 4.** Now since A multiplied by D produces E (given), and A equals B multiplied by C, therefore B multiplied by C and then by D produces E. That is, the three numbers B, C, D having multiplied one another produce E.

**Step 5.** But when three numbers having multiplied one another make some number, the product is solid (D7.17). Therefore E is solid.

**Step 6.** Therefore, if a composite number by multiplying any number make some number, the product will be solid. Q.E.D.

**USED:** D7.13, D7.15, D7.16, D7.17
**Human refs (from References field):** D7.13, D7.15
**Jaccard:** 0.500 — AI adds ['D7.16', 'D7.17']

## Proposition 9.8
**Statement:** If as many numbers as we please beginning from an unit be in continued proportion, the third from the unit will be square, as will also those which successively leave out one; the fourth will be cube, as will also all those which leave out two; and the seventh will be at once cube and square, as will also those which leave out five.

**Step 1.** Let there be as many numbers as we please, A1 = 1 (unit), A2, A3, A4, A5, A6, A7, ..., beginning from the unit and in continued proportion, so that as A1 is to A2, so is A2 to A3, and so on. Let the common ratio be A2; call it r.

**Step 2.** Since A1 = 1 (the unit) and the terms are in continued proportion with ratio r, we have A2 = r, and A3 = r multiplied by r. By D7.18, since A3 is the product of r multiplied by itself (equal multiplied by equal), A3 is a square number. Thus the third from the unit is square.

**Step 3.** Since A3, A4, A5 are three successive terms in the continued proportion, they are in continued proportion. Since A3 is square (Step 2), by 8.22 (if three numbers be in continued proportion and the first be square, the third will also be square), A5 is square. By the same reasoning applied to A5, A6, A7, since A5 is square, A7 is square. This pattern continues: each term that leaves out one from a square term is also square by 8.22. Therefore all terms in positions 3, 5, 7, 9, ... (i.e., those successively leaving out one from the third) are square.

**Step 4.** Now consider A4. Since A1 = 1, A2 = r, A3 = r times r, and A4 = r times r times r, A4 is the product of three equal numbers. By D7.19, A4 is a cube number. Thus the fourth from the unit is cube.

**Step 5.** Since A4, A5, A6, A7 are four successive terms in the continued proportion, they are in continued proportion. Since A4 is cube (Step 4), by 8.23 (if four numbers be in continued proportion and the first be cube, the fourth will also be cube), A7 is cube. By the same reasoning applied to A7, A8, A9, A10, since A7 is cube, A10 is cube. This pattern continues: each term that leaves out two from a cube term is also cube by 8.23. Therefore all terms in positions 4, 7, 10, 13, ... (i.e., those successively leaving out two from the fourth) are cube.

**Step 6.** Consider A7. By Step 3, A7 is square (being in position 7, which is among the odd positions 3, 5, 7, ...). By Step 5, A7 is cube (being in position 7, which is among the positions 4, 7, 10, ...). Therefore A7 is both cube and square. Thus the seventh from the unit is at once cube and square.

**Step 7.** For terms leaving out five from A7: the next such term is A13. Since A7 is square and A7, A8, ..., A13 includes A7, A9, A11, A13 as every-other terms, we apply 8.22 successively: A7 square implies A9 square (from A7, A8, A9), A9 square implies A11 square (from A9, A10, A11), A11 square implies A13 square (from A11, A12, A13). So A13 is square. Since A7 is cube and A7, A8, A9, A10 are four consecutive terms in continued proportion, by 8.23 A10 is cube; then A10, A11, A12, A13 are four consecutive terms and A10 is cube, so by 8.23 A13 is cube. Therefore A13 is both cube and square. The same argument applies to every subsequent term leaving out five, proceeding by repeated applications of 8.22 (three times) and 8.23 (twice) across each span of six terms.

**Step 8.** Therefore, among numbers beginning from a unit in continued proportion: the third from the unit is square, as are all those successively leaving out one; the fourth is cube, as are all those leaving out two; and the seventh is at once cube and square, as are all those leaving out five. Q.E.D.

**USED:** 8.22, 8.23, D7.18, D7.19
**Human refs (from References field):** 8.22, 8.23, D7.20
**Jaccard:** 0.400 — AI adds ['D7.18', 'D7.19']; Human adds ['D7.20']

## Proposition 9.9
**Statement:** If as many numbers as we please beginning from an unit be in continued proportion, and the number after the unit be square, all the rest will also be square.

**Step 1.** Let there be as many numbers as we please, A1, A2, A3, ..., An, beginning from a unit, in continued proportion. Suppose A1, the number after the unit, is square.

**Step 2.** Since the sequence begins from a unit and is in continued proportion, each consecutive triple of terms is itself in continued proportion. That is, for any index k, the three terms A(k-1), A(k), A(k+1) satisfy A(k-1) : A(k) = A(k) : A(k+1), where A(0) denotes the unit.

**Step 3.** The unit is equal multiplied by equal (the unit taken once is the unit), so the unit is square [D7.18].

**Step 4.** Consider the first three terms of the sequence: the unit, A1, and A2. These are in continued proportion. Since the unit is square, by Proposition 8.22 (if three numbers are in continued proportion and the first is square, the third is also square), A2 is square.

**Step 5.** Consider the three consecutive terms A1, A2, A3. These are in continued proportion. Since A1 is square by hypothesis, by 8.22, A3 is also square.

**Step 6.** Consider the three consecutive terms A2, A3, A4. These are in continued proportion. Since A2 is square (established in Step 4), by 8.22, A4 is also square.

**Step 7.** Consider the three consecutive terms A3, A4, A5. These are in continued proportion. Since A3 is square (established in Step 5), by 8.22, A5 is also square.

**Step 8.** In general, proceeding in this manner through the sequence: for any term A(k) where k >= 2, consider the triple A(k-2), A(k-1), A(k), which is in continued proportion. Since A(k-2) has already been shown to be square (the base cases being the unit for k=2 and A1 for k=3), it follows by 8.22 that A(k) is square.

**Step 9.** Therefore all the numbers in the continued proportion after the unit are square, which is what was to be proved.

**USED:** 8.22, D7.18
**Human refs (from References field):** 8.22, 8.23, 9.3, 9.8
**Jaccard:** 0.200 — AI adds ['D7.18']; Human adds ['8.23', '9.3', '9.8']

## Proposition 9.10
**Statement:** If as many numbers as we please beginning from an unit be in continued proportion, and the number after the unit be not square, neither will any other be square except the third from the unit and all those which leave out one.

**Step 1.** Let there be as many numbers as we please, A1 = 1, A2, A3, A4, ..., An, beginning from a unit and in continued proportion, so that A1 : A2 = A2 : A3 = A3 : A4 = ... and so on. Suppose that A2 (the number after the unit) is not square. We must show that no term is square except A3 (the third from the unit) and all those which leave out one, that is, the terms in odd position from the unit: A3, A5, A7, and so on.

**Step 2.** First, by 9.8, in any continued proportion beginning from a unit, the third from the unit is square, as are all those which successively leave out one (i.e., A3, A5, A7, ...). Thus the terms in odd positions from the unit are indeed square.

**Step 3.** It remains to show that no term in an even position from the unit (A2, A4, A6, ...) can be square. We proceed by contradiction. Suppose some term in an even position is square.

**Step 4.** Consider first A2 itself. By hypothesis, A2 is not square.

**Step 5.** Now suppose A4 is square. Since A1, A2, A3, A4 are in continued proportion beginning from a unit, A3 is the third from the unit and is square by 9.8. Now A2, A3, A4 are three numbers in continued proportion (since the original sequence is in continued proportion). The third of these, A4, is assumed square. By 8.22, if three numbers are in continued proportion and the third is square, the first is also square. (More precisely, 8.22 states that if three numbers are in continued proportion and the first is square, then the third is square. We use the contrapositive: if the first A2 is not square, then the third A4 cannot be square.) Since A2 is not square, A4 is not square, contradicting our assumption.

**Step 6.** Next suppose A6 is square. Consider the three consecutive terms A4, A5, A6 in continued proportion. We have shown in Step 5 that A4 is not square. Now A5 is square by 9.8 (being in an odd position). If A6 were square, then A4, A5, A6 would be three numbers in continued proportion with the third (A6) being square. By 8.22 (contrapositive, as in Step 5), the first A4 would have to be square. But A4 is not square (Step 5). Therefore A6 is not square.

**Step 7.** Similarly, for any even-positioned term A_{2k}, consider the three terms A_{2k-2}, A_{2k-1}, A_{2k} in continued proportion. By induction on the even positions: A_{2k-2} is not square (already established for earlier even positions), and A_{2k-1} is square by 9.8 (being in an odd position). If A_{2k} were square, then by 8.22 (contrapositive), A_{2k-2} would also be square, which contradicts the result already established. Therefore A_{2k} is not square.

**Step 8.** Since every even-positioned term from the unit fails to be square, and every odd-positioned term (the third and those which leave out one) is square by 9.8, we conclude: if the number after the unit is not square, no other number in the sequence is square except the third from the unit and all those which leave out one. Q.E.D.

**USED:** 8.22, 9.8
**Human refs (from References field):** 8.25, 8.26, 9.6, 9.8
**Jaccard:** 0.200 — AI adds ['8.22']; Human adds ['8.25', '8.26', '9.6']

## Proposition 9.11
**Statement:** If as many numbers as we please beginning from an unit be in continued proportion, the less measures the greater according to some one of the numbers which have place among the proportional numbers.

**Step 1.** Let there be as many numbers as we please beginning from the unit, in continued proportion: let the sequence be 1, A, B, C, D, where 1 : A = A : B = B : C = C : D. We must show that the less measures the greater according to some one of the numbers which have place among the proportional numbers.

**Step 2.** Since 1 : A = A : B, by 7.19 (the product of the extremes equals the product of the means), 1 times B equals A times A, so B = A times A. Therefore A measures B, and the measure is A itself, which has place among the proportional numbers. [D7.15, D7.3]

**Step 3.** Since 1 : A = B : C, by 7.19, 1 times C equals A times B, so C = A times B. Therefore A measures C according to B, and B measures C according to A; both A and B have place among the proportional numbers. [D7.15, D7.3]

**Step 4.** Since 1 : A = C : D, by 7.19, 1 times D equals A times C, so D = A times C. Therefore A measures D according to C, which has place among the proportional numbers. [D7.15, D7.3]

**Step 5.** Now we show that B also measures D. Since B = A times A (Step 2) and D = A times C (Step 4), and C = A times B (Step 3), we have D = A times (A times B) = (A times A) times B, that is, D = B times B, by 7.18 (if two numbers multiply a number, the products have the ratio of the multipliers) and the associativity established by 7.16 (a times b equals b times a, commutativity of multiplication). More directly: from the continued proportion, since 1 : B = B : D (the first, third, and fifth terms in the sequence, which are in continued proportion by 8.1, recognizing that the ratio 1 : B is duplicated), we have by 7.19 that 1 times D = B times B, so D = B times B. Therefore B measures D according to B, which has place among the proportional numbers.

**Step 6.** For the general argument: consider any two terms in the sequence, say the term in position k (counting the unit as position 1) and the term in position m, where k < m. The terms from position k to position m form a continued proportion of (m - k + 1) terms. By the construction of the original sequence from unity, the ratio between consecutive terms is always 1 : A, and so the term at position m equals the term at position k multiplied by the term at position (m - k + 1), which is itself a term in the original sequence (since m - k + 1 <= m, it has place among the proportional numbers).

**Step 7.** To see this precisely: since 1, A, B, C, D, ... are in continued proportion with common ratio 1 : A, each term is formed by multiplying the previous term by A (by repeated application of 7.19 to the proportion 1 : A = [preceding term] : [next term]). If the term at position k is P_k and the term at position m is P_m, then P_m = P_k multiplied by P_{m-k+1}, because the (m - k + 1)-th term in the original sequence represents A taken (m - k) times as a factor, which is exactly the factor between P_k and P_m. This follows from 7.16 (commutativity of multiplication: a times b = b times a) and the repeated application of 7.19 to the continued proportion.

**Step 8.** Therefore, in every case, the lesser term measures the greater, and the quotient is one of the terms that has place among the proportional numbers.

**Step 9.** Therefore, if as many numbers as we please beginning from an unit be in continued proportion, the less measures the greater according to some one of the numbers which have place among the proportional numbers. Q.E.D.

**USED:** 7.16, 7.18, 7.19, 8.1, D7.15, D7.3
**Human refs (from References field):** 7.15
**Jaccard:** 0.000 — AI adds ['7.16', '7.18', '7.19', '8.1', 'D7.15', 'D7.3']; Human adds ['7.15']

## Proposition 9.12
**Statement:** If as many numbers as we please beginning from an unit be in continued proportion, by however many prime numbers the last is measured, the next to the unit will also be measured by the same.

**Step 1.** Let there be as many numbers as we please, A1 = 1, A2, A3, ..., An, beginning from a unit and in continued proportion, and let the last number An be measured by some prime number p. We must show that p also measures A2, the number next to the unit.

**Step 2.** First consider the case where there are only two terms after the unit, so our sequence is 1, A2, A3, where A3 is the last. Since 1, A2, A3 are in continued proportion, we have 1 : A2 = A2 : A3, so A3 is the product of A2 multiplied by A2 (by Definition D7.15 and the properties of continued proportion from D7.20). That is, A3 = A2 times A2. Now p is prime and p measures A3 = A2 times A2. By Proposition 7.30, since a prime measuring a product must measure one of the factors, p measures A2. Thus the result holds when there are two terms after the unit.

**Step 3.** Now consider the general case with terms 1, A2, A3, ..., An in continued proportion. By Proposition 9.11, the less measures the greater according to some one of the numbers which have place among the proportional numbers. In particular, A2 measures An, and moreover An = A2 times A(n-1), since in the continued proportion 1 : A2 = A(n-1) : An, which gives An = A2 times A(n-1) (by D7.15 and the proportion D7.20).

**Step 4.** Since p is prime and p measures An = A2 times A(n-1), by Proposition 7.30, p measures A2 or p measures A(n-1).

**Step 5.** If p measures A2, the conclusion is established and we are done.

**Step 6.** If p does not measure A2, then p measures A(n-1). Now the numbers 1, A2, A3, ..., A(n-1) are themselves in continued proportion beginning from a unit (being the first n-1 terms of the original sequence), and A(n-1) is their last term, which is measured by the prime p.

**Step 7.** Apply the same reasoning to this shorter sequence: A(n-1) = A2 times A(n-2), so by Proposition 7.30, p measures A2 or p measures A(n-2). If p measures A2, we are done. Otherwise p measures A(n-2).

**Step 8.** Continuing in this manner, at each stage either p measures A2 and we are done, or p measures the preceding term in the sequence. Since the sequence is finite and decreasing toward A2, we must eventually reach the point where we consider that p measures A3. Now A3 = A2 times A2 (as shown in Step 2). By Proposition 7.30, p measures A2.

**Step 9.** Therefore, in all cases, the prime p measures A2, the number next to the unit. This is what was to be proved.

**USED:** 7.30, 9.11, D7.15, D7.20
**Human refs (from References field):** 7.19, 7.20, 7.21, 7.29, 9.11, 9.8, D7.14
**Jaccard:** 0.100 — AI adds ['7.30', 'D7.15', 'D7.20']; Human adds ['7.19', '7.20', '7.21', '7.29', '9.8', 'D7.14']

## Proposition 9.13
**Statement:** If as many numbers as we please beginning from an unit be in continued proportion, and the number after the unit be prime, the greatest will not be measured by any except those which have a place among the proportional numbers.

**Step 1.** Let there be as many numbers as we please, 1, A, B, C, D, beginning from a unit and in continued proportion, and let A (the number after the unit) be prime. We must show that D (the greatest) is not measured by any number except those which have a place among the proportional numbers 1, A, B, C.

**Step 2.** Suppose, for the sake of contradiction, that some number E measures D, and that E is not among the proportional numbers 1, A, B, C. Since E measures D and E is not the unit, E is greater than 1.

**Step 3.** Since E is greater than 1, by 7.31, some prime number F measures E.

**Step 4.** Now since F measures E and E measures D, it follows that F measures D. For if E measures D, then D is a multiple of E, say D = E * G; and since F measures E, E = F * H for some number; thus D = F * H * G, so F measures D. This is by the transitivity of measurement, which follows from D7.3 and D7.15.

**Step 5.** But D is the last term of the continued proportion beginning from 1, and F is a prime number measuring D. Therefore, by 9.12, F also measures A, the number next to the unit.

**Step 6.** Since A is prime, by D7.11 A is measured by a unit alone (and by itself). Since F is a prime number and F measures A, and the only divisors of A are 1 and A, we have F = A (for F, being prime, is greater than 1, so F cannot be the unit).

**Step 7.** Therefore every prime number that measures E is equal to A. That is, the only prime that measures E is A, so A measures E.

**Step 8.** Since A measures E, write E = A * K for some number K (by D7.15 and D7.3). Now since E measures D, D = E * M for some number M. By 9.11, since the numbers 1, A, B, C, D are in continued proportion from unity, the less measures the greater according to some one of the proportional numbers. In particular, A measures D, and A measures B, and so on.

**Step 9.** We now show that E must be among the proportional numbers by examining K. Since E = A * K and E measures D, we have A * K measures D. Now the sequence 1, A, B, C, D is a geometric progression with ratio A, so B = A * A, C = A * B, D = A * C. Thus D = A * C, so A * K measures A * C. By 7.17 (if a number multiplied by two numbers produces results, and one result measures the other, then the corresponding multiplied number measures the other), K measures C.

**Step 10.** Now if K = 1, then E = A * 1 = A, and E is among the proportional numbers, contradicting our assumption. So assume K is greater than 1. Then by the same argument as before: some prime F' measures K (by 7.31); since K measures C, F' measures C; since C is a term in the continued proportion from unity, and F' is prime and measures C, by 9.12, F' measures A; since A is prime, F' = A (by D7.11). So A measures K. Write K = A * L for some number L.

**Step 11.** Then E = A * K = A * A * L = B * L. Since E measures D, B * L measures D. Now D = A * C = A * A * B = B * A * A... more precisely, since D = A * C and C = A * B, we have D = A * A * B = B * A^2. Actually, using the continued proportion: D = A * C, C = A * B, B = A * A. So D = A * (A * (A * A)). But let us use 9.11 again: since B * L measures D, and B is among the proportional numbers, L measures the quotient by which B measures D. By 7.17, since B * L measures B * (A * A) (because D = B * A * A), L measures A * A = B.

**Step 12.** If L = 1, then K = A, so E = A * A = B, and E is among the proportional numbers, contradicting our assumption. If L > 1, we repeat the argument: some prime measures L, and by 9.12 and D7.11 that prime must be A, so A measures L. Write L = A * N. Then E = A * A * A * N = C * N, and since E measures D and D = A * C, C * N measures A * C, so by 7.17, N measures A. Since A is prime, either N = 1 or N = A (by D7.11).

**Step 13.** If N = 1, then E = C, which is among the proportional numbers -- contradiction. If N = A, then E = C * A = D, which means E equals the greatest number itself; but then E is among the proportional numbers -- again a contradiction.

**Step 14.** If E were even larger (in the case of more terms in the proportion), the process would continue: at each stage A divides the remaining factor, and since E measures D and the proportional numbers are 1, A, A*A, A*A*A, ..., and E must be a power of A (as the only prime dividing E is A), and E measures D, E cannot exceed D, so E must equal one of the proportional numbers. In all cases we reach a contradiction with our assumption that E is not among the proportional numbers.

**Step 15.** Therefore, the greatest number D is not measured by any number except those which have a place among the proportional numbers. Q.E.D.

**USED:** 7.17, 7.31, 9.11, 9.12, D7.11, D7.15, D7.3
**Human refs (from References field):** 7.19, 7.31, 9.11, 9.12, 9.8
**Jaccard:** 0.333 — AI adds ['7.17', 'D7.11', 'D7.15', 'D7.3']; Human adds ['7.19', '9.8']

## Proposition 9.14
**Statement:** If a number be the least that is measured by prime numbers, it will not be measured by any other prime number except those originally measuring it.

**Step 1.** Let A be the least number that is measured by the prime numbers p1, p2, ..., pn. Suppose, for the sake of contradiction, that some other prime number q, distinct from each of p1, p2, ..., pn, also measures A.

**Step 2.** Since q measures A, there exists a number B such that A = q * B [by D7.3, D7.5, D7.15].

**Step 3.** Since A = q * B, the numbers q and B multiplied together produce A. Now consider any one of the primes pi (where i ranges from 1 to n). Since pi measures A, and A is the product of q and B, and pi is prime, by 7.30 pi must measure one of the factors q or B.

**Step 4.** Now q is prime, so by D7.11 q is measured by a unit alone. The only numbers that measure q are therefore 1 and q itself. Since pi is prime, pi is greater than 1 [by D7.11, as a prime is a number, and a number is a multitude of units by D7.2, and it is not the unit itself]. And pi is distinct from q by hypothesis. Therefore pi does not measure q.

**Step 5.** Since pi measures one of q or B (Step 3), and pi does not measure q (Step 4), it follows that pi measures B. This holds for every prime pi among p1, p2, ..., pn.

**Step 6.** Therefore B is measured by each of the primes p1, p2, ..., pn.

**Step 7.** Since A = q * B and q is a prime number (hence q is at least 2), B is less than A [by CN5, since A is the whole and B is a part of A, as q measures A according to B, and q is not the unit].

**Step 8.** But A was supposed to be the least number measured by all of p1, p2, ..., pn. We have found B, a number less than A, that is also measured by all of p1, p2, ..., pn. This is a contradiction.

**Step 9.** Therefore no prime number other than p1, p2, ..., pn can measure A. Q.E.D.

**USED:** 7.30, CN5, D7.11, D7.15, D7.2, D7.3, D7.5
**Human refs (from References field):** 7.30
**Jaccard:** 0.143 — AI adds ['CN5', 'D7.11', 'D7.15', 'D7.2', 'D7.3', 'D7.5']

## Proposition 9.15
**Statement:** If three numbers in continued proportion be the least of those which have the same ratio with them, any two whatever added together will be prime to the remaining number.

**Step 1.** Let A, B, C be three numbers in continued proportion that are the least of those which have the same ratio with them, so that A:B = B:C. We must show that any two added together are prime to the remaining one, namely that A+B is prime to C, that B+C is prime to A, and that A+C is prime to B.

**Step 2.** Since A, B, C are three numbers in continued proportion and the least of those having the same ratio, by 8.2, there exist numbers p and q, the least in the ratio A:B, such that A = p*p, B = p*q, and C = q*q.

**Step 3.** Since p and q are the least numbers in the ratio A:B, by 7.22, p and q are prime to one another.

**Step 4.** [Proof that A+B is prime to C.] We have A+B = p*p + p*q = p*(p+q), and C = q*q. Since p is prime to q (Step 3), by 7.28, the sum p+q is prime to each of p and q. In particular, p+q is prime to q.

**Step 5.** Since p+q is prime to q (Step 4), by 7.25, q*q is prime to p+q; that is, p+q is prime to q*q = C.

**Step 6.** Since p is prime to q (Step 3), by 7.25, q*q is prime to p; that is, p is prime to q*q = C.

**Step 7.** Since both p and p+q are prime to C (Steps 6 and 5), by 7.24, their product p*(p+q) is also prime to C. But p*(p+q) = A+B. Therefore A+B is prime to C.

**Step 8.** [Proof that B+C is prime to A.] We have B+C = p*q + q*q = q*(p+q), and A = p*p. Since p is prime to q (Step 3), by 7.28, p+q is prime to p.

**Step 9.** Since p+q is prime to p (Step 8), by 7.25, p*p is prime to p+q; that is, p+q is prime to p*p = A.

**Step 10.** Since q is prime to p (Step 3), by 7.25, p*p is prime to q; that is, q is prime to p*p = A.

**Step 11.** Since both q and p+q are prime to A (Steps 10 and 9), by 7.24, their product q*(p+q) is also prime to A. But q*(p+q) = B+C. Therefore B+C is prime to A.

**Step 12.** [Proof that A+C is prime to B.] We have A+C = p*p + q*q, and B = p*q. Since p is prime to q (Step 3), by 7.26, since p is prime to q and p is prime to q, we have p*p prime to q*q; that is, A is prime to C.

**Step 13.** Since A = p*p is prime to C = q*q (Step 12), by 7.28, their sum A+C = p*p + q*q is prime to both p*p and q*q. In particular, A+C is prime to p*p = A, and A+C is prime to q*q = C.

**Step 14.** Since A+C is prime to A (Step 13), suppose d is any common measure of A+C and p. Then d measures p, so d measures p*p = A. But then d is a common measure of A+C and A. Since A+C is prime to A (Step 13), d must be a unit. Therefore A+C is prime to p.

**Step 15.** Since A+C is prime to C (Step 13), suppose d is any common measure of A+C and q. Then d measures q, so d measures q*q = C. But then d is a common measure of A+C and C. Since A+C is prime to C (Step 13), d must be a unit. Therefore A+C is prime to q.

**Step 16.** Since A+C is prime to p and A+C is prime to q (Steps 14 and 15), by 7.24, A+C is prime to p*q = B.

**Step 17.** Therefore any two of the three numbers A, B, C added together are prime to the remaining number. Q.E.D.

**USED:** 7.22, 7.24, 7.25, 7.26, 7.28, 8.2, D7.12
**Human refs (from References field):** 2.3, 2.4, 7.22, 7.24, 7.25, 7.28, 8.2
**Jaccard:** 0.556 — AI adds ['7.26', 'D7.12']; Human adds ['2.3', '2.4']

## Proposition 9.16
**Statement:** If two numbers be prime to one another, the second will not be to any other number as the first is to the second.

**Step 1.** Let A and B be two numbers prime to one another. Suppose, for the sake of contradiction, that B is to some number C as A is to B; that is, suppose A:B = B:C.

**Step 2.** Since A and B are prime to one another, by definition (D7.12) the only common measure of A and B is the unit. By Proposition 7.21, numbers prime to one another are the least of those which have the same ratio with them. Therefore A and B are the least numbers among all pairs having the ratio A:B.

**Step 3.** Now since A:B = B:C, and A, B are the least numbers in the ratio A:B, by Proposition 7.20 the least numbers measure any numbers having the same ratio with them, the greater the greater and the less the less. Applying this to the proportion A:B = B:C, we conclude that A measures B (the antecedent of the least pair measures the antecedent of any pair in the same ratio, so A divides B).

**Step 4.** Since A measures B, A is a common measure of A and B. But A and B are prime to one another, so the only common measure of A and B is the unit (D7.12). Therefore A must be a unit.

**Step 5.** However, A was given as a number. By definition (D7.2), a number is a multitude composed of units, which is distinct from the unit itself (D7.1). Thus A cannot be both a number and a unit; this is a contradiction.

**Step 6.** Therefore our supposition is false, and there is no number C such that A:B = B:C. That is, the second number B will not be to any other number as the first A is to the second B. Q.E.D.

**USED:** 7.20, 7.21, D7.1, D7.12, D7.2
**Human refs (from References field):** 7.20, 7.21
**Jaccard:** 0.400 — AI adds ['D7.1', 'D7.12', 'D7.2']

## Proposition 9.17
**Statement:** If there be as many numbers as we please in continued proportion, and the extremes of them be prime to one another, the last will not be to any other number as the first to the second.

**Step 1.** Let A_1, A_2, ..., A_n be as many numbers as we please in continued proportion, so that A_1:A_2 = A_2:A_3 = ... = A_{n-1}:A_n, and let A_1 and A_n (the extremes) be prime to one another. We must show that A_n is not to any other number as A_1 is to A_2.

**Step 2.** Since A_1, A_2, ..., A_n are in continued proportion and the extremes A_1 and A_n are prime to one another, by Proposition 8.1 these numbers are the least of those which have the same ratio with them.

**Step 3.** Since A_1, A_2, ..., A_n are the least numbers of those in continued proportion with that ratio, by Proposition 7.22 any two consecutive terms are prime to one another. In particular, A_{n-1} and A_n are prime to one another.

**Step 4.** Since the numbers are in continued proportion, A_{n-1}:A_n = A_1:A_2 (all consecutive ratios in a continued proportion are equal).

**Step 5.** Since A_{n-1} and A_n are prime to one another (Step 3), by Proposition 9.16, A_n will not be to any other number as A_{n-1} is to A_n.

**Step 6.** But A_{n-1}:A_n is the same ratio as A_1:A_2 (Step 4). Therefore A_n is not to any other number as A_1 is to A_2, which is what was to be proved.

**USED:** 7.22, 8.1, 9.16
**Human refs (from References field):** 7.13, 7.20, 7.21
**Jaccard:** 0.000 — AI adds ['7.22', '8.1', '9.16']; Human adds ['7.13', '7.20', '7.21']

## Proposition 9.18
**Statement:** Given two numbers, to investigate whether it is possible to find a third proportional to them.

**Step 1.** Let A and B be two given numbers. We investigate whether it is possible to find a third proportional C to them, that is, a number C such that A : B = B : C.

**Step 2.** Let B, multiplied by itself, produce D. [D7.15]

**Step 3.** Then either A measures D, or A does not measure D.

**Step 4.** First, suppose A measures D. Then there exists a number C such that D = A * C. [D7.3, D7.15]

**Step 5.** Since B, multiplied by itself, produces D, we have D = B * B. And since D = A * C, it follows that A * C = B * B.

**Step 6.** Since the product of the first and fourth (A * C) equals the product of the second and third (B * B), the four numbers A, B, B, C are proportional, that is, A : B = B : C. [7.19]

**Step 7.** Therefore a third proportional C to A and B has been found.

**Step 8.** Now suppose A does not measure D, where D = B * B. We claim that no third proportional to A and B exists.

**Step 9.** For suppose, for the sake of contradiction, that there exists a number E such that A : B = B : E.

**Step 10.** Since A, B, B, E are proportional, the product of the first and fourth equals the product of the second and third, that is, A * E = B * B = D. [7.19]

**Step 11.** Therefore A * E = D, which means A measures D. [D7.3, D7.15]

**Step 12.** But this contradicts the assumption that A does not measure D. Therefore no third proportional to A and B exists in this case.

**Step 13.** Therefore, given two numbers A and B, it is possible to find a third proportional to them if and only if A measures the product of B multiplied by itself. Q.E.D.

**USED:** 7.19, D7.15, D7.3
**Human refs (from References field):** 7.19, 9.16
**Jaccard:** 0.250 — AI adds ['D7.15', 'D7.3']; Human adds ['9.16']

## Proposition 9.19
**Statement:** Given three numbers, to investigate when it is possible to find a fourth proportional to them.

**Step 1.** Let A, B, C be three given numbers. We investigate when it is possible to find a fourth number D such that A, B, C, D are proportional, that is, A : B = C : D. [D7.20]

**Step 2.** Let B multiply C, producing the number E, so that E = B * C. [D7.15]

**Step 3.** First, suppose that A measures E. Then there exists a number D such that E = A * D, that is, A * D = B * C. [D7.3, D7.15]

**Step 4.** Since A * D = B * C, by 7.19 the four numbers A, B, C, D are proportional, that is, A : B = C : D. Therefore a fourth proportional to A, B, C has been found, namely D. [7.19]

**Step 5.** Now suppose that A does not measure E, that is, A does not measure the product B * C. We claim that no fourth proportional D exists.

**Step 6.** Assume for the sake of contradiction that there exists a number D such that A : B = C : D. Then since A, B, C, D are proportional, by 7.19 the product of the first and fourth equals the product of the second and third, that is, A * D = B * C. [7.19]

**Step 7.** But A * D = B * C means that B * C is equal to A multiplied by D, so A measures B * C, that is, A measures E. [D7.3, D7.15]

**Step 8.** This contradicts the assumption in Step 5 that A does not measure E. Therefore no such D exists, and it is not possible to find a fourth proportional to A, B, C in this case.

**Step 9.** Therefore, given three numbers A, B, C, it is possible to find a fourth proportional to them if and only if the first number A measures the product of the second and third, B * C. Q.E.D.

**USED:** 7.19, D7.15, D7.20, D7.3
**Human refs (from References field):** 7.14, 7.19, 7.20, 7.21, 9.17
**Jaccard:** 0.125 — AI adds ['D7.15', 'D7.20', 'D7.3']; Human adds ['7.14', '7.20', '7.21', '9.17']

## Proposition 9.20
**Statement:** Prime numbers are more than any assigned multitude of prime numbers.

**Step 1.** Let A, B, C be any assigned multitude of prime numbers. We shall show that there exists some prime number beyond this collection.

**Step 2.** Take the least number measured by A, B, and C; call it DE. (That is, form the product A * B * C, which by D7.15 is the number produced by successive multiplication.) Each of A, B, and C measures DE by construction.

**Step 3.** Add the unit to DE, obtaining the number EF = DE + 1. By CN5 (the whole is greater than the part), EF is greater than each of A, B, and C individually.

**Step 4.** Now EF is either prime or not prime.

**Step 5.** Case I: Suppose EF is prime. Then since EF is greater than each of A, B, and C, it is a prime number distinct from all of them. Thus a prime has been found which is not among the assigned primes A, B, C.

**Step 6.** Case II: Suppose EF is not prime. Then EF is composite (D7.13). By 7.31, every composite number is measured by some prime number. Let the prime number G measure EF.

**Step 7.** We claim that G is not equal to any of A, B, or C. Suppose, for contradiction, that G is equal to one of them, say G = A. Now A measures DE (by construction in Step 2), and G measures EF (by Step 6). Since G = A, it follows that A measures both DE and EF.

**Step 8.** Since A measures DE and EF = DE + 1, if A measured EF it would also measure the difference EF - DE = 1. (For if a number measures both a whole number and a part of it, it measures the remainder; this follows from D7.3 and the nature of measurement.) But A is a prime and hence is at least 2 (D7.11: a prime is measured by a unit alone, so a prime is not itself a unit). No number greater than 1 can measure the unit (D7.1), yielding a contradiction.

**Step 9.** By the same reasoning, G is not equal to B, and G is not equal to C. Therefore G is a prime number distinct from all of A, B, and C.

**Step 10.** In either case (EF prime, or EF composite), we have produced a prime number not among the originally assigned primes A, B, C. Since A, B, C were any assigned multitude of prime numbers, it follows that the prime numbers are more than any assigned multitude of prime numbers. Q.E.D.

**USED:** 7.31, CN5, D7.1, D7.11, D7.13, D7.15, D7.3
**Human refs (from References field):** 7.31
**Jaccard:** 0.143 — AI adds ['CN5', 'D7.1', 'D7.11', 'D7.13', 'D7.15', 'D7.3']

## Proposition 9.21
**Statement:** If as many even numbers as we please be added together, the whole is even.

**Step 1.** Let AB, BC, CD be any multitude of even numbers, and let their sum be the number AD. We are to show that AD is even.

**Step 2.** Since AB is even, by Definition 7.6 it is divisible into two equal parts. Let AB = AE + EB where AE = EB. Similarly, since BC is even, BC = BF + FC where BF = FC. And since CD is even, CD = CG + GD where CG = GD.

**Step 3.** Now the sum AD = AB + BC + CD = (AE + EB) + (BF + FC) + (CG + GD).

**Step 4.** Consider the sum of the halves: AE + BF + CG. Since AE = EB, BF = FC, and CG = GD, by Common Notion 2 (if equals be added to equals, the wholes are equal), we have AE + BF + CG = EB + FC + GD.

**Step 5.** Therefore AD = (AE + BF + CG) + (EB + FC + GD) = (AE + BF + CG) + (AE + BF + CG), so AD is divided into two equal parts, each equal to AE + BF + CG.

**Step 6.** Since AD is divisible into two equal parts, AD is even by Definition 7.6.

**Step 7.** The same argument applies regardless of how many even numbers are taken: each is halved, the halves are summed, and the total equals twice that sum. Therefore, if as many even numbers as we please be added together, the whole is even. Q.E.D.

**USED:** CN2, D7.6
**Human refs (from References field):** D7.6
**Jaccard:** 0.500 — AI adds ['CN2']

## Proposition 9.22
**Statement:** If as many odd numbers as we please be added together, and their multitude be even, the whole will be even.

**Step 1.** Let as many odd numbers as we please, A1, A2, ..., A2n, be added together, and let their multitude be even.

**Step 2.** Since each Ai is odd, by D7.7 each odd number differs by a unit from an even number. Thus for each Ai there exists an even number Ei such that Ai = Ei + 1.

**Step 3.** Therefore the sum A1 + A2 + ... + A2n = (E1 + 1) + (E2 + 1) + ... + (E2n + 1) = (E1 + E2 + ... + E2n) + (1 + 1 + ... + 1), where the number of units equals the multitude of the odd numbers. [CN2]

**Step 4.** Now E1, E2, ..., E2n are all even numbers. By 9.21, the sum of as many even numbers as we please is even. Therefore E1 + E2 + ... + E2n is even.

**Step 5.** The number of units added is equal to the multitude of the odd numbers, which is even by hypothesis. By D7.6, an even number is divisible into two equal parts, so this sum of units is even.

**Step 6.** Thus the total sum equals the sum of two even numbers: the even sum (E1 + E2 + ... + E2n) and the even sum of units. By 9.21, the sum of even numbers is even. Therefore the whole sum A1 + A2 + ... + A2n is even.

**Step 7.** Therefore, if as many odd numbers as we please be added together, and their multitude be even, the whole will be even. Q.E.D.

**USED:** 9.21, CN2, D7.6, D7.7
**Human refs (from References field):** 9.21, D7.7
**Jaccard:** 0.500 — AI adds ['CN2', 'D7.6']

## Proposition 9.23
**Statement:** If as many odd numbers as we please be added together, and their multitude be odd, the whole will also be odd.

**Step 1.** Let there be as many odd numbers as we please, A1, A2, ..., An, and let their multitude n be odd. We must show that their sum S = A1 + A2 + ... + An is odd.

**Step 2.** Since the multitude n is odd, by D7.7 it differs by a unit from an even number. Therefore n - 1 is even, and n is at least 1, so we may set aside one of the odd numbers, say An.

**Step 3.** The remaining numbers A1, A2, ..., A(n-1) are odd numbers whose multitude n - 1 is even. By 9.22, their sum T = A1 + A2 + ... + A(n-1) is even.

**Step 4.** Since An is odd, by D7.7 it differs by a unit from an even number. That is, An = E + 1 for some even number E.

**Step 5.** Now S = T + An = T + E + 1. Since T is even (Step 3) and E is even (Step 4), by 9.21 the sum T + E is even.

**Step 6.** Therefore S = (T + E) + 1, which is an even number plus a unit. By D7.7, S is odd.

**Step 7.** Therefore, if as many odd numbers as we please be added together, and their multitude be odd, the whole is also odd. Q.E.D.

**USED:** 9.21, 9.22, D7.7
**Human refs (from References field):** 9.21, 9.22, D7.7
**Jaccard:** 1.000 — Perfect match.

## Proposition 9.24
**Statement:** If from an even number an even number be subtracted, the remainder will be even.

**Step 1.** Let AB be an even number, and let BC, an even number, be subtracted from it. I say that the remainder AC is also even.

**Step 2.** Since AB is even, by Definition D7.6, AB is divisible into two equal parts. Let AB = D + D, where D is the half of AB.

**Step 3.** Since BC is even, by Definition D7.6, BC is divisible into two equal parts. Let BC = E + E, where E is the half of BC.

**Step 4.** Now AC = AB - BC. Since AB = D + D and BC = E + E, the half of AB is D and the half of BC is E.

**Step 5.** Subtracting equals from equals: since AB = 2D and BC = 2E, we subtract BC from AB. By CN3 (if equals be subtracted from equals, the remainders are equal), subtracting E from D on each side, we get that AC = (D - E) + (D - E).

**Step 6.** Therefore AC is divisible into two equal parts, each equal to D - E.

**Step 7.** Since AC is divisible into two equal parts, AC is even by Definition D7.6.

**Step 8.** Therefore, if from an even number an even number be subtracted, the remainder is even. Q.E.D.

**USED:** CN3, D7.6
**Human refs (from References field):** D7.6
**Jaccard:** 0.500 — AI adds ['CN3']

## Proposition 9.25
**Statement:** If from an even number an odd number be subtracted, the remainder will be odd.

**Step 1.** Let AB be an even number, and let BC be an odd number subtracted from it. We are to show that the remainder AC is odd.

**Step 2.** Since BC is odd, by Definition D7.7, it differs by a unit from an even number. Let BD be this unit, so that DC equals BC minus one unit, and DC is even.

**Step 3.** Now AB is even and DC is even. But we need to consider the subtraction differently. Since BC is odd, subtract the unit BD from BC to obtain DC, which is even. Equivalently, decompose BC into DC (even) and BD (a unit), where BD = 1.

**Step 4.** Since AB is even and DC is even, their difference AB minus DC is even, by Proposition 9.24.

**Step 5.** But AB minus DC equals AB minus (BC minus BD) equals (AB minus BC) plus BD equals AC plus BD. Therefore AC plus BD is even, that is, AC plus one unit is even.

**Step 6.** Since AC plus a unit is even, AC differs by a unit from an even number. Therefore, by Definition D7.7, AC is odd.

**Step 7.** Therefore, if from an even number an odd number be subtracted, the remainder is odd. Q.E.D.

**USED:** 9.24, D7.7
**Human refs (from References field):** 9.24, D7.7
**Jaccard:** 1.000 — Perfect match.

## Proposition 9.26
**Statement:** If from an odd number an odd number be subtracted, the remainder will be even.

**Step 1.** Let AB be an odd number, and let BC be an odd number subtracted from it. I say that the remainder AC is even.

**Step 2.** Since AB is odd, let the unit BD be subtracted from it. Then AD is even, for an odd number differs by a unit from an even number [D7.7].

**Step 3.** Since BC is also odd, let the same unit BD be subtracted from it. Then DC is even, by the same reasoning [D7.7].

**Step 4.** Now AC equals AD with DC subtracted from it. Since AD is even and DC is even, the remainder AC is even [9.24].

**Step 5.** Therefore, if from an odd number an odd number be subtracted, the remainder is even. Q.E.D.

**USED:** 9.24, D7.7
**Human refs (from References field):** 9.24, D7.7
**Jaccard:** 1.000 — Perfect match.

## Proposition 9.27
**Statement:** If from an odd number an even number be subtracted, the remainder will be odd.

**Step 1.** Let A be an odd number, and let the even number B be subtracted from A, leaving the remainder C, so that A = B + C.

**Step 2.** Suppose, for the sake of contradiction, that C is even.

**Step 3.** Since B is even and C is even, by Proposition 9.21 (if as many even numbers as we please be added together, the whole is even), their sum B + C is even.

**Step 4.** But B + C equals A, so A would be even.

**Step 5.** This contradicts the hypothesis that A is odd (D7.7: an odd number is not divisible into two equal parts, and so is not even per D7.6).

**Step 6.** Therefore the assumption that C is even is false, and hence C is odd. Q.E.D.

**USED:** 9.21, D7.6, D7.7
**Human refs (from References field):** 9.24, D7.7
**Jaccard:** 0.250 — AI adds ['9.21', 'D7.6']; Human adds ['9.24']

## Proposition 9.28
**Statement:** If an odd number by multiplying an even number make some number, the product will be even.

**Step 1.** Let A be an odd number and B be an even number, and let A multiplied by B produce C. We must show that C is even.

**Step 2.** By Definition 7.15, since A multiplied by B produces C, this means that B is added to itself as many times as there are units in A. That is, C is the sum of A copies of B.

**Step 3.** Since B is even (by hypothesis and Definition 7.6), each of the A summands in this sum is an even number.

**Step 4.** We thus have A even numbers added together (each equal to B). By Proposition 9.21, if as many even numbers as we please be added together, the whole is even.

**Step 5.** Therefore C, being the sum of A even numbers, is even. Hence if an odd number by multiplying an even number make some number, the product will be even. Q.E.D.

**USED:** 9.21, D7.15, D7.6
**Human refs (from References field):** 9.21, D7.15
**Jaccard:** 0.667 — AI adds ['D7.6']

## Proposition 9.29
**Statement:** If an odd number by multiplying an odd number make some number, the product will be odd.

**Step 1.** Let A and B be odd numbers, and let A multiplied by B produce C. We must show that C is odd.

**Step 2.** By the definition of multiplication (D7.15), A multiplied by B means that B is added to itself as many times as there are units in A, and the result is C. That is, C is the sum of A copies of B.

**Step 3.** Since B is odd (D7.7), each of the A terms in this sum is an odd number.

**Step 4.** Since A is odd, the multitude of these terms is odd.

**Step 5.** We therefore have as many odd numbers as we please (namely A copies of B) added together, and their multitude (A) is odd. By Proposition 9.23, the whole sum is odd.

**Step 6.** Therefore C, being this sum, is odd. This is what was to be proved.

**USED:** 9.23, D7.15, D7.7
**Human refs (from References field):** 9.23, D7.15
**Jaccard:** 0.667 — AI adds ['D7.7']

## Proposition 9.30
**Statement:** If an odd number measure an even number, it will also measure the half of it.

**Step 1.** Let A be an odd number that measures an even number B. We are to show that A also measures the half of B.

**Step 2.** Since B is even, by definition it is divisible into two equal parts [D7.6]. Let C be the half of B, so that B = C + C.

**Step 3.** Since A measures B, there exists a number D such that D times A equals B [D7.3, D7.15]. That is, A taken D times produces B.

**Step 4.** I claim D must be even. For suppose D were odd. Then D, being odd, multiplied by A, which is also odd, would produce an odd number [9.29]. But B is even, which is a contradiction. Therefore D is not odd.

**Step 5.** Since D is not odd, D is even [D7.7].

**Step 6.** Since D is even, D is divisible into two equal parts [D7.6]. Let E be the half of D, so that D = E + E.

**Step 7.** Now B = D times A. Since D = E + E, the number B equals A taken (E + E) times. But A taken (E + E) times is the same as A taken E times together with A taken E times. Let F equal A taken E times, so that E times A equals F [D7.15]. Then B = F + F.

**Step 8.** We have established that B = C + C and also B = F + F. Suppose F were greater than C. Then F + F would be greater than C + C [CN5], contradicting the fact that both equal B. Similarly, if F were less than C, then F + F would be less than C + C, again a contradiction. Therefore F = C.

**Step 9.** Since E times A equals F, and F = C, we have E times A equals C [CN1]. Therefore A measures C, the half of B [D7.3].

**Step 10.** Hence, if an odd number measures an even number, it also measures the half of it. Q.E.D.

**USED:** 9.29, CN1, CN5, D7.15, D7.3, D7.6, D7.7
**Human refs (from References field):** 9.23
**Jaccard:** 0.000 — AI adds ['9.29', 'CN1', 'CN5', 'D7.15', 'D7.3', 'D7.6', 'D7.7']; Human adds ['9.23']

## Proposition 9.31
**Statement:** If an odd number be prime to any number, it will also be prime to the double of it.

**Step 1.** Let A be an odd number which is prime to any number B. We are to show that A is also prime to the double of B, that is, to 2B.

**Step 2.** Since A is odd, it is not divisible into two equal parts, that is, 2 does not measure A. [D7.7]

**Step 3.** Now 2 is a prime number, since it is measured by a unit alone. [D7.11]

**Step 4.** Since 2 is prime and does not measure A, it follows that 2 and A are prime to one another. [7.29]

**Step 5.** Since A is prime to B (given), B is also prime to A, for numbers prime to one another are measured by a unit alone as a common measure, and this relation is symmetric. [D7.12]

**Step 6.** Similarly, since 2 and A are prime to one another (Step 4), 2 is prime to A. [D7.12]

**Step 7.** Thus two numbers, 2 and B, are each prime to A. Therefore their product, 2 times B, is also prime to A. [7.24]

**Step 8.** Since 2B is prime to A, A is also prime to 2B. [D7.12]

**Step 9.** Therefore, if an odd number be prime to any number, it will also be prime to the double of it. Q.E.D.

**USED:** 7.24, 7.29, D7.11, D7.12, D7.7
**Human refs (from References field):** 9.30
**Jaccard:** 0.000 — AI adds ['7.24', '7.29', 'D7.11', 'D7.12', 'D7.7']; Human adds ['9.30']

## Proposition 9.32
**Statement:** Each of the numbers which are continually doubled beginning from a dyad is even-times even only.

**Step 1.** Let A be any number in the sequence obtained by continually doubling a dyad. Then the sequence from the unit is 1, 2, 4, 8, ..., A, where each term is double the preceding one. These numbers are in continued proportion from the unit with ratio 2, and A equals 2 multiplied by itself some number of times, that is, A is a power of 2.

**Step 2.** Since the numbers 1, 2, 4, ..., A are in continued proportion beginning from the unit, and 2 (the number after the unit) is prime -- for 2 is measured by a unit alone [D7.11] -- it follows by Proposition 9.13 that A is not measured by any number except those which have a place among the proportional numbers, namely 1, 2, 4, ..., and the powers of 2 less than A.

**Step 3.** Now each of the numbers 2, 4, 8, ..., which have a place among the proportional numbers (other than the unit), is even. For each such number is obtained by doubling, so it is divisible into two equal parts [D7.6]. Therefore every number that measures A is even.

**Step 4.** Suppose, for the sake of contradiction, that A is even-times odd, that is, that A is measured by some even number according to an odd number [D7.9]. Then there exists an odd number which measures A. But by Step 2, every number measuring A is one of the proportional numbers 2, 4, 8, ..., and by Step 3, each of these is even. Hence no odd number measures A. This contradicts the assumption, so A is not even-times odd.

**Step 5.** We show that A is even-times even [D7.8]. Since A is in the sequence of continually doubled numbers and A is greater than 2, we can write A as the product of two of the proportional numbers: let B and C be numbers in the sequence 2, 4, 8, ... such that B multiplied by C equals A. (For instance, A is double some preceding term, so A = 2 times the preceding power of 2, and the preceding power of 2 is at least 2.) By Step 3, both B and C are even. Therefore A is measured by the even number B according to the even number C, and so A is even-times even [D7.8].

**Step 6.** Since A is even-times even (Step 5) and not even-times odd (Step 4), A is even-times even only. And A was taken as an arbitrary number in the sequence of continually doubled numbers beginning from a dyad. Therefore each of the numbers which are continually doubled beginning from a dyad is even-times even only. Q.E.D.

**USED:** 9.13, D7.11, D7.6, D7.8, D7.9
**Human refs (from References field):** 9.13, D7.8
**Jaccard:** 0.400 — AI adds ['D7.11', 'D7.6', 'D7.9']

## Proposition 9.33
**Statement:** If a number have its half odd, it is even-times odd only.

**Step 1.** Let N be a number whose half is odd. Then N is divisible into two equal parts (so N is even by D7.6), and N = 2m where m is the half of N and m is odd.

**Step 2.** Since 2 is even and 2 measures N according to m, which is odd, N is an even-times odd number by D7.9.

**Step 3.** We now show that N is not also even-times even. Suppose, for the sake of contradiction, that N is even-times even. Then by D7.8, some even number a measures N according to an even number b, so that N = a * b with a even and b even.

**Step 4.** Since a is even, by D7.6, a is divisible into two equal parts, so a = 2c for some number c. Then since a measures N and a = 2c, we have N = 2c * b.

**Step 5.** Since N = 2m and N = 2c * b, and c measures a while a measures N, it follows that c measures N. Moreover, since a = 2c measures N according to b, and 2 measures a according to c, the number c measures N according to 2b, so that m = c * b (since N = 2m = 2 * (c * b), and 2 measures N according to m on one hand and according to c * b on the other, whence m = c * b by D7.15).

**Step 6.** Now m is odd and m = c * b. We consider whether c is even or odd. First suppose c is even. Then b * c = c * b = m by 7.16 (commutativity of multiplication). Since c is even and b is any number, we write c = 2k for some k. Then m = b * 2k, and so b (taken as a number) multiplied by c (even) gives m. Since c is even and b is a number: if b is odd, then by 9.28, b (odd) multiplied by c (even) produces an even number, so m would be even — contradicting m being odd. If b is even, then by 7.16, b * c = c * b, and c (even) multiplied by b: if c is even, write c = 2k, so m = c * b = 2k * b = 2 * (k * b), meaning 2 measures m, so m is even by D7.6 — again contradicting m being odd.

**Step 7.** Therefore c must be odd. But b is even (by our supposition in Step 3). Then c (odd) multiplied by b (even) produces m. By 9.28, since an odd number (c) multiplied by an even number (b) makes some number, that product is even. So m is even — contradicting the hypothesis that m is odd.

**Step 8.** In every case we reach a contradiction. Therefore N is not even-times even.

**Step 9.** Since N is even-times odd (Step 2) and not even-times even (Step 8), N is even-times odd only. This is what was to be proved.

**USED:** 7.16, 9.28, D7.15, D7.3, D7.6, D7.8, D7.9
**Human refs (from References field):** D7.8, D7.9
**Jaccard:** 0.286 — AI adds ['7.16', '9.28', 'D7.15', 'D7.3', 'D7.6']

## Proposition 9.34
**Statement:** If a number neither be one of those which are continually doubled from a dyad, nor have its half odd, it is both even-times even and even-times odd.

**Step 1.** Let N be a number which is neither one of those continually doubled from a dyad, nor has its half odd. Since N has a half, N is even [D7.6]. Since the half of N is not odd, the half of N is even [D7.6, D7.7].

**Step 2.** Since the half of N is even, N is measured by 2, and the result of the measurement, namely N/2, is itself even. Thus N is measured by the even number 2 according to the even number N/2. Therefore N is even-times even [D7.8].

**Step 3.** Now we must show N is also even-times odd. Since N/2 is even, N/2 has a half, call it M, so that N = 4M. Consider M: either M is odd or M is even.

**Step 4.** If M is odd, then N = 4M, where 4 is even and M is odd. Thus N is measured by the even number 4 according to the odd number M. Therefore N is even-times odd [D7.9].

**Step 5.** If M is even, then M has a half. We continue halving: since N is not one of the numbers continually doubled from a dyad (that is, not 2, 4, 8, 16, ...) [9.32], N cannot be a power of 2. Therefore the repeated halving of N cannot always yield even numbers; at some stage we must reach an odd number.

**Step 6.** More precisely, we can write N = 2^k * Q where k is a positive integer and Q is odd, with k >= 2 (since N/2 is even). Since N is not in the sequence continually doubled from a dyad, Q cannot be 1, so Q is an odd number greater than or equal to 1 (and in particular Q is a legitimate number by D7.2). The number 2^k is even, since k >= 2 means 2^k = 2 * 2^(k-1) and is measured by 2 [D7.6]. Since Q is odd, N is measured by the even number 2^k according to the odd number Q. Therefore N is even-times odd [D7.9].

**Step 7.** In either case (Step 4 or Step 6), N is even-times odd. Combined with Step 2, N is both even-times even and even-times odd. This is what was to be proved.

**USED:** 9.32, D7.2, D7.6, D7.7, D7.8, D7.9
**Human refs (from References field):** D7.8
**Jaccard:** 0.167 — AI adds ['9.32', 'D7.2', 'D7.6', 'D7.7', 'D7.9']

## Proposition 9.35
**Statement:** If as many numbers as we please be in continued proportion, and there be subtracted from the second and the last numbers equal to the first, then, as the excess of the second is to the first, so will the excess of the last be to all those before it.

**Step 1.** Let A1, A2, A3, ..., An be as many numbers as we please in continued proportion, so that A1:A2 = A2:A3 = ... = A(n-1):An. Suppose there be subtracted from A2 and from An numbers equal to A1. We must show that (A2 - A1):A1 = (An - A1):(A1 + A2 + ... + A(n-1)).

**Step 2.** Since A1, A2, A3, ..., An are in continued proportion, we have A1:A2 = A2:A3 = A3:A4 = ... = A(n-1):An [by the definition of continued proportion, D5.8, D7.20].

**Step 3.** Since A1:A2 = A2:A3, and A2 > A1, A3 > A2, by separando [5.17], (A2 - A1):A1 = (A3 - A2):A2.

**Step 4.** Likewise, since A2:A3 = A3:A4, by separando [5.17], (A3 - A2):A2 = (A4 - A3):A3.

**Step 5.** Continuing in this manner for each consecutive pair of equal ratios in the continued proportion, by repeated application of separando [5.17], we obtain (A2 - A1):A1 = (A3 - A2):A2 = (A4 - A3):A3 = ... = (An - A(n-1)):A(n-1).

**Step 6.** Therefore, the numbers (A2 - A1), (A3 - A2), (A4 - A3), ..., (An - A(n-1)) are to the numbers A1, A2, A3, ..., A(n-1) respectively in the same ratio [from Step 5].

**Step 7.** Since there are as many numbers as we please in proportion, namely (A2 - A1):A1 = (A3 - A2):A2 = ... = (An - A(n-1)):A(n-1), by 7.12, as one of the antecedents is to one of the consequents, so are all the antecedents to all the consequents. Therefore (A2 - A1):A1 = [(A2 - A1) + (A3 - A2) + (A4 - A3) + ... + (An - A(n-1))] : [A1 + A2 + A3 + ... + A(n-1)].

**Step 8.** But (A2 - A1) + (A3 - A2) + (A4 - A3) + ... + (An - A(n-1)) = An - A1, since this is a telescoping sum: each intermediate term cancels with its negative counterpart, leaving only An - A1 [by repeated application of CN2 and CN3].

**Step 9.** Therefore, substituting into the result of Step 7, (A2 - A1):A1 = (An - A1):(A1 + A2 + ... + A(n-1)).

**Step 10.** That is, as the excess of the second over the first is to the first, so is the excess of the last over the first to the sum of all those numbers before the last. This is what was to be proved. Q.E.D.

**USED:** 5.17, 7.12, CN2, CN3, D5.8, D7.20
**Human refs (from References field):** 7.11, 7.12, 7.13
**Jaccard:** 0.125 — AI adds ['5.17', 'CN2', 'CN3', 'D5.8', 'D7.20']; Human adds ['7.11', '7.13']

## Proposition 9.36
**Statement:** If as many numbers as we please beginning from an unit be set out continuously in double proportion, until the sum of all becomes prime, and if the sum multiplied into the last make some number, the product will be perfect.

**Step 1.** Let as many numbers as we please, A_0 = 1, A_1, A_2, ..., A_n, be set out beginning from a unit in continued double proportion. Let S = A_0 + A_1 + A_2 + ... + A_n be prime. Let P = S * A_n. We must show that P is perfect, i.e., that P equals the sum of its own parts [D7.22].

**Step 2.** Since A_0, A_1, ..., A_n are in continued double proportion from unity, each term is double the preceding one [by construction]. By 9.35 (on the geometric series with ratio 2), the excess of A_{n+1} over A_0 (which is the next double after A_n, minus the unit) equals twice the sum A_0 + A_1 + ... + A_n minus A_0. More precisely, since 1, A_1, A_2, ..., A_n, A_{n+1} would continue the proportion with A_{n+1} = 2*A_n, by 9.35 we have (A_{n+1} - 1) : 1 = (A_{n+1} - A_0) : A_0 relates to the sum of all terms before it. In fact, the sum S = A_0 + A_1 + ... + A_n = A_{n+1} - 1 = 2*A_n - 1. Thus S = 2*A_n - 1, and so S + 1 = 2*A_n, giving S*A_n = A_n*(2*A_n - 1).

**Step 3.** Now consider what numbers measure P = S * A_n. Since S is prime [by hypothesis], S is measured only by the unit and by S itself [D7.11]. The factors of A_n are determined as follows: since A_0, A_1, ..., A_n are in continued double proportion from unity and A_1 = 2 is prime, by 9.13, A_n is not measured by any number except those which have a place among the proportional numbers A_0, A_1, ..., A_n.

**Step 4.** We identify all proper divisors of P = S * A_n. The divisors of A_n, by 9.13, are exactly A_0 = 1, A_1, A_2, ..., A_n (since A_1 = 2 is prime). Each A_k measures A_n, and by 9.11, A_k measures A_n according to A_{n-k}, that is, A_n = A_k * A_{n-k} [where A_0 = 1].

**Step 5.** Since S is prime, the divisors of P = S * A_n are of two kinds: (i) the divisors of A_n itself, namely A_0, A_1, ..., A_n; and (ii) S times each divisor of A_n, namely S*A_0, S*A_1, ..., S*A_{n-1}, and S*A_n = P itself. By 7.30, since S is prime and A_k (for each k from 0 to n) is not measured by S (because the A_k are all powers of 2 and S is an odd prime, so S and A_k are prime to one another by 7.29 since S is odd and the A_k are powers of 2), S*A_k is the least number measured by both S and A_k. This ensures there are no additional divisors beyond those listed.

**Step 6.** The proper parts of P are therefore: A_0, A_1, A_2, ..., A_n (the divisors of A_n), and S*A_0, S*A_1, ..., S*A_{n-1} (the divisors involving S, excluding P = S*A_n itself). Each of these measures P: the A_k measure A_n which measures P, and S*A_k measures S*A_n = P since A_k measures A_n [D7.3, 7.15, 7.16].

**Step 7.** We now compute the sum of all proper parts. The sum of the first group is A_0 + A_1 + ... + A_n = S. The sum of the second group is S*A_0 + S*A_1 + ... + S*A_{n-1} = S*(A_0 + A_1 + ... + A_{n-1}) [by 7.18, since S multiplied by each and then summed equals S multiplied by the sum].

**Step 8.** Now A_0 + A_1 + ... + A_{n-1} is the sum of the geometric series from 1 up to A_{n-1}. By the same reasoning as Step 2 (applying 9.35), this sum equals 2*A_{n-1} - 1 = A_n - 1. Therefore the second group sums to S*(A_n - 1).

**Step 9.** The total sum of all proper parts is S + S*(A_n - 1) = S + S*A_n - S = S*A_n = P [by CN2, CN3]. Therefore P equals the sum of its own parts, so P is perfect [D7.22].

**Step 10.** Therefore, if as many numbers as we please beginning from a unit be set out continuously in double proportion, until the sum of all becomes prime, and if the sum multiplied into the last make some number, the product will be perfect. Q.E.D.

**USED:** 7.15, 7.16, 7.18, 7.29, 7.30, 9.11, 9.13, 9.35, CN2, CN3, D7.11, D7.15, D7.22, D7.3
**Human refs (from References field):** 7.14, 7.19, 7.20, 7.21, 7.29, 9.13, 9.35, D7.20, D7.22
**Jaccard:** 0.211 — AI adds ['7.15', '7.16', '7.18', '7.30', '9.11', 'CN2', 'CN3', 'D7.11', 'D7.15', 'D7.3']; Human adds ['7.14', '7.19', '7.20', '7.21', 'D7.20']
