### Courses I
**1Q)** There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you **must** take course `bi` first if you want to take course `ai`.

- For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return `true` if you can finish all courses. Otherwise, return `false`.

- Basically a  question for detection of cycle in directed graph, return true if no cycle, else return false

```cpp
bool canFinish(int V, vector<vector<int>>& prerequisites) {
	vector<int> adj[V];
	int e = prerequisites.size();
	
	// Generating adjacency list
	for (int i = 0; i < e; i++)
	{
		adj[prerequisites[i][1]].push_back(prerequisites[i][0]);
	}
	
	vector<int> indegree(V);

	for (int i = 0; i < V; i++)
	{
		for (int it : adj[i])
		{
			indegree[it]++;
		}
	}

	queue<int> q;
	for (int i = 0; i < V; i++)
	{
		if (indegree[i] == 0)
			q.push(i);
	}
	
	int cnt = 0;
	while (!q.empty())
	{
		int curr = q.front();
		q.pop();
		cnt++;
		
		for (int it : adj[curr])
		{
			indegree[it]--;
			if (indegree[it] == 0)
				q.push(it);
		}
	}
	
	return cnt == V;
}
```

<hr>

### Courses II
**2Q)** There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you **must** take course `bi` first if you want to take course `ai`.

- For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return _the ordering of courses you should take to finish all courses_. If there are many valid answers, return **any** of them. If it is impossible to finish all courses, return **an empty array**.

- Same as previous question, but this time we need to return topological array if its possible to finish all courses

```cpp
// Function to find an ordering of courses to take in order to finish all of them.
// Returns a vector representing the course order, or an empty vector if impossible.
vector<int> findOrder(int V, vector<vector<int>>& matrix) {
    // Create an adjacency list to represent course prerequisites
    vector<int> adj[V];
    int e = matrix.size();
    
    // Populate the adjacency list based on prerequisites
    for (int i = 0; i < e; i++)
    {
        adj[matrix[i][1]].push_back(matrix[i][0]);
    }

    // Calculate the incoming edges (indegree) for each course
    vector<int> inorder(V), ans;

    for (int i = 0; i < V; i++)
    {
        for (int it : adj[i])
        {
            inorder[it]++;
        }
    }

    // Initialize a queue with courses having no prerequisites (indegree 0)
    queue<int> q;
    for (int i = 0; i < V; i++)
    {
        if (inorder[i] == 0)
            q.push(i);
    }

    // Perform topological sorting
    while (!q.empty())
    {
        int curr = q.front();
        q.pop();
        ans.push_back(curr);

        // Update indegree for dependent courses and enqueue them if indegree becomes 0
        for (int it : adj[curr])
        {
            inorder[it]--;
            if (inorder[it] == 0)
                q.push(it);
        }
    }

    vector<int> temp;

    // If the number of courses in the answer matches the total number of courses, return the answer
    if (ans.size() == V)
        return ans;
    else
        return temp; // Return an empty vector if it's impossible to finish all courses
}

```

<hr>

### Alien Dictionary
**3Q)** Given a sorted dictionary of an alien language having N words and k starting alphabets of standard dictionary. Find the order of characters in the alien language.  
**Note:** Many orders may be possible for a particular test case, thus you may return any valid order and output will be 1 if the order of string returned by the function is correct else 0 denoting incorrect string returned.

```cpp
string findOrder(string dict[], int N, int K) {
    vector<int> adj[K];         // Adjacency list representing the relationships between characters.
    vector<int> indegree(K);    // Store the indegree (number of incoming edges) for each character.
    
    // Construct the adjacency list and calculate indegrees based on the dictionary.
    for (int i = 0; i < N-1; i++) {
        string s1 = dict[i], s2 = dict[i+1];
        int min_len = min(s1.length(), s2.length());

        for (int j = 0; j < min_len; j++) 
        {
            if (s1[j] != s2[j]) 
            {
                int x = s1[j] - 'a';  // Convert character to index.
                int y = s2[j] - 'a';
                
				adj[x].push_back(y);   // Add y to the adjacency list of x.
				indegree[y]++;         // Increment the indegree of y.
				
                break;  // Break the loop when a difference is found, as the rest of the characters don't matter.
            }
        }  
    }

	// Good 'ol toposort
    queue<int> q;
    for (int i = 0; i < K; i++) {
        if (indegree[i] == 0)
            q.push(i);   // Add characters with indegree 0 to the queue.
    }

    string ans = "";
    while (!q.empty()) {
        int curr = q.front();
        q.pop();
        ans.push_back(curr + 'a');   // Append the character to the answer string.

        // Decrement indegree of adjacent characters and add them to the queue if indegree becomes 0.
        for (int it : adj[curr]) {
            if (--indegree[it] == 0)
                q.push(it);
        }
    }

    return ans;   // Return the order of characters.
}

```

