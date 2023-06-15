# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        stack = deque()
        stack.append(root)
        width = 1

        sol = 0 
        max_sum = -1000000 # small number placeholder
        level = 1

        # do a level order traversal of the tree, calculating sum as you go
        while stack: 
            next_width = 0
            curr_sum = 0
            for i in range(width): 
                curr = stack.popleft()

                curr_sum += curr.val

                if curr.left: 
                    stack.append(curr.left)
                    next_width += 1
                if curr.right: 
                    stack.append(curr.right)
                    next_width += 1
            
            if curr_sum > max_sum: 
                max_sum = curr_sum
                sol = level
            
            width = next_width
            level += 1

        return sol
