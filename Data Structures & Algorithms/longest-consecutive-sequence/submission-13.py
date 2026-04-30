class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        seen = set(nums)

        for x in nums:
            ch = x
            length = 1
            if ch-1 in seen:
                continue
            else:
                while ch + 1 in seen:
                    length += 1
                    ch = ch+1
                longest = max(longest,length)
        return longest

        #time - O(n)
        #space - O(n)
                
