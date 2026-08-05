class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_time = []

        for cp, cs in zip(position, speed):
            pos_time.append([cp, (target - cp) / cs])
        
        pos_time = sorted(pos_time, key = lambda x: x[0], reverse = True)

        stack = []

        for cp, ct in pos_time:
            if not stack:
                stack.append(ct)
            elif ct > stack[-1]:
                stack.append(ct)

        return len(stack)