# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
class Solution:
    #Iterative Solution
    def postorder(self, root: 'Node'):
        if not root:
            return []
        res= []
        stack = [root]
        while(stack):
            n= stack.pop()
            for i in n.children:
                stack.append(i)
            res.append(n.val)
        return res[::-1]
    #Recursive Solution
    # def postorder(self, root: 'Node') -> List[int]:    
    #     res=[]
    #     res = self.dfs(root,res)
    #     return res
    # def dfs(self,root: 'Node',res):
    #     if not root:
    #         return res
    #     if root:
    #         for i in root.children:
    #             self.dfs(i,res)
    #         res.append(root.val)
    #     return res           
