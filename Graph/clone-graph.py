class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        visited = {}
        
        def dfs(node):
            if node.val in visited:
                return visited[node.val]
            
            clone = Node()
            clone.val = node.val
            visited[clone.val] = clone
            
            for item in node.neighbors:
                clone.neighbors.append(dfs(item))
            
            return clone
            
        return dfs(node)
