class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # hashtable with key as unique nums
        hash_table = {}
        for num in nums: 
            hash_table[num] = 0

        # value of keys is num of occurances
        for num in nums: 
            hash_table[num] += 1

        # turns dict into list of tupes sorted by number of occurances
        dic = sorted(hash_table.items(), key= lambda x: x[1], reverse= True)

        sol = []
        for i in range(0, k): 
            sol.append(dic[i][0])

        return sol