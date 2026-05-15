"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Katelyn Nguyen
Student ID:   130820258

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.

    """
    Q1 = "A single shortest-path run from S cannot make globally optimal decisions based on previous results."
    Q2 = "The decision of building a path from starting node S to exit node T."
    Q3 = "This requires a search over orders because the best path needs to consider all possibilities which cannot be done through a single computation."
    return Q1 + Q2 + Q3

# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.

    """
    # Selecting source nodes for precomputing distances.
    nodesList = [spawn] + relics + [exit_node]
    return list(set(nodesList))

def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').

    """
    # Setting the cost for each node to infinity
    nodeCosts = {node: float('inf') for node in graph}

    # Setting the source node cost to 0
    nodeCosts[source] = 0

    # Initializing priority queue with the source node and its cost
    priorityQueue = [(0, source)]

    while priorityQueue:
        [currentCost, currentNode] = heapq.heappop(priorityQueue)

        # If the current cost is greater than the previous cost to reach the current node, skip it
        if currentCost > nodeCosts[currentNode]:
            continue
        for neighbor, edgeCost in graph[currentNode]:

            # If the cost to reach the neighbor + the edge cost is less than the previous cost, we update the cost to reach the neighbor
            if nodeCosts[currentNode] + edgeCost < nodeCosts[neighbor]:
                nodeCosts[neighbor] = nodeCosts[currentNode] + edgeCost
                heapq.heappush(priorityQueue, (nodeCosts[neighbor], neighbor))

    # Returning the dictionary of minimum costs from the source to every node in the graph
    return nodeCosts

def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.

    """
    # Initializing source nodes to precompute distances
    sourceNodes = select_sources(spawn, relics, exit_node)

    # Distance table storing each node and the minimum cost to reach every other node from it
    distTable = {}

    for sourceNode in sourceNodes:
        distTable[sourceNode] = run_dijkstra(graph, sourceNode)

    return distTable

# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.

    """
    Q3A1 = "It must hold true that the minimum cost has been found from the current node to all other nodes in S."
    Q3A2 = "It must hold true that for each node not in S, the distance leading up to that node is the lowest found path since all finalized nodes leading up to the undiscovered node must have the minimum cost from the current node already recorded."
    Q3init = "Before iteration 1, only one node has been discovered with a cost of 0. Discovering the current node means all nodes have been discovered and therefore the minimum cost for all nodes has been computed as well since cost can never be negative."
    Q3main = "Given there can only be nonnegative edge weights, it can be assumed that adding to an already recorded minimum cost would result in a cost greater than that minimum cost. Thus, finalizing the min-dist node always records the minimum cost."
    Q3term = "The invariant guarantees that the minimum cost to reach every other node from the current node has been recorded. Therefore, an optimal path will be discovered from the starting node to the exit node."
    Q3C = "By calculating the correct shortest-path distances from the current node to other nodes, we correctly calculate fuel costs, allowing the torchbearer to make accurate decisions on where to go based on fuel efficiency."
    return Q3A1 + Q3A2 + Q3init + Q3main + Q3term + Q3C


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    """
    failureMode = "Greedy will pick the path with a locally lower fuel cost, not considering if that choice contributes to the globally optimal fuel cost, ultimately failing."
    counterExample = ""
    "'S': [('B', 1), ('C', 2), ('D', 2)] " \
    "'B': [('D', 1), ('T', 2)]" \
    "'C': [('B', 1), ('T', 2)]" \
    "'D': [('B', 1), ('C', 1)] " \
    "'T': [] "
    greedyPick = "Greedy will pick (S, B) + (B, D) + (D, C) + (C, B) + (B, T) with a total cost of 6." 
    optimalPick = "Optimal will pick (S, B) + (B, D) + (D, C) + (C, T) with total cost of 5." 
    greedyLoss = "Greedy loses because it chose the local best path (C, B) without considering that it would cost more to reach the end for path (B, T)."
    algoExplore = "The algorithm must explore all orders in which a path from the starting node to the ending node while reaching all relic nodes at least once exists."
    return failureMode + counterExample + greedyPick + optimalPick + greedyLoss + algoExplore


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    """
    fuelCost = 0
    currentLoc = spawn
    relicsUncollected = list(relics)
    relicsCollected = []

    # A list holding the minimum cost for the torchbearer to reach the exit and the order of visited relics to get there
    bestCost = [float('inf'), []]

    # Recursively explore all possible valid paths from the start to the exit node 
    _explore(dist_table, currentLoc, relicsUncollected, relicsCollected, fuelCost, exit_node, bestCost)

    # Returns the overall best fuel cost and the order of visited relics to achieve it
    return (bestCost[0], bestCost[1])

def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """
    # Base Case:
    # If there are no more relics to visit 
    if len(relics_remaining) == 0:

        # Calculate total cost to reach the exit node from the current location
        totalCost = cost_so_far + dist_table[current_loc][exit_node]

        # Update best cost if total cost is less than current best
        if totalCost < best[0]:
            best[0] = totalCost
            best[1] = relics_remaining.copy()
        return

    # Picking the cheapest cost to reach any relic from the current location
    cheapestRelicCost = min(dist_table[current_loc][relic] for relic in relics_remaining)

    # Picking the cheapest cost to reach the exit node from any remaining relics
    cheapestExitCost = min(dist_table[relic][exit_node] for relic in relics_remaining)

    # Estimates the lowest potential cost to reach the exit node from the current location while visiting all remaining relics
    optimalCost = cheapestRelicCost + cheapestExitCost

    # If the actual cost so far plus this lowest assumed possible cost is more than the current best cost, the path can be pruned since the actual cost would be greater than or equal to this possible cost.
    if cost_so_far + optimalCost >= best[0]:
        return
    
    # Recursive Case:
    for relic in list(relics_remaining):

        # Calculating the current fuel cost to reach the next relic from the current location
        currentFuelCost = cost_so_far + dist_table[current_loc][relic]

        relics_remaining.remove(relic)
        relics_visited_order.append(relic)

        # Recursively explore starting with the reached relic as the new current location along with the currently calculated fuel cost
        _explore(dist_table, relic, relics_remaining, relics_remaining, currentFuelCost, exit_node, best)

        # Backtracking:
        relics_visited_order.pop()
        relics_remaining.append(relic)

# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.
    """
    # Computing the minimum distances from each node to every other node in the graph
    distTable = precompute_distances(graph, spawn, relics, exit_node)

    # Finding the best valid route with optimal fuel costs using these minimum distances
    return find_optimal_route(distTable, spawn, relics, exit_node)

# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()
    explain_problem()
