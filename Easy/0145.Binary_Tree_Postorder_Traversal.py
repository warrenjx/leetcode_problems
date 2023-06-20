# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        sol = []

        curr = root
        stack = deque()
        prev = None

        while True: 
            if curr: # first traverse down the left side of the tree
                stack.append(curr)
                curr = curr.left
            elif stack: 
                # once reached leftmost node, have 2 options
                curr = stack.pop()

                if curr.right == None or curr.right == prev: # if no right path, visit and continue
                    sol.append(curr.val)

                    prev = curr
                    curr = None
                else: # else traverse down right until no more
                    stack.append(curr)
                    curr = curr.right
            else: 
                break
        
        return sol

        # kind of a band-aid patch because its basically a backwards pre-order
        return sol[::-1]
