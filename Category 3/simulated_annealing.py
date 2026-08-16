import random
import math
def objective_function(x):
    return -(x - 5) ** 2 + 25


def simulated_annealing(start):
    current = start
    temperature = 100

    while temperature > 0.1:

        # Generate a neighboring state
        next_state = current + random.choice([-1, 1])

        current_value = objective_function(current)
        next_value = objective_function(next_state)

        difference = next_value - current_value

        if difference > 0:
            current = next_state

        else:
            probability = math.exp(difference / temperature)

            if random.random() < probability:
                current = next_state
        temperature *= 0.95

    return current


start_state = 0

best_state = simulated_annealing(start_state)

print("Starting State:", start_state)
print("Best State Found:", best_state)
print("Best Value:", objective_function(best_state))