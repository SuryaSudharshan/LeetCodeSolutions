class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        letters = [c for c in S if c.isalpha()]
        res = []
        for c in S:
            if c.isalpha():
                res.append(letters.pop())
            else:
                res.append(c)
        return "".join(res)
#This is the Leetcode solution