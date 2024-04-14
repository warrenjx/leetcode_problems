# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = deque()
        stack.append(root)

        sol = 0
        # keep track of previously visited node
        prev = None

        # do preorder traversal visiting left node first
        while stack: 
            curr = stack.pop()

            # if previous.left == current and no current children then it is a left child
            if prev and prev.left and (prev.left == curr) and not (curr.left or curr.right): 
                sol += curr.val
            
            prev = curr

            if curr.right: 
                stack.append(curr.right)
            if curr.left: 
                stack.append(curr.left)
        
        return sol
