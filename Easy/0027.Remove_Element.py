class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)

        q = deque()
        ct = 0

        # build queue of indeces where val is
        for i in range(n): 
            if nums[i] == val: 
                ct += 1
                q.append(i)

        # replace val indeces with nonval values
        for i in range(n - 1, n - ct - 1, -1): 
            if nums[i] != val: 
                nums[q.popleft()] = nums[i]

        return n - ct
