class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # convenience variable
        n = len(nums)

        # populate sol with junk value for debugging
        sol = [-1] * (n - k + 1)

        # q is a queue of terms in order of largest to smallest, q[0] is the current largest
        q = deque()
        # max_idx is the index of q[0] term
        max_idx = 0

        # iterate over nums, starting from 0 leads to a check later
        for i in range(n): 
            # append term so that it is less than all terms before it
            while q and q[-1] < nums[i]: 
                q.pop()
            
            q.append(nums[i])

            # only add term to sol if it is after the first k - 1 terms
            if i - max_idx + 1 == k: 
                # since q[0] contains largest
                sol[i - k + 1] = q[0]

                # if current max is largest, pop it to prepare for next round and increment index
                if q[0] == nums[max_idx]: 
                    q.popleft()
                
                max_idx += 1

        return sol
