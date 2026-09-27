class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        result = [0] * len(temperatures)

        for i,t in enumerate(temperatures):
            while stk and stk[-1][1] < t:
                index, temp = stk.pop()
                result[index] = i - index
            stk.append((i,t))
        return result 
