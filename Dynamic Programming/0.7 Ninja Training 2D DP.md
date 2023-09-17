Ninja is planning this n days long training schedule. Each day he can perform any one of these three activities: ***running, fighting practice**,* or ***learning new moves***. Each activity has some merit points on each day. As Ninja has to improve all his skills, he can't do the same activity on two consecutive days. Can you help Ninja find out the maximum merit points Ninja can earn?
 
**Recurrence** relationship
```cpp
#include <bits/stdc++.h>
using namespace std;

// Recursive function to compute the maximum points that can be earned
// by the ninja on each day, given the points earned on the previous day
// and the restriction that the ninja cannot train on the same activity
// two days in a row.
int actualAnswer(int day, int last, vector<vector<int>> &points)
{
    // Base case: if it's the first day, return the maximum points
    // that can be earned by training on any activity except the one
    // trained on the previous day.
    if (day == 0)
    {
        int maxi = 0;
        for (int i = 0; i < 3; i++)
        {
            if (i != last)
            {
                maxi = max(maxi, points[day][i]);
            }
        }
        return maxi;
    }

    // Recursive case: compute the maximum points that can be earned
    // on the current day by training on each activity except the one
    // trained on the previous day, and return the maximum of these values.
    int maxii = 0;
    for (int i = 0; i < 3; i++)
    {
        if (i != last)
        {
            maxii = max(maxii, actualAnswer(day - 1, i, points) + points[day][i]);
        }
    }
    return maxii;
}

// Function to compute the maximum points that can be earned by the ninja
// over the entire training period, given the points earned on each day.
int ninjaTraining(int n, vector<vector<int>> &points)
{
    // Call the recursive function to compute the maximum points that can
    // be earned on the last day, given that the ninja cannot train on the
    // same activity two days in a row.
    int ans = actualAnswer(n - 1, 3, points);
    return ans;
}

int main()
{
    int n;
    vector<vector<int>> merit = {
        {10, 40, 70},
        {20, 50, 80},
        {30, 60, 90}};

    cout << ninjaTraining(merit.size(), merit) << endl;
    return 0;
}
```




**DP** Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int actualAnswer(int day, int last, vector<vector<int>> &points, vector<vector<int>> &dp)
{
    if (day == 0)
    {
        int maxi = 0;
        for (int i = 0; i < 3; i++)
        {
            if (i != last)
            {
                maxi = max(maxi, points[day][i]);
            }
        }
        return maxi;
    }
    if(dp[day][last] != -1)
        return dp[day][last];
    int maxii = 0;
    for (int i = 0; i < 3; i++)
    {
        if (i != last)
        {
            maxii = max(maxii, actualAnswer(day - 1, i, points, dp) + points[day][i]);
        }
    }
    dp[day][last] = maxii;
    return dp[day][last];
}

int ninjaTraining(int n, vector<vector<int>> &points)
{
    vector<vector<int>>dp(n+1, vector<int>(5, -1));
    int ans = actualAnswer(n - 1, 3, points, dp);
    return ans;
}

int main()
{
    int n;
    vector<vector<int>> merit = {
        {10, 40, 70},
        {20, 50, 80},
        {30, 60, 90}};

    cout << ninjaTraining(merit.size(), merit) << endl;
    return 0;
}
```
***Time Complexity** - O($N*4*3$) for every state we are running a for loop of size 3, so number of states multiplied by 3* 
***Space Complexity** - O($N$) : Stack space + O($N*4$) : dp array size*



**Tabulation** solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int actualAnswer(vector<vector<int>> &points, vector<vector<int>> &dp)
{
    dp[0][0] = max(points[0][1], points[0][2]);
    dp[0][1] = max(points[0][0], points[0][2]);
    dp[0][2] = max(points[0][0], points[0][1]);
    dp[0][3] = max(points[0][0], max(points[0][1], points[0][2]));

    int n = points.size();
    
    for (int day = 1; day < n; day++)
    {
        for (int last = 0; last < 4; last++)
        {
            int maxii = 0;
            for (int task = 0; task < 3; task++)
            {
                if (task != last)
                {
                    maxii = max(maxii, dp[day-1][task] + points[day][task]);
                }
            }
            dp[day][last] = maxii;
        }
    }
    return dp[n-1][3];
}

int ninjaTraining(int n, vector<vector<int>> &points)
{
    vector<vector<int>> dp(n + 1, vector<int>(5, -1));
    int ans = actualAnswer(points, dp);
    return ans;
}

int main()
{
    int n;
    vector<vector<int>> merit = {
        {10, 40, 70},
        {20, 50, 80},
        {30, 60, 90}};

    cout << ninjaTraining(merit.size(), merit) << endl;
    return 0;
}
```
***Time Complexity** - $O(N*4*3)$ just multiplying the for loop size*
***Space Complexity** - O($N*4)$ size of dp array*




**Space optimization** with tabulation
```cpp
#include <bits/stdc++.h>
using namespace std;

int actualAnswer(vector<vector<int>> &points, vector<int> &prev)
{
    prev[0] = max(points[0][1], points[0][2]);
    prev[1] = max(points[0][0], points[0][2]);
    prev[2] = max(points[0][0], points[0][1]);
    prev[3] = max(points[0][0], max(points[0][1], points[0][2]));

    int n = points.size();
    for (int day = 1; day < n; day++)
    {
        vector<int> current(5, -1);
        for (int last = 0; last < 4; last++)
        {
            int maxii = 0;
            for (int task = 0; task < 3; task++)
            {
                if (task != last)
                {
                    maxii = max(maxii,  prev[task] + points[day][task]);
                }
            }
            current[last] = maxii;
        }
        prev = current;
    }
    return  prev[3];
}

int ninjaTraining(int n, vector<vector<int>> &points)
{
    vector<int> prev(5, -1);
    int ans = actualAnswer(points,  prev);
    return ans;
}
```
***Time Complexity** - $O(N*4*3)$ just multiplying the for loop size*
***Space Complexity** - O($4$) just the array space*