class Solution:

    def encode(self, strs: List[str]) -> str:
        elem = "$%&".join(strs)
        return elem + "$*$" + str(len(strs))

    def decode(self, s: str) -> List[str]:
        n = int(s.split("$*$")[1])
        elems = s.split("$*$")[0].split('$%&')
        if not n:
            return []
        return elems