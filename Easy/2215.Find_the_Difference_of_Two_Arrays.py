class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        # create sets out of nums1,2 to utilize property of sets to find difference
        N1 = set(nums1)
        N2 = set(nums2)
        
        # find the difference of each set both ways
        sol = [N1 - N2, N2 - N1]
        
        return sol
