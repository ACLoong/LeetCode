class Solution:
    def containsDuplicate(self, nums):
        """
        Given an array of integers, find if the array contains any duplicates.

        Args:
            nums(List[int]): the name of the array of integers

        Returns:
            A bool value(bool)
        """
        return len(nums) > len(set(nums))
