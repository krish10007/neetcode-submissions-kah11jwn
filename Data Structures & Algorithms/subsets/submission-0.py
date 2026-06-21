class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset[:]) #or subset.copy()
                return
            
            #include call
            subset.append(nums[i])
            dfs(i+1)

            #not include call
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res