# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pseudoPalindromicPaths (self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sol = 0
        self.path_ct = [0] * 10

        self.traverse(root)
        
        return self.sol

    def traverse(self, root): 
        self.path_ct[root.val] += 1

        if not root.left and not root.right: 
            odds = 0
            for ct in self.path_ct: 
                odds += ct & 1

            if odds <= 1: 
                self.sol += 1

        if root.left: 
            self.traverse(root.left)
        if root.right: 
            self.traverse(root.right)

        self.path_ct[root.val] -= 1
