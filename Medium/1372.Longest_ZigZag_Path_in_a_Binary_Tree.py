# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # format: [(node, if node was reached on a left branch, current path length), ...]
        stack = deque()

        # start stack with the left and right subtrees
        if root.left: 
            stack.append((root.left, True, 1))
        if root.right: 
            stack.append((root.right, False, 1))
        
        sol = 0
        while stack: 
            curr, was_left, curr_len = stack.pop()

            # check current path length at each node
            sol = max(sol, curr_len)

            # decide how to increment node
            if curr.left: # left branch
                if not was_left: # if reached left node on a right branch, zig zag maintained
                    stack.append((curr.left, True, curr_len + 1))
                else: # else restart path on current node
                    stack.append((curr.left, True, 1))
            if curr.right: # right branch
                if was_left: # if reached right node on a left branch, zig zag maintained
                    stack.append((curr.right, False, curr_len + 1))
                else: # else restart path on current node
                    stack.append((curr.right, False, 1))
        
        return sol
