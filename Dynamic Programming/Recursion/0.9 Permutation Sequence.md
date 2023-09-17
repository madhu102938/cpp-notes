The set `[1, 2, 3, ..., n]` contains a total of `n!` unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for `n = 3`:

1. `"123"`
2. `"132"`
3. `"213"`
4. `"231"`
5. `"312"`
6. `"321"`

Given `n` and `k`, return the `kth` permutation sequence.

```cpp
class Solution {
public:
    string getPermutation(int n, int k) 
    {
        // Calculate (n-1)! and store it in 'fact'
        int fact = 1;
        for (int i = 1; i < n; i++)
        {
            fact = fact * i;
        }
        
        // Create a vector 'v' containing the numbers 1 to n
        vector<int> v;
        for (int i = 1; i <= n; i++)
        {
            v.push_back(i);
        }
        
        // Initialize an empty string 'ans'
        string ans = "";
        
        // Decrement 'k' to account for 0-based indexing
        k--;
        
        // Loop until 'v' is empty
        while (true)
        {
            // Append the (k/fact)-th element of 'v' to 'ans'
            ans = ans + to_string(v[k/fact]);
            
            // Remove the (k/fact)-th element of 'v'
            v.erase(v.begin() + k/fact);
            
            // If 'v' is empty, break out of the loop
            if (v.size() == 0)
                break;
            
            // Update 'k' and 'fact' for the next iteration
            k = k % fact;
            fact = fact / v.size();
        }
        
        // Return the final permutation
        return ans;
    }
};
```