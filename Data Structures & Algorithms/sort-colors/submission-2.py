class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #counting sort
        counts = [0,0,0]

        for num in nums:
            counts[num] += 1
        
        R,W,B = counts

        nums[:R] = [0] * R
        nums[R:R+W] = [1] * W
        nums[R+W:] = [2] * B

        #time - O(n*k) but here k is 3 so its O(n)
        #space - O(k) but here here k is 3 so its O(1)