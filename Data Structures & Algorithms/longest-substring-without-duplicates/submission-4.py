class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l, r = 0, 1
        subs = s[l:r]
        res = 0
        while r < len(s):
            curr = s[r]
            if curr in subs:
                res = max(res, len(subs))
                l = r
            r+=1
            subs = s[l:r]     
        return res