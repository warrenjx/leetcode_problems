class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root: 
            return 0
        
        # do a level order traversal of tree, keep track of amount of levels traversed
        stack = deque()
        stack.append(root)

        height = 0

        width = 1
        while stack: 
            temp = 0
            for i in range(width): 
                curr = stack.popleft()
                if curr.right: 
                    stack.append(curr.right)
                    temp += 1
                if curr.left: 
                    stack.append(curr.left)
                    temp += 1
            
            width = temp
            height += 1
        
        return height
