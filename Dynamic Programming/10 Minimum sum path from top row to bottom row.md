Given an `n x n` array of integers `matrix`, return _the **minimum sum** of any **falling path** through_ `matrix`.

A **falling path** starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position `(row, col)` will be `(row + 1, col - 1)`, `(row + 1, col)`, or `(row + 1, col + 1)`.


**Recurrence** solution
```cpp
class Solution {
private:
    // Recursive function to compute the minimum falling path sum
    // starting from the given row and column in the matrix.
    int actualAnswer(int row, int column, vector<vector<int>> &matrix)
    {
        // Base cases:
        // If the column is out of bounds, return a large value.
        if (column == matrix[0].size() || column < 0)
            return 2e9;
        // If the row is 0, return the value in the matrix at the given row and column.
        if (row == 0)
            return matrix[row][column];

        // Recursive case:
        // Compute the minimum falling path sum starting from the given row and column
        // by adding the value at the current position to the minimum of the three possible
        // paths (up, left, and right), and store the result in the dp table.
        int ans = 2e9;
        int up = actualAnswer(row - 1, column, matrix) + matrix[row][column];
        int left = actualAnswer(row - 1, column - 1, matrix) + matrix[row][column];
        int right = actualAnswer(row - 1, column + 1, matrix) + matrix[row][column];
        ans = min((up), min(left, right));
        return ans;
    }
public:
    // Function to compute the minimum falling path sum in the matrix.
    int minFallingPathSum(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();

        // Compute the minimum falling path sum starting from each column in the last row,
        // and return the minimum of these values.
        int ans = INT_MAX;
        for (int i = 0; i < n; i++)
        {
            int temp = actualAnswer(m-1, i, matrix, dp);
            ans = min(ans, temp);
        }
        return ans;
    }
};
```



**DP** solution
```cpp
class Solution {
private:
    // Recursive function to compute the minimum falling path sum
    // starting from the given row and column in the matrix.
    int actualAnswer(int row, int column, vector<vector<int>> &matrix, vector<vector<int>> &dp)
    {
        // Base cases:
        // If the column is out of bounds, return a large value.
        if (column == matrix[0].size() || column < 0)
            return 2e9;
        // If the row is 0, return the value in the matrix at the given row and column.
        if (row == 0)
            return matrix[row][column];
        // If the value has already been computed, return it.
        if (dp[row][column] != -1)
            return dp[row][column];

        // Recursive case:
        // Compute the minimum falling path sum starting from the given row and column
        // by adding the value at the current position to the minimum of the three possible
        // paths (up, left, and right), and store the result in the dp table.
        int ans = 2e9;
        int up = actualAnswer(row - 1, column, matrix, dp) + matrix[row][column];
        int left = actualAnswer(row - 1, column - 1, matrix, dp) + matrix[row][column];
        int right = actualAnswer(row - 1, column + 1, matrix, dp) + matrix[row][column];
        ans = min((up), min(left, right));
        dp[row][column] = ans;
        return dp[row][column];
    }
public:
    // Function to compute the minimum falling path sum in the matrix.
    int minFallingPathSum(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        vector<vector<int>> dp(m, vector<int>(n, -1));

        // Compute the minimum falling path sum starting from each column in the last row,
        // and return the minimum of these values.
        int ans = INT_MAX;
        for (int i = 0; i < n; i++)
        {
            int temp = actualAnswer(m-1, i, matrix, dp);
            ans = min(ans, temp);
        }
        return ans;
    }
};
```




**Tabulation** solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution
{
private:
    // Recursive function to compute the minimum falling path sum
    // starting from the given row and column in the matrix.
    int actualAnswer(int m, int n, vector<vector<int>> &matrix, vector<vector<int>> &dp)
    {
        // Initialize the dp table with the values in the first row of the matrix.
        for (int i = 0; i <= n; i++)
            dp[0][i] = matrix[0][i];

        // Compute the minimum falling path sum for each subproblem in the matrix
        // using dynamic programming, and store the results in the dp table.
        for (int row = 1; row <= m; row++)
        {
            for (int column = 0; column <= n; column++)
            {
                // Compute the minimum falling path sum for the current subproblem
                // by adding the value at the current position to the minimum of the
                // three possible paths (up, left, and right), and store the result
                // in the dp table.
                int up = 1e9, left = 1e9, right = 1e9;
                if (row > 0)
                    up = dp[row - 1][column] + matrix[row][column];
                if (row > 0 && column > 0)
                    left = dp[row - 1][column - 1] + matrix[row][column];
                if (row > 0 && column < n)
                    right = dp[row - 1][column + 1] + matrix[row][column];
                dp[row][column] = min((up), min(left, right));
            }
        }

        // Find the minimum falling path sum in the last row of the dp table,
        // and return it.
        sort(dp[m].begin(), dp[m].end());
        return dp[m][0];
    }

public:
    // Function to compute the minimum falling path sum in the matrix.
    int minFallingPathSum(vector<vector<int>> &matrix)
    {
        int m = matrix.size(), n = matrix[0].size();
        vector<vector<int>> dp(m, vector<int>(n, -1));

        // Compute the minimum falling path sum starting from each column in the first row,
        // and return the minimum of these values.
        return actualAnswer(m - 1, n - 1, matrix, dp);
    }
};
```