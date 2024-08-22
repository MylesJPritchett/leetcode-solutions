# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def dfs_preorder(node):
            if not node:
                return
            
            output.append(node.val)
            dfs_preorder(node.left)
            dfs_preorder(node.right)
            
        output = []
        dfs_preorder(root)
        return output