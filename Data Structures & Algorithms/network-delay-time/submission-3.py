class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}

        for source, target, cost in times:
            adj.setdefault(source, []).append((target, cost))

        from collections import deque
        import heapq

        que = [(0, k)]
        seen = set()
        res = 0

        while que:
            time, curr = heapq.heappop(que)
            if curr in seen:
                continue
            seen.add(curr)
            res = max(time, res)
            if curr in adj:
                for target, cost in adj[curr]:
                    if target not in seen:
                        heapq.heappush(que, (time + cost, target))
        if len(seen) == n:
            return res
        return -1

                