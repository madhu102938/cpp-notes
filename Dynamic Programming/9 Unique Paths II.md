You are given an `m x n` integer array `grid`. There is a robot initially located at the **top-left corner** (i.e., `grid[0][0]`). The robot tries to move to the **bottom-right corner** (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

An obstacle and space are marked as `1` or `0` respectively in `grid`. A path that the robot takes cannot include **any** square that is an obstacle.

Return _the number of possible unique paths that the robot can take to reach the bottom-right corner_.


**Recurrence** solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int actualAnswer(int row, int column, vector<vector<int>> &points, vector<vector<int>> &dp)
{
    if(row == 0 && column == 0)
        return points[0][0];
    if(row < 0 || column < 0)
        return 2e9;
    int left = actualAnswer(row - 1, column, points, dp) + points[row][column];
    int right = actualAnswer(row, column - 1, points, dp) + points[row][column];
    return min(left, right);
}

class Solution
{
public:
    int uniquePathsWithObstacles(vector<vector<int>> &obstacleGrid)
    {
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, -1));
        int ans = actualAnswer(m - 1, n - 1, obstacleGrid, dp);
        return ans;
    }
};
```



**DP** solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution
{
private:
    int actualAnswer(int row, int column, vector<vector<int>> &points, vector<vector<int>> &dp)
    {
        if(row == 0 && column == 0)
            return points[0][0];
        if(row < 0 || column < 0)
            return 2e9;
        if (dp[row][column] != -1)
            return dp[row][column];
        int left = actualAnswer(row - 1, column, points, dp) + points[row][column];
        int right = actualAnswer(row, column - 1, points, dp) + points[row][column];
        dp[row][column] = min(left, right);
        return dp[row][column];
}

public:
    int minPathSum(vector<vector<int>> &obstacleGrid)
    {
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, -1));
        int ans = actualAnswer(m - 1, n - 1, obstacleGrid, dp);
        return ans;
    }
};
```



**Tabulation** solution
