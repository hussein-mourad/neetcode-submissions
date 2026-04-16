class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        res = 0
        freq = {}
        l = 0
        maxf = 0
        for r in range(n):
            curr = s[r]
            freq[curr] = 1 + freq.get(curr, 0)
            maxf = max(maxf, freq[curr])
            while (r - l + 1) - maxf > k:
                freq[s[l]] -= 1
                l+=1
            res = max(res, r - l + 1)
        return res


                    