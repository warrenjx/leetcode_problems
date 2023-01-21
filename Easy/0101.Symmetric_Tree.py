class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # for handling trees height 2 or lower
        if root.left == None and root.right == None: 
            return True
        elif root.left == None or root.right == None: 
            return False

        # stack for left and right tree iterative traversal
        l_tree = deque()
        r_tree = deque()

        l_tree.append(root.left)
        r_tree.append(root.right)

        while l_tree or r_tree:
            l_curr = l_tree.pop()
            r_curr = r_tree.pop()

            if not (l_curr or r_curr): # empty spot in both trees
                continue
            elif not (l_curr and r_curr): # one tree has node other doesn't
                return False
            elif (l_curr.val != r_curr.val): # nodes not equal
                return False
            
            # right gets appended in opposite direction because mirrored
            l_tree.append(l_curr.left)
            l_tree.append(l_curr.right)

            r_tree.append(r_curr.right)
            r_tree.append(r_curr.left)
        
        return True