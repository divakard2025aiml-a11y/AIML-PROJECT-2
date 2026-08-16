# Local Beam Search

states = {
    "A": 5,
    "B": 12,
    "C": 8,
    "D": 15,
    "E": 10,
    "F": 18,
    "G": 20,
    "H": 14
}

k = 3

current_states = ["A", "B", "C"]

print("Initial States:", current_states)

for iteration in range(3):

    print("\nIteration", iteration + 1)

    candidates = set()

    for state in current_states:
        index = list(states.keys()).index(state)

        if index > 0:
            candidates.add(list(states.keys())[index - 1])

        if index < len(states) - 1:
            candidates.add(list(states.keys())[index + 1])

    
    candidates.update(current_states)

    current_states = sorted(
        candidates,
        key=lambda state: states[state],
        reverse=True
    )[:k]

    print("Best States:", current_states)

best_state = max(current_states, key=lambda state: states[state])

print("\nBest State Found:", best_state)
print("Best Value:", states[best_state])