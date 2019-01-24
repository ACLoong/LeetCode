class Solution:
    def isHappy(self, n):
        """
        Write an algorithm to determine if a number is "happy".

        Args:
            n(int): the given integer number

        Returns:
            A bool value(bool)
        """
        history = []
        
        while True:
            n = sum([int(d)**2 for d in str(n)])
            if n == 1:
                return True
            if n not in history:
                history.append(n)
            elif n in history and n != 1:
                return False
