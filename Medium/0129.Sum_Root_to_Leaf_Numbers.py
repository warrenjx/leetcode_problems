# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sol = 0

        self.dfs(root, 0)

        return self.sol

    def dfs(self, node, curr_sum): 
        curr_sum *= 10
        curr_sum += node.val

        if node.left or node.right: 
            if node.left: 
                self.dfs(node.left, curr_sum)
            if node.right: 
                self.dfs(node.right, curr_sum)
        else: 
            self.sol += curr_sum
        
