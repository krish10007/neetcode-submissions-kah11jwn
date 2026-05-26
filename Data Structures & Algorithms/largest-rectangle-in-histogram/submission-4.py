class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = [] #index, height
        maxarea = 0

        for i, h in enumerate(heights):
            start = i
            while stk and stk[-1][1] > h:
                index, height = stk.pop()
                maxarea = max(maxarea, height * (i - index))
                start = index
            stk.append((start,h))
        
        for i,h in stk:
            maxarea = max(maxarea, h * (len(heights) - i))
        
        return maxarea
