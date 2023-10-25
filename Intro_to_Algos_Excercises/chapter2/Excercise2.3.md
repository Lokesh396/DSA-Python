####Excercise 2.3

###### 2.3-1 Using figure illustrate the operation of merge sort on the array using A =  [3, 41, 52, 26, 38, 57, 9, 49].

![merge illustration](../Images/merge_illustartion.jpg)


###### 2.3-2 Rewrite the Merge Procedure so that it doesn't use sentinels, instead stopping once either array L or r has had all its elements copied back to A and then copying the remainder of the other array back into A.

```
MERGE(A, p, q, r)
1 n1 = q - p +1
2 n2 = r - q
3 let L[1..n1] and R[1..n2] be new arrays
4 for i = 1 to n1
5    L[i] = A[p+i-1]
6 for j = 1 to n2
7    R[j] = A[q+j]
8 i = 1
9 j = 1
10 k = p
11 while k <= r 
12    if i <= n1 && j <= n2 &&  L[i] <= R[j]
13        A[k] = L[i]
14        i = i + 1
15    else if j <= n2
16        A[k] = R[j]
17        j = j + 1
18    else
19        break
20    k += 1
21 
22 for l = i to n1
23     A[k] = L[i]
24     i += 1
25     k += 1
26 for r = j to n2
27     A[k] = R[j]
28     j += 1
29     k += 1
```

###### 2.3-3 Use mathematical Induction to show that when n is an exact power of 2, the solution of recurrence $T(n) = 2 \text{ if } n = 2, 2T(n/2) + n \text{ if } n = 2^k, \text{ for } k > 1  \text{ is } T(n) = nlgn$.

**BaseCase**
when n = 2, $T(2) = 2 = 2lg2$. so the solution holds for the inital step.

**Inductive Step**
Let's assume there exists a k, greater than 1, such that $T(2^k) = 2^k lg 2^k$. we must prove that the formula holds for $k + 1$ too,i.e.$T(2^k+1) = 2^{k+1} lg 2^{k+1}$

From our recurrence Formula,
$T(2^{k+1}) = 2T(2^{k+1}/2) + 2^{k+1}$ 
= $2T(2^k) + 2.2^k$
= $2.2^klg2^k + 2.2^k$
= $2.2^k(lg2^k+1)$
= $2^{k+1}(lg2^k + lg 2)$
= $2^{k+1}lg2^{k+1}$
 
This completes the inductive step.
Since the both cases have been perfomed by mathematical induction, the statement $T(n) = nlgn$ holds for all n that are exact power of 2.

###### 2.3-4 We can express insertion sort as a recursivve procedure as follows. In order to sort A[1..n], we can recursively A[1..n-1] and then insert A[n] into the sorted array A[1..n-1].Write a recurrence for the running time of the recursive version of insertion sort.