# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = deque()
        curr = root
        prev = None
        
        # iterative postorder traversal of binary tree
        while True: 
            if curr: 
                stack.append(curr)
                curr = curr.left
            elif stack: 
                curr = stack.pop()

                if curr.right == None or curr.right == prev: 
                    # calculate height
                    if not curr.left and not curr.right: 
                        curr.val = 1
                    elif curr.left and curr.right: 
                        curr.val = max(curr.right.val, curr.left.val) + 1
                    elif curr.left:
                        curr.val = curr.left.val + 1
                    else: 
                        curr.val = curr.right.val + 1

                    # calculate balance
                    left = 0
                    right = 0
                    if curr.left: 
                        left = curr.left.val
                    if curr.right: 
                        right = curr.right.val

                    # determine if it is unbalanced
                    if abs(left - right) > 1: 
                        return False

                    prev = curr
                    curr = None
                else: 
                    stack.append(curr)
                    curr = curr.right
            else:
                break
        
        return True
