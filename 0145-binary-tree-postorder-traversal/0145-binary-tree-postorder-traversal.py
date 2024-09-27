# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        self.postorder(root)

        return self.ans

    def postorder(self, node):
        if node is None:
            return
        if node.left:
            self.postorder(node.left)
        if node.right:
            self.postorder(node.right)
        self.ans.append(node.val)
        return