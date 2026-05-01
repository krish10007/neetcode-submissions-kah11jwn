class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

# Time complexity is O(n) as Copying elements takes linear time
# Space complexity is O(n) because + operator create a new array of size 2n.