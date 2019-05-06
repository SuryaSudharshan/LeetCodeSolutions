class Solution:
    def reverseWords(self, s: str) -> str:
        lis = s.split(" ")
        new_str=""
        for j in lis:
            j = j[::-1]
            # print(j)
            new_str = new_str + " "+ j
        new_str = new_str.replace(" ", "",1)
        # new_str = new_str.strip()
        return new_str