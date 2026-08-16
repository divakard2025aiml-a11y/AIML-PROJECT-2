

graph = {
    "Chennai": ["Bangalore", "Hyderabad"],
    "Bangalore": ["Chennai", "Mumbai", "Pune"],
    "Hyderabad": ["Chennai", "Pune"],
    "Mumbai": ["Bangalore", "Delhi"],
    "Pune": ["Bangalore", "Hyderabad", "Delhi"],
    "Delhi": ["Mumbai", "Pune"]
}


def depth_limited_search(current, goal, limit, path):

    path.append(current)

    if current == goal:
        return True

    if limit == 0:
        path.pop()
        return False

    for neighbour in graph[current]:

        if neighbour not in path:

            if depth_limited_search(
                neighbour,
                goal,
                limit - 1,
                path
            ):
                return True

    path.pop()
    return False


start = "Chennai"
goal = "Delhi"

depth_limit = 3
path = []

found = depth_limited_search(
    start,
    goal,
    depth_limit,
    path
)

print("DEPTH LIMITED SEARCH")
print("--------------------")
print("Starting City:", start)
print("Destination:", goal)
print("Depth Limit:", depth_limit)

if found:
    print("Path Found:", path)
    print("Number of Steps:", len(path) - 1)
else:
    print("Goal not found within the given depth limit.")