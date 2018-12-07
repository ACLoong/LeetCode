//使用 STL
// LeetCode, Search for a Range
// 偷懒的做法，使用 STL
// 时间复杂度 O(logn)，空间复杂度 O(1)
class Solution {
public:
	vector<int> searchRange(int A[], int n, int target) {
		const int l = distance(A, lower_bound(A, A + n, target));
		const int u = distance(A, prev(upper_bound(A, A + n, target)));
		if (A[l] != target) // not found
			return vector<int> { -1, -1 };
		else
			return vector<int> { l, u };
	}
};
