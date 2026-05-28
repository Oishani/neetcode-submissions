"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Initialize a map from old to new node.
        old_to_new = {}

        # Define inner DFS function and pass in node.
        def dfs(node):
            # If the node already exists in the map, return the cloned value from the map.
            if node in old_to_new:
                return old_to_new[node]
            # Else, create a new node with the original node's value and add it to the map.
            new_node = Node(node.val)
            old_to_new[node] = new_node
            # Then clone all the neighbors by
            # looping over the neighbors of the original node,
            for neighbor in node.neighbors:
                # calling DFS on each neighbor and appending the call result to the neighbors of the new node.
                new_node.neighbors.append(dfs(neighbor))
            # Return the new node at the end.
            return new_node

        # Return a DFS call on the node if node is not None, else return None.
        return dfs(node) if node else None

# Time: O(V + E)
# Space: O(V)


        