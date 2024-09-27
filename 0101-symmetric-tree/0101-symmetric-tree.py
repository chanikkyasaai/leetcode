# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        return self.checkSymmetry(root.left, root.right)

    def checkSymmetry(self, left,right):
        if (left and not right) or (right and not left):
            return False
        elif not left and not right:
            return True
        elif left.val != right.val:
            return False
        
        return self.checkSymmetry(left.left, right.right) and self.checkSymmetry(left.right, right.left)