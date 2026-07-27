class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = []
        posSpeed = [(p,s) for p,s in zip(position,speed)]

        for p,s in sorted(posSpeed)[::-1]:
            time = (target-p)/s
            stk.append(time)
            if len(stk) >= 2 and stk[-1] <= stk[-2]:
                stk.pop()
        return len(stk)