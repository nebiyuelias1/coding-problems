import copy


class Solution:
    def count_connected_graph(self, graph, n):
        visited_nodes = set()
        count = 0
        for i in range(1, n+1):
            if i in visited_nodes:
                continue
            stk = [i]
            while len(stk) > 0:
                current = stk.pop()
                if current in visited_nodes:
                    continue
                visited_nodes.add(current)
                stk = [*stk, *graph[current]]

            count += 1

        return count

    def get_edges(self, m):
        edges = []
        for _ in range(m):
            x, y = input().split(' ')
            x = int(x)
            y = int(y)
            edges.append([x, y])

        return edges

    def build_graph(self, n, m, edges):
        adj_list = {i+1: [] for i in range(n)}

        for i in range(1, m + 1):
            adj_list[edges[i-1][0]].append(edges[i-1][1])
            adj_list[edges[i-1][1]].append(edges[i-1][0])

        return adj_list

    def build_modified_graph(self, edges, graph, l, r):
        for i in range(l-1, r):
            edge = edges[i]
            graph[edge[0]].remove(edge[1])
            graph[edge[1]].remove(edge[0])

        return graph

    def solve_problem(self):
        n, m = input().split(' ')
        n = int(n)
        m = int(m)
        edges = self.get_edges(m)
        graph = self.build_graph(n, m, edges)

        k = int(input())
        for _ in range(k):
            l, r = input().split(' ')
            l = int(l)
            r = int(r)

            import copy
            copy_graph = copy.deepcopy(graph)
            modified_graph = self.build_modified_graph(edges, copy_graph, l, r)
            count = self.count_connected_graph(modified_graph, n)
            print(count)


if __name__ == '__main__':
    sol = Solution()
    sol.solve_problem()
