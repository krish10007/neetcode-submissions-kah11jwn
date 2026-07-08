class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        larr = [0] * len(nums)
        rarr = [0] * len(nums)
        l = r = 1

        for i in range(len(nums)):
            j = -i-1
            larr[i] = l
            rarr[j] = r
            l *= nums[i]
            r *= nums[j]
        
        return [l*r for l,r in zip(larr,rarr)]