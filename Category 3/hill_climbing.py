def objective_function(x):
    return -(x - 5) ** 2 + 25

def hill_climbing(start):
    current = start

    while True:
        current_value = objective_function(current)

        left = current - 1
        right = current + 1

        left_value = objective_function(left)
        right_value = objective_function(right)

        # Find the best neighboring state
        if left_value > current_value:
            current = left

        elif right_value > current_value:
            current = right

        else:
            break

    return current

start_state = 0

best_state = hill_climbing(start_state)

print("Starting State:", start_state)
print("Local/Global Optimum:", best_state)
print("Maximum Value:", objective_function(best_state))