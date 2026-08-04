class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        cursum = 0

        for x in nums:
            cursum += x
            maxsum = max(maxsum,cursum)
            if cursum < 0:
                cursum = 0
        
        return maxsum