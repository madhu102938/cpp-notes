### Combination Sum
Finding all subsequences of a given vector that add up to a target sum, where elements can be picked **multiple** times
```cpp
#include <iostream>
#include <vector>

class Solution {
public: 
    // Recursive function to find all combinations of elements in the vector that add up to the target sum
    void findCombination(int ind, int target, std::vector<int> &arr, std::vector<std::vector<int>> &ans, std::vector<int>&ds) {
        // Base case: if we have reached the end of the vector
        if(ind == arr.size()) {
            // If the target sum is zero, we have found a valid combination
            if(target == 0) {
                ans.push_back(ds); // Add the current combination to the answer vector
            }
            return; 
        }
        // Recursive case 1: pick up the current element
        if(arr[ind] <= target) {
            ds.push_back(arr[ind]); // Add the current element to the current combination
            findCombination(ind, target - arr[ind], arr, ans, ds); // Recursively find combinations with the remaining sum
            ds.pop_back(); // Remove the current element from the current combination
        }
        // Recursive case 2: do not pick up the current element
        findCombination(ind+1, target, arr, ans, ds); // Recursively find combinations without the current element
    }
public:
    // Function to find all combinations of elements in the vector that add up to the target sum
    std::vector<std::vector<int>> combinationSum(std::vector<int>& candidates, int target) {
        std::vector<std::vector<int>> ans; // Vector to store all valid combinations
        std::vector<int> ds; // Vector to store the current combination
        findCombination(0, target, candidates, ans, ds); // Call the recursive function to find all valid combinations
        return ans; // Return the vector of all valid combinations
    }
};

int main()
{
    std::vector<int> v;
    int N;
    std::cout << "Enter the number of elements: ";
    std::cin >> N;
    std::cout << "Enter the elements: ";
    for (int i = 0; i < N; i++)
    {
        int temporary;
        std::cin >> temporary;
        v.push_back(temporary);
    }
    std::vector<int> temp;
    int sum;
    std::cout << "Enter the sum: ";
    std::cin >> sum;
    Solution ob;
    std::vector<std::vector<int>> result = ob.combinationSum(v, sum);
    for(auto i : result)
    {
        for(auto j : i)
            std::cout << j << " ";
        std::cout << std::endl;
    }
    return 0;
}
```

We are either picking an element or not picking it
- incase we are picking it, we are allowed to pick it again, thus we are not increasing the index
- incase we are not picking it, we are increasing the index by one, then we think about either picking up the next element or not.



### Combination Sum II
Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`.

Each number in `candidates` may only be used **once** in the combination.

**Note:** The solution set must not contain duplicate combinations.
```cpp
class Solution
{
public:
    void findCombination(int ind, int target, std::vector<int> &arr, std::vector<std::vector<int>> &ans, std::vector<int> &ds)
    {
        // Base case: if the target sum is 0, the current combination is valid
        if (target == 0)
        {
            // Sort the current combination and add it to the answer vector
            sort(ds.begin(), ds.end());
            ans.push_back(ds);
            return;
        }

        // Recursive case: pick up the current element and call the function recursively
        for (int i = ind; i < arr.size(); i++)
        {
            // Skip duplicate elements to avoid duplicate combinations
            if (i > ind && arr[i] == arr[i - 1])
                continue;
                
            // If the current element is less than or equal to the target sum, add it to the current combination
            if (arr[i] <= target)
            {
                ds.push_back(arr[i]);
                // Call the function recursively with the index incremented by 1 and the target sum reduced by the value of the current element
                findCombination(i + 1, target - arr[i], arr, ans, ds);
                // Remove the current element from the current combination
                ds.pop_back();
            }
        }
    }

public:
    vector<vector<int>> combinationSum2(vector<int> &candidates, int target)
    {
        std::vector<std::vector<int>> ans;
        std::vector<int> ds;

        // Sort the input vector to ensure that duplicate elements are adjacent
        sort(candidates.begin(), candidates.end());

        // Call the recursive function to find all unique combinations of elements that add up to the target sum
        findCombination(0, target, candidates, ans, ds);

        // Return the answer vector
        return ans;
    }
}

int main()
{
    std::vector<int> v;
    int N;
    std::cout << "Enter the number of elements: ";
    std::cin >> N;
    std::cout << "Enter the elements: ";
    for (int i = 0; i < N; i++)
    {
        int temporary;
        std::cin >> temporary;
        v.push_back(temporary);
    }
    int target;
    std::cout << "Enter the target: ";
    std::cin >> target;
    Solution sol;
    std::vector<std::vector<int>> ans = sol.combinationSum2(v, target);
    for (auto v : ans)
    {
        for (auto i : v)
        {
            std::cout << i << " ";
        }
        std::cout << "\n";
    }
    return 0;
}
```



### Subset sums
Given a list **arr** of **N** integers, print sums of all subsets in it.
```cpp
class Solution
{
private:
    void realSum(vector<int> &arr, int N, vector<int> &ans, int index = 0, int sum=0)
    {
        if(index == N)
        {
            ans.push_back(sum);
            return;
        }
        realSum(arr, N, ans, index + 1, sum + arr[index]);
        realSum(arr, N, ans, index + 1, sum);
    }
public:
    vector<int> subsetSums(vector<int> arr, int N)
    {
        vector<int> ans;
        realSum(arr, N, ans);
        return ans;
    }
};

int main()
{
    std::vector<int> v;
    int N;
    std::cout << "Enter the number of elements: ";
    std::cin >> N;
    std::cout << "Enter the elements: ";
    for (int i = 0; i < N; i++)
    {
        int temporary;
        std::cin >> temporary;
        v.push_back(temporary);
    }
    int target;
    std::cout << "Enter the target: ";
    std::cin >> target;
    Solution sol;
    std::vector<int> ans = sol.subsetSums(v, target);
    for (auto v : ans)
        std::cout << v << " ";
    std::cout << std::endl;
    return 0;
}
```



### Subsets II
Given an integer array `nums` that may contain duplicates, return _all possible subsets (the power set)_.
The solution set **must not** contain duplicate subsets. Return the solution in **any order**.
```cpp
class Solution
{
private:
    // Recursive function to find all subsets of the input vector
    void findSubsets(int ind, vector<int> &nums, vector<int> &ds, vector<vector<int>> &ans)
    {
        // Add the current subset to the answer vector
        ans.push_back(ds);

        // Iterate over the remaining elements in the input vector
        for (int i = ind; i < nums.size(); i++)
        {
            // Skip duplicate elements to avoid duplicate subsets
            if (i != ind && nums[i] == nums[i - 1])
                continue;

            // Add the current element to the current subset
            ds.push_back(nums[i]);

            // Recursively call the function with the index incremented by 1 and the current element added to the current subset
            findSubsets(i + 1, nums, ds, ans);

            // Remove the current element from the current subset to backtrack and explore other subsets
            ds.pop_back();
        }
    }

public:
    // Function to find all subsets of the input vector with duplicates
    vector<vector<int>> subsetsWithDup(vector<int> &nums)
    {
        vector<vector<int>> ans;
        vector<int> ds;

        // Sort the input vector to ensure that duplicate elements are adjacent
        sort(nums.begin(), nums.end());

        // Call the recursive function to find all subsets of the input vector
        findSubsets(0, nums, ds, ans);

        // Return the answer vector
        return ans;
    }
};

int main()
{
    Solution obj;
    vector<int> nums = {1, 2, 2};
    vector<vector<int>> ans = obj.subsetsWithDup(nums);

    // Print all subsets of the input vector
    for (auto v : ans)
    {
        for (auto x : v)
        {
            cout << x << " ";
        }
        cout << endl;
    }

    return 0;
}
```
