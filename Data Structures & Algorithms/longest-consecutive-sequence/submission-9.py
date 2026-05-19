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
        collector = 0
        check = set(nums)
        count = 1
        for n in check:
            if n - 1 in check:
                continue
            else:
                while n + 1 in check:
                    count += 1
                    n += 1
                if count >= len(nums) // 2:
                    return count
                collector = max(collector, count)
                count = 1
        return collector