# GLOBAL OPTIMUM USING GLOBAL SEARCH

import random


states = {
    'A': 3,
    'B': 7,
    'C': 10,
    'D': 6,
    'E': 15,    # Global optimum
    'F': 8,
    'G': 5,
    'H': 12
}

neighbors = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['C', 'E'],
    'E': ['D', 'F', 'H'],
    'F': ['E', 'G'],
    'G': ['F', 'H'],
    'H': ['G', 'E']
}


def global_search(
        start,
        iterations=30,
        exploration_rate=0.4):

    current = start
    best = current

    print("GLOBAL SEARCH")
    print("============================")
    print("Starting State:", current)
    print("Initial Fitness:", states[current])

    for i in range(iterations):

        print("\nIteration", i + 1)



        if random.random() < exploration_rate:

            candidate = random.choice(
                list(states.keys())
            )

            print("Action: EXPLORATION")
            print("Randomly selected:", candidate)


        else:

            candidate = max(
                neighbors[current],
                key=lambda state: states[state]
            )

            print("Action: EXPLOITATION")
            print("Best neighbour:", candidate)

        print("Candidate Fitness:", states[candidate])

        if states[candidate] > states[current]:

            current = candidate

            print(
                "Improvement accepted:",
                current
            )

        else:

            print("No improvement.")


        if states[current] > states[best]:

            best = current

            print(
                "New best state:",
                best
            )

  
        if states[best] == max(states.values()):

            print("\nGlobal optimum reached!")

            break

    return best



result = global_search(
    start='A',
    iterations=30,
    exploration_rate=0.4
)

print("\n============================")
print("FINAL RESULT")
print("============================")
print("Global Optimum:", result)
print("Maximum Fitness:", states[result])



=================================================
OUTPUT:
==================================================
GLOBAL SEARCH
============================
Starting State: A
Initial Fitness: 3

Iteration 1
Action: EXPLOITATION
Best neighbour: B
Candidate Fitness: 7
Improvement accepted: B
New best state: B

Iteration 2
Action: EXPLORATION
Randomly selected: C
Candidate Fitness: 10
Improvement accepted: C
New best state: C

Iteration 3
Action: EXPLOITATION
Best neighbour: D
Candidate Fitness: 6
No improvement.

Iteration 4
Action: EXPLOITATION
Best neighbour: D
Candidate Fitness: 6
No improvement.

Iteration 5
Action: EXPLORATION
Randomly selected: H
Candidate Fitness: 12
Improvement accepted: H
New best state: H

Iteration 6
Action: EXPLOITATION
Best neighbour: E
Candidate Fitness: 15
Improvement accepted: E
New best state: E

Global optimum reached!

============================
FINAL RESULT
============================
Global Optimum: E
Maximum Fitness: 15
