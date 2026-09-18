SIZE = 10

# Create hash table
hash_table = [[] for _ in range(SIZE)]


def insert(key):
    index = key % SIZE

    hash_table[index].append(key)


def display():
    print("Hash Table:")

    for i in range(SIZE):
        print(i, ":", hash_table[i])


insert(25)
insert(35)
insert(15)
insert(26)

display()