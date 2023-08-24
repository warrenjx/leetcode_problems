# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        # variables for the leaf sequences 
        s_1 = []
        s_2 = []

        # stack to be used instead of recursion
        stack = deque()

        # dfs the first tree
        stack.append(root1)
        while stack:  
            curr = stack.pop()

            if not curr.right and not curr.left: 
                s_1.append(curr.val)
                continue
            
            if curr.right: 
                stack.append(curr.right)
            if curr.left: 
                stack.append(curr.left)
        
        # dfs the second tree
        stack.append(root2)
        while stack: 
            curr = stack.pop()

            if not curr.right and not curr.left: 
                s_2.append(curr.val)
                continue
            
            if curr.right: 
                stack.append(curr.right)
            if curr.left: 
                stack.append(curr.left)

        # if sequences are equal
        return s_1 == s_2
                
