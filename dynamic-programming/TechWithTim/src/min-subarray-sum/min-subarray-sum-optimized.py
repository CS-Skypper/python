def min_subarray_sum_dp(array):
  if len(array) == 0:
    return 0

  min_sum_using_last_element = array[0]
  min_sum = array[0]

  for i in range(1, len(array)):
    num = array[i]
    current_min = min(num, num + min_sum_using_last_element)
    min_sum_using_last_element = current_min
    min_sum = min(min_sum, current_min)
  
  return min_sum