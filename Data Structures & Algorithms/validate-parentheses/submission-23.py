class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')':'(', '}':'{', ']':'['}
        stk = []
        for c in s:
            if c not in hashmap:
                stk.append(c)
            else:
                if not stk:
                    return False
                else:
                    popped = stk.pop()
                    if popped != hashmap[c]:
                        return False
        return not stk
#time - O(n), looping through whole array otherwise stack operations are O(1)
#space - O(n),  but stack takes the space n and hashmap is O(1) cause of just 3 entries