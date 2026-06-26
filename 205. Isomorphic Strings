# Pattern: HashMap (Two Dictionaries)
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        # Dictionary to map characters from s -> t
        mapST = {}

        # Dictionary to map characters from t -> s
        mapTS = {}

        # Traverse both strings together
        for i in range(len(s)):

            c1 = s[i]
            c2 = t[i]

            # If an existing mapping doesn't match,
            # the strings are not isomorphic
            if ((c1 in mapST and mapST[c1] != c2) or
                (c2 in mapTS and mapTS[c2] != c1)):
                return False

            # Store the mapping in both directions
            mapST[c1] = c2
            mapTS[c2] = c1

        # All mappings are valid
        return True
        
