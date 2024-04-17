# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        # stores the solution
        self.sol = None
        # current string of characters on the path
        self.curr = []

        # call dfs on the root (postorder)
        self.dfs(root)

        return self.sol
        
    def dfs(self, node): 
        # add current node to the path
        self.curr.append(chr(ord('a') + node.val))

        # check out current node children
        if node.left: 
            self.dfs(node.left)
        if node.right: 
            self.dfs(node.right)
        
        # visit if node is a leaf node
        if not (node.left or node.right):
            # compress path into a string in the correct order 
            string = "".join(self.curr[::-1])
            # compare against the current smallest
            if not self.sol or string < self.sol: 
                self.sol = string

        # done with node, remove it from the path
        self.curr.pop()
