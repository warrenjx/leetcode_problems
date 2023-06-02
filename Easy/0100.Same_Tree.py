# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if not p and not q: 
            return True

        p_stack = deque()
        q_stack = deque()

        p_stack.append(p)
        q_stack.append(q)

        # preorder traversal
        while p_stack and q_stack: 
            p_curr = p_stack.pop()
            q_curr = q_stack.pop()
            
            if not p_curr and not q_curr: # both null
                continue
            elif not p_curr or not q_curr: # one is not null
                return False
            else: # both not null
                if p_curr.val != q_curr.val: 
                    return False

                # append all children even if null
                #   this is the important change from normal BFS
                p_stack.append(p_curr.left)
                p_stack.append(p_curr.right)

                q_stack.append(q_curr.left)
                q_stack.append(q_curr.right)
        
        if p_stack or q_stack: 
            return False

        return True
