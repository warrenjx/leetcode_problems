# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # use a stack to traverse the tree by level
        q = deque()
        q.append(root)
        
        # idx to keep which level we are at
        idx = 0
        while q: 
            # traverse the level and store it in row
            width = len(q)
            row = []
            for _ in range(width): 
                curr = q.popleft()

                row.append(curr.val)

                if curr.left: 
                    q.append(curr.left)
                if curr.right: 
                    q.append(curr.right)

            if idx % 2 == 1: # if row is odd
                # make sure all terms are even and it is strictly decreasing
                if row[-1] % 2 == 1: 
                    return False
                for i in range(len(row) - 2, -1, -1): 
                    if row[i] % 2 == 1: 
                        return False
                    if row[i] <= row[i + 1]: 
                        return False
            else: # if row is even
                # make sure all terms are odd and it is strictly increasing
                if row[0] % 2 == 0: 
                    return False
                for i in range(1, len(row)): 
                    if row[i] % 2 == 0: 
                        return False
                    if row[i] <= row[i - 1]: 
                        return False

            # incrememnt index
            idx += 1
        
        # if it passes all checks
        return True
