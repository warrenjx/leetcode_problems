# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root: 
            return False

        stack = deque() # format: (node, sum val)
        stack.append((root, 0))

        # iterative preorder traversal keeping track of sum at each node
        while stack: 
            curr, tot = stack.pop()

            tot += curr.val
            # only return True if end of path is a leaf node, thus no children
            if tot == targetSum and not (curr.right or curr.left): 
                return True

            if curr.right: 
                stack.append((curr.right, tot))
            if curr.left: 
                stack.append((curr.left, tot))
        
        return False
