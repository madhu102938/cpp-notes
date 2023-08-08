Given two strings `text1` and `text2`, return _the length of their longest **common subsequence**._ If there is no **common subsequence**, return `0`.
A **subsequence** of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
- For example, `"ace"` is a subsequence of `"abcde"`.
A **common subsequence** of two strings is a subsequence that is common to both strings.


**DP** solution
```cpp
class Solution
{
private:
  int actualAnswer(int index1, int index2, string text1, string text2, vector<vector<int>> &dp)
  {
    if (index1 < 0 || index2 < 0)
      return 0;
    if (dp[index1][index2] != -1)
      return dp[index1][index2];
    if (text1[index1] == text2[index2])
      return dp[index1][index2] = actualAnswer(index1-1, index2-1, text1, text2, dp) + 1;
    else
    {
      return dp[index1][index2] = max(actualAnswer(index1-1, index2, text1, text2, dp), actualAnswer(index1, index2-1, text1, text2, dp));
    }
  }

public:
  int longestCommonSubsequence(string text1, string text2)
  {
    int s1len = text1.size(), s2len = text2.size();
    vector<vector<int>> dp(s1len, vector<int>(s2len, -1));
    return actualAnswer(s1len - 1, s2len - 1, text1, text2, dp);
  }
}
```
***Time Complexity** : O($N*M$) : There are N*M states therefore at max ‘N*M’ new problems will be solved.
**Space Complexity** : O($N*M$) + O($N+M$) : We are using an auxiliary recursion stack space(O($N+M$)) (see the recursive tree, in the worst case, we will go till N+M calls at a time) and a 2D array ( O($N*M$)).*
**N = s1len
M = s2len**



*In the recursive logic, we set the base case to if(ind1<0 || ind2<0) but we can’t set the dp array’s index to -1. Therefore a hack for this issue is to shift every index by 1 towards the right.*
**Tabulation** solution
```cpp
public:
  int longestCommonSubsequence(string text1, string text2)
  {
    int s1len = text1.size(), s2len = text2.size();
    vector<vector<int>> dp(s1len + 1, vector<int>(s2len + 1, -1));
    for (int i = 0; i <= s1len; i++)
      dp[i][0] = 0;
    for (int i = 0; i <= s2len; i++)
      dp[0][i] = 0;
    for (int index1 = 1; index1 <= s1len; index1++)
    {
      for (int index2 = 1; index2 <= s2len; index2++)
      {
        if (text1[index1 - 1] == text2[index2 - 1])
          dp[index1][index2] = dp[index1-1][index2-1] + 1;
        else
          dp[index1][index2] = max(dp[index1-1][index2], dp[index1][index2-1]);
      }
    }
    return dp[s1len][s2len];
  }
};
```
***Time Complexity**: O($s1len*s2len$) : There are two nested loops*
***Space Complexity**: O($s1len*s2len$) : We are using an external array of size ‘$s1len*s2len$)’. Stack Space is eliminated.*



**Space Optimization** with tabulation
```cpp
int lcs(string s1, string s2) {
    
    int n=s1.size();
    int m=s2.size();

    vector<int> prev(m+1,0), cur(m+1,0);
    
    // Base Case is covered as we have initialized the prev and cur to 0.
    
    for(int ind1=1;ind1<=n;ind1++){
        for(int ind2=1;ind2<=m;ind2++){
            if(s1[ind1-1]==s2[ind2-1])
                cur[ind2] = 1 + prev[ind2-1];
            else
                cur[ind2] = 0 + max(prev[ind2],cur[ind2-1]);
        }
        prev= cur;
    }
    return prev[m];
}
```