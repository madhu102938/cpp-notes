If we can color all the nodes of the graph with only **two** colors such that **no** two adjacent nodes have the same color then graph is said to be **Bipartite graph**
- A **linear** graph is always **bipartite**
- A **even** cyclic graph is **bipartite**
- An **odd** cyclic graph is **not** bipartite

Code for checking if the graph is bipartite or not **Using BFS**
```cpp
bool actualAnswer(vector<vector<int>> &graph, vector<int> &vis, int prev)
{
    // Mark the current node as visited and initialize its group to 1.
    vis[prev] = 1;
    
    // Create a queue for BFS traversal and start with the current node.
    queue<int> q;
    q.push(prev);
    
    // Perform BFS traversal.
    while (!q.empty())
    {
        int curr = q.front();  // Get the front node from the queue.
        q.pop();  // Remove the front node from the queue.
        
        // Iterate through all adjacent nodes of the current node.
        for (auto it : graph[curr])
        {
            if (vis[it] == -1)  // If the adjacent node is not visited.
            {
                // Assign the opposite group value to the adjacent node.
                // If the current node's group is 1, the adjacent node's group becomes 0,
                // and vice versa. This creates the bipartite property.
                vis[it] = (vis[curr] == 1) ? 0 : 1;
                q.push(it);  // Add the adjacent node to the queue for further processing.
            }
            else
            {
                // If the adjacent node is already visited, check if it's in the same group
                // as the current node. If so, the graph is not bipartite.
                if (vis[curr] == vis[it])
                    return false;
            }
        }
    }
    
    return true;  // If the traversal completes without conflicts, the graph is bipartite.
}

bool isBipartite(vector<vector<int>> &graph)
{
    int V = graph.size();  // Get the number of nodes in the graph.
    vector<int> vis(V, -1);  // Create a vector to keep track of visited nodes and their groups.
    bool ans = true;  // Initialize the answer as true (graph is initially assumed to be bipartite).

    // Iterate through all nodes in the graph and check their bipartite property.
    for (int i = 0; i < V; i++)
    {
        if (vis[i] == -1)  // If the node is not visited yet.
            ans = actualAnswer(graph, vis, i);  // Check its bipartite property.
        
        // If at any point a conflict is detected, ans will be set to false,
        // and the function will immediately return false (not bipartite).
        if (ans == false)
            return false;
    }
    
    return true;  // If all nodes are visited and the graph remains bipartite, return true.
}

```

<hr>

using **DFS**
```cpp
bool actualAnswer(vector<vector<int>> &graph, vector<int> &vis, int prev, int color)
{
    vis[prev] = color;  // Mark the current node with the given color.
    
    // Iterate through all adjacent nodes of the current node.
    for (auto it : graph[prev])
    {
        if (vis[it] == -1)  // If the adjacent node is not visited.
        {
            // Recursively call the function on the adjacent node with the opposite color.
            // If the recursive call returns false, propagate the false result.
            if (actualAnswer(graph, vis, it, !color) == false)
                return false;
        }
        else if (vis[it] == vis[prev])  // If the adjacent node is already visited and has the same color.
            return false;  // Return false as this violates the bipartite property.
    }
    
    return true;  // If the traversal completes without conflicts, the graph is bipartite.
}

bool isBipartite(vector<vector<int>> &graph)
{
    int V = graph.size();  // Get the number of nodes in the graph.
    vector<int> vis(V, -1);  // Create a vector to keep track of visited nodes and their colors.
    
    // Iterate through all nodes in the graph and check their bipartite property.
    for (int i = 0; i < V; i++)
    {
        if (vis[i] == -1)  // If the node is not visited yet.
        {
            // Check its bipartite property, starting with color 0.
            if (actualAnswer(graph, vis, i, 0) == false)
                return false;  // If a conflict is detected, return false.
        }
    }
    
    return true;  // If all nodes are visited and the graph remains bipartite, return true.
}

```