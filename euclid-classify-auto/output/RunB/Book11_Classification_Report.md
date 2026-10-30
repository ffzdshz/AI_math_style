# Book 11 — Classification Report (RunB)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 1 | 11.15 |
| Granularity difference (G) | 28 | 11.1, 11.2, 11.3, 11.4, 11.5, 11.8, 11.9, 11.10, 11.11, 11.12, 11.13, 11.14, 11.16, 11.17, 11.18, 11.19, 11.20, 11.21, 11.22, 11.23, 11.24, 11.25, 11.27, 11.28, 11.30, 11.32, 11.37, 11.39 |
| Path difference (D) | 10 | 11.6, 11.7, 11.26, 11.29, 11.31, 11.33, 11.34, 11.35, 11.36, 11.38 |
| AI proof error (E) | 0 |  |

**Total**: 39 propositions

## Per-Proposition Analysis

### 11.1
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: assume for contradiction that part AB of line ABC lies in the reference plane while part BC is elevated, construct a line BD as the continuation of AB entirely within the reference plane, identify that ABC and ABD share the common segment AB, and derive a contradiction from the impossibility of two distinct straight lines sharing a common segment. Heath appeals to a circle-based argument (diameters cutting unequal circumferences) while the AI appeals to D1.4 (uniqueness of straight line continuation) to establish the impossibility, but these are different expressions of the same geometric fact forming the same key intermediate conclusion. The citation sets differ because Heath has no recorded citations while the AI explicitly cites foundational items (D1.4, D1.7, P2), which are definitions and a postulate representing over-citation at the axiomatic level. Since the backbones match and the differences are only in citation depth, this is a granularity difference (G).

### 11.2
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: that two intersecting straight lines lie in one plane (via contradiction using 11.1) and that every triangle lies in one plane (again via contradiction using 11.1). The AI reverses the order of argument compared to Heath (proving coplanarity of intersecting lines first, then triangles, whereas Heath proves the triangle result first), but the backbone geometric facts are identical. The ai_only items D1.19 (definition of triangle) and P1 (postulate for joining points) are a definition and a postulate that Heath uses implicitly, making this a citation-depth difference rather than a path difference. Since the citation sets are not identical (AI adds D1.19 and P1), this is G rather than P.

### 11.3
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: assume for contradiction that the common section DB is not straight, construct straight lines DEB in plane AB and DFB in plane BC, observe that two distinct straight lines share the same endpoints and thus enclose a space (which is impossible), and conclude DB must be straight. The AI proof explicitly cites D1.7 (definition of a plane surface) and P1 (postulate for drawing straight lines) while Heath's proof uses these same foundations implicitly without explicit citation. Since heath_refs is empty and ai_only contains only a definition and a postulate (not substantive propositions), this is a straightforward case of the AI over-citing foundational axioms and definitions, which is a citation-depth difference with the same backbone. This yields Granularity difference (G).

### 11.4
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions in the same order: (1) AD=BC and angle DAE=angle EBC via triangle congruence I.4 with vertical angles I.15, (2) GE=EH and AG=BH via I.26, (3) FA=FB and FC=FD via I.4, (4) angle FAD=angle FBC via I.8, (5) FG=FH via I.4, (6) angle GEF=angle HEF via I.8, concluding that EF is perpendicular to the plane via XI.Def.3. The logical backbones are identical. The ai_only set consists entirely of construction/foundational items (1.3, P1, P4, CN1, D1.10) that Heath leaves implicit, while heath_only is empty. This is a clear Case A granularity difference where the AI over-cites axiomatic and constructive steps.

### 11.5
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same backbone: assume one of the three lines is not in the plane determined by the other two, use 11.3 to find the intersection line of the assumed separate plane with the original plane, use 11.4 to establish perpendicularity to the original plane, then use D11.3 to show a right angle with the intersection line, and derive a contradiction from having two equal right angles with distinct lines from the same point. The AI proof explicitly cites P4 (all right angles are equal) and CN5 (the whole is greater than the part) to articulate the final contradiction, while Heath leaves these steps implicit, simply stating the equality is impossible. Since heath_only is empty and ai_only contains only axiom-level citations (P4, CN5) that make explicit what Heath uses implicitly, this is a same-backbone, different-citation-depth situation — Case A of Q2.

### 11.6
**Category**: Path difference
**Jaccard**: 0.143
**Analysis**: Q2 decides the classification. Both proofs share the same high-level strategy (construct DE perpendicular to BD, prove angle EDA is right, use XI.5 for coplanarity, conclude parallelism), but the key intermediate conclusions differ substantively. Heath proves angle EDA is right via triangle congruence: I.4 (SAS) yields AD = BE, then I.8 (SSS) yields angle ABE = angle EDA, so EDA is right. The AI instead uses a Pythagorean approach: I.47 applied three times gives squared-length relationships, algebraic substitution (CN1, CN2) yields AE squared = AD squared + DE squared, and I.48 (converse Pythagorean theorem) gives angle ADE is right. These are genuinely different mathematical techniques with different intermediate geometric facts (equality of segments vs. squared-length identities), not merely different levels of granularity. Additionally, the final parallelism step uses different propositions: Heath applies I.28 (co-interior angles) while the AI applies I.27 (alternate angles). The AI's path is logically valid throughout, so this is a path difference (D), not an error.

### 11.7
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Heath proves 11.7 by contradiction: assuming the joining line EF is in a more elevated plane, he uses 11.3 (plane intersection yields a straight line) to derive two lines EGF and EF enclosing an area, which is impossible. The AI instead gives a direct proof: since parallel lines share a plane P (D1.23), it constructs triangle EHF from points on those lines, uses 11.2 (every triangle is in one plane) to place it in plane Q, extends AB fully into Q via 11.1, shows EF lies in Q as a side of the triangle, then similarly shows CD is in Q, and concludes P equals Q by uniqueness of the plane through three non-collinear points. The two proofs have entirely different key intermediate conclusions and share no citations (Jaccard 0.0). The AI's direct constructive path is logically sound, so Q3 confirms a valid different path, yielding category D.

### 11.8
**Category**: Granularity difference
**Jaccard**: 0.444
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) angle ABD is right via D11.3, (2) A,B,C,D coplanar via 11.7, (3) CD perpendicular to BD via 1.29, (4) construct DE perpendicular to BD in the reference plane, (5) angle ABE is right via D11.3, (6) angle ADE is right, (7) DE perpendicular to the plane through BD and AD via 11.4, (8) DC in that plane, (9) DE perpendicular to CD, (10) CD perpendicular to the reference plane via 11.4. The difference lies in how step (6) is established: Heath uses triangle congruence (SAS then SSS, requiring DE = AB) while the AI uses the Pythagorean theorem (1.47) and its converse (1.48). This is a different micro-level technique reaching the same key intermediate conclusion, not a different backbone. The AI's additional citations of 1.11 and P1 are construction-level over-citations, and its omission of 11.2 is a granularity matter since the AI makes the equivalent argument textually without citing 11.2. Same backbone with different citation depth yields G.

### 11.9
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: construct GH and GK perpendicular to EF in their respective planes, apply XI.4 to establish EF is perpendicular to the plane through GH and GK, then use XI.8 to show AB and CD are each perpendicular to that plane, and finally apply XI.6 to conclude AB is parallel to CD. The only difference is that the AI explicitly cites I.11 for the construction of perpendiculars GH and GK, while Heath states the construction without citing this justification. Since 1.11 is a construction proposition and the key intermediate conclusions are identical in both proofs, this is a citation-depth difference (Case A in Q2), yielding Granularity difference.

### 11.10
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions: cutting BA, BC, ED, EF equal, showing AD and CF are each equal and parallel to BE (via I.33 applied twice), deducing AD is equal and parallel to CF (via XI.9 and transitivity), concluding AC equals DF (via I.33 a third time), and finally applying SSS congruence (I.8) to obtain angle ABC = angle DEF. The AI's three extra citations (1.3 for cutting off equal segments, P1 for joining lines, CN1 for transitivity of equality) are all construction-level or axiom-level steps that Heath performs implicitly without explicit citation. With heath_only empty and ai_only consisting entirely of over-citations of foundational steps, this is a clear Case A same-backbone, different-depth scenario, yielding Granularity difference (G).

### 11.11
**Category**: Granularity difference
**Jaccard**: 0.857
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: draw BC in the plane, drop AD perpendicular to BC, draw DE at right angles to BC in the plane, draw AF perpendicular to DE, draw GH parallel to BC through F, then argue that BC is perpendicular to the plane through DA and DE (XI.4), GH is likewise perpendicular to that plane (XI.8 via parallelism), GH is therefore perpendicular to AF (XI.Def.3), and since AF is perpendicular to both GH and DE it is perpendicular to the reference plane (XI.4). The only citation difference is that the AI includes P1 (a postulate for drawing a line) which Heath leaves implicit. Since ai_only contains only a postulate and heath_only is empty, and all key intermediate conclusions match, this is a granularity difference (Case A of Q2).

### 11.12
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification. Both proofs share the identical logical backbone: (1) conceive an elevated point B, (2) draw BC perpendicular to the given plane using 11.11, (3) draw AD through A parallel to BC using 1.31, (4) conclude AD is perpendicular to the plane by 11.8 since it is parallel to a line perpendicular to the plane. The only citation difference is that the AI explicitly cites D11.3 (the definition of a line being at right angles to a plane) to frame the construction goal and the conclusion, while Heath leaves this definition implicit. Since D11.3 is a definition and the key intermediate conclusions are identical in both proofs, this is a citation-depth difference classifying as G.

### 11.13
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided this as Granularity difference (G). Both proofs follow the same logical backbone: assume two lines AB, AC from point A are perpendicular to the same plane on the same side; the plane through AB and AC cuts the reference plane in a straight line DE (by 11.3); both angles BAE and CAE are right by D11.3; therefore BAE equals CAE, yet one is part of the other since AB and AC are distinct lines on the same side, giving a contradiction. The AI proof adds three citations not in Heath: 11.2 (for the fact that AB and AC determine a plane, which Heath simply assumes without citation), P4 (all right angles are equal, which Heath states implicitly), and CN5 (whole is greater than part, which Heath expresses as 'which is impossible' without citing the common notion). All three ai_only items are over-citations of foundational or axiomatic steps that Heath leaves implicit, representing citation-depth differences rather than backbone divergence. Heath_only is empty, confirming the AI covers all of Heath's reasoning. The citation sets differ so this is not P.

### 11.14
**Category**: Granularity difference
**Jaccard**: 0.800
**Analysis**: Q2 decided the classification. Both proofs follow an identical logical backbone: assume the planes are not parallel, derive a common section line GH via 11.3, take a point K on GH, join AK and BK, use D11.3 to establish that both angles ABK and BAK are right angles, then obtain a contradiction via 1.17 (two angles of a triangle sum to two right angles), and conclude the planes are parallel by D11.8. The only citation difference is that the AI explicitly cites postulate P1 for the construction step of joining AK and BK, while Heath performs this step implicitly without citing the postulate. Since ai_only contains only P1 (a postulate/construction axiom) and heath_only is empty, this is a straightforward case of over-citation at the construction level, which is a citation-depth difference under Case A of Q2, yielding category G.

### 11.15
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof follow identical logical backbones: constructing BG perpendicular to the plane through DE, EF (11.11), drawing GH parallel to ED and GK parallel to EF in that plane (1.31), establishing that angles BGH and BGK are right via the definition of perpendicularity to a plane (D11.3), using 11.9 to show AB is parallel to GH and BC is parallel to GK, applying 1.29 to show the transversal BG creates right angles ABG and CBG, concluding via 11.4 that BG is perpendicular to the plane through AB, BC, and finally invoking 11.14 to establish the planes are parallel. The citation sets are identical (Jaccard = 1.0) with ai_only and heath_only both empty, and the key intermediate conclusions match at every stage, yielding a perfect match classification.

### 11.16
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: proof by contradiction assuming the two common-section lines meet at a point K, showing K must lie in both parallel planes (contradicting the hypothesis), and concluding the lines are parallel by definition. The citation differences are purely depth-related. Heath cites 11.1 to justify that a point on a line in a plane must be in that plane; the AI makes the equivalent argument directly from the definition of common section without citing 11.1. The AI explicitly cites 11.3 (common section of two planes is a straight line) and D11.8 (definition of parallel planes), which Heath uses implicitly. These are over-citations of construction and definitional facts. The key intermediate conclusions are identical in both proofs, with only the citation granularity differing.

### 11.17
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: construct AD meeting the middle plane at a point, use 11.16 twice to establish parallelisms (EO/EG parallel to BD, and OF/FG parallel to AC), apply 6.2 twice to obtain proportional relationships in triangles ABD and ACD, and then conclude via 5.11 (transitivity of ratios). The AI's only structural difference is that it applies 6.2 from the opposite vertex in triangle ACD, yielding DF:FC = DG:GA instead of Heath's direct AO:OD = CF:FD, and then explicitly inverts the ratio using definitions D5.5 and D5.13. The ai_only citations (P1, D5.5, D5.13) are all postulates or definitions representing over-citation of construction steps and ratio manipulation that Heath handles implicitly. Since heath_only is empty and the key intermediate conclusions are identical, this is Case A of Q2: same backbone with different citation depth, yielding G.

### 11.18
**Category**: Granularity difference
**Jaccard**: 0.833
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: take an arbitrary plane through AB, identify its common section with the reference plane, draw a line in that plane perpendicular to the common section (I.11), show AB is perpendicular to the common section via D11.3, conclude AB is parallel to FG via I.28, deduce FG is perpendicular to the reference plane via XI.8, and apply D11.4 to conclude the plane is at right angles to the reference plane. The only citation difference is that the AI explicitly cites 11.3 to justify that the intersection of two planes is a straight line, a fact Heath uses implicitly without citation. Since heath_only is empty and ai_only contains only 11.3 (a foundational proposition making explicit what Heath takes for granted), this is a same-backbone, different-citation-depth scenario, yielding Granularity difference (G).

### 11.19
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: assume BD is not perpendicular to the reference plane, draw perpendiculars in each of the two planes to the lines of intersection with the reference plane, apply Definition 11.4 to conclude both constructed lines are perpendicular to the reference plane, then invoke 11.13 to reach a contradiction (two lines from the same point cannot both be perpendicular to a plane on the same side). The AI's two extra citations (1.11 for drawing perpendicular lines and 11.3 for the common section being a straight line) are construction-level propositions that Heath uses implicitly without explicit citation. Since the key intermediate conclusions are identical and the citation differences reflect only citation depth, this is a granularity difference.

### 11.20
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs follow identical logical backbones: (1) construct angle BAE equal to DAB in the plane of BAC with AE equal to AD, (2) show DB = BE via I.4, (3) use I.20 on triangle BDC to derive DC > EC, (4) apply I.25 to conclude angle DAC > angle EAC, and (5) combine to get DAB + DAC > BAC. The AI proof cites additional construction propositions (1.23 for angle construction, 1.3 for cutting off equal lengths), postulate P1 (for drawing lines), and common notions (CN2, CN3, CN5) for the arithmetic inequality reasoning, all of which Heath leaves implicit. Since heath_only is empty and all ai_only items are construction/axiom over-citations, this is a clear Case A granularity difference.

### 11.21
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided this classification as G (Granularity difference). Both proofs share the same logical backbone: (1) use XI.20 to show that at each base vertex the face angles exceed the corresponding base polygon angle, (2) use I.32 to establish that both sets of triangles have equal total angle sums, and (3) conclude by subtraction that the face angles at A are less than four right angles. The AI generalizes from Heath's three-face-angle case to a five-face-angle case with an interior point O, but this is a presentational generalization, not a different logical path. The ai_only citations (1.13, 1.15, CN5, D11.11, P1) are all postulates, definitions, common notions, or low-level supporting propositions that Heath uses implicitly without citation. Heath_only is empty, confirming the AI cites everything Heath cites plus additional granularity. This is a clear case of over-citation at a finer granularity level.

### 11.22
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same key backbone: constructing an auxiliary angle equal to one of the given angles at point H, cutting off a segment equal to the common side length, then using I.4 (SAS congruence) to equate a chord and I.24 (greater angle yields greater opposite side) to establish the needed inequality. Heath's proof constructs KHL equal to angle ABC and derives AC + GK > DF, noting 'similarly' for the other two inequalities. The AI proof takes the largest angle (GHK) first to dispatch two easy inequalities directly, then uses the same construction technique (angle GHL = angle BAC) to prove the critical inequality BC + EF > GK. The heath_only set is empty, confirming the AI cites every proposition Heath cites. The ai_only set consists entirely of construction and auxiliary propositions (1.3, 1.20, 1.22, 1.23, P1) that Heath uses implicitly but does not cite explicitly. This is a citation-depth difference with the same logical backbone, placing it squarely in the G category.

### 11.23
**Category**: Granularity difference
**Jaccard**: 0.190
**Analysis**: Q2 decided the classification. Both proofs share the same backbone of key intermediate conclusions: (1) constructing triangle LMN from the three angle bases via 11.22, (2) circumscribing a circle and finding its center O, (3) establishing that AB is greater than OL, (4) erecting a perpendicular at O and setting its square equal to the excess of AB-squared over OL-squared, (5) showing the resulting segments from the apex equal AB, and (6) proving the solid angle has the given plane angles via I.8. The large symmetric difference in citations (Jaccard 0.19) reflects different methods for proving subsidiary steps rather than different backbones. Heath proves AB > LO through a two-case contradiction using proportionality (VI.2, VI.4, V.16) and I.25/I.29, while the AI proves it by arguing that O must lie inside triangle LMN (using 1.13, 1.21) and then inferring AB > OL. Heath uses I.4 (SAS) to establish RL = RM, while the AI uses I.47 (Pythagorean theorem) directly. The AI also explicitly cites construction steps (P1, P3, 1.3, 4.5, 2.14) and definitions (D1.15, D11.3) that Heath leaves implicit. Since all key intermediate conclusions are the same and the differences are in citation depth and subsidiary argument methods, this is a granularity difference.

### 11.24
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: (1) establish all six faces are parallelograms using XI.16, (2) show corresponding sides of opposite faces are equal using I.34, (3) prove corresponding angles are equal using XI.10, (4) establish congruence of the triangles formed by diagonals using I.4 (SAS), and (5) conclude opposite faces are equal. The AI's two extra citations (1.29 and CN2) represent over-citation rather than a different path. CN2 is used explicitly to add equal triangles into equal parallelograms, where Heath uses I.34 to say each parallelogram is double of the respective triangle. I.29 is used to justify that supplementary angles are equal when their supplements are equal, a step Heath leaves implicit. Since the key intermediate conclusions are identical and the citation differences reflect only explicitness of minor steps, this is a granularity difference (G).

### 11.25
**Category**: Granularity difference
**Jaccard**: 0.154
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same equimultiple strategy: construct replicas of the parallelepiped to form equimultiples of the bases and solids, show the replicated solids are equal by XI.24, verify that the exceed/equal/fall-short relationship between base multiples carries over to solid multiples, and conclude by V. Def. 5 (D5.5) that base is to base as solid is to solid. The AI proof is more verbose and cites many additional foundational results (1.3, 1.34, 1.4, 11.16, 6.1, CN4, CN5, D11.1, D11.2, D11.8, P1) that Heath takes as implicit. The citation of 6.1 in Step 9 is a parenthetical observation not essential to the argument. Heath_only is empty, confirming the AI covers all of Heath's reasoning. The key intermediate conclusions are identical in both proofs, with the AI simply providing finer-grained justification for each step.

### 11.26
**Category**: Path difference
**Jaccard**: 0.333
**Analysis**: Q2 determined this classification. The two proofs construct the same solid angle but through structurally different methods. Heath drops a perpendicular from F to the plane through ED and DC, constructs angles BAL and BAK at A equal to EDC and EDG respectively, then uses three applications of I.4 (SAS) and one of I.8 (SSS) to establish the face angle equalities. The AI instead drops a perpendicular from E to the plane DFC, constructs perpendiculars from the foot G to edges DC and DF, uses 11.18 to establish perpendicularity of planes, D11.4 for line-plane perpendicularity, and employs I.26 (AAS congruence) rather than I.8 (SSS). The construction geometry differs (different perpendicular direction, different intermediate points), and the triangle congruence strategy differs (AAS vs SSS), yielding a genuinely different backbone. The AI's path is logically complete under Q3, with each step supported by cited propositions, so the classification is D.

### 11.27
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same backbone of key intermediate conclusions: (1) construct an equal solid angle at A corresponding to C, (2) establish proportional edges about the equal solid angles, (3) show corresponding faces are similar parallelograms, (4) conclude the solids are similar by D11.9. The difference lies in how proportions are established: Heath sets up two separate proportions (EC:CG=BA:AK and GC:CF=KA:AH) and derives the third via ex aequali (5.22), while the AI sets up all three proportions directly from a single common ratio AB:CE, avoiding the need for 5.22. The heath_only citation 5.22 appears inside Heath's proof of 6.24 (which the AI cites), satisfying the proof-tree containment test and confirming a citation-depth difference. The ai_only items (1.3, 1.31, 11.24, 11.26, 6.24, D6.1) are construction-level and definitional citations that Heath leaves implicit. Since both proofs reach the same geometric conclusions through the same logical backbone at different levels of citation granularity, this is a granularity difference.

### 11.28
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they cut the parallelepiped by a plane through the diagonals of opposite faces, use I.34 to show those diagonals bisect the faces into equal triangles, establish that the lateral faces of the two resulting prisms are equal (because opposite faces of the parallelepiped are equal), and conclude by D11.10 that the two prisms are equal. The AI additionally cites 11.24 explicitly to justify the equality of opposite faces, whereas Heath simply states this as a known fact ('for they are opposite'). The AI also cites D11.13 (definition of a prism) to identify each half as a prism, which Heath leaves implicit. Both ai_only items (11.24 and D11.13) represent over-citation of supporting facts that Heath takes for granted, making this a same-backbone, different-depth situation — Case A of Q2 — yielding Granularity difference (G).

### 11.29
**Category**: Path difference
**Jaccard**: 0.100
**Analysis**: Q2 determines the classification as D (Path difference). Heath's proof establishes equality by showing specific triangular and parallelogram faces of two prisms are congruent (using 1.8/1.4 for triangle congruence and 1.36 for parallelogram equality), then adds a common solid to obtain CM = CN. The AI proof takes a fundamentally different approach: it uses 11.28 to bisect each parallelepiped into triangular prisms via diagonal planes, introduces an auxiliary parallelepiped sharing features of both CM and CN, then shows corresponding prisms are equal using 1.37 (triangle area equality on same base between same parallels), concluding CM = auxiliary solid = CN. The key intermediate conclusions differ entirely: Heath's backbone is face congruence plus addition of a common solid, while the AI's backbone is diagonal-plane decomposition plus an auxiliary solid intermediary. The AI's path is logically valid under the hardened Q1(b) standard, with each step supported by cited propositions, so this is a genuine path difference rather than an error.

### 11.30
**Category**: Granularity difference
**Jaccard**: 0.111
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: construct an auxiliary parallelepiped by extending edges of the two given solids until they meet, show each original solid equals this auxiliary solid via XI.29 (since they share the same base and their standing edges terminate on the same straight lines), then conclude by transitivity that the two original solids are equal. The AI's additional citations (1.31, 1.34, 11.1, 11.24, CN1, D11.13, P1, P2) are all over-citations of construction tools, definitions, postulates, and common notions that Heath leaves implicit. Heath_only is empty, confirming no substantive steps are missing from the AI proof. This is a clear Case A in Q2: same backbone with different citation depth.

### 11.31
**Category**: Path difference
**Jaccard**: 0.333
**Analysis**: Q2 determines the classification. Heath's proof constructs a copy of one solid adjacent to the other, then uses geometric arguments with XI.29 (parallelepipeds with edges on same lines), I.35 (parallelogram equality), and V.11 (ratio transitivity) to show equality. The AI takes a fundamentally different path: it reduces both parallelepipeds to rectangular boxes via two applications of XI.30 (a re-orientation technique not in Heath), then proves the boxes equal using Book VI ratio arguments (6.1, 6.16) and ex aequali (5.22) -- propositions Heath does not use. The backbones differ at the level of key intermediate conclusions: Heath's intermediate is a constructed copy solid shown equal via geometric cutting and proportion transitivity, while the AI's intermediate is a pair of rectangular boxes shown equal via area-based proportion arguments. Both paths are logically complete, so Q3 confirms D.

### 11.32
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same backbone: construct a parallelogram FH equal to AE (by I.45), complete a parallelepiped GK on FH with the same height as CD, show AB equals GK by XI.31 (equal bases, same height), apply XI.25 to establish the ratio between the solids and their bases, then substitute equals to conclude AE:CF = AB:CD. The AI's three extra citations (11.27 for the parallelepiped construction, 5.7 and 5.11 for explicit ratio substitution steps) represent over-citation of steps that Heath performs implicitly without naming specific propositions. Since heath_only is empty and the ai_only items are all construction or ratio-manipulation propositions that merely make explicit what Heath leaves implicit, this is Case A of Q2: same key intermediate conclusions with different citation depth, yielding a Granularity difference.

### 11.33
**Category**: Path difference
**Jaccard**: 0.154
**Analysis**: Q2 reveals genuinely different backbones. Heath establishes the continuous proportion among four solids by first using 6.1 to relate parallelogram areas to edge ratios, then 11.32 to convert parallelogram ratios into solid ratios (AB:EO, EO:QL, QL:KP). The AI takes a fundamentally different route: it constructs different intermediate solids (EX and EY rather than Heath's EO and QL) and applies 11.25 directly three times to establish solid-to-solid ratios without passing through parallelogram ratios at all. The proof-tree containment test confirms this is not mere citation depth: while 11.32 does use 11.25 internally, Heath applies 11.32 to solids sharing the same height (comparing bases), whereas the AI applies 11.25 to cuts of combined solids (effectively comparing heights given the same base), producing a structurally different argument. Both paths validly reach the triplicate ratio via D5.10, making this a path difference rather than a granularity difference.

### 11.34
**Category**: Path difference
**Jaccard**: 0.455
**Analysis**: Q2 decided the classification. Both proofs construct an auxiliary parallelepiped and use proportion chains to establish the reciprocal relationship between bases and heights, but the specific constructions and intermediate conclusions differ substantively. Heath places the auxiliary solid CV on base NQ with height equal to AG and uses 6.1 (parallelograms under same height as bases) and 5.7 (equal magnitudes have same ratio) to establish intermediate ratios, while the AI places the auxiliary solid FO on base EH with height equal to CN and uses 11.25 (solid cut by parallel plane) for height ratios and 5.11/5.16 for ratio manipulation. The heath_only citations (11.30, 5.7, 6.1) do not appear inside the proofs of any AI-cited proposition, confirming this is not a containment/granularity difference but a genuinely different geometric path. The AI's path is logically valid under Q3: each step follows from cited propositions (the miscitation of 5.16 for inverse proportion is a naming error, not a logical gap, since the inversion operation is sound), and the proof covers both the forward direction and the converse.

### 11.35
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: Q2 determined this classification. Heath's proof works by drawing a line HK parallel to GL through a point H on the elevated line (using 11.8 to transfer perpendicularity), then uses 1.48 to establish right angles at C and F, applies 1.26 (AAS) repeatedly to derive equal segments, and ultimately reaches the conclusion via 1.8 (SSS). The AI proof takes a fundamentally different path: it constructs AB = DE and AC = DF directly on the rays (using 1.3), establishes congruence of multiple triangle pairs via 1.4 (SAS) and 1.8 (SSS), then proves the critical equality GH = MN through an innovative area-based contradiction argument using 1.41, showing that unequal perpendicular heights would force unequal triangle areas, contradicting the established equality. The key intermediate conclusions differ substantially -- Heath's backbone involves perpendiculars to the sides of the angle and AAS congruence (1.26), while the AI's backbone involves an area decomposition and proof by contradiction. Since the AI's different path is logically sound, the classification is D.

### 11.36
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 reveals fundamentally different proof backbones, leading to classification D at Q3. Heath's proof directly constructs two parallelepipeds with the given edges and shows they have equal bases (via reciprocal proportionality, VI.14) and equal heights (via XI.35 Porism), then concludes equality by XI.31. The AI proof takes an entirely different ratio-based approach: it introduces an intermediate solid Q with edges A, B, B, uses XI.32 and VI.1 to establish the ratios S:Q = C:B and Q:P = A:B, then applies ex aequali (V.22) to obtain S:P = B:B, concluding S = P by V.9. The citation sets are completely disjoint (Jaccard = 0.0), reflecting genuinely different mathematical strategies rather than mere differences in citation depth. The AI's ratio-chain approach is logically complete and valid, satisfying Q3(b).

### 11.37
**Category**: Granularity difference
**Jaccard**: 0.143
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same backbone: they use XI.33 to establish that similar parallelepipedal solids are in the triplicate ratio of their corresponding sides, then in the forward direction conclude that equal base ratios yield equal solid ratios, and in the converse that equal solid ratios yield equal base ratios. Heath's proof is extremely concise, treating the triplicate ratio relationship as a direct consequence of XI.33 in both directions. The AI proof makes the triplicate ratio construction explicit by building continuous proportions via 6.11 and D5.10, chains proportions using 5.11 and 5.22 (ex aequali), and uses proof by contradiction via 5.8 for the converse direction. Despite the AI's more elaborate machinery and different technique in the converse, the key intermediate conclusions are the same: the triplicate ratio of side ratios determines the solid ratios (forward) and vice versa (converse). The ai_only citations (5.11, 5.22, 5.8, 6.11, D5.10, D5.9) represent over-citation of proportion-theory results that Heath leaves implicit, and heath_only is empty, confirming that no substantive step present in Heath is absent from the AI proof.

### 11.38
**Category**: Path difference
**Jaccard**: 0.188
**Analysis**: Q2 decided the classification as D (Path difference). Heath's proof works by showing DUE and BSG are collinear straight lines (via I.4 SAS congruence and I.14), establishing DB parallel to EG (via XI.9 transitivity of parallelism), then proving DE parallel to BG (via I.33), and finally using AAS triangle congruence (I.26) on triangles DTU and GTS to conclude DT=TG and UT=TS. The AI proof takes a fundamentally different approach: it identifies the intersection points S and T as the centers of opposite faces of the cube, constructs the cross-sectional parallelogram ASTG (using I.34, 11.24, 6.2, and I.33), and concludes that since AG and ST are diagonals of parallelogram ASTG, they bisect each other (via I.29 alternate angles and I.26 triangle congruence). The key intermediate conclusions differ substantially: Heath never constructs parallelogram ASTG, and the AI never establishes collinearity of DUE or the parallelism DB to EG via XI.9. Both paths are logically complete, yielding a valid path difference.

### 11.39
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: complete both prisms to parallelepipeds, show their bases are equal (since both are double the given triangle), conclude the parallelepipeds are equal by XI.31, then conclude the prisms are equal since each is half its parallelepiped by XI.28. The AI's three extra citations (CN1, CN2, D11.13) are all common notions and a definition that Heath leaves implicit. CN1 makes explicit the transitivity step equating the two parallelogram bases, CN2 makes explicit the inference that halves of equal things are equal, and D11.13 cites the definition of a prism. Since heath_only is empty and ai_only contains only axiom-level items, this is a clear case of over-citation at the same logical depth, yielding a granularity difference.
