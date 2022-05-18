# Summary
- [Summary](#summary)
- [What are Data Structures?](#what-are-data-structures)
- [What is an Algorithm?](#what-is-an-algorithm)
- [Why are Data Structures and Algorithms important?](#why-are-data-structures-and-algorithms-important)
- [Types of Data Structures](#types-of-data-structures)
  - [Primitive](#primitive)
  - [Non-Primitive](#non-primitive)
    - [Linear (_Static, Dynamic_)](#linear-static-dynamic)
      - [Static (_Array_):](#static-array)
      - [Dynamic (_Linked List, Stack, Queue_)](#dynamic-linked-list-stack-queue)
      - [Stack](#stack)
    - [Non-Linear (_Tree, Graph_)](#non-linear-tree-graph)
      - [Graph](#graph)
- [Types of Algorithms](#types-of-algorithms)
  - [Simple recursive (Recursion)](#simple-recursive-recursion)
  - [Divide and conquer](#divide-and-conquer)
    - [Quick sort](#quick-sort)
    - [Merge sort](#merge-sort)
  - [Dynamic programming](#dynamic-programming)
  - [Greedy](#greedy)
  - [Brute force](#brute-force)
  - [Randomized](#randomized)

# What are Data Structures?
- Data Structures are different ways to organizing data on your computer, that can be used effectively.
- They directly impact the execution and the resources needed to run a specific task inside a program.

# What is an Algorithm?
- Set of steps/rules to accomplish a task

# Why are Data Structures and Algorithms important?
- for performing the most effective operations on the most adequate Data type
  - take some Data as input, process it, and use that result as an output

# Types of Data Structures
## Primitive
_Integer, Float, Character, String, Boolean_
- built in inside the Porgraming Language
## Non-Primitive
_Linear, Non-Linear_
- user-defined Data Structures, by combining 1 or more Primitive DS
- can be subdivided as:
### Linear (_Static, Dynamic_)
- arrenged in memory in a sequential manner
- can be:
#### Static (_Array_):
- associated memory locations are fixed at compile time
#### Dynamic (_Linked List, Stack, Queue_)
  - associated memory locations change
#### Stack
- **useful when** you have back and forward buttons in your applications
  - **FILO** "first in last out" nature
### Non-Linear (_Tree, Graph_)
- the data item is connected to several other items
  - they are not organized sequentially
#### Graph
- works great for maps

# [Types of Algorithms](#summary)
Algorithms can be classified based on the problem they are trying to solve (sorting algorithms) or they can be classified based on thte problem solving approach
## Simple recursive (Recursion)
- works in the same way as iterative algorithms, recursion X as a loop
<details open>
  <summary>sample code</summary>

  ```py
  Algorithm Sum(A,n)
    if n = 1
      return A[0]
    s = Sum(A, n-1) /* recurse on all but last */
    s = s + A[n-1] /* add last element */
  return s
  ```
</details>

## Divide and conquer
*Fall under this category the algorithms that contains at least 2 recursive calls*
It consists in 2 parts:
- Divide the problem into smaller subproblems of the same type, and solve these subprobles recursively
- Combine the solutions of the subproblems into a solution of the original problem
### Quick sort
Works based on the random number to chose a private number and make a decision based on these.
### Merge sort

## Dynamic programming
They work based on memoization, which means that these algorithms remember the past result and use them to find new results.
Used for optimization problems: find the best solution among other solutions

## Greedy
Finding the best solution for the local scope, it might not be the best solution considered an wider scope.
Work well for optimization problems.
We take the best we can without worrying about future problems.
We hope that by choosing a local optimum solution at each step, we will end up at a global optimum solution.

## Brute force
It tries all possibilities until a satisfactory solution is found, like finding the best path between two locations.

## Randomized
Use a random number at least once during the computation to make a decision