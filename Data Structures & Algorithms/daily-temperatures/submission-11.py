class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []  #temp,index

        for i,t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stk_t,stk_i = stack.pop()
                res[stk_i] = i - stk_i
            stack.append((t,i))
        return res

#Time is O(n) because every index is pushed and popped at most once.
#Space is O(n) because the stack and result array can both grow to size n.