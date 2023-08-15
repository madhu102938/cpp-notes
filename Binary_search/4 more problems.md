**Q)** You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return _the single element that appears only once_.

Your solution must run in `O(log n)` time and `O(1)` space.

```python
def singleNonDuplicate(self, nums: [int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[n-1] != nums[n-2]:
            return nums[n-1]
        low = 1
        high = n-2
        while low <= high:
            mid = (high + low) // 2
            if nums[mid] != nums[mid+1] and nums[mid] != nums[mid-1]:
                return nums[mid]
            elif mid & 1 == 0:
                if nums[mid] == nums[mid+1]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[mid] == nums[mid-1]:
                    low = mid + 1
                else:
                    high = mid - 1
        return nums[low]
```

```ascii
 Index:    0    1    2    3    4    5    6    7    8
         +----+----+----+----+----+----+----+----+----+
 Array:  | 5  | 5  | 9  | 9  | 11 | 13 | 13 | 15 | 15 |
         +----+----+----+----+----+----+----+----+----+
         
         <-----------+                   +----------->
                     |                   |
                 Duplicate            Duplicate
                  Element             Element
                 (even odd)          (odd even)
```
- First, the length of the input array `nums` is stored in the variable `n`.
    
- If the length of the array is 1, then there is only one element in the array, and it is the non-duplicate element. Therefore, the code returns `nums[0]`.
    
- If the first element (`nums[0]`) is not equal to the second element (`nums[1]`), then the first element is the non-duplicate element. The code returns `nums[0]`.
    
- If the last element (`nums[n-1]`) is not equal to the second-to-last element (`nums[n-2]`), then the last element is the non-duplicate element. The code returns `nums[n-1]`.
    
- If the non-duplicate element is not at the beginning or end of the array, a binary search is performed between the indices `low = 1` and `high = n-2`. This is because we've already checked the first and last elements.
    
- Inside the binary search loop, the middle index `mid` is calculated as the average of `high` and `low`.
    
- The code then checks if the element at index `mid` is different from its adjacent elements (`mid+1` and `mid-1`). If it is different from both, then it is the non-duplicate element, and the code returns it.
    
- If the element at index `mid` is not a non-duplicate, the code checks if `mid` is an even index (even indices are 0-based). 
	- If `mid` is even, and `arr[mid] == arr[mid+1]` it means that the non-duplicate element is on the right side of `mid`. The code adjusts the `low` pointer to `mid + 1` to eliminate left side and search only right side.
	- If `mid` is even, and `arr[mid] == arr[mid-1]` it means that the non-duplicate element is on the left side of `mid`. The code adjusts the `high` pointer to `mid - 1` to eliminate right side and search only left side.
    
- If the index were not even, then it will be odd
	- If `mid` is odd, and `arr[mid] == arr[mid-1]` it means that the non-duplicate element is on the right side of `mid`. The code adjusts the `low` pointer to `mid + 1` to eliminate left side and search only right side.
	- If `mid` is odd, and `arr[mid] == arr[mid+1]` it means that the non-duplicate element is on the left side of `mid`. The code adjusts the `high` pointer to `mid - 1` to eliminate right side and search only left side.
    
- The binary search continues until `low` is greater than `high`, indicating that the search range has been exhausted.

<hr>

**Q)** A peak element is an element that is strictly greater than its neighbors.

Given a **0-indexed** integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to **any of the peaks**.

You may imagine that `nums[-1] = nums[n] = -∞`. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in `O(log n)` time.

```python
def findPeakElement(nums: [int]) -> int:
        n = len(nums)
        if n == 1 or nums[0] > nums[1]:
            return 0
        if nums[n-2] < nums[n-1]:
            return n-1
        high = n - 2
        low = 1
        while low <= high:
            mid = (high + low) >> 1
            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid-1] < nums[mid]: # is it increasing?
                low = mid + 1 # eliminate left
            else: # must be decreasing
                high = mid - 1 # elimiate right
        return -1
```

Basically we need to eliminate and left and right halves and get to the element we need.
In this case of peak element
- Left side of peak element is monotonously increasing
- Right side of peak element is monotonously decreasing
So we write a base case, where it checks if the element is peak element, if it is not peak element
- We check if its increasing, then we know, our peak element is towards right and we eliminate left
- or else if must be decreasing, then we know, our peak element is towards left and we eliminate right
The method described here works well for only single peak in the array, but surprising it words multiple peaks too, because in the end we only need to return 1 peak.
