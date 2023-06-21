# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # find the upper and lower bounds
        min_val = min(p.val, q.val)
        max_val = max(p.val, q.val)

        # traverse BST until you find a term in between min and max
        while True: 
            if min_val <= root.val <= max_val: 
                return root
            elif root.val > max_val: 
                root = root.left
            else: 
                root = root.right
        
        return Nones
