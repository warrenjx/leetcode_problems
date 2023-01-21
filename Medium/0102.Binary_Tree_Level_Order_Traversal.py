class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        # empty tree handler
        if root == None: 
            return []

        # deque for iterative traversa;
        stack = deque()
        stack.append(root)
        width = 1

        sol = []

        while stack: 
            row = []
            temp = 0

            # iterative traversal mechanism
            for i in range(0, width): 
                curr = stack.popleft()

                row.append(curr.val)

                if curr.left: 
                    stack.append(curr.left)
                    temp += 1
                if curr.right: 
                    stack.append(curr.right)
                    temp += 1
            
            width = temp
            sol.append(row)

        return sol