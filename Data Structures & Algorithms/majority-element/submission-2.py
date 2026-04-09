class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}

        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        
        ans = -1
        maxcount = -1

        for key,val in counts.items():
            if val > maxcount:
                maxcount = val
                ans = key
        return ans

        #TIME - O(n)
        #space - O(n)