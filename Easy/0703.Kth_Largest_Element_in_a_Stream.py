class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        # initialize priority queue as a min heap of max size k
        self.pq = nums[0:min(k, len(nums))]
        heapify(self.pq)

        # add the rest of elements, mainting size of k
        for i in range(k, len(nums)): 
            heappushpop(self.pq, nums[i])
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        # add new term to heap
        heappush(self.pq, val)

        # maintain heap size
        if len(self.pq) > self.k: 
            heappop(self.pq)
        
        return self.pq[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
