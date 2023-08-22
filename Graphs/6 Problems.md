**1Q)** *Number of components in a graph*  [[3 Non connected graphs]]
There are `n` cities. Some of them are connected, while some are not. If city `a` is connected directly with city `b`, and city `b` is connected directly with city `c`, then city `a` is connected indirectly with city `c`.

A **province** is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an `n x n` matrix `isConnected` where `isConnected[i][j] = 1` if the `ith` city and the `jth` city are directly connected, and `isConnected[i][j] = 0` otherwise.

Return _the total number of **provinces**_.

We are given a adjacency matrix
```cpp
void actualAnswer(int node, vector<vector<int>> &isConnected, vector<int> &vis)
{
	vis[node] = 1;
	for (int i = 0; i < isConnected[node].size(); i++)
	{
		if ((isConnected[node][i] == 1) && (!vis[i]))
			actualAnswer(i, isConnected, vis);
	}
}
    
int findCircleNum(vector<vector<int>>& isConnected) {
	int V = isConnected.size();
	vector<int> vis(V);
	int ans = 0;
	for (int i = 0; i < V; i++)
	{
		if (!vis[i])
		{
			actualAnswer(i, isConnected, vis);
			ans++;
		}
	}
	return ans;
}
```

<hr>

**2Q** *Number of components in a matrix (no. of islands)*
*Given a grid of size $n*m$ (n is the number of rows and m is the number of columns in the grid) consisting of '0's (Water) and '1's(Land). Find the number of islands.  
  
**Note:** An island is either surrounded by water or boundary of grid and is formed by connecting adjacent lands horizontally or vertically or diagonally i.e., in all 8 directions.

```cpp
void bfsOnGrid(int row, int column, int m, int n, vector<vector<char>> &grid, vector<vector<int>> &vis)
	{
		vis[row][column] = 1;
		queue<pair<int, int>> q;
		q.push({row, column});
		while (!q.empty())
		{
			int crow = q.front().first;
			int ccolumn = q.front().second;
			q.pop();
			
			// Checking in all directions
			for (int delrow = -1; delrow <= 1; delrow++)
			{
				for (int delcol = -1; delcol <= 1; delcol++)
				{
					// Checking if nrow and ncol are valid and have land at the position and also if it is previously visited or not.
					int nrow = crow + delrow, ncol = ccolumn + delcol;
					if (nrow >= 0 && nrow < m && ncol >= 0 && ncol < n 
					&& grid[nrow][ncol] == '1' && !vis[nrow][ncol])
					{
						vis[nrow][ncol] = 1;
						q.push({nrow, ncol});
					}
				}
			}
		}
	}
// Function to find the number of islands.
int numIslands(vector<vector<char>> &grid)
{
	int m = grid.size(), n = grid[0].size();
	vector<vector<int>> vis(m, vector<int>(n, 0));
	int ans = 0;
	for (int i = 0; i < m; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (grid[i][j] == '1' && !vis[i][j])
			{
				bfsOnGrid(i, j, m, n, grid, vis);
				ans++;
			}
		}
	}
	return ans;
}
```