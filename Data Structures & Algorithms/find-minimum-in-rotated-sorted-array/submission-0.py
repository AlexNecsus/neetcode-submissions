class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if n is rotating times that means moves the last n elements to the beginning
        return min(nums) 