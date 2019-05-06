class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        s = s.translate(str.maketrans('', '', string.punctuation)).lower()
        s = s.strip().replace(' ', '')
        return s == s[::-1]