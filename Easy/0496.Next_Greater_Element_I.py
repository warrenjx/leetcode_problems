class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        # daily temperatures on nums2
        sols = [-1] * len(nums2)
        stack = []

        for i, val in enumerate(nums2): 
            while stack and val > nums2[stack[-1]]: 
                curr = stack.pop()
                sols[curr] = val
            
            stack.append(i)

        # go through nums1 and look for the term in nums2 then transfer into sol
        sol = []

        for val in nums1: 
            sol.append(sols[nums2.index(val)])

        return sol