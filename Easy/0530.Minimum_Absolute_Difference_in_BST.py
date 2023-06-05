# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        stack = deque()
        curr = root
        prev = -100000
        sol = 100000

        # iterative BST inorder traversal
        while True: 
            # going to the leftmost node at any point
            if curr: 
                stack.append(curr)
                curr = curr.left
                continue
            # no more left, have to visit and go right
            elif stack: 
                curr = stack.pop()

                # visit
                sol = min(sol, abs(curr.val - prev))
                prev = curr.val

                curr = curr.right
            else: 
                break

        return sol
