class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l, r = 0, 1
        subs = s[l:r]
        res = len(subs)
        while r < len(s):
            curr = s[r]
            if curr in subs:
                l = r
            r+=1
            subs = s[l:r]     
            res = max(res, len(subs))
        return res