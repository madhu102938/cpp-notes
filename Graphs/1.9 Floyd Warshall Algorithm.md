The Floyd-Warshall algorithm is an all-pairs shortest path algorithm that works by finding the shortest path between every pair of vertices in a weighted graph. It is based on dynamic programming and can handle negative edge weights.

Here's how the algorithm works:

1. Initialize a 2D array `dist` of size n x n, where n is the number of vertices in the graph. For each pair of vertices (i, j), set `dist[i][j]` to the weight of the edge from i to j, if there is an edge, and infinity otherwise. Also, set `dist[i][i]` to 0 for all i.

2. For each vertex k from 1 to n, go through all pairs of vertices (i, j) and update `dist[i][j]` to `min(dist[i][j], dist[i][k] + dist[k][j])`. This means that if there is a shorter path from i to j that goes through vertex k, then update the distance to that shorter path.

3. After the n-th iteration, the `dist` array contains the shortest path between every pair of vertices in the graph.

Here's the pseudocode for the Floyd-Warshall algorithm:

```
function FloydWarshall(Graph):
    let dist be a |V| x |V| array of minimum distances initialized to infinity
    for each vertex v in Graph:
        dist[v][v] := 0
    for each edge (u,v) in Graph:
        dist[u][v] := weight(u,v)
    for k from 1 to |V|:
        for i from 1 to |V|:
            for j from 1 to |V|:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] := dist[i][k] + dist[k][j]
    for i from 1 to |V|:
        if dist[i][i] < 0:
            // Negative-weight cycle detected
            return "Negative-weight cycle found"
    return dist
```

In this pseudocode, `Graph` is the input graph, `dist` is a 2D array that stores the minimum distance between every pair of vertices, and `|V|` is the number of vertices in the graph. The algorithm first initializes the `dist` array to infinity and sets the diagonal elements to 0. It then updates the `dist` array with the weights of the edges in the graph. Finally, it iterates over all pairs of vertices and updates the `dist` array with the shortest path between them. After the n-th iteration, the `dist` array contains the shortest path between every pair of vertices in the graph.


> [!NOTE] Negative Cycle Detection
> If there is a negative-weight cycle, then there will be at least one vertex that can be reached from itself through a sequence of negative-weight edges. You can detect this by checking the diagonal elements of the `dist` array after the algorithm has finished running.


In this question, we were given that, 
- if a connection doesn't exist between two nodes, then -1 will be given at that place, that is why we are changing all -1s with 1e9
- Also we were guaranteed of no negative cycles
```cpp
void floyd_warshall(vector<vector<int>>&matrix){
	int n = matrix.size();

	// changing all -1s to 1e9s
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (matrix[i][j] == -1)
				matrix[i][j] = 1e9;
		}
	}
	
	
	for (int k = 0; k < n; k++)
	{
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j]);
			}
		}
	}

	// changing all 1e9s to -1s
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (matrix[i][j] == 1e9)
				matrix[i][j] = -1;
		}
	}
}
```
