class Solution:
    def trailingZeroes(self, n):
        """
        Given an integer n, return the number of trailing zeroes in n!.

        Args:
            n(int): the given integer n

        Returns:
            the number of trailing zeroes in n!(int)
        """
        cnt = 0
        while n >= 5:
            n //= 5
            cnt += n
        return cnt
