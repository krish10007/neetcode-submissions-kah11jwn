class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set()
        longest = 0
        sett = set(nums)

        for x in nums:
            if x-1 in sett:
                continue
            char = x
            length = 1
            while char + 1 in sett:
                length += 1
                char = char+1
            longest = max(longest, length)
        return longest

