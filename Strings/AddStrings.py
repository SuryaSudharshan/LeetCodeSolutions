class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if not num1:
            return num2
        if not num2:
            return num1
        int_num1 = ord(num1[0]) - 48
        int_num2 = ord(num2[0]) - 48
        if(len(num1)>1):
            for i in num1[1:]:
                int_num1 = int_num1*10+(ord(i)-48)
        if(len(num2)>1):
            for i in num2[1:]:
                int_num2 = int_num2*10+(ord(i)-48)
        total_sum = int_num1+int_num2
        if total_sum == 0:
            return "0"
        ans = ""
        while(total_sum!=0):
            total_sum,rem = divmod(total_sum,10)
            ans+= chr(rem+48)
        return ans[::-1]
        