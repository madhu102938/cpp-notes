We are given an array `ARR` with `N` positive integers. We need to find if there is a **subset** in `ARR` with a sum equal to `K`. If there is, return *true* else return *false*.


**Recurrence** solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int actualAnswer(int index, int target, vector<int> &arr, vector<vector<int>> &dp)
{
  if (target == 0)
    return 1;
  if (index == 0)
    return (arr[0] == target);
  int take = 0;
  if (target >= arr[index])
    take = actualAnswer(index-1, target-arr[index], arr, dp);
  int notTake = actualAnswer(index-1, target, arr, dp);
  return take || notTake;
}

bool subsetSumToK(int n, int k, vector<int> &arr)
{
  vector<vector<int>> dp(n+1, vector<int>(k+1, -1));
  return actualAnswer(n-1, k, arr, dp);
}
```
***Time Complexity** - O($2^n$) : as for every number we have two options take / notTake*
***Space Complexity** - O($N$) : stack space*



**DP** solution
```cpp
int actualAnswer(int index, int target, vector<int> &arr, vector<vector<int>> &dp)
{
  if (target == 0)
    return 1;
  if (index == 0)
    return (arr[0] == target);
  if (dp[index][target] != -1)
    return dp[index][target];
  int take = 0;
  if (target >= arr[index])
    take = actualAnswer(index-1, target-arr[index], arr, dp);
  int notTake = actualAnswer(index-1, target, arr, dp);
  dp[index][target] = take || notTake;
  return dp[index][target];
}

bool subsetSumToK(int n, int k, vector<int> &arr)
{
  vector<vector<int>> dp(n+1, vector<int>(k+1, -1));
  return actualAnswer(n-1, k, arr, dp);
}
```
***Time Complexity** - O($N * K$) : as every element in the dp in getting calculated with O(1) time*
***Space Complexity**: O($N * K$) + O($N$) : We are using a recursion stack space(O(N)) and a 2D array (O($N * K$)).*




**Tabulation** solution
```cpp
#include <bits/stdc++.h>
using namespace std;

bool subsetSumToK(int n, int k, vector<int> &arr)
{
  vector<vector<int>> dp(n + 1, vector<int>(k + 1, 0));
  for (int i = 0; i < n; i++)
    dp[i][0] = 1;
  if (arr[0] <= k)
    dp[0][arr[0]] = 1;
  for (int index = 1; index < n; index++)
  {
    for (int target = 1; target <= k; target++)
    {
      else
      {
        int take = 0, dontTake = 0;
        if (index > 0 && target - arr[index] >= 0)
          take = dp[index - 1][target - arr[index]];
        if (index > 0)
          dontTake = dp[index - 1][target];
        dp[index][target] = take || dontTake;
      }
    }
  }
  return dp[n - 1][k];
}
```
***Time Complexity**: O($N * K$) : There are two nested loops
**Space Complexity**: O($N * K$) : We are using an external array of size ‘$N * K$’. Stack Space is eliminated.*



**Space optimization** with tabulation
```cpp
#include <bits/stdc++.h>
using namespace std;

bool subsetSumToK(int n, int k, vector<int> &arr)
{
  vector<int> prev(k + 1, 0);
  prev[0] = 1;
  vector<int> curr(k + 1, 0);
  if (arr[0] <= k)
    prev[arr[0]] = 1;
  for (int index = 1; index < n; index++)
  {
    for (int target = 1; target <= k; target++)
    {
      curr[0] = 1;
      int take = 0, dontTake = 0;
      if (index > 0 && target - arr[index] >= 0)
        take = prev[target - arr[index]];
      if (index > 0)
        dontTake = prev[target];
      curr[target] = take || dontTake;
    }
    prev = curr;
  }
  return prev[k];
}
```