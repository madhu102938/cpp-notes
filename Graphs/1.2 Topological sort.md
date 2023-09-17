Topological sort is a linear ordering of the vertices in a directed acyclic graph (DAG) such that for every directed edge `(u, v)`, vertex `u` comes before vertex `v` in the ordering. In other words, it is a way of arranging the nodes of a DAG in a sequence such that each node appears before all the nodes that depend on it.

Topological sort is useful in many applications, such as task scheduling, dependency resolution, and determining the order of compilation tasks in a build system. It can be performed using a modified depth-first search algorithm that visits each node in the graph and adds it to a stack after all its dependent nodes have been visited.

If the graph contains a cycle, then it is not possible to perform a topological sort, since there is no way to order the nodes such that all dependencies are satisfied. Therefore, topological sort can only be performed on DAGs.

In C++, topological sort can be implemented using various algorithms, such as the Kahn's algorithm or the DFS-based algorithm.

### Using DFS

```cpp
// Function to perform depth-first traversal and populate the stack with nodes in topological order.
void actualAnswer(vector<int> adj[], vector<int> &vis, stack<int> &s, int curr)
{
    // Mark the current node as visited
    vis[curr] = 1;
    
    // Traverse through all adjacent nodes of the current node
    for (int it : adj[curr])
    {
        // If the adjacent node hasn't been visited yet, recursively explore it
        if (!vis[it])
            actualAnswer(adj, vis, s, it);
    }
    
    // Push the current node onto the stack after visiting all of its adjacent nodes
    s.push(curr);
}

// Function to perform topological sort on a directed acyclic graph.
// Returns a list of vertices in topological order.
vector<int> topoSort(int V, vector<int> adj[]) 
{
    // Array to keep track of visited nodes
    vector<int> vis(V);
    // Stack to store nodes in topological order
    stack<int> s;
    
    // Iterate through all nodes
    for (int i = 0; i < V; i++)
    {
        // If the node hasn't been visited, initiate DFS traversal from it
        if (!vis[i])
            actualAnswer(adj, vis, s, i);    
    }
    
    vector<int> ans;
    // Pop nodes from the stack and store them in the result vector
    while (!s.empty())
    {
        ans.push_back(s.top());
        s.pop();
    }
    
    return ans;
}

```


### Using Kahn's Algorithm (BFS)

- Add all the nodes with indegree 0, add to the queue
- For each node in the queue, remove the outgoing edges to its adjacent nodes
- if any adjacent node's indegree becomes 0, add it to queue
- Repeat until queue is empty
```cpp
// Function to perform topological sort using Khan's algorithm on a directed acyclic graph.
// Returns a list of vertices in topological order.
vector<int> topoSort(int V, vector<int> adj[]) 
{
    // Array to store the indegree of each vertex
    vector<int> indegree(V);
    // Resultant vector to store the topological order
    vector<int> ans;
    
    // Calculate the indegree of each vertex by traversing the adjacency list
    for (int i = 0; i < V; i++)
    {
        for (int it : adj[i])
        {
            indegree[it]++;
        }
    }

    // Initialize a queue to keep track of nodes with indegree 0
    queue<int> q;
    // Push nodes with indegree 0 into the queue to start the algorithm
    for (int i = 0; i < V; i++)
    {
        if (indegree[i] == 0)
            q.push(i);
    }

    // Process nodes in the queue
    while (!q.empty())
    {
        // Get the front node from the queue
        int curr = q.front();
        q.pop();
        // Add the current node to the result
        ans.push_back(curr);
        
        // Decrement the indegree of adjacent nodes and push those with indegree 0 to the queue
        for (int it : adj[curr])
        {
            indegree[it]--;
            if (indegree[it] == 0)
                q.push(it);
        }
    }
    
    return ans;
}
```


### Cycle detection in directed graph (BFS)
Using Topological sort
- Since topological sort doesn't work for cyclic graph, If the length of topological array is less than number of nodes then there must be a cycle
```cpp
// Function to check if a directed graph contains a cycle using Khan's algorithm.
// Returns true if a cycle is detected, false otherwise.
bool isCyclic(int V, vector<int> adj[]) {
    // Array to store the indegree of each vertex
    vector<int> indegree(V);

    // Calculate the indegree of each vertex by traversing the adjacency list
    for (int i = 0; i < V; i++)
    {
        for (int it : adj[i])
        {
            indegree[it]++;
        }
    }

    // Initialize a queue with vertices having indegree 0
    queue<int> q;
    for (int i = 0; i < V; i++)
    {
        if (indegree[i] == 0)
            q.push(i);
    }
    
    int cnt = 0; // Counter to keep track of processed vertices

    // Perform topological sorting while removing vertices with indegree 0
    while (!q.empty())
    {
        int curr = q.front();
        q.pop();
        cnt++;
        
        // Traverse the adjacency list of the current vertex
        for (int it : adj[curr])
        {
            // Decrement the indegree of adjacent vertices
            indegree[it]--;
            // If the indegree becomes 0, enqueue the vertex
            if (indegree[it] == 0)
                q.push(it);
        }
    }
    
    // If the count of processed vertices is less than the total number of vertices,
    // then there must be a cycle in the graph
    return cnt != V;
}

```