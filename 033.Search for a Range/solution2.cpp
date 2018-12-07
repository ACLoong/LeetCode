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
            //��Ϊfirst=mid+1,���������len��Ҫ�ڼ�ȥhalf�Ļ���֮���ټ�ȥ1
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
## ��ע
lower_bound�㷨Ҫ�����Ѿ����շǵݼ�˳��������������ҵ���һ�����ڵ��ڸ���ֵkey���Ǹ����������ʵ��ԭ���Ƕ��ֲ��ҡ�
��upper_bound����Ҫ���ڰ��շǵݼ�˳���ź�����������ҵ���һ�����ڸ���ֵkey���Ǹ����������ʵ��ԭ���Ƕ��ֲ��ҡ�
����ʵ�ֲο���stl�е�ʵ�ַ�ʽ����������������ֵ�������е��±ꡣ����Ҳ�������������ֵ�����᷵������Ĵ�С������������е�endһ������Ӧ��Ч�±����һ��ֵ��
*/ 


