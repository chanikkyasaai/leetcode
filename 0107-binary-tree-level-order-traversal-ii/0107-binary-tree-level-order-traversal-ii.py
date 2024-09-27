# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is  None:
            return []
        traversal = deque([root])
        ans = []

        while len(traversal) > 0:
            level = []
            i = len(traversal)
            while i > 0:
                node = traversal.popleft()
                if node:
                    level.append(node.val)
                if node.left:
                    traversal.append(node.left)
                if node.right:
                    traversal.append(node.right)
                i-=1
            ans.append(level)
            
        return ans[::-1]

            

         