# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        stack = deque()
        curr = root
        ct = 0

        # inorder traversal of BST
        while True: 
            if curr: 
                stack.append(curr)
                curr = curr.left
            elif stack: 
                curr = stack.pop()

                # visit
                ct += 1
                if ct == k:
                    return curr.val

                curr = curr.right
            else: 
                break
        
        return 0
