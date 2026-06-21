class Solution:
    def encode(self, strs: List[str]) -> str:
        S = ""
        for s in strs:
            S += str(len(s)) + "#" + s
        return S
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            si = i
            while s[si] != "#":
                si += 1
            length = int(s[i : si])
            S = s[si + 1 : length + si + 1]
            res.append(S)
            i = length + si + 1
        return res
            # "Hello","World" -> "5#Hello5#World"
            #           indexes  "012345678" words -> 23456
            # we need to use [:] cut to get words out of it
            