# 035.Search Insert Position 

**<font color=red>level:Easy</font>**


## Description

Given a sorted array and a target value, return the index if the target is found. If not, return the index
where it would be if it were inserted in order.
You may assume no duplicates in the array.
Here are few examples
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0

## Analysis

* Time comlexity:O(logn)

* Space comlexity:O(1)

## Solution in C++
```c++
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        if(nums.empty()){
		return 0;
	}
	int left = 0;
	int right = nums.size() - 1;
	while(left <= right){
		int mid = (left + right)/2;
		if( nums[mid] == target){
			return mid;
		}
		if(nums[mid] < target){
			left = mid + 1;
		}
		else
			right = mid - 1;
	}
	return left;
    }
};

```

## Result

* Success

* Details:

Runtime: 8 ms, faster than 32.84% of C++ online submissions for Search Insert Position.

