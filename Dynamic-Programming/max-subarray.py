class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxSum = -float('inf')

        for num in nums:
            if currSum + num < 0:
                currSum = 0
            else:
                currSum += num
                maxSum = max(currSum, maxSum)
            
            maxSum = max(maxSum, num)
        
        return maxSum
