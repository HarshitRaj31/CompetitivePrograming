def bellman_ford(V, edges, source):

    dist = [999] * V
    dist[source] = 0

    # Repeat V-1 times
    for i in range(V - 1):

        for u, v, w in edges:

            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    print("Shortest distances:")

    for i in range(V):
        print(i, ":", dist[i])


# (source, destination, weight)
edges = [
    (0, 1, 4),
    (0, 2, 5),
    (1, 2, -3),
    (2, 3, 3)
]

bellman_ford(4, edges, 0)