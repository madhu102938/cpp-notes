Given an integer array `nums`, return _the length of the longest **strictly increasing subsequence**_.

**DP** with **Recurrence**
```cpp

int getAns(int arr[], int n,  int ind, int prev_index, vector<vector<int>>& dp)
{    
    // base condition
    if(ind == n)
        return 0;
        
    if(dp[ind][prev_index+1]!=-1)
        return dp[ind][prev_index+1];
    
    int notTake = 0 + getAns(arr,n,ind+1,prev_index,dp);
    
    int take = 0;
    if(prev_index == -1 || arr[ind] > arr[prev_index])
        take = 1 + getAns(arr,n,ind+1,ind,dp);
    
    return dp[ind][prev_index+1] = max(notTake,take);
}


int longestIncreasingSubsequence(int arr[], int n)
{    
    vector<vector<int>> dp(n,vector<int>(n+1,-1));
    return getAns(arr,n,0,-1,dp);
}
```
***Time Complexity**: O($N*N$) : There are $N*N$ states therefore at max ‘$N*N$’ new problems will be solved.
**Space Complexity**: O($N*N$) + O(N) : We are using an auxiliary recursion stack space(O(N)) (see the recursive tree, in the worst case we will go till N calls at a time) and a 2D array ( O($N*(N+1)$)).*




**Tabulation**
```cpp
int longestIncreasingSubsequence(int arr[], int n){
    
    vector<vector<int>> dp(n+1,vector<int>(n+1,0));
    
    for(int ind = n-1; ind>=0; ind --){
        for (int prev_index = ind-1; prev_index >=-1; prev_index --)
        {    
            int notTake = 0 + dp[ind+1][prev_index +1];
    
            int take = 0;
		    if(prev_index == -1 || arr[ind] > arr[prev_index])    
                take = 1 + dp[ind+1][ind+1];
    
            dp[ind][prev_index+1] = max(notTake,take);
        }
    }
    
    return dp[0][-1 + 1];
}
```
***Time Complexity**: O($N*N$) : There are two nested loops
**Space Complexity**: O($N*N$) : We are using an external array of size ‘$(N+1)*(N+1)$’. Stack Space is eliminated.*




**Space optimization** with tabulation
```cpp
int longestIncreasingSubsequence(int arr[], int n)
{    
    vector<int> next(n+1,0);
    vector<int> cur(n+1,0);
    
    for(int ind = n-1; ind>=0; ind--){
        for (int prev_index = ind-1; prev_index >=-1; prev_index --)
        { 
            int notTake = 0 + next[prev_index +1];
    
            int take = 0;
            if(prev_index == -1 || arr[ind] > arr[prev_index])
                take = 1 + next[ind+1];
			cur[prev_index+1] = max(notTake,take);
        }
        next = cur;
    }
    return cur[0];
}
```
***Time Complexity**: O($N^2$) : There are two nested loops.
**Space Complexity**: O(N) : We are only using two rows of size n.*




Most **Efficient** solution
```cpp
class Solution {
public:
    // Function to find the length of the Longest Increasing Subsequence (LIS)
    int lengthOfLIS(vector<int>& arr) {
        int n = arr.size(); // Get the size of the input array
        vector<int> dp(n, 1); // Create a dynamic programming (DP) array to store LIS lengths ending at each index, initialized with 1s
        int ans = 0; // Initialize a variable to store the final result (maximum LIS length)
    
        // Iterate through each element in the input array
        for (int i = 0; i <= n - 1; i++) {
            // For each element, iterate through all previous elements to find potential increasing subsequences
            for (int prev_index = 0; prev_index < i; prev_index++) {    
                // Check if the current element can be added to the increasing subsequence ending at the previous index
                if (arr[prev_index] < arr[i])
                    dp[i] = max(dp[i], 1 + dp[prev_index]); // Update the LIS length ending at the current index if a longer subsequence is found
            }
            ans = max(ans, dp[i]); // Update the overall maximum LIS length
        }
        return ans; // Return the maximum LIS length
    }
};
```
***Time Complexity**: O($N*N$) : There are two nested loops.
**Space Complexity**: O(N) : We are only using two rows of size ‘N’.*