You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.
You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.
Return _the maximum profit you can achieve from this transaction_. If you cannot achieve any profit, return `0`.

**NOT** a DP question
```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxProfit = 0;
        int mini = prices[0];
        for (int i = 0; i < prices.size(); i++)
        {
            maxProfit = max(maxProfit, prices[i] - mini);
            if (prices[i] < mini)
                mini = prices[i];
        }
        return maxProfit;
    }
};
```