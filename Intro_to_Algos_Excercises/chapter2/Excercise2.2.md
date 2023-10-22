#### Excercise 2.2

###### 2.2-1 Express the function $n^3 / 1000 - 100n^2 + 3$ in terms of $\Theta$-notation.

The higher order term in more significant then the lower order terms. So, the the running time is $\Theta(n^3)$.

###### Consider sorting n numbers stored in array A by first finding the smallest element of A and exchanging it with the element in A[1]. Then find the second smallest element of A, and exchange it with A[2]. Continue in this manner for the first $n-1$  elements of A. Write pseudocode for this algorithm, which is known as **selectionsort**. What loop invariant does this algorithm maintain? Why does it need to run for only the first $n-1$ elements, rather than for all n elements? Give the best-caseand worst-case running times of selection sort in ‚-notation.

```
SELECTION_SORT(A)
1 for i = 1 to A.length
2    min_index = i
3    for j = i+1 to A.length
4        if A[j] < A[min_index]
5            min_index = j
6    A[i], A[min_index] = A[min_index], A[i]
```

**Python Code**
```python
def Selection_Sort(A):
    for i in range(len(A)-1):
        min_index = i
        for j in range(i+1, len(A)):
            if A[j] < A[min_index]:
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]                
```

**Loop Invariants**

**Initialization:** Prior to the first iteration the elements from A[1..j-1] is sorted.
**Maintenance:** At the end of the loop, the elements from the A[1..j-1] is sorted and j was incremented by 1 by for loop.
**Termination:** When j is equals n, the loop is terminated and if we observe the elements in the array it is sorted.

**Worst Case**
In worst case the input is reversly sorted. so the line 3 needs to run **$(n(n+1)/2) - 1$** time, for j =2 it is need to check for n-j times, for j = 3 it needs to check for n-j times and so on `(summation of n numbers)` .

Therefore  the total taken for computing Selection Sort is a **quadratic function**. In general we call the worst case running time of Selection Sort  as $\Theta(n^2)$.

**Best Case**
The array is already sorted, but it needs to find the min index for every outer loop. So, the inner loop runs for **$(n(n+1)/2) - 1$** times.

Therefor the total taken for computing Selection Sort is a **quadratic Function**. In general we call the best case running time of Selection as $\Theta(n)$.

The reason why it needs to run for only n-1 times is that, by finding the min_value for every iteration we are placing them exactly in the position they need to be. If we place n-1 elements in their exact position then the $n^{th}$ element is already placed in its correct postion.

###### 2.2-3 Consider linear search again [(see Exercise 2.1-3)](Excercise2.1.md). How many elements of the input sequence need to be checked on the average, assuming that the element being searched for is equally likely to be any element in the array? How about in the worst case? What are the average-case and worst-case running times of linear search in ‚$\Theta$-notation? Justify your answers

**Average-Case Analysis:**

- If the element being searched for is equally likely to be any element in the array, then, on average, you would need to examine half of the elements in the array before finding the target.
- In this scenario, on average, you would check (n + 1) / 2 elements, where n is the total number of elements in the array. This is because, on average, you would find the target after checking approximately half of the elements.
- The average-case running time of linear search is $\Theta$(n), where n is the size of the array. It's linear in the size of the input.

**Worst-Case Analysis:**

- In the worst-case scenario, the element you are searching for is not present in the array, or it is the last element you check.
- This means that in the worst case, you would need to check all n elements in the array.
The worst-case running time of linear search is also $\Theta$(n).

###### 2.2-3 How can we modify almost any algorithm to have a good best-case running time?

By using the correct Algorithmic technique according to the problem and inputs we can modify almost all the algorithms to have a good best-case running time.