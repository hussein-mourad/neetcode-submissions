class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # freqs = {}
        # output=[]
        # for i, s in enumerate(strs):
        #     freq = {}
        #     for c in s:
        #         if c in freq:
        #             freq[c]+=1
        #         freq[c]=1
        #     freqs[i] = freq

        # for f in freqs:
        #     if
        # anagrams = {}
        # n = len(strs)
        # for i in range(n):
        #     s1 = strs[i]
        #     k = "".join(sorted(s1))
        #     if k in anagrams:
        #         if s1 not in anagrams[k]:
        #             anagrams[k].append(s1)
        #     else:
        #         anagrams[k] = [s1]
        #     for j in range(i + 1, n):
        #         s2 = strs[j]
        #         if sorted(s1) == sorted(s2):
        #             if s2 not in anagrams[k]:
        #                 anagrams[k].append(s2)
        #         elif s1 == s2:
        #             anagrams[k].append(s2)

        # return list(anagrams.values())

        anagrams = {}
        n = len(strs)
        for i in range(n):
            curr = strs[i]
            k = "".join(sorted(curr))
            if k in anagrams:
                continue
            anagrams[k] = [curr]
            for j in range(i + 1, n):
                s2 = strs[j]
                if sorted(curr) == sorted(s2):
                    anagrams[k].append(s2)
        return list(anagrams.values())

            
