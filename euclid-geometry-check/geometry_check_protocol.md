# Geometric Configuration Consistency Check Protocol

## Purpose

Post-classification audit of AI-generated Euclid proofs for **spatial configuration contradictions** — errors where individual proof steps each appear logically sound, but their combined spatial/geometric assumptions are mutually inconsistent.

This check is independent of the P/G/D/E classification. A proof classified as D ("valid different path") or G ("granularity difference") may still contain a hidden geometric configuration error.

## Scope

Check AI proofs from **geometric books** (Books 1, 2, 3, 4, 6, 10, 11, 12, 13) that were classified as **D** (these are proofs where the AI took a genuinely different geometric path, most likely to introduce novel spatial constructions with configuration errors). Books 5, 7, 8, 9 are skipped (proportions theory and number theory with no spatial configuration). Book 10 is mixed — some propositions are geometric, others purely algebraic; the SKIP mechanism handles this naturally.

## What to check

### 1. Point Position Consistency

Track every claim about where a constructed or auxiliary point lies:
- "F lies inside triangle DEG"
- "F lies on segment AB"
- "G falls on the same side of line DE as F"
- "H lies outside circle ABC"

For each such claim, verify that ALL subsequent reasoning about that point is compatible with the stated position. Common contradictions:
- A point claimed inside a triangle, but later used as if outside (or vice versa)
- A point claimed on a line segment, but later treated as off the line
- A point claimed on one side of a line, but later implicitly placed on the other side

### 2. Ray/Line "Between" Consistency

When the proof claims one ray or line falls between two others:
- "ray FD falls between rays FE and FG"
- "point M lies between A and B"
- "line CD falls between lines AB and EF"

Verify this is consistent with the established positions of all points involved. The most common error pattern:
- If F is inside triangle DEG, then from F's perspective, D, E, G surround F — no one of FD, FE, FG falls "between" the other two in the simple additive sense. Instead, the three angles around F sum to 360°.

### 3. Angle Decomposition Consistency

When the proof decomposes an angle as a sum:
- "angle EFG = angle EFD + angle DFG"

Verify this decomposition is geometrically valid given the established configuration:
- Additive decomposition (angle = part1 + part2) requires the middle ray to fall BETWEEN the outer two rays
- If a point is inside a triangle, the angles around it sum to 360°, not to any single angle
- Check whether the decomposition implicitly requires a different point position than what was established

### 4. Triangle Interior/Exterior Argument Consistency

When the proof uses Proposition 1.21 (or similar results about interior points):
- 1.21 requires a point strictly inside a triangle
- The consequences of 1.21 (angle inequality) apply only in that configuration
- Subsequent steps must not treat the same point as if it were outside

When the proof uses results about exterior angles or supplementary angles:
- These require specific geometric configurations (point on a line extension, exterior of a triangle)
- Verify the configuration matches

### 5. Circle Inside/Outside Consistency

For proofs involving circles (especially Books 3, 4):
- A point claimed inside a circle vs. outside vs. on the circumference
- Tangent line arguments requiring specific point positions
- Arc arguments requiring points on specific arcs

### 6. Solid Geometry Configuration (Book 11, 12)

For solid geometry proofs:
- Plane membership claims: "point A lies in plane P"
- Above/below plane claims
- Dihedral angle decompositions
- Perpendicularity claims and their spatial consequences

## Process

For each proposition under review:

### Step A: Extract spatial claims
Read through the AI proof and list every explicit or implicit claim about:
- Where a point is located (inside/outside/on a figure)
- How rays, lines, or segments are ordered relative to each other
- How angles are decomposed or compared

### Step B: Build a configuration map
For each constructed or auxiliary point, track its claimed position through every step. Note any step where the position is used but not explicitly re-stated.

### Step C: Check pairwise consistency
For each pair of spatial claims involving the same point or figure, check whether they can simultaneously be true. Pay special attention to:
- Claims in different steps (the error in 1.24 spans Steps 6-8)
- Claims that each cite a different proposition (one requires interior, another requires exterior)
- Implicit spatial assumptions hidden in angle decompositions

### Step D: Verdict

- **PASS**: All spatial claims are mutually consistent, or the proof does not make significant spatial claims (e.g., purely algebraic/proportional arguments)
- **FAIL**: A specific contradiction exists between spatial claims. Document:
  - Which steps are contradictory
  - What spatial assumption each step requires
  - Why they cannot both be true
  - Whether the error is fixable (could the proof be repaired with a different construction?)
- **SKIP**: The proof is purely algebraic/proportional with no geometric configuration claims (common in Books 5, 7-9, parts of 10)

## Output format

```json
{
  "proposition": "1.24",
  "run": "RunA",
  "current_category": "D",
  "verdict": "FAIL",
  "contradictory_steps": ["Step 6", "Step 8"],
  "spatial_claim_1": {
    "step": "Step 6",
    "claim": "F lies inside triangle DEG",
    "required_by": "Application of 1.21 in Step 7"
  },
  "spatial_claim_2": {
    "step": "Step 8",
    "claim": "ray FD falls between rays FE and FG, so angle EFG = angle EFD + angle DFG",
    "required_by": "Angle inequality chain in Steps 8-10"
  },
  "contradiction": "If F is inside triangle DEG, the three angles DFE, EFG, GFD around F sum to 360°. The additive decomposition angle EFG = angle EFD + angle DFG would force angle EFG = 180°, impossible for a triangle vertex.",
  "fixable": true,
  "fix_note": "Heath avoids this by using I.5 (isosceles triangle) instead of I.21, never needing F inside the triangle."
}
```

## Important notes

- **Default presumption is PASS.** Only flag FAIL when you can articulate a specific, concrete contradiction. Vague unease about a configuration is not sufficient.
- **Each step may be individually correct.** The error is in the COMBINATION. Do not flag a step as wrong just because it uses a different approach than Heath.
- **Angle decomposition is the #1 error pattern.** Pay extra attention whenever an angle is written as a sum of two angles — verify the middle ray actually falls between the outer rays given the established geometry.
- **Draw the figure mentally (or describe it).** Before checking consistency, describe the geometric configuration in words. This makes contradictions much easier to spot.
- **A FAIL here means the proof has a genuine error** regardless of its P/G/D/E classification. It should be treated as equivalent to an E classification with error_type "Geometric configuration contradiction".
