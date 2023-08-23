class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        # variables which will be used in the stack
        rep = 0 # how many repetitions
        curr = "" # current pattern

        sol = ""
        
        times = 0 # placeholder for the repetitions if its multiple characters long

        for i in range(len(s)): 
            if s[i].isnumeric(): # parsing digits which will be the repetitions
                times *= 10
                times += int(s[i])
            elif s[i] == '[': # opening parentheses, new pattern start
                stack.append((rep, curr)) # store current pattern on stack to prepare for new one
                rep = times # update current repetition time
                # setup variables for future
                times = 0
                curr = ""
            elif s[i] == ']': # closing bracket, pattern complete
                n_rep, n_curr = stack.pop() # find old pattern to add on to

                for i in range(rep): # add pattern appropriate amount of times
                    n_curr += curr
                
                rep = n_rep # revert rep and curr to past ones
                curr = n_curr
            else: # just a part of a pattern
                curr += s[i]
        
        sol += curr

        return sol
