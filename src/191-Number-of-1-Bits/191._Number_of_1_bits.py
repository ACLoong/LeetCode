class Solution(object):
    def hammingWeight(self, n):
        """
        Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).

        Args:
            n(int): the given integer

        Returns:
            the number of '1' bits the given number has(int)
        """
        res = []
        while n > 0:
            r = n % 2
            n = n // 2
            res.append(r)
        return res.count(1)
