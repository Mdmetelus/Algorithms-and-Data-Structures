def linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1  # not found
    
    # the time complexity is O(n) =linear
