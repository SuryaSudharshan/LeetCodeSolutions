class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        if " " not in s:
            return len(s)
        return len(s.strip().split(" ")[-1])