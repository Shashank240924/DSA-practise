# LeetCode: 389. Find the Difference
# Pattern: HashMap (Frequency Count)
# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import defaultdict

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        # Store the frequency of characters in s
        freq = defaultdict(int)

        for ch in s:
            freq[ch] += 1

        # Traverse t and decrease the frequency
        for ch in t:
            freq[ch] -= 1

            # If frequency becomes negative,
            # this is the extra character
            if freq[ch] < 0:
                return ch
