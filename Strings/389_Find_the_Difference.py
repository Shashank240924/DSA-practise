class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        #for storing result 
        res = 0
        # performing XOR Operation on string s
        for c in s:
            res ^= ord(c)
        # performing XOR Operation on string t     
        for c in t:
            res ^= ord(c)
         # returning the character that's not cancelled out after XOR operation
        return chr(res)   
