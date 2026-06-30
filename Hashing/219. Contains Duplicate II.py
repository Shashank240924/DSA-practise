# LeetCode: 219. Contains Duplicate II
# Pattern: HashMap (Value → Last Seen Index)
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # Stores the last index of each number
        last_seen = {}

        # Traverse the array
        for i in range(len(nums)):

            # If number is already seen,
            # check the distance between indices
            if nums[i] in last_seen and i - last_seen[nums[i]] <= k:
                return True

            # Update the latest index of the current number
            last_seen[nums[i]] = i

        return False
