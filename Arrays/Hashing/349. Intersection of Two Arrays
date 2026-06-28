# LeetCode: 349. Intersection of Two Arrays
# Pattern: HashSet
# Time Complexity: O(n + m)
# Space Complexity: O(n)

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # Store all elements of nums1 for O(1) lookup
        seen = set(nums1)

        # Stores the common unique elements
        res = []

        # Traverse nums2
        for num in nums2:

            # If the number exists in nums1
            if num in seen:

                # Add it to the answer
                res.append(num)

                # Remove it to avoid duplicates
                seen.remove(num)

        return res
