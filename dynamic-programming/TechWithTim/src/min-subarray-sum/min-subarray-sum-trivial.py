def min_subarray_sum(array):
  if len(array) == 0:
    return 0

  min_sum = float("inf")

  for i in range(len(array)):
    for j in range(i + 1, len(array) + 1):
      subarray = array[i: j]
      min_sum = min(min_sum, sum(subarray))
  
  return min_sum