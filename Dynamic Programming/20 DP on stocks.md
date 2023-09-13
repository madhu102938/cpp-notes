### Best Time to Buy and Sell Stocks 1
You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return _the maximum profit you can achieve from this transaction_. If you cannot achieve any profit, return `0`.

```cpp
int maxProfit(vector<int>& prices) 
{
	int maxProfit = 0;
	int mini = prices[0];
	for (int i = 0; i < prices.size(); i++)
	{
		mini = min(mini, prices[i]);
		maxProfit = max(maxProfit, prices[i] - mini);
	}
	return maxProfit;
}
```


<hr>

### Best Time to Buy and Sell Stocks 2
You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

On each day, you may decide to buy and/or sell the stock. You can only hold **at most one** share of the stock at any time. However, you can buy it then immediately sell it on the **same day**.

Find and return _the **maximum** profit you can achieve_.


- We cannot buy a stock if we didn't sell our previous stock, so we are taking `buy` variable to keep track
- If we are allowed to buy stock, then we can either,
	- Buy stock
	- Not buy stock on that day
	- When we buy stock we are not allowed to buy stock again, thus we set `buy` to `0`
- If we are not allowed to buy stock, then we can either,
	- sell it
	- or not sell it
	- When we sell, we are allowed to stock on some other day, thus we are make `buy` variable to `1`
```cpp
int actualAnswer(int index, int buy, int n, vector<int> &prices, vector<vector<int>> &dp)
{
	if (index == n)
	{
		return 0;
	}

	if (dp[index][buy] != -1)
		return dp[index][buy];

	int buying = 0, notBuying = 0, sell = 0, notSell = 0;

	if (buy)
	{
		buying = actualAnswer(index + 1, !buy, n, prices, dp) - prices[index];
		notBuying = actualAnswer(index + 1, buy, n, prices, dp) + 0;
	}
	else
	{
		sell = actualAnswer(index + 1, !buy, n, prices, dp) + prices[index];
		notSell = actualAnswer(index + 1, buy, n, prices, dp) + 0;
	}

	return dp[index][buy] = max(max(buying, notBuying), max(sell, notSell));
}

int maxProfit(vector<int> &prices)
{
	int n = prices.size();
	vector<vector<int>> dp(n + 1, vector<int>(2, -1));
	return actualAnswer(0, 1, n, prices, dp);
}
```


**Tabulation** solution
```cpp
int maxProfit(vector<int> &prices)
{
	int n = prices.size();
	vector<vector<int>> dp(n+1, vector<int>(2, -1));
	dp[n][0] = 0, dp[n][1] = 0;
	for (int index = n-1; index >= 0; index--)
	{
		for (int buy = 1; buy >= 0; buy--)
		{
			int buying = 0, notBuying = 0, sell = 0, notSell = 0;

			if (buy)
			{
				buying = dp[index+1][!buy] - prices[index];
				notBuying = dp[index+1][buy] + 0;
			}
			else
			{
				sell = dp[index+1][!buy] + prices[index];
				notSell = dp[index+1][buy] + 0;
			}
			dp[index][buy] = max(max(buying, notBuying), max(sell, notSell));
		}
	}
	return dp[0][1];
}
```


**Space optimization** with tabulation
```cpp
int maxProfit(vector<int> &prices)
{
	int n = prices.size();
	vector<int> next(2, -1);
	vector<int> curr(2, -1);
	next[0] = 0, next[1] = 0;
	for (int index = n - 1; index >= 0; index--)
	{
		for (int buy = 1; buy >= 0; buy--)
		{
			int buying = 0, notBuying = 0, sell = 0, notSell = 0;

			if (buy)
			{
				buying = next[!buy] - prices[index];
				notBuying = next[buy] + 0;
			}
			else
			{
				sell = next[!buy] + prices[index];
				notSell = next[buy] + 0;
			}
			curr[buy] = max(max(buying, notBuying), max(sell, notSell));
		}
		next = curr;
	}
	return next[1];
}
```

<hr>

### Best Time to Buy and Sell Stocks 3
You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

Find the maximum profit you can achieve. You may complete **at most two transactions**.

**Note:** You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

- Same as the last one, but we have one extra variable to take care, i.e., limit.
- thus, instead of 2d dp we take 3d dp array
- Whenever we sell a stock we will increase the limit
- when limit reaches maxLimit we will return zero (base case)
**DP** solution
```cpp
int actualAnswer(int index, int buy, int limit, int maxLimit, int n, vector<int> &prices, vector<vector<vector<int>>> &dp)
{
	if (limit == maxLimit || index == n)
		return 0;

	if (dp[index][buy][limit] != -1)
		return dp[index][buy][limit];

	int buying = 0, notBuying = 0, sell = 0, notSell = 0;

	if (buy)
	{
		buying = actualAnswer(index + 1, !buy, limit, maxLimit, n, prices, dp) - prices[index];
		notBuying = actualAnswer(index + 1, buy, limit, maxLimit, n, prices, dp) + 0;
	}
	else
	{
		sell = actualAnswer(index + 1, !buy, limit + 1, maxLimit, n, prices, dp) + prices[index];
		notSell = actualAnswer(index + 1, buy, limit, maxLimit, n, prices, dp) + 0;
	}

	return dp[index][buy][limit] = max(max(buying, notBuying), max(sell, notSell));
}

int maxProfit(vector<int> &prices)
{
	int n = prices.size();
	int maxLimit = 2;
	vector<vector<vector<int>>> dp(n + 1, vector<vector<int>>(2, vector<int>(2, -1)));
	return actualAnswer(0, 1, 0, maxLimit, n, prices, dp);
}
```


**Tabulation** solution
```cpp
int maxProfit(vector<int> &prices)
{
	int n = prices.size();
	int maxLimit = 2;
	vector<vector<vector<int>>> dp(n + 1, vector<vector<int>>(2, vector<int>(maxLimit + 1, -1)));
	for (int index = 0; index <= n; index++)
	{
		dp[index][0][maxLimit] = 0;
		dp[index][1][maxLimit] = 0;
		if (index == n)
		{
			for (int i = 0; i < 2; i++)
			{
				for (int limit = 0; limit <= maxLimit; limit++)
				{
					dp[index][i][limit] = 0;
				}
			}
		}
	}

	for (int index = n - 1; index >= 0; index--)
	{
		for (int buy = 1; buy >= 0; buy--)
		{
			for (int limit = maxLimit - 1; limit >= 0; limit--)
			{
				int buying = 0, notBuying = 0, sell = 0, notSell = 0;

				if (buy)
				{
					buying = dp[index + 1][!buy][limit] - prices[index];
					notBuying = dp[index + 1][buy][limit] + 0;
				}
				else
				{
					sell = dp[index + 1][!buy][limit + 1] + prices[index];
					notSell = dp[index + 1][buy][limit] + 0;
				}

				dp[index][buy][limit] = max(max(buying, notBuying), max(sell, notSell));
			}
		}
	}
	return dp[0][1][0];
}
```


**Space Optimization** with tabulation
```cpp
int maxProfit(vector<int> &prices)
{
	int n = prices.size();
	int maxLimit = 2;
	vector<vector<int>> next(2, vector<int>(maxLimit + 1, -1));
	vector<vector<int>> curr(2, vector<int>(maxLimit + 1, -1));

	for (int buy = 0; buy < 2; buy++)
	{
		for (int limit = 0; limit <= maxLimit; limit++)
		{
			next[buy][limit] = 0;
		}
	}

	for (int index = n - 1; index >= 0; index--)
	{
		curr[0][maxLimit] = curr[1][maxLimit] = 0;
		for (int buy = 1; buy >= 0; buy--)
		{
			for (int limit = maxLimit - 1; limit >= 0; limit--)
			{
				int buying = 0, notBuying = 0, sell = 0, notSell = 0;

				if (buy)
				{
					buying = next[!buy][limit] - prices[index];
					notBuying = next[buy][limit] + 0;
				}
				else
				{
					sell = next[!buy][limit + 1] + prices[index];
					notSell = next[buy][limit] + 0;
				}

				curr[buy][limit] = max(max(buying, notBuying), max(sell, notSell));
			}
		}
		next = curr; // after calculating entirety of curr, we update next with curr
	}
	return next[1][0];
}
```

<hr>

### Best Time to Buy and Sell Stocks 4
You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `ith` day, and an integer `k`.

Find the maximum profit you can achieve. You may complete at most `k` transactions: i.e. you may buy at most `k` times and sell at most `k` times.

**Note:** You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

- same as last one
**DP** solution
```cpp
int actualAnswer(int index, int buy, int limit, int maxLimit, int n, vector<int> &prices, vector<vector<vector<int>>> &dp)
{
	if (index == n || limit == maxLimit)
	{
		return 0;
	}

	if (dp[index][buy][limit] != -1)
		return dp[index][buy][limit];

	int buying = 0, notBuying = 0, sell = 0, notSell = 0;

	if (buy)
	{
		buying = actualAnswer(index + 1, !buy, limit, maxLimit, n, prices, dp) - prices[index];
		notBuying = actualAnswer(index + 1, buy, limit, maxLimit, n, prices, dp) + 0;
	}
	else
	{
		sell = actualAnswer(index + 1, !buy, limit+1, maxLimit, n, prices, dp) + prices[index];
		notSell = actualAnswer(index + 1, buy, limit, maxLimit, n, prices, dp) + 0;
	}

	return dp[index][buy][limit] = max(max(buying, notBuying), max(sell, notSell));
}

int maxProfit(int k, vector<int> &prices)
{
	int n = prices.size();
	int maxLimit = k;
	vector<vector<vector<int>>> dp(n+1, vector<vector<int>>(2, vector<int>(maxLimit + 1, -1)));
	return actualAnswer(0, 1, 0, maxLimit, n, prices, dp);
}
```


**Tabulation** solution
```cpp
int maxProfit(int k, vector<int> &prices)
{
	int n = prices.size();
	int maxLimit = k;
	vector<vector<vector<int>>> dp(n+1, vector<vector<int>>(2, vector<int>(maxLimit+1, -1)));
	for (int index = 0; index <= n; index++)
	{
		dp[index][0][maxLimit] = 0;
		dp[index][1][maxLimit] = 0;
		if (index == n)
		{
			for (int i = 0; i < 2; i++)
			{
				for (int limit = 0; limit <= maxLimit; limit++)
				{
					dp[index][i][limit] = 0;
				}
			}
		}
	}

	for (int index = n-1; index >= 0; index--)
	{
		for (int buy = 1; buy >= 0; buy--)
		{
			for (int limit = maxLimit-1; limit >= 0; limit--)
			{
				int buying = 0, notBuying = 0, sell = 0, notSell = 0;

				if (buy)
				{
					buying = dp[index+1][!buy][limit] - prices[index];
					notBuying = dp[index+1][buy][limit] + 0;
				}
				else
				{
					sell = dp[index+1][!buy][limit+1] + prices[index];
					notSell = dp[index+1][buy][limit] + 0;
				}

				dp[index][buy][limit] = max(max(buying, notBuying), max(sell, notSell));
			}
		}
	}
	return dp[0][1][0];
}
```


**Space optimization** with tabulation
```cpp
int maxProfit(int k, vector<int> &prices)
{
	int n = prices.size();
	int maxLimit = k;
	vector<vector<int>> next(2, vector<int>(maxLimit + 1, -1));
	vector<vector<int>> curr(2, vector<int>(maxLimit + 1, -1));

	for (int i = 0; i < 2; i++)
	{
		for (int limit = 0; limit <= maxLimit; limit++)
		{
			next[i][limit] = 0;
		}
	}

	for (int index = n - 1; index >= 0; index--)
	{
		curr[0][maxLimit] = curr[1][maxLimit] = 0;
		for (int buy = 1; buy >= 0; buy--)
		{
			for (int limit = maxLimit - 1; limit >= 0; limit--)
			{
				int buying = 0, notBuying = 0, sell = 0, notSell = 0;

				if (buy)
				{
					buying = next[!buy][limit] - prices[index];
					notBuying = next[buy][limit] + 0;
				}
				else
				{
					sell = next[!buy][limit + 1] + prices[index];
					notSell = next[buy][limit] + 0;
				}

				curr[buy][limit] = max(max(buying, notBuying), max(sell, notSell));
			}
		}
		next = curr;  // after calculating entirety of curr, we update next with curr
	}
	return next[1][0];
}
```


#### More efficient way to do this
- We can solve this problem with just a 2d dp, 
- We use two variables,
	1. Index (start from 0 to n-1)
	2. Transaction (starts from 0 to `2*k`)
- We need to use increase the transaction number every time we buy and every time we sell.
- Every **even** transaction we try to buy and every **odd** transaction we try to sell, with this we can keep track of buy without using buy.
- Base case will be to return 0, when we reach `2*k` transactions

| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |out of bounds |
| ----- |-- |-- |-- |-- |-- |-- |-- |-- |:--------------:|
| Array | 3 | 3 | 5 | 0 | 0 | 3 | 1 | 4 |out of bounds |
|Transaction|0|0|0|0|1|1|2|3|4|
So we are buying stock at index 4, selling at 5, again buying at 6 and selling at 7, after all this we get transaction value to 4 which is (`2 * 2`) thus we return 0

**DP** solution
```cpp
int actualAnswer(int index, int transaction, int k, int n, vector<int> &prices, vector<vector<int>> &dp)
{
	if (transaction == 2*k || index == n)
		return 0;
	
	if (dp[index][transaction] != -1)
		return dp[index][transaction];

	int buying = 0, notBuying = 0, sell = 0, notSell = 0;
	if (!(transaction & 1)) // even number check
	{
		buying = actualAnswer(index+1, transaction+1, k, n, prices, dp) - prices[index];
		notBuying = actualAnswer(index+1, transaction, k, n, prices, dp) + 0;
	}
	else
	{
		sell = actualAnswer(index+1, transaction+1, k, n, prices, dp) + prices[index];
		notSell = actualAnswer(index+1, transaction, k, n, prices, dp) + 0;
	}
	return dp[index][transaction] = max(max(buying, notBuying), max(sell, notSell));
}

int maxProfit(int k, vector<int> &prices)
{
	int n = prices.size();
	vector<vector<int>> dp(n+1, vector<int>(2*k+1, -1));
	return actualAnswer(0, 0, k, n, prices, dp);
}
```


**Tabulation** solution
```cpp
int maxProfit(int k, vector<int> &prices)
{
	int n = prices.size();
	vector<vector<int>> dp(n+1, vector<int>(2*k+1, -1));

	for (int index = 0; index <= n; index++)
	{
		dp[index][2 * k] = 0;
		if (index == n)
		{
			for (int transaction = 0; transaction <= 2 * k; transaction++)
				dp[index][transaction] = 0;
		}
	}

	for (int index = n-1; index >= 0; index--)
	{
		for (int transaction = 2 * k - 1; transaction >= 0; transaction--)
		{
			int buying = 0, notBuying = 0, sell = 0, notSell = 0;
			if (!(transaction & 1))
			{
				buying = dp[index+1][transaction+1] - prices[index];
				notBuying = dp[index+1][transaction] + 0;
			}
			else
			{
				sell = dp[index+1][transaction+1] + prices[index];
				notSell = dp[index+1][transaction] + 0;
			}
			dp[index][transaction] = max(max(buying, notBuying), max(sell, notSell));
		}
	}
	return dp[0][0];
}
```


**Space Optimization** with tabulation
```cpp
int maxProfit(int k, vector<int> &prices)
{
	int n = prices.size();
	vector<vector<int>> dp(n+1, vector<int>(2*k+1, -1));
	vector<int> next(2*k+1, -1);
	vector<int> curr(2*k+1, -1);

	for (int transaction = 0; transaction <= 2 * k; transaction++)
		next[transaction] = 0;

	for (int index = n-1; index >= 0; index--)
	{
		curr[2*k] = 0;
		for (int transaction = 2 * k - 1; transaction >= 0; transaction--)
		{
			int buying = 0, notBuying = 0, sell = 0, notSell = 0;
			if (!(transaction & 1))
			{
				buying = next[transaction+1] - prices[index];
				notBuying = next[transaction] + 0;
			}
			else
			{
				sell = next[transaction+1] + prices[index];
				notSell = next[transaction] + 0;
			}
			curr[transaction] = max(max(buying, notBuying), max(sell, notSell));
		}
		next = curr;
	}
	return next[0];
}
```


<hr>

### Best Time to Buy and Sell Stock with Cooldown
You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

- After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).

**Note:** You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

- Base code is same as *Best time to buy and sell stocks 2* but we need to account for one extra variable that is cool down
- Thus for cooldown we take 3d dp instead of 2d dp
- At first `coolDown` is 0, meaning no cooldown
- After we sell stock, cooldown turns 1, thus we use `!coolDown`
- If `coolDown` is 1, we are not allowed to buy stock, thus just move one day and make `coolDown` 0
```cpp
int actualAnswer(int index, int buy, int coolDown, int n, vector<int> &prices, vector<vector<vector<int>>> &dp)
{
	if (index == n)
	{
		return 0;
	}

	if (dp[index][buy][coolDown] != -1)
		return dp[index][buy][coolDown];

	int buying = 0, notBuying = 0, sell = 0, notSell = 0;

	if (buy)
	{
		if (!coolDown)
		{
			buying = actualAnswer(index + 1, !buy, coolDown, n, prices, dp) - prices[index];
			notBuying = actualAnswer(index + 1, buy, coolDown, n, prices, dp) + 0;
		}
		else
			notBuying = actualAnswer(index + 1, buy, !coolDown, n, prices, dp) + 0;
	}
	else
	{
		sell = actualAnswer(index + 1, !buy, !coolDown, n, prices, dp) + prices[index];
		notSell = actualAnswer(index + 1, buy, coolDown, n, prices, dp) + 0;
	}

	return dp[index][buy][coolDown] = max(max(buying, notBuying), max(sell, notSell));
}
int maxProfit(vector<int> &prices)
{
	int n = prices.size();
	vector<vector<vector<int>>> dp(n+1, vector<vector<int>>(2, vector<int>(2, -1))); // as cooldown can only be 1 or 0, size 2 is enough
	return actualAnswer(0, 1, 0, n, prices, dp); // we are sending cooldown 0 at first, that means no cooldown
}
```


**Tabulation** solution
```cpp
int maxProfit(vector<int> &prices)
{
	int n = prices.size();
	vector<vector<vector<int>>> dp(n+1, vector<vector<int>>(2, vector<int>(2, -1))); // as cooldown can only be 1 or 0, size 2 is enough
	
	for (int buy = 0; buy < 2; buy++)
	{
		for (int coolDown = 0; coolDown < 2; coolDown++)
		{
			dp[n][buy][coolDown] = 0;
		}
	}

	for (int index = n-1; index >= 0; index--)
	{
		for (int buy = 1; buy >= 0; buy--)
		{
			for (int coolDown = 1; coolDown >= 0; coolDown--)
			{
				int buying = 0, notBuying = 0, sell = 0, notSell = 0;

				if (buy)
				{
					if (!coolDown)
					{
						buying = dp[index+1][!buy][coolDown] - prices[index];
						notBuying = dp[index+1][buy][coolDown] + 0;
					}
					else
						notBuying = dp[index+1][buy][!coolDown] + 0;
				}
				else
				{
					sell = dp[index+1][!buy][!coolDown] + prices[index];
					notSell = dp[index+1][buy][coolDown] + 0;
				}

				dp[index][buy][coolDown] = max(max(buying, notBuying), max(sell, notSell));
			}
		}
	}

	return dp[0][1][0];
}
```


**Space optimization** with tabulation
```cpp
int maxProfit(vector<int> &prices)
{
	int n = prices.size();
	vector<vector<int>> next(2, vector<int>(2, -1));
	vector<vector<int>> curr(2, vector<int>(2, -1));

	
	for (int buy = 0; buy < 2; buy++)
	{
		for (int coolDown = 0; coolDown < 2; coolDown++)
		{
			next[buy][coolDown] = 0;
		}
	}

	for (int index = n-1; index >= 0; index--)
	{
		for (int buy = 1; buy >= 0; buy--)
		{
			for (int coolDown = 1; coolDown >= 0; coolDown--)
			{
				int buying = 0, notBuying = 0, sell = 0, notSell = 0;

				if (buy)
				{
					if (!coolDown)
					{
						buying = next[!buy][coolDown] - prices[index];
						notBuying = next[buy][coolDown] + 0;
					}
					else
						notBuying = next[buy][!coolDown] + 0;
				}
				else
				{
					sell = next[!buy][!coolDown] + prices[index];
					notSell = next[buy][coolDown] + 0;
				}

				curr[buy][coolDown] = max(max(buying, notBuying), max(sell, notSell));
			}
		}
		next = curr;  // after calculating entirety of curr, we update next with curr
	}

	return next[1][0];
}
```

#### More efficient way to do this
- We will just use two variables
	1. Index
	2. Buy
- When we sell a stock we will move two places instead of one, by this we account for cooldown
![[Pasted image 20230909141230.png]]

**DP** solution
```cpp

int getAns(vector<int> Arr, int ind, int buy, int n, vector<vector<int>> &dp ){

    if(ind>=n) return 0; //base case
    
    if(dp[ind][buy]!=-1)
        return dp[ind][buy];
        
    int profit;
    
    if(buy==0){// We can buy the stock
        profit = max(0+getAns(Arr,ind+1,0,n,dp), -Arr[ind]+getAns(Arr,ind+1,1,n,dp));
    }
    
    if(buy==1){// We can sell the stock
        profit = max(0+getAns(Arr,ind+1,1,n,dp), Arr[ind]+getAns(Arr,ind+2,0,n,dp));
    }
    
    return dp[ind][buy] = profit;
}


int stockProfit(vector<int> &Arr)
{
    int n = Arr.size();
    vector<vector<int>> dp(n,vector<int>(2,-1));
    
    int ans = getAns(Arr,0,0,n,dp);
    return ans;
}
```

<hr>

### Best Time to Buy and Sell Stock with Transaction Fee
You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day, and an integer `fee` representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

**Note:**

- You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
- The transaction fee is only charged once for each stock purchase and sale.

- This is same as *best time to buy and sell stocks 2* but we just have to add transaction fee
- We can transaction fee to buying a stock or to selling the stock (only 1 of them, not both)
- So here we chose to add transaction fees to selling the stock

**Space optimization** with tabulation
```cpp
int maxProfit(vector<int> &prices, int fee)
{
	int n = prices.size();
	vector<int> next(2, -1);
	vector<int> curr(2, -1);
	next[0] = 0, next[1] = 0;
	for (int index = n - 1; index >= 0; index--)
	{
		for (int buy = 1; buy >= 0; buy--)
		{
			int buying = 0, notBuying = 0, sell = 0, notSell = 0;

			if (buy)
			{
				buying = next[!buy] - prices[index];
				notBuying = next[buy] + 0;
			}
			else
			{
				sell = next[!buy] + prices[index] - fee;
				notSell = next[buy] + 0;
			}
			curr[buy] = max(max(buying, notBuying), max(sell, notSell));
		}
		next = curr;
	}
	return next[1];
}
```