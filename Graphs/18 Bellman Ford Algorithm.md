The Bellman-Ford algorithm is a single-source shortest path algorithm that can handle negative edge weights. It works by relaxing the edges of the graph repeatedly, and it guarantees that after the i-th iteration, the shortest path with at most i edges has been found for all vertices.

Here's how the algorithm works:

1. Initialize the distance of the source vertex to 0, and the distance of all other vertices to infinity.

2. Relax all the edges of the graph n-1 times, where n is the number of vertices in the graph. In each iteration, go through all the edges of the graph and update the distance of the destination vertex if the distance of the source vertex plus the weight of the edge is less than the current distance of the destination vertex.

3. Check for negative-weight cycles. After the n-1 iterations, if there is still a vertex whose distance can be updated, then there must be a negative-weight cycle in the graph. To detect the negative-weight cycle, go through all the edges of the graph one more time and check if the distance of the destination vertex can be updated. If it can be updated, then there is a negative-weight cycle in the graph.

4. If there is no negative-weight cycle, then the shortest path from the source vertex to all other vertices has been found.

Here's the pseudocode for the Bellman-Ford algorithm:

```python
function BellmanFord(Graph, source):
    distance[source] := 0
    for each vertex v in Graph:
        if v ≠ source
            distance[v] := infinity
    for i from 1 to |V|-1:
        for each edge (u, v, w) in Graph:
            if distance[u] + w < distance[v]:
                distance[v] := distance[u] + w
    for each edge (u, v, w) in Graph:
        if distance[u] + w < distance[v]:
            return "Negative-weight cycle found"
    return distance
```

In this pseudocode, `Graph` is the input graph, `source` is the source vertex, `distance` is an array that stores the distance of each vertex from the source vertex, and `|V|` is the number of vertices in the graph. The algorithm first initializes the distance of the source vertex to 0 and the distance of all other vertices to infinity. It then relaxes all the edges of the graph `|V|-1` times, and checks for negative-weight cycles. If there is no negative-weight cycle, then the shortest path from the source vertex to all other vertices has been found.

> [!NOTE] Negative Cycle
> To detect negative-weight cycles using the Bellman-Ford algorithm, you can run the algorithm for one extra iteration after the n-1 iterations. If there is a negative-weight cycle, then there will be at least one vertex that can be reached from itself through a sequence of negative-weight edges. You can detect this by checking if the distance of any vertex can be updated after the n-1 iterations.


```cpp
vector<int> bellman_ford(int V, vector<vector<int>>& edges, int S) 
{
	vector<int> distance(V, 1e8);
	distance[S] = 0;

	for (int i = 0; i < V-1; i++)
	{
		for (auto it : edges)
		{
			int u = it[0], v = it[1], w = it[2];
			if (distance[u] != 1e8 && distance[u] + w < distance[v])
			{
				distance[v] = distance[u] + w; 
			}
		}
	}

	// minimum distance should have been computed in v-1 interations, if even after v-1 iterations, its still finding shorter distances then, there is a negative loop
	for (auto it : edges)
	{
		int u = it[0], v = it[1], w = it[2];
		if (distance[u] != 1e8 && distance[u] + w < distance[v])
		{
			return {-1};
		}
	}

	return distance;
}
```