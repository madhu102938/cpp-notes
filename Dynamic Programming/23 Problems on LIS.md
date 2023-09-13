### Longest Divisible Subset
Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

    answer[i] % answer[j] == 0, or
    answer[j] % answer[i] == 0

If there are multiple solutions, return any of them.


- Code is same as kinda efficient code of LIS, but instead of
	- `arr[j] > arr[i]` we use `arr[j] % arr[i] == 0`
	- We also sort the array at the beginning
```cpp
vector<int> largestDivisibleSubset(vector<int> arr)
{
	int n = arr.size();
	vector<int> dp(n, 1);
	vector<int> hash(n);
	int ans = 0, start_index;
	sort(arr.begin(), arr.end());

	for (int i = 0; i < n; i++)
		hash[i] = i;

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < i; j++)
		{
			if ((arr[i] % arr[j] == 0) && 1 + dp[j] > dp[i])
			{
				dp[i] = dp[j] + 1;
				hash[i] = j;
				if (ans < dp[i])
				{
					ans = dp[i];
					start_index = i;
				}
			}
		}
	}

	if (ans == 0)
		return {arr[0]};

	vector<int> lds(ans);
	ans--;

	while (start_index != hash[start_index])
	{
		lds[ans--] = arr[start_index];
		start_index = hash[start_index];
	}
	lds[ans] = arr[start_index];

	return lds;
}
```

<hr>

### Longest String Chain
You are given an array of `words` where each word consists of lowercase English letters.

`wordA` is a **predecessor** of `wordB` if and only if we can insert **exactly one** letter anywhere in `wordA` **without changing the order of the other characters** to make it equal to `wordB`.

- For example, `"abc"` is a **predecessor** of `"abac"`, while `"cba"` is not a **predecessor** of `"bcad"`.

A **word chain** is a sequence of words `[word1, word2, ..., wordk]` with `k >= 1`, where `word1` is a **predecessor** of `word2`, `word2` is a **predecessor** of `word3`, and so on. A single word is trivially a **word chain** with `k == 1`.

Return _the **length** of the **longest possible word chain** with words chosen from the given list of_ `words`.


```python
def helper(small : str, big : str) -> bool:
    n1 = len(small)
    n2 = len(big)

    # Check if the lengths differ by 1
    if n1 + 1 == n2:
        small_index = 0
        big_index = 0

        # Compare characters of small and big strings
        while small_index < n1 and big_index < n2:
            if small[small_index] == big[big_index]:
                small_index += 1
                big_index += 1
            else:
                big_index += 1

        # If we reached the end of both strings, small is predecessor of big
        if small_index == n1 and big_index == n2:
            return True
        # Edge case : if the extra character were at the end of big string
        elif small_index == big_index:
            return True
        else:
            return False
    else:
        return False


def longestStrChain(words: [str]) -> int:
    n = len(words)
    
    # Sort the words by their length
    words.sort(key=len)
    
	# Initialize an array to store the length of the longest word chain ending at each word
    dp = [1] * n
    
    # Initialize a variable to store the maximum length of word chain found so far
    ans = 1
    
    for i in range(n):
        for j in range(i):
            # Check if words[j] is a predecessor of words[i] and if extending the chain is beneficial
            if helper(words[j], words[i]) and 1 + dp[j] > dp[i]:
                dp[i] = 1 + dp[j]
                ans = max(ans, dp[i])
    
    return ans
```

<hr>

### Longest Bitonic Subsequence
Let us first understand what a bitonic subsequence means.

A bitonic subsequence is a subsequence of an array in which the elements can be any of these three:

- First, increase till a point and then decrease.
- Goes on increasing (Longest increasing subsequence)
- Goes on decreasing (Longest decreasing subsequence)

```cpp
int lengthOfLIS(vector<int> &arr, vector<int> &dp)
{
	int n = arr.size();
	int ans = 0;

	for (int i = 0; i < n; i++)
	{
		for (int prev_index = 0; prev_index < i; prev_index++)
		{
			if (arr[prev_index] < arr[i])
				dp[i] = max(dp[i], 1 + dp[prev_index]);
		}
		ans = max(ans, dp[i]);
	}
	return ans;
}


int longestBitonicSubsequence(vector<int> &arr, int n) 
{
    // Create two arrays 'lis' and 'lds' to store the length of the Longest Increasing Subsequence (LIS)
    // and the Longest Decreasing Subsequence (LDS) respectively.
    vector<int> lis(n, 1); // Initialize all LIS values to 1
    vector<int> lds(n, 1); // Initialize all LDS values to 1
    
    // Calculate the LIS for the original array 'arr'
    lengthOfLIS(arr, lis);
    
    // Reverse the 'arr' to calculate the LDS
    reverse(arr.begin(), arr.end());
    lengthOfLIS(arr, lds); // Calculate the LDS
    
    // Reverse the 'lds' array back to its original order
    reverse(lds.begin(), lds.end());
    
    int ans = 0; // Initialize a variable 'ans' to store the length of the longest bitonic subsequence
    
    // Iterate through the elements of the original array
    for (int i = 0; i < n; i++) 
    {
        // Calculate the length of the bitonic subsequence that ends at 'arr[i]'
        // by summing the length of the LIS ending at 'arr[i]' and the LDS starting at 'arr[i]'
        // and subtracting 1 (to avoid double-counting the 'arr[i]' element)
        ans = max(ans, lis[i] + lds[i] - 1);
    }
    
    // Return the length of the longest bitonic subsequence
    return ans;
}
```

<hr>

### Number of LIS
Given an integer array `nums`, return _the number of longest increasing subsequences._

**Notice** that the sequence has to be **strictly** increasing.

```cpp
int findNumberOfLIS(vector<int>& arr) {
    int n = arr.size();
    int maxi = 0; // Initialize a variable 'maxi' to store the maximum length of LIS
    vector<int> dp(n, 1);
    vector<int> con(n, 1); // Create an array 'con' to store counts of LIS ending at each element
    
    // Iterate through the elements of the input array 'arr'
    for (int i = 0; i < n; i++) {
        for (int prev_index = 0; prev_index < i; prev_index++) {
            if (arr[prev_index] < arr[i] && dp[i] < 1 + dp[prev_index]) {
                // Update the length of LIS ending at 'arr[i]' and the count 'con[i]'
                dp[i] = 1 + dp[prev_index];
                con[i] = con[prev_index];
            }
            // If there are multiple LIS of the same length, add to the count 'con[i]'
            else if (arr[prev_index] < arr[i] && dp[i] == 1 + dp[prev_index]) {
                con[i] += con[prev_index];
            }
        }
        if (maxi < dp[i]) {
            maxi = dp[i];
        }
    }
    
    // If the maximum LIS length is 1, return the total number of elements in 'arr'
    if (maxi == 1)
        return n;
    
    int cnt = 0; // Initialize a variable 'cnt' to store the count of LIS with length 'maxi'
    
    // Iterate through the elements of 'arr' to count LIS with length 'maxi'
    for (int i = 0; i < n; i++) {
        if (dp[i] == maxi)
            cnt += con[i];
    }
    
    return cnt; // Return the count of LIS with length 'maxi'
}

```