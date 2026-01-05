def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1

arr = [3, 5, 7, 9, 10, 14]   
target = 5

result = binary_search(arr, target)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")
