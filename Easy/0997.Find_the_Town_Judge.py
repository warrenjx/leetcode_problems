class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        # initialize adjacency list
        adj_list = {}
        for i in range(1, n + 1): 
            adj_list[i] = set()
        
        # populate it with all the trusts
        for a, b in trust: 
            adj_list[a].add(b)

        # find if there is only 1 person who does not trust anyone
        chief = -1
        for person, trusts in adj_list.items(): 
            if not trusts: 
                if chief == -1: 
                    chief = person
                else: 
                    return -1
        
        # check if that person is trusted by everyone
        for person, trusts in adj_list.items(): 
            if person != chief: 
                if chief not in trusts: 
                    return -1

        return chief
