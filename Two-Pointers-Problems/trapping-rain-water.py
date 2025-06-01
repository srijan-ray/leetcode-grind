from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        leftBound, rightBound = 0, len(height) - 1
        leftMax, rightMax = height[leftBound], height[rightBound]

        res = 0
        while leftBound < rightBound:
            if leftMax < rightMax:
                leftBound += 1
                leftMax = max(leftMax, height[leftBound])
                res += leftMax - height[leftBound]
            else:
                rightBound -= 1
                rightMax = max(rightMax, height[rightBound])
                res += rightMax - height[rightBound]
        
        return res
