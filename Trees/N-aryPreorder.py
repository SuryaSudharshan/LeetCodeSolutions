# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
class Solution:
    #Recursive solution
    def preorder(self, root: 'Node'):
        val=[]
        self.dfs(root,val)
        return val
    def dfs(self,root: 'Node',val):
        if root:
            val.append(root.val)
            for i in root.children:
                self.dfs(i,val)
        return val
    #Iterative solution
    # def preorder(self, root: 'Node'):
    #     if not root:
    #         return []
    #     ans = []
    #     stack = [root]
        
    #     while stack:
    #         n = stack.pop()
    #         ans.append(n.val)
    #         for child in n.children[::-1]:
    #             stack.append(child)
    #     return ans