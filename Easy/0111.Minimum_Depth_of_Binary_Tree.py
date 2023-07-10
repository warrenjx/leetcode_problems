# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # edge case, no tree at all
        if not root: 
            return 0

        stack = deque()
        stack.append(root)
        width = 1
        level = 1

        # level order traversal of tree with stack
        while stack: 
            next_width = 0

            for i in range(width): 
                curr = stack.popleft()

                # visit, first child node return level
                if not curr.left and not curr.right: 
                    return level

                if curr.left: 
                    stack.append(curr.left)
                    next_width += 1
                if curr.right: 
                    stack.append(curr.right)
                    next_width += 1
            
            level += 1
            width = next_width
        
        # should not be reached
        return -1
