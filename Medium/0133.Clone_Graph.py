"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        # edge case: no graph
        if not node: 
            return None
        
        # dictionary mapping node values to the new node
        seen = {}

        stack = deque()
        stack.append(node)

        # iteratively create the graph as you traverse the base graph
        while stack: 
            curr = stack.popleft()

            # either create new node based on current, or retrieve already created one
            new_node = None
            if curr.val in seen: 
                new_node = seen[curr.val]
            else: 
                new_node = Node(curr.val)
                # store created node
                seen[curr.val] = new_node
            
            for neighbor in curr.neighbors: 
                # either create new node for its neighbor or retrieve already created one
                new_neigh = None
                if neighbor.val in seen: 
                    new_neigh = seen[neighbor.val]
                else: 
                    new_neigh = Node(neighbor.val)
                    # store created neighbor
                    seen[neighbor.val] = new_neigh
                    # only branch when it is unvisited, to avoid infinite looping
                    stack.append(neighbor)

                new_node.neighbors.append(new_neigh)

        return seen[node.val]
  
