class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        def dfs(adj, i, currStack, visited):

            if currStack[i]:
                return True
            
            if visited[i]:
                return False
            
            currStack[i] = True
            visited[i] = True

            for nbr in adj[i]:
                if dfs(adj, nbr, currStack, visited):
                    return True
            currStack[i] = False
        
        adj = [[] for _ in range(numCourses)]
        for [to_, from_] in prerequisites:
            adj[from_].append(to_)
        
        visited = [False] * numCourses
        currStack = [False] * numCourses

        for i in range(numCourses):
            if not visited[i]:
                if dfs(adj, i, currStack, visited):
                    return False
        return True