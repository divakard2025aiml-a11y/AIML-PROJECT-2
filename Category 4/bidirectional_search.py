from collections import deque
graph = {
    "Chennai": ["Bangalore", "Hyderabad"],
    "Bangalore": ["Chennai", "Mumbai", "Pune"],
    "Hyderabad": ["Chennai", "Pune"],
    "Mumbai": ["Bangalore", "Delhi"],
    "Pune": ["Bangalore", "Hyderabad", "Delhi"],
    "Delhi": ["Mumbai", "Pune"]
}


def bidirectional_search(start, goal):

    if start == goal:
        return [start]

    # Forward search
    front_queue = deque([start])
    front_visited = {start: None}

    # Backward search
    back_queue = deque([goal])
    back_visited = {goal: None}

    while front_queue and back_queue:

        # Expand from start
        current = front_queue.popleft()

        for neighbour in graph[current]:

            if neighbour not in front_visited:

                front_visited[neighbour] = current
                front_queue.append(neighbour)

                if neighbour in back_visited:
                    return build_path(
                        neighbour,
                        front_visited,
                        back_visited
                    )

        # Expand from goal
        current = back_queue.popleft()

        for neighbour in graph[current]:

            if neighbour not in back_visited:

                back_visited[neighbour] = current
                back_queue.append(neighbour)

                if neighbour in front_visited:
                    return build_path(
                        neighbour,
                        front_visited,
                        back_visited
                    )

    return None


def build_path(meeting_point, front_visited, back_visited):

    front_path = []
    current = meeting_point

    while current is not None:
        front_path.append(current)
        current = front_visited[current]

    front_path.reverse()

    back_path = []
    current = back_visited[meeting_point]

    while current is not None:
        back_path.append(current)
        current = back_visited[current]

    return front_path + back_path


start = "Chennai"
goal = "Delhi"

result = bidirectional_search(start, goal)

print("BIDIRECTIONAL SEARCH")
print("--------------------")
print("Starting City:", start)
print("Destination:", goal)
print("Path Found:", result)

if result:
    print("Number of Steps:", len(result) - 1)