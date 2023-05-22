class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # edge case: if nums1 just needs to be filled with nums2
        if m == 0: 
            for i in range(n): 
                nums1[i] = nums2[i]

        # main process: fill in nums1 in order of greatest to smallest
        while m > 0 and n > 0: 
            if nums2[n - 1] > nums1[m - 1]: 
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
            else:
                nums1[m + n - 1] = nums1[m - 1]
                nums1[m - 1] = 0
                m -= 1
        
        # edge case: when all of nums1 gets moved before nums2 is done
        if n > 0: 
            for i in range(n): 
                nums1[i] = nums2[i]
