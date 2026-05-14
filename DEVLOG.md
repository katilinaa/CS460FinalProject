# Development Log – The Torchbearer

**Student Name:** Katelyn Nguyen
**Student ID:** 130820258

> Instructions: Write at least four dated entries. Required entry types are marked below.
> Two to five sentences per entry is sufficient. Write entries as you go, not all in one
> sitting. Graders check that entries reflect genuine work across multiple sessions.
> Delete all blockquotes before submitting.

---

## Entry 1 – [5/8/2026]: Initial Plan

> Required. Write this before writing any code. Describe your plan: what you will
> implement first, what parts you expect to be difficult, and how you plan to test.

Today, I'll implement parts 1, 2a, 2b, and 2c. I expect distance storage and precomputing distances to be difficult and I plan on testing my code using different test and edge cases.

---

## Entry 2 – [5/10/2026]: Verifying Correctness of Shortest Path

> Required. At least one entry must describe a bug, wrong assumption, or design change
> you encountered. Describe what went wrong and how you resolved it.

Today, I'll be focusing on implementing part 3 of the assignment. For part 3A, I got a bit stumped on the wording for explaining the invariant for the non finalized nodes. I decided that the invariant requires that previous nodes leading up to the current node have been discovered; but I didn't mention anything about minimum cost. I changed my answer to include both but my answer may be too long now so I may change it again in the future.
---

## Entry 3 – [5/11/2026]: Designing Search

Today, I'll be focusing on implementing part 4 of the assignment. My biggest hurdle was creating a counter example that shows greedy failing compared to the optimal solution. To solve this problem, I changed the costs from the spec illustration to the following: (C --> T) = 2, (B --> T) = 2. This created a scenario in which greedy would choose the (C --> B) but would end up with an overall higher cost.

---

## Entry 4 – [5/13/2026]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_Your entry here._

---

## Final Entry – [Date]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | |
| Part 2: Precomputation Design | |
| Part 3: Algorithm Correctness | |
| Part 4: Search Design | |
| Part 5: State and Search Space | |
| Part 6: Pruning | |
| Part 7: Implementation | |
| README and DEVLOG writing | |
| **Total** | |
