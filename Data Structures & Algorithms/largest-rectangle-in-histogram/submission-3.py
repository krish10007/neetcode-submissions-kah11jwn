class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = [] # [height,index]
        maxarea = 0

        for i, height in enumerate(heights):
            start = i
            while stk and height < stk[-1][0]:
                h, index = stk.pop()
                maxarea = max(maxarea, h * (i - index))
                start = index
            stk.append([height, start])
        
        for h,i in stk:
            maxarea = max(maxarea, h * (len(heights) - i))
        return maxarea

        #time - O(n)
        #space - O(n)
