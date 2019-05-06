class Solution(object):
    def isPalindrome(self, s):
        l = len(s)
        if l < 2:
            return True
        
        return True if s == s[::-1] else False
        
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # the whole string becomes palindrome by removing at most a char
        l = len(s)
        if l < 2:
            return True
        i = 0
        j = l - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return self.isPalindrome(s[i:j]) or self.isPalindrome(s[i+1:j+1])
        return True
#This is the leetcode solution
#This is my solution
# if not s:
#             return False
#         for i in range(0,len(s)):
#             new_s = s
#             new_s = s[:i]+s[i+1:]
#             if(new_s == new_s[::-1]):
#                 return True
#         return s == s[::-1]