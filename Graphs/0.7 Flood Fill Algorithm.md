The flood fill algorithm is used to change the color of a connected region in a multi-dimensional array, such as an image. It starts from a seed pixel and replaces all the pixels that have the same color as the seed pixel and are connected to it by a path of the same color

![](https://1.bp.blogspot.com/-euK9E7L6bo0/YNK536q1r5I/AAAAAAAAPC8/SZlCKIk72KIQnhLuNJ9O9JuJ7qburYdfACLcBGAsYHQ/w320-h267/ff.gif)


```cpp
// Function to perform flood fill on the image using DFS
void floodFill_on_image(vector<vector<int>> &ans, int m, int n, int startRow, int startCol, int oldColor, int newColor)
{
    // Set the new color of the current pixel
    ans[startRow][startCol] = newColor;
    // Define the row and column arrays for the 4 directions
    vector<int> row_arr = {-1, 0, 0, 1};
    vector<int> col_arr = {0, -1, 1, 0};
    // Check all 4 directions for pixels with the old color and perform flood fill on them
    for (int i = 0; i < 4; i++)
    {
        int nrow = startRow + row_arr[i], ncol = startCol + col_arr[i];
        if (nrow >= 0 && nrow < m && ncol >= 0 && ncol < n && ans[nrow][ncol] == oldColor)
            floodFill_on_image(ans, m, n, nrow, ncol, oldColor, newColor);
    }
}

// Function to perform flood fill on the image and return the modified image
vector<vector<int>> floodFill(vector<vector<int>> &image, int sr, int sc, int newColor)
{
    // Get the old color of the starting pixel
    int old_color = image[sr][sc];
    // If the old and new colors are the same, return the original image
    if (old_color == newColor)
        return image;
    // Get the dimensions of the image
    int m = image.size();
    int n = image[0].size();
    // Create a copy of the image to perform flood fill on
    vector<vector<int>> ans = image;
    // Perform flood fill on the copy of the image
    floodFill_on_image(ans, m, n, sr, sc, old_color, newColor);
    // Return the modified image
    return ans;
}
```


<hr>


**1Q)** You are given an `m x n` `grid` where each cell can have one of three values:

- `0` representing an empty cell,
- `1` representing a fresh orange, or
- `2` representing a rotten orange.

Every minute, any fresh orange that is **4-directionally adjacent** to a rotten orange becomes rotten.

Return _the minimum number of minutes that must elapse until no cell has a fresh orange_. If _this is impossible, return_ `-1`.


```cpp
int orangesRotting(vector<vector<int>> &grid)
{
    int m = grid.size(), n = grid[0].size(); // Get dimensions of the grid (m rows, n columns)
    int vis[m][n]; // Create a 2D array to keep track of visited cells and their status
    int time = 0, cntFresh = 0, finalCnt = 0;
    queue<pair<pair<int, int>, int>> q; // Create a queue to perform BFS

    // Loop through each cell of the grid to initialize the data structures and count fresh oranges
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (grid[i][j] == 2) // If the cell contains a rotten orange
            {
                q.push({{i, j}, 0}); // Add the coordinates of the rotten orange to the queue along with the time it became rotten (0 minutes)
                vis[i][j] = 2; // Mark the cell as visited with a rotten orange
            }
            else
                vis[i][j] = 0; // Mark the cell as unvisited
            if (grid[i][j] == 1) // If the cell contains a fresh orange
                cntFresh++; // Increment the count of fresh oranges
        }
    }

    // Perform BFS to simulate the process of rotting oranges
    while (!q.empty())
    {
        int row = q.front().first.first;
        int col = q.front().first.second;
        int nowTime = q.front().second;

        time = max(time, nowTime); // Update the elapsed time to the maximum of current time and time of the current rotten orange

        q.pop(); // Remove the processed cell from the queue

        int delrow[] = {-1, 0, 0, 1}; // Define the changes in row index for the four possible directions
        int delcol[] = {0, -1, 1, 0}; // Define the changes in column index for the four possible directions

        // Check the four adjacent cells to the current rotten orange
        for (int i = 0; i < 4; i++)
        {
            int nrow = row + delrow[i], ncol = col + delcol[i]; // Calculate the new coordinates

            // Check if the new coordinates are within the grid and correspond to a fresh orange
            if (nrow >= 0 && nrow < m && ncol >= 0 && ncol < n && grid[nrow][ncol] == 1 && vis[nrow][ncol] != 2)
            {
                vis[nrow][ncol] = 2; // Mark the adjacent fresh orange as rotten
                finalCnt++; // Increment the final count of rotten oranges
                q.push({{nrow, ncol}, nowTime + 1}); // Add the adjacent cell to the queue with an incremented time
            }
        }
    }
    
    // If the final count of rotten oranges is not equal to the count of initial fresh oranges, it means some oranges cannot be rotten.
    if (finalCnt != cntFresh)
        return -1; // Return -1 as it's impossible to rot all oranges
    
    return time; // Return the elapsed time, which represents the minimum time needed for all oranges to rot
}

```

<hr>

