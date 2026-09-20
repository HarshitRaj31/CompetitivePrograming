
SIZE=10
hash_Table=[[] for _ in range(SIZE)]

def insert(key):

  index=key%SIZE
  hash_Table[index].append(key)

def display():
    print("\nHash TABLE")
    for i in range(SIZE):
         print("Index",i,":",hash_Table[i])


insert(25)
insert(35)
insert(15)
insert(26)
  
# Display
display()   