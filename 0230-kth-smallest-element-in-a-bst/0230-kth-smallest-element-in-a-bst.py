# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # brute force way would be to add it all to an array and then sort it
        # better would be to order it first by the way we search and add each to array
        # even better would be to go left dfs first to stop when we reach it to not have to go through every node
        # to get it in order we need to use in order traversal (left, root, right)
        self.result = None
        self.count = 0
        def dfs(node):
            if not node or self.result is not None:
                return
            
            dfs(node.left)
            self.count += 1
            if self.count == k:
                self.result = node.val
                return
            dfs(node.right)
            
        
        dfs(root)
            
        return self.result
    
            
        
         