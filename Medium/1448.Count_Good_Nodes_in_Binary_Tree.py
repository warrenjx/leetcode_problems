# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        good_ct = 0

        # iterative preorder traversal
        stack = deque() # format: (node, current max on path)
        stack.append((root, -10001))

        while stack: 
            curr, curr_max = stack.pop()
            
            # visit node
            if curr.val >= curr_max: 
                good_ct += 1
                curr_max = curr.val

            # append right first so it explores left path first
            if curr.right: 
                stack.append((curr.right, curr_max))
            if curr.left: 
                stack.append((curr.left, curr_max))
        
        return good_ct
