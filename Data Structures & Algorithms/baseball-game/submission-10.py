class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []

        for c in operations:
            if c == '+':
                stk.append(stk[-1] + stk[-2])
                
            elif c == 'D':
                stk.append(2*stk[-1])
            elif c == 'C':
                stk.pop()
            else:
                stk.append(int(c))
        return sum(stk)
