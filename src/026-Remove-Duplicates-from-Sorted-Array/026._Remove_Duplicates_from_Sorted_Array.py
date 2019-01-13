class Solution:
    def removeDuplicates(self, nums):
        """
        Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

        Args:
            nums(List[int]): the name of the array of integer

        Returns:
            the new length of the array of integer
        """
        if(nums == None or len(nums) == 0):
            return 0
        
        cur = nums[0]
        index = 1
        for i in range(1, len(nums)):
            if(nums[i] == cur):
                continue
            else:
                nums[index] = nums[i]
                index += 1
                cur = nums[i]
        return index      