# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        output = []
        if not root:
            return output
        next_level = []
        next_level.append(root)
        while next_level:
            level_size = len(next_level)
            builder = []
            for i in range(0, level_size):
                node = next_level.pop(0)
                builder.append(node.val)
               

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                
            output.append(builder)   
        return output
            
        