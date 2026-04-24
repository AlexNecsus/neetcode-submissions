class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        hashmap = {}
        for a, b in zip(s, t):
            hashmap[a] = hashmap.get(a, 0) + 1
            hashmap[b] = hashmap.get(b, 0) - 1
        return all(val == 0 for val in hashmap.values())