# Development Log – The Torchbearer

**Student Name:** Katelyn Nguyen
**Student ID:** 130820258

---

## Entry 1 – [5/8/2026]: Initial Plan

Today, I'll implement parts 1, 2a, 2b, and 2c. I expect distance storage and precomputing distances to be difficult and I plan on testing my code using different test and edge cases.

---

## Entry 2 – [5/10/2026]: Verifying Correctness of Shortest Path

Today, I'll be focusing on implementing part 3 of the assignment. For part 3A, I got a bit stumped on the wording for explaining the invariant for the non finalized nodes. I decided that the invariant requires that previous nodes leading up to the current node have been discovered; but I didn't mention anything about minimum cost. I changed my answer to include both but my answer may be too long now so I may change it again in the future.
---

## Entry 3 – [5/11/2026]: Designing Search

Today, I'll be focusing on implementing part 4 of the assignment. My biggest hurdle was creating a counter example that shows greedy failing compared to the optimal solution. To solve this problem, I changed the costs from the spec illustration to the following: (C --> T) = 2, (B --> T) = 2. This created a scenario in which greedy would choose the (C --> B) but would end up with an overall higher cost.

---

## Entry 4 – [5/13/2026]: Post-Implementation Reflection

I've implemented the find_optimal_route along with the _explore recursive helper function today. One thing that I'd like to improve would be to find a better way of pruning unnecessary paths given I had more time to brainstorm. I'd also try and see what other data strucures I could use for holding the remaining relics to be collected.

---

## Final Entry – [5/14/2026]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | 15 minutes |
| Part 2: Precomputation Design | 30 minutes |
| Part 3: Algorithm Correctness | 30 minutes |
| Part 4: Search Design | 30 minutes |
| Part 5: State and Search Space | 2 hours |
| Part 6: Pruning | 4 hours |
| Part 7: Implementation | 4 hours |
| README and DEVLOG writing | 4 hours |
| **Total** | 15.75 hours |
