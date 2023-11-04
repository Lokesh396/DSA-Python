###### The maximum-subarray problem

The maximum-subarray problem states that we need to find the contiguous subarray sum which is the maximum in the total array. we call that array as contigius subarray the maximum subarray.

We can solve this problem using brute force where we compare every possible combination. It takes $\Theta(n^2)$.

The maximum-subarray problem is intresting only when the array contains some negative numbers. If all the array entiries were nonnegative, then the maximum-subarray problem would present no challenge, since the entire array would give the greateset sum.


**A solution using divide-and-conquer**

Divide and conquer suggests that we divide the subarray into two subarays of as equal size as possible.That is, we find the midpoint, say mid of the subarray, and consider the subarrays A[low..mid] and A[mid+1..high], any contiguous subarray must lie in one of the following places;

- entirely in the subarray A[loww..mid] so that low $\leq$ i $\leq$ j $\leq$ mid.
- entirely in the subarray A[mid+1..hight] so that mid < i $\leq$ j $\leq$ high, or 
- crossing the midpoint, so that low $\leq$ i $\leq$ j $\leq$ high.

The first two cases are the instances of the main problem, we can solve them recursively but the three case is not an instance of the subarray problem, it has an added restriction that it should cross the midpoint. we can solve this liear time. we first find maximum subarrays from A[low..mid] and A[mid+1...high] and we will combine them.

###### Pseudocode

```
FIND-MAX-CROSSING-SUBARRAY(A, low, mid, high)
1 left_sum = -∞
2 sum = 0
3 for i = mid downto low
4     sum = sum + A[i]
5     if sum > left_sum
6         left_sum = sum
7         max_left = i
8 right_sum = -∞
9 sum = 0
10 for j = mid+1 to high
11     sum = sum+A[j]
12     if sum > right_sum
13         right_sum = sum
14         max_right = j
15 return (max_left, max_right, left_Sum + right_sum)
```

It takes $\Theta(n)$ time. Since each of the two for loops take $\Theta(1)$ time for each iteration. we just need to count how many time the loop will run, it will run for n times beacuse the left loop runs mid - low + 1 times and right runs for high - mid times, so the total number of iterations is

$(mid - low + 1) + (high - mid) = high - low + 1 = n$

With a linear time FIND-MAX-CROSSING-SUBARRAY procedure in hand we can write pseudocode for a divide-and-conquer algorithm to solve the maximum subarray problem:


```
FIND-MAXIMUM-SUBARRAY(A, low, high)
1 if high == low
2    return(low, high, A[low])
3 else mid = ⌊(low+high)/2⌋
4    (left-low, left-high, left-sum) = FIND-MAXIMUM-SUBARRAY(A, low, mid)
5    (right-low, right-high, right-sum) = FIND-MAXIMUM-SUBARRAY(A, mid + 1, high)
6    (cross-low, cross-high, cross-sum) = FIND-MAX-CROSSING-SUBARRAY(A, low, mid, high)
7 if left-sum ≥ right-sum and left-sum ≥ cross-sum
8     return(left-low, left-high, left-sum)
9 elseif right-sum ≥ left-sum and right-sum ≥ cross-sum
10    return(right-low, right-high, right-sum)
11 else return(cross-low, cross-high, cross-sum)
```

**Analyzing the divide-and-conquer algorithm**

We need to setup a recurrence that describes the running time of the recursive FIND-MAXIMUM-SUBARRAY procedure.

lines 1 to 3 takes constant time $T(1) = \Theta(1)$
lines 4 and 5 takes $T(n/2)$ times each, as we are dividing the two halfs with n/2 elements each (assuming it as a power of 2). so in total it takes $2T(n/2)$.
line 6 takes $\Theta(n)$ time we already seen that
the lines 8,9,10 11 takes constant time that is $\Theta(1)$.

$T(n) = \Theta(1) + 2T(n/2) + \Theta(n) + \Theta(1)$
$ = 2T(n/2) + \Theta(n)$

$T(n) = \Theta(1) \text{ if } n = 1 , 2T(n/2)+\Theta(n) \text{ if } n > 1$.
The recrrence is same as the recurrence of mergesort, the solution for this recurrence is $T(n) = \Theta(nlgn)$.