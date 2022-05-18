[Course Link: Dynamic Programming explained with practical examples](https://www.youtube.com/watch?v=Sz9yH-RDAgo)

# Dynamic Programming
Dynamic Programming (DP) is an algorithmic technique for solving an optimization problem by breaking it down into simpler subproblems and utilizing the fact that the optimal solution to the overall problem depends upon the optimal solution to its subproblems
- find the best solution out of multiple solutions

## Fibonacci index calculator
- ### Unpotionized solution O(2^n)
The time complexity of this solution is very high, unoptimized
- **O(2^n)**
  - Ending up doing the same calculations a lot times
  - To [optimize](#optimized-solution-on) the solution we should store the calculated values in order to faster access it
- [fibonacci-sequence-trivial.py](src/fib/fibonacci-sequence-trivial.py)

- ### Optimized solution O(n)
Using the **memoization technique** (a cache) because there is no point to calculate the values which we already had calculated
- A linear number of computations
- [fibonacci-sequence-optimal-1.py](src/fib/fibonacci-sequence-optimal-1.py)
- [fibonacci-sequence-optimal-2.py](src/fib/fibonacci-sequence-optimal-2.py)

## Minimum sum for a continuous subarray
- ### Unpotionized solution O(n^2)
- [min-subarray-sum-trivial.py](src/min-subarray-sum/min-subarray-sum-trivial.py)
