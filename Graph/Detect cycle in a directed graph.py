class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        
        visited  = [0]*V
        helper = [0]*V
        
        def dfs(v):
            visited[v] = 1
            helper[v] = 1
            
            for neighbour in adj[v]:
                if not visited[neighbour]:
                    if dfs(neighbour):
                        return True
                
                if helper[neighbour]:
                    return True
                
            
            helper[v] = 0
            return False
        
        for i in range(V):
            if not visited[i]:
                if dfs(i):
                    return True
        
        return False
