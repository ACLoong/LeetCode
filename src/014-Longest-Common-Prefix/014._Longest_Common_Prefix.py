class Solution:
    def longestCommonPrefix(self, strs):
        """
        Write a function to find the longest common prefix string amongst an array of strings.

        Args:
            strs(List[str]): the name of an array of strings

        Returns:
            the longest common prefix string(str)
        """
        if len(strs) == 0:
            return ""
        
        result = ""
        s_len = len(strs[0])
        for l in strs:
            s_len = min(s_len, len(l))
     
        for i in range(s_len):
            ch = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != ch:
                    return result
            result += ch
     
        return result
                    