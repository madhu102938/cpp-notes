### Number of provinces
**1Q** Given an **undirected** graph with **V** vertices. We say two vertices u and v belong to a single province if there is a path from u to v or v to u. Your task is to find the number of provinces.  
  
**Note:** A province is a group of **directly** or **indirectly connected** cities and no other cities outside of the group.

Here `rank`, `size`, `parent` are put in public, so that they can be accessed and used as attributes
```cpp
class DisjointSet
{
public:
	vector<int> rank, size, parent;
	DisjointSet(int n)
	{
		size.resize(n + 1, 1);
		parent.resize(n + 1);
		for (int i = 0; i < n + 1; i++)
			parent[i] = i;
	}

	int findUlParent(int node)
	{
		if (node == parent[node])
			return node;
		return parent[node] = findUlParent(parent[node]);
	}

	void unionUsingSize(int u, int v)
	{
		int ulpu = findUlParent(u);
		int ulpv = findUlParent(v);

		if (ulpv == ulpu)
			return;

		if (size[ulpu] < size[ulpv])
		{
			parent[ulpu] = ulpv;
			size[ulpv] += size[ulpu];
		}
		else
		{
			parent[ulpv] = ulpu;
			size[ulpu] += size[ulpv];
		}
	}
};

// This function takes an adjacency matrix 'adj' and the number of vertices 'V' as input,
// and returns the number of connected components in the graph represented by the adjacency matrix.
int numProvinces(vector<vector<int>> adj, int V)
{
    // Create a DisjointSet object with 'V' elements.
    DisjointSet ds(V);

    // Iterate over all pairs of vertices (i, j) in the adjacency matrix.
    for (int i = 0; i < V; i++)
    {
        for (int j = 0; j < V; j++)
        {
            // If there is an edge between vertices i and j, and they are not already in the same set,
            // then union their sets using the DisjointSet object.
            if (adj[i][j] == 1)
            {
                if (ds.findUlParent(i) != ds.findUlParent(j))
                {
                    ds.unionUsingSize(i, j);
                }
            }
        }
    }

    // Count the number of sets in the DisjointSet object that have a parent equal to their own index,
    // which corresponds to the number of connected components in the graph.
    int ans = 0;
    for (int i = 0; i < V; i++)
    {
        if (ds.parent[i] == i)
            ans++;
    }

    // Return the number of connected components.
    return ans;
}
```

<hr>

### Number of Operations to Make Network Connected
**2Q)** There are `n` computers numbered from `0` to `n - 1` connected by ethernet cables `connections` forming a network where `connections[i] = [ai, bi]` represents a connection between computers `ai` and `bi`. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network `connections`. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return _the minimum number of times you need to do this in order to make all the computers connected_. If it is not possible, return `-1`.


```cpp
class DisjointSet
{
public:
	vector<int> rank, size, parent;
	DisjointSet(int n)
	{
		size.resize(n + 1, 1);
		parent.resize(n + 1);
		for (int i = 0; i < n + 1; i++)
			parent[i] = i;
	}

	int findUlParent(int node)
	{
		if (node == parent[node])
			return node;
		return parent[node] = findUlParent(parent[node]);
	}

	void unionUsingSize(int u, int v)
	{
		int ulpu = findUlParent(u);
		int ulpv = findUlParent(v);

		if (ulpv == ulpu)
			return;

		if (size[ulpu] < size[ulpv])
		{
			parent[ulpu] = ulpv;
			size[ulpv] += size[ulpu];
		}
		else
		{
			parent[ulpv] = ulpu;
			size[ulpu] += size[ulpv];
		}
	}
};

// This function takes the number of computers 'n' and a vector of connections 'connections'.
// It aims to determine the minimum number of cable extractions and placements needed to connect all computers.
int makeConnected(int n, vector<vector<int>>& connections) 
{
    // Create a DisjointSet data structure initialized with 'n' elements.
    DisjointSet ds(n);
    
    // Initialize a variable to keep track of extra edges that don't form new connections.
    int extra_edges = 0;
    
    // Iterate through each connection.
    for (auto it : connections)
    {
        int u = it[0]; // First computer in the connection
        int v = it[1]; // Second computer in the connection

        // Check if the two computers are not already connected.
        if (ds.findUlParent(u) != ds.findUlParent(v))
        {
            // If not, join the sets containing these computers to connect them.
            ds.unionUsingSize(u, v);
        }
        else
        {
            // If they are already connected, count this as an extra edge that doesn't form a new connection.
            extra_edges++;
        }
    }

    // Count the number of distinct components in the network.
    int components = 0;
    for (int i = 0; i < n; i++)
    {
        if (i == ds.parent[i])
        {
            components++;
        }
    }
    
    // The minimum number of cables needed to connect all computers is one less than the number of components.
    int ans = components - 1;

    // If there are enough extra edges to cover the gaps between components, return the answer.
    if (extra_edges >= ans)
    {
        return ans;
    }
    else
    {
        // Otherwise, it's not possible to connect all computers, so return -1.
        return -1;
    }
}

```

<hr>

### Accounts Merge
**3Q)** Given a list of `accounts` where each element `accounts[i]` is a list of strings, where the first element `accounts[i][0]` is a name, and the rest of the elements are **emails** representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails **in sorted order**. The accounts themselves can be returned in **any order**.

1. **Initialization**: The code starts by initializing some necessary data structures. `n` represents the number of accounts, `DisjointSet` is a custom class that likely implements a disjoint-set data structure, and `mp` is an unordered map that maps email addresses to their corresponding account index.
    
2. **Merging Accounts**: The code then iterates through each account in the `accounts` vector and their associated email addresses. For each email address, it checks whether it already exists in the `mp` map. If it doesn't exist, it adds the email address to the map and associates it with the current account index. If the email address already exists, it means that it belongs to another account, so the code uses the `DisjointSet` data structure to merge the current account with the account that previously contained the same email address.
    
3. **Creating Temporary Groups**: After processing all accounts and merging them as needed, the code creates temporary groups of email addresses based on the disjoint-set structure. It collects all email addresses belonging to the same merged group into `temp` arrays.
    
4. **Building the Result**: Finally, the code constructs the final result, which is a vector of vectors of strings. It iterates through the `temp` arrays, sorts the email addresses within each group, and constructs a vector with the name of the account (from the original `accounts` input) followed by the sorted email addresses. These vectors are then added to the `ans` vector.
    
5. **Returning the Result**: The code returns the `ans` vector, which contains the merged accounts with the specified format.

```cpp
class DisjointSet
{
public:
	vector<int> rank, size, parent;
	DisjointSet(int n)
	{
		size.resize(n + 1, 1);
		parent.resize(n + 1);
		for (int i = 0; i < n + 1; i++)
			parent[i] = i;
	}

	int findUlParent(int node)
	{
		if (node == parent[node])
			return node;
		return parent[node] = findUlParent(parent[node]);
	}

	void unionUsingSize(int u, int v)
	{
		int ulpu = findUlParent(u);
		int ulpv = findUlParent(v);

		if (ulpv == ulpu)
			return;

		if (size[ulpu] < size[ulpv])
		{
			parent[ulpu] = ulpv;
			size[ulpv] += size[ulpu];
		}
		else
		{
			parent[ulpv] = ulpu;
			size[ulpu] += size[ulpv];
		}
	}
};


vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
    int n = accounts.size();  // Get the number of accounts
    DisjointSet ds(n);  // Initialize a DisjointSet data structure for union-find operations
    unordered_map<string, int> mp;  // Create a map to associate email addresses with account indices

    // Step 1: Merge accounts based on common email addresses
    for (int i = 0; i < n; i++) {
        for (int j = 1; j < accounts[i].size(); j++) {
            if (mp.find(accounts[i][j]) == mp.end()) {
                // If the email address is not in the map, associate it with the current account index
                mp[accounts[i][j]] = i;
            } else {
                // If the email address already exists, merge the current account with the previous one
                if (ds.findUlParent(i) != ds.findUlParent(mp[accounts[i][j]])) {
                    ds.unionUsingSize(i, mp[accounts[i][j]]);
                }
            }
        }
    }

    vector<string> temp[n];  // Create temporary arrays to group merged accounts

    // Step 2: Collect email addresses into temporary groups based on merged accounts
    for (auto i : mp) {
        string s = i.first;
        int index = ds.findUlParent(i.second);  // Find the representative account index for the group
        temp[index].push_back(s);  // Add the email address to the appropriate group
    }

    vector<vector<string>> ans;  // Initialize the final result

    // Step 3: Build the final result in the specified format
    for (int i = 0; i < n; i++) {
        if (temp[i].size() != 0) {
            sort(temp[i].begin(), temp[i].end());  // Sort email addresses within each group
            vector<string> temp_vector;
            temp_vector.push_back(accounts[i][0]);  // Add the account name to the result
            for (auto it : temp[i]) {
                temp_vector.push_back(it);  // Add sorted email addresses to the result
            }
            ans.push_back(temp_vector);  // Add the group to the final result
        }
    }

    return ans;  // Return the merged accounts in the specified format
}
```

<hr>

### Number of islands II

**4Q)** You are given a **n,m** which means the row and column of the 2D matrix and an array of  size k denoting the number of operations. Matrix elements is 0 if there is water or 1 if there is land. Originally, the 2D matrix is all 0 which means there is no land in the matrix. The array has k operator(s) and each operator has two integer A[i][0], A[i][1] means that you can change the cell matrix[A[i][0]][A[i][1]] from sea to island. Return how many island are there in the matrix after each operation.You need to return an array of size **k**.  
**Note :** An island means group of 1s such that they share a common side.

1. **Initialization**: The code starts by initializing a Disjoint Set data structure (`ds`) with a size of `n * m`. The `vis` matrix is used to keep track of which cells have been visited, and the `ans` vector will store the number of islands after each operation. `island` is used to keep track of the current number of islands.
    
2. **Loop through Operations**: The code iterates through each operation given in the `operators` vector.
    
3. **Extract Row and Column**: It extracts the row and column from the current operation.
    
4. **Check If Already Visited**: If the cell at `(row, col)` has already been visited (`vis[row][col]` is true), it appends the current number of islands to the `ans` vector and continues to the next operation.
    
5. **Mark Cell as Visited**: If the cell at `(row, col)` hasn't been visited before, it marks it as visited by setting `vis[row][col]` to 1.
    
6. **Neighbor Checking Loop**: It then checks the neighbors of the current cell in the up, down, left, and right directions.
    
7. **Union of Disjoint Sets**: If a neighboring cell has also been visited (`vis[newRow][newCol]` is true), it checks whether the current cell and the neighbor belong to the same island using the Disjoint Set data structure. If they don't, it performs a union operation and decreases the `island` count by 1.
    
8. **Append Result**: After processing all the neighbors, it appends the current number of islands to the `ans` vector.
    
9. **Return Result**: Finally, after processing all operations, the code returns the `ans` vector containing the number of islands after each operation.

```cpp
class DisjointSet
{
public:
	vector<int> rank, size, parent;
	DisjointSet(int n)
	{
		size.resize(n + 1, 1);
		parent.resize(n + 1);
		for (int i = 0; i < n + 1; i++)
			parent[i] = i;
	}

	int findUlParent(int node)
	{
		if (node == parent[node])
			return node;
		return parent[node] = findUlParent(parent[node]);
	}

	void unionUsingSize(int u, int v)
	{
		int ulpu = findUlParent(u);
		int ulpv = findUlParent(v);

		if (ulpv == ulpu)
			return;

		if (size[ulpu] < size[ulpv])
		{
			parent[ulpu] = ulpv;
			size[ulpv] += size[ulpu];
		}
		else
		{
			parent[ulpv] = ulpu;
			size[ulpu] += size[ulpv];
		}
	}
};

vector<int> numberOfIslandII(int n, int m, vector<vector<int>>& operators, int q)
{
    // Initialize a Disjoint Set data structure with n * m elements
    DisjointSet ds(n * m);

    // Create a 2D matrix to keep track of visited cells
    vector<vector<int>> vis(n, vector<int>(m, 0));

    // Initialize a vector to store the number of islands after each operation
    vector<int> ans;

    // Initialize a variable to keep track of the current number of islands
    int island = 0;

    // Iterate through each operation in the 'operators' vector
    for (auto it : operators)
    {
        int row = it[0];
        int col = it[1];

        // If the cell is already visited, append the current island count to 'ans' and continue
        if (vis[row][col])
        {
            ans.push_back(island);
            continue;
        }

        // Mark the cell as visited
        vis[row][col] = 1;

        // Define directions for neighboring cells (up, left, right, down)
        vector<int> delrow = {-1, 0, 0, 1};
        vector<int> delcol = {0, -1, 1, 0};

        // Increment the island count for the current operation
        island++;

        // Store the index of the current cell in 'prevds'
        int prevds = row * m + col;

        // Check neighbors of the current cell
        for (int k = 0; k < 4; k++)
        {
            int newRow = row + delrow[k], newCol = col + delcol[k];

            // Check if the neighboring cell is within the matrix bounds
            if (newRow >= 0 && newRow < n && newCol >= 0 && newCol < m)
            {
                // If the neighboring cell has been visited
                if (vis[newRow][newCol])
                {
                    // Calculate the index of the neighboring cell and check if it's in a different island
                    int currds = newRow * m + newCol;
                    if (ds.findUlParent(prevds) != ds.findUlParent(currds))
                    {
                        // Perform a union operation and decrement the island count
                        ds.unionUsingSize(prevds, currds);
                        island--;
                    }
                }
            }
        }

        // Append the current island count to 'ans' after processing the operation
        ans.push_back(island);
    }

    // Return the vector containing the number of islands after each operation
    return ans;
}
```

<hr>

### Making a Large Island

**5Q** You are given an `n x n` binary matrix `grid`. You are allowed to change **at most one** `0` to be `1`.

Return _the size of the largest **island** in_ `grid` _after applying this operation_.

An **island** is a 4-directionally connected group of `1`s.

```cpp
class DisjointSet
{
public:
	vector<int> rank, size, parent;
	DisjointSet(int n)
	{
		size.resize(n + 1, 1);
		parent.resize(n + 1);
		for (int i = 0; i < n + 1; i++)
			parent[i] = i;
	}

	int findUlParent(int node)
	{
		if (node == parent[node])
			return node;
		return parent[node] = findUlParent(parent[node]);
	}

	void unionUsingSize(int u, int v)
	{
		int ulpu = findUlParent(u);
		int ulpv = findUlParent(v);

		if (ulpv == ulpu)
			return;

		if (size[ulpu] < size[ulpv])
		{
			parent[ulpu] = ulpv;
			size[ulpv] += size[ulpu];
		}
		else
		{
			parent[ulpv] = ulpu;
			size[ulpu] += size[ulpv];
		}
	}
};



int largestIsland(vector<vector<int>>& grid) {
    int n = grid.size();
    int m = grid[0].size();
    
    // Create a Disjoint Set data structure to represent connected components.
    DisjointSet ds(n * m);
    
    // Define arrays to represent the possible directions for checking neighbors.
    vector<int> delrow = {-1, 0, 0, 1};
    vector<int> delcol = {0, -1, 1, 0};
    
    // Iterate through the grid to build the disjoint set and make connections between all the 1s
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] == 1) {
                int prevDS = i * m + j;
                for (int k = 0; k < 4; k++) {
                    int newRow = i + delrow[k], newCol = j + delcol[k];
                    if (newRow >= 0 && newRow < n && newCol >= 0 && 
                    newCol < m && grid[newRow][newCol] == 1) {
                        int currDS = newRow * m + newCol;
                        ds.unionUsingSize(prevDS, currDS);
                    }
                }
            }
        }
    }

    int ans = 0;
    bool diditenter = false;

    // Iterate through the grid again to find 0s and calculate the size of the largest island after changing one 0 to 1.
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] == 0) {
                diditenter = true;
                set<int> s; // we might encounter 1s that have the same ultimate parent thus we are storing them in a set to avoid this
                for (int k = 0; k < 4; k++) {
                    int newRow = i + delrow[k], newCol = j + delcol[k];
                    if (newRow >= 0 && newRow < n && newCol >= 0 
                    && newCol < m && grid[newRow][newCol] == 1) {
                        int currDS = newRow * m + newCol;
                        s.insert(ds.findUlParent(currDS));
                    }
                }
                int temp = 0;
                for (auto it : s)
                    temp += ds.size[it];
                ans = max(ans, temp + 1);
            }
        }
    }
    
    // If no 0s were encountered, return the size of the entire grid as the largest island.
    if (diditenter)
        return ans;
    else
        return n * m; 
}

```

<hr>

### Most Stones removed with same row or column

**6Q)** On a 2D plane, we place `n` stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either **the same row or the same column** as another stone that has not been removed.

Given an array `stones` of length `n` where `stones[i] = [xi, yi]` represents the location of the `ith` stone, return _the largest possible number of stones that can be removed_.


- In the disjoint set, first m elements are for rows and next elements are for columns
- We are using an map, just to count the number of components with a rock, if we don't use a map, then will we will end up counting empty elements 
```cpp
class DisjointSet
{
public:
	vector<int> rank, size, parent;
	DisjointSet(int n)
	{
		size.resize(n + 1, 1);
		parent.resize(n + 1);
		for (int i = 0; i < n + 1; i++)
			parent[i] = i;
	}

	int findUlParent(int node)
	{
		if (node == parent[node])
			return node;
		return parent[node] = findUlParent(parent[node]);
	}

	void unionUsingSize(int u, int v)
	{
		int ulpu = findUlParent(u);
		int ulpv = findUlParent(v);

		if (ulpv == ulpu)
			return;

		if (size[ulpu] < size[ulpv])
		{
			parent[ulpu] = ulpv;
			size[ulpv] += size[ulpu];
		}
		else
		{
			parent[ulpv] = ulpu;
			size[ulpu] += size[ulpv];
		}
	}
};


int removeStones(vector<vector<int>>& stones) {
    // Initialize variables to keep track of the maximum row and column values.
    int rowMax = 0, colMax = 0;
    int n = stones.size();

    // Find the maximum row and column values among the given stones.
    for (auto it : stones) {
        rowMax = max(rowMax, it[0]);
        colMax = max(colMax, it[1]);
    }

    // Create a Disjoint Set data structure with a size of (rowMax + colMax + 1).
    DisjointSet ds(rowMax + colMax + 1);

    // Create a map to count the occurrences of rows and columns.
    unordered_map<int, int> mp;

    // Iterate through the stones.
    for (auto it : stones) {
        int row = it[0];
        int col = rowMax + 1 + it[1];

        // Union the row and column elements in the Disjoint Set.
        ds.unionUsingSize(row, col);

        // Update the map to count occurrences of rows and columns.
        mp[row]++;
        mp[col]++;
    }

    // Initialize a variable to count connected components.
    int components = 0;

    // Iterate through the map to count the connected components.
    for (auto it : mp) {
        if (ds.findUlParent(it.first) == it.first)
            components++;
    }

    // Return the number of stones that can be removed (total stones - connected components).
    return n - components;
}

```