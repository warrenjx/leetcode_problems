# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root: 
            return []

        sol = []
        stack = deque()
        
        while stack or root: 
            if root: # go to leftmost child of parent
                stack.append(root)
                root = root.left
            else: # visit node, then go right one
                root = stack.pop()
                sol.append(root.val)
                root = root.right
        
        return sol
        
