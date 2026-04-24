class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        hashmap = {}
        for v in s:
            if v in hashmap:
                hashmap[v] += 1
            else:
                hashmap.update({v:1})
        hashmap1 = {}
        for n in t:
            if n in hashmap1:
                hashmap1[n] += 1
            else:
                hashmap1.update({n:1})
        return hashmap == hashmap1