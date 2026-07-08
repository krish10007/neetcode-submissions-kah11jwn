class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupset = set()

        for x in nums:
            if x in dupset:
                return True
            dupset.add(x)
        return False
