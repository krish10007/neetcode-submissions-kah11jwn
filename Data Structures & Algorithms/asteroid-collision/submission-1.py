class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        
        for a in asteroids:
            while stk and stk[-1] > 0 and a < 0:
                diff = stk[-1] + a
                if diff > 0:
                    a = 0
                elif diff < 0:
                    stk.pop()
                else:
                    a = 0
                    stk.pop()
            if a:
                stk.append(a)
        return stk 
