# EXPERIMENT 5 – HEURISTIC SEARCH

## Aim
To study and implement heuristic search algorithms using Python.

## Introduction
Heuristic Search uses additional information to estimate how close a current state is to the goal state. This helps in finding solutions efficiently.

A heuristic function is represented as h(n), where n is the current node.

## 1. Greedy Best-First Search

Greedy Best-First Search selects the node that appears closest to the goal based on the heuristic value.

**Evaluation Function:**

f(n) = h(n)

**Working:**
1. Start from the initial node.
2. Calculate heuristic values of neighboring nodes.
3. Select the node with the lowest heuristic value.
4. Repeat until the goal is reached.

**Example:** Finding a route using straight-line distance to the destination.

## 2. A* Search Algorithm

A* Search combines the actual cost and estimated cost to find an efficient path.

**Evaluation Function:**

f(n) = g(n) + h(n)

Where:
- g(n): Actual cost from the starting node.
- h(n): Estimated cost from the current node to the goal.
- f(n): Total estimated cost.

**Working:**
1. Start from the initial node.
2. Calculate g(n), h(n) and f(n).
3. Select the node with the lowest f(n).
4. Expand its neighboring nodes.
5. Repeat until the goal is reached.

**Example:** Solving the Eight Puzzle Problem.

## 3. AO* Search Algorithm

AO* is a heuristic search algorithm used for AND-OR graphs.

- OR node: Only one child needs to be selected.
- AND node: All required child nodes must be solved.

**Working:**
1. Start from the initial node.
2. Calculate estimated costs using heuristic values.
3. Select the most promising path.
4. Expand the selected node.
5. Update the costs.
6. Continue until the solution graph is found.

**Example:** Solving problems that can be divided into smaller subproblems.

## 4. Memory-Bounded Heuristic Search

Memory-Bounded Search algorithms perform heuristic search while controlling the amount of memory used.

**Example: IDA* (Iterative Deepening A*)**

IDA* combines ideas from A* and iterative deepening search.

**Working:**
1. Calculate the initial f-cost.
2. Set it as the search threshold.
3. Perform depth-first search within that threshold.
4. If the goal is not found, increase the threshold.
5. Repeat until the goal is reached.

## Applications

### Tic-Tac-Toe
A game where two players place X and O on a 3×3 board. Search algorithms can help select the best move.

### Missionaries and Cannibals
A river-crossing problem where missionaries and cannibals must cross without violating safety conditions.

### Eight Puzzle
A 3×3 board containing eight numbered tiles and one blank space. The objective is to arrange the tiles in the correct order.

## Comparison

| Algorithm | Main Idea |
|---|---|
| Greedy Best-First | Uses heuristic value only |
| A* | Uses actual cost and heuristic |
| AO* | Searches AND-OR graphs |
| IDA* | Uses iterative deepening with f-cost limits |

## Result
Different heuristic search algorithms and their applications were studied and implemented successfully.
