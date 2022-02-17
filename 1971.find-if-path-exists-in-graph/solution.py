from typing import Dict, List


class Solution:
    def validPathRec(self, adj_list, visited, source, destination) -> bool:
        if source == destination:
            return True
        
        visited[source] = True
        
        for neighbor in adj_list[source]:
            if neighbor not in visited:
                has_path = self.validPathRec(adj_list, visited, neighbor, destination)
                if has_path:
                    return True

        return False

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = {i: [] for i in range(n)}
        visited = {}
        for e in edges:
            adj_list[e[0]].append(e[1])
            adj_list[e[1]].append(e[0])

        return self.validPathRec(adj_list, visited, source, destination)


sol = Solution()
print(sol.validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5))
