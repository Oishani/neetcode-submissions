# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder = []

        def recurse(node):
            if not node:
                return 
            recurse(node.left)
            inorder.append(node.val)
            recurse(node.right)
        
        recurse(root)
        return inorder[k - 1]

# Time: O(n) where n is number of nodes
# Space: O(n)

