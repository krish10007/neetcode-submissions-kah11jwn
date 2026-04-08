class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            if nums[i]>0:
                break
            l = i+1
            r = len(nums) - 1
            while l < r:
                summ = nums[i] + nums[l] + nums[r]
                if summ == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

                elif summ < 0:
                    l+=1
                else:
                    r-=1
                
        return res
# Time: O(n²)
# Space: O(1) extra space (not counting output)                        
# If interviewer asks about Python specifically,
# sorting may use recursion/internal stack, so some people say:
# O(log n) extra space because of sort

