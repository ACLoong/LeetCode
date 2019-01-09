class Solution:
    def reverse(self, x):
        """
        Given a 32-bit signed integer, reverse digits of an integer.

        Args:
            x(int): a 32-bit signed interger

        Returns:
            the inverse digits of the given interger(int)
        """
        s = str(x)
        if s[0] == '-':
            res = int('-' + s[1:][::-1])
        else:
            res = int(s[::-1])
        if -2**31 <= res <= 2**31-1:
            return res
        else:
            return 0
        