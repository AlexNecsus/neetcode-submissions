class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # so we need to find the best way to make all characters distinct to their neighbors
        count = {}
        res = 0
        maxf = 0 #opt
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k: # max(count.values())
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res