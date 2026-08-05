class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for _ in range(len(temperatures))]

        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append([temp, i])
            else:
                while stack and temp > stack[-1][0]:
                    _, j = stack.pop()
                    result[j] = i - j
                stack.append([temp, i])
        
        return result