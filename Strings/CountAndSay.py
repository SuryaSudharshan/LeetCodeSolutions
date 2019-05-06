class Solution:
    def countAndSay(self, n: int) -> str:
        cas = "1"  #The first term of count-and-say sequence
        for i in range(n-1): #Each iteration generate one C-A-S sequence
            count = 0
            analysis = []  #Store the splited analysised nums
            for i in range(len(cas) - 1):
                count += 1
                if cas[i] != cas[i+1]:
                    analysis.append(str(count*10+int(cas[i]))) 
                    count = 0
            analysis.append(str((count+1)*10 + int(cas[-1]))) #For loop cannot reach the last analysised nums, so append it after for loop
            cas =  "".join(analysis) #Return the string as requirement
        return cas
#This is the leetcode solution