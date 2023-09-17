### You are given an array list of n integers. You are supposed to return the maximum sum of the subsequence with the constraint that no two elements are adjacent in the given array list.

**Recurrence** solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int actualAnswer(vector<int> &nums, int index)
{
    if (index == 0)
        return nums[index];
    if (index < 0)
        return 0;
    int pick = actualAnswer(nums, index - 2) + nums[index];
    int notPick = actualAnswer(nums, index - 1);
	return max(pick, notPick);
}

int maximumNonAdjacentSum(vector<int> &nums)
{
    int ans = actualAnswer(nums, nums.size() - 1);
    return ans;
}
```

Solution with **DP**
```cpp
#include <bits/stdc++.h>
using namespace std;

int actualAnswer(vector<int> &nums, int index, vector<int> &dp)
{
    if (index == 0)
        return nums[index];
    if (index < 0)
        return 0;
    if(dp[index] != -1)
        return dp[index];
    int pick = actualAnswer(nums, index - 2, dp) + nums[index];
    int notPick = actualAnswer(nums, index - 1, dp);
    dp[index] = max(pick, notPick);
    return dp[index];
}

int maximumNonAdjacentSum(vector<int> &nums)
{
    vector<int> dp(nums.size() + 1, -1);
    int ans = actualAnswer(nums, nums.size() - 1, dp);
    return ans;
}
```

Solution with **Tabulation**
```cpp
#include <bits/stdc++.h>
using namespace std;

int actualAnswer(vector<int> &nums, vector<int> &dp)
{
    dp[0] = nums[0];
    int negative = 0;
    int n = nums.size();
    for(int i = 1; i < n; i++)
    {
	    int pick = nums[i];
	    if(i - 2 < 0)
		    pick += negative;
		else
			pick += dp[i - 2];
	    int notPick = dp[i - 1];
	    dp[i] = max(pick, notPick);
    }
    return dp[n - 1];
}

int maximumNonAdjacentSum(vector<int> &nums)
{
    vector<int> dp(nums.size() + 1, -1);
    int ans = actualAnswer(nums, dp);
    return ans;
}
```

**Space optimization** with tabulation
```cpp
#include <bits/stdc++.h> 
using namespace std;

int actualAnswer(vector<int> &nums)
{
    int prev = nums[0];
    int prev2 = 0;
    int n = nums.size();
    for(int i = 1; i < n; i++)
    {
	    int pick = nums[i];
        if(i - 2 < 0)
		    pick += 0;
		else
			pick += prev2;
	    int notPick = prev;
	    int current = max(pick, notPick);
        prev2 = prev;
        prev = current;
    }
    return prev;
}

int maximumNonAdjacentSum(vector<int> &nums)
{
    int ans = actualAnswer(nums);
    return ans;
}
```

### House Robber II
#### Mr. X is a professional robber planning to rob houses along a street. Each house has a certain amount of money hidden. All houses along this street are arranged in a circle; that means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night

Since this is circular, first and last are neighbors, so we cannot directly use the logic from the previous problem.
- First we will send an array with elements from $0$ to `n-2` and store the result in `ans1`
- Then we will send an array with elements from $1$ to `n-1` and store the result in `ans2`
- We will return the maximum of `ans1` and `ans2`

**Recurrence** solution
```cpp
#include <bits/stdc++.h> 
using namespace std;

int actualAnswer(vector<int> &housesOne, int index)
{
    if(index == 0)
        return housesOne[0];
    if(index < 0)
        return 0;
    int left = actualAnswer(housesOne, index - 2) + housesOne[index];
    int right = actualAnswer(housesOne, index - 1);
    return max(left, right);
}

long long int houseRobber(vector<int>& valueInHouse)
{
    if(valueInHouse.size() == 1)
        return valueInHouse[0];
    vector<int> housesOne, housesTwo;

    for (auto i = 0; i < valueInHouse.size(); i++) 
    {
        if (i != n - 1)
            housesOne.push_back(valueInHouse[i]);
        if (i != 0)
            housesTwo.push_back(valueInHouse[i]);
    }
    
    int ans1 = actualAnswer(housesOne, housesOne.size() - 1);
    int ans2 = actualAnswer(housesTwo, housesTwo.size() - 1);
    return max(ans1, ans2);
}
```

Solution with **DP**
```cpp
#include <bits/stdc++.h> 
using namespace std;

int actualAnswer(vector<int> &housesOne, int index, vector<int> &dp)
{
    if(index == 0)
        return housesOne[0];
    if(index < 0)
        return 0;
    if(dp[index] != -1)
        return dp[index];
    int left = actualAnswer(housesOne, index - 2, dp) + housesOne[index];
    int right = actualAnswer(housesOne, index - 1, dp);
    dp[index] = max(left, right);
    return dp[index];
}

int houseRobber(vector<int>& valueInHouse)
{
    int n = valueInHouse.size();
    if(n == 1)
        return valueInHouse[0];
    vector<int> dp1(n, -1);
    vector<int> dp2(n, -1);
    vector<int> housesOne, housesTwo;

    for (auto i = 0; i < valueInHouse.size(); i++) 
    {
        if (i != n - 1)
            housesOne.push_back(valueInHouse[i]);
        if (i != 0)
            housesTwo.push_back(valueInHouse[i]);
    }
    
    int ans1 = actualAnswer(housesOne, housesOne.size() - 1, dp1);
    int ans2 = actualAnswer(housesTwo, housesTwo.size() - 1, dp2);
    return max(ans1, ans2);
}
```

Solution with **Tabulation**
```cpp
#include <bits/stdc++.h> 
using namespace std;

int actualAnswer(vector<int> &nums, vector<int> &dp)
{
    dp[0] = nums[0];
    int negative = 0;
    int n = nums.size();
    for(int i = 1; i < n; i++)
    {
	    int pick = nums[i];
	    if(i - 2 < 0)
		    pick += negative;
		else
			pick += dp[i - 2];
	    int notPick = dp[i - 1];
	    dp[i] = max(pick, notPick);
    }
    return dp[n - 1];
}

int houseRobber(vector<int>& valueInHouse)
{
    int n = valueInHouse.size();
    if(n == 1)
        return valueInHouse[0];
    vector<int> dp1(n, -1);
    vector<int> dp2(n, -1);
    vector<int> housesOne, housesTwo;

    for (auto i = 0; i < valueInHouse.size(); i++) 
    {
        if (i != n - 1)
            housesOne.push_back(valueInHouse[i]);
        if (i != 0)
            housesTwo.push_back(valueInHouse[i]);
    }
    
    int ans1 = actualAnswer(housesOne, dp1);
    int ans2 = actualAnswer(housesTwo, dp2);
    return max(ans1, ans2);
}
```

**Space Optimization** of Tabulation
```cpp
#include <bits/stdc++.h> 
using namespace std;

int actualAnswer(vector<int> &nums)
{
    int prev = nums[0];
    int prev2 = 0;
    int n = nums.size();
    for(int i = 1; i < n; i++)
    {
	    int pick = nums[i];
        if(i - 2 < 0)
		    pick += 0;
		else
			pick += prev2;
	    int notPick = prev;
	    int current = max(pick, notPick);
        prev2 = prev;
        prev = current;
    }
    return prev;
}

int houseRobber(vector<int>& valueInHouse)
{
    int n = valueInHouse.size();
    if(n == 1)
        return valueInHouse[0];
    vector<int> housesOne, housesTwo;

    for (auto i = 0; i < valueInHouse.size(); i++) 
    {
        if (i != n - 1)
            housesOne.push_back(valueInHouse[i]);
        if (i != 0)
            housesTwo.push_back(valueInHouse[i]);
    }
    
    int ans1 = actualAnswer(housesOne);
    int ans2 = actualAnswer(housesTwo);
    return max(ans1, ans2);
}
```
