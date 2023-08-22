```cpp
void actualAnswer(int node, vector<int> adj[], vector<int> &vis, vector<int> &dfs)
{
	dfs.push_back(node);
	vis[node] = 1;
	for (auto it : adj[node])
	{
		if (!vis[it])
			actualAnswer(it, adj, vis, dfs);
	}
}

vector<int> dfsofGraph(int V, vector<int> adj[]) 
{
	vector<int> vis(V);
	vector<int> dfs;
	actualAnswer(0, adj, vis, dfs);
	return dfs;
}

```


