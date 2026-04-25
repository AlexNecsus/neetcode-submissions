class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums: return list()
        zero_count = 0
        product = 1
        for n in nums:
            if n == 0:
                zero_count += 1
                continue
            product *= n
            
        for i in range(len(nums)):
            if zero_count == 1:
                if nums[i] == 0:
                    nums[i] = product
                else:
                    nums[i] = 0
            elif zero_count >= 2:
                return [0] * len(nums)
            else:
                nums[i] = product // nums[i]
        return nums