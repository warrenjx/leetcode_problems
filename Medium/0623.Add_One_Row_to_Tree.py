# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """
        # edge case, need to insert at the top
        if depth == 1: 
            # create new root at the top and put old tree under it
            new_root = TreeNode(val=val, left=root)
            return new_root

        # perform a level order traversal
        q = deque()

        # indicates what row is currently being traversed
        row = 1
        q.append(root)
        while q: 
            # traverse a row
            width = len(q)
            for _ in range(width): 
                curr = q.popleft()

                if curr.left: 
                    q.append(curr.left)
                if curr.right: 
                    q.append(curr.right)
                
                # if current row is depth, add a new row for each child
                if row == depth - 1: 
                    tmp = curr.left
                    curr.left = TreeNode(val=val, left=tmp)
                    tmp = curr.right
                    curr.right = TreeNode(val=val, right=tmp)

            row += 1

        return root
