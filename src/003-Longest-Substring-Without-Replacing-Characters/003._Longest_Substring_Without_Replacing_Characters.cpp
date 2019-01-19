class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        set<char> setStr;
        int maxLen = 0;
        int end = 0;
        for (int i = 0; i < s.length(); i++) {
            while (setStr.insert(s[end]).second && end < s.length()) {
                end++;
                maxLen = max(maxLen, end - i);
            }
            setStr.erase(s[i]);
        }
        return maxLen;
    }
};
