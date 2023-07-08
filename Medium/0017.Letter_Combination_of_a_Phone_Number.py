class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # handles edge case of 0
        if len(digits) == 0:
            return None

        sol = []

        stack = deque()
        # keep track of index and current string
        stack.append((0, ""))

        while stack: 
            idx, curr = stack.pop()

            # case for ending branch
            if idx == len(digits): 
                sol.append(curr)
                continue
            
            # branching out
            if   digits[idx] == "2": 
                stack.append((idx + 1, curr + "a"))
                stack.append((idx + 1, curr + "b"))
                stack.append((idx + 1, curr + "c"))
            elif digits[idx] == "3": 
                stack.append((idx + 1, curr + "d"))
                stack.append((idx + 1, curr + "e"))
                stack.append((idx + 1, curr + "f"))
            elif digits[idx] == "4": 
                stack.append((idx + 1, curr + "g"))
                stack.append((idx + 1, curr + "h"))
                stack.append((idx + 1, curr + "i"))
            elif digits[idx] == "5": 
                stack.append((idx + 1, curr + "j"))
                stack.append((idx + 1, curr + "k"))
                stack.append((idx + 1, curr + "l"))
            elif digits[idx] == "6": 
                stack.append((idx + 1, curr + "m"))
                stack.append((idx + 1, curr + "n"))
                stack.append((idx + 1, curr + "o"))
            elif digits[idx] == "7": 
                stack.append((idx + 1, curr + "p"))
                stack.append((idx + 1, curr + "q"))
                stack.append((idx + 1, curr + "r"))
                stack.append((idx + 1, curr + "s"))
            elif digits[idx] == "8": 
                stack.append((idx + 1, curr + "t"))
                stack.append((idx + 1, curr + "u"))
                stack.append((idx + 1, curr + "v"))
            elif digits[idx] == "9": 
                stack.append((idx + 1, curr + "w"))
                stack.append((idx + 1, curr + "x"))
                stack.append((idx + 1, curr + "y"))
                stack.append((idx + 1, curr + "z"))
        
        return sol
