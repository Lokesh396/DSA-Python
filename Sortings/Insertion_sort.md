##### Insertion Sort

Insertion Sort is an efficient algorithm for sorting a small number of elements. The Algorithm sorts the input numbers **in place**: it rearranges the numbers with in the array A, with most a constant number stored outside the array at any time. The input array A contains the sorted array after insertion-sort procedure is finished.

##### Intution

###### How Insertion sort works ?

Insertion sort works the way we play cards, we start with a empty left hand and the cards face down on the table. we take one card from the table and insert the card in it's correct position in the left hand. To find the correct position we compare with each card already presents in the hand. At all times, the cards in the left hand is sorted.

##### Pseudocode

```
INSERTION-SORT(A)
1 for j =2 to A.length
2    key = A[j]
3    // Insert A[j] into the sorted sequence of A[1..j-1]
4    i = j - 1
5    while i > 0 and A[i] >  key
6        A[i+1] = A[i]
7        i = i-1
8    A[i+1] = key
```

##### Python code

```python

def Insertion_Sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i- 1
        A[i+1] = key
```

##### Loop Invariants and correctness of Insertion sort.

At the beggining of each for loop, which is indexed by j, we have A[1..j-1] constitues the currently sorted hand and the remaining cards are the ones which is still on the table. The elements in A[1..j-1] are the elements originally in positions 1 through j-1, now in sorted order. we state these properties of A[1..j-1] as loop invariant.

**Initialization:** It is true prior to the first iteration of the loop.
**Maintenance:** If it is true before an iteration of the loop, it remains true before the next iteration.
**Termination:** When the loop terminates, the invariant gives us a useful property that shows that the algorithm is correct.

###### Loop Invarinats for Insertion Sort

**Initialization:** Prior to the first iteration the elements from A[1..j-1] is sorted.
**Maintenance:** At the end of the loop, the elements from the A[1..j-1] is sorted and j was incremented by 1 by for loop.
**Termination:** When j is greater than n, the loop is terminated and if we observe the elements in the array it is sorted.



###### Analysis of Insertion Sort

The time taken by Insertion Sort depends on the input size: sorting thousand numbers takes more time than sorting three numbers.More over it takes different amount of time based on how nearly the numbers in the input is sorted. In general, the time taken by an algorithm grows with the size of the input, so it is traditional to describe the running time of a program as a function of the size of its input.

The running time of the algorithm is the sum of the running time for each statement exected.

**Worst Case**
In worst case the input is reversly sorted, where the new card in the right hand need to check for every card presents in the left hand. so the line 5 needs to run **$(n(n+1)/2) - 1$** for j =2 it is need to check for 1 time, for j = 3 it needs to check for 2 times and so on `(summation of n numbers)` .

Therefore  the total taken for computing InsertionSort is a **quadratic function**. In general we call the worst case running time of InsertionSort  as $\Theta(n^2)$.

**Best Case**
The array is already sorted, where the new card in the right needs to check only one card . so the line executes only one time for every j.

Therefor the total taken for computing InsertionSort is a **Linear Function**. In general we call the best case running time of InsertionSort as $\Theta(n)$.