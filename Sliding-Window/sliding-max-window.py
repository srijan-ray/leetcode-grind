from typing import List
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = nums[0:k]
        res = [] 
        windowHeap: list[tuple[int, int]] = []

        for i in range(0, len(window)):
            heapq.heappush(windowHeap, ( -window[i], i ))

        heapq.heapify(windowHeap)
        res.append(-windowHeap[0][0])

        prev = 0
        for i in range(k, len(nums)):
            if windowHeap[0][0] == -nums[prev]:
                while windowHeap and windowHeap[0][1] < prev + 1:
                    heapq.heappop(windowHeap)

            heapq.heappush(windowHeap, (-nums[i], i))
            prev += 1
            res.append(-windowHeap[0][0])

        return res
