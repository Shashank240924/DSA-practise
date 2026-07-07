# LeetCode: 75. Sort Colors
# Pattern: Counting Sort
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Count the occurrences of 0, 1, and 2
        counts = [0, 0, 0]

        for color in nums:
            counts[color] += 1

        # Number of Red(0), White(1), and Blue(2)
        red, white, blue = counts

        # Fill the array with all 0's
        nums[:red] = [0] * red

        # Fill the array with all 1's
        nums[red:red + white] = [1] * white

        # Fill the remaining positions with 2's
        nums[red + white:] = [2] * blue
