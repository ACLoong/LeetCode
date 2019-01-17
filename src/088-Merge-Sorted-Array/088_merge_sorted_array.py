class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

        Args:
            nums1(List[int]): the name of the integer array nums1
            m(int): the size(length) of the integer array nums1 
            nums2(List[int]): the name of the integer array nums2
            n(int): the size(length) of the integer array nums2

        Returns:
            void Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
