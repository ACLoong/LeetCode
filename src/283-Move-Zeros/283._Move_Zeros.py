class Solution:
    def moveZeroes(self, nums):
        """
        Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

        Args:
            nums(List[int]): the name of array of integers

        Returns:
            void Do not return anything, modify nums in-place instead.
        """
        point = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[point] , nums[i] = nums[i], nums[point]
                point += 1


if __name__ == "__main__":
    arr = [0, 1, 0, 3, 12]
    Solution().moveZeroes(arr)
    print(arr)
