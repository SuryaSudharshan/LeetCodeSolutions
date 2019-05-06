class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = S.split(" ")
        for i,k in enumerate(words):
            if k[0] in "AEIOUaeiou":
                words[i] = words[i] +"ma"+((i+1)*"a")
            else:
                words[i] = words[i][1:]+words[i][0]+"ma"+((i+1)*"a")
        return " ".join(words)