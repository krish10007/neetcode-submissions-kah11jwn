class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSpeed = [(p,s) for p,s in zip(position,speed)]
        stk = []

        for pos, spd in sorted(posSpeed)[::-1]:
            time = (target - pos)/spd
            if not stk or time > stk[-1]:
                stk.append(time)
        return len(stk)

# Time O(n log n), space O(n) where n is number of cars.
# Time: sorting the cars by position is O(n log n), that's the dominant part.
# The loop after is just O(n).
# Space: the paired list + stack both hold up to n in the worst case where
# every car is its own fleet.