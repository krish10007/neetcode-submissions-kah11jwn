class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSpeed = [(p,s) for p,s in zip(position,speed)]
        stk = []
        for p,s in sorted(posSpeed)[::-1]:
            time = (target - p)/s
            if not stk or stk[-1] < time:
                stk.append(time)
        return len(stk)

# Time: O(n log n) because of sorting
# Space: O(n) for stack / pairs
