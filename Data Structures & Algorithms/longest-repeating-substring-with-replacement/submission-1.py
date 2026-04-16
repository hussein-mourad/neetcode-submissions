class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        res = 0
        # freq = {}
        # for c in s:
        #     freq[c] = 1 + freq.get(c, 0)
        
        for i in range(n):
            a = s[i]
            curr_k = k
            size = 0
            for j in range(i, n):
                b = s[j]
                if a != b and curr_k == 0:
                    break
                if a == b:
                    size += 1
                elif curr_k != 0:
                        curr_k -= 1
                        size += 1
                res = max(res, size)
        return res


                    