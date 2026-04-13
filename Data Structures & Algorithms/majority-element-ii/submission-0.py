class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        res = []
        for key,val in counts.items():
            if val > len(nums)//3:
                res.append(key)
        return res