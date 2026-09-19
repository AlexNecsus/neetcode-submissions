class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        check = set()
        cur = 0
        while nums[cur] not in check:
            if nums[cur] in check:
                return nums[cur]
            else:
                check.add(nums[cur])
            cur += 1
        return nums[cur]