### Pattern Identification:

Whenever we need to find the answer to a large problem such that the problem can be broken into subproblems and the final answer varies due to the **order** in which the subproblems are solved, we can think in terms of partition DP.

<hr>

### Matrix Chain Multiplication
Given a chain of matrices A1,…, An denoted by an array of size n+1, find out the minimum number of operations to multiply these n matrices.

Here `n` means number of matrices, thus `n+1` is the size of the array

**DP** solution
`dp[i][j]` stores the minimum cost required to multiply the matrices from the `i`-th matrix to the `j`-th matrix inclusively, considering the most efficient parenthesization of these matrix multiplications.
```cpp
// Function to calculate the minimum cost of multiplying matrices from i to j
int actualAnswer(int i, int j, int *arr, vector<vector<int>> &dp)
{
    // If there's only one matrix, the cost is 0 (base case)
    if (i == j)
        return 0;
    
    // If the minimum cost for this range (i, j) has already been computed, return it
    if (dp[i][j] != -1)
        return dp[i][j];

    int mini = INT_MAX; // Initialize the minimum cost as infinity

    // Loop through all possible positions to split the matrices in the range (i, j)
    for (int k = i; k < j; k++)
    {
        // Calculate the cost of multiplying matrices from i to k and k+1 to j
        // Then add the cost of multiplying the resulting matrices
        int number = arr[i-1] * arr[k] * arr[j] + actualAnswer(i, k, arr, dp) + actualAnswer(k+1, j, arr, dp);

        // Update the minimum cost if the current number is smaller
        mini = min(mini, number);
    }

    // Store the minimum cost in the dp array for future reference
    return dp[i][j] = mini;
}

// Main function to compute the minimum cost of matrix chain multiplication
int matrixChainMultiplication(int *arr, int n)
{
    // Initialize a 2D DP array to store the computed results
    vector<vector<int>> dp(n+1, vector<int>(n+1, -1));

    // Call the recursive function to compute the minimum cost from matrices 1 to n
    return actualAnswer(1, n, arr, dp);
}
```


**Tabulation** Solution
- As we can see that in recursive approach `i` goes from 1 to N-1 and `j` decreases from N-1
- Here `i` and `j` are the starting and end points of the block of array we chose, thus `j >= i` (thus the second loop start `j=i+1`)
```cpp
int matrixChainMultiplication(int *arr, int n)
{
    n++;
	vector<vector<int>> dp(n, vector<int>(n, 0));
	
	for (int i = 1; i < n; i++)
		dp[i][i] = 0;
	
	for (int i = n-1; i >= 1; i--)
	{
		for (int j = i+1; j < n; j++)
		{
			int mini = 1e9;
			for (int k = i; k <= j-1; k++)
			{
				int number = arr[i-1] * arr[k] * arr[j] + dp[i][k] + dp[k+1][j];
				mini = min(mini, number);
			}
			dp[i][j] = mini;
		}
	}
	return dp[1][n-1];
}
```

<hr>

### Minimum cost to cut a stick
Given a wooden stick of length `n` units. The stick is labelled from `0` to `n`. For example, a stick of length **6** is labelled as follows:

![](https://assets.leetcode.com/uploads/2020/07/21/statement.jpg)

Given an integer array `cuts` where `cuts[i]` denotes a position you should perform a cut at.

You should perform the cuts in order, you can change the order of the cuts as you wish.

The cost of one cut is the length of the stick to be cut, the total cost is the sum of costs of all cuts. When you cut a stick, it will be split into two smaller sticks (i.e. the sum of their lengths is the length of the stick before the cut). Please refer to the first example for a better explanation.

Return _the minimum total cost_ of the cuts.

**DP** solution
```cpp
int actualAnswer(int i, int j, vector<int> &cuts, vector<vector<int>> &dp)
{
	if (i > j)
	  return 0;

	if (dp[i][j] != -1)
	  return dp[i][j];

	int mini = INT_MAX;
	for (int k = i; k <= j; k++)
	{
	   int number = cuts[j+1] - cuts[i-1] + actualAnswer(i, k-1, cuts, dp) + actualAnswer(k+1, j, cuts, dp);
	   mini = min(mini, number);
	}
	return dp[i][j] = mini;
}

int minCost(int n, vector<int>& cuts) {
	vector<vector<int>> dp(n, vector<int>(n, -1));
	sort(cuts.begin(), cuts.end());
	cuts.insert(cuts.begin(), 0);
	cuts.push_back(n);
	return actualAnswer(1, cuts.size()-2, cuts, dp);
}
```


**Tabulation** solution
```cpp
int minCost(int n, vector<int> &cuts)
{
	int c = cuts.size();
	vector<vector<int>> dp(c+2, vector<int>(c+2, 0));
	sort(cuts.begin(), cuts.end());
	cuts.insert(cuts.begin(), 0);
	cuts.push_back(n);
	
	for (int i = 0; i < c+2; i++)
	{
		for (int j = 0; j < c+2; j++)
		{
			if (i > j)
				dp[i][j] = 0;
		}
	}
	
	for (int i = c; i >= 1; i--)
	{
		for (int j = 1; j <= c; j++)
		{
			if (i > j)	continue;
			else
			{
				int mini = INT_MAX;
				for (int k = i; k <= j; k++)
				{
					int number = cuts[j + 1] - cuts[i - 1] + dp[i][k-1] + dp[k+1][j];
					mini = min(mini, number);
				}
				dp[i][j] = mini;
			}
		}
	}
	return dp[1][c];
}
```

<hr>

### Burst Balloons
You are given `n` balloons, indexed from `0` to `n - 1`. Each balloon is painted with a number on it represented by an array `nums`. You are asked to burst all the balloons.

If you burst the `ith` balloon, you will get `nums[i - 1] * nums[i] * nums[i + 1]` coins. If `i - 1` or `i + 1` goes out of bounds of the array, then treat it as if there is a balloon with a `1` painted on it.

Return _the maximum coins you can collect by bursting the balloons wisely_.

**DP** solution
- We need to use bottom up approach for this, like
- what would be the last balloon to be burst, then we need to add more balloons sequentially
```cpp
int actualAnswer(int i, int j, vector<int> &nums, vector<vector<int>> &dp)
{
    if (i > j)
        return 0;

    if (dp[i][j] != -1)
        return dp[i][j];

    int mini = INT_MIN;
    for (int k = i; k <= j; k++)
    {
        int number = nums[i-1] * nums[k] * nums[j+1] 
        + actualAnswer(i, k-1, nums, dp) + actualAnswer(k+1, j, nums, dp);
        mini = max(mini, number);
    }
    return dp[i][j] = mini;
}

int maxCoins(vector<int> &nums)
{
    int n = nums.size();
    nums.push_back(1);
    nums.insert(nums.begin(), 1);
    vector<vector<int>> dp(n+1, vector<int>(n+1, -1));
    return actualAnswer(1, n, nums, dp);
}
```


**Tabulation** solution
```cpp
int maxCoins(vector<int> &nums)
{
	int n = nums.size();
	nums.push_back(1);
	nums.insert(nums.begin(), 1);
	vector<vector<int>> dp(n+2, vector<int>(n+2, -1));

	for (int i = 0; i < n+2; i++)
	{
		for (int j = 0; j < n+2; j++)
		{
			if (i > j)
				dp[i][j] = 0;
		}
	}
	
	for (int i = n; i >= 1; i--)
	{
		for (int j = 1; j <= n; j++)
		{
			if (i > j) continue;
			else
			{
				int mini = INT_MIN;
				for (int k = i; k <= j; k++)
				{
					int number = nums[i-1] * nums[k] * nums[j+1] + 
					dp[i][k-1] + dp[k+1][j];
					
					mini = max(mini, number);
				}
				dp[i][j] = mini;
			}
		}
	}
	return dp[1][n];	
}
```

<hr>

### Evaluate Boolean expression to true
Given an expression, A, with operands and operators (OR, AND, XOR), in how many ways can you evaluate the expression to be true, by grouping it in different ways?

1. The function `actualAnswer` takes several parameters:
    
    - `i` and `j` represent the indices of the subexpression being considered.
    - `isTrue` indicates whether the subexpression should evaluate to true (1) or false (0).
    - `exp` is a reference to the expression string.
    - `dp` is a 3D memoization table to store intermediate results.
2. Base Cases:
    
    - If `i > j`, it means the subexpression is empty, and the result is 0.
    - If `i == j`, it means the subexpression consists of a single operand. The result depends on whether it should evaluate to true or false.
3. Memoization:
    
    - Before performing any calculations, the code checks if the result for the current subexpression with the given `isTrue` value has already been computed and stored in the `dp` table. If so, it returns the cached result to avoid redundant calculations.
4. Loop and Recursion:
    
    - The code uses a loop with variable `k` to iterate through the operators in the expression between indices `i` and `j`. It processes the expression by dividing it into two subexpressions: one from `i` to `k-1` and another from `k+1` to `j`.
    - For each operator `k`, it recursively calculates the number of ways to make the subexpressions on the left and right side of the operator evaluate to true or false.
    - It calculates four values: `lf` (left subexpression evaluates to false), `lt` (left subexpression evaluates to true), `rf` (right subexpression evaluates to false), and `rt` (right subexpression evaluates to true).
5. Operator Evaluation:
    
    - Depending on the operator at index `k` in the expression, the code calculates the number of ways to make the current subexpression true or false.
    - For each operator (|, &, ^), it computes the possibilities as per the problem's requirements and accumulates them in the `ans` variable.
6. Returning and Memoization:

    - Finally, the code stores the result for the current subexpression with the given `isTrue` value in the `dp` table to avoid recomputation and returns the result.

```cpp
int actualAnswer(int i, int j, int isTrue, string &exp, vector<vector<vector<int>>> &dp)
{
	// Base Case 1: If the subexpression is empty (i > j), return 0.
	if (i > j)
		return 0;
	
	// Base Case 2: If the subexpression has a single operand,
	// check if it should evaluate to true or false.
	if (i == j)
	{
		if (isTrue == 1)
			return (exp[i] == 'T');  // Return 1 if 'T', else 0 if 'F'.
		else
			return (exp[i] == 'F');  // Return 1 if 'F', else 0 if 'T'.
	}
	
	// Check if the result for the current subexpression and isTrue value
	// has already been computed and stored in the dp table.
	if (dp[i][j][isTrue] != -1)
		return dp[i][j][isTrue];
	
	// Initialize a variable to accumulate the number of ways
	// to make the subexpression true.
	int ans = 0;
	
	// Loop through the operators in the subexpression.
	for (int k = i + 1; k < j; k = k + 2)
	{
		// Recursively calculate the number of ways to make the left
		// subexpression evaluate to false (lf) and true (lt).
		int lf = actualAnswer(i, k - 1, 0, exp, dp);
		int lt = actualAnswer(i, k - 1, 1, exp, dp);
		
		// Recursively calculate the number of ways to make the right
		// subexpression evaluate to false (rf) and true (rt).
		int rf = actualAnswer(k + 1, j, 0, exp, dp);
		int rt = actualAnswer(k + 1, j, 1, exp, dp);

		// Check the operator at index k and compute the number of ways
		// to make the current subexpression true or false based on it.
		if (exp[k] == '|')
		{
			if (isTrue == 1)
				ans = ans + ((lf * rt) + (lt * rf) + (lt * rt));  // OR operator
			else
				ans = ans + (lf * rf);
		}
		else if (exp[k] == '&')
		{
			if (isTrue == 1)	
				ans = ans + (lt * rt);  // AND operator
			else
				ans = ans + ((lf * rt) + (lt * rf) + (lf * rf));
		}
		else if (exp[k] == '^')
		{
			if (isTrue == 1)
				ans = ans + ((lf * rt) + (lt * rf));  // XOR operator
			else
				ans = ans + ((lf * rf) + (lt * rt));
		}
	}
	
	// Store the computed result for the current subexpression
	// and isTrue value in the dp table to avoid recomputation.
	return dp[i][j][isTrue] = ans;
}

int evaluateExp(string &exp)
{
	int n = exp.size();
	vector<vector<vector<int>>> dp(n+1, vector<vector<int>>(n+1, vector<int>(2, -1)));
	int ans = actualAnswer(0, n-1, 1, exp, dp);	
	return ans;
}
```


**Tabulation** solution
```cpp
int evaluateExp(string &exp)
{
	int n = exp.size();
	vector<vector<vector<int>>> dp(n + 1, vector<vector<int>>(n + 1, vector<int>(2, -1)));
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (i > j)
				dp[i][j][1] = dp[i][j][0] = 0;
			else if (i == j)
			{
				if (exp[i] == 'T')
				{
					dp[i][j][1] = 1;
					dp[i][j][0] = 0;
				}
				else if (exp[i] == 'F')
				{
					dp[i][j][0] = 1;
					dp[i][j][1] = 0;
				}
			}
		}
	}

	for (int i = n - 1; i >= 0; i--)
	{
		for (int j = 0; j < n; j++)
		{
			if (i >= j)
				continue;

			
			for (int isTrue = 0; isTrue < 2; isTrue++)
			{
				int ans = 0;

				for (int k = i + 1; k < j; k = k + 2)
				{
					int lf = dp[i][k-1][0];
					int lt = dp[i][k-1][1];
					int rf = dp[k+1][j][0];
					int rt = dp[k+1][j][1];

					if (exp[k] == '|')
					{
						if (isTrue == 1)
							ans = ans + ((lf * rt) + (lt * rf) + (lt * rt));
						else
							ans = ans + (lf * rf);
					}

					else if (exp[k] == '&')
					{
						if (isTrue == 1)
							ans = ans + (lt * rt);
						else
							ans = ans + ((lf * rt) + (lt * rf) + (lf * rf));
					}

					else if (exp[k] == '^')
					{
						if (isTrue == 1)
							ans = ans + ((lf * rt) + (lt * rf));
						else
							ans = ans + ((lf * rf) + (lt * rt));
					}
				}
				dp[i][j][isTrue] = ans;
			}
		}
	}
	return dp[0][n-1][1];
}
```