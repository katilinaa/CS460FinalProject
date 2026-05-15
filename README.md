# The Torchbearer

**Student Name:** Katelyn Nguyen
**Student ID:** 130820258
**Course:** CS 460 – Algorithms | Spring 2026

---

## Part 1: Problem Analysis

- **Why a single shortest-path run from S is not enough:**
- A single shortest-path run from S cannot make globally optimal decisions based on previous results.

- **What decision remains after all inter-location costs are known:**
- The decision of building a path from starting node S to exit node T.

- **Why this requires a search over orders (one sentence):**
- This requires a search over orders because the best path needs to consider all possibilities which cannot be done through a single computation.

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

| Source Node Type | Why it is a source |
|---|---|
| Spawn Node | This is the node the Torchbearer has to start from |
| Relic Node | One of the nodes the Torchbearer must visit at least once |
| Exit Node | The ending node the Torchbearer has to exit from |

### Part 2b: Distance Storage

| Property | Your answer |
|---|---|
| Data structure name | Heap |
| What the keys represent | Keys represent vertices |
| What the values represent | Values represent edge costs|
| Lookup time complexity | O(V) where V is the number of vertices |
| Why O(1) lookup is possible | If we have 1 vertice, we would have O(1) lookup time |

### Part 2c: Precomputation Complexity

- **Number of Dijkstra runs:** Let n = |V| vertices. Dijkstra runs n times.
- **Cost per run:** Let n = |V|, m = |E|. O(n) insertions + O(log(n)) minimum cost look up + O(m) pops from priority queue to equal O(m + nlog(n + k)).
- **Total complexity:** O(n(m + nlog(n + k)))
- **Justification (one line):** As Dijkstra runs n times and each run costs O(m + nlog(n + k)) time, multiplying the costs together gives the overall complexity of O(n(m + nlog(n + k))).

---

## Part 3: Algorithm Correctness

### Part 3a: What the Invariant Means

- **For nodes already finalized (in S):**
  It must hold true that the minimum cost has been found from the current node to all other nodes in S.

- **For nodes not yet finalized (not in S):**
  It must hold true that for each node not in S, the distance leading up to that node is the lowest found path since all finalized nodes leading up to the undiscovered node must have the minimum cost from the current node already recorded.

### Part 3b: Why Each Phase Holds

- **Initialization : why the invariant holds before iteration 1:**
  Before iteration 1, only one node has been discovered with a cost of 0. 
  Discovering the current node means all nodes have been discovered and therefore the minimum cost for all nodes has been computed as well since cost can never be negative. 

- **Maintenance : why finalizing the min-dist node is always correct:**
  Given there can only be nonnegative edge weights, it can be assumed that adding to an already recorded minimum cost would result in a cost greater than that minimum cost. Thus, finalizing the min-dist node always records the minimum cost.

- **Termination : what the invariant guarantees when the algorithm ends:**
  The invariant guarantees that the minimum cost to reach every other node from the current node has been recorded.
  Therefore, an optimal path will be discovered from the starting node to the exit node.

### Part 3c: Why This Matters for the Route Planner

By calculating the correct shortest-path distances from the current node to other nodes, we correctly calculate fuel costs, allowing the torchbearer to make accurate decisions on where to go based on fuel efficiency.

---

## Part 4: Search Design

### Why Greedy Fails

- **The failure mode:** Greedy will pick the path with a locally lower fuel cost, not considering if that choice contributes to the globally optimal fuel cost, ultimately failing.
- **Counter-example setup:**
    'S': [('B', 1), ('C', 2), ('D', 2)]
    'B': [('D', 1), ('T', 2)]
    'C': [('B', 1), ('T', 2)]
    'D': [('B', 1), ('C', 1)]
    'T': []
- **What greedy picks:** Greedy will pick (S, B) + (B, D) + (D, C) + (C, B) + (B, T) with a total cost of 6.
- **What optimal picks:** Optimal will pick (S, B) + (B, D) + (D, C) + (C, T) with total cost of 5.
- **Why greedy loses:** Greedy loses because it chose the local best path (C, B) without considering that it would cost more to reach the end for path (B, T).

### What the Algorithm Must Explore

- The algorithm must explore all orders in which a path from the starting node to the ending node while reaching all relic nodes at least once exists.

---

## Part 5: State and Search Space

### Part 5a: State Representation

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | currentLoc | node | The current location of the Torchbearer |
| Relics already collected | relicsCollected | List[node] | A list representing the relics we've already collected |
| Fuel cost so far | fuelCost | float | A float value representing the amount of fuel the Torchbearer has used to traverse |

### Part 5b: Data Structure for Visited Relics

| Property | Your answer |
|---|---|
| Data structure chosen | List |
| Operation: check if relic already collected | Time complexity: O(N)|
| Operation: mark a relic as collected | Time complexity: O(1)|
| Operation: unmark a relic (backtrack) | Time complexity: O(1)|
| Why this structure fits | This fits because we can easily add and remove relics if needed for backtracking |

### Part 5c: Worst-Case Search Space

- **Worst-case number of orders considered:** Worst case, we would consider O(k!) orders
- **Why:** There's a case in which all possible paths from the start to exit with k nodes must be explored to find the optimal solution, resulting in k! orders.

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

- **What is tracked:** Tracking the cheapest fuel cost to reach a relic from the current location and the cheapest fuel cost to reach the exit from all remaining relics.
- **When it is used:** Used to calculate the potential fuel cost for the path from the next cheapest relic to the exit.
- **What it allows the algorithm to skip:** Skips paths that would incur higher fuel costs.

### Part 6b: Lower Bound Estimation

- **What information is available at the current state:** The current location, the relics collected, and the amount of fuel used.
- **What the lower bound accounts for:** Accounts for the current fuel used plus the optimal fuel used for all potential paths from the current location.
- **Why it never overestimates:** Since assuming most optimal fuel cost for all potential paths, if the actual cost is more, the path can be safely eliminated since the lowest amount it could have been still wouldn't beat the current best fuel cost. 

### Part 6c: Pruning Correctness

- Pruning is safe because the Torchbearer is still forced to visit a remaining relic and follow a valid path to the exit. Since the cheapest costing relic is visited and the cheapest costing path from that relic to the exit is assumed, the actual cost can never be lower than that.

---

## References

- Lecture notes
- Python Wiki https://wiki.python.org/moin/TimeComplexity: used for finding the time complexity for list operations. Verified correctness by iterating for each list operation by hand.
- Pruning Techniques https://fastercapital.com/content/Pruning-Techniques--Cutting-Corners--Pruning-Techniques-in-Branch-and-Bound.html#Introduction-to-Branch-and-Bound: used for brainstorming ways to prune unwanted paths and for verifying pruning correctness. Verified the result by debugging the code step by step to ensure pruning correctness.
