class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack and not needle:
            return 0
        if not needle:
            return 0
        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1