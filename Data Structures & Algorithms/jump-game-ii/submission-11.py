class Solution:
    def jump(self, nums: List[int]) -> int:
        l,r = 0,0
        farthest = 0  #farthest here will work but inside loop is clearer explains a level of bfs
        res = 0

        while r < len(nums)-1:
            for i in range(l,r+1):
                farthest = max(i+nums[i], farthest)
            l = r+1
            r = farthest
            res+=1
        return res
            