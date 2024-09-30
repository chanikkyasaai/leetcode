# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        self.ans = []
        self.computepaths(root,[], targetSum)
        return self.ans

    def computepaths(self,node,path, remainingsum):
        if node is None:
            return
        path.append(node.val)
        if not node.left and not node.right and node.val == remainingsum:
             self.ans.append(list(path))
        
        self.computepaths(node.left,path,remainingsum - node.val)
        self.computepaths(node.right,path,remainingsum - node.val)

        path.pop()
