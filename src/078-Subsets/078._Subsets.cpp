class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> cur;
        sort(nums.begin(), nums.end());
        getSub(nums, nums.begin(), cur, res);
        return res;
    }
    void getSub(vector<int>& nums, vector<int>::iterator it, vector<int>& cur, vector<vector<int>>& res) {
        res.push_back(cur);
        for (auto iter = it; iter != nums.end(); iter++) {
            cur.push_back(*iter);
            getSub(nums, iter + 1, cur, res);
            cur.pop_back();
        }
    }
};
