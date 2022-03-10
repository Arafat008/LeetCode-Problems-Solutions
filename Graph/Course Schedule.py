class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for i in range(numCourses)]
        visited = [0]*numCourses
        helper = [0]*numCourses
        
        def check_cycle(v):
            visited[v] = 1
            helper[v] = 1
            
            for neighbour in adj_list[v]:
                if not visited[neighbour]:
                    if check_cycle(neighbour):
                        return True
                if helper[neighbour]:
                    return True
            
            helper[v] = 0
            return False
        
        for child,root in prerequisites:
            adj_list[root].append(child)
        
        for i in range(numCourses):
            if not visited[i]:
                if check_cycle(i):
                    return False
        
        return True
