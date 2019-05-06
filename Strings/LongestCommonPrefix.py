class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            less = min(len(prefix), len(s))
            prefix = prefix[:less]
            for i in range(less):
                if prefix[i] != s[i]:
                    prefix = prefix[:i]
                    break
        return prefix
            