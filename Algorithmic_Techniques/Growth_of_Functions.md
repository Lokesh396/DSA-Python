#### Asymptotic Notations

When we look at input sizes large enough to make only the order of growth of the running timr relevant, we are studying the **asymptotic** efficiency of the algorithms. That is, we are concerned  with how the runnning time of an algorithm increases with the size of the input in the limit, as the size of the input increases without bound. Usually, an algorithm that is asymptotically more efficient will be the best choice for all but very small inputs.

**$\Theta$-notation**

For a given function $g(n)$, we denote by $\Theta(g(n))$ the set of functions.

$\Theta(g(n))$ = there exists positive constants c~1~, c~2~, n~0~ such that 0<= c~1~g(n) <= f(n) <= c~2~g(n) for all n >= n~0~.


**O-notation**

The $\Theta$-notation bounds a function from above and below.When we have only an **asymptotic upper bound**, we use O-notaion. For a given function $g(n)$, we denote $O(g(n))$ the set of functions.

$O(g(n))$ = f(n) : there exists positve constants c and n~0~ such that 0<= f(n) <= cg(n) for all n >= n~0~.

**$\Omega$-notation**

Just as *O*-notation provides an asymptotic upper bound on a function, $\Omega$-notation provides an **asymptotic lower bound**.For a given function g(n), we denote by $\Omega$(g(n)) the set of functions

$\Omega(g(n)) = f(n) : there exists positive constants c and n~0~ such that 0<= cg(n) <= f(n) for all n >= n~0~.

**Explanation**

![Asymptotic notation](./images/asymptotic-notations.png)


Theorem 3.1

For any two functions $f(n)$ and $g(n)$, we have $f(n) = \Theta(g(n))$ if and only if $f(n) = O(g(n))$ and $f(n) = \Omega(g(n))$.

**o-notation**

The asymptotic upper bound provided by the *O*-notation may or may not be asymptotically tight. The bound $2n^2$ = $O(n^2)$ is asymptotically tight but the bound $2n = O(n^2)$ id not. we use **o-notation** to denote an upper bound that is not asymptotically tight. we formally define $o(g(n))$ as the set

$o(g(n)) = f(n) : $ for any positive constant $c > 0$, there exists a constant n~0~ > 0 such that $0 <= f(n) < c(g(n))$ for all $n >= n$~0~.

For example, $2n = o(n^2)$, but $2n^2 \neq o(n^2)$.

**$\omega$-notation**

By analogy $\omega$-notation is to $\Omega$ as *o*-notation is to *O*-notation. We use $\omega$-notation to denote a lower bound that is not asymptotically tight. One way yo define it is by $f(n) \in \omega(g(n))$ if and only if $g(n) \in o(f(n))$.
Formally, however, we define $w(g(n))$ as the set
$\omega(g(n))  = f(n) :$for any positive constant $c > 0$, there exists a constant $n~0~ > 0$ such that $0<= c(g(n)) < f(n)$ for all $n >= n$~0~.
