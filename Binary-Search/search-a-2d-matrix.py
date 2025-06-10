# pyright: basic
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, (rows * cols) - 1

        while left <= right:
            mid = left + (right - left) // 2
            median = matrix[mid // cols][mid % cols]
            if target < median:
                right = mid - 1
            elif target > median:
                left = mid + 1
            else:
                return True

        return False
