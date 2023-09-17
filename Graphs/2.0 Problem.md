### Find the City With the Smallest Number of Neighbors at a Threshold Distance

You are given a network of `n` nodes, labeled from `1` to `n`. You are also given `times`, a list of travel times as directed edges `times[i] = (ui, vi, wi)`, where `ui` is the source node, `vi` is the target node, and `wi` is the time it takes for a signal to travel from source to target.

We will send a signal from a given node `k`. Return _the **minimum** time it takes for all the_ `n` _nodes to receive the signal_. If it is impossible for all the `n` nodes to receive the signal, return `-1`.

```cpp
int dijkstra(int source, vector<pair<int,int>> adj[],int &n, int &dt) {
    vector<int> dis(n,INT_MAX);
    
    // Priority queue to store nodes and their distances from the source node.
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>> > pq;
    pq.push({0,source});
    dis[source] = 0;
    
    // Dijkstra's algorithm loop
    while(!pq.empty()) {
        int node = pq.top().second;
        int dist = pq.top().first;
        pq.pop();
        
        // Iterate through neighboring nodes of the current node.
        for(auto child:adj[node]) {
            int nextnode = child.first;
            int nextdist = child.second;
            
            // Relaxation step: update distance if a shorter path is found.
            if(dis[node] + nextdist < dis[nextnode]) {
                dis[nextnode] = dis[node] + nextdist;
                pq.push({dis[nextnode],nextnode});
            }
        }
    }
    
    // Count nodes that can be reached within the distance threshold.
    int count = 0;
    for(int i=0; i<dis.size(); i++) {
        if(dis[i] <= dt) {
            count++;
        }
    }
    return count;
}

int findTheCity(int n, vector<vector<int>>& edges, int distanceThreshold) {
    vector<pair<int,int>> adj[n];
    
    // Create adjacency list representation of the graph.
    for(int i=0; i<edges.size(); i++) {
        int u = edges[i][0], v = edges[i][1], w = edges[i][2];
        adj[u].push_back({v,w});
        adj[v].push_back({u,w});
    }
    
    int maxe = INT_MAX;
    int ans = -1;
    
    // Iterate through each node as the potential starting node.
    for(int i=0; i<n; i++) {
        // Calculate the count of nodes reachable from the current node within the threshold.
        int count = dijkstra(i, adj, n, distanceThreshold);
        
        // Update maxe and ans if a better starting node is found.
        if(count <= maxe) {
            maxe = count;
            ans = i;
        }
    }
    
    return ans; // Return the optimal starting node.
}

```