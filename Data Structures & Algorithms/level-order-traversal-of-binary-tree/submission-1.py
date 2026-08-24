# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        result = []

        if not root:
            return []

        q.append(root)

        while q:
            len_q = len(q)
            level = []
            for i in range(len_q):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                result.append(level)
    
        return result

# Time: O(n) where n is number of nodes in tree
# Space: O(n)


