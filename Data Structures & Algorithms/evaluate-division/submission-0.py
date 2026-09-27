class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for idx, (numerator, denominator) in enumerate(equations):
            graph[numerator].append([denominator, values[idx]])
            graph[denominator].append([numerator, 1/values[idx]])


        # pass source and target
        def bfs(src, target):
            if src not in graph or target not in graph:
                return float(-1)
            q, seen = deque(), set()
            q.append([src, 1])
            seen.add(src)
            while q:
                node, weight = q.popleft()
                if node == target:
                    return weight
                for nei, nei_weight in graph[node]:
                    if nei not in seen:
                        q.append([nei, weight*nei_weight])
                        seen.add(nei)
            return float(-1)            

        return [bfs(eq[0], eq[1]) for eq in queries]
