### Disjoint Set Data Structure (Union-Find)

The disjoint set data structure, also known as the union-find data structure, is used to efficiently manage a partition of elements into disjoint sets. It is commonly used to solve problems involving connectivity, such as determining if two elements are in the same set or finding connected components in a graph. The main operations in a disjoint set are `union` (combining sets) and `find` (determining the set representative). Here's a detailed explanation along with a C++ implementation:

```cpp
class DisjointSet {
public:
	vector<int> rank, parent, size;
    DisjointSet(int n) {
        rank.resize(n + 1, 0);
        parent.resize(n + 1);
        size.resize(n + 1);
        for (int i = 0; i <= n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    int findUPar(int node) {
        if (node == parent[node])
            return node;
        return parent[node] = findUPar(parent[node]);
    }

    void unionByRank(int u, int v) {
        int ulp_u = findUPar(u);
        int ulp_v = findUPar(v);
        if (ulp_u == ulp_v) return;
        if (rank[ulp_u] < rank[ulp_v]) {
            parent[ulp_u] = ulp_v;
        }
        else if (rank[ulp_v] < rank[ulp_u]) {
            parent[ulp_v] = ulp_u;
        }
        else {
            parent[ulp_v] = ulp_u;
            rank[ulp_u]++;
        }
    }

    void unionBySize(int u, int v) {
        int ulp_u = findUPar(u);
        int ulp_v = findUPar(v);
        if (ulp_u == ulp_v) return;
        if (size[ulp_u] < size[ulp_v]) {
            parent[ulp_u] = ulp_v;
            size[ulp_v] += size[ulp_u];
        }
        else {
            parent[ulp_v] = ulp_u;
            size[ulp_u] += size[ulp_v];
        }
    }
};
```

- The `DisjointSet` class encapsulates the disjoint set data structure with two union strategies: union by rank and union by size.
- The `rank` array keeps track of the rank of each set's representative (initially all set to 0).
- The `parent` array stores the parent representative of each element.
- The `size` array stores the size of each set (initially all set to 1).
- The constructor initializes each element as its own parent and sets its size to 1.
- `findUPar` method finds the ultimate parent of a node while performing path compression by updating the parent references along the path to the ultimate parent.
- `unionByRank` method implements the union by rank strategy. It compares the ranks of the ultimate parents and attaches the smaller rank tree under the root of the larger rank tree. If ranks are equal, it promotes the rank of one tree.
- `unionBySize` method implements the union by size strategy. It compares the sizes of the sets and attaches the smaller size tree under the root of the larger size tree. The size of the larger set is then updated.

These strategies ensure that the tree remains relatively balanced, which helps optimize the efficiency of the disjoint set data structure. You can choose either `unionByRank` or `unionBySize` based on your specific use case to achieve better performance.


> [!NOTE] Time Complexity
> O(4a) here a is almost equal to 1, thus we can consider it as constant time
