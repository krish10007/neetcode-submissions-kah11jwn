class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        sett = set(nums)
        for i in range(len(nums)):
            if nums[i] - 1 not in sett:
                long = 1
                x = nums[i]
                while x+1 in sett:
                    long += 1
                    x += 1
                longest = max(long,longest)
            continue
        return longest
        
                    
            