Generally in questions we will be given `n` and `m` where `n` means number of *nodes* and `m` means number of *edges* and we will be given *2D array* which tells us how the nodes are connected

## Adjacency Matrix
```cpp
int main()
{
    int n, m;
    cin >> n >> m;
    // adjacency matrix for undirected graph
    // time complexity: O(n)
    // Space complexity = O(n*n)
    int adj[n+1][n+1];
    for(int i = 0; i < m; i++)
    {
        int u, v;
        cin >> u >> v;
        adj[u][v] = 1;
        adj[v][u] = 1;  // this statement will be removed in case of directed graph
    }
    return 0;
}
```

For weighted graphs we store the weight instead of 1
```cpp
int main()
{
    int n, m;
    cin >> n >> m;
    // adjacency matrix for undirected graph
    // time complexity: O(n)
    // Space complexity = O(n*n)
    int adj[n+1][n+1];
    for(int i = 0; i < m; i++)
    {
        int u, v;
        cin >> u >> v >> w;
        adj[u][v] = w;
        adj[v][u] = w;  // this statement will be removed in case of directed graph
    }
    return 0;
}
```

## Adjacency Lists
```cpp
int main()
{
    int n, m;
    cin >> n >> m;
    // adjacency list for undirected graph
    // time complexity: O(2E) E - no. of edges
    vector<int> adj[n+1]; // Array of vectors
    for(int i = 0; i < m; i++)
    {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u); // this statement will be removed in case of directed graph
    }
    return 0;
}
```

For weighted graphs we used `vector<pair<int, int>> adj[n+1]`
```cpp
int main()
{
    int n, m;
    cin >> n >> m;
    // adjacency list for undirected graph
    // time complexity: O(2E)
    vector<int> adj[n+1];
    for(int i = 0; i < m; i++)
    {
        int u, v;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w}); // this statement will be removed in case of directed graph
    }
    return 0;
}
```

