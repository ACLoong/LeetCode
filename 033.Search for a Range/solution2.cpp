#include <iostream>
#include <vector>
#include <iterator>
using namespace std;


int lower_bound(vector<int>& arr, int key) {
    int half;
    int len = arr.size();
    int mid;
    int first = 0;
    while (len > 0) {
        half = len >> 1;
        mid = first + half;
        //in the right part
        if (arr[mid] < key) {
            first = mid + 1;
            //因为first=mid+1,所以这里的len需要在减去half的基础之上再减去1
            len = len - half - 1;
        } else {
            //in the left part
            len = half;
        }
    }
    return first;
}
int upper_bound(vector<int>& arr, int key) {
    int mid;
    int first = 0;
    int len = arr.size();
    int half;
    while (len > 0) {
        half = len >> 1;
        mid = half + first;
        if (arr[mid] > key) {//in the left part
            len = half;
        } else {//if arr[mid]<= key ,in the right part
            first = mid + 1;
            len = len - half - 1;
        }
    }
    return first;
}
	
class Solution {
public:
	vector<int> searchRange (vector<int>& arr,int target) {
		int lower = lower_bound(arr, target);
		int upper = upper_bound(arr, target);
		vector<int> res; 
		if (lower != -1)
			res.push_back(lower);
		res.push_back(upper-1);
		return res;
	}

};

/*
## 备注
lower_bound算法要求在已经按照非递减顺序排序的数组中找到第一个大于等于给定值key的那个数，其基本实现原理是二分查找。
　upper_bound函数要求在按照非递减顺序排好序的数组中找到第一个大于给定值key的那个数，其基本实现原理是二分查找。
两种实现参考了stl中的实现方式，返回满足条件的值在数组中的下标。如果找不到满足条件的值，将会返回数组的大小，就像迭代器中的end一样，对应有效下标的下一个值。
*/ 


