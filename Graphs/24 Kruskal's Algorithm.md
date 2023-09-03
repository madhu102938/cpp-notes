Find weight of the minimum spanning tree
We use disjoint set for this
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

int spanningTree(int V, vector<vector<int>> adj[])
{
	vector<pair<int, pair<int, int>>> edges;
	for (int i = 0; i < V; i++)
	{
		for (auto it : adj[i])
			edges.push_back({it[1], {i, it[0]}});
	}

	sort(edges.begin(), edges.end());

	DisjointSet ds(V);
	int mstW = 0;

	for (auto it : edges)
	{
		int w = it.first;
		int u = it.second.first;
		int v = it.second.second;

		if (ds.findUlParent(u) != ds.findUlParent(v))
		{
			mstW += w;
			ds.unionUsingSize(u, v);
		}
	}

	return mstW;
}
```