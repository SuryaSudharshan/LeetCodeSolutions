# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        stack = []
        max_depth = 0
        stack.append((root,1))
        while(stack):
            curr_node, curr_depth = stack.pop()
            if(curr_node):
                max_depth = max(max_depth,curr_depth)
                for i in curr_node.children:
                    stack.append((i,curr_depth+1))
        return max_depth
            
        