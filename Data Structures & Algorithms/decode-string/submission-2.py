class Solution:
    def decodeString(self, s: str) -> str:
        stk = []

        for x in s:
            if x != ']':
                stk.append(x)
            else:
                substr = ""
                while stk and stk[-1] != '[':
                    substr = stk.pop() + substr
                stk.pop()
                k = ''
                while stk and stk[-1].isdigit():
                    k = stk.pop() + k
                stk.append(int(k) * substr)
        return ''.join(stk)
            