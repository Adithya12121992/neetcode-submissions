class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for source, dest in edges:
            graph[source].append(dest)
            graph[dest].append(source)
        seen = set()
        
        def dfs(root, prev):
            if root in seen:
                return False
            seen.add(root)
            for nei in graph[root]:
                if nei == prev:
                    continue
                if not dfs(nei, root):
                    return False
            return True
        return dfs(0, -1) and n == len(seen)