class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in '+-*/':
                term2 = stack.pop()
                term1 = stack.pop()

                if token == "+":
                    stack.append(term1 + term2)
                elif token == "-":
                    stack.append(term1 - term2)
                elif token == "*":
                    stack.append(term1 * term2)
                else:
                    stack.append(int(term1 / term2))
            else:
                stack.append(int(token))

        result = stack.pop()
        return result