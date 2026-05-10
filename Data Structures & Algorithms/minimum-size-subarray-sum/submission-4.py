class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minlength = float("inf")
        l = 0
        summ = 0

        for r in range(len(nums)):
            summ += nums[r]
            while summ >= target:
                minlength = min(r-l+1, minlength)
                summ -= nums[l]
                l+=1
        return 0 if minlength == float('inf') else minlength