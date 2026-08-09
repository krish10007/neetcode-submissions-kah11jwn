class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0 # n^0 = n
        for n in nums:
            res = n ^ res
        return res

#time - O(n) and space O(1)
#we could use a hashset but that would lead to O(n) space - like add item to hashset
# and remove from hashset if its already there and at the end return single
#element left in hashset