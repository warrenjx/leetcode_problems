# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = deque()
        curr = root
        prev = None

        max_len = 0
        
        # iterative postorder traversal of tree
        while True: 
            if curr: 
                stack.append(curr)
                curr = curr.left
            elif stack: 
                curr = stack.pop()

                if curr.right == None or curr.right == prev: 
                    curr_len = 0

                    # calculate the height of current node
                    # also calculate the largest diameter from this node
                    if not curr.right and not curr.left: 
                        curr.val = 1
                    elif curr.right and curr.left: 
                        curr.val = max(curr.right.val, curr.left.val) + 1
                        curr_len += curr.right.val + curr.left.val
                    elif curr.left: 
                        curr.val = curr.left.val + 1
                        curr_len += curr.left.val
                    else: 
                        curr.val = curr.right.val + 1
                        curr_len += curr.right.val
                    
                    max_len = max(max_len, curr_len)

                    prev = curr
                    curr = None
                else: 
                    stack.append(curr)
                    curr = curr.right
            else: 
                break
        
        return max_len
