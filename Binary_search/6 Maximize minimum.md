### Aggressive Cows
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

### Allocate books / Painter Partitions / Split Array
**2Q)** Given an array `arr` of integer numbers, `ar[i]` represents the number of pages in the `i-th` book. There are a ‘m’ number of students, and the task is to allocate all the books to the students.  
Allocate books in such a way that:

1. Each student gets at least one book.
2. Each book should be allocated to only one student.
3. Book allocation should be in a contiguous manner.

You have to allocate the book to ‘m’ students such that the maximum number of pages assigned to a student is minimum. If the allocation of books is not possible. return -1

**Book allocation / Painters Partitions / Split Array**

```python
class Solution:
    def helper_fun(self, nums: [int], tryNumber: int):
        students_over = 1  # Initialize the count of students exceeding the tryNumber
        pages_comp = 0      # Initialize the cumulative pages read by a student

        # Iterate through each book's pages in nums
        for i in nums:
            if pages_comp + i <= tryNumber:
                pages_comp += i  # If current book can be added to current student's reading, add it
            else:
                students_over += 1  # If adding the current book exceeds the tryNumber, increment student count
                pages_comp = i       # Reset cumulative pages for a new student
        return students_over     # Return the total number of students needed

    def splitArray(self, nums: [int], k: int) -> int:
        low = max(nums)  # Initialize lower bound for binary search as the maximum pages in a book
        high = 0         # Initialize upper bound for binary search as the sum of all pages in nums
        
        # Calculate the sum of all pages in nums to set the initial upper bound
        for i in nums:
            high += i
        
        # Binary search loop
        while low <= high:
            mid = (high + low) >> 1  # Calculate the midpoint between low and high
            
            # Call the helper function to determine the number of students needed for mid pages
            temp_ans = self.helper_fun(nums, mid)
            
            if temp_ans <= k:
                high = mid - 1  # If the required students are less than or equal to k, adjust the upper bound
            else:
                low = mid + 1   # If the required students are more than k, adjust the lower bound
        
        return low  # Return the lowest possible tryNumber that satisfies the condition
```

<hr>

**3Q)** 