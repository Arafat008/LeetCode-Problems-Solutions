from queue import PriorityQueue
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        dist = [float('inf')]*V
        queue = PriorityQueue()
        dist[S] = 0
        queue.put((dist[S],S))
        
        while not queue.empty():
            cost, node = queue.get()
            
            for adj_node,adj_node_cost in adj[node]:
                if adj_node_cost+cost<dist[adj_node]:
                    dist[adj_node] = cost+adj_node_cost
                    queue.put((dist[adj_node],adj_node))
        return dist
