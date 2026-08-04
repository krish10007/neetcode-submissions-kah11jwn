class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        cursum = 0

        for x in nums:
            if cursum < 0:
                cursum = 0
            
            cursum += x
            maxsum = max(maxsum,cursum)
        return maxsum