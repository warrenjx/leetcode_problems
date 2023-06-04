# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        if not root: 
            return root
        
        stack = deque()
        stack.append(root)

        # iterative traversal of binary tree
        while stack: 
            curr = stack.popleft()

            if curr.left: 
                stack.append(curr.left)
            if curr.right: 
                stack.append(curr.right)
            
            # visit by swapping the left and right nodes
            curr.right, curr.left = curr.left, curr.right
        
        return root
