def fib_memoization(n, cache={0:1, 1:1}):  
  if n in cache:
    return cache[n]

  cache[n] = fib_memoization(n - 1, cache) + fib_memoization(n - 2, cache)
  return cache[n]