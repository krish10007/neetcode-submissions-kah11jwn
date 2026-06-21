class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i,cur,total):
            if total == target:
                res.append(cur[:])
                return 
            if i == len(nums) or total > target:
                return
            
            cur.append(nums[i])
            dfs(i,cur,total + nums[i])
            cur.pop()
            dfs(i+1,cur,total)
        
        dfs(0,[],0)
        
        return res
    
# Time complexity is exponential because for each number we either 
# choose it or skip it. The max depth is about target divided by the 
# smallest number, so roughly O(2^(target / min(nums))). 
# Space is O(target / min(nums)) for the recursion stack and current 
# combination, not counting the output.