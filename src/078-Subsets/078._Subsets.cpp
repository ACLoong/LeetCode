class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> cur;
        sort(nums.begin(), nums.end());
        getSub(nums, 0, cur, res);
        return res;
    }
    void getSub(vector<int>& nums, int pos, vector<int>& cur, vector<vector<int>>& res) {
        res.push_back(cur);
        for (int i = pos; i < nums.size(); ++i) {
            cur.push_back(nums[i]);
            getSub(nums, i + 1, cur, res);
            cur.pop_back();
        }
    }
};