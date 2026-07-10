class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        counts = defaultdict(int)
        countt = defaultdict(int)
        for cs in s:
            counts[cs] += 1
        for ct in t:
            countt[ct] += 1
        return counts == countt
