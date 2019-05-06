# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        val_to_check = root.val
        if(root.left == None and root.right == None):
            return True
        if(root.left == None and root.right.val == val_to_check):
            proceed = self.isUnivalTree(root.right)
            return proceed
        if(root.left == None and root.right.val != val_to_check):
            return False
        if(root.left.val == val_to_check and root.right == None):
            proceed = self.isUnivalTree(root.left)
            return proceed
        if(root.left.val != val_to_check and root.right == None):
            return False
        if(root.left.val == val_to_check and root.right.val == val_to_check):
            proceed = self.isUnivalTree(root.left)
            proceed2 = self.isUnivalTree(root.right)
            return (proceed and proceed2)
        if(root.left.val != val_to_check or root.right.val != val_to_check):
            return False

# Leetcode DFS Solution:
# class Solution(object):
#     def isUnivalTree(self, root):
#         vals = []
#         def dfs(node):
#             if node:
#                 vals.append(node.val)
#                 dfs(node.left)
#                 dfs(node.right)
#         dfs(root)
#         return len(set(vals)) == 1
        
        
        