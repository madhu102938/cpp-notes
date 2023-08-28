### Using Priority Queue
```cpp
// Dijkstra's algorithm implementation in C++

// This function performs Dijkstra's algorithm to find the shortest distances from a source node to all other nodes in a weighted graph.
// Inputs:
//   V: Number of nodes in the graph
//   adj: Adjacency list representation of the graph where adj[i] is a vector of pairs (node, weight) representing edges from node i
//   S: Source node from which to find the shortest distances
// Outputs:
//   Returns a vector of shortest distances from the source node to all other nodes

vector<int> dijkstra(int V, vector<vector<int>> adj[], int S)
{
    // Priority queue to store nodes with their current distance from the source
    // Min heap priority queue, smallest element will be on top
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    
    // Initialize a vector to store the shortest distances, all initialized to a large value
    vector<int> dist(V, 1e9);
    
    // Set the distance of the source node to itself as 0
    dist[S] = 0;
    
    // Push the source node and its distance (0) into the priority queue
    pq.push({0, S});
    
    // Start the main loop
    while (!pq.empty())
    {
        // Get the node with the smallest distance from the priority queue
        int dis = pq.top().first;   // Current distance
        int node = pq.top().second; // Current node
        pq.pop();                   // Remove the node from the queue
        
        // Iterate through the adjacent nodes of the current node
        for (auto it : adj[node])
        {
            // Calculate the potential new distance to reach the adjacent node through the current node
            int new_distance = it[1] + dis;
            
            // If the new distance is smaller than the current known distance to the adjacent node,
            // update the distance and push the adjacent node into the priority queue
            if (new_distance < dist[it[0]])
            {
                dist[it[0]] = new_distance;
                pq.push({dist[it[0]], it[0]});
            }
        }
    }
    
    // Return the vector containing the shortest distances from the source node
    return dist;
}

```

***Time Complexity** - $E * log(V)$
E : no. of edges || V : no. of vertices*
- We replace `priority_queue` with regular `queue` and it will still work fine.


### Using Set
```cpp
// Function to find the shortest distances from a source vertex to all other vertices
vector<int> dijkstra(vector<vector<int>> &edge, int v, int e, int src) 
{
    vector<pair<int, int>> adj[v]; // Adjacency list representation of the graph
    for (int i = 0; i < e; i++) 
    {
        // Creating the adjacency list using input edge information
        adj[edge[i][0]].push_back({edge[i][1], edge[i][2]});
        adj[edge[i][1]].push_back({edge[i][0], edge[i][2]});
    }

    vector<int> dist(v, 1e9); // Initialize distances to a large value
    set<pair<int, int>> s;    // Set to keep track of vertices with their distances
    s.insert({0, src});       // Insert source vertex with distance 0
    dist[src] = 0;            // Set distance of source vertex to 0

    // Dijkstra's algorithm loop
    while (!s.empty()) 
    {
        auto now = *(s.begin()); // Get the vertex with the smallest distance
        int dis = now.first;     // Current shortest distance
        int curr = now.second;   // Current vertex
        s.erase(now);            // Remove the current vertex from the set

        // Traverse the neighbors of the current vertex
        for (auto it : adj[curr]) 
        {
            // Update the distance if a shorter path is found
            if (it.second + dis < dist[it.first]) 
            {
                if (dist[it.first] != 1e9)
                    s.erase({dist[it.first], it.first}); // Remove old entry from set
                s.insert({it.second + dis, it.first});  // Insert updated entry into set
                dist[it.first] = it.second + dis;        // Update distance
            }
        }
    }

    return dist; // Return the vector of shortest distances
}
```


- Here we are erasing previous entry of a node, if we find a better distance, this will reduce the iterations
- But erasing elements in set takes complexity of $log(N)$ 
**- [plus] Reducing the iterations, by erasing previous entries when better ones are found**
**- [minus] erasing taking $log(N)$ time**
Basing these two we can cannot clearly say if set is actually the more efficient approach compared to priority queue approach.