class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = r = 0
        while l < len(haystack) and r < len(needle):
            start = l
            while l < len(haystack) and r < len(needle) and haystack[l] == needle[r]:
                l += 1
                r += 1
            if r == len(needle):
                return start
            l = start + 1
            r = 0
        return -1   
