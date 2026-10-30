# Book 13 — Classification Report (Fable)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 0 |  |
| Granularity difference (G) | 12 | 13.3, 13.6, 13.8, 13.9, 13.10, 13.11, 13.13, 13.14, 13.15, 13.16, 13.17, 13.18 |
| Path difference (D) | 6 | 13.1, 13.2, 13.4, 13.5, 13.7, 13.12 |
| AI proof error (E) | 0 |  |

**Total**: 18 propositions

## Per-Proposition Analysis

### 13.1
**Category**: Path difference
**Jaccard**: 0.154
**Analysis**: Q2 decided the classification. Heath's proof constructs geometric squares and a gnomon figure, using VI.1 (triangles under the same height are proportional to their bases) to establish that CK is double CH, then shows the whole square AE equals the gnomon MNO, and derives the 5:1 ratio through gnomon arithmetic. The AI proof takes a fundamentally different algebraic route using Book II area identities: it applies 2.2 to get rect(AB,AC) + sq(AC) = sq(AB), applies 2.4 to decompose sq(DC) into sq(DA) + sq(AC) + 2*rect(DA,AC), uses 2.1 to show rect(AB,AC) = 2*rect(DA,AC), and uses 2.4 again to show sq(AB) = 4*sq(AD), then combines these to reach sq(DC) = 5*sq(AD). The two proofs share only the initial step of converting the extreme-and-mean-ratio definition into rect(AB,CB) = sq(AC) via D6.3 and 6.17; after that, the key intermediate conclusions diverge entirely. Heath's use of VI.1 for proportional areas within a constructed figure has no counterpart in the AI proof, and the AI's Book II decompositions have no counterpart in Heath. This is a genuine path difference (Case B in Q2), and Q3 confirms the AI's path is logically complete and valid.

### 13.2
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q1 found no logical errors in the AI proof; every step follows validly from the preceding ones. Q2 identified different backbones (Case B): Heath proves rect(CD,DB) = CB squared through a geometric construction involving squares AF and CG, gnomon area manipulations, and the proportionality result VI.1 (triangles under the same height are proportional to their bases), while the AI derives the same key equality entirely through algebraic identities from Book 2 (II.4 for expanding squares of sums, II.1 for distributing rectangles, II.2 for another rectangle decomposition), plus an explicit proof by contradiction that CB < CD. The completely disjoint citation sets (Jaccard = 0.0) confirm the path divergence: Heath uses none of the Book 2 propositions, and the AI uses none of Heath's geometric proportionality machinery. Q3 verified that the AI's algebraic chain is logically complete, so the classification is D (path difference).

### 13.3
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs establish the same three key intermediate conclusions in the same logical order: (1) rect(AB,BC) = sq(AC) from the extreme and mean ratio property, (2) sq(AC) = 4*sq(DC) since AC = 2*DC, and (3) sq(DB) = rect(AB,BC) + sq(DC), combining to yield sq(DB) = 5*sq(DC). Heath reaches these through geometric area manipulation within a constructed figure (gnomons and square regions), while the AI cites explicit propositions (6.17, 2.4, 2.6) for the same steps. The Jaccard of 0.0 is an artifact of Heath's proof having no extracted references; all AI citations (1.10, 2.4, 2.6, 6.17, CN1, CN2, D1.22, D6.3) make explicit what Heath uses implicitly, constituting a citation-depth difference rather than a path divergence.

### 13.4
**Category**: Path difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the initial key conclusion that rect(AB,BC) = sq(AC) via the golden ratio definition and 6.17, but their backbones diverge after that point. Heath constructs the square on AB and argues through a gnomon decomposition of areas within the figure, while the AI takes a purely algebraic route using 2.3 to decompose rect(AB,CB) into rect(AC,CB) + sq(CB), then 2.4 to expand sq(AB), and substitutes to reach the triple relation. The AI's intermediate conclusion rect(AC,CB) + sq(CB) = sq(AC) has no counterpart in Heath, and Heath's gnomon argument has no counterpart in the AI proof. Since the backbones differ and the AI's algebraic path is logically complete and valid (Q3), the classification is D.

### 13.5
**Category**: Path difference
**Jaccard**: 0.286
**Analysis**: The classification hinges on Q2 (backbone comparison). Heath's proof converts the extreme-and-mean-ratio proportion into an area equality via 6.17, constructs a square on AB and manipulates the resulting rectangles geometrically (showing rect(BD,DA) = sq(AB) through figure-based area additions), then converts back to a proportion using 6.17. The AI proof stays entirely within the domain of proportions, applying Book 5 ratio manipulations -- inversion (5.7 Porism), transitivity (5.11), and componendo (5.18) -- to transform the initial EMR proportion AB:AC :: AC:CB directly into the target proportion DB:AB :: AB:AD without ever passing through areas. These are genuinely different key intermediate conclusions: Heath argues through area equalities (rect(AB,BC)=sq(AC) and rect(BD,DA)=sq(AB)), while the AI argues through intermediate ratio chains (AC:AB :: CB:AC, then AD:AB :: CB:AC, then DB:AB :: AB:AC). The AI's purely proportional path is logically complete and valid, warranting classification as D (Path difference).

### 13.6
**Category**: Granularity difference
**Jaccard**: 0.533
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions in the same order: sq(CD) = 5*sq(DA) via 13.1, commensurability of sq(CD) and sq(DA) via 10.6, rationality of DA and CD, incommensurability of CD and DA in length via 10.9, AC is an apotome via 10.73, rect(AB,BC) = sq(AC) via 6.17, and CB is a first apotome via 10.97. The backbones are identical. The AI proof adds over-citations for construction steps (1.10, 1.3), a postulate (P2), definitions (D10.1.2, D10.1.3, D10.3.1), and one intermediate result for transitivity of commensurability (10.12), all of which Heath leaves implicit. Since heath_only is empty, every proposition Heath cites also appears in the AI proof. This is Case A of Q2: same backbone, different citation depth, yielding G.

### 13.7
**Category**: Path difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Heath's Case 1 proof works by joining diagonals AC and BE, showing they are equal (I.4), then using their intersection point F to derive AF=BF via I.6 (converse of the isosceles triangle theorem), subtracting to get FC=FE, and applying I.8 on triangles FCD and FED. The AI's Case 1 proof takes a fundamentally different route: it joins AC, BD, and AD, shows AC=DB via I.4 on triangles ABC and DCB, then applies I.8 on triangles ACD and DBA to get angle CDA = angle BAD, invokes I.5 on triangle EAD, and adds equal angles via CN2 to conclude angle CDE = angle BAE. The AI never introduces the intersection point F and never uses I.6, instead relying on a different set of triangle congruences (I.8 applied to different triangle pairs) combined with the isosceles triangle theorem (I.5) and angle addition (CN2). Heath's unique citation I.6 reflects a genuinely different logical backbone, not mere citation-depth variation. The AI's second case also differs: it reduces the non-consecutive case to the consecutive case by showing angle C = angle B, whereas Heath proves the non-consecutive case independently using I.4 and I.5 on different triangles. Both proofs are logically complete, covering both required cases, but through different key intermediate conclusions.

### 13.8
**Category**: Granularity difference
**Jaccard**: 0.444
**Analysis**: Q2 decided the classification. Both proofs share identical key intermediate conclusions: BE=AC by I.4, angle AHE = 2*angle BAH by I.32, angle EAC = 2*angle BAC, HE=EA=AB by I.6, triangles ABE and ABH equiangular yielding EB:BA=AB:BH by VI.4, and BE:EH=EH:HB with V.14 giving extreme and mean ratio. The sole heath_only citation (VI.33) passes the proof-tree containment test: III.27, which the AI cites instead, appears inside Heath's proof of VI.33, so the AI re-derives the needed special case from the more elementary equal-arc-equal-angle result rather than invoking the general proportionality theorem. The remaining ai_only items are Common Notions (CN1, CN2, CN3, CN5), a definition (D6.3), a postulate (P1), and proportion-manipulation lemmas (5.7, 5.11) that Heath applies implicitly. The AI also explicitly proves the AC case (Steps 11-12) where Heath says 'similarly'. All differences are citation-depth differences within the same logical backbone, yielding G.

### 13.9
**Category**: Granularity difference
**Jaccard**: 0.278
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions in the same order: arc AC equals four times arc CB, angle AEC equals four times angle CEB (via 6.33), angle AEC equals twice angle ECB (via 1.5 and 1.32), EC equals CD as both equal the radius (via 4.15), angle ECB equals twice angle EDC (via 1.5 and 1.32), angle EDC equals angle BEC, triangles EBD and EBC are equiangular, DB:BE equals EB:BC (via 6.4), and BD:DC equals DC:CB by substituting EB for CD. The logical backbone is the same in both proofs. The AI's 13 extra citations (ai_only) are entirely construction propositions (3.1, P1, P2), definitions (D1.15, D1.17, D6.3), common notions (CN1, CN3, CN5), and auxiliary proportion results (3.28, 5.7, 5.11, 5.14) that Heath leaves implicit. The heath_only set is empty, confirming the AI cites everything Heath does plus additional granularity. This is Case A of Q2: same backbone, different citation depth.

### 13.10
**Category**: Granularity difference
**Jaccard**: 0.409
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they establish arc relationships showing AK is a decagon side, derive angle relationships leading to triangle ABF being similar to triangle BFN (yielding rect(AB,BN) = sq(BF)), prove triangle KBA similar to triangle KNA (yielding rect(BA,AN) = sq(AK)), and combine these via II.2 to reach sq(AB) = sq(BF) + sq(AK). The key intermediate conclusions are identical at every stage. The citation differences are purely depth-related: the AI's 12 additional citations (1.12, 3.1, 3.28, 3.29, 3.3, CN1-3, D1.10, D1.17, P1, P2) are all construction propositions, basic circle theorems, common notions, definitions, and postulates that Heath uses implicitly. The sole heath_only citation (1.26, ASA congruence) is replaced by the AI's use of 1.4 (SAS congruence) at the same logical position to reach the same conclusion (angle AFK = angle KFB), a micro-level substitution of congruence criteria that does not alter the backbone. This is Case A of Q2: same backbone, different citation depth.

### 13.11
**Category**: Granularity difference
**Jaccard**: 0.209
**Analysis**: Q2 decided the classification. Both proofs establish the same sequence of key intermediate conclusions: FK=AF/4 with FK and BK rational, right angles at L and M with CD=2CL and AC=2CM, triangles ACL and AMF equiangular, the proportion DC:CM=MF:FK, componendo to (DC+CM):CM=MK:KF, the ratio of squares, sq(MK)=5*sq(KF) via XIII.8 and XIII.1, MK rational, sq(BK)=5*sq(MK) with BK incommensurable in length with KM, MB as a fourth apotome via X.73, and finally sq(side)=BH*BM yielding the side as minor via X.94. The two heath_only citations (10.15 and 5.19) are sub-step tools whose underlying conclusions appear in both proofs at the same logical positions: Heath uses X.15 to show BK commensurable with BH while the AI establishes this directly via arithmetic (BK=5FK, FK measures BH), and Heath uses V.19 (convertendo) while the AI computes sq(BK)-sq(MK)=4*sq(MK) directly. The 32 ai_only items are overwhelmingly construction propositions, definitions, postulates, common notions, and lower-level ratio tools that fill in steps Heath leaves implicit. This is Case A: same backbone, different citation depth.

### 13.12
**Category**: Path difference
**Jaccard**: 0.111
**Analysis**: Q2 decided the classification. Both proofs reach the same ultimate conclusion (AB^2 = 3DE^2) and share the final algebraic steps (angle ABE right via 3.31, Pythagorean theorem via 1.47, AE^2 = 4DE^2). However, the key intermediate lemma BE = DE is established through fundamentally different mathematical techniques: Heath uses arc reasoning and the hexagon property (4.15), showing that arc BE is 1/6 of the circle so BE equals the radius, while the AI uses angle-at-center reasoning (3.20, 1.13, 1.5, 1.6, 1.32), showing through angle-chasing that triangle BDE has all angles equal to angle ACB and therefore BE = DE. The containment test fails because the AI does not cite a higher-level proposition subsuming 4.15 but instead employs entirely different geometric concepts (central angles vs. arcs/hexagons). The AI's sub-proof tools (3.20, 1.13, 1.6) are largely absent from Heath's proof of 4.15 (which uses 3.26, 3.27, 3.29, 1.15). Since the backbones diverge in their indispensable intermediate facts, this is Case B (different backbone). Q3 confirms the AI's path is logically complete and valid, yielding D.

### 13.13
**Category**: Granularity difference
**Jaccard**: 0.258
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same backbone of key intermediate conclusions: cutting the diameter so AC = 2CB, establishing sq(AD) = 3 sq(CD) via the semicircle construction, inscribing equilateral triangle EFG in a circle of radius CD, using XIII.12 to show AD = EF, proving all six edges equal via I.4 to construct the pyramid, comprehending it in the sphere with diameter KL = AB, and proving the 3:2 ratio of squares. The AI's 22 extra citations are overwhelmingly over-citations: postulates (P1-P4), common notions (CN1, CN2), definitions (D1.15, D11.12, D11.14, D11.17), construction propositions (1.1, 1.3, 1.10, 1.11), and elementary results (1.5, 1.6, 1.13, 6.9) that Heath leaves implicit. The AI's use of II.5 and I.47 for the sphere-comprehension argument (versus Heath's more compact VI.8/III.31 approach) and 6.1/6.4 for explicit proportion steps represent sub-argument detail, not a different logical path. The sole heath_only item (III.1, finding the center of a circle) is avoided because the AI constructs the circle with center H from the start rather than finding the center afterward. All key conclusions appear at the same logical positions in both proofs.

### 13.14
**Category**: Granularity difference
**Jaccard**: 0.160
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: constructing square EFGH with side equal to DB, erecting perpendiculars KL and KM from the center K, using I.47 to show sq(EH) = 2*sq(EK) and sq(LE) = 2*sq(EK) hence LE = EH, concluding all eight triangles are equilateral to form the octahedron, comprehending it in a sphere via semicircle rotation (KL=KM=KE), then establishing sq(LM) = 2*sq(LE) via III.31 and I.47, and sq(AB) = 2*sq(DB) to conclude LM = AB. The heath_only set is empty, meaning every proposition Heath cites (I.4, I.47, XI.12, III.31) is also cited by the AI. The ai_only set consists entirely of postulates (P1, P2, P3), definitions (D1.15, D1.17, D1.18, D1.20, D1.22, D11.14, D11.17, D11.26, D11.3), common notion (CN1), and basic construction and triangle propositions (1.3, 1.5, 1.6, 1.8, 1.10, 1.11, 1.32, 1.46), all of which are elementary steps that Heath uses implicitly. The AI's slightly different sub-derivation of sq(AB) = 2*sq(DB) (using I.4 to show AD = DB directly, rather than Heath's proportional route) reaches the same key conclusion and does not alter the backbone. This is Case A: same backbone, different citation depth.

### 13.15
**Category**: Granularity difference
**Jaccard**: 0.065
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: setting up the diameter and establishing sq(AB) = 3*sq(BD) via the semicircle construction, constructing the cube with side equal to DB, proving all eight vertices lie on a sphere with diameter KG by showing each angle subtended at a vertex is right, proving sq(KG) = 3*sq(EF) via the Pythagorean theorem, and concluding KG = AB. The heath_only set is empty, meaning Heath's two citations (I.47 and XI.Def.3) are a strict subset of the AI's 31 citations. The AI's 29 additional citations are all postulates (P1, P3), definitions (D1.18, D1.22, D1.23, D11.14, D11.17, D11.25, D5.5, D5.9), common notions (CN1), construction propositions (1.3, 1.10, 1.11, 1.46), Book 11 solid geometry fundamentals (11.4, 11.6, 11.7, 11.9, 11.10, 11.12), and standard theorems (1.28, 1.29, 1.33, 3.31, 5.11, 6.8, 6.9, 6.20) that Heath invokes implicitly. This is Case A of Q2: same backbone, different citation depth.

### 13.16
**Category**: Granularity difference
**Jaccard**: 0.231
**Analysis**: Q2 decided the classification. Both proofs construct the icosahedron through identical key intermediate conclusions: cutting the diameter so the square on AB equals five times the square on BD, inscribing the pentagon and decagon in a circle of radius DB, raising perpendiculars to form the upper pentagon QRSTU, applying XIII.10 (the pentagon-hexagon-decagon relation) to verify that all connecting edges equal the pentagon side, constructing the 20 equilateral triangles in three bands (10 middle, 5 upper cap at Z, 5 lower cap at X), using XIII.9 and XIII.3 to establish the extreme-and-mean-ratio property for the sphere comprehension, proving XZ equals AB so the sphere matches the given sphere, and finally applying XIII.11 to classify the side as minor. The large ai_only set (29 items) consists entirely of postulates, common notions, definitions, and elementary construction or foundational theorems that Heath invokes without explicit citation. The sole heath_only item D5.9 (V. Def. 9, duplicate ratio) is a definition the AI covers through its direct use of 6.8. The identical logical backbone with differing citation depth places this squarely in Case A of Q2, yielding G.

### 13.17
**Category**: Granularity difference
**Jaccard**: 0.267
**Analysis**: Q2 decided the classification. Both proofs share an identical backbone: constructing a regular pentagon on a cube edge by bisecting sides, cutting segments in extreme and mean ratio, erecting perpendiculars, then proving the pentagon equilateral (via XIII.4, I.47), coplanar (via VI.32, XI.1), equiangular (via I.8, XIII.7), extending to all twelve edges for the dodecahedron, comprehending it in the sphere (via XI.38, XIII.15), and showing the side is an apotome (via V.15, XIII.6). heath_only is empty, meaning the AI cites every proposition Heath does. The 33 ai_only items consist entirely of definitions, common notions, postulates, basic construction propositions (1.3, 1.10, 1.29, 1.30, 1.33, 1.34, 6.30, 11.12), elementary computational and ratio results (2.4, 5.7, 5.11, 5.14), spatial propositions (11.7, 11.9), and one substantive reference (10.6) used to explicitly justify that the cube side is rational, a fact Heath also establishes at the same logical position but without naming the proposition. This is a pure over-citation pattern where the AI makes explicit every foundational step that Heath leaves implicit, yielding Case A of Q2: same backbone, different citation depth.

### 13.18
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs construct and identify the sides of all five Platonic solids inscribed in a sphere of diameter AB through the same sequence of key intermediate conclusions: AF as the pyramid side (via sq(AB) = 1.5 sq(AF) and 13.13), BF as the cube side (via sq(AB) = 3 sq(BF) and 13.15), BE as the octahedron side (via sq(AB) = 2 sq(BE) and 13.14), KL as the icosahedron-circle radius and hexagon side (via sq(AB) = 5 sq(KL) and 13.16), AK and LB as decagon sides, MB as the icosahedron side (via 13.10 and 13.16), and NB as the dodecahedron side (via 13.17). The comparison section and the proof that MB > NB follow the same logical chain. The heath_only set is empty, meaning every reference Heath cites is also cited by the AI. The 24 ai_only items are entirely construction propositions (1.10, 1.11, 1.12, 1.3), postulates (P1, P3, P4), common notions (CN1, CN2, CN3, CN5), definitions (D1.15, D1.18, D5.5, D5.9, D6.3, D10.1.2, D10.1.3), and elementary propositions (1.32, 1.47, 3.31, 6.17, 6.30, 6.9, 10.13) that Heath uses implicitly but does not cite. This is a clear Case A: same backbone, different citation depth.
