# Book 11 — Classification Report (RunA)

## Summary

| Category | Count | Propositions |
|---|---|---|
| Perfect match (P) | 2 | 11.11, 11.15 |
| Granularity difference (G) | 28 | 11.1, 11.2, 11.3, 11.4, 11.5, 11.6, 11.8, 11.9, 11.10, 11.12, 11.13, 11.14, 11.16, 11.17, 11.19, 11.20, 11.21, 11.22, 11.23, 11.24, 11.25, 11.27, 11.28, 11.30, 11.32, 11.34, 11.37, 11.39 |
| Path difference (D) | 8 | 11.7, 11.18, 11.26, 11.29, 11.33, 11.35, 11.36, 11.38 |
| AI proof error (E) | 1 | 11.31 |

**Total**: 39 propositions

## Error Details

| Proposition | Error type | Details |
|---|---|---|
| 11.31 | Invalid inference | CANDIDATE E — 11.31   violated_claim : In Step 5, the AI applies 11.29/11.30 (which require solids on 'the same base') to solids AB (on base FGHK) and RS (on base FGPQ), which are on different (though |

## Per-Proposition Analysis

### 11.1
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: assume for contradiction that part AB of line ABC lies in the reference plane while part BC is elevated, construct a line BD continuing AB within the reference plane, then derive a contradiction from the fact that the extension of AB beyond B is unique (so BC and BD must coincide, yet one is in the plane and the other is not). Heath arrives at this contradiction via an implicit common-segment impossibility argument citing no explicit references, while the AI explicitly invokes D1.4 (straight line lies evenly with its points), D1.7 (plane surface lies evenly with straight lines on itself), and P2 (finite straight line can be produced) to justify the same uniqueness conclusion. Since heath_only is empty and ai_only contains only definitions and a postulate, this is a classic Case A granularity difference: same key intermediate conclusions, different citation depth.

### 11.2
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: they use a contradiction argument via XI.1 to establish that triangle ECB is in one plane, then extend this to show the full lines AB and CD lie in that plane, and finally generalize to show every triangle is in one plane. The AI's ai_only citations (P1, P2) are postulates cited for construction steps (drawing straight lines and extending lines), which Heath uses implicitly without citation. The heath_only set is empty, confirming no substantive propositions are missing from the AI proof. This is a classic over-citation pattern where the AI explicitly references basic postulates that Heath takes for granted, making it a granularity difference rather than a path difference.

### 11.3
**Category**: Granularity difference
**Jaccard**: 0.000
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs use the same reductio ad absurdum backbone: assume the common section is not straight, draw two distinct straight lines DEB and DFB from D to B in the respective planes, observe that two straight lines would enclose a space (absurd), and conclude the common section must be straight. The AI proof adds explicit citations to P1 (drawing straight lines), D1.4 (definition of straight line), and 11.1 (a line joining two points in a plane lies entirely in that plane) where Heath's proof cites nothing at all, leaving these foundational steps implicit. Since heath_refs is empty and all ai_only items are either postulates, definitions, or an early proposition making explicit what Heath assumes, this is a citation-depth difference with the same logical backbone, satisfying Case A of Q2.

### 11.4
**Category**: Granularity difference
**Jaccard**: 0.455
**Analysis**: Q2 decided this classification as G (granularity difference). Both proofs share the same logical backbone: they set up equal segments AE=EB and CE=ED from E, draw an arbitrary line GEH through E, and then establish the chain of equalities GE=EH, AG=BH, FA=FB, FC=FD, FG=FH, culminating in angle GEF = angle HEF via I.8 to prove EF is perpendicular to the arbitrary line and hence to the plane. The AI uses a symmetrically equivalent triangle pair (AEC/BED yielding AC=BD) compared to Heath (AED/CEB yielding AD=CB), and routes through triangles GCF/HDF rather than Heath's implicit FAG/FBH path, but these are minor presentational variations that establish the same key intermediate conclusions. The ai_only set consists entirely of construction references (1.3, P1, 11.2), axioms/common notions (CN3, P4), and a definition (D1.10) that Heath uses implicitly but does not cite. The heath_only set is empty, confirming the AI cited a superset of Heath's references. This is a citation-depth difference, not a backbone difference.

### 11.5
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs employ the same proof-by-contradiction backbone: assume one of the three lines is not in the plane determined by the other two, use 11.4 to establish that AB is perpendicular to that plane, use 11.3 to find the common section line BF of two intersecting planes, invoke D11.3 to conclude that angle ABF is right, note the given right angle with the assumed-out-of-plane line, and derive a contradiction from the impossibility of two equal right angles on distinct lines in one plane. The AI proof differs only in explicitly citing P4 (to equate the right angles) and CN5 (whole greater than part, for the contradiction), which Heath leaves implicit by simply stating 'which is impossible.' Since heath_only is empty and ai_only contains only axiom-level citations (P4, CN5) that make explicit what Heath's proof uses implicitly, this is Case A of Q2: same backbone, different citation depth, yielding Granularity difference (G).

### 11.6
**Category**: Granularity difference
**Jaccard**: 0.231
**Analysis**: Q2 decided the classification. Both proofs establish the same key intermediate conclusions: (1) AD = BE, (2) angle ADE is right, (3) BD, DA, DC are coplanar via XI.5, (4) AB parallel to CD via I.28. The difference lies in citation depth: Heath uses I.4 (SAS) to show AD = BE and I.8 (SSS) to transfer the right angle, while the AI uses I.47 (Pythagorean theorem) and I.48 (its converse) to reach the same conclusions via metric computation. The proof-tree containment test confirms that I.4 appears inside Heath's proof of I.47 and I.8 appears inside Heath's proof of I.48, so the AI cites higher-level results that subsume the lower-level tools Heath deploys. The AI's remaining ai_only items (1.11, 1.3, P1, P4, CN1) are construction props, postulates, and common notions, indicating over-citation. Heath's citation of 11.2 (every triangle is in one plane) is handled informally by the AI in Step 12 without explicit citation, a minor under-citation. Since the backbone conclusions are the same and the citation differences are explained by depth, this is a granularity difference.

### 11.7
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: Q2 determined this classification. Heath's proof argues by contradiction using 11.3: assuming the joining line EGF is in a more elevated plane, a plane through EGF intersects the reference plane in a straight line EF (by 11.3), producing two distinct straight lines between the same endpoints that enclose an area, which is impossible. The AI proof takes a fundamentally different path: it establishes that both endpoints E and F lie in the plane P (since they lie on the parallel lines which are in P by D1.23), then argues by contradiction using 11.1 that if EF were not entirely in P, part would be in P and part elevated, directly contradicting 11.1. The key intermediate conclusions differ — Heath's pivotal step is constructing a planar section via 11.3 to get two lines between the same points, while the AI's pivotal step is showing both endpoints are in the plane and invoking 11.1 to force the entire line into the plane. Both arguments are logically complete and valid, but they proceed through different geometric reasoning, yielding a Jaccard of 0.0 with entirely disjoint citation sets.

### 11.8
**Category**: Granularity difference
**Jaccard**: 0.364
**Analysis**: Q2 decided the classification as G (granularity difference). Both proofs share the same backbone of key intermediate conclusions: (1) angle CDB is right via I.29 and the parallel lines, (2) AD equals BE, (3) angle ADE/EDA is right so ED is perpendicular to AD, (4) ED is perpendicular to the plane through BD and DA via XI.4, (5) CD lies in that plane, and (6) CD is perpendicular to the plane of reference via XI.4 again. The difference lies in how certain intermediate results are derived: Heath uses implicit SAS and SSS triangle congruence (I.4 and I.8, which are not even in his citation list) to establish AD = BE and angle EDA = right, while the AI uses the Pythagorean theorem (I.47) and its converse (I.48) to reach those same conclusions. The ai_only set {1.11, 1.3, 1.47, 1.48, CN1, P1} consists of construction/postulate over-citations (1.11, 1.3, P1, CN1) and the Pythagorean approach (1.47, 1.48), while the heath_only item {11.2} is used by Heath to place CD in the plane through BD and DA, which the AI handles through 11.7 at Step 13 to the same effect. Since all key conclusions are the same and the differences are purely in citation depth and auxiliary lemma choice, this is Case A of Q2.

### 11.9
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct perpendiculars GH and GK to EF in the respective planes, show EF is perpendicular to the plane through GH and GK (11.4), use parallelism to transfer perpendicularity to AB and CD (11.8), then conclude AB is parallel to CD (11.6). The AI adds two extra citations not in Heath: 1.11 (explicitly citing the construction of perpendiculars, which Heath performs implicitly) and 1.29 (establishing that GH is perpendicular to AB and GK is perpendicular to CD via parallel line properties, an intermediate step Heath does not include). These are over-citations providing additional granularity on the same argument, not a different proof path. Since heath_only is empty and the ai_only items are construction and supporting propositions that elaborate the same backbone at finer detail, this is Case A of Q2: same backbone, different citation depth.

### 11.10
**Category**: Granularity difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: cut off equal segments on the meeting lines, show that two auxiliary segments (AD/GD and CF/HF) are each equal and parallel to BE via I.33, conclude those two auxiliary segments are parallel and equal to each other via XI.9 and transitivity, then show the bases (AC/GH and DF) are equal and parallel via I.33, and finally conclude the angles are equal by SSS (I.8). The AI proof is structurally identical to Heath's but explicitly cites additional foundational items that Heath uses implicitly: I.3 for cutting off equal segments, XI.7 for establishing coplanarity of parallel lines, CN1 for transitivity of equality, and P1 for joining lines. Since heath_only is empty and all ai_only items are construction, axiomatic, or auxiliary citations present implicitly in both proofs, this is Case A of Q2: same backbone, different citation depth.

### 11.11
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof of proposition 11.11 follows the exact same logical structure as Heath's proof, establishing identical key intermediate conclusions in the same order: (1) BC is at right angles to the plane through ED and DA via 11.4, (2) GH is at right angles to that same plane via 11.8 since GH is parallel to BC, (3) GH is at right angles to AF via D11.3, (4) AF is at right angles to both GH and DE, and (5) AF is therefore at right angles to the reference plane via 11.4. The citation sets are identical (ai_used = heath_refs = {1.11, 1.12, 1.31, 11.4, 11.8, D11.3}) with Jaccard similarity 1.0, and both proofs share the same backbone of key conclusions. Since both the logical backbone and the citation sets match exactly, the classification is Perfect match (P).

### 11.12
**Category**: Granularity difference
**Jaccard**: 0.600
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: conceive an elevated point B, draw BC perpendicular to the plane via 11.11, draw AD parallel to BC through A via 1.31, and conclude AD is perpendicular to the plane via 11.8. The AI proof adds two over-citations (D11.3 for the definition of perpendicularity to a plane, and P1 for drawing a line), which are a definition and a postulate respectively, and also handles a trivial special case where the foot of the perpendicular coincides with A. Since heath_only is empty and ai_only contains only definitional/postulatory items, this is a classic Case A granularity difference: same backbone, different citation depth.

### 11.13
**Category**: Granularity difference
**Jaccard**: 0.400
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs follow the same logical backbone: assume two perpendiculars AB, AC from point A to a plane, establish their coplanarity, find the intersection line DAE of the two planes via 11.3, show both angles with DAE are right via D11.3, then derive a contradiction. The AI proof explicitly cites 11.2 (two intersecting lines are in one plane), P4 (all right angles are equal), and CN5 (the whole is greater than the part) to justify steps that Heath leaves implicit. Since heath_only is empty and the three ai_only items (11.2, CN5, P4) are a construction proposition, a common notion, and a postulate that make explicit what Heath takes for granted, this is a same-backbone, different-depth case — classic granularity difference.

### 11.14
**Category**: Granularity difference
**Jaccard**: 0.667
**Analysis**: Q2 decided the classification. Both proofs follow the same backbone: assume the planes are not parallel, derive a common section line (11.3), pick a point on it to form a triangle with the endpoints of the perpendicular line, show both base angles are right using D11.3 (perpendicularity to each plane), and reach a contradiction via 1.17 (two angles of a triangle must be less than two right angles). The AI proof adds two extra citations not in Heath: P1 (to justify joining points) and 11.2 (to justify the triangle lies in one plane). These are construction-level and supporting-detail over-citations that do not alter the logical backbone. Heath's proof omits these as implicit. Since the key intermediate conclusions match at every logical position and the citation differences reflect only depth of justification, this is a granularity difference (G).

### 11.15
**Category**: Perfect match
**Jaccard**: 1.000
**Analysis**: The AI proof and Heath's proof of proposition 11.15 follow an identical logical backbone: construct BG perpendicular to the plane through DE, EF (11.11), draw parallels GH to ED and GK to EF in that plane (1.31), establish right angles BGH and BGK via the definition of perpendicularity to a plane (D11.3), use transitivity of parallels (11.9) to show AB is parallel to GH and BC to GK, apply the co-interior angle theorem (1.29) to deduce that angles GBA and GBC are right, conclude GB is perpendicular to the plane through AB, BC (11.4), and finally invoke that planes perpendicular to the same line are parallel (11.14). The citation sets are exactly identical with Jaccard similarity 1.0, and the key intermediate conclusions match perfectly. Since ai_used equals heath_refs exactly and both proofs argue through the same intermediate steps, the classification is P (Perfect match).

### 11.16
**Category**: Granularity difference
**Jaccard**: 0.250
**Analysis**: Q2 decided this classification. Both proofs share the same logical backbone: a proof by contradiction showing that if the common sections EF and GH of parallel planes met at a point K, then K would lie in both parallel planes, contradicting their being parallel, hence the lines are parallel by definition. The citation differences are all at the granularity level: the AI explicitly cites 11.3 (common sections are straight lines) and D11.8 (definition of parallel planes) where Heath leaves these implicit, while Heath cites 11.1 to justify that K lies in plane AB whereas the AI reasons directly from the definition of common section without needing 11.1. Since the key intermediate conclusions (K in both planes, contradiction with parallelism, conclusion of line parallelism) are identical in both proofs and the differences are only in citation depth, this is a granularity difference.

### 11.17
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification. Both proofs follow the identical logical backbone: join AD, find its intersection with the middle plane, use XI.16 twice to establish two parallel lines (EO||BD and AC||OF in Heath; EG||BD and GF||AC in the AI), apply VI.2 twice to obtain proportionality in two triangles sharing the segment AD, then use V.11 to chain the equal ratios and conclude AE:EB = CF:FD. The only citation difference is that the AI additionally cites P1 (the postulate for joining straight lines), which is a construction postulate constituting over-citation. Since the key intermediate conclusions are the same and the citation difference is limited to a construction postulate, this is a granularity difference (Case A of Q2).

### 11.18
**Category**: Path difference
**Jaccard**: 0.429
**Analysis**: Q2 decided the classification as D (path difference). Heath and the AI reach the same conclusion (the tilted plane is perpendicular to the reference plane) through genuinely different intermediate conclusions. Heath constructs a line FG in the tilted plane perpendicular to the common section, proves FG is parallel to AB via I.28, then deduces FG is perpendicular to the reference plane via XI.8, and applies XI.Def.4. The AI instead constructs a line AG in the reference plane perpendicular to the common section, shows AG is perpendicular to both AB and CE (which lie in the tilted plane Q) via D11.3, deduces AG is perpendicular to plane Q via XI.4, and then applies D11.4. The key intermediate conclusions differ: Heath's backbone relies on parallelism (AB parallel to FG) while the AI's backbone relies on perpendicularity to a plane (AG perpendicular to plane Q via the two-line criterion). Both paths are logically complete and valid, but they employ different geometric strategies and different substantive propositions (heath_only: 1.28, 11.8 vs ai_only: 11.3, 11.4).

### 11.19
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish the same key intermediate conclusions: (1) construct a perpendicular within each plane to its common section with the reference plane, (2) apply D11.4 to show each constructed perpendicular is perpendicular to the reference plane, and (3) invoke 11.13 to force the conclusion that BD is perpendicular to the reference plane. The AI uses a direct proof structure while Heath uses proof by contradiction, but the key geometric facts are identical. The AI's extra citations (1.11 for constructing perpendiculars in a plane, 11.3 for the common section being a straight line) are construction and infrastructure propositions that Heath uses implicitly without citation, representing over-citation rather than a different logical path. Heath_only is empty, confirming the AI covers all of Heath's cited material. This is Case A: same backbone, different citation depth.

### 11.20
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs establish identical key intermediate conclusions: (1) construct angle BAE equal to angle DAB with AE equal to AD, (2) apply SAS congruence (I.4) to obtain DB = BE, (3) use the triangle inequality (I.20) on triangle BDC to derive DC > EC, (4) apply I.25 to conclude angle DAC > angle EAC, and (5) combine to show DAB + DAC > BAC. The AI's additional citations (1.23, 1.3, P1) are all construction-level propositions and a postulate that Heath uses implicitly without citing. Heath says 'let the angle BAE be constructed equal to the angle DAB' without citing I.23, 'let AE be made equal to AD' without citing I.3, and 'let DB, DC be joined' without citing P1. The AI explicitly cites these construction steps, making the difference purely one of citation depth rather than logical backbone. This is a clear Case A granularity difference.

### 11.21
**Category**: Granularity difference
**Jaccard**: 0.286
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: construct triangles from the solid angle vertex to a base figure, apply XI.20 at each base vertex to show the paired base angles exceed the corresponding base figure angle, sum these inequalities, compute total triangle angles via I.32, and subtract to conclude the face angles sum to less than four right angles. The AI generalizes Heath's 3-face proof to n faces using an n-sided polygon cross-section rather than a triangle, but this is a generalization of the same method, not a different path. The ai_only citations (11.2, CN2, CN3, CN5, P1) are all over-citations: 11.2 explicitly justifies that each triangle is in a plane (implicit in Heath), and the common notions and postulate are axioms Heath invokes without citation. heath_only is empty, confirming the AI covers all of Heath's cited dependencies. The proofs establish the same key intermediate conclusions at the same logical positions, differing only in citation granularity.

### 11.22
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: they handle the trivial equal-angles case, then for the unequal case construct auxiliary triangles using SAS congruence (I.4) to transfer chord lengths to a common vertex, apply I.24 to compare bases via angle comparison, and use the triangle inequality to establish that the sum of two chords exceeds the third. The AI proof is more verbose and has some false starts in its construction, but the final argument (Steps 14-24) follows the same key intermediate conclusions as Heath. The heath_only set is empty, confirming the AI covers all of Heath's reasoning. The ai_only set consists entirely of over-citations: construction propositions (1.23, 1.3), axioms (CN5, P1), and propositions Heath uses implicitly without citation (1.20 for triangle inequality, 1.22 for the final construction, 1.5 for isosceles base angles). This is Case A of Q2: same backbone with different citation depth.

### 11.23
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same key intermediate conclusions: construct triangle LMN from sides AC, DF, GK using XI.22; circumscribe a circle about LMN with center O; establish that AB > OL; erect a perpendicular from O to the plane of the circle; show that PL = PM = PN = AB via the Pythagorean theorem (I.47); and use SSS congruence (I.8) to establish that the solid angle's plane angles equal the given angles. The critical difference lies in how each proof establishes AB > OL: Heath provides a rigorous two-case contradiction using detailed proportional reasoning through VI.2, I.29, VI.4, V.16, and I.25, plus I.4 for congruence, while the AI provides a compressed but logically sound argument based on central angle sums versus given angle sums without citing these specific sub-steps. The heath_only citations (1.25, 1.29, 1.4, 5.16, 6.2, 6.4) all serve Heath's detailed proof of the sub-case 'AB is not less than LO,' and the ai_only citations (1.22, 1.3, 4.5, D1.15, D11.11, D11.3, D3.1, P1) are construction, definitional, and postulate references that Heath treats as implicit. This is a classic same-backbone, different-depth scenario.

### 11.24
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: use XI.16 to establish that opposite edges of the solid are parallel, thereby showing each face is a parallelogram; then use XI.10 for equal angles between non-coplanar parallel lines, I.34 for equal sides of parallelograms, I.4 for SAS triangle congruence, and I.34 again to conclude that each parallelogram is double the congruent triangle and therefore opposite faces are equal. The AI proof is more explicit, citing D1.22 (definition of parallelogram) where Heath applies it implicitly, citing CN1 and CN2 (common notions for transitive equality and doubles of equals) where Heath leaves them implicit, and using 1.8 (SSS) for a secondary triangle congruence that Heath handles via 'similarly we can prove.' All ai_only items (1.8, CN1, CN2, D1.22) are over-citations reflecting greater explicitness, not a different proof path. Heath_only is empty. This is Case A of Q2: same backbone, different citation depth.

### 11.25
**Category**: Granularity difference
**Jaccard**: 0.222
**Analysis**: Q2 decided the classification. Both proofs follow the same equimultiple strategy: they cut the parallelepiped with a parallel plane to form two sub-parallelepipeds, construct m-fold and n-fold copies of these sub-solids by extending the base segments, show each copy is equal to the original sub-solid (via XI.24), establish that the ordering of the m-fold and n-fold bases matches the ordering of the m-fold and n-fold solids, and conclude proportionality by V. Def. 5. The key intermediate conclusions are identical in both proofs. The AI cites additional lower-level results that Heath uses implicitly: 1.33 and 1.34 for parallelogram properties, 11.16 for intersections of parallel planes, 6.1 for ratios of parallelograms, CN4 and CN5 for common notions, and D11.10 for the definition of equal solid figures. Since heath_only is empty and all ai_only items are supporting sub-steps of the same logical backbone, this is a granularity difference (Case A of Q2).

### 11.26
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Q2 reveals genuinely different logical backbones, leading to classification via Q3. Heath constructs the solid angle directly using perpendiculars to planes (11.11 to drop a perpendicular from an elevated point, 11.12 to erect a perpendicular from a point in a plane, and D11.3 for the definition of perpendicularity to a plane), constructing only two face angles explicitly and then proving the third face angle matches via congruent triangles (I.4, I.8). The AI takes a fundamentally different approach: it constructs all three face angles explicitly at the vertex using I.23 and I.3, verifies the conditions of 11.20 (any two face angles sum to more than the third) and 11.21 (all three sum to less than four right angles), then invokes 11.23 as a black-box existence theorem to assert that a solid angle with those face angles can be constructed. The AI's path is logically valid under Q3: the chain from premises to conclusion is complete, with 11.23 providing the key construction step that replaces Heath's perpendicular-based approach. The large symmetric difference (Jaccard 0.25) reflects this genuine path divergence rather than mere granularity differences.

### 11.27
**Category**: Granularity difference
**Jaccard**: 0.375
**Analysis**: Q2 decided the classification. Both proofs share the same logical backbone: construct a solid angle at A equal to the solid angle at C, set up proportional edges using VI.12/6.12, derive the third proportion via V.22/5.22 ex aequali, show that three pairs of corresponding faces are similar parallelograms (by equal angles with proportional sides), note that opposite faces are equal and similar, and conclude by XI.Def.9 that the solids are similar. The AI proof cites all three of Heath's references (5.22, 6.12, D11.9) and adds five more (11.26 for solid angle construction, 11.24 for opposite faces being equal and similar, 11.15 and P1 for completing the solid, D6.1 for the definition of similar rectilinear figures). Heath uses all of these facts implicitly without formal citation. Since heath_only is empty and every ai_only item is an over-citation of a step Heath performs without explicit reference, this is a citation-depth difference with the same backbone, yielding category G.

### 11.28
**Category**: Granularity difference
**Jaccard**: 0.333
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs establish the same key intermediate conclusions: (1) the diagonal of each opposite face bisects it into two equal triangles via I.34, (2) opposite faces of the parallelepiped are equal parallelograms, (3) the cutting plane divides the solid into two prisms, and (4) these two prisms are equal because they are contained by planes equal in multitude and magnitude (D11.10). The AI proof makes the same argument as Heath but with more explicit detail. The ai_only items (11.24, CN1, CN4, D11.13) are all over-citations where the AI makes explicit what Heath leaves implicit: Heath says 'for they are opposite' without citing 11.24, refers to prisms without citing D11.13, and uses equality reasoning without citing CN1 or CN4. heath_only is empty, confirming the AI covers all of Heath's citations. This is Case A of Q2: same backbone, different citation depth.

### 11.29
**Category**: Path difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification. Heath's proof works directly with plane geometry results (I.34, I.36, I.4, I.8), establishing specific triangle equalities (DCE=HBK, AFG=MLN) and parallelogram equalities (DG=HN) to show two prisms are equal, then adding a common solid. The AI proof takes a structurally different approach, invoking parallelepiped properties (11.24), constructing an auxiliary parallelepiped between the two top faces, using the bisection theorem (11.28), and arguing through decomposition into a common solid plus two equal prisms whose equality follows from I.8 and I.34. The AI uses I.35 (parallelograms on same base) where Heath uses I.36 (parallelograms on equal bases), and brings in 11.24 and 11.28 which Heath does not cite at all. Since I.36 is not contained in any AI-cited proposition's proof tree and represents a genuinely different approach to establishing the key parallelogram equalities, the backbones differ (Case B). Under Q3, the AI's chain is logically sound — valid propositions are cited and the decomposition argument, though verbose, runs from premises to conclusion — yielding D.

### 11.30
**Category**: Granularity difference
**Jaccard**: 0.167
**Analysis**: Q2 decided this classification. Both proofs share the same logical backbone: construct an auxiliary parallelepiped, show it equals solid CM by XI.29 (standing edges on the same straight lines), show it equals solid CN by XI.29 (same reasoning for the other pair of sides), then conclude CM equals CN by transitivity. The AI proof cites additional supporting references (1.34 for parallelogram properties, 11.24 for opposite faces of parallelepipeds, CN1 for the transitivity step, and P1/P2 for line constructions) that Heath leaves implicit. Since heath_only is empty, the AI covers everything Heath cites and more. The ai_only items are all auxiliary citations providing deeper justification for the same logical steps, making this a granularity difference rather than a path difference.

### 11.31
**Category**: AI proof error
**Jaccard**: 0.125
**Analysis**: The classification was decided at Q1(b). The AI proof constructs a comparison solid RS on base FGPQ (constructed equal to LMNO via I.45) and then claims in Step 5 that solids AB (on base FGHK) and RS (on base FGPQ) are 'on the same base (sharing the side FG in the base plane)' and applies 11.29 or 11.30 to conclude AB equals RS. However, 11.29 and 11.30 both require the solids to be on THE SAME base - meaning the identical base parallelogram - not merely on equal bases that share one edge. FGHK and FGPQ are different parallelograms (equal in area but geometrically distinct), so the hypothesis of 11.29/11.30 is not satisfied. This is not a matter of compression or terseness: the AI explicitly identifies two different bases and then incorrectly claims they constitute 'the same base' for purposes of applying 11.29/11.30. Heath's proof avoids this by using a ratio argument through 11.25, 5.7, 5.9, and 5.11 to compare solids on different but related bases.
**Audit Record**: CANDIDATE E — 11.31
  violated_claim : In Step 5, the AI applies 11.29/11.30 (which require solids on 'the same base') to solids AB (on base FGHK) and RS (on base FGPQ), which are on different (though equal) bases sharing only edge FG
  failure_mode   : invalid_inference
  missing_is     : support — there is no proposition or valid argument licensing the conclusion that solids on different bases sharing one edge can be compared via 11.29/11.30, which explicitly require the same base
  evidence       : AI Step 5: 'solids AB and RS are on the same base (sharing the side FG in the base plane) and of the same height... by Proposition 11.29 the solids are equal. If not, then by Proposition 11.30 they are still equal.' But 11.29 states 'on the same base' meaning the identical parallelogram, not equal parallelograms sharing an edge. FGHK ≠ FGPQ.
  why_not_terse  : The AI explicitly identifies two distinct bases (FGHK and FGPQ) in Step 4, then incorrectly equates sharing one edge with being 'on the same base' in Step 5. This is not compression of a sound argument but misapplication of a proposition whose central hypothesis is not met. Heath's proof shows the gap is real: comparing solids on equal-but-different bases requires the ratio argument via 11.25, 5.7, 5.9, 5.11, which the AI entirely omits.

### 11.32
**Category**: Granularity difference
**Jaccard**: 0.750
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: construct a parallelogram equal to one base using I.45, complete a parallelepiped on it with matching height, apply XI.25 to establish a ratio between the solids and their bases, use XI.31 to equate the constructed solid with the other given solid, then substitute equals to reach the conclusion. The only difference is that the AI explicitly cites 5.7 (equal magnitudes have the same ratio to the same magnitude) to justify the final substitution step, while Heath performs this substitution without explicit citation. Since heath_only is empty and ai_only contains only 5.7 (a ratio-substitution principle used implicitly by Heath), this is a citation-depth difference with the same backbone, yielding category G.

### 11.33
**Category**: Path difference
**Jaccard**: 0.250
**Analysis**: Q2 decides this classification as Case B (different backbone), leading to Q3 which confirms the AI's path is valid. Heath's proof constructs an auxiliary solid KP equal to CD, then builds intermediary solids EO and QL to establish a four-term continued proportion of solids (AB:EO = EO:QL = QL:KP) using XI.32 and VI.1, then applies V.Def.10 for the triplicate ratio. The AI proof takes a fundamentally different approach: it sets up a continued proportion of lengths (AE, CF, EN, EP), then separates the volume comparison into a base-ratio component (using 6.22 for similar parallelograms to get the duplicate ratio) and a height-ratio component (using 11.25 and 11.32), chaining them via 5.22 (ex aequali) to obtain AB:CD = AE:EP, which is the triplicate ratio by D5.10. These are genuinely different logical backbones. The AI's path is logically complete under the hardened Q1(b) standard: each step is supported by a cited proposition, and the chain runs from premises to conclusion, so Q3(b) holds and the classification is D.

### 11.34
**Category**: Granularity difference
**Jaccard**: 0.545
**Analysis**: Q2 decided the classification as G. Both proofs share the same logical backbone: they construct an auxiliary parallelepiped on one base with the other solid's height, establish two key proportions (the ratio of the original solids to the auxiliary via XI.32 and the ratio involving heights via XI.25/VI.1), and then combine these with ratio arithmetic (V.7/V.9) for the forward and converse directions respectively. The heath_only items (11.29, 11.30) are explained by the proof-tree containment test: both appear inside Heath's own proof of XI.31, which the AI cites as a unit. Heath re-derives the oblique-to-perpendicular reduction inline at the level of 11.34, while the AI relies on XI.31 and XI.32 already covering all parallelepipeds (perpendicular and oblique). The ai_only items (5.11, 5.18, D5.13) reflect the AI's more explicit ratio manipulation and its cutting-plane technique for establishing CD:FO = h_CD:h_AB, where Heath uses a slightly different construction but reaches the same intermediate conclusion. These differences are citation-depth variations, not backbone differences.

### 11.35
**Category**: Path difference
**Jaccard**: 0.267
**Analysis**: Q2 decided this classification as Case B (different backbone), leading to Q3 which confirmed a valid different path (D). Heath's proof constructs AH equal to DM, draws HK parallel to GL, applies XI.8 to establish HK perpendicular to the plane, then works through perpendiculars from K and N to the original lines, ultimately concluding via I.8 (SSS). The AI proof instead makes DM equal to AG, drops perpendiculars from G directly to lines AB and AC using I.12, proves these feet are also the feet of perpendiculars from H (via I.47 and I.48), then proceeds through a chain of I.26 and I.4 applications to reach the conclusion via I.4 (SAS). The constructive strategies differ fundamentally: Heath uses a parallel-line construction with XI.8, while the AI uses direct perpendicular-to-line constructions with I.12 and XI.11. The intermediate conclusions also differ: Heath establishes right angles at C and F as key intermediates, while the AI establishes that perpendicular feet from G to the original lines coincide with perpendicular feet from H. The AI's final step uses I.8's converse direction (I.4 with SAS) rather than Heath's I.8 (SSS). The AI proof is logically complete and sound throughout.

### 11.36
**Category**: Path difference
**Jaccard**: 0.000
**Analysis**: The classification is decided at Q2/Q3. Heath's proof establishes that the base parallelograms of the two solids are equal (via VI.14, reciprocal proportion in equiangular parallelograms) and that their perpendicular heights are equal (via XI.35 Porism), then concludes equality by XI.31 (equal bases and same height implies equal solids). The AI takes a fundamentally different route: it uses VI.1 to establish that the ratio of the base areas equals A:B, combines this with the given proportion A:B = B:C and the ratio of heights B:C to show the bases are reciprocally proportional to the heights, then invokes XI.34 (the converse: reciprocally proportional bases and heights implies equal solids). Heath works with equalities throughout while the AI works with proportions and ratios. XI.35 (equal perpendiculars from elevated lines) plays no role in the AI proof, and 11.34 plays no role in Heath's proof for this proposition, confirming genuinely different logical backbones. The AI's chain is logically complete and valid, so this is a path difference.

### 11.37
**Category**: Granularity difference
**Jaccard**: 0.200
**Analysis**: Q2 decided the classification as G (Granularity difference). Both proofs share the same logical backbone: in the forward direction, apply 11.33 to establish that each pair of similar parallelepipedal solids has the triplicate ratio of their corresponding edges, then conclude from equal base ratios that the triplicate ratios (and hence the solid ratios) are equal; in the converse, reverse the argument. The AI proof explicitly cites 5.11 for the transitivity of equal ratios, 5.9 for duplicate ratio properties, and definitions D5.9/D5.10 for the concepts of duplicate and triplicate ratio, whereas Heath leaves all of this implicit, citing only 11.33. Since heath_only is empty and all ai_only items (5.11, 5.9, D5.10, D5.9) are supporting citations for reasoning steps that Heath performs without explicit citation, this is a citation-depth difference rather than a path difference.

### 11.38
**Category**: Path difference
**Jaccard**: 0.056
**Analysis**: Q2 decided the classification. Heath's proof establishes the bisection result through triangle congruence: first showing DUE is a straight line via congruent triangles DOU and PUE (I.4, I.14), then proving triangles DTU and GTS are congruent (I.26) using alternate angles (I.29) and vertical angles (I.15). The AI takes a fundamentally different approach: it identifies the common section ST by showing S and T each lie on both cutting planes via midpoint-proportionality collinearity arguments (6.2), then constructs a parallelogram ACGE using properties of the cube's parallel faces (11.24, 1.34, 1.30, 1.33), builds a sub-parallelogram ASTG, and concludes that AG and ST bisect each other as diagonals of ASTG (1.34). The key intermediate conclusions are entirely different — Heath never forms parallelograms ACGE or ASTG, and the AI never uses triangle congruence or the straight-line arguments central to Heath. The Jaccard similarity of 0.056 with only 1.33 shared confirms the near-total divergence. The AI's path is logically complete and valid, so this is a path difference (D).

### 11.39
**Category**: Granularity difference
**Jaccard**: 0.500
**Analysis**: Q2 decided the classification. Both proofs follow the same logical backbone: complete each prism to a parallelepiped, show the parallelogram bases are equal (since both are double the given triangle, via I.34), apply XI.31 to conclude the parallelepipeds are equal, then use XI.28 to note each prism is half its parallelepiped and conclude the prisms are equal. The AI's extra citations (CN1, CN3, D11.13) are common notions and a definition that Heath uses implicitly — CN1 for the transitivity step establishing base equality, CN3 for the 'halves of equals are equal' conclusion, and D11.13 as a definition. These are over-citations of axiom-level items, not substantive path differences. Since the key intermediate conclusions are identical but the citation sets differ only by these implicit axioms/definitions, this is a granularity difference (G).
