# LeetCode: 347. Top K Frequent Elements
# Pattern: HashMap + Bucket Sort
# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Count the frequency of each number
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        # Bucket index = frequency
        # bucket[i] stores numbers that appear i times
        bucket = [[] for _ in range(len(nums) + 1)]

        # Place each number into its corresponding bucket
        for num, count in freq.items():
            bucket[count].append(num)

        res = []

        # Traverse buckets from highest frequency to lowest
        for i in range(len(bucket) - 1, 0, -1):

            for num in bucket[i]:
                res.append(num)

                # Stop after collecting k elements
                if len(res) == k:
                    return res
