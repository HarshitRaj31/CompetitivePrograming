SIZE = 10

# Create hash table
hash_table = [-1] * SIZE


def insert(key):
    index = key % SIZE

    # Linear probing
    while hash_table[index] != -1:
        index = (index + 1) % SIZE


    hash_table[index] = key
    print(key, "inserted at index", index)


def display():
    print("\nHash Table:")

    for i in range(SIZE):
        print("Index", i, ":", hash_table[i])


# Insert elements
insert(25)
insert(35)
insert(15)
insert(26)

# Display
display()