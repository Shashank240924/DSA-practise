# LeetCode: 33. Search in Rotated Sorted Array
# Pattern: Modified Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Initialize the search range
        left, right = 0, len(nums) - 1

        # Continue searching while the range is valid
        while left <= right:

            # Find the middle index
            mid = (left + right) // 2

            # Target found
            if nums[mid] == target:
                return mid

            # Check if the left half is sorted
            if nums[left] <= nums[mid]:

                # Target lies in the left sorted half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1

                # Otherwise search the right half
                else:
                    left = mid + 1

            # Right half is sorted
            else:

                # Target lies in the right sorted half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1

                # Otherwise search the left half
                else:
                    right = mid - 1

        # Target not found
        return -1
        
