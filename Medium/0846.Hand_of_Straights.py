class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        n = len(hand)

        # edge case: if hand cannot be split into even groups of groupsize
        if n % groupSize != 0: 
            return False

        # build hashmap containing all elements and their frequencies
        hashmap = {}
        for num in hand: 
            if num in hashmap: 
                hashmap[num] += 1
            else: 
                hashmap[num] = 1
        
        # nums represents all the unique elements in the hand
        nums = hashmap.keys()
        nums.sort()

        # build groups repeatedly
        while nums: 
            # curr is the start of a group
            curr = nums[0]

            # build a group
            for i in range(groupSize): 
                if curr in hashmap: # if you can build group
                    hashmap[curr] -= 1

                    if hashmap[curr] <= 0: 
                        hashmap.pop(curr)
                        nums.remove(curr)
                else: # can't build group
                    return False
                
                curr += 1
        
        return True
