# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        curr = root

        # basic binary tree search
        while curr: 
            if curr.val == val: # found, return the subtree
                return curr
            elif curr.val > val: # if larger, go left (smaller tree)
                curr = curr.left
            else: # if smaller, go right (larger tree)
                curr = curr.right
        
        return None
