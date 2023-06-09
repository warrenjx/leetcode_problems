class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """

        # gets rid of edge case that messes up because next letter greater than target
        if letters[len(letters) - 1] <= target: 
            return letters[0]

        # gets rid of duplicates
        letters = list(set(letters))
        letters.sort()

        # standard binary search
        bot = 0
        top = len(letters) - 1
        while bot < top: 
            mid = (top + bot) / 2

            if letters[mid] == target: 
                if mid == len(letters) - 1: 
                    return letters[0]
                else:
                    return letters[mid + 1]
            elif target < letters[mid]: 
                top = mid
            else: 
                bot = mid + 1
        
        return letters[bot]
