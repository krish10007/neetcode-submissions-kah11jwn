class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sett = set()
        for x in nums:
            if x not in sett:
                sett.add(x)
            else:
                return True
        return False