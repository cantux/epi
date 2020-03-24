    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        N = len(graph)
        colors = [0] * N
        
        for i in range(N):
            if colors[i] != 0:
                continue
            colors[i] = 1
            q = [i]
            while q:
                curr_node = q.pop(0)
                curr_node_color = colors[curr_node]
                next_color = curr_node_color * -1
                for neighbor in graph[curr_node]:
                    if colors[neighbor] == 0:
                        colors[neighbor] = next_color
                        q.append(neighbor)
                    elif colors[neighbor] != next_color:
                        return False
        return True
