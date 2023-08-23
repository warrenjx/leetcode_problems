class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        # initialize q with all the characters of senate
        q = deque()
        for char in senate: 
            q.append(char)
        
        # count determines how many senators have to be banned
        r_ct = 0
        d_ct = 0

        # go through rounds until an end condition is reached
        while True: 
            rd = len(q)

            # go through senate in rounds
            for i in range(rd): 
                curr = q.popleft()

                if curr == 'R': # radiant senator turn
                    if r_ct == 0: # can only vote if a D had not banned him before
                        q.append('R') # voted
                        d_ct += 1 # ban a D
                    else: # else just eat a D vote
                        r_ct -= 1
                elif curr == 'D': # dire senator turn
                    if d_ct == 0: # same process as R but reversed
                        q.append('D')
                        r_ct += 1
                    else: 
                        d_ct -= 1

            # when senators stop getting banned, break from loop
            if len(q) == rd:
                break

        # the remaining queue should have only 1 type of senator
        if q[0] == 'R': 
            return "Radiant"
        else: 
            return "Dire"
        
