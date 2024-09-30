# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.inordert = []
        self.top = -1
        self.inorder(root)
        for i in range(1, self.top):
            if self.inordert[i-1] >= self.inordert[i]:
                return False
        return True


    def inorder(self,node):
        if node is None:
            return
        if node.left is not None:
            self.inorder(node.left)

        self.top +=1
        self.inordert.append(node.val)
        
        if node.right is not None:
            self.inorder(node.right)

