def selection_sort(arr):
  for i in range(0, len(arr) -1):
      current_index = i
      smallest_index = current_index

      for j in range(current_index, len(arr)):
          if arr[j] < arr[smallest_index]:
              smallest_index = j
        
      # swap
      temp = arr[smallest_index]
      arr[smallest_index] = arr[current_index]
      arr[current_index] = temp


return arr

# the time complexity is O(n**2) = Quadratic
# because of the nested for loops