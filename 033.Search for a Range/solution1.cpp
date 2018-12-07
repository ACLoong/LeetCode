//ʹ�� STL
// LeetCode, Search for a Range
// ͵����������ʹ�� STL
// ʱ�临�Ӷ� O(logn)���ռ临�Ӷ� O(1)
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
