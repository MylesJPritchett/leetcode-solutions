"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # try normal binary tree traversal, but guess it would be slightly different
        def dfs(node):
            if not node:
                return
            
            output.append(node.val)
            for n in range(0, len(node.children)):
                dfs(node.children[n])
                
        output = []
        dfs(root)
        return output