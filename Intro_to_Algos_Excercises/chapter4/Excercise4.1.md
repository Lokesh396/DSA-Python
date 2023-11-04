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
    max_sum = -float('inf')
    left_index = None
    right_index = None
    for i in range(low, high):
        temp_sum = 0
        for j in range(i, high):
            temp_sum = temp_sum + A[j]
            if temp_sum > max_sum:
                if i == j left_index = i
                max_sum = temp_sum
                right_index = j
    return(left_index, right_index, max_sum)
```

***Recursive***

```python
import math
def maximum_cross_subarray_sum(A, low, mid, high):
    left_sum = -float('inf')
    right_sum = -float('inf')
    max_left = None
    max_right = None
    temp_sum = 0
    for i in range(mid, low-1, -1):
        temp_sum = temp_sum + A[i]
        if temp_sum > left_sum:
            left_sum = temp_sum
            max_left = i
    temp_sum = 0
    for j in range(mid+1, high):
        temp_sum = temp_sum + A[j]
        if temp_sum > right_sum:
            right_sum = temp_sum
            max_right = j
    return(max_left, max_right, left_sum + right_sum)
    

def maximum_subarray_sum(A, low, high):
    if low == high:
        return(low, high, A[low])
    else:
        mid = math.floor((high+low)/2)
        left_low, left_high, left_sum = maximum_subarray_sum(A, low, mid)
        right_low, right_high, right_sum = maximum_subarray_sum(A, mid+1, high)
        cross_low, cross_high, cross_sum = maximum_cross_subarray_sum(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return(cross_low, cross_high, cross_sum)
```

###### 4.1-4 Suppose we change the definition of the maximum-subarray problem to allow the result to be an empty subarray, where sum of the values of an empty subarray is 0.How would you change any of algorithms that do not allow empty subarrays to permit an empty subarray to be the result?

we can initialize left-sum and right-sum to zero instead of −∞ as we are not going to accept any negative sum as the answer in FIND-MAX-CROSSING-SUBARRAY.

###### 4.1-5 Use the following ideas to develop a nonrecursive, linear-time algorithm for the maximum-subarray problem. Start at the left end of the array, and progress toward the right, keeping track of the maximum subarray seen so far. Knowing a maximum subarray of A[1...j], extend the answer to find a maximum subarray ending at index j+1 by using the following observation: a maximum subarray of A[1..j+1] is either a maximum subarray of A[1...j] or a subarray A[1..j+1], for some 1 $\leq$ i$\leq$  j + 1.Determine a maximum subarray of the form A[i..j+1] in constant time based on knowing a maximum subarray ending at index j .


```python
def max_subarray_sum(A):
    low = 0
    high = 0
    max_sum = -float('inf')
    temp_sum = 0
    current_left  = 0
    for i in range(len(A)):
        temp_sum += A[i]
        if temp_sum  > max_sum:
            high = i
            low = current_left
            max_sum = temp_sum
        if temp_sum < 0:
            temp_sum = 0
            current_left = i + 1
    return(low, high, max_sum)
```

Using [*Kadane's*](https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/) Algorithm


```python
def maxSubArray(nums):
    cm = nums[0]
    gm = nums[0]
    for i in range(1, len(nums)):
        cm = max(nums[i], cm + nums[i])
        gm = max(gm, cm)

    return gm
```
