graph = {
    0: [1, 2],
    1: [3, 4],
    2: [],
    3: [],
    4: []
}

visited = set()


def dfs(node):
    visited.add(node)

    print(node, end=" ")

    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(neighbour)


dfs(0)