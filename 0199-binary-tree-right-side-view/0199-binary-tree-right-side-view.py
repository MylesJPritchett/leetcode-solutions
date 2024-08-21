# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        if not root:
            return output
        next_level = [root]
        while next_level:
            builder = []
            for i in range(0, len(next_level)):
                node = next_level.pop(0)
                builder.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                
            print(builder)
            output.append(builder[-1])
        return output