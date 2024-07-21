class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        r_order = self.topo_sort(rowConditions, k)
        c_order = self.topo_sort(colConditions, k)
        if not r_order or not c_order:
            return []
        matrix = [[0] * k for _ in range(k)]
        for i in range(k):
            for j in range(k):
                if r_order[i] == c_order[j]:
                    matrix[i][j] = r_order[i]
        return matrix

    def topo_sort(self, edges, n):
        adj = [[] for _ in range(n+1)]
        deg = [0] * (n+1)
        order = []
        for x in edges:
            adj[x[0]].append(x[1])
            deg[x[1]] += 1
        q = deque()
        for i in range(1, n+1):
            if deg[i] == 0:
                q.append(i)
        while q:
            f = q.popleft()
            order.append(f)
            n -= 1
            for v in adj[f]:
                deg[v] -= 1
                if deg[v] == 0:
                    q.append(v)
        if n != 0:
            return []
        return order
