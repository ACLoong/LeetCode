class Solution:
    def intersect(self, nums1, nums2):
        """
        Given two arrays, write a function to compute their intersection.

        Args:
            nums1(List[int]):the name of array nums1
            nums2(List[int]):the name of array nums2

        Returns:
            the intersection of the two arrays(List[int])
        """
        record, result = {}, []
        for num in nums1:
            record[num] = record.get(num, 0) + 1
                
        for num in nums2:
            if num in record and record[num]:
                result.append(num)
                record[num] -= 1
        
        return result
