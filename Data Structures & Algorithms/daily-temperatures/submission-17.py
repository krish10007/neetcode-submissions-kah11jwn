class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = [] # temp,index
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stk and stk[-1][0] < t:
                temp, index = stk.pop()
                res[index] = i - index
            stk.append((t,i))
        return res