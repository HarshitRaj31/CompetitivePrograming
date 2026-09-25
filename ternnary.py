def ternary_search(arr, left, right, key):
    if left > right:
        return -1

    mid1 = left + (right - left) // 3
    mid2 = right - (right - left) // 3

    if arr[mid1] == key:
        return mid1

    if arr[mid2] == key:
        return mid2

    if key < arr[mid1]:
        return ternary_search(arr, left, mid1 - 1, key)

    elif key > arr[mid2]:
        return ternary_search(arr, mid2 + 1, right, key)

    else:
        return ternary_search(arr, mid1 + 1, mid2 - 1, key)


# Main
arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
key = 70

result = ternary_search(arr, 0, len(arr) - 1, key)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")