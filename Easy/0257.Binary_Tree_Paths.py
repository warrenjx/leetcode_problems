# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = []

        # iterative dfs of tree
        stack = deque()
        # use string instead of list due to some not deep copy issues
        stack.append((root, ""))
        while stack: 
            curr, curr_path = stack.pop()
            
            # visit the node
            curr_path += str(curr.val) + "->"
            if not (curr.right or curr.left): 
                paths.append(curr_path)

            if curr.right: 
                stack.append((curr.right, curr_path))
            if curr.left: 
                stack.append((curr.left, curr_path))
        
        # strip the last arrow from each path
        for i in range(len(paths)): 
            paths[i] = paths[i].rstrip("->")

        return paths
