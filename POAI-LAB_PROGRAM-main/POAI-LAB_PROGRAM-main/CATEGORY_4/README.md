# EXPERIMENT 4 – UNINFORMED SEARCH

## Aim
To study and implement different uninformed search algorithms using Python.

## Introduction
Uninformed Search is a search technique that explores possible states without using additional knowledge about how close a state is to the goal.

## 1. Breadth First Search (BFS)

BFS explores nodes level by level. It visits all neighboring nodes before moving to the next level.

**Data Structure:** Queue (FIFO).

**Working:**
1. Start from the initial node.
2. Add it to the queue.
3. Remove the front node.
4. Visit its unvisited neighbors.
5. Add those neighbors to the queue.
6. Continue until the goal is found.

**Example:** Finding the shortest path in an unweighted graph.

## 2. Depth First Search (DFS)

DFS explores one path as deeply as possible before backtracking.

**Data Structure:** Stack (LIFO) or recursion.

**Working:**
1. Start from the initial node.
2. Visit an unvisited neighboring node.
3. Continue deeper into the graph.
4. Backtrack when no unvisited neighbor exists.
5. Continue until the goal is found.

**Example:** Exploring paths in a maze.

## 3. Depth Limited Search (DLS)

DLS is a modified version of DFS that uses a fixed depth limit.

It does not explore nodes beyond the specified depth.

**Working:**
1. Start from the initial node.
2. Set a maximum depth limit.
3. Explore nodes using DFS.
4. Stop expanding nodes when the depth limit is reached.
5. Return the result if the goal is found.

**Example:** Searching for a destination within a limited number of steps.

## 4. Bidirectional Search

Bidirectional Search performs two searches simultaneously:
- Forward search from the initial state.
- Backward search from the goal state.

The search stops when both searches meet.

**Working:**
1. Start one search from the initial node.
2. Start another search from the goal node.
3. Expand both search frontiers.
4. Check whether the frontiers intersect.
5. Combine the paths when they meet.

**Example:** Finding a route between two locations.

## Comparison

| Algorithm | Main Feature |
|---|---|
| BFS | Searches level by level |
| DFS | Searches deeply first |
| DLS | DFS with a depth limit |
| Bidirectional | Searches from both ends |

## Result
Breadth First Search, Depth First Search, Depth Limited Search and Bidirectional Search were studied and implemented successfully.
