There is a frog on the 1st step of an n-stairs long staircase. The frog wants to reach the nth stair's height. H(i) is the height of the (i+1)th stair. If the frog jumps from the ith to the jth stair, the energy lost in the jump is given by the absolute value of (H(i+1) - H(j+1)). If the frog is on the ith staircase, he can jump either to the (i+1)th stair or to the (i+2)th stair. Your task is to find the minimum total energy used by the frog to reach from the 1st stair to the nth stair.

### recurrence relationship of this is like
```cpp
#include <bits/stdc++.h> 
using namespace std;
int actualAnswer(int n, vector<int> &heights, int index = 0)
{
    if(index == n-1)
        return 0;
    int right = INT_MAX;
    int left = actualAnswer(n, heights, index + 1) + abs(heights[index] - heights[index + 1]);
    if(index < n-2)
        right = actualAnswer(n, heights, index + 2) + abs(heights[index] - heights[index + 2]);
	return min(left, right);
}


int frogJump(int n, vector<int> &heights)
{
    int ans = actualAnswer(heights.size(), heights);
    return ans;
}
```
- frog can either jump 1 step or 2 steps
	- in each case, we have to add the energy it takes
- then we return the **minimum** of both
- ***Time Complexity** - O($2^n$)*
- Here we are going from **index 0 to index n-1**, we can do the opposite too
```cpp
#include <bits/stdc++.h>
using namespace std;
int actualAnswer(int index, vector<int> &heights)
{
	if (index == 0)
		return 0;
	int left = actualAnswer(index - 1, heights) + abs(heights[index] - heights[index - 1]);
	int right = INT_MAX;
	if(index > 1)
		right = actualAnswer(index - 2, heights) + abs(heights[index] - heights[index - 2]);
	return min(left, right);
}

int frogJump(int n, vector<int> &heights)
{
	int ans = actualAnswer(heights.size() - 1, heights);
	return ans;
}
```


### Doing it with DP
```cpp
#include <bits/stdc++.h> 
using namespace std;
int actualAnswer(int n, vector<int> &heights, vector<int> &dp, int index = 0)
{
    if(index == n-1)
        return 0;
    if(dp[index] != -1)
        return dp[index];
    int right = INT_MAX;
    int left = actualAnswer(n, heights, dp, index + 1) + abs(heights[index] - heights[index + 1]);
    if(index < n-2)
        right = actualAnswer(n, heights, dp, index + 2) + abs(heights[index] - heights[index + 2]);
    dp[index] = min(left, right);
    return dp[index];
}


int frogJump(int n, vector<int> &heights)
{
    vector<int> dp(heights.size()+1, -1);
    int ans = actualAnswer(heights.size(), heights, dp);
    return ans;
}
```
- we are initializing dp vector with $-1$s, we are updating dp vector with each function call
- We are using those values in the future calls if needed.
- ***Time Complexity** - O(N)*
Doing it in the opposite way
```cpp
#include <bits/stdc++.h> 
using namespace std;
int actualAnswer(int index, vector<int> &heights, vector<int> &dp)
{
    if(index == 0)
        return 0;
    if(dp[index] != -1)
        return dp[index];
    int right = INT_MAX;
    int left = actualAnswer(index - 1 , heights, dp) + abs(heights[index] - heights[index - 1]);
    if(index > 1)
        right = actualAnswer(index - 2, heights, dp) + abs(heights[index] - heights[index - 2]);
    dp[index] = min(left, right);
    return dp[index];
}


int frogJump(int n, vector<int> &heights)
{
    vector<int> dp(heights.size()+1, -1);
    int ans = actualAnswer(heights.size() - 1 , heights, dp);
    return ans;
}
```


### DP with Tabulation
```cpp
#include <bits/stdc++.h> 
using namespace std;
int actualAnswer(int n, vector<int> &heights, vector<int> &dp)
{
    dp[n-1] = 0;
    for(auto i = n-2; i >= 0; i--)
    {
        int fs = dp[i+1] + abs(heights[i] - heights[i + 1]);
        int ss = INT_MAX;
        if(i < n-2)
            ss = dp[i+2] + abs(heights[i] - heights[i + 2]);
        dp[i] = min(fs, ss);
    }
    return dp[0];
}
int frogJump(int n, vector<int> &heights)
{
    vector<int> dp(heights.size()+1, -1);
    int ans = actualAnswer(heights.size(), heights, dp);
    return ans;
}
```


**The *opposite* way**
```cpp
#include <bits/stdc++.h> 
using namespace std;

int actualAnswer(int n, vector<int> &heights, vector<int> &dp)
{
    dp[0] = 0;
    for(auto i = 1; i < n; i++)
    {
        int fs = dp[i-1] + abs(heights[i] - heights[i - 1]);
        int ss = INT_MAX;
        if(i > 1)
            ss = dp[i-2] + abs(heights[i] - heights[i - 2]);
        dp[i] = min(fs, ss);
    }
    return dp[n - 1];
}

int frogJump(int n, vector<int> &heights)
{
    vector<int> dp(heights.size()+1, -1);
    int ans = actualAnswer(heights.size(), heights, dp);
    return ans;
}
```


### Space optimization with tabulation
Did using "The opposite way" dp method
```cpp
#include <bits/stdc++.h>
using namespace std;

int actualAnswer(int n, vector<int> &heights)
{
	int prev2 = 0;
	int prev = 0;
	for(auto i = 1; i < n; i++)
	{
		int fs = prev + abs(heights[i] - heights[i - 1]);
		int ss = INT_MAX;
		if(i > 1)
			ss = prev2 + abs(heights[i] - heights[i - 2]);
		int current = min(fs, ss);
		prev2 = prev;
		prev = current;
	}
	return prev;
}

int frogJump(int n, vector<int> &heights)
{
    int ans = actualAnswer(heights.size(), heights);
    return ans;
}
```

<hr>
### Frog jumps to 1, 2, ,3...
There is an array of heights corresponding to `n` stones. You have to reach from stone 1 to stone `n`. From stone, it is possible to reach stones 'i'+1, ‘i’+2… ‘i’+`k` , and the cost incurred will be | Height[i]-Height[j] |, where `j` is the landing stone.

*Return* the minimum possible total cost incurred in reaching the stone `n`.

**DP** solution
```cpp
int actualAnswer(int index, int k, vector<int> &heights, vector<int> &dp)
{
    if (index == 0)
        return 0;
    
    if (dp[index] != -1)
        return dp[index];
        
    int ans = 0;
    int mini = INT_MAX;
    for (int i = index-1; i >= index - k; i--)
    {
        if (i >= 0) 
        {
          ans = actualAnswer(i, k, heights, dp) + abs(heights[index] - heights[i]);
          mini = min(ans, mini);
        }
    }
    return dp[index] = mini;
}

int minimizeCost(int n, int k, vector<int> &heights){
    vector<int> dp(n+1, -1);
    return actualAnswer(n-1, k, heights, dp);
}
```