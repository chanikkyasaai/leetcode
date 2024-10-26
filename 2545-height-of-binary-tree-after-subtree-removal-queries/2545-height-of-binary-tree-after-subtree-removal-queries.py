# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        @lru_cache(None)
        def height(node):
            if not node:
                return -1

            return 1 + max(height(node.left),height(node.right))

        dict1 = collections.defaultdict(int)

        def dfs(node,depth,max_val):
            if not node: return 

            dict1[node.val] = max_val

            dfs(node.left,depth+1,max(max_val,depth+1+height(node.right)))
            dfs(node.right,depth+1,max(max_val,depth+1+height(node.left)))

        dfs(root,0,0)

        return [dict1[i] for i in queries]