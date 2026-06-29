# LeetCode: 448. Find All Numbers Disappeared in an Array
# Pattern: HashSet
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        # Store all numbers in a HashSet for O(1) lookup
        seen = set(nums)

        # Stores the missing numbers
        res = []

        # Check every number from 1 to n
        for i in range(1, len(nums) + 1):

            # If the number is not present, it is missing
            if i not in seen:
                res.append(i)

        return res
