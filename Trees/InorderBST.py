# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        stack = []
        def inorder(root: TreeNode,stack):
            if root:
                inorder(root.left,stack)
                stack.append(root.val)
                inorder(root.right,stack)
            return stack
        res = inorder(root,stack)
        ans = cur = TreeNode(None)
        for i in res:
            cur.right = TreeNode(i)
            cur = cur.right
        return ans.right