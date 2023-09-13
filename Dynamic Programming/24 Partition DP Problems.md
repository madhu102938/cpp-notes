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