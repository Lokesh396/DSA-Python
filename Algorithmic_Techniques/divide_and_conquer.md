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