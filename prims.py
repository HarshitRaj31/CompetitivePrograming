V = 4

graph = [
    [0, 2, 3, 0],
    [2, 0, 0, 1],
    [3, 0, 0, 4],
    [0, 1, 4, 0]
]

visited = [0] * V

visited[0] = True

total = 0

for i in range(V - 1):

    minimum = 999
    x = -1
    y = -1

    for j in range(V):
        if visited[j]:

            for k in range(V):
                if not visited[k] and graph[j][k] != 0:

                    if graph[j][k] < minimum:
                        minimum = graph[j][k]
                        x = j
                        y = k

    print(x, "->", y, "=", minimum)

    visited[y] = True
    total += minimum

print("Total cost =", total)