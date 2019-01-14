class Solution:
    def plusOne(self, digits):
        """
        Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

        Args:
            digits(List[int]): the name of the array of integer

        Returns:
            A new array of integer that plus one from the old array of integer(List[int])
        """
        i = len(digits) - 1
        while i >= 0:
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
            i -= 1
        
        digits[0] = 1
        digits.append(0)
        return digits
