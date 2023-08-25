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
        self.sol = None # will be set during dfs

        # do a postorder traversal of the tree
        self.dfs(root, p, q)

        return self.sol

    def dfs(self, curr, p, q): 
        seen = 0
        # visit neighbors first because its a postorder traversal
        if curr.left: 
            seen += self.dfs(curr.left, p, q)
        if curr.right: 
            seen += self.dfs(curr.right, p, q)

        if curr == p: # different numbers to know when both are found
            seen += 1
        elif curr == q: 
            seen += 2
        
        if seen == 3: # if 3, that means the 2 dfs above returned 1 and 2
            self.sol = curr
            # return -1 so no others match solution condition
            return -1

        return seen
