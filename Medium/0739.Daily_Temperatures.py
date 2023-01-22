class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        # standard stack stuff
        sol = [0] * len(temperatures)
        stack = []

        # loop iterates through temperatures forward, but stack effectively moves backwards
        for i, t in enumerate(temperatures): 
            # loop only happens while top of stack is less than current temperature
            while stack and temperatures[stack[-1]] < t: 
                # iterate through stack backwards
                curr = stack.pop()
                sol[curr] = i - curr
            
            # only on the stack if its sol entry is empty
            stack.append(i)

        return sol