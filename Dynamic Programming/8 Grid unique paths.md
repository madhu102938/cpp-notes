### Unique paths
There is a robot on an `m x n` grid. The robot is initially located at the **top-left corner** (i.e., `grid[0][0]`). The robot tries to move to the **bottom-right corner** (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

Given the two integers `m` and `n`, return _the number of possible unique paths that the robot can take to reach the bottom-right corner_.

**Recurrence** solution
```cpp
class Solution {
private:
    int actualAnswer(int row, int column)
    {
        if (row == 0 && column == 0)
            return 1;
        if (row == -1 || column == -1)
            return 0;
        int left = actualAnswer(row - 1, column);
        int right = actualAnswer(row, column - 1);
		return left + right;
    }
public:
    int uniquePaths(int m, int n) {
        int ans = actualAnswer(m-1, n-1);
        return ans;
    }
};
```
***Time Complexity** - `O(2^(m*n))`*
***Space Complexity** - `O(Path length)`*
*Path Length = $m - 1 + n - 1$


**DP** Solution
```cpp
class Solution {
private:
    int actualAnswer(int row, int column, vector<vector<int>> &dp)
    {
        if (row == 0 && column == 0)
            return 1;
        if (row == -1 || column == -1)
            return 0;
        if (dp[row][column] != -1)
            return dp[row][column];
        int left = actualAnswer(row - 1, column, dp);
        int right = actualAnswer(row, column - 1, dp);
        dp[row][column] = left + right;
        return dp[row][column];
    }
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>> dp(m, vector<int>(n, -1));
        int ans = actualAnswer(m-1, n-1, dp);
        return ans;
    }
};
```
***Time Complexity** - O($m*n$) we can at max have $m*n$ calls*
***Space Complexity** - O($Path length$) + O($m*n$) : dp size*
*Path Length = $m - 1 + n - 1$*


**Tabulation** solution
```cpp
class Solution {
private:
    int actualAnswer(int m, int n, vector<vector<int>> &dp)
    {
        dp[0][0] = 0;

        for(int row = 0; row <= m; row++){
            for(int column = 0; column <= n; column++)
            {
                if (row == 0 && column == 0)
                    dp[0][0] = 1;
                else
                {
                    int left = 0, right = 0;
                    if (row > 0)    
                        left = dp[row - 1][column];
                    if (column > 0)
                        right = dp[row][column - 1];
                    dp[row][column] = left + right;
                }
            }
        }
        return dp[m][n];
    }
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>> dp(m, vector<int>(n, -1));
        int ans = actualAnswer(m-1, n-1, dp);
        return ans;
    }
};
```
***Time Complexity** - O($m*n$) we can at max have $m*n$ calls*
***Space Complexity** - O($m*n$) : dp size*