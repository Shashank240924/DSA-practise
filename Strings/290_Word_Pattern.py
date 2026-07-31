class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words= s.split()
        if len(words) != len(pattern):
            return False 

        d = {}
        seen= set()
        for i,c in enumerate(pattern):
            if c not in d:
                if words[i] in seen:
                    return False
                d[c] = words[i] 
                seen.add(words[i])
            else:
                if d[c] != words[i]:
                    return False        
        return True  
