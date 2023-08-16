**Q)** Given a non-negative integer `x`, return _the square root of_ `x` _rounded down to the nearest integer_. The returned integer should be **non-negative** as well.

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

**Q)** You are given 2 numbers **(n , m)**; the task is to find **n√m** (nth root of m). If answer is not an integer return -1

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

**Q)** Koko loves to eat bananas. There are `n` piles of bananas, the `ith` pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

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

<hr>

**Q)** You are given an integer array `bloomDay`, an integer `m` and an integer `k`.

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