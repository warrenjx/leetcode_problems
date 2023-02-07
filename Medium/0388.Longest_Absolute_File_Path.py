class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """

        # get all the different files with their depths
        input = input.split('\n')
        
        depths = []

        # tuple format (depth in file structure, length, actual text)
        for dir in input: 
            depth = 0
            fil = False
            while (dir[depth] == '\t'): 
                depth += 1
            
            if '.' in dir: 
                fil = True
            
            if (depth == 0): 
                depths.append((depth, len(dir), fil))
            else: 
                depths.append((depth, len(dir) - depth + 1, fil))

        stack = []
        sol = 0
        # stack builder
        for curr in depths: 
            while stack and curr[0] <= stack[-1][0]: 
                stack.pop()
            
            stack.append(curr)

            # only calculate sum if file is at end
            if stack and stack[-1][2]: 
                curr_sum = sum(map(lambda x: x[1], stack))

                if sol < curr_sum: 
                    sol = curr_sum

        return sol  