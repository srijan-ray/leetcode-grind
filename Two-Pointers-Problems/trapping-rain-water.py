from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        # if height is empty, return 0 for max area
        if not height:
            return 0

        leftBound, rightBound = 0, len(height) - 1
        leftMax, rightMax = height[leftBound], height[rightBound]

        res = 0
        while leftBound < rightBound:
            # if leftMax is greater than right max, increment leftBound
            if leftMax < rightMax:
                leftBound += 1
                leftMax = max(leftMax, height[leftBound])
                # amount of water that can be stored at that index
                res += leftMax - height[leftBound]
            else:
                # Repeat for right bounds
                rightBound -= 1
                rightMax = max(rightMax, height[rightBound])
                res += rightMax - height[rightBound]
        
        return res
