class Solution(object):
    def partition(self, s):
        sol = []

        stack = deque()
        # decision space, solution space
        stack.append((s, []))

        while stack: 
            ds, ans = stack.pop()

            # base case: decision space is empty, answer contains all palindrome partitions
            if not ds: 
                sol.append(ans)
                continue
            
            # generate next paths
            for i in range(1, len(ds) + 1): 
                # only generate path if a part is a palindrome
                if self.check(ds[:i]): 
                    # palindrome part is put in ans space, rest of string in ds 
                    stack.append((ds[i:], ans + [ds[:i]]))
        
        return sol

    
    # helper function to check if it is a palindrome
    def check(self, s): 
        if len(s) == 1: 
            return True
        
        for i in range(len(s) // 2): 
            if s[i] != s[-i - 1]: 
                return False
        
        return True
