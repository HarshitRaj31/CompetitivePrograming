SIZE = 10

hash_table = [-1] * SIZE


def insert(key):
    original_index = key % SIZE

    for i in range(SIZE):

        index = (original_index + i * i) % SIZE

        if hash_table[index] == -1:
            hash_table[index] = key
            print(key, "inserted at index", index)
            return

    print("Hash table is full!")


def display():
    for i in range(SIZE):
        print("Index", i, ":", hash_table[i])


insert(25)
insert(35)
insert(15)

display()