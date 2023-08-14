Lets take an array = {1, 2, 3}

| Subset       | Binary Representation |
|-------------|-------------------------|
| {}                | 000                |
| {1}              | 001                   |
| {2}              | 010                   |
| {1, 2}          | 011                   |
| {3}              | 100                   |
| {1, 3}          | 101                   |
| {2, 3}          | 110                   |
| {1, 2, 3}      | 111                   |

Binary representation corresponds to the index, if there is 1 somewhere we take that index of array.

```cpp
class Solution {
public:
    vector<vector<int>> subSetGeneration(vector<int>& nums) 
    {
        int n = nums.size();  // Get the size of the input array
        vector<vector<int>> ans;  // Initialize a vector to store subsets
        
        // Iterate over all possible combinations of elements using binary representation
        for (int i = 0; i < (1 << n); i++)  // Generating 2^n combinations
        {
            vector<int> temp;  // Temporary vector to hold each subset
            int j = i;  // Copy the current combination representation
            int count = 0;  // Counter to keep track of which element to consider
            
            // Extract individual elements from the current combination representation
            while (j != 0)
            {
                if (j & 1)  // Check if the last bit is set (element is included in subset)
                    temp.push_back(nums[count]);  // Add the corresponding element to the subset
                j = j >> 1;  // Shift right to process the next bit
                count++;  // Move to the next element
            }
            
            ans.push_back(temp);  // Add the generated subset to the answer vector
        }
        
        return ans;  // Return the vector containing all subsets of the input array
    }
};
```
