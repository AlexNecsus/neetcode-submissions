class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in matrix:
            if target <= m[-1]:
                for i in m:
                    if i == target:
                        return True
        return False