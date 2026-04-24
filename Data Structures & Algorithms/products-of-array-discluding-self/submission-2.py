class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # the best of the best strategy here is to use prefix-postfix
        # iterate through value once, than update prefix and go through loop backwards
        pre = 1
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] *= pre
            pre *= nums[i]
        pre = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= pre
            pre *= nums[i]
        return res