class Solution:
    # encode is easy but decode is trickier
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += s + "水"
        return res
    def decode(self, s: str) -> List[str]:
        # we can use nonASCII characters. or len + some key
        res = []
        tmp = ""
            
        for i in range(len(s)):
            if s[i] == "水":
                res.append(tmp)
                tmp = ""
                continue
            else:
                tmp += s[i]
        if tmp != "":
            res.append(tmp)
        return res