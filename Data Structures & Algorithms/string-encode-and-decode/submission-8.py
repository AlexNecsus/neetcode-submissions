class Solution:
    # we need to encode strings so it has "#" special key and length of string
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        # we need to count length of string and then by using slicing iterate through them and add them to the result 
        # now we have this "5#hello5#world" -> so we need to decode this. or we can use non ascii char.
        # strat: find length of string, get slice of it and then append it to our list regarding update of i.
        # "5#hello5#world"
        i, res = 0, []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return res