# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []

        self.performInorder(root)
        return self.ans
    
    def performInorder(self, node):
        if node is None:
            return
        if node.left:
            self.performInorder(node.left)
        self.ans.append(node.val)
        if node.right:
            self.performInorder(node.right)
        return