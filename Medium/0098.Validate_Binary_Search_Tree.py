# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        stack = deque()
        curr = root
        first = True
        prev = 0

        # inorder traversal
        while True: 
            if curr: 
                stack.append(curr)
                curr = curr.left
            elif stack: 
                curr = stack.pop()

                # visit
                if first: 
                    prev = curr.val
                    first = False
                else: 
                    if curr.val <= prev: 
                        return False
                    prev = curr.val

                curr = curr.right
            else: 
                break

        return True
