class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        in_degree = [0]*numCourses
        queue = []
        result = []
        
        for child,root in prerequisites:
            adj[root].append(child)
        
        for i in range(numCourses):
            for neighbour in adj[i]:
                in_degree[neighbour]+=1
        
        for i in range(numCourses):
            if in_degree[i]==0:
                queue.append(i)
        
        while len(queue):
            node = queue.pop(0)
            result.append(node)
            
            for neighbour in adj[node]:
                in_degree[neighbour]-=1
                if in_degree[neighbour]==0:
                    queue.append(neighbour)
            
        if len(result)==numCourses:
            return result
        else:
            return []
