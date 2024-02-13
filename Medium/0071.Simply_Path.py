class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # split tokens into more digestable 
        tokens = path.split('/')

        stack = deque()
        # iterate through the path
        for token in tokens: 
            if not token: # repeated '/'
                continue
            elif token == "..": # need to go back a level
                if not stack: # cant go back more than root
                    continue
                else: # go back a level
                    stack.pop()
            elif token == ".": # stay in directory
                continue
            else: # add token to path
                stack.append(token)
        
        # convert stack to string path
        sol = ""
        while stack: 
            sol += "/" + stack.popleft()

        if not sol: # empty path
            return "/"
        else: # nonempty path
            return sol
