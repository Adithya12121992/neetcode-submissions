class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(set)
        for source, dest in edges:
            graph[source].add(dest)
        
        # the graph[source] musrt satisfy all thesee 3 rules
        # 1. atleast 1 path from source to destoination --> DFS on the graph[source] --> this will be easy to fins out.
        # 2. for all graph[source] there has to be an entry in graph, if not return False 
        # 3. no loops , it has to be finite path.

        # lets implement 2
        seen = set()
        def check_rule2(source1):
            if source1 in seen:
                return False
            seen.add(source1)
            if len(graph[source1]) == 0 and source1!=destination:
                return False
            for nei in graph[source1]:
                if not check_rule2(nei):
                    seen.remove(source1)
                    return False
            seen.remove(source1)
            return True
        return check_rule2(source)
        

        