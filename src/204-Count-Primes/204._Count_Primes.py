class Solution:
    def countPrimes(self, n):
        """
        Count the number of prime numbers less than a non-negative number, n.

        Args:
            n(int): the given non-negative number

        Returns:
            the number of prime numbers(int)
        """
        if n <= 2:
            return 0
        res = [1] * n
        res[0] = res[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if res[i] == 1:
                res[i * i:n:i] = [0] * len(res[i * i:n:i])
        return sum(res)
