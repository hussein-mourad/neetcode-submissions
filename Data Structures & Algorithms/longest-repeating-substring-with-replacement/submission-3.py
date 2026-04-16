class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        res = 0
        
        for i in range(n):
            count, max_count = {}, 0
            for j in range(i, n):
                curr = s[j]
                count[curr] = 1 + count.get(curr, 0)
                max_count = max(max_count, count[curr])
                length = j - i + 1
                if length - max_count <= k:
                    res = max(res, length)
        return res


                    