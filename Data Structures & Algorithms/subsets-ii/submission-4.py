class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()

        def backtrack(i):
            if  i == len(nums):
                res.append(subset[:])
                return
            
            subset.append(nums[i])
            backtrack(i+1)

            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i+=1

            backtrack(i+1)
        
        backtrack(0)
        return res

# Time complexity is O(n * 2^n) because we generate all subsets and copy each subset. 
# Space complexity is O(n) for recursion and the current subset, not counting the
#  output. If counting output, space is O(n * 2^n).