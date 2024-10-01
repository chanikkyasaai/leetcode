# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        self.pretr = []
        self.preorder(root)
        prev = None
        for node in self.pretr:
            node.left = None
        for i in range(len(self.pretr) +1):
            if i+1 < len(self.pretr):
                self.pretr[i].right = self.pretr[i+1]

        return
    def preorder(self, node):
        if node is None:
            return
        self.pretr.append(node)
        self.preorder(node.left)
        self.preorder(node.right)

    
        