# LeetCode: 704. Binary Search
# Pattern: Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Initialize the search range
        left = 0
        right = len(nums) - 1

        # Continue searching while the range is valid
        while left <= right:

            # Find the middle index
            mid = (left + right) // 2

            # Target found
            if nums[mid] == target:
                return mid

            # Target is smaller, search the left half
            elif nums[mid] > target:
                right = mid - 1

            # Target is larger, search the right half
            else:
                left = mid + 1

        # Target not found
        return -1
