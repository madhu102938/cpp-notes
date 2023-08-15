## Lower bound
lower bound of `x` means, smallest index in an array which satisfies the condition `arr[ind] >= x`
```python
def lower_bound(nums : [int], target : int) -> int:
    low = 0
    ans = len(nums)
    high = ans - 1
    while high >= low:
        mid = (high + low) >> 1
        if nums[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans
```

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    vector<int> arr = {1,1,2,2,3,3};
    int ans = lower_bound(arr.begin(), arr.end(), 2) - arr.begin();
    cout << ans;
    return 0;
}
```

<hr>

## Higher bound
lower bound of `x` means, smallest index in an array which satisfies the condition `arr[ind] > x`

```python
def upper_bound(nums : [int], target : int) -> int:
    low = 0
    ans = len(nums)
    high = ans - 1
    while high >= low:
        mid = (high + low) >> 1
        if nums[mid] > target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans
```

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    vector<int> arr = {1,1,2,2,3,3};
    int ans = upper_bound(arr.begin(), arr.end(), 2) - arr.begin();
    cout << ans;
    return 0;
}
```

<hr>

**Q) Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with `O(log n)` runtime complexity.**
This is just a lower bound in disguise

<hr>

**Q) You're given an unsorted array a of n integers and an integer x 
Find the floor and ceiling of `X` in `A[0..N-1]`
Floor of 'X' is the largest element in the array which is smaller than or equal to 'X'.
Ceiling of 'X' is the smallest element in the array greater than or equal to `X`.**
- Ceiling in nothing but the lower bound
- Floor is nothing but the largest index in an array such that this condition is satisfied                     `arr[ind]<=target`
```cpp
pair<int, int> getFloorAndCeil(int nums[], int n, int x) {
	sort(nums, nums+n);
	int lower = lower_bound(nums, nums+n, x) - nums;
	lower = (lower == n) ? -1 :nums[lower];
	int low = 0;
    int ans = -1;
    int high = n - 1;
    while (high >= low)
	{
        int mid = (high + low) >> 1;
        if (nums[mid] <= x) {
          ans = nums[mid];
          low = mid + 1;
        } else
          high = mid - 1;
    }
    pair<int, int> final_ans = {ans, lower}; 
    return final_ans;
}

```

<hr>

**Q) Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.
If `target` is not found in the array, return `[-1, -1]`.
You must write an algorithm with `O(log n)` runtime complexity.**
- First occurrence can be lower bound
- Last occurrence can be upper bound - 1, we just need to cover some edge cases

```cpp
vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> res = {-1, -1};
        res[0] = lower_bound(nums.begin(), nums.end(), target) - nums.begin();
        int n = nums.size();
        if (res[0] == n)
        {
            res[0] = -1;
            res[1] = -1;
            return res;
        }
        else
        {
            if (nums[res[0]] != target)
            {
                res[0] = -1;
                res[1] = -1;
                return res;
            }
        }
        res[1] = upper_bound(nums.begin(), nums.end(), target) - nums.begin() - 1;
        return res;
    }
```

