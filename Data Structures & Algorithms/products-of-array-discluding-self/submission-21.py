class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        larr = [0] * n
        rarr = [0] * n
        l = r = 1

        for i in range(n):
            j = -i-1
            larr[i] = l
            rarr[j] = r
            l *= nums[i]
            r *= nums[j]
        
        return [l*r for l,r in zip(larr,rarr)]

