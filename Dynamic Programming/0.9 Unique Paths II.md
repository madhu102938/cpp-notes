You are given an `m x n` integer array `grid`. There is a robot initially located at the **top-left corner** (i.e., `grid[0][0]`). The robot tries to move to the **bottom-right corner** (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

An obstacle and space are marked as `1` or `0` respectively in `grid`. A path that the robot takes cannot include **any** square that is an obstacle.

Return _the number of possible unique paths that the robot can take to reach the bottom-right corner_.


**Recurrence** solution
```cpp
int mazeObstaclesUtil(int i, int j, vector<vector<int>> &maze) 
{
	if(i>0 && j>0 && maze[i][j]==-1) 
		return 0; 
	if(i==0 && j == 0)
		return 1;
	if(i<0 || j<0)
		return 0;
	
	int up = mazeObstaclesUtil(i-1,j,maze,dp);
	int left = mazeObstaclesUtil(i,j-1,maze,dp);
	
	return up+left;
}

int mazeObstacles(int n, int m, vector<vector<int> > &maze)
{
    return mazeObstaclesUtil(n-1,m-1,maze,dp);
}
```



**DP** solution
```cpp
int mazeObstaclesUtil(int i, int j, vector<vector<int>> &maze, vector<vector<int>> 
&dp) 
{
	if(i>0 && j>0 && maze[i][j]==-1) return 0; 
	if(i==0 && j == 0)
	return 1;
	if(i<0 || j<0)
	return 0;
	if(dp[i][j]!=-1) return dp[i][j];
	
	int up = mazeObstaclesUtil(i-1,j,maze,dp);
	int left = mazeObstaclesUtil(i,j-1,maze,dp);
	
	return dp[i][j] = up+left;
  
}

int mazeObstacles(int n, int m, vector<vector<int> > &maze)
{
    vector<vector<int> > dp(n,vector<int>(m,-1));
    return mazeObstaclesUtil(n-1,m-1,maze,dp);
    
}
```
