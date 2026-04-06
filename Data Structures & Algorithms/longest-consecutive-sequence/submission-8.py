class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        seen = set(nums)
        for x in seen:
            if x-1 not in seen:
                current = x
                length = 1
                while current+1 in seen:
                    current += 1
                    length += 1
                longest = max(length,longest)
                  
        return longest
#time - O(n) as each number gets touched once. like in array [1,2,3,4]
# we only start checking from 1 or start of sequence and not from 2,3,4 
#space - O(n) due to set seen