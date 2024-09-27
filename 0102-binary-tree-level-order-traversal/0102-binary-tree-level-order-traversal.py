# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        traverse = deque([root])
        ans = []

        while len(traverse) > 0:
            i = len(traverse)
            level = []
            while i >0:
                node = traverse.popleft()
                if node:
                    level.append(node.val)
                if node.left:
                    traverse.append(node.left)
                if node.right:
                    traverse.append(node.right)
                i-=1
            ans.append(level)
        
        return ans





