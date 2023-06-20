# Iterative Solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2

        root = TreeNode(nums[mid])

        stack = deque() # format is (parent, left bound, right bound, is left tree)
        stack.append((root, left, mid - 1, True))
        stack.append((root, mid + 1, right, False))

        # build tree iteratively, by depth first
        while stack: 
            parent, left, right, is_left = stack.pop()

            if left > right: 
                continue
            
            mid = (left + right) // 2
            if is_left: 
                parent.left = TreeNode(nums[mid])
                stack.append((parent.left, left, mid - 1, True))
                stack.append((parent.left, mid + 1, right, False))
            else: 
                parent.right = TreeNode(nums[mid])
                stack.append((parent.right, left, mid - 1, True))
                stack.append((parent.right, mid + 1, right, False))

        return root

# Simple recursive solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        root = self.build_tree(nums)

        return root
    
    def build_tree(self, nums): 
        if not nums: 
            return None
        
        mid = len(nums) // 2
        root = TreeNode(nums[mid])

        root.left = self.build_tree(nums[0:mid])
        root.right = self.build_tree(nums[mid + 1:len(nums)])

        return root
