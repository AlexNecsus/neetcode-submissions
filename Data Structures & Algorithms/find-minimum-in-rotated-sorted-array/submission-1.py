class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if n is rotating times that means moves the last n elements to the beginning.
        # O(log n) time required, its basically writing your own min() function
        # list has been rotated between 1 and n times
        # I am thinking abt doing first guess random and then doin l, r, m  algo.
        if nums[0] == min(nums): return nums[0]
        # the problem with this solution , it takes memory to create these instead of keeping it O(1)
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] < min(nums):
                l = m + 1
            elif nums[m] > min(nums):
                r = m - 1
            else: 
                return nums[m]
        return min(nums)