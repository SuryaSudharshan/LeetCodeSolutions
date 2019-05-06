class Solution:
    def checkRecord(self, s: str) -> bool:
        absence_test = s.replace('A',"",1)
        if 'A' in absence_test:
            return False
        if 'LLL' in s:
            return False
        return True