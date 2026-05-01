class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        for num,freq in count.items():
            if freq > len(nums)//2:
                return num

# Time — O(n)
# Counter(nums) loops through the array once → O(n)
# count.items() loop → O(n) worst case

# Space — O(n)
# Counter stores every unique element and its frequency
# Worst case every element is unique → n entries → O(n)