class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        visit = set()

        def dfs(i):
            if i in visit:
                return
            visit.add(i)
            
            for nei in adj[i]:
                dfs(nei)
        
        connected = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                connected += 1
        return connected
