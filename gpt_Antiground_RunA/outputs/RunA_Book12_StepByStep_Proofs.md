# Book 12 of Euclid's Elements — Step-by-Step AI Proofs (Run A)

## Proposition 12.1
**Statement:** Similar polygons inscribed in circles are to one another as the squares on the diameters.

**Step 1.** Let P and Q be similar polygons inscribed in two circles, with A, B, C three consecutive vertices of P and a, b, c the corresponding vertices of Q. These vertices lie on their respective circumferences (D4.3). We will show that corresponding polygonal sides are proportional to the diameters, then apply 6.22 directly, rather than decompose the polygonal areas.

**Step 2.** Join AC and ac (P1). Similarity of the polygons gives AB:ab = BC:bc and ∠ABC = ∠abc (D6.1). Therefore triangles ABC and abc are equiangular by 6.6, which applies directly to these proportional adjacent sides and their equal included angles.

**Step 3.** At least one of ∠BAC and ∠ACB is acute, since together they are less than two right angles (1.17). Reverse the labels A, C and simultaneously a, c if necessary, so that ∠ACB is acute. Its corresponding angle ∠acb is equal to it and hence also acute. This choice avoids supplementary-angle cases in the circle-angle comparison below.

**Step 4.** Find the centres of the circles (3.1), and draw through A and a the diameters AX and ax; join BX and bx (P1, P2, D1.17). Neither AB nor ab is a diameter, since its angle at C or c is acute, whereas an angle in a semicircle is right (3.31). Thus X differs from B, and x differs from b, so triangles ABX and abx are nondegenerate.

**Step 5.** Since AX and ax are diameters, ∠ABX and ∠abx are right angles (3.31), and therefore equal (P4). The remaining angles ∠AXB and ∠axb are acute (1.17). Consequently C and X lie in the same, greater segment on chord AB: an angle in the lesser segment would be greater than a right angle (3.31). Likewise c and x lie in the same, greater segment on chord ab.

**Step 6.** Angles in the same segment are equal, so ∠AXB = ∠ACB and ∠axb = ∠acb (3.21; either equality is immediate if its two vertices coincide). Together with Step 2, these yield ∠AXB = ∠axb (CN1). The triangles ABX and abx thus have two corresponding angles equal; their remaining angles are equal by 1.32. Their corresponding sides are therefore proportional (6.4), giving AB:ab = AX:ax.

**Step 7.** Construct squares S and T on AX and ax respectively (1.46). These squares are similar, since their angles are right and their corresponding sides proportional (D1.22, P4, D6.1). The four-line proportion from Step 6 is precisely the hypothesis of 6.22: the similar polygons P and Q are described on corresponding sides AB and ab, and the similar squares S and T on AX and ax. Hence P:Q = S:T (6.22). Therefore similar polygons inscribed in circles are to one another as the squares on the diameters.

**USED:** 1.17, 1.32, 1.46, 3.1, 3.21, 3.31, 6.22, 6.4, 6.6, CN1, D1.17, D1.22, D4.3, D6.1, P1, P2, P4
**Human refs (from References field):** 1.32, 3.27, 3.31, 6.20, 6.4, 6.6, D6.1
**Jaccard:** 0.263 — AI adds ['1.17', '1.46', '3.1', '3.21', '6.22', 'CN1', 'D1.17', 'D1.22', 'D4.3', 'P1', 'P2', 'P4']; Human adds ['3.27', '6.20']

## Proposition 12.2
**Statement:** Circles are to one another as the squares on the diameters.

**Step 1.** Let C and D denote the two circular areas, and let S and T denote the squares on their respective diameters. We use exhaustion by inscribed polygons: 12.1 is the natural comparison theorem because it already gives the required diameter-square ratio, while 10.1 will make the polygonal remainders arbitrarily small. We shall establish the final proportion directly by the equimultiple definition D5.5.

**Step 2.** Inscribe a square in each circle using perpendicular diameters (4.6). In each circle bisect every angle at the centre between consecutive vertices (1.9), produce the bisectors to the circumference (P2), and join consecutive circumference points (P1). Repeat this construction, performing the same number of refinements in both circles. Write P_j and Q_j for the resulting polygonal areas after j refinements, with P_0 and Q_0 the original squares. Their sides, and consequently their polygonal regions, lie within their respective circles (3.2).

**Step 3.** The corresponding central angles initially are right angles and therefore equal; they remain equal under corresponding bisections (4.6, P4, 1.9). Each pair of corresponding radial triangles has equal included angles and proportional bounding radii, since all radii within either circle are equal (D1.15). These triangles are equiangular by 6.6, and their corresponding sides are proportional by 6.4. Thus corresponding polygon sides all have the same ratio, namely that of the radii, and corresponding polygon angles are equal because they are sums of corresponding equal triangle angles (CN2). The polygons are therefore similar (D6.1). Consequently, at every stage,
P_j : Q_j = S : T. (12.1)

**Step 4.** Consider any side AB of one of these polygons, let O be the centre, and let M be the new vertex introduced on the minor arc AB by bisecting angle AOB. Let H be the intersection of OM with AB. Since OA = OB and OM bisects angle AOB, triangles OAH and OBH are congruent (D1.15, 1.4). Hence their adjacent angles at H are equal, so OM is perpendicular to AB (D1.10).

Through M draw a line parallel to AB, and through A and B draw lines parallel to OM. These lines, together with AB, form a rectangle R (1.31, 1.29). Its side through M is perpendicular to OM and therefore lies outside the circle except at M (3.16).

**Step 5.** Let G be the minor circular segment bounded by AB and the minor arc AB. For any interior point X of this arc, angle AXB is greater than a right angle (3.31). The other two angles of triangle AXB are therefore acute (1.17), so X lies between the perpendiculars to AB through A and B. Together with the supporting line through M from Step 4, this shows that G is a proper part of R. Thus G < R (3.16, CN5).

The rectangle R is twice triangle AMB, since they have the same base AB and lie between the same parallels (1.41). Therefore triangle AMB is greater than half of G. Removing this triangle leaves the two new circular segments, whose combined area is less than half of G (CN3).

**Step 6.** Apply Step 5 to every side of a polygon and add the comparisons. Each refinement removes more than half of the total area remaining between the polygon and its circle (CN2, CN3). Thus each of the sequences of remainders C − P_j and D − Q_j loses more than half its magnitude at every refinement. Any fixed positive integral multiple of these remainders has the same property (CN2).

It follows from 10.1 that, for every prescribed positive area E and every positive integer h, some stage satisfies
h(C − P_j) < E.
The corresponding assertion holds for D − Q_j as well.

**Step 7.** Let m and n be arbitrary positive integers. Suppose first that mC > nD. Apply Step 6 with E = mC − nD and h = m. We obtain a stage for which
m(C − P_j) < mC − nD,
and hence
mP_j > nD > nQ_j. (CN2, CN3, CN5)
But P_j : Q_j = S : T by Step 3. Therefore the equimultiple definition gives mS > nT (D5.5). Interchanging the two circles proves likewise that
mC < nD implies mS < nT.

**Step 8.** Now suppose mC = nD. If mS > nT, put Δ = mS − nT. By the Archimedean condition in D5.4, choose a positive integer k such that kΔ > T. Adding the corresponding multiples gives
(km)S > (kn + 1)T. (CN2, CN3)
On the other hand,
(km)C = (kn)D < (kn + 1)D. (CN2, CN5)
The strict comparison established in Step 7 would therefore give
(km)S < (kn + 1)T,
a contradiction. The possibility mS < nT is excluded by the same argument with the two circles interchanged. Consequently mC = nD implies mS = nT.

**Step 9.** For every pair of positive integers m and n, the multiples mC and nD alike exceed, equal, or fall short of one another exactly as mS and nT do, by Steps 7–8. Therefore, by D5.5,
C : D = S : T.
Thus circles are to one another as the squares on their diameters.

**USED:** 1.17, 1.29, 1.31, 1.4, 1.41, 1.9, 10.1, 12.1, 3.16, 3.2, 3.31, 4.6, 6.4, 6.6, CN2, CN3, CN5, D1.10, D1.15, D5.4, D5.5, D6.1, P1, P2, P4
**Human refs (from References field):** 12.1, 5.11, 5.16
**Jaccard:** 0.037 — AI adds ['1.17', '1.29', '1.31', '1.4', '1.41', '1.9', '10.1', '3.16', '3.2', '3.31', '4.6', '6.4', '6.6', 'CN2', 'CN3', 'CN5', 'D1.10', 'D1.15', 'D5.4', 'D5.5', 'D6.1', 'P1', 'P2', 'P4']; Human adds ['5.11', '5.16']

## Proposition 12.3
**Statement:** Any pyramid which has a triangular base is divided into two pyramids equal and similar to one another, similar to the whole and having triangular bases, and into two equal prisms; and the two prisms are greater than the half of the whole pyramid.

**Step 1.** Let ABCD be the given pyramid, with vertex A and triangular base BCD. Bisect AB, AC, AD, BC, BD, CD at E, F, G, H, I, J respectively, and join the midpoints lying in each face. [1.10, P1] We use the midpoint dissection: equality of the two resulting prisms will follow by dividing them into corresponding equal pyramids, without introducing a formula for pyramidal volume.

**Step 2.** In each triangular face, the line joining two midpoints is parallel to the third side and equal to its half: parallelism follows from 6.2, and the length relation follows from the resulting equal angles and proportional sides. [6.2, 1.29, 6.4]
In particular, FH and GI are parallel to AB, while FG and HI are parallel to CD. Therefore FH is parallel to GI, and FG to HI. [11.9] The parallel lines FH and GI lie in one plane, so FGIH is a plane parallelogram. [D1.23]
Moreover, EF and EG are respectively parallel to BC and BD; hence plane EFG is parallel to plane BCD. Similarly, GI and GJ are respectively parallel to AB and AC, so plane GIJ is parallel to plane ABC. [11.15]

**Step 3.** Consider the four corner pyramids
K_A = AEFG, K_B = BEHI, K_C = CFHJ, and K_D = DGIJ. [D11.12]
The respective correspondences from the vertices (A, B, C, D) of the whole pyramid are
(A, E, F, G), (E, B, H, I), (F, H, C, J), and (G, I, J, D).
Under each correspondence, every edge is half the corresponding edge of ABCD, by Step 2 and the original bisections. Thus every corresponding pair of triangular faces has proportional sides and is similar. [6.5, D6.1] Consequently each corner pyramid is similar to the whole. [D11.9]
Furthermore, corresponding faces of any two corner pyramids have their three sides respectively equal. Their corresponding angles are therefore equal, and the triangles themselves are equal. [1.8, 1.4] Hence the four corner pyramids are equal and similar to one another. [D11.10]

**Step 4.** Cut the original pyramid first by triangle EFG, cutting off K_A, and then by triangle GIJ, cutting off K_D. Cut the remaining solid by the parallelogram FGIH. The two further pieces are:
P, whose opposite triangular faces are EFG and BHI and whose other faces are EBHF, EBIG, and FGIH;
Q, whose opposite triangular faces are GIJ and FHC and whose other faces are FGIH, HIJC, and FGJC.
These cuts give four pieces with disjoint interiors, filling ABCD: K_A, K_D, P, and Q. The first two are triangular-based pyramids. [D11.12]
For P, the triangles EFG and BHI are equal and similar by Step 3 and lie in parallel planes by Step 2. Its three other faces are parallelograms by the midpoint parallelisms. The same is true of Q: GIJ and FHC are equal and similar, their planes are parallel, and its other faces are parallelograms. Thus P and Q are prisms. [D11.13]

**Step 5.** To compare the prisms, cut P by triangle EHI. This separates it into K_B and the quadrangular pyramid U with vertex E and base FGIH. Likewise, cutting Q by triangle FHJ separates it into K_C and the quadrangular pyramid V with vertex J and the same base FGIH. [D11.12] Thus, with addition denoting the joining of these non-overlapping solid pieces,
P = K_B + U and Q = K_C + V.

**Step 6.** Compare U and V under the vertex correspondence
(E, F, G, I, H) ↦ (J, I, H, F, G).
Their common base FGIH corresponds to itself with opposite vertices paired. Opposite sides and angles of a parallelogram are equal, so this correspondence makes the bases similar; the bases are also equal, being the same figure. [1.34, D6.1, CN4]
Their triangular faces correspond as follows:
EFG ↔ JIH,
EGI ↔ JHF,
EIH ↔ JFG,
EHF ↔ JGI.
In each pair, corresponding sides are equal, since they are halves of the same respective edges of ABCD, as established in Step 2. The corresponding angles and triangles are therefore equal. [1.8, 1.4] Hence U and V are equal and similar solid figures. [D11.10]
Since K_B = K_C by Step 3 and U = V, adding equals to equals in the decompositions of Step 5 gives P = Q. [CN2]

**Step 7.** Let R denote K_A + K_D and S denote P + Q. The equality of the corner pyramids and the decompositions in Step 5 give
S = R + U + V. [CN2]
Both U and V are genuine solid pieces, so R is a proper part of this sum. Hence S > R. [CN5] But the whole pyramid is R + S by Step 4. Therefore 2S > R + S, and S is greater than half the whole pyramid. [CN2, CN5]
Thus ABCD has been divided into two equal and similar triangular-based pyramids K_A and K_D, each similar to ABCD, and into two equal prisms P and Q; and the two prisms together are greater than half of ABCD, as required.

**USED:** 1.10, 1.29, 1.34, 1.4, 1.8, 11.15, 11.9, 6.2, 6.4, 6.5, CN2, CN4, CN5, D1.23, D11.10, D11.12, D11.13, D11.9, D6.1, P1
**Human refs (from References field):** 1.29, 1.34, 1.4, 11.10, 11.39, 6.2, D11.10, D6.1
**Jaccard:** 0.273 — AI adds ['1.10', '1.8', '11.15', '11.9', '6.4', '6.5', 'CN2', 'CN4', 'CN5', 'D1.23', 'D11.12', 'D11.13', 'D11.9', 'P1']; Human adds ['11.10', '11.39']

## Proposition 12.4
**Statement:** If there be two pyramids of the same height which have triangular bases, and cach of them be divided into two pyramids equal to one another and similar to the whole, and into two equal prisms, then, as the base of the one pyramid is to the base of the other pyramid, so will all the prisms in the one pyramid be to all the prisms, being equal in multitude, in the other pyramid.

**Step 1.** Let VABC and V′A′B′C′ be the two pyramids, with triangular bases ABC and A′B′C′ and the same height h. Apply the division of 12.3 to each, repeating that division on the remaining pyramids when further prisms are required. Write [XYZ] for the area of a triangle, and use a solid’s name also for its magnitude. We shall compare the prisms through parallelepipeds, rather than assume any proportionality theorem for pyramids. [12.3]

**Step 2.** In the midpoint division of VABC, let D, E, F be the midpoints of VA, VB, VC, and K, L, M the midpoints of AB, BC, CA. The remaining pyramids are DAKM and VDEF. One prism, P, has triangular bases BKL and EDF; its equal companion, Q, has triangular bases KMD and LCF. Thus P = Q. Use corresponding primed letters in the other pyramid, so that P′ = Q′. The midpoint joins are parallel to the corresponding edges, and consequently the plane DEF is parallel to ABC. [12.3, 6.2, 11.15]

**Step 3.** The prism P and both remaining pyramids have height h/2. To verify this explicitly, draw the perpendicular VH to the base plane, choosing the label A so that A ≠ H, and let X be its intersection with the plane DEF. In the plane VAH, the intersections DX and AH with the parallel planes are parallel. Since VD = DA, it follows that VX = XH = h/2. Moreover, VH is perpendicular to DEF: plane sections through VH give parallel intersection lines in the two planes, so its right angles transfer to two intersecting lines through X, and the perpendicular-to-a-plane criterion applies. Finally, perpendiculars between the two parallel planes are parallel and form opposite sides of a parallelogram in their common plane; hence their lengths are equal. Thus the separation of ABC and DEF is XH, while the altitude of VDEF is VX. The same reasoning applies to the primed pyramid. [11.11, 11.16, 6.2, 1.29, 11.4, 11.6, 1.34, D6.4]

**Step 4.** Each of the triangles BKL, AKM, and DEF is similar to ABC, with corresponding sides half as great. Each therefore has one quarter of its area. The corresponding statements hold in the primed figure. Since taking equal multiples preserves a ratio, we obtain
[BKL] : [B′K′L′] = [ABC] : [A′B′C′].
Likewise, each pair of corresponding remaining pyramids has bases in the ratio [ABC] : [A′B′C′]. [6.2, 6.4, 6.19, D5.9, 5.15]

**Step 5.** Complete the triangular base BKL of P to a parallelogram, and make the corresponding completion at its opposite base EDF. This completes P to a parallelepiped S. Complete P′ similarly to S′. The parallelogram bases have areas 2[BKL] and 2[B′K′L′], respectively; and the diagonal plane dividing each completed parallelepiped gives S = 2P and S′ = 2P′. The completed solids retain the heights of P and P′, and so have equal height. [1.31, D11.13, 1.41, 11.28]

**Step 6.** Parallelepipeds of equal height are to one another as their bases. Hence
S : S′ = 2[BKL] : 2[B′K′L′].
Removing the equal multiples on both sides gives
P : P′ = [BKL] : [B′K′L′] = [ABC] : [A′B′C′].
This is the natural application of 11.32: the prisms have just been exhibited as halves of parallelepipeds, so no comparison of pyramid magnitudes is needed. [11.32, 5.15, 5.11]

**Step 7.** Since Q = P and Q′ = P′, the companion prisms also satisfy
Q : Q′ = [ABC] : [A′B′C′].
Further, the two prisms together are respective doubles of P and P′. Therefore
(P + Q) : (P′ + Q′) = [ABC] : [A′B′C′].
This proves the assertion for the first division. [12.3, 5.15, 5.11]

**Step 8.** Now divide corresponding remaining pyramids in the same manner. By Steps 3 and 4, each such pair has equal heights and bases in the original ratio [ABC] : [A′B′C′]. Consequently, the argument of Steps 5–7 applies to that pair and proves that its corresponding prisms have this same ratio. Its new remaining pyramids again have equal heights, while their bases are corresponding quarters of the preceding bases and therefore retain the same ratio. Repeating this argument establishes the required ratio for every corresponding pair of prisms produced through any finite number of successive divisions. [12.3, 5.15, 5.11; Steps 3–7]

**Step 9.** Let all the prisms obtained through equally many stages be R₁, …, Rₙ in the first pyramid and R′₁, …, R′ₙ in the second, paired according to the construction. Every ratio Rᵢ : R′ᵢ equals [ABC] : [A′B′C′]. When any number of magnitudes are proportional, one antecedent is to its consequent as all the antecedents are to all the consequents. Thus
[ABC] : [A′B′C′] = (R₁ + ⋯ + Rₙ) : (R′₁ + ⋯ + R′ₙ).
Therefore, as the base of the one pyramid is to the base of the other, so are all the prisms in the one to all the prisms, equal in multitude, in the other. [5.12, 5.11]

**USED:** 1.29, 1.31, 1.34, 1.41, 11.11, 11.15, 11.16, 11.28, 11.32, 11.4, 11.6, 12.3, 5.11, 5.12, 5.15, 6.19, 6.2, 6.4, D11.13, D5.9, D6.4
**Human refs (from References field):** 11.39, 12.3, 5.12, 5.16, 6.22
**Jaccard:** 0.083 — AI adds ['1.29', '1.31', '1.34', '1.41', '11.11', '11.15', '11.16', '11.28', '11.32', '11.4', '11.6', '5.11', '5.15', '6.19', '6.2', '6.4', 'D11.13', 'D5.9', 'D6.4']; Human adds ['11.39', '5.16', '6.22']

## Proposition 12.5
**Statement:** Pyramids which are of the same height and have triangular bases are to one another as the bases.

**Step 1.** Let X and Y be the solid magnitudes of the two pyramids, and let A and B be their respective triangular base areas. Their heights are equal. We use the prism-exhaustion route supplied by 12.3 and 12.4, with 10.1 controlling the remainders, and verify the definition of equal ratios directly. [12.3, 12.4, 10.1, D5.5]

**Step 2.** Subdivide both pyramids by 12.3, and repeatedly subdivide every remaining pyramid in the same manner, completing the same number of rounds in each original pyramid. After round k, let S_k and T_k be the respective sums of all prisms removed, and R_k and U_k the respective sums of the remaining pyramids. Thus
X = S_k + R_k,     Y = T_k + U_k.
Each round removes more than half of every remaining pyramid. Adding these removals shows that
R_(k+1) < R_k/2,     U_(k+1) < U_k/2.
Moreover, S_k and T_k strictly increase, while S_k < X and T_k < Y. [12.3, CN2, CN5]

**Step 3.** For any positive integer r and any positive solid magnitude ε, a sufficiently late round therefore satisfies
rR_k < ε,     rU_k < ε.
Indeed, the multiple remainders also lose more than half at each round. Apply 10.1 to each sequence and take a round at least as late as both rounds obtained; further subdivision only decreases the remainders. [CN2, 10.1]

**Step 4.** The corresponding finite prism collections are equal in multitude. Hence 12.4 gives, at every round,
S_k : T_k = A : B.
In particular, for k > 1,
S_k : T_k = S_1 : T_1. [12.4, 5.11]
Since the first prism sums are parts of the later sums, 5.19 applies directly to these proportional wholes and proportional parts. It gives
(S_k − S_1) : (T_k − T_1) = A : B. [5.19, 5.11]

**Step 5.** Let m and n be arbitrary positive integers. First suppose mA > nB. By Step 4 and D5.5,
d = mS_1 − nT_1 > 0,
and, whenever k > 1,
m(S_k − S_1) > n(T_k − T_1).
Consequently,
mS_k > nT_k + d. [D5.5, CN2, CN3]
Choose k > 1 so late that nU_k < d, as permitted by Step 3. Then
mX > mS_k > nT_k + d > nT_k + nU_k = nY.
Thus mA > nB implies mX > nY. Interchanging the two pyramids and the two integers proves likewise that mA < nB implies mX < nY. [Step 3, CN2, CN5]

**Step 6.** Now suppose mA = nB. By Step 4 and D5.5, mS_k = nT_k at every round. If mX > nY, choose a round with
mR_k < mX − nY,
using Step 3. Subtracting gives
mS_k = mX − mR_k > nY > nT_k,
contrary to mS_k = nT_k. If instead nY > mX, choose a round with nU_k < nY − mX. Then
nT_k = nY − nU_k > mX > mS_k,
which is the same contradiction. Therefore mX = nY. [D5.5, Step 3, CN2, CN3, CN5]

**Step 7.** For every pair of positive integers m and n, the multiples mX and nY therefore exceed, equal, or fall short of one another exactly as mA and nB do. By D5.5,
X : Y = A : B.
Hence pyramids of the same height having triangular bases are to one another as their bases. [D5.5]

**USED:** 10.1, 12.3, 12.4, 5.11, 5.19, CN2, CN3, CN5, D5.5
**Human refs (from References field):** 10.1, 12.2, 12.3, 12.4, 5.16, 5.2
**Jaccard:** 0.250 — AI adds ['5.11', '5.19', 'CN2', 'CN3', 'CN5', 'D5.5']; Human adds ['12.2', '5.16', '5.2']

## Proposition 12.6
**Statement:** Pyramids which are of the same height and have polygonal bases are to one another as the bases.

**Step 1.** Let P and Q be pyramids of the same height, with polygonal bases A and B. Draw nonintersecting diagonals dividing A into triangles A₁,…,Aₘ and B into triangles B₁,…,Bₙ (P1). Thus, as plane magnitudes, A = A₁ + ⋯ + Aₘ and B = B₁ + ⋯ + Bₙ. The numbers m and n need not be equal.

**Step 2.** Join the endpoints of each dividing diagonal to the corresponding pyramid’s apex (P1). Each triangle so formed lies in a plane (11.2). These planes divide P into triangular-based pyramids P₁,…,Pₘ with bases A₁,…,Aₘ, and Q into triangular-based pyramids Q₁,…,Qₙ with bases B₁,…,Bₙ (D11.12). Consequently P = P₁ + ⋯ + Pₘ and Q = Q₁ + ⋯ + Qₙ. Each piece has its original pyramid’s apex and base plane, hence its original height; therefore all these pieces have the same height (D6.4).

**Step 3.** Use the already established triangular-base theorem, 12.5; this is the direct reduction, requiring no new exhaustion argument. Fix Q₁ as a reference pyramid. For every i and j, 12.5 gives
Pᵢ : Q₁ = Aᵢ : B₁,
and
Qⱼ : Q₁ = Bⱼ : B₁.

**Step 4.** Apply 5.24 repeatedly to the first family of proportions. This is the appropriate addition rule because the corresponding consequents Q₁ and B₁ remain fixed. It yields
(P₁ + ⋯ + Pₘ) : Q₁ = (A₁ + ⋯ + Aₘ) : B₁,
so P : Q₁ = A : B₁. Applying 5.24 in exactly the same way to the second family yields
(Q₁ + ⋯ + Qₙ) : Q₁ = (B₁ + ⋯ + Bₙ) : B₁,
so Q : Q₁ = B : B₁. If either family has only one member, its displayed proportion already holds without addition.

**Step 5.** Inverting the latter proportion gives Q₁ : Q = B₁ : B: inversion preserves equality of ratios because it reverses the corresponding comparisons of equimultiples in D5.5. Combining this with P : Q₁ = A : B₁, ex aequali by 5.22 gives
P : Q = A : B.
Therefore pyramids of the same height with polygonal bases are to one another as their bases.

**USED:** 11.2, 12.5, 5.22, 5.24, D11.12, D5.5, D6.4, P1
**Human refs (from References field):** 12.5, 5.18, 5.22
**Jaccard:** 0.222 — AI adds ['11.2', '5.24', 'D11.12', 'D5.5', 'D6.4', 'P1']; Human adds ['5.18']

## Proposition 12.7
**Statement:** Any prism which has a triangular base is divided into three pyramids equal to one another which have triangular bases.

**Step 1.** Let the prism have opposite triangular bases ABC and DEF, with corresponding vertices A,D; B,E; and C,F. Its remaining faces are the parallelograms ABED, BCFE, and CADF. [D11.13]

**Step 2.** Join AF, BF, and AE, and cut the prism by the plane ABF. This separates the triangular-based pyramid F–ABC from the quadrilateral-based pyramid F–ABED, whose lateral faces are FAB, FBE, FED, and FDA. Cut the latter pyramid by the plane AEF: its base ABED is divided along AE, giving the two triangular-based pyramids F–ABE and F–ADE. Thus the original prism is partitioned, without overlapping interiors, into F–ABC, F–ABE, and F–ADE. [P1, 11.2, D11.12, D11.13]

**Step 3.** Path choice: compare these pyramids by changing which triangular face is regarded as the base, and apply the triangular-base theorem 12.5 directly; its polygonal-base extension is unnecessary. In the parallelogram BCFE, the diagonal BF divides the face into equal triangles BCF and BEF. [1.34] Regard F–ABC and F–ABE as pyramids A–BCF and A–BEF, respectively. They have the same height, since they have the same vertex A and their bases lie in the same plane. [D6.4] Therefore, by 12.5, their ratio is the ratio of the equal triangles BCF and BEF, and hence they are equal: F–ABC = F–ABE. Here equality follows directly by taking unit equimultiples in the definition of equal ratios. [12.5, D5.5]

**Step 4.** In the parallelogram ABED, the diagonal AE divides the face into equal triangles ABE and ADE. [1.34] The pyramids F–ABE and F–ADE have the same vertex F and coplanar bases, so they have the same height. [D6.4] Their ratio is therefore the ratio of their equal bases, giving F–ABE = F–ADE. [12.5, D5.5]

**Step 5.** Consequently all three pyramids F–ABC, F–ABE, and F–ADE are equal to one another. [CN1] By the partition in Step 2, they together constitute the given prism, and each has a triangular base. Thus any prism with a triangular base is divided into three equal pyramids having triangular bases. [D11.12]

**USED:** 1.34, 11.2, 12.5, CN1, D11.12, D11.13, D5.5, D6.4, P1
**Human refs (from References field):** 1.34, 12.5
**Jaccard:** 0.222 — AI adds ['11.2', 'CN1', 'D11.12', 'D11.13', 'D5.5', 'D6.4', 'P1']

## Proposition 12.8
**Statement:** Similar pyramids which have triangular bases are in the triplicate ratio of their corresponding sides.

**Step 1.** Let P = ABCD and P′ = A′B′C′D′ be similar pyramids with triangular bases ABC and A′B′C′, the vertices corresponding in the indicated order. Their corresponding triangular faces are similar. Consequently, all corresponding edges have the same ratio; in particular,
AB:A′B′ = AC:A′C′ = AD:A′D′,
and the three angles between AB, AC, AD respectively equal those between A′B′, A′C′, A′D′. [D11.9, D6.1]

**Step 2.** Complete a parallelepiped S on the three edges AB, AC, AD. Label its base ABEC and its opposite face DFHG, so that AD, BF, EH, CG are equal and parallel. Complete S′ correspondingly. These constructions use parallels in the face planes; opposite face planes are parallel because their intersecting sides are respectively parallel. [1.31, 1.34, 11.15] The direct path is to compare each pyramid with its completion using the triangular-prism dissection of 12.7, and then apply the triplicate-ratio theorem 11.33.

**Step 3.** The parallelepipeds S and S′ are similar. Indeed, every face has sides equal to two of the three generating edges, by the equality of opposite sides of parallelograms. Thus corresponding face sides are proportional by Step 1. Their corresponding angles are also equal: angles between parallel pairs of lines are equal, and the adjacent angles of parallelograms are supplementary. Hence all six pairs of corresponding faces are similar. [1.34, 11.10, 1.29, D6.1, D11.9]

**Step 4.** Cut S by the plane through BC and FG, which are diagonals of its opposite faces ABEC and DFHG. This plane bisects S. One half is the triangular prism R with opposite triangular bases ABC and DFG. Likewise, the corresponding cut bisects S′ and gives the prism R′ with bases A′B′C′ and D′F′G′. Therefore S = 2R and S′ = 2R′. [11.28, D11.13]

**Step 5.** Apply the triangular-prism dissection of 12.7 to R, taking the cutting planes BCD and CDF. Its three equal pyramids are ABCD, BCFD, and CDFG; the first is P. Thus R = 3P. The corresponding dissection gives R′ = 3P′. Consequently,
S = 6P and S′ = 6P′. [12.7, CN2]

**Step 6.** Equimultiples have the same ratio as the original magnitudes, so
P:P′ = S:S′. [5.15]
Since S and S′ are similar parallelepipeds, S:S′ is the triplicate ratio of AB:A′B′. [11.33] Therefore P:P′ is likewise the triplicate ratio of AB:A′B′. [5.11] By Step 1 this is the ratio of any pair of corresponding edges. Hence similar pyramids with triangular bases are in the triplicate ratio of their corresponding sides.

**USED:** 1.29, 1.31, 1.34, 11.10, 11.15, 11.28, 11.33, 12.7, 5.11, 5.15, CN2, D11.13, D11.9, D6.1
**Human refs (from References field):** 11.24, 11.28, 11.33, 12.7
**Jaccard:** 0.200 — AI adds ['1.29', '1.31', '1.34', '11.10', '11.15', '5.11', '5.15', 'CN2', 'D11.13', 'D11.9', 'D6.1']; Human adds ['11.24']

## Proposition 12.9
**Statement:** In equal pyramids which have triangular bases the bases are reciprocally proportional to the heights; and those pyramids in which the bases are reciprocally proportional to the heights are equal.

**Step 1.** Let the given triangular pyramids be P = SABC and Q = TDEF. Denote their base areas by b and c, and their perpendicular heights by h and k, respectively [D11.12, D6.4]. We shall pass to parallelepipeds and apply 11.34, which already supplies both directions of the reciprocal-base-and-height criterion.

**Step 2.** Complete the three edges AB, AC, AS issuing from A into a parallelepiped K, and similarly complete DE, DF, DT into a parallelepiped L, drawing the required parallels [1.31, 11.15]. Let their base parallelograms have areas U and V. The diagonals BC and EF bisect these parallelograms, so
U = 2b and V = 2c [1.34].
The opposite base planes pass through S and T, respectively; hence K and L have heights h and k [D6.4].

**Step 3.** Cut each parallelepiped by the plane through its base diagonal and the corresponding diagonal of its opposite face. Each is thereby divided into two equal triangular prisms [11.28]. Consider the resulting prisms on ABC and DEF. Apply the division of 12.7, taking the lower triangular face as the base of one of the three equal pyramids and a vertex of the opposite face as its apex. This member has the same triangular base and height as P or Q, respectively. It therefore equals P or Q: by 12.5 their ratio is the ratio of their equal bases, and equality follows from D5.5 by taking both multiples once. The triangular-base theorem is sufficient here; no polygonal generalization is needed. Consequently the two prisms equal 3P and 3Q, and thus
K = 6P and L = 6Q [12.7, CN2].

**Step 4.** Parts have the same ratio as their equimultiples. Applying this to the doubles of the bases and to the sixfold multiples of the pyramids gives
U : V = b : c and K : L = P : Q [5.15].

**Step 5.** Suppose first that P = Q. Their sixfold multiples are equal, so K = L [Step 3, CN2]. Equal parallelepipedal solids have bases reciprocally proportional to their heights; therefore
U : V = k : h [11.34].
Combining this with Step 4 yields
b : c = k : h [5.11].
Thus equal triangular pyramids have bases reciprocally proportional to their heights.

**Step 6.** Conversely, suppose that b : c = k : h. By Step 4,
U : V = k : h [5.11].
The converse in 11.34 therefore gives K = L. But K : L = P : Q by Step 4. Taking both multiples once in the definition of equal ratios, the equality K = L implies P = Q [D5.5]. Hence triangular pyramids whose bases are reciprocally proportional to their heights are equal. Both assertions are proved.

**USED:** 1.31, 1.34, 11.15, 11.28, 11.34, 12.5, 12.7, 5.11, 5.15, CN2, D11.12, D5.5, D6.4
**Human refs (from References field):** 1.34, 11.34, 5.11
**Jaccard:** 0.231 — AI adds ['1.31', '11.15', '11.28', '12.5', '12.7', '5.15', 'CN2', 'D11.12', 'D5.5', 'D6.4']

## Proposition 12.10
**Statement:** Any cone is a third part of the cylinder which has the same base with it and equal height.

**Step 1.** Let K be the cone, with vertex S and circular base Ω, whose centre is O. Let C be the cylinder with base Ω and height SO. By coincidence, place the cylinder on the same side of the base as the cone, so that its upper base lies in the plane through S parallel to Ω. We use the same letters for the magnitudes of these solids, and write 3X for three equal copies of a magnitude X. (D11.18, D11.20, D11.21, D11.23; CN4; D5.2.)

**Step 2.** For a convex polygon F in the base plane, denote by W(F) the pyramid with base F and vertex S, and by J(F) the prism with base F and the cylinder’s height. Then
J(F) = 3W(F).
Indeed, triangulate F. The dissection in 12.7 divides each triangular prism into three equal pyramids, one having the prism’s lower triangular base and its full height. By 12.5, that pyramid equals the pyramid with the same triangular base and vertex S. Adding over the triangles proves the displayed equality. (D11.12, D11.13; P1; 12.7; 12.5; D5.5; CN2.)
Path choice: we shall combine this previously proved prism dissection with two-sided polyhedral exhaustion. The triangular-base comparison 12.5 is the natural choice because the dissection already supplies triangular pieces.

**Step 3.** Inscribe a square G₀ in Ω, and draw the tangents at its vertices, forming a circumscribed polygon H₀. Repeatedly refine these polygons by the construction in Step 4, obtaining inscribed polygons Gₙ and their corresponding tangent polygons Hₙ. Chords lie inside the circle, while tangents do not cut it; hence
Gₙ ⊂ Ω ⊂ Hₙ.
The region between Hₙ and Gₙ consists of triangles ATB with disjoint interiors: A and B are consecutive vertices of Gₙ, and T is the intersection of their tangents. Every intervening minor arc is at most a quadrant, initially by the square construction and subsequently by subdivision. (4.6; 3.17; 3.2; D3.2.)

**Step 4.** Consider one such triangle ATB. The radii OA and OB are equal, and they are perpendicular to the tangents. Applying 1.47 to the right triangles OAT and OBT gives TA = TB. Thus triangles OAT and OBT are congruent by 1.8, and OT bisects the minor angle AOB. Let M be the intersection of OT with the minor arc AB. Draw the tangent at M, meeting AT at U and BT at V. This tangent cuts off the corner T: U lies between A and T, and V between B and T. Inserting M into the inscribed polygon replaces the old gap triangle ATB by the two gap triangles AUM and BVM. (D1.15; 3.18; 1.47; CN3; 1.8; P1; 3.17.)
The tangent segments UA and UM are equal, by applying 1.47 to the right triangles OAU and OMU. But triangle TMU is right-angled at M, so UT > UM. Consequently AU < UT; similarly BV < VT. (3.18; 1.47; CN3; CN5.)

**Step 5.** Write W(ABC) for the pyramid with vertex S and triangular base ABC. Triangles AUM and UTM have bases AU and UT on the same line and the same altitude. Since AU < UT, their areas satisfy AUM < UTM by 6.1. Their pyramids have equal height, so 12.5 gives
W(AUM) < W(UTM).
Since these two pyramids together constitute W(ATM), it follows that
2W(AUM) < W(ATM).
Similarly,
2W(BVM) < W(BTM).
Here the passage from equal ratios to the corresponding inequalities follows directly from D5.5. (6.1; 12.5; D5.5; CN2.)
Moreover, M lies inside triangle ATB, so W(ATM) and W(BTM) together are less than W(ATB), the remaining piece being W(ABM). Therefore
2[W(AUM) + W(BVM)] < W(ATB). (CN2; CN5.)

**Step 6.** Perform this refinement at every side of Gₙ. Define the positive solid magnitudes
Eₙ = W(Hₙ) − W(Gₙ),
Dₙ = J(Hₙ) − J(Gₙ).
The first difference is the sum of the pyramids over the old gap triangles ATB. After refinement it is the sum of the pyramids over their replacement triangles AUM and BVM. Summing Step 5 therefore gives
2Eₙ₊₁ < Eₙ.
By Step 2 and subtraction, Dₙ = 3Eₙ; consequently
2Dₙ₊₁ < Dₙ. (CN2; CN3.)

**Step 7.** Thus, in passing from Dₙ to Dₙ₊₁, more than half the preceding magnitude is removed. Proposition 10.1 therefore ensures that, for any assigned positive solid magnitude ε, a finite refinement can be chosen for which
Dₙ < ε.
This is exhaustion of the polyhedral solid gaps themselves. (10.1.)

**Step 8.** Joining the points of the base polygons to S, their containment relations give
W(Gₙ) < K < W(Hₙ).
Likewise, erecting their prisms through the cylinder’s height gives
J(Gₙ) < C < J(Hₙ).
These are containments of solids, so the inequalities follow from the whole being greater than its proper part. By Step 2, the first pair of inequalities also gives
J(Gₙ) < 3K < J(Hₙ).
Thus C and 3K lie strictly between the same lower and upper polyhedral bounds. (D11.12, D11.13, D11.18, D11.21; CN5; CN2.)

**Step 9.** If C and 3K were unequal, let ε be their positive difference. Choose n by Step 7 so that Dₙ < ε. But Step 8 places the larger of C and 3K below J(Hₙ), and the smaller above J(Gₙ). Their difference must therefore be less than
J(Hₙ) − J(Gₙ) = Dₙ,
contradicting Dₙ < ε. (CN3; CN5; 10.1.)
Hence C = 3K. Therefore any cone is a third part of the cylinder having the same base and equal height. (D5.1; D5.2.)

**USED:** 1.47, 1.8, 10.1, 12.5, 12.7, 3.17, 3.18, 3.2, 4.6, 6.1, CN2, CN3, CN4, CN5, D1.15, D11.12, D11.13, D11.18, D11.20, D11.21, D11.23, D3.2, D5.1, D5.2, D5.5, P1
**Human refs (from References field):** 10.1, 11.32, 12.2, 12.7, 4.6, 4.7
**Jaccard:** 0.103 — AI adds ['1.47', '1.8', '12.5', '3.17', '3.18', '3.2', '6.1', 'CN2', 'CN3', 'CN4', 'CN5', 'D1.15', 'D11.12', 'D11.13', 'D11.18', 'D11.20', 'D11.21', 'D11.23', 'D3.2', 'D5.1', 'D5.2', 'D5.5', 'P1']; Human adds ['11.32', '12.2', '4.7']

## Proposition 12.11
**Statement:** Cones and cylinders which are of the same height are to one another as their bases.

**Step 1.** Let C and D be cones of the same height, with circular bases A and B, respectively; the same letters will denote their magnitudes (D11.18, D11.20). We first prove C:D = A:B by exhausting the cones with inscribed pyramids. The direct polygonal-pyramid theorem 12.6 avoids a separate triangulation argument; afterward, 12.10 will transfer the result to cylinders.

**Step 2.** Inscribe a square in each base, and repeatedly bisect every intervening arc, joining consecutive division points (4.6, 3.30, P1). Denote the resulting polygons at stage j by p_j and q_j. They are regular polygons with the same number of sides. Their corresponding central triangles are equiangular and therefore have proportional sides (6.4); their polygonal angles are also equal. Thus p_j and q_j are similar (D6.1).
Join their vertices to the respective cone vertices, forming pyramids X_j and Y_j (P1, D11.12). These pyramids lie inside their cones, increase at every stage, and have the same height as the cones (D11.18).

**Step 3.** By 12.1, p_j:q_j is the ratio of the squares on the diameters of A and B. By 12.2, A:B is that same ratio. Consequently p_j:q_j = A:B (5.11). Since X_j and Y_j have equal heights, 12.6 gives X_j:Y_j = p_j:q_j. Hence, at every stage,
X_j:Y_j = A:B (5.11).

**Step 4.** We establish that these pyramids exhaust their cones. Consider any circular segment remaining outside one of the inscribed polygons. Let its chord be UV and its arc midpoint be M. All such arcs are at most a quadrant. The perpendicular-bisector construction of 3.30 places M on the diameter perpendicular to UV (3.3). The tangent at M is therefore parallel to UV (3.16, 1.28).
Form the rectangle with base UV, opposite side on this tangent, and lateral sides perpendicular to UV. It contains the circular segment: the tangent bounds the circle on that side (3.16), while any point beyond either lateral side and on the segment's side of UV has distance from the centre greater than a radius, by 1.47. The triangle UMV has the same base and lies between the same parallels as the rectangle, so its area is half the rectangle's area (1.41).

**Step 5.** Let W be the portion of the cone obtained by joining its vertex to this circular segment. Let T be the pyramid on triangle UMV, and H the pyramid on the enclosing rectangle, both with that same vertex. Thus W is contained properly in H, so W < H (D11.18, D11.12, CN5). The pyramids T and H have equal heights; therefore 12.6 and the base-area equality from Step 4 give 2T = H (D5.5). Consequently 2T > W: inserting M removes more than half of W.
The remaining portions of the cone correspond exactly to its remaining circular segments. Adding the preceding inequalities over all these portions shows that each refinement removes more than half the entire remainder (CN2, CN3). Hence
2(C − X_{j+1}) < C − X_j,
and likewise
2(D − Y_{j+1}) < D − Y_j.

**Step 6.** It follows that, for every positive solid magnitude E and every positive integer k, some stage j satisfies
k(C − X_j) < E.
Indeed, the successive k-fold remainders also decrease by more than half at each refinement (CN2), so 10.1 applies. The same conclusion holds for k(D − Y_j). Thus both cones can be exhausted to within any assigned positive solid magnitude, including after taking any fixed multiple.

**Step 7.** Let m and n be arbitrary positive integers. Suppose first that mC > nD, and put E = mC − nD. By Step 6 choose j such that m(C − X_j) < E. Subtracting gives mX_j > nD; since Y_j is properly contained in D, we also have nD > nY_j (CN3, CN5). Thus mX_j > nY_j. The proportion X_j:Y_j = A:B from Step 3 now gives mA > nB by D5.5.
Interchanging the cones proves likewise that mC < nD implies mA < nB.

**Step 8.** Suppose now that mC = nD. If mA > nB, let Δ = mA − nB. Choose a positive integer k such that kΔ > B (D5.4). Then
kmA > (kn + 1)B
by addition and subtraction of equal magnitudes (CN2, CN3). But
kmC = knD < (kn + 1)D
(CN2, CN5). Applying the strict-inequality implication of Step 7 to the positive integers km and kn + 1 gives
kmA < (kn + 1)B,
a contradiction. Interchanging the cones excludes mA < nB in the same way. Therefore mC = nD implies mA = nB.

**Step 9.** For every pair of positive integers m,n, the multiples mC and nD therefore exceed, equal, or fall short of one another exactly as mA and nB do. By the definition of equal ratios,
C:D = A:B
(D5.5). Thus cones of the same height are to one another as their bases.

**Step 10.** Finally, let K and L be cylinders of the same height, with bases A and B, and take cones C and D on those respective bases with that height. By 12.10, K = 3C and L = 3D. Equimultiples have the same ratio as the original magnitudes, so K:L = C:D (5.15). Step 9 and 5.11 therefore give K:L = A:B. Hence cones of equal height are to one another as their bases, and cylinders of equal height are likewise to one another as their bases.

**USED:** 1.28, 1.41, 1.47, 10.1, 12.1, 12.10, 12.2, 12.6, 3.16, 3.3, 3.30, 4.6, 5.11, 5.15, 6.4, CN2, CN3, CN5, D11.12, D11.18, D11.20, D5.4, D5.5, D6.1, P1
**Human refs (from References field):** 10.1, 12.1, 12.10, 12.2, 12.6, 5.11, 5.16
**Jaccard:** 0.231 — AI adds ['1.28', '1.41', '1.47', '3.16', '3.3', '3.30', '4.6', '5.15', '6.4', 'CN2', 'CN3', 'CN5', 'D11.12', 'D11.18', 'D11.20', 'D5.4', 'D5.5', 'D6.1', 'P1']; Human adds ['5.16']

## Proposition 12.12
**Statement:** Similar cones and cylinders are to one another in the triplicate ratio of the diameters in their bases.

**Step 1.** Let A and B be similar cylinders, with base diameters a and b and heights h and k. Their heights are the lengths of their axes, so h:k = a:b. [D11.21, D11.22, D11.24] We prove the assertion for cylinders first: the equal-height comparison in 12.11 applies directly after introducing one auxiliary cylinder, and 12.10 will then transfer the conclusion to cones.

**Step 2.** Construct successive third proportionals c and d, so that a:b = b:c = c:d. [6.11] The squares on a and b have the duplicate ratio of a:b, and therefore their ratio is a:c. Here 6.20 applies directly to the squares, without requiring their division into triangles. [6.20, D5.9] Moreover, a:d is the triplicate ratio of a:b. [D5.10]

**Step 3.** Let T be the cylinder having the same base as B and height h, obtained by rotating a rectangle of that height about its fixed side. [D11.21] Since A and T have equal heights, A:T is the ratio of their bases. [12.11] Those bases are circles with diameters a and b, so their ratio is that of the squares on a and b. [12.2] Consequently, A:T = a:c. [Step 2, 5.11]

**Step 4.** We establish the particular comparison T:B directly by equimultiples. Take any positive whole numbers m and n. Stack m congruent copies of T end to end, and likewise n congruent copies of B. The resulting solids represent mT and nB. [CN4, CN2] Because all copies have the same circular base, these stacks are cylinders with that base and respective heights mh and nk: their generating rectangles are precisely the corresponding stacks of the original generating rectangles. [D11.21]

Place these two cylinders on the same initial base and along the same axis in the same direction. If mh exceeds nk, the second cylinder is a proper part of the first, so mT exceeds nB; if mh falls short of nk, the reverse holds. [CN5] If mh equals nk, the cylinders coincide, so mT equals nB. [CN4] Thus the equimultiples mT and nB have exactly the same comparisons as mh and nk, for every m and n. Hence T:B = h:k. [D5.5]

**Step 5.** By Steps 1 and 2, h:k = c:d; hence T:B = c:d. [5.11] Combining this with A:T = a:c gives, ex aequali, A:B = a:d. [5.22] Since a, b, c, d are continuously proportional, the cylinders A and B are therefore in the triplicate ratio of their base diameters a and b. [D5.10]

**Step 6.** Finally, let E and F be any similar cones, and take cylinders A and B with their respective bases and heights. These cylinders are similar because their axes and base diameters have the same proportions as those of the cones. [D11.24] Each cylinder is three times its corresponding cone. [12.10] Equimultiples have the same ratio as the original magnitudes, so E:F = A:B. [5.15] By Step 5, this is the triplicate ratio of the respective base diameters. [5.11] Therefore similar cones, and likewise similar cylinders, are to one another in the triplicate ratio of the diameters in their bases.

**USED:** 12.10, 12.11, 12.2, 5.11, 5.15, 5.22, 6.11, 6.20, CN2, CN4, CN5, D11.21, D11.22, D11.24, D5.10, D5.5, D5.9
**Human refs (from References field):** 10.1, 12.10, 12.8, 4.6, 5.12, 5.16, 5.22, 6.5, 6.6, D11.24, D11.9, D6.1
**Jaccard:** 0.115 — AI adds ['12.11', '12.2', '5.11', '5.15', '6.11', '6.20', 'CN2', 'CN4', 'CN5', 'D11.21', 'D11.22', 'D5.10', 'D5.5', 'D5.9']; Human adds ['10.1', '12.8', '4.6', '5.12', '5.16', '6.5', '6.6', 'D11.9', 'D6.1']

## Proposition 12.13
**Statement:** If a cylinder be cut by a plane which is parallel to its opposite planes, then, as the cylinder is to the cylinder, so will the axis be to the axis.

**Step 1.** Let the original cylinder have axis AB, and let the cutting plane meet AB at C. Denote the resulting cylinders adjacent to A and B by U and V. In the plane of the generating rectangle, the cutting plane has its trace parallel to the two radial sides, because the three section planes are parallel (11.16). It therefore divides the generating rectangle into two rectangular parallelograms with equal radial sides (1.34). Their rotations generate U and V, whose axes are AC and CB and whose bases have the same radius r (D11.21, D11.22, D11.23). These circular bases are equal (D3.1).

**Step 2.** We take the direct equimultiple route, using 12.11 because it supplies precisely the equal-height comparison needed. Any two cylinders of radius r with equal axes have equal heights; therefore their ratio is the ratio of their bases (12.11). Their bases are equal (D3.1), so the cylinders are equal: in the criterion defining equality of ratios, take one copy of each magnitude (D5.5). Thus cylinders of this fixed radius and equal axis lengths are equal.

**Step 3.** Let m and n be arbitrary positive integers. On the ray AB, produced as necessary, lay off m successive lengths equal to AC and n successive lengths equal to CB, obtaining endpoints X and Y. Thus AX = m·AC and AY = n·CB (P2, 1.3). In the generating plane, draw parallels to the original radial side through the division points, extending the original outer side as necessary (1.31, P2). Revolve the rectangles of radial width r and axial lengths AX and AY about the common axis. Let the resulting cylinders, both standing on the original base circle at A, be M and N (D11.21, D11.22).

**Step 4.** The subdivisions of AX divide its generating rectangle into m rectangles, and hence divide M into m cylinders, each of radius r and axis length AC (D11.21). Each is equal to U by Step 2. Adding these equal magnitudes gives M = m·U (CN2). Likewise, the subdivisions of AY give N = n·V (D11.21, Step 2, CN2).

**Step 5.** Compare AX and AY. If AX is greater than AY, the generating rectangle for N is a proper part of that for M, so N is a proper part of M; consequently M is greater than N (D11.21, CN5). If AX equals AY, then M equals N by Step 2. If AX is less than AY, the same containment argument gives M less than N (D11.21, CN5). Thus m·U exceeds, equals, or falls short of n·V exactly as m·AC exceeds, equals, or falls short of n·CB.

**Step 6.** Since m and n were arbitrary, the equimultiples of U and AC compare alike with the corresponding equimultiples of V and CB. By the definition of equal ratios (D5.5), U : V = AC : CB. Therefore, as the cylinder is to the cylinder, so is its axis to the other axis, as required.

**USED:** 1.3, 1.31, 1.34, 11.16, 12.11, CN2, CN5, D11.21, D11.22, D11.23, D3.1, D5.5, P2
**Human refs (from References field):** 12.11, D5.5
**Jaccard:** 0.154 — AI adds ['1.3', '1.31', '1.34', '11.16', 'CN2', 'CN5', 'D11.21', 'D11.22', 'D11.23', 'D3.1', 'P2']

## Proposition 12.14
**Statement:** Cones and cylinders which are on equal bases are to one another as their heights.

**Step 1.** Let A and B be cylinders on equal circular bases α and β, with heights h and k respectively. Their axes have lengths h and k (D11.21, D11.22, D11.23). We first prove the assertion for cylinders: the direct route is to make two pieces of one cylinder, so that 12.13 applies. We shall then pass to cones using 12.10.

**Step 2.** Produce the axis of A beyond its upper base by a segment equal to k, and prolong its generating rectangle accordingly. Rotating the enlarged rectangle about the extended axis gives a cylinder T of height h + k (P2, 1.3, D11.21). The original upper-base plane of A cuts T into A and another cylinder E, whose height is k and whose base is equal to α (D11.21, D11.23). This cutting plane is parallel to the bases of T, since all these planes are perpendicular to the same axis (11.14).

**Step 3.** The cylinders E and B have the same height k. Therefore, by 12.11,
E : B = α : β.
Since α = β, the equality clause in the definition of equal ratios, taking one copy of each magnitude, gives E = B (D5.5).

**Step 4.** Apply 12.13 to the two cylinders into which the indicated parallel plane cuts T. Their axes have lengths h and k, so
A : E = h : k.
Substituting E = B from Step 3 gives
A : B = h : k.
Thus cylinders on equal bases are to one another as their heights.

**Step 5.** Now let K and L be cones on equal bases, with heights h and k. Let U and V be the cylinders on their respective bases and of their respective heights. By 12.10, U is three times K and V is three times L. Equimultiples have the same ratio as the magnitudes of which they are equimultiples; hence
K : L = U : V (5.15).

**Step 6.** By the cylinder result of Step 4,
U : V = h : k.
Combining this with Step 5 yields K : L = h : k (5.11). Therefore cones on equal bases, and likewise cylinders on equal bases, are to one another as their heights.

**USED:** 1.3, 11.14, 12.10, 12.11, 12.13, 5.11, 5.15, D11.21, D11.22, D11.23, D5.5, P2
**Human refs (from References field):** 12.10, 12.11, 12.13
**Jaccard:** 0.250 — AI adds ['1.3', '11.14', '5.11', '5.15', 'D11.21', 'D11.22', 'D11.23', 'D5.5', 'P2']

## Proposition 12.15
**Statement:** In equal cones and cylinders the bases are reciprocally proportional to the heights; and those cones and cylinders in which the bases are reciprocally proportional to the heights are equal.

**Step 1.** Let X and Y be two cones, or two cylinders, with circular bases B₁ and B₂ and respective heights h₁ and h₂. Construct a third solid T of the same kind, with base B₂ and height h₁, using the generating right triangle for a cone or rectangle for a cylinder (D11.18, D11.21). Path choice: this auxiliary solid supplies an equal-height comparison and an equal-base comparison, so 12.11 and 12.14 apply directly to either kind of solid without reducing one kind to the other.

**Step 2.** Since X and T have the same height h₁, they are to one another as their bases:
X : T = B₁ : B₂. (12.11)

**Step 3.** Since Y and T have the same base B₂, they are to one another as their heights:
Y : T = h₂ : h₁. (12.14)

**Step 4.** First suppose that X and Y are equal. Equal magnitudes have the same ratio to the same magnitude, so X : T = Y : T (5.7). Combining this with Steps 2 and 3 gives B₁ : B₂ = h₂ : h₁ (5.11). Thus the bases of the equal solids are reciprocally proportional to their heights.

**Step 5.** Conversely, suppose that the bases are reciprocally proportional to the heights, so B₁ : B₂ = h₂ : h₁. By Steps 2 and 3, X : T = Y : T (5.11). Magnitudes having the same ratio to the same magnitude are equal; hence X = Y (5.9). Both assertions therefore hold for two cones and for two cylinders.

**USED:** 12.11, 12.14, 5.11, 5.7, 5.9, D11.18, D11.21
**Human refs (from References field):** 12.11, 12.13, 5.11, 5.7, 5.9
**Jaccard:** 0.500 — AI adds ['12.14', 'D11.18', 'D11.21']; Human adds ['12.13']

## Proposition 12.16
**Statement:** Given two circles about the same centre, to inscribe in the greater circle an equilateral polygon with an even number of sides which does not touch the lesser circle.

**Step 1.** Let O be the common centre. Choose A on the greater circumference, join OA, and let T be its intersection with the lesser circumference. Write R = OA, r = OT, and g = TA. Thus R = r + g and 0 < g < R. We shall construct equal sides shorter than the radial gap g; the triangle inequality will then exclude contact with the lesser circle. [P1, D1.15, CN5; 1.20]

**Step 2.** Since g is less than a radius, it is less than a diameter of the greater circle. Fit into that circle a chord EF equal to g, and join OE and OF. Let β = ∠EOF. This angle is positive and less than two right angles, since EF is neither zero nor a diameter. [D1.17, CN5, 4.1, P1]

**Step 3.** Inscribe a square in the greater circle by 4.6, using its perpendicular-diameter construction, and join its vertices to O. The four triangles thereby formed have their corresponding sides equal: their two radial sides are radii of the same circle, and their bases are sides of the square. Hence their four central angles are equal. [4.6, P1, D1.15, D1.22, 1.8]

**Step 4.** Refine this division by bisecting every central angle and then bisecting each resulting angle; extend the new bisectors to the greater circumference. Repeat this operation uniformly. All central angles remain equal, and after each round their common magnitude is one quarter of its preceding magnitude. Consequently, by 10.1, after finitely many rounds their common angle α is less than β. Two bisections per round are used so that the decrease is greater than half, exactly as required by 10.1. [1.9, P2, 10.1]

**Step 5.** Join the resulting circumference points consecutively. If k rounds were performed, the polygon has 4·4^k sides, an even number, and is inscribed in the greater circle. Its central triangles have two corresponding radii equal and their included angles all equal to α; therefore their bases, which are the polygon's sides, are all equal. [P1, D4.3, D7.6, D1.15, 1.4]

**Step 6.** Let UV be any side of this polygon. In triangles OUV and OEF, the two sides issuing from O are respectively equal, whereas ∠UOV = α < β = ∠EOF. Therefore UV < EF = g by 1.24. This is the natural comparison because the construction refined central angles. In particular, UV is shorter than a radius and is not a diameter. [D1.15, 1.24, D1.17, CN5]

**Step 7.** Let X be an interior point of UV. Since UV is not a diameter, OUX is a triangle. Now UX < UV < g, while the triangle inequality gives OX + UX > OU = R. Hence OX > R − UX > R − g = r. The endpoints U and V likewise have distance R > r from O. Thus every point of every side is strictly farther from O than the lesser circle's radius, so no side meets its circumference. The constructed polygon is therefore equilateral, has an even number of sides, is inscribed in the greater circle, and does not touch the lesser circle, as required. [CN5, 1.20, CN3, D1.15]

**USED:** 1.20, 1.24, 1.4, 1.8, 1.9, 10.1, 4.1, 4.6, CN3, CN5, D1.15, D1.17, D1.22, D4.3, D7.6, P1, P2
**Human refs (from References field):** 1.4, 10.1, 3.16, 3.3
**Jaccard:** 0.105 — AI adds ['1.20', '1.24', '1.8', '1.9', '4.1', '4.6', 'CN3', 'CN5', 'D1.15', 'D1.17', 'D1.22', 'D4.3', 'D7.6', 'P1', 'P2']; Human adds ['3.16', '3.3']

## Proposition 12.17
**Statement:** Given two spheres about the same centre, to inscribe in the greater sphere a polyhedral solid which does not touch the lesser sphere at its surface.

**Step 1.** Let O be the common centre, and let R and r be the radii of the greater and lesser spheres, with R > r. The spherical definitions identify these radii with the radii of their generating semicircles [D1.15, D11.14, D11.16]. Path choice: use the planar construction of 12.16 twice, with an intermediate radius chosen to control both approximations. Construct the mean proportional s between r and R; thus s² = rR and r < s < R [6.13, 6.17, CN5]. Products and squares below denote the corresponding rectangles and squares.

**Step 2.** In a great circle of the greater sphere, apply 12.16 with the concentric circle of radius s. Obtain an equilateral polygon with an even number 2p of sides, none of which meets the smaller circle [12.16]. Equal chords cut off equal arcs, so the vertices are equally spaced; consequently opposite vertices N and S terminate a diameter [3.28, D1.17]. Let V₀ = N, V₁, …, Vₚ = S be the vertices on one semicircle. Draw perpendiculars from O to the sides. They bisect the sides, and all have one length a, because the chords are equal [1.12, 3.3, 3.14]. Since the sides do not meet the circle of radius s, a > s.

**Step 3.** In the equatorial great circle perpendicular to NS, apply 12.16 again, obtaining an equilateral polygon with q sides whose common distance from O is b > s [12.16, 3.3, 3.14]. Its vertices are equally spaced [3.28]. A right triangle formed by a radius and half a side gives 0 < b < R [1.47]. Write k = b/R. Then 0 < k < 1 and

ka = ab/R > s²/R = r,

because the rectangle contained by a and b is greater than the square on s [CN5, 6.17].

**Step 4.** Rotate the semicircular chain V₀V₁…Vₚ about NS into the q positions determined by the radii to the equatorial polygon's vertices. All its vertices remain on the greater sphere [D11.14]. At each non-polar level this gives a regular q-sided polygon in a circle centred on NS. Call these the rings. Join consecutive vertices around each ring, and join corresponding vertices on consecutive rings; at the ends join the first and last rings to N and S respectively [P1].

**Step 5.** Consider two consecutive half-meridian planes used in this construction, and let Π be their bisecting meridian plane. For a non-polar ring, let Cᵢ be its centre, let ρᵢ be its radius, and let Mᵢ be the midpoint of its edge between the chosen half-meridians. The triangle formed by its two bounding radii is similar to the corresponding equatorial triangle: the included angles are equal by construction and the containing sides are proportional [6.6]. Comparing their midpoint right triangles therefore gives

CᵢMᵢ/ρᵢ = b/R = k,

and Mᵢ lies in Π [3.3, 6.4]. Each such ring edge is perpendicular both to the radial line in Π and to the axis direction, and hence is perpendicular to Π [3.3, D11.3, 11.4]. Thus the successive ring edges are parallel [11.6], and two consecutive ones, together with their joining sides, form a plane trapezoid [11.7]. At a pole the corresponding face is a triangle [11.2]. Put M₀ = N and Mₚ = S.

**Step 6.** Between each pair of consecutive non-polar rings take the solid bounded by their two polygonal bases and these trapezoids. At either end take the pyramid whose vertex is the pole and whose base is the adjacent ring [D11.12]. Stack these finitely many solids in their order along NS. Their common polygonal bases become internal, leaving precisely the trapezoids and polar triangles as the boundary of a polyhedral solid K [D11.1, D11.2]. Every ring surrounds its centre on NS, and every intermediate polygonal section has positive size away from the poles. Hence O is interior to K.

**Step 7.** The whole of K is within the greater sphere. Indeed, a segment joining two points on or inside that sphere lies inside it: take a plane containing its line and O, and apply the circle chord theorem in the resulting great circle [11.2, 3.2, D11.14]. Each ring polygon lies in its circular section by the same chord theorem [3.2]. Each layer of K consists of segments joining corresponding points of its two polygonal bases; a polar layer consists of segments joining its base to the pole. Therefore every layer is inside the sphere. Since all vertices of K are on its surface by Step 4, K is inscribed in the greater sphere.

**Step 8.** Let X be any point of a boundary face F, and use the bisecting plane Π belonging to that face. Suppose F lies between levels i and i+1, allowing a pole as either level. Through X draw the line parallel to the ring edges. It meets the segment MᵢMᵢ₊₁ at a point H: parallel sections of a trapezoid, or of a polar triangle, meet its midpoint segment within that segment [1.31, 6.2]. By Step 5, XH is perpendicular to Π. Since O and H lie in Π, the right-triangle theorem gives

OX ≥ OH,

with equality when X = H [D11.3, 1.47].

**Step 9.** In Π place the original meridian chain, and denote its vertices at the two relevant levels by Uᵢ and Uᵢ₊₁. Step 5 says that Mᵢ and Mᵢ₊₁ are obtained from these vertices by multiplying their perpendicular distances from NS by k, while leaving their levels unchanged. The same correspondence takes the entire side UᵢUᵢ₊₁ onto MᵢMᵢ₊₁. To see this directly, if the side meets NS at T, compare the right triangles with vertex T and bases perpendicular to NS; similarity gives the same factor k at every intermediate level [6.4]. If the side is parallel to NS, the assertion follows from its constant distance from NS. Thus there is a point Y on UᵢUᵢ₊₁ at the same level as H such that, writing C for their common perpendicular foot on NS,

CH = k·CY.

**Step 10.** The rotated meridian side has distance a from O, so every point Y on it satisfies OY ≥ a [3.14, 1.47]. Applying the right-triangle theorem to OCH and OCY, and using 0 < k < 1, gives

OH² = OC² + CH²
     = OC² + k²CY²
     ≥ k²(OC² + CY²)
     = k²OY²
     ≥ k²a².

Here the inequality follows because OC² ≥ k²OC² [1.47, CN5]. Consequently, by Steps 3 and 8,

OX ≥ OH ≥ ka > r.

Thus every point of every boundary face is strictly farther than r from O.

**Step 11.** The boundary of K therefore has no point on or inside the lesser sphere [D11.14, D11.16]. Moreover, since O is interior to K, every radius of the lesser sphere remains inside K: any first exit would be a boundary point at distance at most r, contrary to Step 10 [D11.2]. Hence K is a polyhedral solid inscribed in the greater sphere which encloses the lesser sphere without touching its surface, as required.

**USED:** 1.12, 1.31, 1.47, 11.2, 11.4, 11.6, 11.7, 12.16, 3.14, 3.2, 3.28, 3.3, 6.13, 6.17, 6.2, 6.4, 6.6, CN5, D1.15, D1.17, D11.1, D11.12, D11.14, D11.16, D11.2, D11.3, P1
**Human refs (from References field):** 1.26, 1.33, 1.47, 11.11, 11.18, 11.2, 11.6, 11.7, 11.9, 3.27, 3.31, 6.2, 6.8, D11.14, D11.3, D11.4
**Jaccard:** 0.194 — AI adds ['1.12', '1.31', '11.4', '12.16', '3.14', '3.2', '3.28', '3.3', '6.13', '6.17', '6.4', '6.6', 'CN5', 'D1.15', 'D1.17', 'D11.1', 'D11.12', 'D11.16', 'D11.2', 'P1']; Human adds ['1.26', '1.33', '11.11', '11.18', '11.9', '3.27', '3.31', '6.8', 'D11.4']

## Proposition 12.18
**Statement:** Spheres are to one another in the triplicate ratio of their respective diameters.

**Step 1.** Let S and T be the two spheres, with diameters d and e, and let C and D be their circumscribing cubes, whose edges are respectively d and e. Letters denoting solids will also denote their solid magnitudes. By 11.33, C:D is the triplicate ratio of d:e. It therefore suffices to prove S:T = C:D according to D5.5. The chosen route uses 12.17 to bracket a sphere by polyhedra and 12.8 to compare their triangular pyramids; 12.8 is the natural choice because triangulating the faces and joining them to the centre produces exactly such pyramids.

**Step 2.** We first explain the comparison of the similarly situated polyhedra used below. Triangulate the faces of a convex polyhedron and join their triangles to an interior point O, thereby dividing the solid into triangular pyramids (P1). Construct a copy by placing corresponding vertices on the same rays from O, with every distance from O changed in one fixed ratio (P2, 6.12). Corresponding triangles through O are similar by 6.6; hence corresponding edges have that fixed ratio, and corresponding face triangles are similar by 6.5. The corresponding pyramids are therefore similar (D11.9). By 12.8, every pair of corresponding pyramids has the triplicate ratio of the fixed linear ratio. Their sums have this same ratio by 5.12, and consequently have the same ratio as cubes on corresponding lengths, by 11.33 and 5.11. Such radial copying also carries a sphere to the sphere with correspondingly changed radius (D11.14, D11.17). The diameters have the same ratio as the radii, since they are their doubles (5.15).

**Step 3.** To establish the comparisons required by D5.5, take arbitrary positive integers m and n such that mC ≤ nD. Suppose, for a contradiction, that mS > nT, and denote the positive excess mS − nT by Δ. Thus mS = nT + Δ (CN3). We shall construct an inscribed polyhedron P such that m(S − P) < Δ.

**Step 4.** For a length h with 0 < h ≤ d, let L_h be a rectangular slab with dimensions d, d, h. Let E_h be a cube of edge d + h, containing C with one vertex and the three incident edge-directions common. Cutting at the three opposite faces of C divides E_h − C into seven rectangular blocks: three with dimensions d, d, h; three with dimensions d, h, h; and one with dimensions h, h, h. Each is no greater than L_h, since h ≤ d, by coincidence and containment. Consequently E_h − C ≤ 7L_h (CN4, CN5, CN2).

**Step 5.** Starting with h = d, repeatedly quarter h by two bisections (1.10). Each corresponding slab is one quarter of the preceding slab, as is seen by division into four congruent slabs (CN4). Thus 7mL_h is likewise quartered at every stage (CN2). Since each operation removes more than half of the preceding magnitude, 10.1 supplies a finite stage at which 7mL_h < Δ. Fix this h and write E = E_h. Step 4 then gives m(E − C) ≤ 7mL_h < Δ.

**Step 6.** Construct a sphere S⁺ concentric with S and having diameter d + h (P3, D11.14). Apply 12.17 to S⁺ and S: obtain an inscribed polyhedral solid Q whose surface lies outside the inner sphere S, so that Q contains S. Contract Q radially about their common centre in the ratio d:(d + h), obtaining P by the construction in Step 2. The contraction carries S⁺ to S, so P is inscribed in S. We therefore have P ⊆ S ⊆ Q and S − P ≤ Q − P (CN3, CN5).

**Step 7.** By Step 2, the similarly situated polyhedra satisfy Q:P = E:C. Separation and alternation give
(Q − P):(E − C) = P:C
(5.17, 5.16). Since P lies within S and S is a proper part of its circumscribing cube C, P < C (CN5). The displayed proportion therefore implies Q − P < E − C, by D5.5 applied to the single multiples. Together with Steps 5 and 6, this yields
m(S − P) ≤ m(Q − P) < m(E − C) < Δ
(CN2, CN3).

**Step 8.** Copy P radially into T with linear ratio e:d, and call the resulting inscribed polyhedron R. By Step 2, P:R = C:D. Since mC ≤ nD, D5.5 gives mP ≤ nR. Also R ⊆ T, so nR ≤ nT (CN5, CN2). Hence mP ≤ nT. But Step 7 gives
mP = mS − m(S − P) > mS − Δ = nT,
a contradiction (CN2, CN3). We have proved, for all positive integers m and n,
mC ≤ nD implies mS ≤ nT.

**Step 9.** Exchanging the two spheres in Step 8 proves that mC ≥ nD implies mS ≥ nT. Thus mC = nD implies mS = nT. Now suppose mC < nD. Step 8 gives mS ≤ nT. If equality held, use D5.4 to choose a positive integer k such that k(nD − mC) > C. Adding and subtracting equal magnitudes gives
(km + 1)C < knD
(CN2, CN3). Step 8 would then imply (km + 1)S ≤ knT. But mS = nT gives kmS = knT, and adding the positive magnitude S gives (km + 1)S > knT, a contradiction (CN2, CN5). Therefore mC < nD implies mS < nT. Interchanging the spheres also proves that mC > nD implies mS > nT.

**Step 10.** Consequently, for every pair of positive integers m and n, the comparison of mS with nT agrees exactly with that of mC with nD. Hence S:T = C:D by D5.5. Since C:D is the triplicate ratio of their edges d:e by 11.33, the spheres are to one another in the triplicate ratio of their respective diameters.

**USED:** 1.10, 10.1, 11.33, 12.17, 12.8, 5.11, 5.12, 5.15, 5.16, 5.17, 6.12, 6.5, 6.6, CN2, CN3, CN4, CN5, D11.14, D11.17, D11.9, D5.4, D5.5, P1, P2, P3
**Human refs (from References field):** 12.17, 12.2, 5.16
**Jaccard:** 0.077 — AI adds ['1.10', '10.1', '11.33', '12.8', '5.11', '5.12', '5.15', '5.17', '6.12', '6.5', '6.6', 'CN2', 'CN3', 'CN4', 'CN5', 'D11.14', 'D11.17', 'D11.9', 'D5.4', 'D5.5', 'P1', 'P2', 'P3']; Human adds ['12.2']
