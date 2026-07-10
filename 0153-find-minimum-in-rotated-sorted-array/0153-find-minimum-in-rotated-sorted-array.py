
# Pattern: Modified Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:

        # Initialize the search range
        left, right = 0, len(nums) - 1

        # Continue searching until both pointers meet
        while left < right:

            # Find the middle index
            mid = left + (right - left) // 2

            # If mid element is smaller than the rightmost element,
            # the minimum lies in the left half (including mid)
            if nums[mid] < nums[right]:
                right = mid

            # Otherwise, the minimum lies in the right half
            # (excluding mid)
            else:
                left = mid + 1

        # Both pointers point to the minimum element
        return nums[left]