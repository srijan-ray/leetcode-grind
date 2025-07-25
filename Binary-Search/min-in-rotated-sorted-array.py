# pyright: basic
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        res = nums[0]

        while left <= right:
            mid = left + (right - left) // 2

            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
            
            res = min(res, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1

        return res

