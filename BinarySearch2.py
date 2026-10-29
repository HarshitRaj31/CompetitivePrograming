
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            high = mid - 1  
        else:
            low = mid + 1   
    return -1

arr = [90,80,70,60,50,40,30]
key = 50
result = binary_search(arr, key)
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
