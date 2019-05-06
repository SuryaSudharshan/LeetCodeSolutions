class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        st = ransomNote
        for i in ransomNote:
            if i in magazine:
                st = st.replace(i,"",1)
                magazine = magazine.replace(i,"",1)
        if(len(st)==0):
            return True
        else:
            return False