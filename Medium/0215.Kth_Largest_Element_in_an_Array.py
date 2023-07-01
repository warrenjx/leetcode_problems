class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # create a min heap of size k
        heap = nums[0:k]
        heapify(heap)

        # add terms to k
        for i in range(k, len(nums)): 
            heappushpop(heap, nums[i])
        
        # heap[0] will always be the smallest term in heap
        return heap[0]
