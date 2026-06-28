from collections import defaultdict

class Solution:
    def findLucky(self, arr: List[int]) -> int:

        # Store the frequency of each number
        freq = defaultdict(int)

        for num in arr:
            freq[num] += 1

        ans = -1

        # Check every unique number
        for num in freq:

            # If value equals frequency
            if num == freq[num]:
                ans = max(ans, num)

        return ans
