# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # iterative BFS of tree
        stack = deque()
        stack.append(root)

        leftmost = root
        width = 1

        while stack: 
            next_width = 0
            for i in range(width): 
                curr = stack.popleft()

                # check if node is leftmost in layer
                if i == 0: 
                    leftmost = curr.val
                
                if curr.left: 
                    stack.append(curr.left)
                    next_width += 1
                if curr.right: 
                    stack.append(curr.right)
                    next_width += 1
            
            width = next_width
        
        return leftmost
        