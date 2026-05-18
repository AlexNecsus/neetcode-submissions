class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        1'st idea: brute force, 2nd is: find considerable number and then start adding one while checking
        and while checking we'd like to count length of string and if its bigger than half return it.
        its enough to just count value if its consecutive or not.
        """
        # actully theres one more solution: sorting!
        if nums == []: return 0
        # iteration:
        collector = set()
        check = set(nums)
        count = 1
        for n in nums:
            if n - 1 in check:
                continue
            else:
                while n + 1 in check:
                    count += 1
                    n += 1
                collector.add(count)
                count = 1
        return max(collector)