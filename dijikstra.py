V = 4

graph = [
    [0, 4, 2, 0],
    [4, 0, 0, 1],
    [2, 0, 0, 3],
    [0, 1, 3, 0]
]

distance = [999] * V
visited = [False] * V

source = 0
distance[source] = 0


for i in range(V):

    # Find minimum distance vertex
    minimum = 999
    u = -1

    for j in range(V):
        if not visited[j] and distance[j] < minimum:
            minimum = distance[j]
            u = j

    visited[u] = True

    # Update distances
    for v in range(V):

        if graph[u][v] != 0 and not visited[v]:

            new_distance = distance[u] + graph[u][v]

            if new_distance < distance[v]:
                distance[v] = new_distance


print("Shortest distances:")

for i in range(V):
    print(i, ":", distance[i])