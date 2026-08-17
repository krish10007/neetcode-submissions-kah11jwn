class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i,sol):
            if sum(sol) == target:
                res.append(sol[:])
                return 
            
            if i == len(nums) or sum(sol) > target:
                return
            
            sol.append(nums[i])
            backtrack(i,sol)

            sol.pop()
            backtrack(i+1, sol)
        
        backtrack(0,[])
        return res