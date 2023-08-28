### Using DFS
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

<hr>

**1Q)** There is a directed graph of `n` nodes with each node labeled from `0` to `n - 1`. The graph is represented by a **0-indexed** 2D integer array `graph` where `graph[i]` is an integer array of nodes adjacent to node `i`, meaning there is an edge from node `i` to each node in `graph[i]`.

A node is a **terminal node** if there are no outgoing edges. A node is a **safe node** if every possible path starting from that node leads to a **terminal node** (or another safe node).

Return _an array containing all the **safe nodes** of the graph_. The answer should be sorted in **ascending** order.


- Nodes part of a cycle cannot be safe
- Nodes leading to cycle cannot be safe

```cpp
bool actualAnswer(vector<vector<int>> &graph, vector<int> &vis, vector<int> &path, vector<int> &ans, int curr) {
    // Mark the current node as unsafe
    ans[curr] = 0;
    // Mark the current node as visited
    vis[curr] = 1;
    // Mark the current node as part of the current traversal path
    path[curr] = 1;

    // Traverse through all adjacent nodes of the current node
    for (int it : graph[curr]) {
        // If the adjacent node hasn't been visited yet
        if (!vis[it]) {
            // Recursively check if this node is part of a cycle or leads to a cycle
            if (actualAnswer(graph, vis, path, ans, it))
                return true;
        }
        // If the adjacent node is part of the current traversal path, it's part of a cycle
        else if (path[it])
            return true;
    }

    // Mark the current node as safe and remove it from the current path
    ans[curr] = 1;
    vis[curr] = 0;
    return false;
}

vector<int> eventualSafeNodes(vector<vector<int>> &graph) {
    int V = graph.size();
    // vis array keeps track of visited nodes
    // path array keeps track of nodes in the current traversal path
    // ans array stores whether a node is safe (1) or not (0)
    vector<int> vis(V, 0), path(V, 0), ans(V, 0);

    // Iterate through all nodes
    for (int i = 0; i < V; i++) {
        // If the node hasn't been visited, start checking if it's safe
        if (!vis[i])
            actualAnswer(graph, vis, path, ans, i);
    }

    vector<int> safeNodes;
    // Collect all safe nodes into the safeNodes vector
    for (int i = 0; i < V; i++) {
        if (ans[i] == 1)
            safeNodes.push_back(i);
    }

    return safeNodes;
}

```


**Approach 2**
- Using topological sort, but with outdegree vector
- If we were to indegree topological sort, then we would have just eliminated the nodes of the loop element, but the elements that lead to a loop would be left out
- To account for that we are using an outdegree vector
- We create a reversed adjacency list
- We calculate outdegree of each node, and push those that have outdegree as zero, we push them to queue
- We reduce the outdegree of other element connected to the ones in the queue and continue that process
```cpp
vector<int> eventualSafeNodes(vector<vector<int>> &graph) {
    int V = graph.size();
    vector<int> out[V];         // Create an "inverse" graph where nodes point to their parents.
    vector<int> outdegree(V);   // Store the outdegree (number of outgoing edges) for each node.
    vector<int> ans;            // Store the safe nodes.
    queue<int> q;               // Queue for BFS traversal.

    // Loop through each node in the graph.
    for (int i = 0; i < V; i++) {
        // Create the inverse graph and calculate outdegree for each node.
        for (int it : graph[i]) {
            out[it].push_back(i);   // Add the current node as a parent to its neighbor.
        }
        outdegree[i] = graph[i].size();  // Store the number of outgoing edges.
        if (outdegree[i] == 0)
            q.push(i);   // If outdegree is 0, add the node to the queue.
    }
    
    // Perform BFS traversal to identify safe nodes.
    while (!q.empty()) {
        int curr = q.front();   // Get the current node from the front of the queue.
        q.pop();

        ans.push_back(curr);    // Add the current node to the list of safe nodes.

        // Decrement outdegree of each parent node and add to queue if outdegree becomes 0.
        for (int it : out[curr]) {
            --outdegree[it];
            if (outdegree[it] == 0)
                q.push(it);
        }
    }
    
    sort(ans.begin(), ans.end());   // Sort the safe nodes in ascending order.
    return ans;   // Return the list of safe nodes.
}

```