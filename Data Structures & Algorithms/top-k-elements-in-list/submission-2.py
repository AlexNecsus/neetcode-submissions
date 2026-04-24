class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # creating a counter of repeateability
        # creating a list containing lists to put it in asceading order

        # So the idea of the best solution for this problem is using a list of 0 to len(nums),
        # and paste the number to occurences index, confusing but this is the main idea.
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res