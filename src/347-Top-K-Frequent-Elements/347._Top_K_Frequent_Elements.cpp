class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> res;
        vector<pair<int, int>> pairCur;
        vector<int>::iterator it;
        sort(nums.begin(), nums.end());
        for (it = nums.begin(); it != nums.end(); it++) {
            int count = 1;
            while ((it + 1) != nums.end() && *(it+1) == *it) {
                count++;
                it++;
            }
            pairCur.push_back(pair<int, int>(*it, count));
        }
        auto cmp = [](const pair<int,int>& left, const pair<int, int>& right) {
            return left.second > right.second;
        };
        
        sort(pairCur.begin(), pairCur.end(), cmp);
        for (int j = 0; j < k; j++) {
            res.push_back(pairCur[j].first);
        }
        return res;
    }
};