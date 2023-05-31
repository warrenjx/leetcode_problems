# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root: 
            return []

        sol = []

        stack = deque()
        stack.append(root)
        width = 1

        # level order traversal of the binary tree
        while stack: 
            row = []
            next_width = 0
            for i in range(width): 
                curr = stack.popleft()

                if curr.left: 
                    stack.append(curr.left)
                    next_width += 1
                if curr.right: 
                    stack.append(curr.right)
                    next_width += 1

                row.append(curr.val)
            
            width = next_width
            # append last value of each row, it is the rightmost node
            sol.append(row[-1])
        
        return sol
