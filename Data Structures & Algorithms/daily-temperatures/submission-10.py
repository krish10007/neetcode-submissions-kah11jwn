class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = len(temperatures)
        res = [0] * temps
        stk = []  #temp, index
        for i,t in enumerate(temperatures):
            while stk and stk[-1][0] < temperatures[i]:
                temp, index = stk.pop()
                res[index] = i - index 
            stk.append([t,i])
        return res

#Time is O(n) because every index is pushed and popped at most once.
#Space is O(n) because the stack and result array can both grow to size n.
