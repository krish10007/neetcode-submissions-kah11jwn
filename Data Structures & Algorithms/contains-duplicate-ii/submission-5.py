class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for j in range(len(nums)):
            if nums[j] in seen and abs(j-seen[nums[j]]) <= k:
                return True
            else:
                seen[nums[j]] = j 
        return False