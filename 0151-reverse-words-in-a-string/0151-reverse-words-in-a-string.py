class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        wrds = []
        
        wrds = s[::-1] 
        return " ".join(wrds)