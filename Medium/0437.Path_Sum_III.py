# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        # edge case: no nodes, return 0
        if not root: 
            return 0

        # path holds the previous path sums
        path = []

        # use recursion rather than stack because its not tail recursion
        def dfs(curr, path_sum): 
            # add previous path sum to path
            path.append(path_sum)
            # update path_sum
            path_sum += curr.val

            # check to see if there are any combinations of path prefix sums that equal targetSum
            sol = 0
            for i in range(len(path)): 
                if path_sum - path[i] == targetSum: 
                    sol += 1

            # check neighbors
            if curr.left: 
                sol += dfs(curr.left, path_sum)
            if curr.right: 
                sol += dfs(curr.right, path_sum)
            
            # pop last sum off of path (path is basically global)
            path.pop()

            return sol

        return dfs(root, 0)
