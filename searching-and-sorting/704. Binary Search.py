"""
LeetCode: 704. Binary Search

Problem:
Given a sorted array of integers `nums` in ascending order and a target value,
return the index of the target if it exists. Otherwise, return -1.

Approach:
- Use Recursive Binary Search.
- Compare the target with the middle element.
- If the target is smaller, search the left half.
- If the target is larger, search the right half.
- Continue recursively until the target is found or the search space becomes empty.

Time Complexity:
O(log n)
- The search space is reduced by half in each recursive call.

Space Complexity:
O(log n)
- Recursive calls use the call stack.
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Searches for the target element in a sorted array.

        Parameters:
        nums (List[int]): Sorted list of integers.
        target (int): Value to search for.

        Returns:
        int: Index of the target if found, otherwise -1.
        """

        def binarySearch(left: int, right: int) -> int:
            """
            Performs recursive binary search.

            Parameters:
            left (int): Left boundary of the search.
            right (int): Right boundary of the search.

            Returns:
            int: Index of the target if found, otherwise -1.
            """

            # Base case: target not found
            if left > right:
                return -1

            # Find the middle index
            mid = (left + right) // 2

            # Target found
            if nums[mid] == target:
                return mid

            # Search the right half
            elif nums[mid] < target:
                return binarySearch(mid + 1, right)

            # Search the left half
            else:
                return binarySearch(left, mid - 1)

        # Start searching from the entire array
        return binarySearch(0, len(nums) - 1)