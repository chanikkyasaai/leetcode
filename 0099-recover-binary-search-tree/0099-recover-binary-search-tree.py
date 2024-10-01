# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.arr = []

        self.inorder(root)
        self.arr.sort()
        self.i=0

        self.insert(root)


    def inorder(self,node):
        if node is None:
            return
        self.inorder(node.left)
        self.arr.append(node.val)
        self.inorder(node.right)

    def insert(self, node):
        if node is None:
            return
        self.insert(node.left)
        node.val = self.arr[self.i]
        self.i+=1
        self.insert(node.right)


    


        

        