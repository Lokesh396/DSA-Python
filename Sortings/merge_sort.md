The ***merge sort*** closely follows divide and conquer approach.

**Divide:** Divide the n-element sequence to be sorted into two subsequences of n/2 elements each.

**Conquer:** Sort the two subsequenes recursively using the merge sort.

**Combine:** Merge the two sorted subsequences to produce the sorted answer..

The recursion "bottoms out" when the sequence to be sorted has length 1, in which case there is no work to be done, since every sequence of length 1 is already sorted.

The key operation of merge sort algorithm is merge procedure. It will merge the two sorted subarrays into the single array. It just woks liked pack of cards on the table. where we have two piles of cards. We compare the top card of both the piles and place the correct card in the output pile, it any of the input piles is empty we place the other pile on the output pile. It takes $\Theta(n)$ to complete this procedure.
$\infty$
**Pseudocode**

```
MERGE(A, p, q, r)
1 n1 = q - p + 1
2 n2 = r - q
3 let L[1..n1 + 1] and R[1..n2 + 1] be new arrays
4 for i = 1 to n1
5    L[i] = A[p+i-1]
6 for j = 1 to n2
7    R[j] = A[q+j]
8 L[n1 + 1] = ∞
9 R[n2 + 1] = ∞
10 i = 1
11 j = 1
12 for k = p to r
13    if L[i] <= R[j]
14        A[k] = L[i]
15        i = i + 1
16    else
17        A[k] = R[j]
18        j = j + 1 

19 Merge_Sort(A, p , r)
20 if p < r
21     q = ⌊p + r / 2⌋
22     Merge_Sort(A, p, q)
23     Merge_Sort(A, q+1, r)
24     MERGE(A, p, q, r)
```

**Python Code**

```python
def merge(A, p, q, r):
    L = A[p:q]
    R = A[q:r+1]
    L.append(float('inf'))
    R.append(float('inf'))
    i = 0
    j = 0
    for k in range(p, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def merge_sort(A, p , r):
    if p < r:
        q = math.ceil((p + r)/2)
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)
```