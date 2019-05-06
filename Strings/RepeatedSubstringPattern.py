class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not s:
            return False
        if(len(s) == 1):
            return False
        for i in range(1,(len(s)//2)+1):
            sub = s[0:i]
            if(len(s)//len(sub)*sub == s):
                return True
        return False