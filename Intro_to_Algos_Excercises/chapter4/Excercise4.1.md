#### Excercise 4.1

###### 4.1-1 What does FIND-MAXIMUM-SUBARRAY  return when all the elements of A are negative? 

The FIND-MAXIMUM-SUBARRAY return the index of the highest negative number in the array.

###### 4.1-2 Write pseudocode for the brute-force method for solving the maximum-subarray problem. you procedure should run in $\Theta(n^2)$ time.

```
MAXIMUM-SUBARRAY-SUM-BRUTE-FORCE(A, low, high)
1 max-sum = -∞
2 left-index = null
3 right-index = null
4 for i = low to high
5   sum  = 0
6    for j = i to high
7        sum = sum + A[j]
8        if sum > max-sum
9             if i == j left-index = i
10            max-sum = sum
11            right-index = j
12   return(left-index, right-index, max-sum)
```

###### 4.1-3 Implement both the brute-force and recursive algorithms for the maximumsubarray problem on your own computer. What problem size n~0~ gives the crossover point at which the recursive algorithm beats the brute-force algorithm? Then, change the base case of the recursive algorithm to use the brute-force algorithm whenever the problem size is less than n~0~. Does that change the crossover point?


***Brute-Force***
```python
def maximum_subarray_sum(A, low, high):
    max-sum = -float('inf')
    left-index = None
    right-index = None
    for i in range(low, high):
        sum = 0
        for j in range(i, high):
            sum = sum + A[j]
            if sum > max-sum:
                if i == j left-index = i
                max-sum = sum
                right-index = j
    return(left-index, right-index, max-sum)
```

***Recursive***

```python
import math
def maximum_cross_subarray_sum(A, low, mid, high):
    pass

def maximum_subarray_sum(A, low, high):
    if low == high:
        return(low, high, A[low])
    else:
        mid = math.floor((high+low)/2)
```