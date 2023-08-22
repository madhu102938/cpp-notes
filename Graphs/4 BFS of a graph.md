- It is a level wise traversal technique
- We will be given a starting node
- First we will start at the given node, the given node is considered to be at level 0, there can only be one node at level 0
- Then we will visit all the nodes at level 1, then so on and so forth
- We take a queue data structure to apply BFS on a graph

```cpp
vector<int> bfsOfGraph(int V, vector<int> adj[]) 
{
	// we have an adjacency list
	// we need to create visited array
	vector<int> vis(V);
	vector<int> bfs;
	queue<int> q;
	q.push(0);
	vis[0] = 1;
	while (!q.empty())
	{
		int node = q.front();
		q.pop();
		bfs.push_back(node);
		for (auto it : adj[node])
		{
			if (!vis[it])
			{
				vis[it] = 1;
				q.push(it);
			}
		}
	}
	return bfs;
}
```