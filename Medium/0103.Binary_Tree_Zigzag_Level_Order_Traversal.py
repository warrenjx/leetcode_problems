class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None: 
            return []
        
        # pretty much same code as 102
        sol = []
        stack = deque()
        stack.append(root)

        # used to append to rows in reverse for every other
        rev = False
        
        while stack: 
            row = []
            
            length = len(stack)
            
            for i in range(length): 
                curr = stack.popleft()
            
                if curr.left: 
                    stack.append(curr.left)
                if curr.right: 
                    stack.append(curr.right)
            
                row.append(curr.val)
            
            # mechanism difference compared to 102
            if rev: 
                sol.append(row[::-1])
                rev = False
            else: 
                sol.append(row)
                rev = True
        
        return sol