#### Strassen's Algorithm for matrix multiplication

If A = (a~ij~) and B = (b~ij~) are some $n * n$ matrices, then the product *C = A.B*, we define entry c~ij~, for i, j = 1,2,...n, by
$c_{ij} = \sum_{k=1}^{n} a_{ik}.b_{kj}$

We must compute n2 matrix entries, and each is the sum of n values. The following procedure takes n * n matrices A and B and multiplies them, returning their n * n product C. We assume that each matrix has an attribute rows, giving the number of rows in the matrix.

**PseudoCode**

```
SQUARE-MATRIX-MULTIPLICATION(A, B)
1 n = A.rows
2 let C be a new n * n matrix
3 for i = 1 to n
4   for j = 1 to n
5       cij = 0
6       for k = 1 to n
7           cij = cij + aik . bkj
8 return C
```

Each of the triply-nested for loops runs exactly n iterations, and each execution of line 7 takes constant time, the SQUARE-MATRIX-MULTIPLY procedure takes $\Theta(n^3)$ time.

**A simple divide-and-conquer algorithm**

To keep things simple, when we use a divide-and-conquer algorithm to compute the matrix product C = A * B, we assume that n is an exact power of 2 in each of the n * n matrices. We make this assumption because in each divide step, we will divide n * n matrices into four $n/2 * n/2$ matrices, and by assuming that n is an exact power of 2, we are guaranteed that as long as n $\ge$ 2, the dimension n=2 is an integer.

A = $\begin{matrix}&A_{11}&A_{12}\\&A_{21}&A_{22}\end{matrix}$

B = $\begin{matrix}&B_{11}&B_{12}\\&B_{21}&B_{22}\end{matrix}$

C  = $\begin{matrix}&C_{11}&C_{12}\\&C_{21}&C_{22}\end{matrix}$

The above is the equation (4.9)
 
$C = A.B$

$C_{11} = A_{11}.B_{11} + A_{12}.B_{21}$
$C_{12} = A_{11}.B_{12} + A_{12}.B_{22}$
$C_{13} = A_{21}.B_{11} + A_{22}.B_{21}$
$C_{14} = A_{21}.B_{12} + A_{22}.B_{22}$

Each of these four equations specifies two multiplications of $n/2 * n/2$ matrices and the addition of their n/2 * n/2 products. We can use these equations to create a straightforward, recursive, divide-and-conquer algorithm:

**PseudoCode**

```
SQUARE-MATRIX-MULTIPLY-RECURSIVE(A, B)
1 n = A.rows
2 let C be a new n * n matrix
3 if n == 1
4   c11 = a11 . b11
5 else partition A,B, and C as in equation (4.9)
6   C11 = SQUARE-MATRIX-MULTIPLY-RECURSIVE(A11, B11) + SQUARE-MATRIX-MULTIPLY-RECURSIVE(A12, B21)
7   C12 = SQUARE-MATRIX-MULTIPLY-RECURSIVE(A11, B22) + SQUARE-MATRIX-MULTIPLY-RECURSIVE(A12, B22)
8   C21 = SQUARE-MATRIX-MULTIPLY-RECURSIVE(A21, B11) + SQUARE-MATRIX-MULTIPLY-RECURSIVE(A22, B21)
9   C22 = SQUARE-MATRIX-MULTIPLY-RECURSIVE(A21, B12) + SQUARE-MATRIX-MULTIPLY-RECURSIVE(A22, B22)
10 return C
```