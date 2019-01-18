class Solution:
    def isPalindrome(self, s):
        """
        Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

        Args:
            s(str): the given string

        Returns:
            reeturn a bool value(bool)
        """
        charList = []
        for ch in s:
            if ch.isalnum():
                charList.append(ch.lower())
        return charList == charList[::-1]
