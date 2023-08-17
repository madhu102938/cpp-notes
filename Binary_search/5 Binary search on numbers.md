**1Q)** Given a non-negative integer `x`, return _the square root of_ `x` _rounded down to the nearest integer_. The returned integer should be **non-negative** as well.

You **must not use** any built-in exponent function or operator.

- For example, do not use `pow(x, 0.5)` in c++ or `x ** 0.5` in python.

```python
def mySqrt(x: int) -> int:
    if x == 0:
        return 0
    
    # Initialize the search range
    high = x
    low = 1
    ans = 1
    
    # Perform binary search to find the square root
    while low <= high:
        mid = (high + low) >> 1  # Calculate the midpoint
        
        if mid * mid <= x:
            ans = mid  # Update the potential answer
            low = mid + 1  # Search in the upper half
        else:
            high = mid - 1  # Search in the lower half
    
    return ans  # Return the calculated square root

```

<hr>

**2Q)** You are given 2 numbers **(n , m)**; the task is to find **n√m** (nth root of m). If answer is not an integer return -1

```python
class Solution:
    # This helper function checks if check^power is equal to, greater than, or less than final.
    def helper(self, check: int, power: int, final: int) -> int:
        ans = 1
        for i in range(1, power + 1):
            ans *= check
            if ans > final:
                return 2  # Result is greater than final
        if ans == final:
            return 0  # Result is equal to final
        elif ans > final:
            return 2  # Result is greater than final
        else:
            return 1  # Result is less than final
    
    def NthRoot(self, n, m):
        high = m
        low = 1
        while low <= high:
            mid = (high + low) >> 1
            temp_ans = self.helper(mid, n, m)  # Calling helper function
            if temp_ans == 0:
                return mid  # Found the Nth root
            elif temp_ans == 2:
                high = mid - 1  # Nth root is lower, search in the lower half
            else:
                low = mid + 1  # Nth root is higher, search in the upper half
        return -1  # No exact Nth root found within the given range

```

<hr>

**3Q)** Koko loves to eat bananas. There are `n` piles of bananas, the `ith` pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return _the minimum integer_ `k` _such that she can eat all the bananas within_ `h` _hours_.

```python
import math

class Solution:
    # Helper function: Calculates the total hours required to eat all bananas at a given eating speed.
    def helper(self, allBananas: [int], trynumber: int, maxlimit: int):
        ans = 0
        
        # Calculate the total hours required to eat all bananas at the given eating speed.
        for i in allBananas:
            ans += math.ceil(i / trynumber)
            
            # Check if the total hours exceed the maximum limit.
            if ans > maxlimit:
                return 2  # Result exceeds the limit
        
        if ans <= maxlimit:
            return 0  # Result is within the limit
        else:
            return 2  # Result exceeds the limit

    # Main function: Finds the minimum eating speed required to eat all bananas within the given hours.
    def minEatingSpeed(self, piles: [int], h: int) -> int:
        # Finding max element in the list, as the minimum number of 
        # bananas will be less than or equal to  max number
        for i in piles:  
			high = max(high, i)
        low = 1  # Initialize the lower limit of the binary search
        ans = int(2e9)  # Initialize the answer
        
        # Perform binary search to find the minimum eating speed
        while low <= high:
            mid = (high + low) >> 1  # Calculate the midpoint
            temp_ans = self.helper(piles, mid, h)  # Call the helper function
            
            if temp_ans == 0:
                ans = min(ans, mid)  # Update the answer with the minimum eating speed
                high = mid - 1  # Search in the lower half
            elif temp_ans == 2:
                low = mid + 1  # Search in the upper half
        
        return ans  # Return the minimum eating speed
```

|time | low | high |
|------|------|------|
|Start | Impossible value | Possible value|
|End | Possible value | Impossible value|

We can also return `low` which will be correct answer

<hr>

**4Q)** You are given an integer array `bloomDay`, an integer `m` and an integer `k`.

You want to make `m` bouquets. To make a bouquet, you need to use `k` **adjacent flowers** from the garden.

The garden consists of `n` flowers, the `ith` flower will bloom in the `bloomDay[i]` and then can be used in **exactly one** bouquet.

Return _the minimum number of days you need to wait to be able to make_ `m` _bouquets from the garden_. If it is impossible to make m bouquets return `-1`.

```python
class Solution:
    def isItPossible(self, my_list: [int], tryAnswer: int, totalNumber: int, groups: int) -> int:
        presentAnswer = 0
        cnt = 0
        for i in my_list:
            if tryAnswer >= i:
                cnt += 1
            else:
                presentAnswer += int(cnt // groups)  # Increment presentAnswer by the count of groups that can be formed using cnt
                cnt = 0  # Reset cnt since the current flower can't be included in the current group
        presentAnswer += int(cnt // groups)  # Increment presentAnswer by the remaining count of groups that can be formed using cnt
        return presentAnswer

    def minDays(self, bloomDay: [int], m: int, k: int) -> int:
        low = bloomDay[0]
        high = bloomDay[0]
        for i in bloomDay:
            low = min(i, low)  # Update the lowest bloom day encountered so far
            high = max(i, high)  # Update the highest bloom day encountered so far
        ans = 1e9 + 1  # Initialize ans to a large value
        
        # Binary search to find the minimum number of days needed for m bouquets with k flowers each
        while low <= high:
            mid = (high + low) >> 1  # Calculate the midpoint
            temp_ans = self.isItPossible(bloomDay, mid, m, k)  # Check if it's possible to create m bouquets with k flowers each using mid days
            
            if temp_ans >= m:  # If it's possible to create at least m bouquets
                ans = min(ans, mid)  # Update ans with the minimum of the current ans and mid
                high = mid - 1  # Move the upper bound of the search to mid - 1
            else:
                low = mid + 1  # Move the lower bound of the search to mid + 1 since we need more days to form m bouquets
            
        if ans == 1e9 + 1:  # If ans wasn't updated, meaning it's not possible to create m bouquets
            return -1
        else:
            return ans  # Return the minimum number of days required

```

|time | low | high |
|------|------|------|
|Start | Impossible value | Possible value|
|End | Possible value | Impossible value|

We can return low in this question, but in impossible case (where we don't have an answer) low will exceed the maximum element in the array so we need to account for that case
```python
if low > maxi:
	return -1
return low
```

<hr>

**5Q)** Given an array of integers `nums` and an integer `threshold`, we will choose a positive integer `divisor`, divide all the array by it, and sum the division's result. Find the **smallest** `divisor` such that the result mentioned above is less than or equal to `threshold`.

Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example: `7/3 = 3` and `10/2 = 5`).

The test cases are generated so that there will be an answer.

```python
# Importing all functions and variables from the math module
from math import *

# Helper function to calculate the sum of ceil(i / tryNumber) for each i in nums
def helper_fun(nums : [int], tryNumber : int):
    maybe_ans = 0
    for i in nums:
        maybe_ans += ceil(i / tryNumber)  # Incrementing maybe_ans with the ceiling division of i by tryNumber
    return maybe_ans

# Function to find the smallest divisor that makes the sum of ceil(i / divisor) for each i in nums <= threshold
def smallestDivisor(nums: [int], threshold: int) -> int:
    high = nums[0]  # Initialize the upper bound of the binary search range as the first element of nums
    low = 1  # Initialize the lower bound of the binary search range as 1
    for i in nums:
        high = max(high, i)  # Update high with the maximum value between high and i (used for binary search range)
    while low <= high:
        mid = (high + low) >> 1  # Calculate the middle point of the binary search range
        temp_ans = helper_fun(nums, mid)  # Calculate the sum using helper_fun with mid as tryNumber
        if temp_ans <= threshold:
            ans = mid  # Update ans with mid if temp_ans is within the threshold
            high = mid - 1  # Update the upper bound of the binary search range
        else:
            low = mid + 1  # Update the lower bound of the binary search range
    return low  # Return the lower bound when the binary search is complete

# End of code
```

|time | low | high |
|------|------|------|
|Start | Impossible value | Possible value|
|End | Possible value | Impossible value|

Thus we can return low

<hr>

**6Q)** A conveyor belt has packages that must be shipped from one port to another within `days` days.

The `ith` package on the conveyor belt has a weight of `weights[i]`. Each day, we load the ship with packages on the conveyor belt (in the order given by `weights`). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within `days` days.

```python
class Solution:
    # Helper function to determine how many days are needed to ship all items using a given capacity
    def helper_fun(self, nums: [int], tryNumber: int, n: int):
        maybe_ans = 0       # Initialize the count of required days
        cum_weight = 0      # Initialize the cumulative weight for the current day's shipment
        
        # Loop through each item in the list
        for i in range(n):
            if cum_weight + nums[i] > tryNumber:
                maybe_ans += 1              # Increment days count, as the cumulative weight exceeds the given capacity
                cum_weight = nums[i]        # Reset cumulative weight for the next day's shipment
            else:
                cum_weight += nums[i]       # Add the item's weight to the cumulative weight
        
        return maybe_ans + 1   # Return the total days required for shipment (adding 1 to account for the last day)

    # Function to find the minimum capacity needed to ship items within a given threshold of days
    def shipWithinDays(self, nums: [int], threshold: int) -> int:
        high = 0           # Initialize the upper bound of binary search as 0 (maximum capacity)
        low = nums[0]      # Initialize the lower bound of binary search as the weight of the first item
        n = 0              # Initialize the count of items
        
        # Calculate the maximum and minimum capacity bounds, and count the total number of items
        for i in nums:
            low = max(low, i)    # Update the minimum capacity with the maximum weight of an item
            high += i            # Calculate the total sum of weights (maximum capacity)
            n += 1               # Increment the item count
        
        # Perform binary search to find the minimum capacity that satisfies the threshold
        while low <= high:
            mid = (high + low) >> 1   # Calculate the middle point of the capacity range
            temp_ans = self.helper_fun(nums, mid, n)   # Calculate days needed using the helper function
            
            if temp_ans <= threshold:
                high = mid - 1   # Adjust the upper bound for capacity search
            else:
                low = mid + 1    # Adjust the lower bound for capacity search
        
        return low   # Return the minimum capacity needed to ship items within the given threshold of days

# End of code
```

|time | low | high |
|------|------|------|
|Start | Impossible value | Possible value|
|End | Possible value | Impossible value|

We can just return low here.


<hr>

**7Q)** Given an array `arr` of positive integers sorted in a **strictly increasing order**, and an integer `k`.

Return _the_ `kth` _**positive** integer that is **missing** from this array._

### Brute force
```python
def bruteForceKthMissing(nums: [int], k: int) -> int:
    for i in nums:
        if i < k:
            k += 1    # Increment k because we've found a number in the array that is less than k
        else:
            return k  # Return k when we've found a number in the array greater than or equal to k

# End of code
```

### Optimal solution
- We take `high` set to end of array and `low` set to start of array
- At any element number of numbers missing are `arr[i] - (i + 1)` as ideally we should have `i+1` at `i`th index
- We do this using high and low
```python
while low <= high:
	mid = (high + low) >> 1
	cur_miss_num = arr[mid] - mid - 1
	if cur_miss_num < k:
		low = mid + 1
	else:
		high = mid - 1
```
- We are making the high pointer point to just before the kth element which is present in the array
- As now we have high pointer, we can the answer by, `arr[high] + some_extra`
- `some_extra = k - {arr[high] - (high+1)}` this is basically `k - elements missing at high index`
- So finally get answer = (~~arr[high]~~ + k - ~~arr[high]~~ + high + 1)
- ans is `k + high + 1`
- When the loop ends `low` will one greater than `high` so `low` will be `high + 1`
- ans is `k + low`

```python
def findKthPositive(arr: [int], k: int) -> int:
	high = len(arr) - 1
	low = 0
	while low <= high:
		mid = (high + low) >> 1
		cur_miss_num = arr[mid] - mid - 1
		if cur_miss_num < k:
			low = mid + 1
		else:
			high = mid - 1
	return low + k
```