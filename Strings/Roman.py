class Solution:
    def romanToInt(self, s: str) -> int:
        new_s = s
        ans=0
        for i in range(0,len(s)//2):
            if "CM" in new_s:
                ans+= 900
                new_s = new_s.replace("CM","",1)
            if "CD" in new_s:
                ans+= 400
                new_s = new_s.replace("CD","",1)
            if "IV" in new_s:
                ans+= 4
                new_s = new_s.replace("IV","",1)
            if "IX" in new_s:
                ans+= 9
                new_s = new_s.replace("IX","",1)
            if "XL" in new_s:
                ans+= 40
                new_s = new_s.replace("XL","",1)
            if "XC" in new_s:
                ans+= 90
                new_s = new_s.replace("XC","",1)
        for i in range(0,len(new_s)):
            if(new_s[i]=='I'):
                ans+=1
            if(new_s[i]=='V'):
                ans+=5
            if(new_s[i]=='X'):
                ans+=10
            if(new_s[i]=='L'):
                ans+=50
            if(new_s[i]=='C'):
                ans+=100
            if(new_s[i]=='D'):
                ans+=500
            if(new_s[i]=='M'):
                ans+=1000
        return ans
            
                