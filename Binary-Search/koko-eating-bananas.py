import math
from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)

        # if the hours is equal to length, you have to eat max each time
        if h == len(piles):
            return res
        
        # Min num of bananas you can eat is 1, max is the max in the array
        lowBound = 1
        upBound = res

        while lowBound <= upBound:
            mid = lowBound + (upBound - lowBound) // 2
            totalTime = 0
            # calc how much time it takes to eat each banana with mid
            for pile in piles:
                totalTime += math.ceil(pile / mid)
            # If its lower than h, than you can read just bounds to get lower min, otherwise try to find upper
            if totalTime <= h:
                res = mid
                upBound = mid - 1
            else:
                lowBound = mid + 1
        
        return res
