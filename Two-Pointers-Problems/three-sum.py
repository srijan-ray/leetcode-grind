from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort to make the problem similar to two sum part 2
        nums.sort()
        
        res: List[List[int]] = []
        
        for i, a in enumerate(nums):
            # Check for duplicate a value
            if i > 0 and a == nums[i - 1]:
                continue

            # two sum part 2 check with start starting right after a
            start = i + 1
            end = len(nums) - 1

            while start < end:
                # Check if condition is met
                if a + nums[start] + nums[end] == 0:
                    res.append([ a, nums[start], nums[end] ])
                    start += 1
                    end -= 1

                    # Search for next non duplicate start value
                    while nums[start] == nums[start - 1] and start < end:
                        start += 1

                # If the sum is greater than 0, then you need a smaller end number
                elif a + nums[start] + nums[end] > 0:
                    end -= 1
                # If the sum is less than 0, then you need a larger start number to increase the sum
                elif a + nums[start] + nums[end] < 0:
                    start += 1

        return res
