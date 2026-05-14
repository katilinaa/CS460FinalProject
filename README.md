# The Torchbearer

**Student Name:** Katelyn Nguyen
**Student ID:** 130820258
**Course:** CS 460 – Algorithms | Spring 2026

> This README is your project documentation. Write it the way a developer would document
> their design decisions , bullet points, brief justifications, and concrete examples where
> required. You are not writing an essay. You are explaining what you built and why you built
> it that way. Delete all blockquotes like this one before submitting.

---

## Part 1: Problem Analysis

> Document why this problem is not just a shortest-path problem. Three bullet points, one
> per question. Each bullet should be 1-2 sentences max.

- **Why a single shortest-path run from S is not enough:**
- A single shortest-path from S does not take into account all future possibilites, so an overall optimal choice is not guaranteed.

- **What decision remains after all inter-location costs are known:**
- The decision of building a path from starting node S to exit node T.

- **Why this requires a search over orders (one sentence):**
- A search over orders takes into account all future possibilites, preventing the blocking of future optimal choices.

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

> List the source node types as a bullet list. For each, one-line reason.

| Source Node Type | Why it is a source |
|---|---|

| Spawn Node | This is the node the torchbearer has to start from |
| Relic Node | One of the nodes the torchbearer must visit once |
| Exit Node | The ending node the torchbearer has to end at|

### Part 2b: Distance Storage

> Fill in the table. No prose required.

| Property | Your answer |
|---|---|
| Data structure name | Heap |
| What the keys represent | Keys represent vertices |
| What the values represent | Represent edge costs|
| Lookup time complexity | O(V) where V is the number of vertices |
| Why O(1) lookup is possible | If we have 1 vertice, we would have O(1) lookup time|

### Part 2c: Precomputation Complexity

> State the total complexity and show the arithmetic. Two to three lines max.

- **Number of Dijkstra runs:** Let n = |V| vertices. Dijkstra runs n times.
- **Cost per run:** Let n = |V|, m = |E|, k = |M|. O(N) insertions + O(log(N)) minimum cost look up + O(E) pops from priority queue.
- **Total complexity:** O(E + Nlog(N))
- **Justification (one line):** As Dijkstra's algorithm requires all three actions, we add the time complexities up to get O(E + Nlog(N))

---

## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
  It must hold true that the minimum cost has been found from the current node to all other nodes in S.

- **For nodes not yet finalized (not in S):**
  It must hold true that for each node not in S, the node with the lowest cost from the current node is discovered. Thus, all nodes leading up to the undiscovered node must have the minimum cost from the current node already recorded.

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  Since we are starting with the current node, the cost to reach the current node is 0 which is the minimum cost for all nodes discovered given we've only discovered one node.

- **Maintenance : why finalizing the min-dist node is always correct:**
  Given that we only have nonnegative edge weights, it can be assumed that adding to an already recorded minimum cost may result in that cost not being minimal anymore. Thus, finalizing the min-dist node always records the minimum cost.

- **Termination : what the invariant guarantees when the algorithm ends:**
  The invariant guarantees that we've recorded the minimum costs to reach every other node from the current node, correctly solving the problem for the shortest-path.

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

By calculating the correct shortest distances from the current node to other nodes, we correctly calculate fuel costs, allowing the torchbearer to make accurate decisions on where to go based on fuel efficiency.

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** Greedy will pick the path with the overall highest fuel cost when picking the current shortest path from the current node.
- **Counter-example setup:**
    'S': [('B', 1), ('C', 2), ('D', 2)]
    'B': [('D', 1), ('T', 1)]
    'C': [('B', 1), ('T', 2)]
    'D': [('B', 1), ('C', 1)]
    'T': []
- **What greedy picks:** Greedy will pick (S, B) + (B, D) + (D, C) + (C, B) + (B, T) with a total cost of 6.
- **What optimal picks:** Optimal will pick (S, B) + (B, D) + (D, C) + (C, T) with total cost of 5.
- **Why greedy loses:** Greedy loses because it greedily chooses the shortest path from the current node without considering future choices.

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- The algorithm must explore the order in which the shortest path from the starting node to the ending node while reaching all relic nodes at least once exists.

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | currentLoc | node | The current location of the Torchbearer |
| Relics already collected | relicsCollected | List[node] | A list representing the relics we've already collected |
| Fuel cost so far | fuelCost | float | A float value representing the amount of fuel the Torchbearer has used to traverse |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | List |
| Operation: check if relic already collected | Time complexity: O(N)|
| Operation: mark a relic as collected | Time complexity: O(N)|
| Operation: unmark a relic (backtrack) | Time complexity: O(N)|
| Why this structure fits | This fits because we can easily add and remove relics if needed for backtracking |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** Worst case, we would consider O(k^3) orders
- **Why:** Since all of the operations we are performing when searching for the best path take O(k) time, this equates to O(k^3) time.

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** Tracking the cheapest fuel cost to reach a relic from the current relic and the cheapest fuel cost to reach the exit from all remaining relics.
- **When it is used:** Used to calculate the potential fuel cost for the path from the next cheapest relic to the exit
- **What it allows the algorithm to skip:** Skips paths that would incur higher fuel costs

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** The current location, the relics collected, and the amount of fuel used.
- **What the lower bound accounts for:** Accounts for the current fuel used plus the optimal fuel used for all potential paths from the current location.
- **Why it never overestimates:** Since assuming most optimal fuel cost for all potential paths, if the actual cost is more, the path can be safely eliminated since the lowest amount it could have been still wouldn't beat the current best fuel cost. 

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- Pruning is safe because the Torchbearer is still forced to visit a remaining relic and follow a valid path to the exit. Since the cheapest costing relic is visited and the cheapest costing path from that relic to the exit is assumed, the actual cost can never be lower than that.

---

## References

> Bullet list. If none beyond lecture notes, write that.

- Lecture notes
- Python Wiki https://wiki.python.org/moin/TimeComplexity
- Pruning Techniques https://fastercapital.com/content/Pruning-Techniques--Cutting-Corners--Pruning-Techniques-in-Branch-and-Bound.html#Introduction-to-Branch-and-Bound
