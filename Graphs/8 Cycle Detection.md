### Using BFS
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
