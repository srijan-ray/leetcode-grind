# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        # if the mid is a bad version, discard mmid - top, focus on start to mid
        # if the mid is not bad, discard start - mid, focus on mid to end

        earliestBad = end
        while start <= end:
            mid = (start + end) // 2
            if isBadVersion(mid):
                earliestBad = mid
                end = mid - 1
            else:
                start = mid + 1
        
        return earliestBad
