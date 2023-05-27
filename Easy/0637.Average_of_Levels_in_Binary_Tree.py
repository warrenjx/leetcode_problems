# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        
        # level order traversal business
        sol = []
        stack = deque()

        stack.append(root)
        width = 1

        while stack: 
            next_width = 0
            tot = 0

            for i in range(width): 
                curr = stack.popleft()
                tot += curr.val
                if curr.left: 
                    stack.append(curr.left)
                    next_width += 1
                if curr.right: 
                    stack.append(curr.right)
                    next_width += 1
            
            sol.append(float(tot) / width)
            width = next_width

        return sol
