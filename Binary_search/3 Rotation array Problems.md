**Q)** There is an integer array `nums` sorted in ascending order (with **distinct** values).
Prior to being passed to your function, `nums` is **possibly rotated** at an unknown pivot index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index `3` and become `[4,5,6,7,0,1,2]`.

Given the array `nums` **after** the possible rotation and an integer `target`, return _the index of_ `target` _if it is in_ `nums`_, or_ `-1` _if it is not in_ `nums`.

You must write an algorithm with `O(log n)` runtime complexity.

```python
def search(self, nums: List[int], target: int) -> int:
    # Initialize low and high pointers for binary search
    low = 0
    high = len(nums) - 1
    
    # Perform binary search while the search interval is valid
    while high >= low:
        # Calculate the middle index using bitwise right shift (equivalent to dividing by 2)
        mid = (high + low) >> 1
        
        # Check if the middle element is the target
        if nums[mid] == target:
            return mid
        # Check if the left part of the array is sorted
        elif nums[mid] >= nums[low]:
            # Check if the target is within the sorted left part
            if nums[low] <= target <= nums[mid]:
                # Adjust the high pointer to search the left part
                high = mid - 1
            else:
                # Adjust the low pointer to search the right part
                low = mid + 1
        else:
            # Check if the target is within the sorted right part
            if nums[mid] <= target <= nums[high]:
                # Adjust the low pointer to search the right part
                low = mid + 1
            else:
                # Adjust the high pointer to search the left part
                high = mid - 1
                
    # Target element not found in the array
    return -1

```

<hr>

**Q)** There is an integer array `nums` sorted in non-decreasing order (not necessarily with **distinct** values).

Before being passed to your function, `nums` is **rotated** at an unknown pivot index `k` (`0 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,4,4,5,6,6,7]` might be rotated at pivot index `5` and become `[4,5,6,6,7,0,1,2,4,4]`.

Given the array `nums` **after** the rotation and an integer `target`, return `true` _if_ `target` _is in_ `nums`_, or_ `false` _if it is not in_ `nums`_._

You must decrease the overall operation steps as much as possible.

```python
def search(self, nums: List[int], target: int) -> int:
    low = 0                    # Initialize the lower bound of the search range
    high = len(nums) - 1       # Initialize the upper bound of the search range
    
    while high >= low:         # Continue the search as long as the search range is valid
        mid = (high + low) >> 1    # Calculate the middle index using bitwise right shift
        
        if nums[mid] == target:    # If the middle element is the target, return True
            return True
        
        # Check if the first, middle, and last elements are the same
        elif nums[low] == nums[mid] == nums[high]:
            low = low + 1           # Adjust the lower bound to exclude duplicates
            high = high - 1         # Adjust the upper bound to exclude duplicates
            continue
        
        # Check if the left part of the array is sorted
        elif nums[mid] >= nums[low]:
            # Check if the target is within the sorted left part
            if nums[low] <= target <= nums[mid]:
                high = mid - 1       # Adjust the upper bound to search the left part
            else:
                low = mid + 1        # Adjust the lower bound to search the right part
        else:
            # Check if the target is within the sorted right part
            if nums[mid] <= target <= nums[high]:
                low = mid + 1        # Adjust the lower bound to search the right part
            else:
                high = mid - 1       # Adjust the upper bound to search the left part
    
    return False    # Return False if the target element is not found in the array
```

<hr>

**Q)** Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:

- `[4,5,6,7,0,1,2]` if it was rotated `4` times.
- `[0,1,2,4,5,6,7]` if it was rotated `7` times.

Notice that **rotating** an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array `nums` of **unique** elements, return _the minimum element of this array_.

You must write an algorithm that runs in `O(log n) time.`


*If right is sorted, take the minimum of that and eliminate it or else do that with left*
```python
class Solution:
    def findMin(self, nums: [int]) -> int:
        high = len(nums) - 1
        low = 0
        min_element = 2e9  # Initialize the minimum element with a large value

        while low <= high:
            mid = (high + low) >> 1  # Calculate the middle index using bitwise right shift

            if nums[mid] <= nums[high]:  # checking if right side is sorted
                min_element = min(nums[mid], min_element)  # Update the minimum element if needed
                high = mid - 1  # eliminate right
            else: # if right is not sorted, then left must be sorted
                min_element = min(nums[low], min_element)  # Update the minimum element if needed
                low = mid + 1  # eliminate left

        return min_element  # Return the minimum element found

```

