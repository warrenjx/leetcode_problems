# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        sol = []

        # dfs and store path to target node
        path = []

        # dfs path nodes add nodes before target node to sol
        root = self.dfs(root, path, target.val)
        
        # set to prevent backtracking down target path
        path_vals = set()
        # obviously don't track down target path
        path_vals.add(target.val)
        
        # do a level order traversal from all nodes along path to get to target
        for i in range(1, min(len(path), k) + 1): 
            stack = deque()
            stack.append(path[-i])

            level = 0
            width = 1

            while stack: 
                next_width = 0

                for j in range(width): 
                    curr = stack.popleft()

                    # if current node is in the path, discard
                    if curr.val in path_vals: 
                        continue
                    # if it is the right depth for solution
                    if (level + i) - k == 0: 
                        sol.append(curr.val)
                    
                    if curr.left: 
                        stack.append(curr.left)
                        next_width += 1
                    if curr.right: 
                        stack.append(curr.right)
                        next_width += 1
                
                width = next_width
                level += 1

                # break early rather than full k depth because no need to go as far on path nodes
                if level + i > k: 
                    break
            
            path_vals.add(path[-i].val)

        # add nodes after target node to sol
        stack = deque()
        stack.append(root)

        level = 0
        width = 1

        # do a level order traversal and when level == k add nodes
        while stack: 
            next_width = 0

            for i in range(width): 
                curr = stack.popleft()

                if level == k: 
                    sol.append(curr.val)
                
                if curr.right: 
                    stack.append(curr.right)
                    next_width += 1
                if curr.left: 
                    stack.append(curr.left)
                    next_width += 1
            
            level += 1
            width = next_width

            # break after k as no need to go further
            if level > k: 
                break
        
        return sol
    
    # helper recursive dfs to build path list
    def dfs(self, node, path, target): 
        if node.val == target: 
            return node
        
        path.append(node)

        tar_node = None
        if node.left: 
            tar_node = self.dfs(node.left, path, target)
        if tar_node: 
            return tar_node

        if node.right: 
            tar_node = self.dfs(node.right, path, target)
        if tar_node: 
            return tar_node
        
        path.pop()

        return None
