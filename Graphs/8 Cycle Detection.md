### Using BFS
For **undirected**
```cpp
bool actualAnswer(int node, vector<int> adj[], int vis[])
{
    vis[node] = 1; // Mark the current node as visited
    queue<pair<int, int>> q; // Create a queue to perform BFS
    q.push({node, -1}); // Push the current node and its previous node (initialized as -1) into the queue

    while (!q.empty())
    {
        int curr = q.front().first; // Get the current node from the front of the queue
        int prev = q.front().second; // Get the previous node from the front of the queue
        q.pop(); // Remove the processed node from the queue

        // Iterate through all neighbors of the current node
        for (auto it : adj[curr])
        {
            if (!vis[it]) // If the neighbor hasn't been visited
            {
                vis[it] = 1; // Mark the neighbor as visited
                q.push({it, curr}); // Push the neighbor into the queue along with the current node as the previous node
            }
            else if (prev != it) // If the neighbor has been visited and it's not the previous node (meaning it's not the direct parent)
                return true; // A back edge is found, indicating a cycle
        }
    }
    return false; // No cycle found
}

bool isCycle(int V, vector<int> adj[])
{
    int vis[V] = {0}; // Create an array to keep track of visited nodes, initialized as 0 (not visited)
    for (int i = 0; i < V; i++)
    {
        if (!vis[i]) // If the node hasn't been visited
        {
            if (actualAnswer(i, adj, vis)) // Call the actualAnswer function to detect a cycle starting from the current node
                return true; // If a cycle is found, return true
        }
    }
    return false; // If no cycle is found after checking all nodes, return false
}
```

<hr>

### Using DFS
for **undirected**
```cpp
bool actualAnswer(int node, vector<int> adj[], int vis[])
{
    queue<pair<int, int>> q;
    q.push({node, -1}); // Push the current node and its parent node into the queue
    vis[node] = 1; // Mark the current node as visited
    while (!q.empty())
    {
        int curr = q.front().first; // Store the current node
        int parent = q.front().second; // Store the parent node
        q.pop(); // Pop the current node
        for (auto it : adj[curr])
        {
            if (!vis[it])
            {
                vis[it] = 1; // Mark the current node as visited
                q.push({it, curr}); // Push the current node and its parent node into the queue
            }
            else if (it != parent) // If the current node has been visited and it is not the parent node
                return true;
        }
    }
    return false; // If no cycle is found, return false
    
}

bool isCycle(int V, vector<int> adj[])
{
    int vis[V] = {0}; // Create an array to keep track of visited nodes, initialized as 0 (not visited)
    for (int i = 0; i < V; i++)
    {
        if (!vis[i]) // If the node hasn't been visited
        {
            if (actualAnswer(i, adj, vis)) // Call the actualAnswer function to detect a cycle starting from the current node
                return true; // If a cycle is found, return true
        }
    }
    return false; // If no cycle is found after checking all nodes, return false
}
```

For **directed**
```cpp
bool actualAnswer(vector<int> adj[], vector<int> &vis, vector<int> &path, int curr)
{
    vis[curr] = 1;    // Mark the current node as visited.
    path[curr] = 1;   // Mark the current node as part of the current path being traversed.

    // Iterate through all adjacent nodes of the current node.
    for (auto it : adj[curr])
    {
        if (!vis[it])  // If the adjacent node is not visited yet.
        {
            // Recursively check for a cycle starting from the adjacent node.
            if (actualAnswer(adj, vis, path, it))
                return true;  // If a cycle is found, propagate the true result.
        }
        else if (path[it])  // If the adjacent node is part of the current path being traversed.
            return true;     // Return true as a cycle is detected in the current path.
    }
    
    path[curr] = 0;  // Remove the current node from the path as the traversal backtracks.
    return false;    // If no cycle is found in the current path, return false.
}

bool isCyclic(int V, vector<int> adj[])
{
    vector<int> vis(V, 0);    // Create a vector to track visited nodes.
    vector<int> path(V, 0);   // Create a vector to track nodes in the current path.

    // Iterate through all nodes in the graph.
    for (int i = 0; i < V; i++)
    {
        if (!vis[i])  // If the node is not visited yet.
        {
            // Check for a cycle starting from the current node.
            if (actualAnswer(adj, vis, path, i))
                return true;  // If a cycle is found, return true.
        }
    }
    
    return false;  // If no cycle is found in any path, return false.
}

```