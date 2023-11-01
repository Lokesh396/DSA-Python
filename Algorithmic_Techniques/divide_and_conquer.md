### Divide and Conquer Approach

Many useful algorithms are recursive in structure: to solve a given problem, they
call themselves recursively one or more times to deal with closely related subproblems.
These algorithms typically follow a divide-and-conquer approach: they
break the problem into several subproblems that are similar to the original problem
but smaller in size, solve the subproblems recursively, and then combine these
solutions to create a solution to the original problem.

The divide-and-conquer paradigm involves three steps at each level of the recursion:

**Divide** the problem into a number of subproblems that are smaller instances of the
same problem.

**Conquer** the subproblems by solving them recursively. If the subproblem sizes are
small enough, however, just solve the subproblems in a straightforward manner.

**Combine** the solutions to the subproblems into the solution for the original problem.


**Recurrences**

Recurrences go hand in hand with the divide and conquer paradigm, because they give us natural way to  characterize the running time of divide and conquer algorithms. A **recurrence** is an equation or inequality that describes a function in terms of its value on smaller inputs.

Methods for solving recurrences- that is for obtaining asymptotic "$\Theta$" or "O" bounds on the solution:

- In the ***substitution method***, we guess a bound and then use mathematical induction to prove our guess correct.
- The ***recursion-treee method*** converts the recurrence into a tree whose node represents the cost incurred at various levels of the recursion. We use techniques for bounding summations to solve the recurrence.

- The ***master method*** provides bounds for recurrences of the form

    $T(n) = aT(n/b) + f(n)$
where a>=1, b>1 anf f(n) is a given function.

###### The maximum-subarray problem

The maximum-subarray problem states that we need to find the contiguous subarray sum which is the maximum in the total array. we call that array as contigius subarray the maximum subarray.

We can solve this problem using brute force where we compare every possible combination. It takes $\Theta(n^2)$.
