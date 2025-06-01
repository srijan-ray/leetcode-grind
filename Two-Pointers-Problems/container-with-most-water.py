from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start, end = 0, len(heights) - 1

        res = 0
        while start < end:
            lower = min(heights[start], heights[end])
            area = lower * (end - start)
            res = max(area, res)

            if heights[start]  <= heights[end]:
                start += 1
            else:
                end -= 1
        return res
