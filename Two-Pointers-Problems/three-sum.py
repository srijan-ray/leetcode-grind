from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res: List[List[int]] = []
        
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            start = i + 1
            end = len(nums) - 1

            while start < end:
                if a + nums[start] + nums[end] == 0:
                    res.append([ a, nums[start], nums[end] ])
                    start += 1
                    end -= 1

                    while nums[start] == nums[start - 1] and start < end:
                        start += 1

                elif a + nums[start] + nums[end] > 0:
                    end -= 1
                elif a + nums[start] + nums[end] < 0:
                    start += 1

        return res
