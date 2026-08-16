

graph = {
    "Chennai": ["Bangalore", "Hyderabad"],
    "Bangalore": ["Chennai", "Mumbai", "Pune"],
    "Hyderabad": ["Chennai", "Pune"],
    "Mumbai": ["Bangalore", "Delhi"],
    "Pune": ["Bangalore", "Hyderabad", "Delhi"],
    "Delhi": ["Mumbai", "Pune"]
}


def dfs(current, goal, visited, path):

    visited.add(current)
    path.append(current)

    if current == goal:
        return True

    for neighbour in graph[current]:

        if neighbour not in visited:

            if dfs(neighbour, goal, visited, path):
                return True

    path.pop()
    return False


start = "Chennai"
goal = "Delhi"

visited = set()
path = []

dfs(start, goal, visited, path)

print("DEPTH FIRST SEARCH")
print("------------------")
print("Starting City:", start)
print("Destination:", goal)
print("Path Found:", path)
print("Number of Steps:", len(path) - 1)