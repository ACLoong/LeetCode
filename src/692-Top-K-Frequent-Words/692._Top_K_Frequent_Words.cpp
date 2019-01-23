//using hash map & priority queue, O((n + k)logn)
class Solution {
public:
    struct Comp {
        bool operator()(const pair<int, string>& lhs, const pair<int, string>& rhs) const {
            if (lhs.first != rhs.first) {
                return lhs.first < rhs.first;
            }
            return lhs.second > rhs.second;
        }
    };

    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string, int> cnt;
        vector<string> res;
         // count occurances of each word
        for (auto& w : words) {
            ++cnt[w];
        }
        
        priority_queue<pair<int, string>, vector<pair<int, string>>, Comp> p_queue;
        for (auto it : cnt) {
            p_queue.emplace(it.second, it.first);
        }
        
        while (k-- > 0 && !p_queue.empty()) {
            res.push_back(p_queue.top().second);
            p_queue.pop();
        }
        
        return res;
    }
};
