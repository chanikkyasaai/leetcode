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
        self.valid = True
        self.inorder(root)
        # for i in range(1, len(self.inordert)):
        #     if self.inordert[i-1] >= self.inordert[i]:
        #         return False
        # return True
        

        return self.valid



    def inorder(self,node):
        if self.valid == False:
            return
        if node is None:
            return
        if node.left is not None:
            self.inorder(node.left)

        if self.top > -1 and self.inordert[self.top] >= node.val:
            self.valid = False
            return

        self.inordert.append(node.val)
        self.top+=1
        
        if node.right is not None:
            self.inorder(node.right)

