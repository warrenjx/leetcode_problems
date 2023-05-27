class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        sol = []

        # encapsulate 2-sum code basically, n^2 eww
        for i in range(len(nums) - 2): 
            j = i + 1
            k = len(nums) - 1

            # to prevent duplicate triplits
            if i > 0 and nums[i] == nums[i - 1]: 
                continue

            while j < k: 
                if j > i + 1 and nums[j] == nums[j - 1]: 
                    j += 1
                    continue
                elif k < len(nums) - 1 and nums[k] == nums[k + 1]: 
                    k -= 1
                    continue

                # 2-sum process
                total = nums[i] + nums[j] + nums[k]
                if total == 0: 
                    sol.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif total > 0: 
                    k -= 1
                else: 
                    j += 1

        return sol
