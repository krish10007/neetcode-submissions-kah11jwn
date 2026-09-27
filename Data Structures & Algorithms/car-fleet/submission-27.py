class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSpeed = [(p,s) for p,s in zip(position,speed)]
        stk = []

        for pos, spd in sorted(posSpeed)[::-1]:
            time = (target - pos)/spd
            if not stk or time > stk[-1]:
                stk.append(time)
        return len(stk)