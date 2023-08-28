### Shortest path in an undirected unweighted graph
 Just our good 'ol BFS is enough to calculate the shortest path
 - BFS finds the shortest path between two nodes (unweighted graph)

```cpp
vector<int> shortestPath(vector<vector<int>>& edges, int N, int M, int src) {
    vector<int> adj[N];   // Adjacency list for the graph.

    // Populate the adjacency list based on the edges.
    for (int i = 0; i < M; i++) {
        adj[edges[i][0]].push_back(edges[i][1]);
        adj[edges[i][1]].push_back(edges[i][0]);
    }

    queue<pair<int, int>> q;
    q.push({src, 0});   // Initialize the queue with source node and distance 0.

    vector<int> dist(N, 1e9), vis(N);   // Initialize distance and visited arrays.

    while (!q.empty()) {
        int curr = q.front().first;
        int dis = q.front().second;
        q.pop();
        dist[curr] = dis   // Update the minimum distance to the current node.

        for (int it : adj[curr]) {
            if (!vis[it]) {
                vis[it] = 1;   // Mark the node as visited.
                q.push({it, dis + 1});   // Push adjacent nodes into the queue with incremented distance.
            }
        }
    }

    // Handle nodes that are unreachable with -1 distance.
    for (int i = 0; i < N; i++) {
        if (dist[i] == 1e9)
            dist[i] = -1;
    }
    
    return dist;   // Return the array of distances from the source node.
}

```


### Shortest path in directed weighted graph
Started for a node with indegree 0

Here are we taking node 0 as always the one with indegree 0
```cpp
void dfs_on_graph(vector<pair<int, int>> adj[], vector<int> &vis, stack<int> &s, int curr) {
    vis[curr] = 1;   // Mark the current node as visited.

    // Explore adjacent nodes in a depth-first manner.
    for (auto it : adj[curr]) {
        int now = it.first;
        if (!vis[now])
            dfs_on_graph(adj, vis, s, now);   // Recursively visit unvisited neighbors.
    }

    s.push(curr);   // Push the current node to the stack after all its neighbors have been visited.
}

vector<int> shortestPath(int N, int M, vector<vector<int>>& edges) {
    vector<pair<int, int>> adj[N];   // Adjacency list with weights for the directed weighted graph.

    // Populate the adjacency list based on the edges and their weights.
    for (int i = 0; i < M; i++) {
        adj[edges[i][0]].push_back({edges[i][1], edges[i][2]});
    }

    vector<int> dist(N, 1e9), vis(N);
    stack<int> s;

    // Iterate through all nodes and perform DFS if not visited yet.
    for (int i = 0; i < N; i++) {
        if (!vis[i])
            dfs_on_graph(adj, vis, s, i);   // Perform DFS to create a topological ordering.
    }

    dist[0] = 0;   // Distance to the starting node is 0.
    while (!s.empty()) {
        int curr = s.top();
        s.pop();

        // Update distances to adjacent nodes if a shorter path is found.
        for (auto it : adj[curr]) {
            if (dist[curr] + it.second < dist[it.first])
                dist[it.first] = dist[curr] + it.second;
        }
    }

    // Handle nodes that are unreachable with -1 distance.
    for (int &it : dist) {
        if (it == 1e9)
            it = -1;
    }

    return dist;   // Return the array of shortest distances from the starting node.
}

```


> [!NOTE] Intuition
> Finding the shortest path to a vertex is easy if you already know the shortest paths to all the vertices that can precede it. Finding the longest path to a vertex in DAG is easy if you already know the longest path to all vertices that can precede it.
> Processing the vertices in topological order ensures that by the time you get to a vertex, you've already processed all the vertices that can precede it.
> Dijkstra's algorithm is necessary for graphs that can contain cycles, because they can't be topologically sorted.
