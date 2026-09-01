class Solution:
    def jump(self, nums: List[int]) -> int:
        from collections import deque
        que = deque([0])
        visited = {0}
        steps = 0
        while que:
            dim = len(que)
            for _ in range(dim):
                curr = que.popleft()
                if curr >= len(nums) - 1:
                    return steps
                for i in range(curr, min(len(nums), curr + nums[curr] + 1)):
                    if i not in visited:
                        que.append(i)
                        visited.add(i)
            steps += 1
        
