# LeetCode: 34. Find First and Last Position of Element in Sorted Array
# Pattern: Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # Finds either the first or last occurrence of target
        def binarySearch(find_first):
            left, right = 0, len(nums) - 1
            position = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    # Store the current target position
                    position = mid

                    if find_first:
                        # Continue searching toward the left
                        right = mid - 1
                    else:
                        # Continue searching toward the right
                        left = mid + 1

                elif nums[mid] < target:
                    left = mid + 1

                else:
                    right = mid - 1

            return position

        # Find the first and last occurrence
        first = binarySearch(True)
        last = binarySearch(False)

        return [first, last]