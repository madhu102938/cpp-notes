**1Q)** You are given an array **‘arr’** of size **‘n’** which denotes the position of stalls.  
You are also given an integer **‘k’** which denotes the number of aggressive cows.  

You are given the task of assigning stalls to **‘k’** cows such that the minimum distance between any two of them is the maximum possible.  

Find the maximum possible minimum distance.

```cpp
// Helper function to determine if it's possible to place 'cows' number of cows
// in stalls with at least 'tryNumber' distance between them
bool helper_fun(vector<int> &stalls, int tryNumber, int n, int cows)
{
    int i = 0;        // Starting position of the first cow
    int cows_used = 1;  // Count of cows placed
    int j = 1;        // Position of the next stall

    // While there are more stalls to consider and cows are not all placed
    while (j < n && i < n && cows_used != cows)
    {
        // Check if the distance between current and next stall is at least 'tryNumber'
        if (abs(stalls[j] - stalls[i]) >= tryNumber)
        {
            i = j;             // Move the starting position of the next cow
            j = j + 1;         // Move to the next stall
            cows_used++;       // Increment the count of placed cows
        }
        else
            j++;               // Move to the next stall without placing a cow
    }

    if (cows == cows_used)
        return true;          // If all cows are placed, return true
    return false;             // Otherwise, return false
}

// Function to find the maximum minimum distance between cows in stalls
int aggressiveCows(vector<int> &stalls, int k)
{
    sort(stalls.begin(), stalls.end());  // Sort the stalls in ascending order
    int n = stalls.size();                // Total number of stalls
    int high = stalls[n - 1] - stalls[0]; // Maximum possible distance
    int low = 1;                          // Minimum possible distance

    // Perform binary search to find the maximum minimum distance
    while (low <= high)
    {
        int mid = (high + low) >> 1;      // Calculate the middle distance
        bool temp_ans = helper_fun(stalls, mid, n, k);  /* Check if it's possible to place 'k' cows with minimum 'mid' distance*/

        if (temp_ans)
        {
            low = mid + 1;                 // If it's possible, search for larger distances
        }
        else
            high = mid - 1;                // If not possible, search for smaller distances
    }
    return high;                           // Return the maximum minimum distance found
}
```

Here first `low` starts possible value (as it is possible to have cows with 1 gap) and `high` starts at an impossible value (as it is possible to have maximum minimum distance as the highest for all cases) and towards to the end of iteration `low` moves to an impossible value and `high` moves to possible value, thus we return `high`
Basically polarities have been switched, 


|time | low | high |
|------|------|------|
|Start | Possible value | Impossible value|
|End | Impossible value | Possible value|


<hr>

