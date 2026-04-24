class Solution:
    # we need to encode strings so it has "#" special key and length of string
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s 
        return res
    def decode(self, s: str) -> List[str]:
        # we need to count length of string and then by using slicing iterate through them and add them to the result 
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            # important part of algorithm:
            length = int(s[i : j]) # counting length
            res.append(s[j + 1 : j + length + 1]) # appending string to a result
            i = j + 1 + length # updating i to be the start of the next string 
        return res