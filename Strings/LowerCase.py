class Solution:
    def toLowerCase(self, str: str) -> str:
        for i in range(0,len(str)):
            # print(ord(str[i]))
            if(ord(str[i])<= 90 and ord(str[i])>=65):
                num = ord(str[i])
                num+=32
                str = str.replace(str[i],chr(num))
        return str