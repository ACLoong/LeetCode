# 088.Merge Sorted Array

**<font color=red>level: Easy</font>**

## Description

```c++
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

    The number of elements initialized in nums1 and nums2 are m and n respectively.
    You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
```

## C++ Solutions

* Time complexity: O(m+n)
* Space complexity: O(1)

```c++
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int index_nums1 = m - 1;
        int index_nums2 = n - 1;
        int icur = m + n - 1;

        while (index_nums1 >= 0 && index_nums2 >= 0) {
            nums1[icur--] = (nums1[index_nums1] >= nums2[index_nums2] ? nums1[index_nums1--] : nums2[index_nums2--]);
        }
        while (index_nums2 >= 0) {
            nums1[icur--] = nums2[index_nums2--];
        }
    }
};
```

## Submissions

* Success
* Details:  
Runtime: 4 ms, faster than 99.39% of C++ online submissions for Merge Sorted Array.


