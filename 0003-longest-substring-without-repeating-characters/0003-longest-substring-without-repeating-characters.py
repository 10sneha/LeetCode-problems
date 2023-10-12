class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxlength = 0
        charmap = {}
        left = 0

        for right in range(n):
            if s[right] in charmap and charmap[s[right]] >= left:
                left = charmap[s[right]] + 1
            charmap[s[right]] = right
            maxlength = max(maxlength, right-left+1)

        return maxlength
        