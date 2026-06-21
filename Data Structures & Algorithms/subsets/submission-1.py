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

# "Time is O(n × 2ⁿ) if we count the cost of copying each subset,
#  or O(2ⁿ) if we exclude that. Space is O(n × 2ⁿ) for the output, 
#  O(n) auxiliary for the recursion stack and current subset."