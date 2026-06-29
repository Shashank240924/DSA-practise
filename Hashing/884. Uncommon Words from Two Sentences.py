# LeetCode: 884. Uncommon Words from Two Sentences
# Pattern: HashMap (Frequency Count)
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)

from collections import defaultdict

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        # Split both sentences into words
        words1 = s1.split()
        words2 = s2.split()

        # Store the frequency of every word
        freq = defaultdict(int)

        # Count words from the first sentence
        for word in words1:
            freq[word] += 1

        # Count words from the second sentence
        for word in words2:
            freq[word] += 1

        # Store uncommon words
        res = []

        # Words with frequency 1 are uncommon
        for word, count in freq.items():
            if count == 1:
                res.append(word)

        return res
