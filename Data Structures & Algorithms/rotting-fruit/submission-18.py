class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid), len(grid[0])
        time,fresh = 0,0
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])
        
        def addorange(row,col):
            nonlocal fresh
            if (row < 0 or row == len(grid) or col < 0 or col == len(grid[0]) or grid[row][col] != 1):
                return    
            grid[row][col] = 2     
            q.append([row,col])
            fresh -= 1

        
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                addorange(r+1,c)
                addorange(r,c-1)
                addorange(r-1,c)
                addorange(r,c+1)

            time += 1 
        
        return time if not fresh else -1



