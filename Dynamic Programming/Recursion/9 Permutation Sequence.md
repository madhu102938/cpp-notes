The set `[1, 2, 3, ..., n]` contains a total of `n!` unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for `n = 3`:

1. `"123"`
2. `"132"`
3. `"213"`
4. `"231"`
5. `"312"`
6. `"321"`

Given `n` and `k`, return the `kth` permutation sequence.

```cpp
class Solution {
public:
    string getPermutation(int n, int k) 
    {
        // Calculate (n-1)! and store it in 'fact'
        int fact = 1;
        for (int i = 1; i < n; i++)
        {
            fact = fact * i;
        }
        
        // Create a vector 'v' containing the numbers 1 to n
        vector<int> v;
        for (int i = 1; i <= n; i++)
        {
            v.push_back(i);
        }
        
        // Initialize an empty string 'ans'
        string ans = "";
        
        // Decrement 'k' to account for 0-based indexing
        k--;
        
        // Loop until 'v' is empty
        while (true)
        {
            // Append the (k/fact)-th element of 'v' to 'ans'
            ans = ans + to_string(v[k/fact]);
            
            // Remove the (k/fact)-th element of 'v'
            v.erase(v.begin() + k/fact);
            
            // If 'v' is empty, break out of the loop
            if (v.size() == 0)
                break;
            
            // Update 'k' and 'fact' for the next iteration
            k = k % fact;
            fact = fact / v.size();
        }
        
        // Return the final permutation
        return ans;
    }
};
```


```java
public static int maximumLearning(List<Integer> iv, List<Integer> articles, int p){
        int n=iv.size();    //finding the size of the list
        int associated[][]=new int[n][2];    //creating a 2-d associated array with dimension n and 2
        for(int i=0;i<n;i++){    //creating the associated array
            associated[i][0]=articles.get(i)*2;
            associated[i][1]=iv.get(i);
        }
        int max_learning=-1,pages=0,learning=0;
        for(int i=0;i<n;i++){    //generating all possible sub-arrays of the associated array
            for(int k=0;k<n-i;k++){
                learning=0;
                pages=0;
                for(int j=i;j<=k;j++){
                    pages+=associated[j][0];    //adding the pages
                    if(pages>p){    //if pages exceed break the loop
                        break;
                    }
                    learning+=associated[j][1];    //adding the iv value
                }
                if(learning>max_learning){    //current learning greater than max_learning
                    max_learning=learning;    //set max_learning to current_learning
                }
            }
        }
        return max_learning;    //return the max_learning

    }    
}
```


```cpp
int maximumLearning(vector<int> iv, vector<int> articles, int p){
    int n = iv.size();    //finding the size of the list
    int associated[n][2];    //creating a 2-d associated array with dimension n and 2
    for(int i=0;i<n;i++){    //creating the associated array
        associated[i][0]=articles.at(i)*2;
        associated[i][1]=iv.at(i);
    }
    int max_learning=-1,pages=0,learning=0;
    for(int i=0;i<n;i++){    //generating all possible sub-arrays of the associated array
        for(int k=0;k<n-i;k++){
            learning=0;
            pages=0;
            for(int j=i;j<=k;j++){
                pages+=associated[j][0];    //adding the pages
                if(pages>p){    //if pages exceed break the loop
                    break;
                }
                learning+=associated[j][1];    //adding the iv value
            }
            if(learning>max_learning){    //current learning greater than max_learning
                max_learning=learning;    //set max_learning to current_learning
            }
        }
    }
    return max_learning;    //return the max_learning
}
```


```java
static int getMaximumJobs (int n, int m, int k) {
        k--;                                // Change k to zero based index instead of one based index 
        int arr [] = new int [n];
        for (int i = 0; i < n; i++) arr [i] = 1; // Fill the array with 1's first 
        int sum = n, maxjob = 1;                 // With all 1's, the sum is n and maxjob is 1 
        
        while (sum <= m) {
            // Increase the kth item by 1; this increased value is now maxjob 
            arr [k]++;
            maxjob = arr [k];
            // Make sure difference between elements (on left of kth element) is 1 or less (for balanced schedule)
            // If the difference is more than 1, increase element so that difference is 1 
            for (int i = k - 1; i >= 0; i--) 
                if ((arr [i + 1] - arr [i]) > 1) arr [i]++;
            // Do same thing for elements to the right of kth element 
            for (int i = k + 1; i < n; i++) 
                if ((arr [i - 1] - arr [i]) > 1) arr [i]++;
            
            // Find the new sum of all elements again 
            sum = 0;
            for (int i = 0; i < n; i++) sum += arr [i];
        }
        // When we reach here, the sum of the elements is > m, so maxjob is one value too high 
        // decrement maxjob and return it 
        return maxjob - 1;
    }
```


```cpp
int getMaximumJobs (int n, int m, int k) {
        k--;                                // Change k to zero based index instead of one based index 
        int arr [n];
        for (int i = 0; i < n; i++) arr [i] = 1; // Fill the array with 1's first 
        int sum = n, maxjob = 1;                 // With all 1's, the sum is n and maxjob is 1 
        
        while (sum <= m) {
            // Increase the kth item by 1; this increased value is now maxjob 
            arr [k]++;
            maxjob = arr [k];
            // Make sure difference between elements (on left of kth element) is 1 or less (for balanced schedule)
            // If the difference is more than 1, increase element so that difference is 1 
            for (int i = k - 1; i >= 0; i--) 
                if ((arr [i + 1] - arr [i]) > 1) arr [i]++;
            // Do same thing for elements to the right of kth element 
            for (int i = k + 1; i < n; i++) 
                if ((arr [i - 1] - arr [i]) > 1) arr [i]++;
            
            // Find the new sum of all elements again 
            sum = 0;
            for (int i = 0; i < n; i++) sum += arr [i];
        }
        // When we reach here, the sum of the elements is > m, so maxjob is one value too high 
        // decrement maxjob and return it 
        return maxjob - 1;
    }
```


```cpp
int maximumLearning(vector<int>& iv,vector<int> &articles,int p) {
    int total = articles.size();
    vector<vector<int>> dp(total + 1, vector<int>(p + 1, 0));

    for (int i = 1; i <= total; ++i) {
        for (int pages = 0; pages <= p; ++pages) {
            dp[i][pages] = dp[i - 1][pages];

            if (pages >= articles[i - 1]) {
                dp[i][pages] = max(dp[i][pages], dp[i - 1][pages - iv[i-1]] + 2 * iv[i - 1] * iv[i - 1]);
            }
        }
    }

    return dp[total][p];
}
```



```cpp
int ok(vector<vector<int>> &f,vector<int> &iv,vector<int> &articles,int p,int i=0)
{
    if(i == iv.size()) return 0;
    if(f[i][p] != -1) return f[i][p];
    int a1=ok(f,iv,articles,p,i+1);
    int a2=0;
    if(2*articles[i] <= p)
    a2=iv[i] + ok(f,iv,articles,p-2*articles[i],i+1);
    f[i][p] = max(a1,a2);
    return f[i][p];
}
int maximumLearning(vector<int> iv,vector<int> articles,int p)
{
    int n=articles.size();
    vector<vector<int>> f(n+1,vector<int>(p+1,-1));
    return ok(f,iv,articles,p);
}
```