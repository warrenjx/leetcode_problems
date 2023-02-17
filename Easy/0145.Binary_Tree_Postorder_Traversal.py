# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
    
        if not root: 
            return []
        
        sol = []

        stack = deque()
        stack.append(root)

        while stack: 
            curr = stack.pop()

            sol.append(curr.val)
            
            if curr.left: 
                stack.append(curr.left)
            if curr.right: 
                stack.append(curr.right)

        # kind of a band-aid patch because its basically a backwards pre-order
        return sol[::-1]