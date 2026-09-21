
SIZE=10
hash_Table=[-1]*SIZE

def insert(key):

  index=key%SIZE
  for i in range(SIZE):
      index=(index+i*i)%SIZE
    
      while hash_Table[index]==-1:
            hash_Table[index]=key
            print(key,"inserted at  index",index)

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