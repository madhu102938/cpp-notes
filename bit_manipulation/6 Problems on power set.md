**Q) You are given an array, you are supposed to place `+` and `-` in front each number, such they add up to a number that is divisible by 360 *(i.e., 0, 360, -360, ....)***
[Petr and a Combination Lock](https://codeforces.com/problemset/problem/1097/B)

Lets take an array = {10, 20, 30}

| Subset       | Binary Representation |
|-------------|-------------------------|
| {-10, -20, -30}                | 000                |
| {10, -20, 30}              | 001                   |
| {-10, 20, -30}              | 010                   |
| {10, 20, -30}          | 011                   |
| {-10, -20, 30}              | 100                   |
| {10, -20, 30}          | 101                   |
| {-10, 20, 30}          | 110                   |
| {10, 20, 30}      | 111                   |

We use the same logic as power set but, when we get a zero we take negative of that index, and positive when we get a 1.

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool subSetGeneration(vector<int>& nums) 
    {
        int n = nums.size();
        int sum = 0;
        for (int i = 0; i < (1 << n); i++)
        {
            sum = 0;
            int count = 0;
            int k = i;
            for (int j = 0; j < n; j++)
            {
                if (k & 1)
                    sum += nums[count];
                else
                    sum -= nums[count];
                count++;
                k = k >> 1;
            }
            if (sum % 360 == 0)
                return true;
        }
        return false;
    }
};

int main()
{
    int n;
    vector<int> arr;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int temp;
        cin >> temp;
        arr.push_back(temp);
    }
    Solution ob;
    int ans = ob.subSetGeneration(arr);
    if (ans)
        cout << "YES";
    else
        cout << "NO";
    return 0;
}
```

