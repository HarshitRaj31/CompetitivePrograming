V = 4

edges = [
    (2, 0, 1),
    (3, 0, 2),
    (1, 1, 3),
    (4, 2, 3)
]

# Sort edges by weight
edges.sort()

parent = list(range(V))


def find(x):
    while parent[x] != x:
        x = parent[x]

    return x


total = 0
count = 0

for weight, u, v in edges:

    root1 = find(u)
    root2 = find(v)

    # If different, no cycle
    if root1 != root2:

        print(u, "->", v, "=", weight)

        parent[root1] = root2

        total += weight
        count += 1

        if count == V - 1:
            break


print("Total cost =", total)