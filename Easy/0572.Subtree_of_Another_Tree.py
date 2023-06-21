# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        # idea: create a string representation of each tree and compare
        # format: ...(node value)N... where N is for Null
        main = ""
        sub = ""

        # do iterative dfs traversal of each tree 
        stack = deque()
        
        stack.append(root)
        while stack: 
            curr = stack.pop()

            if curr == None: 
                main += "N"
                continue
            else: 
                main += "(" + str(curr.val) + ")"
            
            stack.append(curr.right)
            stack.append(curr.left)
        
        stack.append(subRoot)
        while stack: 
            curr = stack.pop()

            if curr == None: 
                sub += "N"
                continue
            else: 
                sub += "(" + str(curr.val) + ")"
            
            stack.append(curr.right)
            stack.append(curr.left)
        
        # see if sub is a substring of the main
        return sub in main
