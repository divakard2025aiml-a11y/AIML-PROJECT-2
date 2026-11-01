# GLOBAL OPTIMUM USING LOCAL SEARCH

states = {
    'A': 2,
    'B': 5,
    'C': 8,
    'D': 12,
    'E': 15,    
    'F': 10,
    'G': 6
}

neighbors = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['C', 'E'],
    'E': ['D', 'F'],
    'F': ['E', 'G'],
    'G': ['F']
}


def local_search(start):

    current = start

    print("LOCAL SEARCH")
    print("----------------------------")
    print("Starting State:", current)
    print("Fitness:", states[current])

    while True:

        best_neighbor = current


        for neighbor in neighbors[current]:

            if states[neighbor] > states[best_neighbor]:

                best_neighbor = neighbor

    
        if states[best_neighbor] <= states[current]:

            break

        current = best_neighbor

        print(
            "Exploitation ->",
            current,
            "Fitness =",
            states[current]
        )

    return current



result = local_search('A')

print("\nFinal Result")
print("----------------------------")
print("Global Optimum Found:", result)
print("Fitness:", states[result])


=====================================================
OUTPUT:
=====================================================
LOCAL SEARCH
----------------------------
Starting State: A
Fitness: 2
Exploitation -> B Fitness = 5
Exploitation -> C Fitness = 8
Exploitation -> D Fitness = 12
Exploitation -> E Fitness = 15

Final Result
----------------------------
Global Optimum Found: E
Fitness: 15
