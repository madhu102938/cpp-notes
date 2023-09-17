A palindromic string is a string that is equal to its reverse. For example: “nitin” is a palindromic string. Now the question states to find the length of the longest palindromic subsequence of a string. It is that palindromic subsequence of the given string with the greatest length.

```cpp
int lcs(string &str1, string &str2)
{
    int s1len = str1.size(), s2len = str2.size();
    vector<vector<int>> dp(s1len + 1, vector<int>(s2len + 1, 0));

    for (int index1 = 1; index1 <= s1len; index1++)
    {
      for (int index2 = 1; index2 <= s2len; index2++)
      {
        if (str1[index1 - 1] == str2[index2 - 1])
          dp[index1][index2] = dp[index1-1][index2-1] + 1;
        else
          dp[index1][index2] = 0; // + max(dp[index1-1][index2], dp[index1][index2-1]);
      }
    }

    int max_number = dp[0][0];

  // Iterate through the 2D vector and find the largest number.
    for (int i = 1; i <= s1len; i++) 
    {
        for (int j = 1; j <= s2len; j++) 
        {
            if (dp[i][j] > max_number) 
            {
                max_number = dp[i][j];
            }
        }
    }
    return max_number;
}
```