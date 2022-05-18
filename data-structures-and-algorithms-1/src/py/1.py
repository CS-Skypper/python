

# take an input of n and return the sum of the numbers from 0 to n

def sum1(n):
  final_sum = 0           # let the var starts from 0
  for x in range(n+1):    #
    final_sum += x        # increments the var by +1 and assign the final value to x
    print("this is the value of x -> " + str(x))
    print('----')
  return final_sum        # 


#print(sum1(10))
#print(sum1(5))
print("this is the value of sum1 -> " + str(sum1(2)))

range(10)
