# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # traverse = deque([root])
        # depth = 0

        # if root is None:
        #     return 0

        # while len(traverse) >0:
        #     depth+=1
        #     i = len(traverse)
        #     while i >0:
        #         node = traverse.popleft()
        #         if node.left:
        #             traverse.append(node.left)
        #         if node.right: 
        #             traverse.append(node.right)
        #         i-=1

        # return depth

        if root is None:
            return 0

        l = 1+ self.maxDepth(root.left)
        r = 1+ self.maxDepth(root.right)

        return max(l,r)

        