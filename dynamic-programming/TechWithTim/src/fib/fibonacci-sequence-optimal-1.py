
n = 5

def fib_memoization(n, cache={}):
  if n < 2:
    return n
  
  if n in cache:
    return cache[n]

  cache[n] = fib_memoization(n - 1, cache) + fib_memoization(n - 2, cache)
  # print(type(cache))
  return cache[n]

fib_memoization(n)
