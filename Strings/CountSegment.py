class Solution:
    def countSegments(self, s: str) -> int:
        if not s:
            return 0
        li =[]
        for i in s.split(" "):
            if(len(i)> 0):
                li.append(i)
        return (len(li))