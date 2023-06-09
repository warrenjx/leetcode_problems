class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        # takes care of edge case
        if len(nums) <= 1: 
            return k

        max_len = 0
        
        tail = 0
        head = 0
        # use a stack for holding zeros so can just pop first zero out when needed
        zeros = deque()

        while head < len(nums): 
            if nums[head] == 0: # need to replace a zero
                if k == 0: # don't interact with stack at all when no replacements
                    tail = head + 1
                else: 
                    if len(zeros) == k: # move tail to next position after last zero
                        tail = zeros.popleft() + 1
                    zeros.append(head) # add current zero to stack
            else: # only calculate new max_len if current head is 1
                max_len = max(max_len, head - tail + 1) # do + 1 because current nums[head] is 1 too

            head += 1
        
        return max(max_len, head - tail) # head will be at len(nums), so no need to + 1
