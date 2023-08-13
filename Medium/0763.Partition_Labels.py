class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        # create hashmap representing the first and last occurance of each letter
        letters = {}

        for i in range(len(s)): 
            if s[i] in letters: # if letter seen again, update its last occurance
                letters[s[i]][1] = i
            else: # add letter to database
                letters[s[i]] = [i, -1] # -1 to represent if a letter is alone
        
        # sort intervals by starting term
        intervals = letters.values()
        intervals.sort(key = lambda x: x[0])

        # merged holds the length of each interval
        merged = []

        # initialize variables
        head = -1
        tail = 0

        # solve like merge intervals problem
        for i in range(len(intervals)): 
            if intervals[i][0] < head: # merge interval
                head = max(head, intervals[i][1])
            else: # new interval
                merged.append(head - tail + 1)
                
                tail = intervals[i][0]
                if intervals[i][1] == -1: # if its a single character, adjust head accordingly
                    head = intervals[i][0]
                else: 
                    head = intervals[i][1]
        
        merged.append(head - tail + 1)
        
        # return from 1 onwards because first term of merged is 0 because loop starts at 0 for simplicity
        return merged[1:]
        
