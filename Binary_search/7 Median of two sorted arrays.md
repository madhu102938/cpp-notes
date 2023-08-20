```cpp
double findMedianSortedArrays(vector<int> &nums1, vector<int> &nums2)
    {
        int n1 = nums1.size();
        int n2 = nums2.size();
        if (n1 > n2) return findMedianSortedArrays(nums2, nums1);

        int left = (n1 + n2 + 1) >> 1;
        int n = n1 + n2;
        int low = 0;
        int high = n1;
        
        while (low <= high)
        {
            int mid1 = (low + high) >> 1;
            int mid2 = left - mid1;

            int l1 = INT_MIN, l2 = INT_MIN;
            int r1 = INT_MAX, r2 = INT_MAX;

            if (mid1 < n1) r1 = nums1[mid1];
            if (mid2 < n2) r2 = nums2[mid2];
            if (mid1 > 0) l1 = nums1[mid1-1];
            if (mid2 > 0) l2 = nums2[mid2-1];

            if (l1 <= r2 && l2 <= r1)
            {
                if (n % 2 == 0)
                    return (double(max(l1, l2) + min(r1, r2))) / 2.0;
                else
                    return max(l1, l2);
            }
            else if (l1 > r2)
                high = mid1 - 1;
            else
                low = mid1 + 1;
        }
        return 0;
    }
```


<hr>


**2Q)** Kth element after merging 2 sorted arrays

```cpp
int kthElement(vector<int> &nums1, vector<int> &nums2, int n1, int n2, int k)
{
    if (n1 > n2) return kthElement(nums2, nums1, n2, n1, k);

	// If we have only 3 elements in nums1 and 10 in nums2 and we are asked if find 12th element, then we cannot just have 0 for low, because we need to atleast pick 2 elements from nums1, so get 12 (2 + 10) elements in total thus we need to consider k-n2 also
    int low = max(0, k-n2);
    // if k is less than n1, then we need not pick all the elements in nums1, only up till k
    int high = min(k, n1);
    
    while (low <= high)
    {
        int mid1 = (low + high) >> 1;
        int mid2 = k - mid1;

        int l1 = INT_MIN, l2 = INT_MIN;
        int r1 = INT_MAX, r2 = INT_MAX;

        if (mid1 < n1) r1 = nums1[mid1];
        if (mid2 < n2) r2 = nums2[mid2];
        if (mid1 > 0) l1 = nums1[mid1-1];
        if (mid2 > 0) l2 = nums2[mid2-1];

        if (l1 <= r2 && l2 <= r1)
        {
            return max(l1, l2);
        }
        else if (l1 > r2)
            high = mid1 - 1;
        else
            low = mid1 + 1;
    }
    return 0;
}
```