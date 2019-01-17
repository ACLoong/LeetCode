class Solution:
    def mySqrt(self, x):
        """
        Implement int sqrt(int x).

        Args:
            x(int): the given integer value

        Returns:
            the square root of x(int)
        """
        low = 0
        high = x
        while low <= high:
            mid = (low + high) // 2
            
            if mid ** 2 == x:
                return mid
            
            elif mid ** 2 < x and (mid+1) ** 2 >x:
                return mid
            
            if mid ** 2 > x:
                high = mid - 1
            
            if mid ** 2 < x:
                low = mid + 1
