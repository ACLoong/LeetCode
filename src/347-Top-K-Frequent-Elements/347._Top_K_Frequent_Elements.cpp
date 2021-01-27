class Solution {
public:
    //use vector
    vector<int> topKFrequent_approach1(vector<int>& nums, int k) {
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

    //use hash map & priority queue
    vector<int> topKFrequent_approach2(vector<int>& nums, int k) {
        vector<int> res;
        unordered_map<int, int> cnt;
        for (int num : nums) {
            ++cnt[num];
        }
        
        priority_queue<pair<int, int>, vector<pair<int, int>>> p_queue;
        
        for (auto it = cnt.begin(); it != cnt.end(); ++it) {
            //in p_queue<pair<int, int>...>,the 1st int is the frequency, the 2nd int is the num.
            p_queue.push(make_pair((*it).second, (*it).first));
            if (p_queue.size() > cnt.size() - k) {
                res.push_back(p_queue.top().second);
                p_queue.pop();
            } 
        }
        return res;
    }

};
