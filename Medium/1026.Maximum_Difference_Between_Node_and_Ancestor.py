# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ancestors = []
        self.diff = 0

        # check in a postorder traveral
        self.postorder(root, ancestors)

        return self.diff
        
    def postorder(self, root, ancestors): 
        # add current node to ancestors list
        ancestors.append(root.val)

        # visit children
        if root.left: 
            self.postorder(root.left, ancestors)
        if root.right: 
            self.postorder(root.right, ancestors)
        
        # remove node from ancestors list
        ancestors.pop()
        
        # check differences between ancestors
        for ancestor in ancestors: 
            self.diff = max(self.diff, abs(ancestor - root.val))
