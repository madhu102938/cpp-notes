### Overlapping Subproblems
Overlapping subproblems is a property of some problems that can be solved using dynamic programming. It refers to the fact that the same subproblems are often solved multiple times in the process of solving the larger problem.

For example, in the Fibonacci sequence, the value of `fibo(n)` depends on the values of `fibo(n-1)` and `fibo(n-2)`. As a result, when computing `fibo(n)`, we need to compute `fibo(n-1)` and `fibo(n-2)` separately. However, these subproblems are also needed when computing `fibo(n-1)` and `fibo(n-2)`, respectively. This leads to redundant computation of the same subproblems.

Dynamic programming solves this problem by storing the results of subproblems in a memoization table, which can be used to avoid re-computing the same subproblems multiple times. By storing the results of subproblems, we can reduce the time complexity of the algorithm from exponential to polynomial.

In general, problems that exhibit overlapping subproblems can be solved using dynamic programming. The key is to identify the subproblems and the relationships between them, and to use memoization or tabulation to store the results of subproblems for future use.

<hr>
### Memoization
Memoization is a technique used in dynamic programming to speed up the computation of subproblems by storing their results in a memoization table. The memoization table is used to avoid re-computing the same subproblems multiple times, leading to a significant speedup in the computation of larger problems.

In memoization, the results of subproblems are stored in a table, typically implemented as an array or a hash table. When a subproblem needs to be solved, the algorithm first checks if the result is already stored in the memoization table. If so, the stored result is returned. Otherwise, the subproblem is solved recursively, and the result is stored in the memoization table for future use.

Memoization is particularly useful when the same subproblems are solved multiple times in the process of solving the larger problem. By storing the results of subproblems, we can avoid redundant computation and reduce the time complexity of the algorithm.

Memoization can be used to solve a wide range of problems, including the Fibonacci sequence, the longest common subsequence problem, and the knapsack problem, among others. The key is to identify the subproblems and the relationships between them, and to use memoization to store the results of subproblems for future use.

<hr>
### Tabulation
Tabulation is a technique used in dynamic programming to solve problems by filling in a table of solutions to subproblems in a bottom-up manner. Unlike memoization, which solves subproblems recursively and stores the results in a memoization table, tabulation solves subproblems iteratively and stores the results in a tabulation table.

In tabulation, the tabulation table is initialized with the base cases of the problem, and the solutions to subproblems are filled in iteratively using a loop. The final solution to the problem is then read from the tabulation table.

Tabulation is particularly useful when the subproblems can be solved in a natural order, such as from the smallest subproblem to the largest. It is also useful when the memoization table required for memoization would be too large to fit in memory.

Tabulation can be used to solve a wide range of problems, including the Fibonacci sequence, the longest common subsequence problem, and the knapsack problem, among others. The key is to identify the subproblems and the relationships between them, and to use tabulation to fill in the tabulation table with the solutions to subproblems.

In the code you provided, the Fibonacci sequence is being computed using tabulation. The `fibo()` function fills in the `dp` vector iteratively using a loop, starting with the base cases of `dp[0] = 0` and `dp[1] = 1`. The final solution to the problem is then read from `dp[fb]`.