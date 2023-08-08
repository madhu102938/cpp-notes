Given an integer array `nums`, return `true` _if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or_ `false` _otherwise_.


**DP** solution
```cpp
class Solution {
private:
    bool actualAnswer(int index, int target, vector<int> &nums, vector<vector<int>> &dp)
    {
        if (target == 0)
            return true;
        if (index == 0)
            return (target == nums[0]);
        if (dp[index][target] != -1)
            return dp[index][target];
        int notPick = actualAnswer(index-1, target, nums, dp);
        int pick = 0;
        if (target >= nums[index])
            pick = actualAnswer(index-1, target-nums[index], nums, dp);
        return dp[index][target] = pick || notPick;
    }
public:
    bool canPartition(vector<int>& nums) {
        int numSum = 0;
        int n = nums.size();
        for (int i : nums)
                numSum += i;
        if (numSum%2 != 0)
                return false;
        else
        {
            int target = numSum / 2;
            vector<vector<int>> dp(n, vector<int>(target+1, -1));
            return actualAnswer(n-1, target, nums, dp);
        }
    }
};
```




**Tabulation** solution
```cpp
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int numSum = 0;
        int n = nums.size();
        for (int i : nums)
                numSum += i;
        if (numSum%2 != 0)
                return false;
        else
        {
            int target = numSum / 2;
            vector<vector<int>> dp(n, vector<int>(target+1, 0));
            for (int i = 0; i < n; i++)
                dp[i][0] = 1;
            if (nums[0] <= target)
                dp[0][nums[0]] = 1;
            for (int index = 1; index < n; index++)
            {
                for (int tar = 1; tar <= target; tar++)
                {
                    int notPick = dp[index-1][tar];
                    int pick = 0;
                    if (tar >= nums[index])
                        pick = dp[index-1][tar-nums[index]];
                    dp[index][tar] = pick || notPick;
                }
            }
            return dp[n-1][target];
        }
    }
};
```



**Space optimization** with tabulation
```cpp
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int numSum = 0;
        int n = nums.size();
        for (int i : nums)
                numSum += i;
        if (numSum%2 != 0)
                return false;
        else
        {
            int target = numSum / 2;
            vector<int>prev(target+1, 0);
            vector<int>curr(target+1, 0);
            prev[0] = 1;
            if (nums[0] <= target)
                prev[nums[0]] = 1;
            for (int index = 1; index < n; index++)
            {
                curr[0] = 1;
                for (int tar = 1; tar <= target; tar++)
                {
                    int notPick = prev[tar];
                    int pick = 0;
                    if (tar >= nums[index])
                        pick = prev[tar-nums[index]];
                    curr[tar] = pick || notPick;    
                }
                prev = curr;
            }
            return prev[target];
        }
    }
};
```



