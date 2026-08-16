from collections import deque
graph = {
    "Chennai": ["Bangalore", "Hyderabad"],
    "Bangalore": ["Chennai", "Mumbai", "Pune"],
    "Hyderabad": ["Chennai", "Pune"],
    "Mumbai": ["Bangalore", "Delhi"],
    "Pune": ["Bangalore", "Hyderabad", "Delhi"],
    "Delhi": ["Mumbai", "Pune"]
}


def bfs(start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:

        path = queue.popleft()
        current = path[-1]

        if current == goal:
            return path

        if current not in visited:
            visited.add(current)

            for neighbour in graph[current]:
                if neighbour not in visited:
                    new_path = path + [neighbour]
                    queue.append(new_path)

    return None


start = "Chennai"
goal = "Delhi"

result = bfs(start, goal)

print("BREADTH FIRST SEARCH")
print("--------------------")
print("Starting City:", start)
print("Destination:", goal)
print("Path Found:", result)
print("Number of Steps:", len(result) - 1)