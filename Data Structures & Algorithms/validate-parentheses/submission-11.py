class Solution:
    def isValid(self, s: str) -> bool:
        map = {')':'(', ']':'[', '}':'{'}
        stk = []

        for x in s:
            if x not in map:
                stk.append(x)
            else:
                if not stk:
                    return False
                popped = stk.pop()
                if map[x] != popped:
                    return False
        return not stk