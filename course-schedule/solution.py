from typing import List


class Solution:
    def traverse(self, vertex, graph, visited, path):
        path.add(vertex)
        
        for neighbor in graph[vertex]:
            if neighbor in path:
                return False
            
            if neighbor not in visited:
                visited.add(neighbor)
                if not self.traverse(neighbor, graph, visited, path):
                    return False
        path.remove(vertex)
        return True
                
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i: [] for i in range(numCourses)}
        for pre in prerequisites:
            adj_list[pre[1]].append(pre[0])
            
        visited = set()
        
        for i in range(numCourses):
            visited.add(i)
            path = set()
            if not self.traverse(i, adj_list, visited, path):
                return False
            
        return True
            
sol = Solution()
print(sol.canFinish(4, [[1,0],[2,0],[3,1],[3,2]]))