# LeetCode: 128. Longest Consecutive Sequence
# Pattern: HashSet
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Store all numbers in a HashSet for O(1) lookup
        nums_set = set(nums)

        # Stores the length of the longest sequence
        max_len = 0

        # Traverse every unique number
        for num in nums_set:

            # Start counting only if this number is
            # the beginning of a sequence
            if num - 1 not in nums_set:

                curr_num = num
                curr_len = 1

                # Continue until the sequence ends
                while curr_num + 1 in nums_set:
                    curr_num += 1
                    curr_len += 1

                # Update the maximum sequence length
                max_len = max(max_len, curr_len)

        return max_len
