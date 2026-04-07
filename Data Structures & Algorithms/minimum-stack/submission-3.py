class MinStack:

    def __init__(self):
        self.stk = []
        self.min_stk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.min_stk:
            self.min_stk.append(val)
        else:
            if val < self.min_stk[-1]:
                self.min_stk.append(val)
            else:
                self.min_stk.append(self.min_stk[-1])

    def pop(self) -> None:
        self.stk.pop()
        self.min_stk.pop()

    def top(self) -> int:
        return self.stk[-1]
        

    def getMin(self) -> int:
        return self.min_stk[-1]
        
# Each operation runs in O(1) time because we only push, pop, or 
# read from the end of the lists.
# Space is O(n) because both the main stack and min stack
# can each store up to n elements.