class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = [c for c in s if c in "AEIOUaeiou"]
        res = []
        for i in s:
            if i in "AEIOUaeiou":
                res.append(vowels.pop())
            else:
                res.append(i)
        return "".join(res)