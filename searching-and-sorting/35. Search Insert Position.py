# LeetCode: 35. Search Insert Position
# Pattern: Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        # Initialize the search range
        left = 0
        right = len(nums) - 1

        # Perform Binary Search
        while left <= right:

            # Find the middle index
            mid = (left + right) // 2

            # Target found
            if nums[mid] == target:
                return mid

            # Search in the left half
            elif nums[mid] > target:
                right = mid - 1

            # Search in the right half
            else:
                left = mid + 1

        # Target not found.
        # 'left' is the correct position where target should be inserted.
        return left
