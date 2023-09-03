In graph theory, a strongly connected component (SCC) of a directed graph is a maximal strongly connected subgraph. A strongly connected subgraph is a subgraph in which there is a directed path between any two vertices. **In other words, a strongly connected component is a group of vertices that are all reachable from each other.**


### Kosaraju Algorithm
1. Sort the nodes by their starting - finish time (recursive toposort)
2. Reverse the connections
3. Start traversing from the starting point


### Printing number of strongly connected components
```cpp
void kindaToposort(int node, vector<vector<int>> &adj, vector<bool> &visited, stack<int> &st)
{
	visited[node] = true;
	for (auto it : adj[node])
	{
		if (!visited[it])
			kindaToposort(it, adj, visited, st);
	}
	st.push(node);
}

void regularDFS(int node, vector<int> adjR[], vector<bool> &visited)
{
	visited[node] = true;
	for (auto it : adjR[node])
	{
		if (!visited[it])
			regularDFS(it, adjR, visited);
	}
}

int kosaraju(int V, vector<vector<int>>& adj)
{
	stack<int> s;
	vector<bool> visited(V, false);
	for (int i = 0; i < V; i++)
	{
		if (!visited[i])
			kindaToposort(i, adj, visited, s);
	}

	vector<int> adjR[V];
	for (int i = 0; i < V; i++)
	{
		for (auto it : adj[i])
			adjR[it].push_back(i);
	}

	visited.assign(V, false);
	int ans = 0;

	while (!s.empty())
	{
		int curr = s.top();
		s.pop();

		if (!visited[curr])
		{
			regularDFS(curr, adjR, visited);
			ans++;
		}
	}
	
	return ans;
}
```

<hr>

### Printing the strongly connected components
```cpp
void kindaToposort(int node, vector<vector<int>> &adj, vector<bool> &visited, stack<int> &st)
{
	visited[node] = true;
	for (auto it : adj[node])
	{
		if (!visited[it])
			kindaToposort(it, adj, visited, st);
	}
	st.push(node);
}

vector<int> regularBFS(int node, vector<int> adjR[], vector<bool> &visited)
{
	queue<int> q;
	q.push(node);
	visited[node] = true;
	vector<int> strongComponent;

	while (!q.empty())
	{
		int current = q.front();
		q.pop();
		strongComponent.push_back(current);

		for (auto it : adjR[current])
		{
			if (!visited[it])
			{
				q.push(it);
				visited[it] = true;
			}
		}
	}
	return strongComponent;
}

vector<vector<int>> kosaraju(int V, vector<vector<int>> &adj)
{
	stack<int> s;
	vector<bool> visited(V, false);
	for (int i = 0; i < V; i++)
	{
		if (!visited[i])
			kindaToposort(i, adj, visited, s);
	}

	vector<int> adjR[V];
	for (int i = 0; i < V; i++)
	{
		for (auto it : adj[i])
			adjR[it].push_back(i);
	}

	visited.assign(V, false);
	vector<vector<int>> ans;

	while (!s.empty())
	{
		int curr = s.top();
		s.pop();

		if (!visited[curr])
			ans.push_back(regularBFS(curr, adjR, visited));
	}

	return ans;
}
```