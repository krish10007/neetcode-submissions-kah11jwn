class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        
        for x in asteroids:
            while stk and stk[-1] >0 and x < 0:
                if stk[-1] > abs(x):
                    x = 0
                elif stk[-1] < abs(x):
                    stk.pop()
                else:
                    stk.pop()
                    x = 0
            if x:
                stk.append(x)
        return stk
