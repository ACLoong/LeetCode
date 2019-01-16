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