# LeetCode: 169. Majority Element
# Pattern: HashMap (Frequency Count)
# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import defaultdict
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # Store the frequency of each number
        freq = defaultdict(int)

        # Majority element must appear more than n // 2 times
        limit = len(nums) // 2

        # Count the frequency of every number
        for num in nums:
            freq[num] += 1

        # Return the number whose frequency is greater than n // 2
        for num, count in freq.items():
            if count > limit:
                return num
