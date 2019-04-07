# iterative binary search:
def binary_search(arr, target):
    low =0
    high = len(arr) -1
    while low <= high:
        middle = (low + high)/2
        if target < arr[middle]:
            high = middle -1 # eliminate RHS
        elif target > arr[middle]:
            low = middle + 1 # eliminate LHS
        else:
            return middle
    return -1 # not found
    # the time complexity is O(log(n)) = logorithmic


# recursive binary search:
# def binary_search_recusive(arr, target):