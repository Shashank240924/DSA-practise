class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = defaultdict(int)
        n = len(nums) 
        nm = n // 2

        for n in nums:
            maj[n] += 1
        for key,value in maj.items():
            if value > nm:
                return key   

        