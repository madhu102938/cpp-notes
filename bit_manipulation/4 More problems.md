**Q) You are given a list of numbers where all the numbers except two appear exactly twice, those 2 numbers appear only once, return those two numbers**
Brute force
- We can nest two for loops to get all the numbers which only appeared only once
Better
- We can use a map
Optimal
- Find the XOR of all elements in the array
- Find the position of the rightmost set bit in the XOR result
- Divide the elements into two groups based on the set bit at 'setbit' position
- XOR of all elements in 1st set gives us first element
- XOR of all elements in 2dn set gives us second element
```cpp
class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        int n = nums.size();
        int ans = nums[0];  // Initialize ans with the first element of the array
        
        // Step 1: Find the XOR of all elements in the array
        for (int i = 1; i < n; i++)
            ans = ans ^ nums[i];  // XOR operation combines all elements
        
        int setbit = 0;
        
        // Step 2: Find the position of the rightmost set bit in the XOR result
        while (ans != 0)
        {
            if (ans & 1)  // Check if the last bit is set
                break;
            ans = ans >> 1;  // Shift right to check the next bit
            setbit++;  // Increment the setbit count
        }

        int ans1 = 0, ans2 = 0;
        
        // Step 3: Divide the elements into two groups based on the set bit at 'setbit' position
        for (int i = 0; i < n; i++)
        {
            if (nums[i] & (1 << setbit))  // Check if the set bit at 'setbit' position is 1
                ans1 = ans1 ^ nums[i];  // XOR operation to find one unique element
            else
                ans2 = ans2 ^ nums[i];  // XOR operation to find the other unique element
        }
  
        vector<int> final_ans = {ans1, ans2};  // Store the unique elements in a vector
        return final_ans;  // Return the vector containing the two unique elements
    }
};

```

<hr>

**Q) Given N integers print the XOR of all subsets**
Answer will always be zero as every number will be repeating
[1,2,3] 
	[1]
	[2]
	[3]
	[1,2]
	[2,3]
	[1,3]
	[1,2,3]
As we can every number repeats, thus XOR of all subsets will zero, if there is only one element then that will edge case

<hr>

