class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for c in "!?',;.": paragraph = paragraph.replace(c, " ")
        words = paragraph.lower().split(" ")
        for i in words:
            if i.lower() in banned:
                words = list(filter(lambda a: a!= i,words))
        words = list(filter(lambda a: a!= "",words))
        frequency = collections.Counter(words)
        for word,freq in frequency.most_common(1):
            return ("%s" %(word))