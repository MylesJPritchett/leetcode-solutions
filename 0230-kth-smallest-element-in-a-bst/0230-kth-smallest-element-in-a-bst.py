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
        def dfs(node):
            if not node:
                return None
            
            dfs(node.left)
            array.append(node.val)
            dfs(node.right)
            
        array = []
        dfs(root)
        print(array)
        # while len(array) < k:
            
        return array[k-1]
    
            
        
         