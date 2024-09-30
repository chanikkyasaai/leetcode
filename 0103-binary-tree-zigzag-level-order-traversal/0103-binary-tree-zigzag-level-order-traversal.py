# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        ans = []
        traverse = deque([root])
        zigzag = False

        while len(traverse) > 0:
            i = len(traverse)
            level = []
            while i > 0:
                x = traverse.popleft()
                level.append(x.val)
                if x.left is not None:
                    traverse.append(x.left)
                if x.right is not None:
                    traverse.append(x.right)
                i-=1

            if zigzag == False:
                ans.append(level)
                zigzag = True
            elif zigzag == True:
                ans.append(reversed(level))
                zigzag = False
        
        return ans
