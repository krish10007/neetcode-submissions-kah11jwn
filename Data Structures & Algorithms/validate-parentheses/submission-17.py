class Solution:
    def isValid(self, s: str) -> bool:
        mapp = {')':'(', '}':'{', ']':'['}
        stk = []

        for x in s:
            if x not in mapp:
                stk.append(x)
            else:
                if not stk:
                    return False
                else:
                    popped = stk.pop()
                    if popped != mapp[x]:
                        return False
        return not stk

