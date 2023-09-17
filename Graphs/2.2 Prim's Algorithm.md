### Finding the weight of minimum spanning tree
Weight of minimum spanning tree is  sum of all its edges

```cpp
// This function uses Prim's algorithm to find the minimum spanning tree weight in a graph.

// Include necessary libraries and headers

int spanningTree(int V, vector<vector<int>> adj[])
{
	// Initialize a vector to keep track of visited vertices
	vector<bool> vis(V, false);
	
	// Initialize a priority queue to store edges in ascending order of weights
	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
	
	// Push the starting vertex with weight 0 into the priority queue
	pq.push({0, 0});
	
	// Initialize a variable to keep track of the total sum of edge weights in the MST
	int sum = 0;

	// Start the Prim's algorithm loop
	while (!pq.empty())
	{
		// Extract the edge with the smallest weight from the priority queue
		auto iter = pq.top();
		pq.pop();
		
		// Extract the current vertex and its weight from the iterator
		int curr = iter.second;
		
		// If the current vertex is already visited, skip the rest of the loop
		if (vis[curr])	continue;
		
		// Mark the current vertex as visited
		vis[curr] = true;
		
		// Add the weight of the current edge to the total sum
		sum += iter.first;
		
		// Iterate through the adjacent vertices of the current vertex
		for (auto it : adj[curr])
		{
			// Extract the adjacent vertex and the weight of the edge to it
			int ncurr = it[0];
			int nweight = it[1];
			
			// If the adjacent vertex is not visited, add the edge to the priority queue
			if (!vis[ncurr])
				pq.push({nweight, ncurr});
		}
	}
	
	// Return the total sum of edge weights in the minimum spanning tree
	return sum;
}
```
***Time Complexity** - O(E logV)*

### Getting all the edges of minimum spanning tree
```cpp
vector<pair<int, int>> spanningTree(int V, vector<vector<int>> adj[])
{
	vector<bool> vis(V, false);
	priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
	vector<pair<int, int>> ans;
	pq.push({0, 0, 0});
	int sum = 0;

	while (!pq.empty())
	{
		auto iter = pq.top();
		pq.pop();
		int curr = iter[1];
		
		if (vis[curr])	continue;
		vis[curr] = true;
		if (curr != iter[2])
			ans.push_back({iter[2], curr});
		
		for (auto it : adj[curr])
		{
			int ncurr = it[0];
			int nweight = it[1];
			if (!vis[ncurr])
				pq.push({nweight, ncurr, curr});
		}
	}
	return ans;
}
```