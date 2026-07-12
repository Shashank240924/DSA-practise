# LeetCode: 69. Sqrt(x)
# Pattern: Binary Search
# Time Complexity: O(log x)
# Space Complexity: O(1)

class Solution:
    def mySqrt(self, x: int) -> int:

        # Handle small values directly
        if x < 2:
            return x

        left, right = 1, x // 2
        answer = 0

        while left <= right:

            # Find the middle value
            mid = (left + right) // 2

            # Check the square of mid
            square = mid * mid

            if square == x:
                return mid

            # mid can be a possible answer,
            # but search for a larger valid value
            elif square < x:
                answer = mid
                left = mid + 1

            # Square is too large, search the left half
            else:
                right = mid - 1

        # Return the floor value of the square root
        return answer