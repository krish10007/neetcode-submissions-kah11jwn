class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in seen:
                x = num 
                length = 1
                while x + 1 in seen:
                    length += 1
                    x += 1
                longest = max(longest, length)
        return longest

            