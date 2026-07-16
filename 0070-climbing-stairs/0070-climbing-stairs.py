# LeetCode: 70. Climbing Stairs
# Pattern: Dynamic Programming (Space Optimized)
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def climbStairs(self, n: int) -> int:

        # Base cases
        if n <= 2:
            return n

        # Ways to reach step 1 and step 2
        first = 1
        second = 2

        # Calculate the number of ways for the remaining steps
        for _ in range(3, n + 1):
            first, second = second, first + second

        # second stores the answer for step n
        return second

        
        