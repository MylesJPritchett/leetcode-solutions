"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def dfs(node):
            if not node:
                return
            for n in range(0, len(node.children)):
                dfs(node.children[n])
            
            output.append(node.val)
            
        output = []
        dfs(root)
        return output