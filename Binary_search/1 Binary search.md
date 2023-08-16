## Binary Search Iterative
```python
def search(nums : [int], target : int) -> int:  
    high = len(nums) - 1
    low = 0  
    while high >= low:  
        mid = (high + low) >> 1
        if nums[mid] == target:  
            return mid  
        elif nums[mid] > target:  
            high = mid - 1  
        else:  
            low = mid + 1  
    return -1
```

<hr>

## Recursive binary search

```python
def search(nums : [int], target : int, high, low = 0) -> int:
    if low > high: # Base case
        return - 1 # Not found
    mid = (high + low) >> 1 # Bitwise division by 2
    if nums[mid] == target: # Base case
        return mid # Found
    elif nums[mid] > target: # Recursive case
        return search(nums, target, mid-1) # Search left
    else: # Recursive case
        return search(nums, target, high, mid+1) # Search right
```
