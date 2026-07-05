# LeetCode: 49. Group Anagrams
# Pattern: HashMap + Frequency Count
# Time Complexity: O(n × k)
# Space Complexity: O(n × k)

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Dictionary to group anagrams
        # Key   -> Frequency tuple
        # Value -> List of anagrams
        groups = defaultdict(list)

        # Traverse every word
        for word in strs:

            # Count the frequency of each character (a-z)
            count = [0] * 26

            for ch in word:
                count[ord(ch) - ord('a')] += 1

            # Convert list to tuple because lists cannot be dictionary keys
            key = tuple(count)

            # Add the word to its corresponding group
            groups[key].append(word)

        # Return all grouped anagrams
        return list(groups.values())
