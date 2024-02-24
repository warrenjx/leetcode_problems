class Solution(object):
    def findAllPeople(self, n, meetings, firstPerson):
        """
        :type n: int
        :type meetings: List[List[int]]
        :type firstPerson: int
        :rtype: List[int]
        """
        # sort meetings by time
        meetings.sort(key=lambda x: x[2])

        # group meetings by time slot
        groups = []
        cache = []
        curr_time = -1
        for x, y, time in meetings: 
            if time != curr_time: 
                if cache: 
                    groups.append((cache, curr_time))
                cache = []
                curr_time = time
            
            cache.append((x, y))
        
        if cache: 
            groups.append((cache, curr_time))

        # union[i] is the root of i, if 0 that means secret is shared
        union = [i for i in range(n)]
        union[firstPerson] = 0

        # all meets share the same time
        for meets, time in groups: 
            # union all meetings
            for x, y in meets: 
                self.join(x, y, union)
            
            for x, y in meets: 
                # check meeting roots
                rx = self.find(x, union)
                ry = self.find(y, union)

                if rx == 0 or ry == 0: # if one of the roots is 0, they know secret
                    union[x] = union[y] = 0
                else: # if none of the roots 0, functionally no meeting occurred
                    union[x] = x
                    union[y] = y

        # everyone with root 0 knows 0's secret
        sol = []
        for i in range(n): 
            if union[i] == 0: 
                sol.append(i)

        return sol

    # find function for union find
    def find(self, node, union): 
        while union[node] != node: 
            node = union[node]
        
        return node
    
    # join 2 nodes for union find
    def join(self, n1, n2, union): 
        r1 = self.find(n1, union)
        r2 = self.find(n2, union)

        if r1 == r2: 
            return

        if r1 == 0 or r2 == 0: # set to 0, because 0 is the secret spreader
            union[r1] = union[r2] = 0
        else: # set arbirarily if none 0
            union[r2] = r1

        return
    
