# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # def height(node):
        #     if not node:
        #         return 0
        #     return 1+ max(height(node.left), height(node.right))
        
        # if not root:
        #     return True
        
        # if abs(height(root.left) - height(root.right)) >1:
        #     return False
        # return self.isBalanced(root.left) and self.isBalanced(root.right)

        def dfs(node):
            if not node:
                return [True, 0]
            left, right = dfs(node.left), dfs(node.right)
            balanced = left[0] and right[0] and abs(left[1]-right[1]) <=1
            return [balanced, 1+max(left[1], right[1])]
        return dfs(root)[0]
