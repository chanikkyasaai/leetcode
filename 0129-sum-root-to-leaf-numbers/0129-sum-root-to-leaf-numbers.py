# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.arr= []
        self.calcNum(root, [])

        return sum(self.arr)

    def calcNum(self,node,path):
        if node is None:
            return
        path.append(str(node.val))
        if not node.left and not node.right:
            self.arr.append(int("".join(path)))

        self.calcNum(node.left,path)
        self.calcNum(node.right,path)
        path.pop()


        
        


