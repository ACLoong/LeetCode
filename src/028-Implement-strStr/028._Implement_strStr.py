class Solution:
    def strStr(self, haystack, needle):
        """
        Implement strStr().

        Args:
            haystack(str): the name of the given string
            needle(str): the name f the given substring

        Returns:
            the index of the first occurrence of needle in haystack(int)
        """
        l1 = len(haystack)
        l2 = len(needle)
        if l1 < l2:
            return -1
        end = l2
        start = 0
        while end <= l1:
            if haystack[start:end:] == needle:
                return start
            start +=1
            end +=1
        return -1
        