class Solution:
    def Rsearch(self, l, r, target, nums):
        if l > r: return -1
        m = l + ((r - l)// 2)
        if nums[m] > target:
            return self.Rsearch(l, m - 1, target, nums)
        elif nums[m] == target:
            return m
        else:
            return self.Rsearch(m + 1, r, target, nums)
    def search(self, nums: List[int], target: int) -> int:
        return self.Rsearch(0, len(nums) - 1, target, nums)