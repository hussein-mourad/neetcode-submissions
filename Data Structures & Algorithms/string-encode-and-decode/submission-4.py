class Solution:

    def encode(self, strs: List[str]) -> str:
        elem = "$%^&".join(strs)
        return elem + "*****" + len(strs)

    def decode(self, s: str) -> List[str]:
        n = s.split("*****")[1]
        if not n:
            return []
        return s.split("*****")[0].split('$%^&')