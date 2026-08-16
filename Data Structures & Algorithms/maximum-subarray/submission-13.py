class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        cursum = 0

        for n in nums:
            cursum += n
            maxsum = max(maxsum,cursum)
            if cursum < 0:
                cursum = 0
        return maxsum 