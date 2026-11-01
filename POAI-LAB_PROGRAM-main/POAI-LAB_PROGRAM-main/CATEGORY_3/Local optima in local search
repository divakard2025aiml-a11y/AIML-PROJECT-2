# LOCAL OPTIMUM USING LOCAL SEARCH
states = {
    'A': 4,
    'B': 7,
    'C': 10,    # Local optimum
    'D': 6,
    'E': 15,    # Global optimum
    'F': 8,
    'G': 5

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

        current_value = states[current]

    
        best_neighbor = current

        for neighbor in neighbors[current]:

            if states[neighbor] > states[best_neighbor]:
                best_neighbor = neighbor
        if states[best_neighbor] <= current_value:

            print("\nNo better neighbour found.")
            print("Local Optimum Reached!")

            break

        
        current = best_neighbor

        print("Moving to:", current)
        print("Fitness:", states[current])

    return current

result = local_search('A')

print("\nFinal Result")
print("----------------------------")
print("Local Optimum:", result)
print("Fitness:", states[result])



=======================================================
OUTPUT:
=======================================================
LOCAL SEARCH
----------------------------
Starting State: A
Fitness: 4
Moving to: B
Fitness: 7
Moving to: C
Fitness: 10

No better neighbour found.
Local Optimum Reached!

Final Result
----------------------------
Local Optimum: C
Fitness: 10
