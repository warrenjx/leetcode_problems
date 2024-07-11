class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = deque()
        curr = ""

        for c in s: 
            if c == '(': # store currently held chars, new reverseable set is being made
                stack.append(curr)
                curr = ""
            elif c == ')': # reverse current set, add it to previous set
                curr = curr[::-1]
                curr = stack.pop() + curr
            else: # add current char to current set
                curr += c

        # all valid inputs should have equal amounts of closing parentheses, so curr should be accurate by the end
        return curr
