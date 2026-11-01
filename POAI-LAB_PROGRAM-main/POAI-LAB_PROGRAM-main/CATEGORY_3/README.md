# EXPERIMENT 3 – OPTIMIZATION TECHNIQUES

## Aim
To study optimization techniques and implement local search algorithms using Python.

## Introduction
Optimization is the process of finding the best possible solution from a set of available solutions.

## 1. Local Optima

A local optimum is a solution that is better than its nearby solutions but may not be the best solution overall.

**Example:** A hill climber reaches the top of a small hill but another higher hill exists elsewhere.

## 2. Global Optima

A global optimum is the best solution among all possible solutions.

**Example:** Finding the highest point across an entire mountain range.

## 3. Exploration and Exploitation

- **Exploration:** Searching new areas to discover better solutions.
- **Exploitation:** Improving the current solution using the information already available.

A good optimization algorithm balances both techniques.

## 4. Hill Climbing Algorithm

Hill Climbing is a local search algorithm that repeatedly moves towards a better neighboring solution.

**Working:**
1. Start with an initial solution.
2. Evaluate its neighboring solutions.
3. Select a better neighbor.
4. Repeat until no better neighbor is available.

**Example:** Solving the Eight Queens Problem by reducing the number of attacking queen pairs.

**Limitation:** It can get stuck at a local optimum.

## 5. Simulated Annealing Algorithm

Simulated Annealing is an optimization algorithm inspired by the cooling process of metals.

It sometimes accepts a worse solution to escape local optima.

**Working:**
1. Start with an initial solution and high temperature.
2. Generate a neighboring solution.
3. Calculate the change in solution quality.
4. Accept better solutions.
5. Sometimes accept worse solutions based on temperature.
6. Gradually reduce the temperature.
7. Stop when the temperature becomes very low.

**Example:** Generating a college timetable with minimum subject conflicts.

## 6. Local Beam Search

Local Beam Search maintains multiple candidate solutions at the same time.

**Working:**
1. Generate several initial solutions.
2. Evaluate all solutions.
3. Select the best candidates.
4. Generate their neighboring solutions.
5. Repeat until a good solution is found.

**Example:** Finding a good arrangement for the Eight Queens Problem.

## Applications

### Eight Queens Problem
Place eight queens on a chessboard so that no two queens attack each other.

### Job Scheduling
Assign jobs to available machines or time slots while reducing delays and conflicts.

### Travelling Salesman Problem
Find a shortest possible route that visits every city once and returns to the starting city.

### Timetable Generation
Arrange subjects, classrooms and time slots without scheduling conflicts.

## Comparison

| Algorithm | Main Idea |
|---|---|
| Hill Climbing | Moves to a better neighbor |
| Simulated Annealing | Sometimes accepts worse solutions |
| Local Beam Search | Maintains multiple candidate solutions |

## Result
Different optimization concepts and local search algorithms were studied and implemented successfully.
