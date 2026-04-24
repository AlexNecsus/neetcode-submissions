class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1. double arrays from start of opposite points till nums[i]
        # 2. we can use hashset incrementing values inside each time we see a new one
        final = []
        for i in range(len(nums)):
            l, r = 0, len(nums) - 1
            res = 1
            # we need to access values through index
            # then start multiplying values on each side and at last multiply and append at same time (l * r)
            while i != r:
                res *= nums[r]
                r -= 1
            while i != l:
                res *= nums[l]
                l += 1
            final.append(res)
        return final
                
                