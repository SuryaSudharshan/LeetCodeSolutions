import math
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        test = math.ceil(len(s)/(2*k))
        j =0
        for i in range(0,test):
            s = s.replace(s[j:j+k],s[j:j+k][::-1])
            j= j+(2*k)
        return s